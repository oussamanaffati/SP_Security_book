# Draft v2 status

**As of:** 17 November 2026

**Editorial status:** Expanded six-chapter manuscript for author review. Not publication-ready.

**Git status:** The current revision is prepared locally from baseline `e1abb9ad68e1d396a8d16b3712e1cb1f9409f82c`. Local `main` and the live `origin/main` matched that baseline at the last read. Commit and publication status for this revision are pending.

## Active files
- Assembled reader-facing manuscript: [`../draft-v2/manuscript.md`](../draft-v2/manuscript.md)
- Canonical components: [`../draft-v2/introduction.md`](../draft-v2/introduction.md) and six `chapter-*.md` files in `draft-v2/`
- Governing six-chapter structure: [`../outline-v3.md`](../outline-v3.md)
- Current claim dispositions: [`../research/claim-ledger.md`](../research/claim-ledger.md)
- Current paragraph/source map: [`../research/draft-v2-source-map.md`](../research/draft-v2-source-map.md)
- Editorial report: [`draft-v2-editorial-report.md`](draft-v2-editorial-report.md)
- Work log: [`daily-log.md`](daily-log.md)

## Counts and method
- **9,025 prose words** (headings, table rows and hidden HTML comments excluded).
- **9,559 visible word tokens** including title, contents, headings and tables.
- Per-component prose counts: Introduction 489; Chapter 1 877; Chapter 2 808; Chapter 3 1,458; Chapter 4 1,824; Chapter 5 1,536; Chapter 6 2,033.
- Chapter 6 contains 2,065 visible word tokens.
- Counts use `re.findall(r"\b\w+(?:[-’]\w+)*\b")`; prose excludes headings, table rows and HTML comments, and list items count separately. The visible count is about 1,895 tokens above the user-provided approximate baseline of 7,664; that comparison includes headings and tables on both sides.

## Revision summary
- Chapters 3–4 follow one fictional NOC assistant from its ordinary read/draft task and overbroad shared identity through a stale ticket note, accepted/queued request, detection, investigation, containment, degraded operation and limited restoration. The scenario’s assumptions and evidence limits are explicit.
- Credential revocation is separated from preventing new requests, handling existing sessions, accounting for queued/accepted work and checking resulting target state. Chapter 4 explains what to do when the target cannot cancel accepted work.
- Chapter 6 makes a qualitative, hypothetical choice among independent alarm visibility, supported patch preparation/change, identity separation and supplier diagnostic review. Capacity, a single assumed production window, parallel preparation, interim restrictions, residual exposure, the rejected alternative and reversal evidence are stated.
- Chapters 1–2 restore explanation around deployment/activity/productivity/service/security measures and show how public threat observations lead to conditional local defensive priorities without inferring AI use.
- The supplied style sample informed the introduction and Chapter 1: concrete subjects, familiar verbs, conversational cadence and clear distinctions between what a report says and what it does not establish.
- Source-map anchors and Chapter 3’s internal source map were refreshed. No new external sources, operator outcomes, measurements, costs, ROI or tests were added.

## Verification and limits
- Reassembled from seven canonical components, each exactly once; contents links match all seven headings.
- Structural validation passed: source-map anchors in range, two Markdown tables have consistent columns, README links resolve, and no hidden comments, numeric citations, placeholders, reader-facing Sources heading, leaked “composite” terminology or removed ENISA count digression appear in the reader-facing assembly.
- `git diff --check` passed. Scenario editorial meta-language checks passed.
- No PDF was generated. ReportLab is installed, but no page renderer was available for visual inspection. No rendered page count is claimed.
- No human, operator or legal-counsel review is claimed. Local service scope, legal applicability, costs, staffing, supplier rights and fallback readiness still require operator-specific verification.