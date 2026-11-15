# Editorial queue: structural repair and expansion

**Current checkpoint (2026-11-15):** After replacing Chapter 4’s board-facing metric/assurance recap with the operational evidence record, the consistent on-disk count is 35,693 words: Ch1 4,911; Ch2 4,725; Ch3 5,298; Ch4 10,345; Ch5 10,414. Python `re.findall(r'\b\w+\b', text)` was used on all five files. The previous Chapter 4 pilot-handoff checkpoint was 36,122; at initial reconciliation the count was 38,743. The daily log’s 38,752 is a historical cycle count and 40,029 is not present in the current queue. Reconciliation began from clean local `main` at `ca808d3683b79e885e11be3d86ed3b8c702c4f09`, four commits ahead of live `origin/main` `19983fc24c98bf57833e2140bb0621e71e57f3b6`. The four approved scenarios are illustrative. Remove repetition, not useful implementation or funding depth.

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

Automated whole-book checks found no exact duplicate paragraph blocks, numeric citations, reader-facing Sources headings or TODO/TBD/FIXME markers; titles and cross-references were consistent. The four first scenario introductions in Chapter 1 were labeled illustrative. The prior read-only review flagged repeated supplier-feature decisions and a second close in Chapter 4, plus a repeated patch decision and second close in Chapter 5. Chapter 4’s ACSC [25] guidance claim remains limited to the official search excerpt: a 2026-11-15 page/PDF retrieval attempt did not return body text, so do not broaden the claim until it can be checked. The earlier table scan found a 188-character funding-condition cell in Chapter 5 line 167; that baseline will be checked after the current edit. No Chapter 4 or 5 edits had been made at that earlier review.

## Next sequence
1. Read revised Chapter 4 end to end with the outline and Chapters 3/5, check repeated reasoning and reader-facing/source constraints, then commit and attempt publication. Verify the actual remote `main` ref before claiming success.
2. Chapter 5: reduce supplier-feature and NOC-assistant sections to board funding, appetite and oversight decisions; remove repeated operational assumptions, test branches and residual-risk fields owned by Chapter 4.
3. Compress the patch discussion to the board’s readiness/resource decision and conditions for management’s return, not a second operational patch procedure.
4. Review Chapter 1’s opening and state once that the four operational examples are illustrative composites. Then run whole-book consistency, claim/source, citation, table and count checks; commit and publish completed chapters as authorized.
