# Chapter 4: Four Moves for Service Providers in the Next 12 Months

AI changes the risk. Agents add authority inside the operator. Some threats may move faster than a provider can safely respond. The leadership question is how to respond without putting service continuity at risk.

A separate AI security program is not always needed. Security, network, architecture, supplier and change processes already cover much of the work. The practical question is where AI can act, how much authority it needs, how teams will rehearse a response and what gaps remain.

No sequence will eliminate risk. The value is in checking whether controls work and making residual risk explicit, so leaders can decide whether it fits their risk appetite. The order is useful, but not rigid. If an agent already has broad production access, the operator can limit it while the wider review continues.

## Move 1: Visibility means more than an AI inventory

A model list does not show what the system can do. AI may arrive as a feature in a network-management product, customer-service platform or supplier portal. The feature may use a supplier identity to read service data or trigger a workflow. The product may keep the same name.

Two questions frame the work: **Where can AI reach our systems or data? What actions can it take?** A review can draw on Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation, even when no one calls them AI.

Potential starting points include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. The priority depends on the services at risk. A customer-care summary tool is different from an assistant that can reach network configuration or subscriber records.

A short record can make the difference visible. It can name an owner and purpose, identify the model or supplier, and show the identity, data and tools involved. It can also note affected services, available logs, fallback, relevant markets and who can suspend the use. Unknowns remain visible; they are not marked complete.

In October 2026, TRAI, India’s telecom regulator, published draft guidelines on AI use in telecommunications.[9]
The proposal calls for an inventory of active, inactive and decommissioned systems, with each system’s source, purpose and risk classification.[9]
It also proposes due diligence before third-party AI is acquired or used.[9]
The document is a consultation draft, not a final rule.[9]

The draft does not prescribe a global inventory. It highlights a practical gap: supplier features and product capabilities can escape the project register. Legal and Compliance can confirm what applies in each market.

A practical first step may be to review a few uses that could affect a critical service or sensitive data. Project, procurement, cloud and supplier records can help identify them. Workflow owners can fill in the gaps.

**Composite scenario: supplier feature.** A network-management supplier enables an AI diagnostic feature during a routine update. It is missing from the operator’s project list, but can read topology and propose actions. A review links the feature to its contract, service domain, identity and change process. The first decision need not be to ban it. The team needs a clear owner and evidence about its reach.

Seeing an important use tells the team where to focus. It does not show whether the agent has more authority than its task requires.

## Move 2: Match authority to the task

A system that summarizes public guidance is not the same as an agent that can read subscriber records, open a change request or reach a network-management API. Many operators may begin with the identities and tools that could have the greatest service impact.

The boundary comes down to three things: the data an agent can read, the actions it can take, and how to stop it without stopping the surrounding service.

Where the platform allows it, the agent can use a dedicated identity rather than an employee account or broad shared-service permissions. Access can be limited to the data and tools needed for the task. Time-bounded credentials may help. Logs should show which identity acted, what tool it called and what happened.

The control is only useful if it works in practice. Can the team trace the activity? Can it revoke access without disrupting the monitoring or service-assurance process around the agent? Those are questions of control effectiveness, not policy wording.

It helps to separate “read,” “recommend” and “execute.” Read-only access is often a sensible start. A low-impact, reversible action may fit within clear limits and monitoring. An action that could change production, affect customers or interrupt an essential workflow should stay within the operator’s normal authorization and change process. An agent can prepare the change; people approve and validate it.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses.[10] This is general guidance, not a telco control standard. Legacy platforms and supplier connections matter as much as modern APIs. If a legacy system cannot support a separate identity, a controlled gateway may help. Until then, read-only access may be safer.

In practice, many operators begin by choosing one or two high-impact uses and tracing the identity and tool path. They check whether permissions fit the task, which actions need human approval, and who can revoke access. A test shows whether revocation works without disrupting NOC or service-assurance work.

**Composite scenario: legacy access.** A service-assurance assistant on a legacy OSS platform reads alarms and drafts a maintenance recommendation. The platform cannot issue a separate identity for the assistant. An access gateway limits its read path to one service domain, while write actions stay in the existing change process. Until activity can be traced and revoked, the assistant remains read-only. If it is unavailable, engineers use normal monitoring and approvals. No new failover is introduced during live service.

Permissions matter only if teams can contain a failure without losing the surrounding service. That takes rehearsal.

## Move 3: Rehearsal tests the response before an incident

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

A focused exercise can bring together the SOC and NOC, identity and platform owners, service assurance, change management and business continuity. Legal, communications, procurement and a supplier contact can join when the scenario needs them. A useful scenario centers on a decision that could affect a service.

Possible scenarios include a supplier feature misusing an agent identity, a threat actor steering an assistant through hostile content, or an agent changing a service workflow during a network event. The team can test when to declare an incident, who can revoke access and what evidence to preserve. It can identify which service may lose visibility, what fallback exists and who can authorize an emergency change. Teams can also clarify who handles regulatory and customer notifications while the scope is uncertain.

The Canadian Centre for Cyber Security recommends practising for incidents that may unfold within hours, with isolation steps approved in advance and manual alternatives tested for critical functions.[14] Joint Australian and international guidance warns that external content can carry instructions designed to steer an agent. This is known as indirect prompt injection.[13] These are general recommendations. Operators can test them against their own systems and response roles.

A short rehearsal around one critical service domain can be a low-risk start. It stays separate from live production changes. A note of decisions, owners, missing information and service impact gives the next review something concrete to check.

**Composite scenario: response exercise.** During a planned maintenance window, an assistant reads hostile instructions in a supplier bulletin while analyzing alarms. It proposes a change that could remove visibility from a network domain. The SOC and NOC decide whether the proposed change is approved and who can stop the assistant. They also consider how to preserve the bulletin and logs, and what monitoring remains if they isolate the connector. The same questions apply to a compromised integration or service account.

The rehearsal gives the CISO and CTO evidence about what worked, what was unclear and which service alternative remains untested. That is a stronger basis for funding than a list of tools.

## Move 4: A funded roadmap beats a collection of tools

The first three moves produce evidence about authority, control effectiveness and response gaps. That gives leaders a basis for funding decisions. A credible board paper names the service at risk, the work proposed, its owners, the resources required and the residual risk.

A 12-month roadmap is easier to govern with three or four priorities. Each can name an executive owner, an operational lead, a milestone, supplier and legacy dependencies, maintenance-window limits and the decision needed from leaders. A board case is stronger when the cost of delay is clear in operator terms: customer-data exposure, reduced network control, slower containment, missed regulatory duties or loss of service.

Measures are more useful when they show whether risk is changing, not how many tools were purchased. Evidence can include owners and data paths for high-impact uses, tested access revocation, clear containment authority, exercised service alternatives and closed exercise findings. A tool count can rise while access and response stay the same.

Assurance is more than confirming that a policy exists. It is evidence that controls work under the operator’s service conditions. For high-impact uses, review independent of the delivery team can add confidence, especially when tests reflect real service pressure. Leaders need to see residual risk, compare it with risk appetite, know who accepts it and understand what would trigger review. The aim is not zero risk. It is to show which controls work, where residual risk remains and whether it fits the agreed appetite.

Regulation belongs in this roadmap, but it need not delay action. Legal and Compliance can track binding obligations by market and separate them from consultation drafts. Where duties overlap with identity, supplier assurance, incident reporting or continuity, existing governance may be enough. A separate AI approval board is not always needed.

**At an executive review,** the CISO and CTO can present the priorities, owners, service constraints and evidence gaps. The request might be funding for an identity boundary, time for a continuity test, and regular review of outcomes and residual risk. The paper can make clear what risk leadership accepts until later work is complete.

**Composite scenario: funding decision.** An exercise finds that a supplier identity can reach two operational domains and that one service fallback is untested. The supplier’s patch schedule delays the permanent fix until an agreed window. The CISO and CTO present linked choices: fund an interim identity boundary, test continuity with Network Operations, and name who accepts the residual risk until then. The board sees the trade-off, not just a product request.

## Keep the sequence, adjust the pace

The moves build on one another. Visibility helps the operator choose where to constrain access. Boundaries make the rehearsal realistic, and the exercise shows what may need funding. But the sequence is not a reason to leave excess access in place. A supplier-connected agent with broad production access can be restricted while the wider review continues.

In the near term, many providers can map high-impact uses, review priority identities, rehearse a service scenario and bring an evidence-based choice to executives. Over the coming year, they can extend controls, close exercise gaps and test service alternatives. Leaders should see what changed, what risk remains and who owns it.

The point is not to prove that every AI risk has disappeared. It is to make choices visible and manageable while the network changes. Chapter 5 takes these moves into the boardroom: how to explain the stakes, ask for decisions and win support before an incident makes the case for you.
