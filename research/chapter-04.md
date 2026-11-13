# Chapter 4 research notes — 13 November 2026

## Scope

Chapter 4 turns the book’s earlier findings into a sequenced, operator-owned 12-month agenda. Research focused on government guidance and telecom-specific regulatory signals relevant to inventory, third-party use, access boundaries, incident rehearsal, service continuity and executive oversight. The cited guidance is not presented as proof of how every telco currently operates.

## Sources used

1. **Telecom Regulatory Authority of India (TRAI), Draft Guidelines on Responsible Use of AI in Telecommunication Networks (published for consultation 30 October 2026).** Primary telecom regulator proposal. It proposes an inventory covering active, inactive and decommissioned AI systems, with source, purpose and risk classification; it also proposes due diligence before third-party AI is acquired or used. The chapter identifies this as a draft consultation, not a final or universally applicable obligation. It uses the proposal as a current regulatory signal for visibility and supplier review. Source [9]: https://trai.gov.in/sites/default/files/2026-10/Draft_CP_30102026.pdf.

2. **CISA and international partners, “Careful Adoption of Agentic AI Services” (1 May 2026).** Primary multi-agency guidance. It advises organizations to avoid broad or unrestricted agent access, especially to sensitive data and critical systems, and to begin with low-risk, non-sensitive use cases. The chapter uses this as general guidance, then applies it to service-provider identities, legacy platforms and change controls. It is not a telecom-specific control standard. Source [10]: https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai.

3. **Joint ASD ACSC and partner agencies, “Careful Adoption of Agentic AI Services” (May 2026, PDF).** Primary public-sector guidance. It explains that external content, including web-search results, can enter an agent’s prompt context and enable indirect prompt injection. The chapter uses this as a failure mode for a composite incident exercise, not as a claim that a telco incident occurred. Source [13]: https://www.cyber.gov.au/sites/default/files/2026-05/careful_adoption_of_agentic_ai_services.pdf.

4. **Canadian Centre for Cyber Security, “Cyber threat bulletin: Agentic artificial intelligence is accelerating cyber attacks” (date modified 26 October 2026).** Primary government guidance. It recommends practising for incidents that unfold within hours rather than days. Its critical-infrastructure advice includes pre-authorized isolation procedures, identifying essential functions, and testing safe manual or alternative operation. The chapter applies these recommendations to service-provider rehearsal while retaining local network authority and continuity constraints. The bulletin is not a telco incident report. Source [14]: https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-agentic-artificial-intelligence-accelerating-cyber-attacks.

## Chapter decisions and boundaries

- Sequenced the four moves as visibility, authority reduction, rehearsal, and funded governance. The order makes each move produce evidence the next can use, but obvious excess access should be reduced immediately rather than waiting for a complete inventory.
- Replaced fixed 90-day milestones with measured near-term language. The four moves remain bounded and sequenced, with the 12-month roadmap focused on named owners, tested access and recovery controls, and closed exercise gaps rather than tool counts.
- Kept the initial register consequence-based: identity, data, tools, supplier, service impact, jurisdiction, logs and suspension path. Used the TRAI consultation draft as a dated signal only, not as binding global regulation.
- Added one clearly labeled composite illustration to each move. The examples are constructed; none is presented as an operator incident or private customer conversation.
- Explicitly covered legacy limitations, existing change processes, NOC/SOC and other team coordination, jurisdiction-specific regulatory duties, maintenance windows and service continuity.
- Closed with a transition to Chapter 5’s board-level case. Chapter 5 was not drafted or edited.

## Self-critique

The revision keeps the four moves and four clearly labeled composite scenarios while replacing fixed 90-day urgency with a measured near-term sequence. The language is shorter, and the transitions now connect visibility, authority, rehearsal and funding. Risk appetite, control effectiveness, residual risk and assurance are explicit; a recommendation for independent review of high-impact uses is presented as advice, not as a cited requirement. The main limitation is evidence: only the TRAI consultation is telecom-specific, while the other sources are cross-sector guidance. The examples are illustrative, not reported operator incidents. The four-move structure remains deliberately organized, but its repeated scenario labels may still feel formulaic. No private conversation or personal experience is presented as fact.
