# Evidence and provenance

Keep ingestion state, source evidence, and claim assessment separate.

Resolve the installed product root from the invoking skill's own location, not
from the user-vault working directory:

```bash
PRODUCT_ROOT=/absolute/path/to/installed/claude-obsidian
CORE="$PRODUCT_ROOT/scripts/claude-obsidian.py"
test -f "$CORE"
```

## Ledgers

- `.raw/.manifest.json`: legacy-compatible ingestion hashes, generated pages,
  address map, and last processing result.
- `wiki/meta/ledgers/source-ledger.json`: stable source identities, authority,
  SHA-256, retrieval/freshness, review state, and linked pages.
- `wiki/meta/ledgers/claim-ledger.json`: falsifiable claims, note locations,
  support, contradictions, confidence, risk, and review state.

Do not overload one ledger with all three jobs.

## Source rules

- Use SHA-256 for new source identity and delta checks.
- File locators are vault-relative. Remote locators are absolute HTTPS URLs.
- Source authority is one of `official`, `primary`, `secondary`, `community`,
  `synthetic`, or `unknown`.
- Review state is `unreviewed`, `active`, `superseded`, or `rejected`.
- Compute staleness from `refresh_due`; do not store a second stale flag.
- Sources sharing an `independence_key` do not count as independent
  corroboration.
- Sources that resolve to the same canonical URL origin do not count as
  independent merely because IPv6, IDN, Unicode, dot-segment, default-port, or
  percent-encoding spelling differs. Escaped reserved path/query bytes remain
  distinct because they can identify a different resource.

## Claim rules

- Assessment is `accepted`, `provisional`, `contested`, `unsupported`, or
  `deprecated`.
- Accepted claims need at least one fresh, active, non-synthetic source.
- High-risk accepted claims need two independent sources.
- Preserve contradictory evidence. Do not silently select a winner.
- `unsupported` is the canonical no-data state. A grounded refusal is better
  than confident invention.
- Never fabricate quotations, page numbers, dates, or evidence locators.

## Claim proposal field requirements

The transaction core validates the claim ledger mechanically; a proposal that
violates any of these fails the whole bundle. Check them before drafting:

- `reviewed_at`: an ISO date; required for `accepted`; never after the audit
  date (UTC — a local calendar date can sit ahead of it), and never earlier
  than the supporting source's `retrieved_at`/`ingested_at`.
- `risk`: `normal` or `high` only. There is no `low`.
- `location`: `{path, anchor}` where the anchor is a heading or block that
  exists in that page — validated against the prospective content when the
  same bundle replaces the page.
- `evidence`: an array of `{source_id, relation, locator}` objects; a bare
  object or a string fails.
- `accepted` requires at least one fresh active supporting source (additional
  stale or inactive supporting sources do not block acceptance): the source
  must be `review_status: active`, non-synthetic, not stale by `refresh_due`,
  and dated no later than the claim's `reviewed_at`.
- High-risk `accepted` claims additionally need two independent sources:
  distinct `independence_key` is necessary but not sufficient — the engine
  also merges supporting sources that share a normalized origin or an
  identical content hash.

## Migration

Run migration as a dry-run first:

```bash
python3 "$CORE" migrate --vault VAULT \
  --generated-at <ISO-UTC> --operation-id migrate-reviewed
python3 "$CORE" migrate --vault VAULT \
  --generated-at <ISO-UTC> --operation-id migrate-reviewed \
  --approved-plan-sha256 <reviewed-sha256> --apply
```

Migration leaves `.raw/.manifest.json` byte-for-byte unchanged, creates missing
ledgers, defaults unknown evidence fields honestly, and never extracts claims
from legacy prose automatically. A legacy source key that resolves to a regular
file remains a file source with its computed SHA-256. A valid key with no file
is preserved as an unreviewed manual source with unknown authority and no
verified payload hash. This unresolved record preserves the legacy identity,
date, and page links; it does not prove a batch-to-file relationship. Migration
never enumerates raw payloads to invent that relationship or promotes the
legacy short hash to SHA-256.
The reviewed migration bundle also pins each legacy locator's observed file
state. Apply fails if an unresolved label appears, becomes unsafe, cannot be
inspected, or if a file source changes after review.
