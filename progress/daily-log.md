# Active editorial log

Historical cycle detail is preserved verbatim in `progress/archive/daily-log-before-structural-pass.md`.

## Verified baseline

- Repository: `/data/SP_Security_book`, branch `main`; last confirmed local/remote commit before this pass: `bd32ad4`.
- Baseline manuscript before the opening edit: 21,108 words across five chapters. Current count after the opening edit: 21197 (Ch1 3980; Ch2 4113; Ch3 3155; Ch4 6368; Ch5 3581).
- Goal: 40,000–45,000 substantive words and a defensible 9/10. Use only the four established operator scenarios; no invented outcomes.

## Active cycle

- 2026-11-14 | Structure / Chapter 1 opening | Ch1 3,980; book 21,197 | 7.4/10 baseline per author; no score change after one section | Created the 646-word editorial queue with primary homes and definitions; rewrote the opening around the NOC assistant’s alternatives, continuity/staff costs, conditional recommendation and verification evidence; removed the internal “Composite scenario” label. Archived the 750-line history unchanged and reduced the active log. `git diff --check` passed; all five chapters recounted. Next: Chapter 4—turn the supplier diagnostic into a complete conditional decision and place the single evidence-level definition there.
- 2026-11-14 | Chapter 4 | Ch4 6,596; book 21,425 | 7.5/10 provisional—modest improvement from a decision path with explicit evidence levels and costs; still far below 9/10 | Defined four evidence levels once in Chapter 4; replaced the supplier-feature data-flow caveat with a conditional choice that distinguishes independent disablement, target-side limits, pause/rollback and time-limited use, and specifies the test, service/fallback evidence and costs. Removed internal “composite/supplied” labels from Chapter 4 and corrected an unsupported edge/agent conflation. No new source, outcome or number added. Style check: direct and operator-specific, but still too much repeated ownership/evidence language elsewhere in Chapter 4. Editorial pass: gpt-6-luna; Grok not used because optional. `git diff --check` passed; all five chapters and the 648-word queue recounted. Biggest open issue: deferred patch-window decision is not yet a complete worked example, and residual-risk endings still repeat. Next: Chapter 4—complete the patch-window decision with separate threat and change-readiness evidence, tested interim controls, continuity/staff/supplier costs and a conditional recommendation.
