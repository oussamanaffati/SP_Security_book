# Editorial queue: structural repair and expansion

**Current checkpoint (2026-11-15):** After the Chapter 1 NOC-benefit edit, the consistent on-disk count is 28,203 words: Ch1 3,840; Ch2 4,748; Ch3 5,298; Ch4 9,432; Ch5 4,885. Python `re.findall(r'\b\w+\b', text)` was used on all five files. The previous checkpoint was 28,454; before Chapter 4’s structural pass it was 35,186; at initial reconciliation the count was 38,743. The daily log’s 38,752 is a historical cycle count and 40,029 is not present in the current queue. Reconciliation began from clean local `main` at `ca808d3683b79e885e11be3d86ed3b8c702c4f09`, four commits ahead of live `origin/main` `19983fc24c98bf57833e2140bb0621e71e57f3b6`. The four approved scenarios are illustrative. Remove repetition, not useful implementation or funding depth.

## Primary homes and chapter boundaries

- **Chapter 1 — stakes, thesis, investment choices.** Show why an operator faces two different AI risks: delegated authority inside the business and faster external threats. Frame the consequences for service continuity and where an investment changes the choice. Do not repeat the implementation instructions.
- **Chapter 2 — identity, data, connectors and enforceable boundaries.** Explain what an agent can reach, how authority crosses systems, and how to prove that a boundary is enforced. Keep the source-contract and memory-scope tests here.
- **Chapter 3 — decisions under pressure.** Own response timing, decision rights during an incident, containment choices, fallback and restoration. Keep live-incident and recovery guidance here; distinguish authorization from technical proof.
- **Chapter 4 — implementation sequence and tools.** Primary home for the agent/workflow register, read/recommend/execute matrix, SOC/NOC exercise criteria and 12-month implementation roadmap. Define evidence levels here: supplier assertion/design documentation, deployed-configuration review, bounded technical test, and operational exercise or observation. They answer different questions; none proves the whole workflow.
- **Chapter 5 — executive choices, funding and oversight.** Primary home for the board decision paper and residual-risk decision record. Define roles once: the service owner supplies impact, tolerance and fallback evidence; the authorized service executive accepts service residual risk only within delegated authority and approved appetite; the board sets appetite, resources and challenge, not operational acceptance. Escalate when authority is absent or appetite is exceeded.

## Structural rules

Replace repeated paragraph-ending formulas about evidence, ownership, appetite and escalation with the decision consequence that matters in that passage. Revisit authority only when the decision or affected service changes. Keep a limitation only where it changes an option or confidence in the control.

Remove reader-facing process labels such as “supplied composite” and “author guidance.” Introduce a scenario naturally as illustrative once; state only the factual boundary a reader needs, such as whether a change actually occurred. Do not repeat caveats at every retelling.

Keep tables only for comparison or compact decisions. Give each tool one primary home; convert dense narration/checklist rows into short prose, reduce columns, and preserve only fields needed to decide or verify. Use varied openings and sentence lengths. Prefer concrete verbs and a clear recommendation under stated conditions. Archive the oversized historical daily log unchanged, then keep the active `progress/daily-log.md` to a compact status plus short cycle entries and an exact next action.

## Worked decisions: first pass

1. **Supplier diagnostic feature (Chapter 4):** expanded from known topology-read/action-proposal facts and unknown identity, data destination/retention, write path, disablement and fallback into a conditional choice. Retain or restrict only with tested limits; otherwise pause/rollback or escalate. Do not imply a supplier commitment, test result, measured benefit or cost.
2. **Deferred patch window (Chapter 4):** expanded into a decision that separates threat/reach evidence from change readiness; compares earlier supported change, waiting with verified controls, and restricting affected access; weighs continuity, staff, supplier and effort costs; states recommendation triggers and post-change verification. No local threat, version, control effectiveness or price is assumed.

## Whole-book review after first pass

Automated whole-book checks found no exact duplicate paragraph blocks, numeric citations, reader-facing Sources headings or TODO/TBD/FIXME markers; titles and cross-references were consistent. The four first scenario introductions in Chapter 1 were labeled illustrative. The prior read-only review flagged repeated supplier-feature decisions and a second close in Chapter 4, plus a repeated patch decision and second close in Chapter 5. Chapter 4’s ACSC [25] guidance claim remains limited to the official search excerpt: a 2026-11-15 page/PDF retrieval attempt did not return body text, so do not broaden the claim until it can be checked. The earlier table scan found a 188-character funding-condition cell in Chapter 5 line 167; later Chapter 5 structural edits removed that table. The latest scan reports maxima under 180 characters in every chapter: 139, 113, 150, 179 and 149 respectively. No Chapter 4 or 5 edits had been made at that earlier review.

## Next sequence
1. Chapter 4 structural pass is committed locally as `4e13d28`; post-commit readback showed `origin/main` still at `19983fc24c98bf57833e2140bb0621e71e57f3b6`. Publication is pending after authentication failure; continue locally and do not retry unchanged credentials.
2. Chapter 5 case decisions, funding gates, investment rationale, run-cost ownership, board dashboard, exception process and duplicate close are revised. Its portfolio section now points to per-case board asks and Chapter 4’s operational gates instead of repeating their test steps; the conditional funding sequence and local dependency check remain.
3. Chapter 1’s NOC benefit-measurement table is removed; the chapter retains the strategic distinction that a value pilot tests task benefit but does not reduce account reach. Chapter 4 owns pilot evidence and Chapter 5 funding/oversight. Next inspect Chapter 1’s board-evidence briefing against Chapter 5’s dashboard and oversight for repeated reporting structure, preserving the distinct evidence layers of the sourced incident and vulnerability cases and their research mappings.
4. Publication remains pending unless authentication circumstances change; verify remote `main` before any publication claim.
