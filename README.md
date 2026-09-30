# claude-obsidian (K4rl-M4rx fork)

> **This is a fork of
> [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian)
> (v2.2.0, merge commit `32ac5a0`) — not the original project.**
> Upstream owns the shared base: the product itself, its installation path,
> and its feature documentation. This fork carries its own increments on top
> of that base, described under
> [What this fork changes](#what-this-fork-changes). The MIT license is
> inherited unchanged ([LICENSE](LICENSE)); lineage is recorded in
> [ATTRIBUTION.md](ATTRIBUTION.md) and every fork change is tracked in
> [CHANGELOG.md](CHANGELOG.md). Upstream stays the `origin` remote and is
> never pushed to; fork work goes to the
> [`fork` remote](https://github.com/K4rl-M4rx/claude-obsidian).

## Why this fork exists

The maintainer runs a real PDE research vault day to day, and this fork is
where improvements validated in that workflow get fed back into the
agent-side Obsidian skill stack. Two kinds of additions land here:
conventions proven against the research workflow itself, and concepts
ported from [nashsu/llm_wiki](https://github.com/nashsu/llm_wiki)
(GPL-3.0) — the purpose-page direction file and the graph-analysis layer.
Ports are concept-only; no code is copied, and both are credited in
[ATTRIBUTION.md](ATTRIBUTION.md).

## What this fork changes

Every addition below is recorded in detail in
[CHANGELOG.md](CHANGELOG.md) under *Unreleased*:

- **`synthesis` and `comparison` page types.** `synthesis` joins the page
  vocabulary as a routable cross-source type, and `comparison` — previously
  valid frontmatter with no filing destination — is now routable. Generic
  mode files them under `wiki/synthesis/` and `wiki/comparisons/` through new
  default-config folder keys, so existing vaults need no migration. See
  `claude_obsidian/page_schema.py` and `WIKI.md`.
- **`wiki-graph` analytics.** `scripts/graph-report.py` (skill:
  `skills/wiki-graph/SKILL.md`) is a read-only, standard-library-only graph
  report: 4-signal page relevance (direct link ×3.0, shared sources ×4.0,
  smoothed Adamic-Adar ×1.5, type affinity ×1.0), deterministic Louvain
  communities with cohesion scores (loose below 0.15), bridge pages
  (articulation points), and knowledge gaps (concept/question pages with no
  inbound link and no `sources:`). The report goes to stdout; nothing is
  written to the vault.
- **Analysis-first ingest.** `skills/wiki-ingest/SKILL.md` formalizes a
  two-step flow: a structured per-source analysis (entities, claims,
  contradictions, cross-source opportunities, proposed page plan) completes
  before any page is drafted, travels in partial worker packets as the
  resumable intermediate, and is shown next to the proposed pages at
  preview. A source already in the source ledger — content hash match with
  at least one linked page — is a proposed skip unless re-analysis is asked
  for.
- **`wiki/purpose.md`.** A user-owned direction page, shipped by `init` as a
  template, that ingest and query read first to bound what counts as worth
  ingesting, synthesizing, and answering. Agents never fill it in unasked;
  changes go through a reviewed transaction at the user's direction.
- **Cascade source removal.** The engine writes create-or-replace only, so
  removing a source's traces is planned as tombstones (`status: deprecated`
  or `archived`), ledger records moved to `rejected`/`superseded`, and
  indexes, ledgers, and the log updated in one reviewed bundle; pages kept
  alive by other sources lose only the dropped reference and its exclusive
  claims. Physical deletion stays a manual user choice. See the
  "Cascade source removal" section of `skills/wiki-lint/SKILL.md`.
- **Research-source page skeleton.** A source page for research/paper
  material follows a fixed seven-section skeleton — 研究背景, 所研究的数学实体,
  新颖点, 主要结果（自然语言）, 精确陈述与方法, 总结, 局限与未决问题 — enforced
  by an orchestrator quality gate with at most one rework; content the
  payload does not state is reported as a gap, never invented. The full
  contract lives in `agents/wiki-ingest.md`.
- **Claim-proposal field contract.** Claim proposals must be field-complete
  at drafting time, and the transaction core rejects the bundle otherwise: a
  UTC `reviewed_at` never after the audit date, `risk` of `normal` or `high`
  only, a `location.anchor` that exists in the target page, and array-shaped
  `evidence`. `accepted` requires a fresh active non-synthetic source, and
  high-risk acceptance two independent sources — distinct `independence_key`
  plus normalized-origin and content-hash merging decides independence. All
  of it is specified in `skills/wiki/references/provenance.md`.
- **Article identifier policy.** A page with `type: source` and
  `source_type: article` must carry a well-formed `doi` or `arxiv_id`, or
  mark the absence with a short `identifier_note` such as `none`; non-article
  sources such as `source_type: manuscript` are exempt. Lint reports
  violations as the `source_identifier_issues` category — a report finding,
  not a checkpoint gate (`claude_obsidian/lint_engine.py`).
- **Frontmatter capture.** The lint frontmatter parser now captures
  top-level inline scalar values, stripping inline comments only outside
  quotes; block-scalar indicators (`|`, `>`, and their variants) capture as
  empty values.

## Attribution & license

MIT, inherited from upstream without modification — see
[LICENSE](LICENSE). [ATTRIBUTION.md](ATTRIBUTION.md) records the lineage:
the upstream project itself (AgriciDaniel / AI Marketing Hub), Andrej
Karpathy's LLM Wiki pattern as the design template, and — for this fork's
purpose-page and graph-analysis additions — a concept-only credit to
nashsu/llm_wiki (GPL-3.0; no code copied).

## The upstream project

Upstream claude-obsidian is a local-first knowledge system for Claude Code
and compatible Agent Skills hosts: it turns captured sources into linked,
source-cited Obsidian pages, answers read-only from vault evidence, and
keeps the vault healthy through linting and reviewed transactions. Its
README is the authoritative documentation for installation, quick start,
the trust and transaction architecture, capability boundaries, and
requirements — none of that is duplicated here; start at
<https://github.com/AgriciDaniel/claude-obsidian> (the shared
[docs/install-guide.md](docs/install-guide.md) in this repository covers
the same ground).

The shared base in this repository — `WIKI.md`, the skills under `skills/`
(invoked namespaced as `/claude-obsidian:<skill>` in Claude Code, with
contracts in each `skills/<name>/SKILL.md`), and the `claude_obsidian/`
Python package — matches upstream at the merge point. This fork's deltas
against that base are exactly the ones listed under
[What this fork changes](#what-this-fork-changes) and in
[CHANGELOG.md](CHANGELOG.md).
