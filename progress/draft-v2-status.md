# Draft v2 status

**As of:** 16 November 2026
**Status:** Complete six-chapter working draft for author review; final editorial pass and assembly validation are complete. Local commit and requested push verification are pending. Not publication-ready.

## Active files
- Reader-facing assembly: [`../draft-v2/manuscript.md`](../draft-v2/manuscript.md)
- Governing structure: [`../outline-v3.md`](../outline-v3.md)
- Source components: [`../draft-v2/introduction.md`](../draft-v2/introduction.md) and six `chapter-*.md` files in `draft-v2/`
- Claim dispositions: [`../research/claim-ledger.md`](../research/claim-ledger.md)
- Paragraph/source map: [`../research/draft-v2-source-map.md`](../research/draft-v2-source-map.md)
- Chapter 6 research/editorial record: [`../research/chapter-06.md`](../research/chapter-06.md)
- Work log: [`daily-log.md`](daily-log.md)
- Historical chapters are preserved under `chapters/`; they are not the active manuscript or factual authority.

## Verified in the current draft
- All six outline chapters, an introduction, title/subtitle and contents are assembled in reading order.
- Reader-facing component text appears once; internal HTML audit comments are omitted from the assembly.
- All six chapter headings match the contents anchors. Four Markdown tables have consistent columns.
- No reader-facing `Sources` heading, numeric citation, TODO/TBD/FIXME marker or exact duplicate block was found.
- Source-map validation checked 66 paragraph/sentence anchor tokens; none were out of range.
- Readability diagnostics: 10,661 reader-facing word tokens including title, contents, headings and tables; 9,630 prose words; 666 prose sentences; mean 14.46 words/sentence; maximum 30; none over 30. See the work log for the counting method.
- Two whole-book editorial passes have been completed: argument/reader journey and, on the current assembly, evidence boundaries, acronyms, structure, cadence and repetition.

## Review and release limits
- Two separate-context Chapter 6 critiques by GPT-6-Luna (same available model, not human or independent-model review). The first identified a missing local selection rule and per-priority decision record. The second found no High-severity defect and recommended commit; it raised Medium concerns about treating four rows as a default package and repeating decision fields, plus Low concerns about displaced-work specificity and trigger repetition. These were addressed by naming candidate areas, recording owners/triggers for omitted rows, requiring local displaced-work identifiers, reducing the board prompt to four fields and trimming the conclusion/trigger language.
- No human, legal-counsel or independent-model review is claimed. The work uses current claim-ledger dispositions; it does not certify every historical claim in the repository. Operator-specific costs, staffing, service tolerances, supplier rights and legal applicability remain local inputs, not manuscript facts. No PDF was rendered: no page-level renderer is installed for visual inspection.
- Prior pre-commit baseline: branch `main`; local `HEAD` and fetched/live `origin/main` were both `8f07e72c00635191aaa2fbabc04130090e8b404d`, with zero ahead/behind. That check predates the final editorial edits. The current request authorizes commit and push; refresh Git state before proceeding. No push attempt has yet been made.

## Exact continuation point
The Chapter 6 critique and final whole-book pass are complete. The working manuscript is assembled and validated. Refresh Git state and diff checks, commit the author-review version, attempt the requested push once, and verify the remote branch and commit; if authentication fails, preserve the local commit and report the exact failure without retrying.
