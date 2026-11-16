# Draft v2 status

**As of:** 16 November 2026

**Editorial status:** Revised six-chapter author-review manuscript. Not publication-ready.
**Git status:** Manuscript revision committed locally as `0db70ac0334d98711aea450a4492cb6b004f55d2`. A normal push was attempted after confirming the live baseline; GitHub rejected authentication (`Invalid username or token. Password authentication is not supported for Git operations.`). At the failed-push readback, local `HEAD` was `0db70ac0334d98711aea450a4492cb6b004f55d2` and live `origin/main` remained `c4257d11554709363f385a864090955bfe855cc2` (one local commit ahead, zero behind). The final status/log correction is a separate local documentation commit; no retry will be made without changed credentials.

## Active files
- Assembled reader-facing manuscript: [`../draft-v2/manuscript.md`](../draft-v2/manuscript.md)
- Canonical components: [`../draft-v2/introduction.md`](../draft-v2/introduction.md) and six `chapter-*.md` files in `draft-v2/`
- Governing six-chapter structure: [`../outline-v3.md`](../outline-v3.md)
- Current claim dispositions: [`../research/claim-ledger.md`](../research/claim-ledger.md)
- Current paragraph/source map: [`../research/draft-v2-source-map.md`](../research/draft-v2-source-map.md)
- Chapter 6 evidence and editorial record: [`../research/chapter-06.md`](../research/chapter-06.md)
- Editorial report: [`draft-v2-editorial-report.md`](draft-v2-editorial-report.md)
- Work log: [`daily-log.md`](daily-log.md)

## Counts and verification
- **8,092 prose words** (headings, tables and hidden HTML comments excluded).
- **8,622 visible word tokens** including title, contents, headings and tables.
- Chapter 6: **1,644 prose words**, down 36.3% from the prior recorded 2,581-word version; slightly beyond the requested approximate 25–35% range.
- Assembled from seven canonical components exactly once. Contents links match all seven headings; source-map anchors are in range; both Markdown tables have consistent columns; README relative links resolve; `git diff --check` passed.
- The reader-facing manuscript contains no hidden audit comments, inline numeric citations, TODO/TBD/FIXME markers, stale ENISA Member State-count digression or “composite” terminology.

Counts use `re.findall(r"\b\w+(?:[-’]\w+)*\b")`; prose excludes headings, table rows and HTML comments, with list items counted separately.

## Main changes
- Chapters 3 and 4 now work through the shared edge/core account and NOC-assistant situations, with supplied facts separated from educational assumptions. Chapter 4 explains target-side session/queue checks and the operational value of an independent alarm view.
- Chapter 6 has four candidate areas, one local selection method, one hypothetical three-of-four choice, a concise sequence, a single board brief used as the decision record, and conditions that change the order.
- Chapters 1 and 2 retain the deployment/activity/productivity/service-quality/security distinctions, separate ENISA datasets and bounded AI attribution. The introduction promises two fully developed situations and one shorter supplier-feature example.
- The source map and research notes were refreshed; no new research claims, incidents, costs, ROI or test outcomes were introduced.

## Limits
No PDF was generated. ReportLab, pypdf and Markdown modules are installed, but no page renderer is available for visual inspection. There is therefore no rendered page count. No human, operator or legal-counsel review is claimed. Operator-specific costs, capacity, owners, work items, service tolerances, supplier rights and legal applicability remain local inputs.
