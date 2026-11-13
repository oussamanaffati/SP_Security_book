# Chapter 4: Four Moves Every Service Provider Should Start in the Next 12 Months

Chapters 1 to 3 establish the case: AI changes the risk, agents add authority inside an operator, and some threats may move faster than a service provider can safely respond. The leadership question is what to do first without disrupting services or building a parallel AI program.

One practical sequence is: **see where high-impact AI can act, limit that authority, rehearse the response, and fund the gaps that remain.** In practice, many operators will use existing security, network, architecture, supplier and change processes. A new committee or tool adds value only if it improves control effectiveness or assurance.

Each move can begin within 90 days. The first milestone need not be a complete AI inventory. A risk-based view of uses most likely to affect a critical service or sensitive data can guide the next step. The aim is not zero risk. It is to reduce exposure, understand residual risk and make choices within the operator’s risk appetite.

## Move 1: See what can act, not just what is called AI

For many operators, a complete AI inventory is not a practical first milestone. A model list can miss what matters operationally: a vendor feature may use a supplier identity, read service data or trigger a workflow. Two questions frame the review: “Where is AI?” and “Which AI-enabled use can reach sensitive systems or data, or trigger a service change?”

A review can draw on Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation even when it is not marketed as AI. Potential starting points include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access.

For each high-impact use, keep a short record: its business and technical owners, purpose, model or supplier, identity, data and tools, actions available, and services it could affect. Also note available logs, relevant jurisdictions, fallback options and who can suspend it. Keep unknowns visible. That is more honest than a false “complete” status.

In October 2026, India’s TRAI published draft guidelines on AI use in telecommunications.[9]
The proposal calls for an inventory of active, inactive and decommissioned systems, including their source, purpose and risk classification. It also proposes due diligence before third-party AI is acquired or used.[9]
The document is a consultation draft, not a final binding rule.[9]
The point is not to copy the proposed form. It is to include suppliers and less-visible product features in the operator’s view, while Legal tracks which requirements apply in each market.

**First 90 days:** the CISO and CTO can name an executive sponsor and operational lead, agree the record fields, and start with existing project, procurement, cloud and supplier information. Interviews can focus on workflows that touch production or sensitive data. By day 90, aim for a prioritized register with owners and dates for key unknowns. Counts alone do not show security progress.

**Supplier example (composite).** A network-management supplier enables an AI diagnostic feature during a routine update. The feature is absent from the AI project list, yet it reads topology and proposes actions. A cross-functional review links it to the supplier contract, service domain, identity and change process. The decision is not automatically to ban it. First establish its owner and evidence before expanding it.

## Move 2: Limit the authority before increasing the use

Once the operator knows which uses matter, the next step is to match authority to the task. A system that summarizes public guidance is not equivalent to an agent that can read subscriber records, open a change request or reach a network-management API. Many operators may get more value by reviewing the highest-impact identities and tools first, rather than treating every model as an equal risk.

Three questions define the control boundary: **What may it read? What may it change or trigger? How can the operator stop it without stopping the service around it?** Where the platform supports it, give the use a dedicated identity. Avoid borrowed employee accounts and broad shared-service permissions. Limit data and tools to the task, use time-bounded credentials where available, and log the identity, tool call and result. Then test control effectiveness: can the team trace activity and revoke access without disrupting service?

It helps to separate “read,” “recommend” and “execute.” Read-only access is often a prudent starting point for a new use. A low-impact, reversible change may be acceptable within a defined boundary and with monitoring. For actions that could alter a production network, affect customers or interrupt an essential workflow, the operator’s normal authorization and change process remains important. An agent can prepare a change package while people retain approval and validation.

CISA and its international partners advise organizations to avoid broad or unrestricted agent access, especially to sensitive data and critical systems, and to begin with low-risk, non-sensitive use cases.[10]
That is a general starting point, not a telco control standard. In a service provider, the access boundary has to include legacy platforms and vendor connections as well as modern APIs. If a legacy system cannot support a separate agent identity, a controlled gateway or narrow intermediary may provide a safer path. Until then, read-only access may be the prudent boundary.

**Access review in the first 90 days:** the team can select one or two uses from the register and trace the identity and tool path. Check permissions against the task and remove excess access. The review should clarify which actions need human approval, what is logged and who can revoke access. A revocation test can confirm that the NOC or service-assurance process still works. Extend the review when the first controls work as intended.

**Legacy access example (composite).** A service-assurance assistant on a legacy platform retrieves alarms and drafts a maintenance recommendation. It does not need permission to change network configuration. A dedicated identity limits it to one service domain; any write action follows the existing change process. If the assistant is unavailable, engineers keep their normal monitoring and approval path. This tightens access without adding an untested failover to a live service.

## Move 3: Rehearse the incident before the real one

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

A realistic exercise brings together the SOC, NOC, identity and platform owners, service assurance, change management, business continuity, legal or regulatory leads, communications, procurement and a supplier contact who can respond during an incident. One scenario is enough if the service impact is clear. For example, a supplier feature misuses an agent identity, a threat actor attempts to steer an assistant through hostile content, or an agent changes a customer or service workflow during a network event.

The exercise can test a practical set of decisions. What signal is enough to declare an incident? Who can revoke a credential or disable a connector? What evidence must be preserved first? Which service could lose visibility or function if the path is isolated? What safe manual or alternative operation is available? Who can authorize an emergency change outside the usual window? Which regulatory and customer notifications can proceed while technical scope is still being confirmed?

The Canadian Centre for Cyber Security recommends practising for incidents that unfold within hours rather than days.[14]
Its critical-infrastructure guidance also calls for pre-authorized isolation procedures, identifying essential functions and testing manual or alternative operation.[14]
Joint Australian and international guidance warns that external content can carry instructions designed to steer an agent.[13]
This is known as indirect prompt injection.[13]
These are not telecom-specific prescriptions, but they give the exercise concrete failure modes to test against the provider’s own architecture.

**A two-hour tabletop in the first 90 days:** it can focus on one critical service domain and stay separate from live production changes. Record each decision, its owner, the information missing and the service consequence. Within 30 days, each high-priority gap can have an owner and due date. Before year-end, repeat the scenario with senior decision-makers or test a control safely in a non-production environment.

**Exercise scenario (composite).** During a planned maintenance window, an assistant encounters hostile instructions in a supplier bulletin while analyzing alarms. It proposes a change that could remove visibility from a network domain. The exercise tests whether SOC and NOC can distinguish the signal from approved work, who can stop the assistant, how to preserve the bulletin and logs, and what monitoring remains if the connector is isolated. Similar decisions apply to a compromised integration or service account, even before an operator puts an agent into production.

## Move 4: Fund the roadmap, not a collection of tools

The first three moves produce evidence: what has authority, which controls are missing, and where response decisions break down. That evidence can support executive choices. A credible board paper explains which service or obligation is exposed, what the operator proposes to do, who owns the work, what it requires in people and change capacity, and what residual risk remains. “AI is a risk” or “we need a platform” is not enough.

A 12-month roadmap is easier to govern when it focuses on three or four priorities rather than twenty disconnected actions. For each, identify an accountable executive, an operational owner, the first milestone, legacy or supplier dependencies (including patch schedules), the service or change-window constraint, and the decision needed from leadership. Describe the potential consequence of deferral in operator terms: customer-data exposure, reduced ability to manage the network, delayed containment, a missed regulatory duty or loss of service continuity. If the evidence supports a service or risk statement but not a monetary estimate, keep the case at that level.

Measures matter when they show risk reduction and control effectiveness. Evidence might show whether high-impact uses have named owners and known data paths; whether priority identities can be revoked in a test; whether containment decisions are pre-authorized; whether continuity alternatives have been exercised; and whether exercise findings are closed. A tool count can rise while access and response remain unchanged.

Assurance means more than confirming that a policy exists. It means having evidence that the control works under the operator’s service conditions. The board or executive committee should also see the residual risk, how it compares with the organization’s risk appetite, who accepts it, and what change would trigger a review.

Regulation belongs in this roadmap, but it should not become a reason to wait. A practical approach is to track binding obligations by jurisdiction with Legal and Compliance, and treat consultation drafts as signals to monitor, not as law. Where requirements overlap with identity, supplier assurance, incident reporting or continuity, an operator can extend existing governance rather than create a parallel AI approval board.

**At an executive review in the first 90 days:** the CISO and CTO can take a one-page, evidence-based proposal to the risk committee. It can ask for a named sponsor, agreement on priorities, protected time for cross-team work, and quarterly review of outcomes and residual risk. The paper should state what needs funding, which service constraints shape the sequence, and what risk leadership accepts until later phases are complete.

**Funding example (composite).** A provider’s first exercise finds that a supplier identity can reach two operational domains and that the fallback for one service has not been tested. The supplier’s patch schedule means a permanent change must wait for the next agreed window. The CISO and CTO present linked choices, not a request for an AI security product: fund an interim identity boundary, schedule a continuity test with Network Operations, and name who accepts the residual risk until the permanent change. The board can see the trade-off and assign ownership.

## Keep the sequence, adjust the pace

These moves build on one another. Visibility helps the operator choose where to constrain access. Access boundaries make the exercise realistic. The exercise shows what may need funding. The sequence should not become a reason to leave obvious excess access in place until an inventory is complete. If a supplier-connected agent already has broad production access, the operator can limit that access while the wider review continues.

The first 90 days can establish the register, review access for one or two high-impact uses, run a tabletop and bring one roadmap decision to executives. Over the next two quarters, the operator can extend controls, close exercise gaps and test service alternatives. By month twelve, leadership should see the decisions made, risk reduced, open gaps and their owners.

The point is not to prove that every AI risk has disappeared. It is to make the operator’s choices visible and manageable while transformation continues. Chapter 5 takes the same four moves into the boardroom: how to explain the stakes, ask for the right decisions and win support before the next incident makes the argument for you.

## Sources

[9] https://trai.gov.in/sites/default/files/2026-10/Draft_CP_30102026.pdf — TRAI Draft Guidelines on Responsible Use of AI in Telecommunication Networks, 30 October 2026
[10] https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai — Careful Adoption of Agentic AI Services, CISA and international partners, 1 May 2026
[13] https://www.cyber.gov.au/sites/default/files/2026-05/careful_adoption_of_agentic_ai_services.pdf — Careful Adoption of Agentic AI Services, joint ASD ACSC and partner agencies report, 1 May 2026
[14] https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-agentic-artificial-intelligence-accelerating-cyber-attacks — Cyber threat bulletin: Agentic artificial intelligence is accelerating cyber attacks, Canadian Centre for Cyber Security, 26 October 2026
