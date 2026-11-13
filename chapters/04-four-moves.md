# Chapter 4: Four Moves for Service Providers in the Next 12 Months

An agent can link an OSS query, a service ticket and an operational action through one identity. That changes how far a mistake or compromised tool can travel before a person intervenes. AI can also compress parts of an attacker’s workflow.[14] For a service provider, the challenge is to contain both risks without disrupting service.

Operators can often extend existing security, network, architecture, supplier and change processes rather than create a separate AI program. The practical questions are which identities can reach which data or tools, which actions need approval, how NOC and SOC teams will rehearse a response, and what gaps remain.

No sequence will eliminate risk. The four moves help test controls and make residual risk visible against the operator’s risk appetite. They are a guide, not a reason to delay action: broad production access can be restricted while the wider review continues.

## Move 1: Visibility means more than an AI inventory

A model list does not show what the system can do. AI may arrive as a feature in a network-management product, customer-service platform or supplier portal. The feature may use a supplier identity to read service data or trigger a workflow. The product may keep the same name.

Two questions frame the work: where can AI reach the operator’s systems or data, and what actions can it take? A review can draw on Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation, even when no one calls them AI.

Potential starting points include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. The priority depends on the services at risk. A customer-care summary tool has a different service impact from an assistant that can reach network configuration or subscriber records.

A short record can capture the owner and purpose, model or supplier, identity, data and tools. It can also note affected services, available logs, fallback, relevant markets and who can suspend the use. Record unresolved questions rather than marking them complete.

In October 2026, TRAI, India’s telecom regulator, published draft guidelines on AI use in telecommunications. The consultation proposal calls for an inventory of active, inactive and decommissioned systems, with each system’s source, purpose and risk classification, and due diligence before third-party AI is acquired or used.[9] The document is a consultation draft, not a final rule.

The draft does not prescribe a global inventory. It highlights a practical gap: supplier features and product capabilities can escape the project register. Legal and Compliance can confirm what applies in each market.

A first pass should focus on uses that could affect a critical service or sensitive data. Project, procurement, cloud and supplier records can help find them; workflow owners can clarify the gaps.

**Composite scenario: supplier feature.** A network-management supplier enables an AI diagnostic feature during a routine update. It is missing from the operator’s project list, but can read topology and propose actions. The team assigns an owner, then checks the feature’s contract, service domain, identity and change process. Evidence about its reach supports the decision to restrict or retain it.

Seeing an important use tells the team where to focus. It does not show whether the agent has more authority than its task requires.

## Move 2: Match authority to the task

A system that summarizes public guidance has a different risk from an agent that can read subscriber records, open a change request or reach a network-management API. A useful first review focuses on identities and tools with the greatest potential service impact.

The boundary comes down to three things: the data an agent can read, the actions it can take, and how to stop it without stopping the surrounding service.

Where the platform allows it, the agent can use a dedicated identity rather than an employee account or broad shared-service permissions. Access can be limited to the data and tools needed for the task. Short-lived or just-in-time credentials may help. Logs should show which identity acted, what tool it called and what happened.

The control matters only if it works in practice. Can the team trace activity and revoke access without disrupting monitoring or service assurance? These are tests of control effectiveness, not questions answered by policy wording.

Separate “read,” “recommend” and “execute.” Read-only access is often a sensible start. A low-impact, reversible action may fit within clear limits and monitoring. Actions that could change production, affect customers or interrupt an essential workflow should follow the operator’s normal authorization and change process. An agent can prepare a change; an authorized person approves and validates it.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses.[10] This is general guidance, not a telco control standard. Legacy platforms and supplier connections matter as much as modern APIs. If a legacy system cannot support a separate identity, a controlled gateway may help. Until then, read-only access may be safer.

For one or two high-impact uses, trace the identity and tool path. Check whether permissions fit the task, which actions need human approval, and who can revoke access. Test revocation without disrupting NOC or service-assurance work.

**Composite scenario: legacy access.** A service-assurance assistant on a legacy OSS platform reads alarms and drafts a maintenance recommendation. The platform cannot issue a separate identity for the assistant. An access gateway limits its read path to one service domain, while write actions stay in the existing change process. Until activity can be traced and revoked, the assistant remains read-only. If it is unavailable, engineers use normal monitoring and approvals. No new failover is introduced during live service.

Permissions matter only if teams can contain a failure without losing the surrounding service. That takes rehearsal.

## Move 3: Rehearsal tests the response before an incident

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

Bring the SOC and NOC, identity and platform owners, service assurance, change management and business continuity into the exercise. Legal, communications, procurement and a supplier contact can join when the scenario needs them. Center it on a decision that could affect a service.

Possible scenarios include a supplier feature misusing an agent identity, a threat actor steering an assistant through hostile content, or an agent changing a service workflow during a network event. The team can test when to declare an incident, who can revoke access and what evidence to preserve. It can identify which service may lose visibility, what fallback exists and who can authorize an emergency change. Teams can also clarify who handles regulatory and customer notifications while the scope is uncertain.

The Canadian Centre for Cyber Security recommends practising for incidents that may unfold within hours, with isolation steps approved in advance and manual alternatives tested for critical functions.[14] Joint Australian and international guidance warns that external content can carry instructions designed to steer an agent. This is known as indirect prompt injection.[13] These are general recommendations. Operators can test them against their own systems and response roles.

Test a short rehearsal around one critical service domain, separate from live production changes. Record each decision, owner, service impact, missing information and fallback; the next review can check whether those gaps have closed.

**Composite scenario: response exercise.** During a planned maintenance window, an assistant reads hostile instructions in a supplier bulletin while analyzing alarms. It proposes a change that could remove visibility from a network domain. The SOC and NOC decide whether the proposed change is approved and who can stop the assistant. They also consider how to preserve the bulletin and logs, and what monitoring remains if they isolate the connector. The same questions apply to a compromised integration or service account.

The rehearsal shows the CISO and CTO what worked, what was unclear and which service alternative remains untested. That is a stronger basis for funding than a list of tools.

## Move 4: A funded roadmap beats a collection of tools

The first three moves reveal gaps in authority, control effectiveness and response. Leaders can use those findings to decide what to fund. A credible board paper names the service at risk, proposed work, owners, required resources and remaining risk.

A 12-month roadmap is easier to govern with three or four priorities. Each can name an executive owner, an operational lead, a milestone, supplier and legacy dependencies, maintenance-window limits and the decision needed from leaders. A board case is stronger when the cost of delay is clear in operator terms: customer-data exposure, reduced network control, slower containment, missed regulatory duties or loss of service.

Measures should show whether risk is changing, not how many tools were purchased. Useful indicators include named owners and data paths for high-impact uses, tested access revocation, clear containment authority, exercised service alternatives and closed exercise findings. A tool count can rise while access and response stay the same.

Assurance means showing that controls work under the operator’s service conditions, not only that a policy exists. For high-impact uses, an independent review can add confidence, especially when tests reflect real service pressure. Leaders need to see residual risk, compare it with risk appetite, know who accepts it and understand what would trigger review. The aim is to show which controls work, where risk remains and whether it fits the agreed appetite.

Regulation belongs in this roadmap, but it need not delay action. Legal and Compliance can track binding obligations by market and separate them from consultation drafts. Where duties overlap with identity, supplier assurance, incident reporting or continuity, existing governance may be enough; a separate AI approval board is not always needed.

**At an executive review,** the CISO and CTO can present the priorities, owners, service constraints and evidence gaps. The request might be funding for an identity boundary, time for a continuity test, and regular review of outcomes and residual risk. The paper should identify which accountable service executive accepts the remaining risk until later work is complete.

**Composite scenario: funding decision.** An exercise finds that a supplier identity can reach two operational domains and that one service fallback is untested. The supplier’s patch schedule delays the permanent fix until an agreed window. The CISO and CTO present linked choices: fund an interim identity boundary, test continuity with Network Operations, and name who accepts the residual risk until then. The board sees the trade-off, not just a product request.

## Keep the sequence, adjust the pace

Visibility guides access limits, and rehearsals expose gaps that may need funding. If a supplier-connected agent already has broad production access, restricting it need not wait for the wider review.

In the near term, providers can map high-impact uses, review priority identities, rehearse a service scenario and bring a clear choice to executives. Over the coming year, they can extend controls, close exercise gaps and test service alternatives. Leaders should see what changed, what risk remains and who owns it.

Take the four moves to the board with named owners, service constraints, tested controls and an explicit residual-risk decision. Chapter 5 explains how to make that case and secure the decisions needed to act.
