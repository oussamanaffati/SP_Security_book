# Daily Log

## Repository setup
- Created the initial repository structure, approved five-chapter working outline, and chapter briefs.
- Added the `book-continuous-improvement` skill for sequential, research-led chapter cycles.
- Chapter files are working briefs, not complete manuscript drafts.
- Next: wait for the author to request the first chapter cycle; do not start cycles automatically.

## 2026-11-13 — Chapter 1 first manuscript cycle
- Researched developments published within 12 months: Singapore CSA/IMDA Operation CYBER GUARDIAN (9 Feb 2026), ENISA NIS360 (May 2026), and six-agency agentic-AI adoption guidance (1 May 2026); NIS2 Commission page used only for regulatory background. Research notes: `research/chapter-01.md`.
- Read the prior Chapter 1 brief and outline, then replaced the brief with a full English first draft (2,442 words before the Sources section). Added citations to four sources; strict citation verification passed.
- Draft anchors the argument in Singapore’s documented telco campaign, ENISA findings on telecom criticality/legacy constraints, and current agentic-AI guidance. It explicitly does not claim the Singapore campaign involved AI.
- Honest self-critique: the core thesis is clear and SP-grounded, and Chapter 2’s attack-surface question is set up. Still needed: more operator voices and regional regulatory detail; the present sources establish agentic risks and sector pressures, but do not establish that AI has already accelerated all external threats. Keep that uncertainty explicit. No claim that a hypothetical operator scenario is a real incident.
- Next: author feedback on Chapter 1 only; do not begin Chapter 2 until requested.

## 2026-11-13 — Chapter 1 style and urgency revision
- Updated the continuous-improvement skill and `/data/memories/MEMORY.md` with Oussama’s requested English-language voice, quality gates and shorter-cycle process. Recorded that Paris/EMEA/Cisco Live biographical context may be used sparingly when relevant; none was added to this chapter.
- Checked the full Cisco blog “A Glimpse Into Cisco Mobile Infrastructure Security Developments” and both official Cisco Live PDFs, BRKSEC-2325 and BRKSEC-2763, as style references. Kept the manuscript direct and conversational, without product promotion or invented customer anecdotes.
- Re-ran current research. Added CISA’s 10 Nov 2026 KEV entry and Cisco’s 12 Nov advisory on CVE-2026-20320, plus Malbear Labs’ 8 Nov “Operation Snowball” report. Carefully separated confirmed active exploitation from the research group’s AI-campaign claims; retained caveats that the victim is unnamed and reported impacts are not independently confirmed in the public record reviewed.
- Chapter changes: reduced body from 2,442 to 2,016 words (17.44% shorter); removed em dashes from the manuscript body; tightened repeated passages; sharpened the board-level urgency; added the client-reported edge-workload theme, a supplier-delivered AI feature example, and the current BroadWorks case with explicit caveats; retained concrete maintenance-window, rollback and vendor-coordination constraints; rewrote the ending to distinguish Chapter 1’s “why risk changed” from Chapter 2’s “where it lands.”
- Hard self-critique: “Does this sound like Oussama?” More direct and closer to the checked public samples, but authentic customer voice still needs Oussama’s review. “Too AI-written?” Less formulaic and no em dashes in the body, though the three recommendations remain deliberately structured. “Natural?” Mostly short, varied sentences; watch for the polished explanatory cadence. “Strong SP reality?” Improved with operational constraints and a live service-provider example. Keep the Malbear caveat; do not present it as official attribution or verified in every detail.
- Strict citation verification passed; no Telegram message was sent (previously waived for this project).
- Next: stop and wait for author feedback on Chapter 1; do not start Chapter 2.

## 2026-11-13 — Chapter 2 first full cycle
- Researched the previous 12 months with primary regulator and cyber-agency sources: TRAI’s 30 Oct 2026 telecom AI consultation draft, CISA and partner agencies’ May 2026 agentic-AI guidance and full report, and CERT-In’s 15 Oct 2026 advisory; added TM Forum’s Feb 2026 report of specific telco agent-security examples. Evidence, dates, scope and limitations are recorded in `research/chapter-02.md`.
- Replaced the Chapter 2 brief with a full first draft of 2,012 words before the Sources section. The chapter maps exposure across identities, data, tools, workflows and suppliers, then connects the issue to OSS/BSS and network domains, legacy, maintenance windows, change control and supplier access.
- Added a clearly labeled composite fiber-assurance scenario, not a reported incident. It shows how untrusted supplier content, broad identity, operational data and ticket/workflow tools could combine, with bounded controls that preserve normal network change approval.
- Kept the Chapter 2/3 boundary clear: this chapter asks where exposure enters and spreads; Chapter 3 will address threat speed and the operator’s ability to decide and respond. Chapter 3 was not edited.
- Hard self-critique: the draft is direct and grounded in operator processes, but the public evidence for production agent use at telcos remains limited. The TRAI source is a consultation draft, the CERT-In events are not identified as telecom incidents, and the TM Forum examples are attributed reporting. The composite scenario should be tested against the author’s lived NOC experience. Some explanatory cadence remains; no private operator conversation or personal experience was invented.
- Strict citation verification passed with evidence quotes for all five source references; 14 of 127 prose sentences carry citations (11%). The body has no em dashes. `git diff --check` passed. No Telegram message was sent under the project’s existing waiver.
- Next: stop and wait for author feedback on Chapter 2; do not start Chapter 3.

## 2026-11-13 — Chapter 3 first full cycle
- Researched recent primary sources: the Canadian Centre for Cyber Security’s 26 Oct 2026 agentic-AI bulletin, CERT-In’s 15 Oct 2026 advisory, and South Korea MSIT’s 2025 SK Telecom investigation and customer-protection updates. Recorded dates, direct evidence, limits and chapter decisions in `research/chapter-03.md`.
- Replaced the Chapter 3 brief with a full first draft of 2,091 words before the Sources section. The central frame separates detection, decision, action, and continuity/recovery clocks, so response speed is not reduced to SOC alerting.
- Used the Canadian and CERT-In findings as attributed evidence of compressed attack stages, while stating that they are not telecom-specific and do not establish universal or fully autonomous attacks. Used the SK Telecom record to distinguish detection, statutory notification, forensic scope and customer protection; did not label the breach AI-driven or claim it caused a network outage.
- Added a clearly labeled composite NOC/SOC scenario during a planned maintenance window. It covers a suspicious management identity, service dependencies, supplier input, tiered containment, fallback operation and cross-team decision authority. The scenario is illustrative, not a reported incident.
- Ended with a transition to Chapter 4’s four practical moves. Chapter 4 was not edited.
- Hard self-critique: the chapter is direct and operator-focused, and the boundary with Chapter 2 is clear. Its limitation is that no public source reviewed here documents an AI-driven telecom incident; the current speed evidence comes from wider cyber activity, and the SKT case is a traditional breach. The proposed response model is prescriptive, and Oussama should test the composite scenario against NOC/SOC practice. Some frameworks and leadership questions may feel structured. No private conversation or personal experience was invented.
- Strict citation verification passed with evidence quotes for all four cited sources; 11 of 146 prose sentences carry citations (8%). The body is 2,091 words with no em dashes. `git diff --check` passed. Telegram was skipped under the project’s existing waiver.
- Next: stop and wait for author feedback on Chapter 3; do not start Chapter 4.
