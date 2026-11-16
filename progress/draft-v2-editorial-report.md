# Draft v2 editorial report

**Date:** 16 November 2026

**Status:** Revised manuscript for author review; not publication-ready.

**Active file:** [`../draft-v2/manuscript.md`](../draft-v2/manuscript.md)
**Canonical sources:** `draft-v2/introduction.md` and the six `draft-v2/chapter-*.md` files. `outline-v3.md` remains the governing structure.

## Counts

- **Prose:** 8,092 words, excluding headings, table rows and hidden HTML comments.
- **Visible manuscript:** 8,622 word tokens, including title, subtitle, contents, headings and tables.
- **Chapter 6:** 1,644 prose words, 36.3% below the previous recorded 2,581-word version. This is slightly above the requested approximate 25–35% reduction; the cut removed repetition while retaining the substantive decision set.

Counts use `re.findall(r"\b\w+(?:[-’]\w+)*\b")`; list items count separately. These are editorial word counts, not a page target.

## What changed

### Chapters 3 and 4: show the authority and the service consequence

Chapter 3 develops the author-supplied shared edge/core account situation. It distinguishes its known scope (one account reaches edge nodes and parts of core; remediation depends on supplier configuration and a safe window) from educational assumptions about an assistant, data, connector and target API. It follows the call and compares continued use, a tested gateway, separate target-native identities and a staged migration. The recommendation keeps the agent out of the write path until scope and migration are proven; Network Engineering and the supplier verify supported identities and windows, while the service executive owns any necessary period of broad support.

Chapter 4 fully introduces the NOC-assistant situation and separates known details (alarm summaries, ticket drafts, neighboring-domain reads, supplier cases, and an unexecuted visibility-reducing proposal) from added assumptions about the shared identity, connectors and target. It explains that stopping a runtime may leave a connector credential, active target session or accepted queued request in place. It gives concrete checks at runtime, connector and target, and explains why a verified independent alarm view changes whether the broad identity can be revoked without losing operational visibility. These are recommendations, not claimed test results.

### Chapter 6: one decision record, less repetition

The four-row priority table and repeated decision fields were removed. The chapter now has four candidate work areas, one local selection method, one explicitly hypothetical three-of-four choice, one concise sequence, one board brief that serves as the portfolio decision record, and conditions that change the order. The close asks the reader to choose three or four local priorities and uses the worked choice only as an example. Local owners, budgets, work-item identifiers and windows remain fields to fill; no operator values are invented.

### Chapters 1 and 2, introduction and transitions

Chapter 1 explains the distinctions among deployment, activity, productivity, service quality, security effectiveness and ROI together, then applies them to attributed examples without repeating the full caveat after each one. Chapter 2 preserves the material difference between ENISA’s 30-incident OSINT overview and 188 authority-submitted significant-incident reports, removes the unused Member State-count digression, states the AI-attribution limit and turns toward local preparation. The introduction now promises two fully developed illustrative situations plus a shorter supplier-feature example. Chapter 2 and Chapter 5 now transition to the next decision rather than summarizing themselves.

## Final critique pass: findings and corrections

One continuous internal read of the assembled manuscript found and corrected these passage-level issues:

1. **Chapter 6, selection and board sections:** the per-priority decision record repeated owners, evidence, cost, capacity, displacement and fallback in the later board brief. Removed the duplicate record and made the board brief the single portfolio record.
2. **Chapter 6, final paragraph:** the meeting recommendation could read as a universal three-work-area package. It now asks the reader to select three or four from local evidence and labels the three-work-area decision as the hypothetical example.
3. **Chapters 3–4, scenario boundaries:** clarified which details belong to the supplied situations and which are educational assumptions. Changed wording that implied the supplier feature was already disabled; the recommendation now says not to enable or expand it until release checks pass.
4. **Reader journey and terminology:** replaced reader-facing “composite” language with “illustrative scenario,” expanded Network Operations Center (NOC) and Security Operations Center (SOC) at first use, and repaired the Chapter 2/5 transitions.
5. **Source anchors:** corrected Chapter 1 and 2 anchors and recalculated current paragraph/list-item mappings for all revised chapters.

No external claim was added or broadened. The current claim-ledger dispositions govern; historical repository claims are not automatically certified. No successive critique rounds or new reviewers were launched.

## Verification and limitations

- Regenerated `draft-v2/manuscript.md` from the introduction and six chapter files. Each component appears exactly once; all contents anchors match headings.
- Verified source-map paragraph anchors against the current components, both Markdown tables for consistent columns, repository-local README links, and `git diff --check`.
- No hidden audit comments, inline numeric citations, TODO/TBD/FIXME markers, reader-facing “composite” terminology or ENISA Member State-count digression remain in the assembled manuscript.
- No PDF was generated. ReportLab, pypdf and Markdown are installed, but no page renderer (Pandoc, LibreOffice, Chromium, wkhtmltopdf, `pdftoppm` or `mutool`) is available for visual inspection. No rendered page count can be reported.
- No human, operator or legal-counsel review is claimed. Costs, staffing, service tolerances, supplier rights, legal applicability, and local fallback paths require operator-specific verification.

## Git status at revision start

On `main`, local `HEAD` and live `origin/main` were verified as `c4257d11554709363f385a864090955bfe855cc2`; the branch had no ahead/behind commits. This corrected earlier status text that said the preceding work was local-only. The commit and push status for the current revision will be recorded after the final Git operation.
