# Chapter 4: Four Moves Every Service Provider Should Start in the Next 12 Months

Chapters 1 to 3 made the case: AI changes the risk, agents add authority inside the operator, and threats can move faster than a service provider can safely respond. The next question is practical. What should a CISO and CTO do first?

The answer is not to launch four new committees or buy four new tools. It is to make four moves in sequence: **see where consequential AI can act, limit that authority, rehearse what happens when it goes wrong, and secure funding for the risks that remain.** The work should fit existing security, network, architecture, supplier and change processes. A new label does not improve security if the same teams still cannot see the same risk.

Each move can start in the next 90 days. The first output is deliberately modest: an agreed view of the highest-consequence uses, not a claim that every AI feature has been found. From there, the operator can test controls, exercise response and make an informed investment case.

## Move 1: See what can act, not just what is called AI

Start with visibility, but do not wait for a perfect inventory. A spreadsheet listing model names will miss the important part: an assistant embedded in a vendor product may have a supplier identity, access to service data and the ability to trigger a workflow. The question is not only “Where is AI?” It is “Which AI-enabled use can reach a sensitive system, data set or service-changing tool?”

The CISO and CTO should sponsor a short, cross-functional discovery. Ask Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers for the AI-enabled features and agent workflows they already use or plan to activate. Include pilots, SaaS features and automation that is not marketed as AI. In a carrier environment, begin with OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access.

For each consequential use, record a small set of fields: business owner; technical owner; purpose; model or supplier; machine identity; data it can read; tools it can call; actions it can take; network or customer services it could affect; logs available; jurisdiction; fallback; and the person who can suspend it. Mark unknown fields as unknown. An honest gap is more useful than a false “complete” status.

In October 2026, India’s TRAI published draft guidelines that propose an inventory of active, inactive and decommissioned AI systems, including source, purpose and risk classification, and due diligence before third-party AI is acquired or used.[9]
The document is a consultation draft, not a final binding rule.[9]
The useful lesson is not to copy its proposed form. It is to make suppliers and less-visible product features part of the operator’s view, while Legal tracks which requirements actually apply in each market.

**Start in the next 90 days:** name an executive sponsor and an operational lead; agree the fields above; gather existing project, procurement, cloud and supplier records; then interview the owners of the few workflows most likely to touch production or sensitive data. By day 90, review a prioritized register with named owners and dates for closing the most important unknowns. Do not report an inventory count as a security outcome.

**Composite illustration.** A network-management supplier enables an AI diagnostic feature as part of a routine software update. The operator’s AI project list does not include it, but the feature can read topology and create recommended actions. A cross-functional review connects the feature to its supplier contract, service domain, identity and change workflow. The finding is not “ban it.” It is “this use is consequential, here is its owner, and here are the decisions we need before expanding it.”

## Move 2: Limit the authority before increasing the use

Once the operator knows which uses matter, reduce the authority they carry. Start with the highest-consequence identities and tools, not every model at once. A system that can only summarize public guidance is not equivalent to an agent that can read subscriber records, open a change request or reach a network-management API.

For each priority use, answer three questions. **What may it read? What may it change or trigger? How do we stop it without stopping the service around it?** Give the agent a distinct identity. Do not let it borrow an employee’s account or inherit the full rights of a shared service account. Limit data and tools to the task. Use time-bounded credentials where the platform supports them. Log the identity, tool call and result so an operator can reconstruct what happened.

Separate “read,” “recommend” and “execute.” Read-only access should be the starting point for a new use. Where the agent can make a low-impact, reversible change, define that boundary and monitor it. Where an action could alter a production network, affect customers or interrupt an essential workflow, keep the operator’s existing authorization and change process. An agent can prepare a change package; it should not quietly bypass the people who approve and validate a network change.

CISA and its international partners advise organizations to avoid broad or unrestricted agent access, especially to sensitive data and critical systems, and to begin with low-risk, non-sensitive use cases.[10]
That is a general starting point, not a telco control standard. In a service provider, the access boundary has to include legacy platforms and vendor connections as well as modern APIs. If a legacy system cannot support a separate agent identity, put a controlled gateway or a narrow intermediary in front of it, or keep the use read-only until a safer path exists.

**Start in the next 90 days:** select one or two uses from the priority register. Trace their actual identity and tool path, test whether the permissions match the stated task, and remove access they do not need. Agree which actions can be pre-approved, which require a person, what evidence is logged, and who can revoke access. Test the revocation and confirm that the remaining NOC or service-assurance process still works. Repeat across the next tier only after the first controls are operating.

**Composite illustration.** A legacy service-assurance assistant can retrieve alarms and draft a maintenance recommendation, but it does not need permission to change a network configuration. The operator assigns a dedicated identity with access to one service domain and routes write actions through the existing change workflow. If the assistant becomes unavailable, engineers retain their normal monitoring and approval path. Security improves without asking the network team to accept an untested failover.

## Move 3: Rehearse the incident before the real one

A policy does not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. The exercise should be about decisions and service impact, not a demonstration of an AI product.

Bring together the SOC, NOC, identity and platform owners, service assurance, change management, business continuity, legal or regulatory leads, communications, procurement and the supplier contact who would actually answer during an incident. Use one plausible scenario with a clear operational stake: a supplier feature misuses an agent identity; hostile content steers a tool-using assistant; or an agent changes a customer or service workflow during a network event.

Make the team decide what it will do. What signal is enough to declare an incident? Who can revoke a credential or disable a connector? Which evidence must be preserved first? What service could lose visibility or function if the path is isolated? What safe manual or alternative operation is available? Who authorizes an emergency change outside the usual window? Which regulatory and customer notifications can proceed while technical scope is still being confirmed?

The Canadian Centre for Cyber Security recommends practising for incidents that unfold within hours rather than days.[14]
Its critical-infrastructure guidance also calls for pre-authorized isolation procedures, identifying essential functions and testing manual or alternative operation.[14]
Joint Australian and international guidance warns that content from external sources can introduce indirect prompt-injection attacks into an agent’s context.[13]
These are not telecom-specific prescriptions, but they give the exercise concrete failure modes to test against the provider’s own architecture.

**Start in the next 90 days:** choose one critical service domain and run a two-hour tabletop. Do not make live changes to production. Capture each decision, the owner, the information missing and the service consequence. Within 30 days of the exercise, assign an owner and due date to each high-priority gap. Before the end of the year, repeat the scenario with senior decision-makers or test a safe technical control in a non-production environment.

**Composite illustration.** During a planned maintenance window, a trusted supplier bulletin includes hostile instructions that an agent reads while analyzing alarms. The agent proposes a change that could remove visibility from a network domain. The exercise tests whether SOC and NOC can distinguish the signal from approved work, who can stop the agent, how to preserve the bulletin and agent logs, and what monitoring remains if the connector is isolated. The exercise is useful even if the operator has no production agent today; the same decisions apply to a compromised integration or service account.

## Move 4: Fund the roadmap, not a collection of tools

The first three moves produce evidence: what has authority, which controls are missing, and where response decisions break down. Use that evidence to ask executives for decisions. A board paper should not say only “AI is a risk” or “we need a platform.” It should explain what service or obligation is exposed, what the operator will do, who owns it, what it costs in people and change capacity, and what residual risk remains.

Build a 12-month roadmap with three or four priorities, not twenty disconnected actions. For each, show an accountable executive, an operational owner, the first milestone, dependencies on legacy or suppliers, the change window or service constraint, and the decision needed from leadership. Include the cost of doing nothing in operator terms: exposure of customer data, reduced ability to manage the network, delayed containment, a missed regulatory duty or loss of service continuity. Do not invent a monetary estimate when the evidence supports only a service or risk statement.

Keep measures tied to risk reduction. Useful evidence includes whether the highest-consequence uses have named owners and known data paths; whether priority identities have been tested and can be revoked; whether containment decisions are pre-authorized; whether continuity alternatives have been exercised; and whether remediation actions from exercises are closed. “Number of AI tools deployed” is a poor success measure. It can rise while access and response remain unchanged.

Regulation belongs in this roadmap, but it should not become a reason to wait. Track binding obligations by jurisdiction with Legal and Compliance. Treat consultation drafts as signals to monitor, not as law. Where requirements overlap with identity, supplier assurance, incident reporting or continuity, extend the existing governance process instead of creating a parallel AI approval board.

**Start in the next 90 days:** the CISO and CTO should jointly take a one-page, evidence-based proposal to the executive risk committee. Ask for a named sponsor, agreement on the first three or four priorities, protected staff time for cross-team work, and a quarterly review of outcomes and residual risk. Put the board’s specific decisions on the page: what it is being asked to fund, which service constraints shape the sequence, and what risk leadership is accepting until later phases are complete.

**Composite illustration.** A provider’s first exercise reveals that a supplier identity can reach two operational domains and that the fallback for one service has not been tested. The CISO and CTO present those as linked decisions, not as a request to buy an AI security product: fund the identity boundary now, schedule a continuity test with Network Operations, and accept a documented residual risk for the second domain until its maintenance window. The board can then see the trade-off and assign ownership.

## Keep the sequence, adjust the pace

These moves build on one another. Visibility gives the operator a basis for choosing where to constrain access. Access boundaries make the exercise realistic. The exercise exposes what needs funding. But the sequence is not an excuse to leave an obvious risk untouched until a full inventory is complete. If a supplier-connected agent already has broad production access, limit it while the broader review continues.

In the first 90 days, start the register, select one or two high-consequence uses for access review, run one tabletop and put the first roadmap decision in front of executives. Over the next two quarters, extend the controls, close the exercise gaps and test service alternatives. By month twelve, leadership should be able to point to decisions made, risk reduced, gaps still open and owners for each.

The point is not to prove that every AI risk has disappeared. It is to make the operator’s choices visible and manageable while transformation continues. Chapter 5 takes the same four moves into the boardroom: how to explain the stakes, ask for the right decisions and win support before the next incident makes the argument for you.

## Sources

[9] https://trai.gov.in/sites/default/files/2026-10/Draft_CP_30102026.pdf — TRAI Draft Guidelines on Responsible Use of AI in Telecommunication Networks, 30 October 2026
[10] https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai — Careful Adoption of Agentic AI Services, CISA and international partners, 1 May 2026
[13] https://www.cyber.gov.au/sites/default/files/2026-05/careful_adoption_of_agentic_ai_services.pdf — Careful Adoption of Agentic AI Services, joint ASD ACSC and partner agencies report, 1 May 2026
[14] https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-agentic-artificial-intelligence-accelerating-cyber-attacks — Cyber threat bulletin: Agentic artificial intelligence is accelerating cyber attacks, Canadian Centre for Cyber Security, 26 October 2026
