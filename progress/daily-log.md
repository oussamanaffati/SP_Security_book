# Active editorial log

Older cycle history is preserved in `progress/archive/daily-log-before-compaction-2026-11-14.md` and earlier archives under `progress/archive/`.

## Current status
- Repository: `/data/SP_Security_book`, branch `main`; latest local commit before this log cleanup: `9100bce`.
- Push authentication previously failed. The last read remote `main` was `bd32ad4`; do not retry unchanged credentials. Local work remains unpushed.
- Manuscript: 20,220 words (Ch1 4,030; Ch2 4,244; Ch3 2,662; Ch4 6,056; Ch5 3,228), versus the 40,000–45,000-word target. Gap to the lower target: 19,780 words.
- First structural/expansion pass and whole-book review are complete. Chapter homes are distinct; no exact duplicate paragraphs or reader-facing internal labels, numeric citations or Sources headings were found. Some table cells in Chapters 2–4 still need shortening. The generic Chapter 4 risk disclaimer was removed; Chapter 5 remains the home for executive risk decisions.
- Four existing scenarios only. No operator outcomes, quotes, costs or test results were invented. Editorial score 7.6/10 is provisional and self-assessed; 9/10 is not defensible yet. Primary model: gpt-6-luna. Grok was skipped under the local-first waiver; no new source claims were added or re-fetched.

## Recent cycles
- 2026-11-14 | Active-log compaction | Archived the prior active log verbatim and retained the current status, recent decisions and exact next action.
- 2026-11-14 | Chapter 3 after-hours authority | 20,124 words | Compared case-by-case approval, broad standing authority and narrow pre-authorized actions; added service boundaries, deputies, supplier dependencies and exercise evidence. `git diff --check` and counts passed.
- 2026-11-14 | Chapter 3 customer protection | 20,260 words | Added the conditional choice between waiting for fuller scope and staged factual updates when customer action is supported; included review duties, contact capacity and overstatement risk. No internal process was attributed to SK Telecom.
- 2026-11-14 | Whole-book review | 20,238 words | Confirmed distinct chapter/tool homes and no exact duplicates. Removed generic residual-risk wording from Chapter 4’s introduction and replaced “supplied composite” in the outline. Long table cells remain a quality issue.
- 2026-11-14 | Chapter 4 exercise choice | 20,268 words | Clarified when a tabletop, bounded technical test or integrated rehearsal answers the unresolved question; accounted for service, staffing and supplier effort. No new scenario or universal timeline.
- 2026-11-14 | Chapter 4 supplier table | 20,247 words | Shortened cells while preserving data/retention questions, supplier friction, manual NOC effort, alternatives and verification. `git diff --check` and counts passed.
- 2026-11-14 | Chapter 4 edge-access change gate | 20,231 words | Shortened the four gate rows while retaining service impact, supplier readiness, allowed/denied-path proof, rollback and review trigger. Critique: the table is easier to scan without weakening the migration decision. `git diff --check` and counts passed.
- 2026-11-14 | Chapter 4 roadmap table | 20,220 words | Shortened the stage/lead/evidence cells and kept the four implementation gates, support dependencies, capacity and proof. Critique: the roadmap scans more easily; detailed effort and displacement remain in the accompanying prose. `git diff --check` and counts passed.

## Next
Chapter 4, Move 1: shorten the remaining long supplier-feature table cells while leaving the detailed decision reasoning in prose.