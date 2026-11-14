# Active editorial log

Detailed history is preserved in `progress/archive/daily-log-before-structural-pass.md`, `progress/archive/daily-log-before-cycle-compaction.md` and `progress/archive/daily-log-before-chapter5-compaction.md`.

## Current status
- Repository: `/data/SP_Security_book`, branch `main`. A prior push was rejected for invalid credentials; continue local work and retry only after the existing credential setup is corrected.
- Current manuscript: 19,033 words (Ch1 3,775; Ch2 3,888; Ch3 2,354; Ch4 5,858; Ch5 3,158). Target: 40,000–45,000 substantive words. Editorial score remains provisional at 7.6/10, self-assessed; no independent review.
- The active log is intentionally compact; the preceding full log was archived with matching SHA-256 before compaction.

## Recent cycles
- 2026-11-14 | Chapter 4 Moves 3–4 | 19,193 words | Consolidated the NOC exercise criteria, separated tabletop discussion from technical validation, reduced the portfolio roadmap from four to three columns, and removed repeated authority/assurance endings. Critique: clearer, more scannable decisions; structural compression is not substantive expansion. Commits `693240f`, `1f84764`; `git diff --check`, chapter counts and table shape passed. No new facts. Next: Chapter 5.
- 2026-11-14 | Chapter 5 board framing and authority | 19,033 words | Tightened the service-first board framing, shortened the supplier-feature oversight test, and merged repeated review-trigger/authority language. Critique: more direct and less repetitive, without changing the established authority model or adding facts; Ch5 evidence, board tools and substantive expansion remain. Primary editorial model: gpt-6-luna; Grok not run under the author’s local-first waiver. `git diff --check` and chapter counts passed. Next: Chapter 5 evidence and board tools.
