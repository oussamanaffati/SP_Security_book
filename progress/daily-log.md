# Active editorial log

Detailed history is preserved in `progress/archive/daily-log-before-structural-pass.md`, `progress/archive/daily-log-before-cycle-compaction.md`, `progress/archive/daily-log-before-chapter5-compaction.md` and `progress/archive/daily-log-before-wholebook-compaction.md`.

## Current status
- Repository: `/data/SP_Security_book`, branch `main`. A prior push was rejected for invalid credentials; continue local work and retry only after the configured credential is corrected.
- Manuscript: 18,474 words (Ch1 3,767; Ch2 3,874; Ch3 2,316; Ch4 5,735; Ch5 2,782), versus the 40,000–45,000-word target. Editorial score remains provisional at 7.6/10; self-assessed, not independently reviewed.
- Full pre-compaction log archived byte-for-byte; SHA-256 matched.

## Recent cycles
- 2026-11-14 | Chapter 4 Moves 3–4 and Chapter 5 structural pass | Removed repeated authority/evidence endings, consolidated the NOC exercise, reduced roadmap/board tables and preserved the conditional worked decisions. Commits `693240f`, `1f84764`, `699a0f5`, `838aee6`, `eba3861`.
- 2026-11-14 | Whole-book rebalance | Corrected Chapter 1’s patch wording so a scheduled window is not implicit acceptance; shortened the Chapter 2 source-contract row, Chapter 3 containment choice and Chapter 4 supplier register. Diff checks and table-shape checks passed. Critique: cleaner structure, but several long cells remain in Chapter 3 and Chapter 4; these need one more pass before expansion. No new facts. Primary model: gpt-6-luna; Grok not run under the author’s local-first waiver.
- 2026-11-14 | Whole-book rebalance: Chapter 3 containment card | 18,558 words | Shortened scope, authority/service and verification cells; largest remaining row cell is 200 characters. Critique: reduced table density while preserving incident decision, service impact and proof; no new facts. Primary model: gpt-6-luna; Grok not run under local-first waiver. `git diff --check` and counts passed. Next: Chapter 4 authority matrix and final book-wide checks.
- 2026-11-14 | Whole-book rebalance: Chapter 4 authority matrix | 18,474 words | Shortened Read/Recommend/Execute cells while retaining target-side limits, evidence checks, operator decision and service fallback. Critique: materially more scannable without changing its boundaries or making untested claims; no new facts. Primary model: gpt-6-luna; Grok not run under local-first waiver. `git diff --check`, counts and table shape passed. Next: final whole-book structural checks, then Chapter 4 expansion.

## Next
Rerun whole-book format, table-density, repetition and cross-reference checks, then begin substantive Chapter 4 expansion toward the word target.
