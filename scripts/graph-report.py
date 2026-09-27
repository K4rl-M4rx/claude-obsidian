#!/usr/bin/env python3
"""graph-report.py — read-only graph analytics over a claude-obsidian vault.

Adapts the graph-analysis layer of the LLM Wiki pattern (4-signal relevance,
community detection, insight report) as a stdlib-only, deterministic, read-only
reporter. It never writes to the vault: the report goes to stdout, and any
decision taken from it (new pages, deep research) flows through the normal
transactional skills.

Signals per unordered page pair (llm_wiki weights, indicator-scaled):

  direct link      ×3.0   either page links to the other
  shared sources   ×4.0   both pages cite ≥1 common source in `sources:`
  smoothed Adamic-Adar ×1.5   common-neighbour measure on the link graph,
                          normalised: 1.5 × min(aa, 2) / 2
  type affinity    ×1.0   both pages have the same non-empty `type:`

Communities use Louvain modularity optimisation on the link graph,
deterministic: nodes iterate in sorted-path order, ties break toward the
community with the smallest smallest-member. Cohesion is internal edge weight
over total incident edge weight; communities below 0.15 are flagged loose and
pages of degree ≤ 1 are listed as isolated.

Insights: bridge pages (articulation points — removing one disconnects the
link graph), unsupported pages (concept/question with no inbound link and no
`sources:` entries), and dangling-link counts.

Exit codes: 0 success, 2 usage or vault error.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
PLUGIN_ROOT = Path(__file__).resolve().parent.parent
if str(PLUGIN_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_ROOT))

from claude_obsidian.paths import VaultSelectionError, resolve_vault_root  # noqa: E402

WIKILINK_BODY_RE = re.compile(r"\[\[([^\]\r\n]+?)\]\]")
FENCE_RE = re.compile(r"^[ ]{0,3}(```+|~~~+)(.*)$")
INLINE_CODE_RE = re.compile(r"`[^`\r\n]*`")
FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)

SIGNAL_DIRECT = 3.0
SIGNAL_OVERLAP = 4.0
SIGNAL_ADAMIC = 1.5
SIGNAL_AFFINITY = 1.0
ADAMIC_CAP = 2.0
LOOSE_COHESION = 0.15
SUPPORTED_TYPES = {"concept", "question"}
EXCLUDED_DIRS = {"meta", "folds"}


def _mask_code(text: str) -> str:
    """Mask inline code and whole fenced blocks, line-paired like lint_engine.

    A fence opens on a line with 0-3 leading spaces followed by ``` or ~~~
    (with info string), and closes on the next line whose fence marker is the
    same character and at least as long. Everything inside is masked.
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    fence: str | None = None
    for line in lines:
        if fence is None:
            open_match = FENCE_RE.match(line.rstrip("\r\n"))
            if open_match:
                fence = open_match.group(1)[0] * len(open_match.group(1))
                out.append("\n" * line.count("\n"))
                continue
            out.append(INLINE_CODE_RE.sub("", line))
        else:
            close = FENCE_RE.match(line.rstrip("\r\n"))
            if (
                close
                and close.group(1)[0] == fence[0]
                and len(close.group(1)) >= len(fence)
                and not close.group(2).strip()
            ):
                fence = None
            out.append("\n" * line.count("\n"))
    return "".join(out)


def _normalise_target(target: str) -> str:
    target = target.strip()
    if target.endswith(".md"):
        target = target[: -len(".md")]
    target = target.rsplit("/", 1)[-1]
    return unicodedata.normalize("NFC", target).casefold()


def parse_page(path: Path, relative: str) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        text = ""
    text = text.lstrip("\ufeff")
    fm_match = FRONTMATTER_RE.match(text)
    frontmatter = fm_match.group(1) if fm_match else ""
    body = text[fm_match.end():] if fm_match else text

    type_match = re.search(r"(?m)^type:\s*\"?([A-Za-z0-9_-]+)\"?\s*$", frontmatter)
    status_match = re.search(r"(?m)^status:\s*\"?([A-Za-z0-9_-]+)\"?\s*$", frontmatter)
    sources = _parse_sources(frontmatter)

    masked = _mask_code(body)
    targets = []
    for match in WIKILINK_BODY_RE.finditer(masked):
        body_target = match.group(1).split("|")[0].split("#")[0]
        targets.append(_normalise_target(body_target))
    return {
        "path": relative,
        "basename": unicodedata.normalize(
            "NFC", relative.rsplit("/", 1)[-1][: -len(".md")]
        ).casefold(),
        "type": type_match.group(1).casefold() if type_match else "",
        "status": status_match.group(1).casefold() if status_match else "",
        "sources": sources,
        "outbound": targets,
    }


def _parse_sources(frontmatter: str) -> set[str]:
    sources: set[str] = set()
    in_sources = False
    for line in frontmatter.splitlines():
        if re.match(r"^\S", line):
            in_sources = line.strip().rstrip(":").casefold() == "sources"
            continue
        if not in_sources:
            continue
        for match in re.finditer(r"\[\[([^\]\r\n]+?)\]\]", line):
            sources.add(_normalise_target(match.group(1).split("|")[0].split("#")[0]))
    return sources


def collect_pages(vault: Path) -> dict[str, dict]:
    wiki = vault / "wiki"
    pages: dict[str, dict] = {}
    for path in sorted(wiki.rglob("*.md")):
        relative = path.relative_to(vault).as_posix()
        parts = relative.split("/")
        if len(parts) > 2 and parts[1] in EXCLUDED_DIRS:
            continue
        pages[relative] = parse_page(path, relative)
    return pages


def build_graph(
    pages: dict[str, dict],
) -> tuple[dict[str, set[str]], dict[str, int], dict[str, set[str]], int]:
    """Return (undirected neighbours, degree, resolved inbound, dangling count).

    Outbound targets that resolve to a non-page file (.canvas/.base) are
    skipped rather than counted dangling — the graph covers wiki pages only.
    """
    by_basename: dict[str, list[str]] = defaultdict(list)
    for relative, page in pages.items():
        by_basename[page["basename"]].append(relative)

    neighbours: dict[str, set[str]] = {relative: set() for relative in pages}
    inbound: dict[str, set[str]] = {relative: set() for relative in pages}
    dangling = 0
    for relative, page in pages.items():
        for target in page["outbound"]:
            if target.endswith((".canvas", ".base")):
                continue
            candidates = by_basename.get(target, [])
            if len(candidates) == 1 and candidates[0] != relative:
                neighbours[relative].add(candidates[0])
                neighbours[candidates[0]].add(relative)
                inbound[candidates[0]].add(relative)
            elif not candidates:
                dangling += 1
    return neighbours, {r: len(n) for r, n in neighbours.items()}, inbound, dangling


def adamic_adar(neighbours: dict[str, set[str]], degree: dict[str, int], a: str, b: str) -> float:
    """Smoothed Adamic-Adar: 1/log1p(deg) per common neighbour."""
    common = neighbours[a] & neighbours[b]
    return sum(1.0 / math.log1p(degree[n]) for n in common)


def pair_relevance(pages: dict[str, dict], neighbours: dict[str, set[str]], degree: dict[str, int]) -> list[dict]:
    ordered = sorted(pages)
    rows: list[dict] = []
    for i, a in enumerate(ordered):
        page_a = pages[a]
        for b in ordered[i + 1:]:
            page_b = pages[b]
            linked = b in neighbours[a]
            shared = page_a["sources"] & page_b["sources"]
            if not linked and not shared:
                continue
            relevance = 0.0
            signals: list[str] = []
            if linked:
                relevance += SIGNAL_DIRECT
                signals.append("direct")
            if shared:
                relevance += SIGNAL_OVERLAP
                signals.append("sources")
            aa = adamic_adar(neighbours, degree, a, b)
            if aa > 0:
                relevance += SIGNAL_ADAMIC * min(aa, ADAMIC_CAP) / ADAMIC_CAP
                signals.append("adamic-adar")
            if page_a["type"] and page_a["type"] == page_b["type"]:
                relevance += SIGNAL_AFFINITY
                signals.append("type")
            rows.append({"a": a, "b": b, "relevance": round(relevance, 3), "signals": signals})
    rows.sort(key=lambda row: (-row["relevance"], row["a"], row["b"]))
    return rows


def louvain(neighbours: dict[str, set[str]]) -> dict[str, int]:
    """Deterministic Louvain on the undirected link graph.

    Conventions: adjacency is symmetric (each undirected edge stored once per
    direction); self-loops carry internal weight counted once but add it twice
    to the node degree, the standard undirected treatment. Nodes iterate in
    sorted order; the ranking `links_in(c) - total(c)*k_i/(2m)` is
    proportional to the true modularity gain for a fixed moving node, and ties
    break toward the smaller community id, so output is deterministic.
    """
    adjacency: dict[str, dict[str, float]] = {node: {} for node in sorted(neighbours)}
    for node in sorted(neighbours):
        for other in neighbours[node]:
            adjacency[node][other] = 1.0
    selfloop: dict[str, float] = {node: 0.0 for node in adjacency}
    owner: dict[str, list[str]] = {node: [node] for node in adjacency}

    for _level in range(12):
        degree = {
            node: sum(links.values()) + selfloop[node] for node, links in adjacency.items()
        }
        m = sum(degree.values()) / 2.0
        if m <= 0:
            break
        community: dict[str, int] = {}
        for node in sorted(adjacency):
            community[node] = len(community)

        for _pass in range(len(adjacency)):
            community_total: dict[int, float] = defaultdict(float)
            for node, comm in community.items():
                community_total[comm] += degree[node]
            moved = False
            for node in sorted(adjacency):
                current = community[node]
                community_total[current] -= degree[node]
                links_in: dict[int, float] = defaultdict(float)
                for other, weight in adjacency[node].items():
                    if other != node:
                        links_in[community[other]] += weight
                best = current
                best_gain = (
                    links_in.get(current, 0.0)
                    - community_total[current] * degree[node] / (2.0 * m)
                )
                for candidate in sorted(links_in):
                    if candidate == current:
                        continue
                    gain = (
                        links_in[candidate]
                        - community_total[candidate] * degree[node] / (2.0 * m)
                    )
                    if gain > best_gain + 1e-9:
                        best_gain = gain
                        best = candidate
                community[node] = best
                community_total[best] += degree[node]
                if best != current:
                    moved = True
            if not moved:
                break

        groups: dict[int, list[str]] = defaultdict(list)
        for node in sorted(adjacency):
            groups[community[node]].append(node)
        if len(groups) == len(adjacency):
            break

        remap = {old: new for new, old in enumerate(sorted(groups))}
        new_adjacency: dict[str, dict[str, float]] = {
            remap[comm]: {} for comm in sorted(groups)
        }
        new_selfloop: dict[str, float] = defaultdict(float)
        for node in sorted(adjacency):
            target = remap[community[node]]
            new_selfloop[target] += selfloop[node]
            for other, weight in adjacency[node].items():
                if other == node:
                    continue
                target_other = remap[community[other]]
                if target_other == target:
                    new_selfloop[target] += weight / 2.0
                else:
                    new_adjacency[target][target_other] = (
                        new_adjacency[target].get(target_other, 0.0) + weight
                    )
        new_owner: dict[str, list[str]] = {}
        for old in sorted(groups):
            target = remap[old]
            for node in groups[old]:
                for orig in owner[node]:
                    new_owner.setdefault(target, []).append(orig)
        adjacency = {
            node: {**dict(links), node: new_selfloop[node]} for node, links in new_adjacency.items()
        }
        selfloop = dict(new_selfloop)
        owner = new_owner

    labels: dict[str, str] = {}
    for node in sorted(owner):
        for orig in owner[node]:
            labels[orig] = node
    relabel: dict[str, int] = {}
    for node in sorted(labels):
        relabel.setdefault(labels[node], len(relabel))
    return {orig: relabel[aggregate] for orig, aggregate in labels.items()}


def community_stats(
    pages: dict[str, dict], neighbours: dict[str, set[str]], community: dict[str, int]
) -> tuple[dict[int, dict], list[dict]]:
    members: dict[int, list[str]] = defaultdict(list)
    for node in sorted(community):
        members[community[node]].append(node)

    stats: dict[int, dict] = {}
    for comm in sorted(members):
        internal = 0.0
        boundary = 0.0
        for node in members[comm]:
            for other in neighbours[node]:
                if community[other] == comm:
                    internal += 1.0
                else:
                    boundary += 1.0
        internal /= 2.0
        total = 2.0 * internal + boundary
        cohesion = internal / total if total else 1.0
        stats[comm] = {
            "members": members[comm],
            "cohesion": round(cohesion, 3),
            "loose": bool(total) and cohesion < LOOSE_COHESION,
        }

    bridges = [
        {"path": node, "communities": sorted({community[other] for other in neighbours[node]})}
        for node in _articulation_points(neighbours)
    ]
    return stats, bridges


def _articulation_points(neighbours: dict[str, set[str]]) -> list[str]:
    """Iterative Tarjan low-link articulation points, sorted output.

    A bridge page is one whose removal disconnects the link graph — the
    graph-theoretic notion behind llm_wiki's "bridging nodes" insight.
    """
    disc: dict[str, int] = {}
    low: dict[str, int] = {}
    parent: dict[str, str | None] = {}
    points: set[str] = set()
    counter = 0
    for root in sorted(neighbours):
        if root in disc:
            continue
        parent[root] = None
        disc[root] = low[root] = counter
        counter += 1
        root_children = 0
        stack = [(root, iter(sorted(neighbours[root])))]
        while stack:
            node, edges = stack[-1]
            advanced = False
            for other in edges:
                if other not in disc:
                    parent[other] = node
                    disc[other] = low[other] = counter
                    counter += 1
                    if node == root:
                        root_children += 1
                    stack.append((other, iter(sorted(neighbours[other]))))
                    advanced = True
                    break
                elif other != parent[node]:
                    low[node] = min(low[node], disc[other])
            if advanced:
                continue
            stack.pop()
            if stack:
                back = stack[-1][0]
                low[back] = min(low[back], low[node])
                if back != root and low[node] >= disc[back]:
                    points.add(back)
        if root_children >= 2:
            points.add(root)
    return sorted(points)


def find_gaps(
    pages: dict[str, dict], inbound: dict[str, set[str]]
) -> list[str]:
    """Concept/question pages with no INBOUND link and no `sources:` entries."""
    gaps = []
    for relative in sorted(pages):
        page = pages[relative]
        if page["type"] in SUPPORTED_TYPES and not inbound[relative] and not page["sources"]:
            gaps.append(relative)
    return gaps


def render_markdown(
    pages: dict[str, dict],
    degree: dict[str, int],
    dangling: int,
    rows: list[dict],
    stats: dict[int, dict],
    bridges: list[dict],
    gaps: list[str],
    top: int,
) -> str:
    lines = ["# Vault Graph Report", "", "Read-only analysis; generated by `scripts/graph-report.py`.", ""]
    lines += [
        "## Overview",
        "",
        f"- pages analysed: {len(pages)}",
        f"- dangling links: {dangling}",
        f"- communities: {len(stats)}",
        f"- bridges: {len(bridges)}",
        f"- unsupported pages: {len(gaps)}",
        "",
    ]
    lines += ["## Strongest page pairs", "", "| relevance | pair | signals |", "|---|---|---|"]
    for row in rows[:top]:
        lines.append(f"| {row['relevance']} | {row['a']} ↔ {row['b']} | {', '.join(row['signals'])} |")
    lines += ["", "## Communities", ""]
    for comm, info in sorted(stats.items()):
        flag = " (loose)" if info["loose"] else ""
        lines.append(f"### Community {comm}{flag} — cohesion {info['cohesion']}")
        lines.append("")
        for member in info["members"]:
            marker = " (isolated)" if degree[member] <= 1 else ""
            lines.append(f"- {member}{marker}")
        lines.append("")
    lines += ["## Bridges", ""]
    lines += [f"- {item['path']} (links communities {', '.join(map(str, item['communities']))})" for item in bridges] or ["- none."]
    lines += ["", "## Unsupported pages", ""]
    lines += [f"- {item}" for item in gaps] or ["- none."]
    lines.append("")
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Read-only wiki graph analytics report.")
    parser.add_argument("--vault", help="Explicit vault root")
    parser.add_argument("--top", type=int, default=20, help="Page pairs to list")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of markdown")
    args = parser.parse_args(argv)

    try:
        selection = resolve_vault_root(args.vault, start=Path.cwd(), plugin_root=PLUGIN_ROOT)
    except VaultSelectionError as exc:
        print(f"ERR {exc.code}: {exc}", file=sys.stderr)
        return 2
    vault = selection.root
    if not (vault / "wiki").is_dir():
        print("ERR VAULT_WIKI_MISSING: vault has no wiki/ directory", file=sys.stderr)
        return 2

    pages = collect_pages(vault)
    neighbours, degree, inbound, dangling = build_graph(pages)
    rows = pair_relevance(pages, neighbours, degree)
    community = louvain(neighbours)
    stats, bridges = community_stats(pages, neighbours, community)
    gaps = find_gaps(pages, inbound)
    top = max(0, args.top)

    if args.json:
        print(json.dumps({
            "pages": len(pages),
            "dangling_links": dangling,
            "relevance": rows[:top],
            "communities": [
                {"id": comm, "cohesion": info["cohesion"], "loose": info["loose"], "members": info["members"]}
                for comm, info in sorted(stats.items())
            ],
            "bridges": bridges,
            "unsupported": gaps,
        }, indent=2, sort_keys=True))
    else:
        print(render_markdown(pages, degree, dangling, rows, stats, bridges, gaps, top), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
