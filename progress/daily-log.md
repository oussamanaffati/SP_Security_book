# Active editorial log

Detailed cycle history is preserved in `progress/archive/daily-log-before-recompaction.md` and earlier archives under `progress/archive/`.

## Current status
- Repository: `/data/SP_Security_book`, branch `main`. Push was rejected for invalid credentials; local commits remain unpushed and remote `main` remains `bd32ad4`. Do not retry until credentials are corrected.
- Manuscript: 19,482 words (Ch1 3,767; Ch2 4,075; Ch3 2,316; Ch4 6,096; Ch5 3,228), versus the 40,000–45,000-word target. Editorial score 7.6/10 remains provisional and self-assessed.
- Structural pass is complete. Chapter 4's first implementation pass and Chapter 5's first board-governance/funding pass are committed locally; Chapter 2's processing-boundary and identity-to-connector decisions have now been expanded. The four existing composites remain the only worked scenarios; no operator outcomes, quotes, costs or test results were invented.
- Critique: repetition and table density improved, and decision paths are clearer. The manuscript remains far below target; Chapters 1–3 still need substantive expansion, so 9/10 is not yet defensible. Primary model: gpt-6-luna. Grok was not run under the author’s local-first waiver.

## Recent cycles
- 2026-11-14 | Chapter 2 processing-boundary decision | 19,447 words | Compared operator-managed processing, supplier-hosted service and data minimization; added verification of runtime destination, retention, support and backup paths, and kept advisory/restricted use as the fallback when evidence is missing. Critique: balances service utility with supplier, staffing and continuity costs; no operator facts or test results invented. Primary model: gpt-6-luna; Grok not run under the author’s local-first waiver. `git diff --check` and counts passed. Next: identity-to-connector boundary.
- 2026-11-14 | Chapter 2 identity/revocation path | 19,482 words | Expanded per-hop principal correlation and clarified that upstream revocation may not end downstream sessions or queued actions; recommended human-mediated or restricted high-impact work where target-side termination cannot be verified. Critique: useful containment distinction without claiming a specific system behavior or incident. Primary model: gpt-6-luna; Grok not run under the author’s local-first waiver. `git diff --check` and counts passed. Next: broker failure and service visibility.

## Next
Continue Chapter 2 with broker-failure behavior, then finish its pass before Chapter 1 and Chapter 3. Recount and rebalance the full book after that pass.