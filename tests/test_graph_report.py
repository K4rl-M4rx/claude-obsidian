#!/usr/bin/env python3
"""Deterministic graph analytics tests: relevance, communities, bridges, gaps."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "graph_report", ROOT / "scripts" / "graph-report.py"
)
gr = importlib.util.module_from_spec(_spec)
sys.modules["graph_report"] = gr
_spec.loader.exec_module(gr)

GRAPH = ROOT / "scripts" / "graph-report.py"


def _page(title: str, ptype: str, status: str, sources: list[str], links: list[str]) -> str:
    lines = [
        "---",
        f"title: {title}",
        f"type: {ptype}",
        f"status: {status}",
        "created: 2026-09-28",
        "updated: 2026-09-28",
        "tags:",
        f"  - {ptype}",
    ]
    if sources:
        lines.append("sources:")
        lines += [f'  - "[[{item}]]"' for item in sources]
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    for link in links:
        lines.append(f"- link to [[{link}]].")
    lines.append("")
    return "\n".join(lines)


def _build_vault(root: Path) -> None:
    """Two source-backed cliques (energy, geometry) joined by a bridge page,
    plus one unsupported question, one dangling link, fenced-code ghost links,
    an alias link, an NFD-encoded unicode link, and an outbound-only concept."""
    (root / ".obsidian").mkdir(parents=True)
    concepts = root / "wiki" / "concepts"
    questions = root / "wiki" / "questions"
    sources = root / "wiki" / "sources"
    concepts.mkdir(parents=True)
    questions.mkdir()
    sources.mkdir()

    (sources / "Evans PDE.md").write_text(
        _page("Evans PDE", "source", "active", [], []), encoding="utf-8"
    )
    (sources / "GT Book.md").write_text(
        _page("GT Book", "source", "active", [], []), encoding="utf-8"
    )
    (concepts / "Energy Methods.md").write_text(
        _page("Energy Methods", "concept", "developing", ["Evans PDE"],
              ["Sobolev Embedding|the embedding page"]),
        encoding="utf-8",
    )
    (concepts / "Sobolev Embedding.md").write_text(
        _page("Sobolev Embedding", "concept", "developing", ["Evans PDE"],
              ["Energy Methods"]),
        encoding="utf-8",
    )
    (concepts / "Curvature Estimates.md").write_text(
        _page("Curvature Estimates", "concept", "developing", ["GT Book"], ["Comparison Bridge"]),
        encoding="utf-8",
    )
    (concepts / "Comparison Bridge.md").write_text(
        _page("Comparison Bridge", "concept", "developing", ["Evans PDE", "GT Book"],
              ["Sobolev Embedding", "Curvature Estimates",
               unicodedata.normalize("NFD", "Café Page")]),
        encoding="utf-8",
    )
    (concepts / "Café Page.md").write_text(
        _page("Café Page", "concept", "seed", ["Evans PDE"], []), encoding="utf-8"
    )
    (questions / "Open Regularity Question.md").write_text(
        _page("Open Regularity Question", "question", "provisional", [], []),
        encoding="utf-8",
    )
    (concepts / "Outbound Only.md").write_text(
        _page("Outbound Only", "concept", "seed", [], ["Energy Methods"]),
        encoding="utf-8",
    )
    (concepts / "Dangling Notes.md").write_text(
        _page("Dangling Notes", "concept", "seed", ["Evans PDE"], ["Nonexistent Page"])
        + "\n```python\nlink = '[[Ghost In Fence]]'\n```\n\n"
        "Inline `[[Ghost Inline]]` stays inert.\n\n"
        "~~~\n[[Ghost In Tilde]]\n~~~\n",
        encoding="utf-8",
    )


class GraphReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.vault = Path(cls._tmp.name) / "vault"
        _build_vault(cls.vault)
        cls.pages = gr.collect_pages(cls.vault)
        cls.neighbours, cls.degree, cls.inbound, cls.dangling = gr.build_graph(cls.pages)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def test_links_resolve_and_code_spans_are_ignored(self) -> None:
        # Exactly one dangling link: "Nonexistent Page". The fenced and inline
        # ghost wikilinks inside "Dangling Notes" must not count.
        self.assertEqual(self.dangling, 1)
        sobolev = "wiki/concepts/Sobolev Embedding.md"
        energy = "wiki/concepts/Energy Methods.md"
        self.assertIn(sobolev, self.neighbours[energy])
        # The alias form [[Sobolev Embedding|the embedding page]] resolved.
        self.assertIn(energy, self.neighbours[sobolev])
        # The NFD-encoded unicode target resolved to the NFC-named file.
        cafe = unicodedata.normalize("NFC", "wiki/concepts/Café Page.md")
        self.assertIn(cafe, self.neighbours["wiki/concepts/Comparison Bridge.md"])

    def test_gaps_flag_unsupported_questions(self) -> None:
        gaps = gr.find_gaps(self.pages, self.inbound)
        self.assertEqual(
            gaps,
            ["wiki/concepts/Outbound Only.md", "wiki/questions/Open Regularity Question.md"],
        )

    def test_relevance_weights(self) -> None:
        rows = gr.pair_relevance(self.pages, self.neighbours, self.degree)
        by_pair = {(row["a"], row["b"]): row for row in rows}
        energy = "wiki/concepts/Energy Methods.md"
        sobolev = "wiki/concepts/Sobolev Embedding.md"
        # direct link (3) + shared source (4) + type affinity (1) = 8.0;
        # adamic-adar is 0 (no common neighbour)
        self.assertAlmostEqual(by_pair[(energy, sobolev)]["relevance"], 8.0)
        self.assertEqual(
            by_pair[(energy, sobolev)]["signals"], ["direct", "sources", "type"]
        )
        # bridge pair shares one source and links: 3 + 4 + 1 = 8.0
        bridge = "wiki/concepts/Comparison Bridge.md"
        curvature = "wiki/concepts/Curvature Estimates.md"
        self.assertAlmostEqual(by_pair[(bridge, curvature)]["relevance"], 8.0)
        # rows are sorted by descending relevance, then path
        relevances = [row["relevance"] for row in rows]
        self.assertEqual(relevances, sorted(relevances, reverse=True))

    def test_louvain_splits_cliques_and_joins_bridges(self) -> None:
        community = gr.louvain(self.neighbours)
        energy = "wiki/concepts/Energy Methods.md"
        sobolev = "wiki/concepts/Sobolev Embedding.md"
        curvature = "wiki/concepts/Curvature Estimates.md"
        bridge = "wiki/concepts/Comparison Bridge.md"
        self.assertEqual(community[energy], community[sobolev])
        self.assertEqual(community[curvature], community[bridge])
        self.assertNotEqual(community[energy], community[curvature])

    def test_bridges_are_articulation_points(self) -> None:
        # Removing "Comparison Bridge" disconnects the geometry clique;
        # removing "Sobolev Embedding" strands "Energy Methods"; removing
        # "Energy Methods" strands the outbound-only leaf. All three are
        # articulation points. "Outbound Only" itself is a leaf, and a leaf
        # dropping off is not a split.
        self.assertEqual(
            gr._articulation_points(self.neighbours),
            [
                "wiki/concepts/Comparison Bridge.md",
                "wiki/concepts/Energy Methods.md",
                "wiki/concepts/Sobolev Embedding.md",
            ],
        )
        stats, bridges = gr.community_stats(self.pages, self.neighbours, gr.louvain(self.neighbours))
        self.assertEqual(
            [item["path"] for item in bridges],
            [
                "wiki/concepts/Comparison Bridge.md",
                "wiki/concepts/Energy Methods.md",
                "wiki/concepts/Sobolev Embedding.md",
            ],
        )

    def test_cli_markdown_and_json_are_deterministic(self) -> None:
        done = subprocess.run(
            [sys.executable, str(GRAPH), "--vault", str(self.vault), "--json"],
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(done.returncode, 0, done.stderr)
        document = json.loads(done.stdout)
        self.assertEqual(
            document["unsupported"],
            ["wiki/concepts/Outbound Only.md", "wiki/questions/Open Regularity Question.md"],
        )
        self.assertEqual(document["dangling_links"], 1)

        first = subprocess.run(
            [sys.executable, str(GRAPH), "--vault", str(self.vault)],
            capture_output=True, text=True, timeout=30,
        )
        second = subprocess.run(
            [sys.executable, str(GRAPH), "--vault", str(self.vault)],
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn("# Vault Graph Report", first.stdout)
        self.assertIn("## Bridges", first.stdout)

    def test_missing_wiki_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            vault = Path(td) / "empty"
            (vault / ".obsidian").mkdir(parents=True)
            done = subprocess.run(
                [sys.executable, str(GRAPH), "--vault", str(vault)],
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(done.returncode, 2)
            self.assertIn("VAULT_WIKI_MISSING", done.stderr)


def main() -> None:
    print("=== test_graph_report.py ===")
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(GraphReportTests)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    print("\nAll graph-report tests passed.")


if __name__ == "__main__":
    main()
