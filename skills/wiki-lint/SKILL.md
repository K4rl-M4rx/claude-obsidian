---
name: wiki-lint
description: "Run a deterministic, read-only health check on an Obsidian wiki. Use for lint, vault health check, audit wiki health, find orphans, find dead links, frontmatter audit, provenance audit, or wiki audit. Reports graph, link, frontmatter, provenance-ledger, empty-section, and stale-index findings; it does not reason broadly or repair files."
---

# Lint the wiki

Use the portable lint engine as the source of truth. Lint observes vault state;
it does not create reports, dashboards, canvases, stubs, or fixes.

Resolve the installed product root from this skill's own location, not from the
vault or current working directory:

```bash
PRODUCT_ROOT=/absolute/path/to/installed/claude-obsidian
CORE="$PRODUCT_ROOT/scripts/claude-obsidian.py"
test -f "$CORE"
```

Every `../wiki/references/` link in this file resolves the same way, relative
to this skill's own directory under `$PRODUCT_ROOT`, never relative to the
selected vault's `wiki/` directory.

## Run

Resolve the user vault, then run one of:

```bash
python3 "$CORE" lint --vault "$VAULT"
python3 "$CORE" lint --vault "$VAULT" --format markdown
python3 "$CORE" lint --vault "$VAULT" --exclude "wiki/scratchpad/*"
```

The repeatable `--exclude GLOB` flag scopes a path (for example a scratchpad
folder) out of page, link-resolution, orphan, frontmatter, empty-section, and
stale-index scanning.

Use `--strict` only when a nonzero exit for findings is useful in automation.
The command remains read-only either way.

The deterministic parser understands Obsidian wikilinks and embeds, Markdown
links, aliases, heading and block fragments, escaped aliases, and code fences.
It skips dot-prefixed directories by default, mirroring Obsidian's own
indexer. Link resolution honors `.gitignore` files inside the vault (no `git`
subprocess): when a link is ambiguous between a page and a gitignored file
such as a build artifact, the gitignored candidate is dropped.
It reports such categories as dead or ambiguous links, orphan pages, required
frontmatter gaps (including `title`), empty sections, stale index entries, and
source/claim ledger contract violations. Report only the
checks and counts present in its output; do not claim that it performed
semantic, stylistic, or prose-level contradiction analysis when it did
not.

## Explain findings

1. Preserve the engine's paths, line numbers, targets, categories, and counts.
2. Group findings by likely impact: broken navigation, ambiguous resolution,
   metadata quality, then maintainability.
3. Explain that an orphan may be intentional and an ambiguous basename needs a
   path-qualified link; do not infer intent from the finding alone.
4. Treat allowlisted findings as policy, not as proof that the target exists.
5. Separate deterministic facts from suggested remediation.

Do not write the Markdown rendering into the vault. Return it in chat or stdout.

## Repair is a separate operation

Never auto-fix a lint result. After the user chooses specific findings to
repair:

1. Re-read each target and record its expected SHA-256.
2. Draft only the selected changes; do not delete or merge pages without
   explicit consent.
3. Build one repair bundle with a new operation ID.
4. Inspect the bundle and show exact changed paths.
5. Apply only after that separate review.
6. Re-run lint read-only and compare the relevant findings.

Follow the [operation transaction contract](../wiki/references/operation-transactions.md).
Lint itself never applies that transaction and never commits Git.

### Cascade source removal

When the user asks to remove a source's traces from the vault, plan the
cascade before writing anything. The engine writes create-or-replace only, so
"removal" of a canonical page is a tombstone (`status: deprecated` or
`archived`), never a file deletion; `.raw/` captures and the ingestion
manifest stay untouched by this workflow.

1. Enumerate everything tied to the source: the source's summary page, pages
   listing it in `sources:` (and in `related:`, `first_mentioned:`, or
   `subjects:`), claim-ledger records citing it, and index/MOC entries
   pointing at any of them.
2. A page supported by other sources keeps existing. Replace it without the
   dropped source reference and its exclusive prose, clearing or re-pointing
   the `location.anchor` of claims whose anchored text the change removes.
   Mark the source's ledger
   record `rejected` or `superseded` rather than deleting it, and mark claims
   exclusive to that source `deprecated` (or `unsupported` where no data
   backs them). Remove any wikilinks or embeds the change strands.
3. A page supported only by the removed source becomes a tombstone proposal:
   `status: deprecated` (or `archived`) in the same bundle, with its claims
   reassessed. Physical file deletion is the user's manual choice outside the
   transaction system, followed by a fresh lint.
4. Update index/MOC entries, `wiki/overview.md`, `wiki/hot.md`, both ledgers,
   and the log in that one bundle so navigation and provenance stay
   consistent.
5. Re-run lint after the repair and report the remaining findings.

## Checkpoint

Observe the deterministic report, think about root causes rather than finding
count, verify proposed repairs against current hashes, and grow by improving the
workflow that produced repeated findings.
