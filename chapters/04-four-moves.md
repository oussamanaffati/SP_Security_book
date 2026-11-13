# Chapter 4: Four Moves for Service Providers in the Next 12 Months

An agent can link an OSS query, a service ticket and an operational action through one identity. That changes how far a mistake or compromised tool can travel before a person intervenes. AI may shorten parts of an attacker’s workflow.[14] For a service provider, the challenge is to contain both risks without disrupting service.

Extend existing security, network, architecture, supplier and change processes where they cover the function. Check for gaps where agent identities, tools or supplier features fall outside their controls. Then ask which identities can reach which data or tools, which actions need approval, how NOC and SOC teams will rehearse a response, and what remains uncovered.

No sequence will eliminate risk. The four moves help test controls and make residual risk visible against the operator’s risk appetite.

## Move 1: Visibility means more than an AI inventory

A model list does not show what the system can do. AI may arrive as a feature in a network-management product, customer-service platform or supplier portal. The feature may use a supplier identity to read service data or trigger a workflow. The product may keep the same name.

Two questions frame the work: where can AI reach the operator’s systems or data, and what actions can it take? A review can draw on Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation, even when no one calls them AI.

Prioritize by the live services and network domains an AI use can affect, not by model type. Potential starting points include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. A customer-care summary tool has a different service impact from an assistant that can reach network configuration or subscriber records.

A short record can capture the owner and purpose, model or supplier, identity, data and tools. It can also note affected services, available logs, fallback, relevant markets and who can suspend the use. Record unresolved questions rather than marking them complete.

The Australian Cyber Security Centre’s guidance says asset identification should include AI services, agents, connectors and unsanctioned applications.[25] Supplier review should establish where prompts and outputs are retained, whether customer data is used for training and which regions process it.[25] This is cross-sector guidance; local legal duties still need review.

In October 2026, TRAI, India’s telecom regulator, published draft guidelines on AI use in telecommunications. The consultation proposal calls for an inventory of active, inactive and decommissioned systems, with each system’s source, purpose and risk classification, and due diligence before third-party AI is acquired or used.[9] The document is a consultation draft, not a final rule.

The draft does not prescribe a global inventory. It highlights a practical gap: supplier features and product capabilities can escape the project register. Legal and Compliance can confirm what applies in each market.

A first pass should focus on uses that could affect a critical service or sensitive data. Project, procurement, cloud and supplier records can help find them; workflow owners can clarify the gaps.

**Composite scenario: supplier feature.** A network-management supplier enables an AI diagnostic feature during a routine update. It is missing from the operator’s project list, but can read topology and propose actions. The team assigns an owner, then checks the feature’s contract, service domain, identity and change process. Evidence about its reach supports the decision to restrict or retain it.

Inventory shows where to look. Access review shows whether an agent has more authority than its task requires.

## Move 2: Match authority to the task

The first review should start with high-impact identities and tools. An agent that can read subscriber records, open a change request or reach a network-management API needs tighter control than a system limited to public guidance.

Review three boundaries: which data can the agent read, which actions can it take, and can access be stopped without stopping the surrounding service?

Where the platform allows it, the agent can use a dedicated identity rather than an employee account or broad shared-service permissions. Access can be limited to the data and tools needed for the task. Short-lived credentials issued only when needed may help. Logs should show which identity acted, what tool it called and what happened.

Policy does not prove that a permission boundary works under service conditions. For one or two high-impact uses, follow the agent from its identity to the tools it calls, check that permissions fit the task and verify where a person must approve an action. Then test revocation without disrupting monitoring or service assurance.

Separate “read,” “recommend” and “execute.” Read-only access is often a sensible start. A low-impact, reversible action may fit within clear limits and monitoring. Actions that could change production, affect customers or interrupt an essential workflow should follow the operator’s normal authorization and change process. An agent can prepare a change; an authorized person approves and validates it.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses.[10] This is general guidance, not a telco control standard. Legacy platforms and supplier connections matter as much as modern APIs. If a legacy system cannot support a separate identity, a controlled gateway may help. Until then, read-only access may be safer.

**Composite scenario: legacy access.** A service-assurance assistant on a legacy OSS platform reads alarms and drafts a maintenance recommendation. The platform cannot issue a separate identity for the assistant. An access gateway limits its read path to one service domain, while write actions stay in the existing change process. Until activity can be traced and revoked, the assistant remains read-only. If it is unavailable, engineers use normal monitoring and approvals. No new failover is introduced during live service.

Permissions matter only if teams can contain a failure without losing the surrounding service. That takes rehearsal.

## Move 3: Rehearsal tests the response before an incident

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

Bring the SOC and NOC, identity and platform owners, service assurance, change management and business continuity into the exercise. Legal, communications, procurement and a supplier contact can join when the scenario needs them. Center it on a decision that could affect a service.

Possible scenarios include a supplier feature misusing an agent identity, a threat actor steering an assistant through hostile content, or an agent changing a service workflow during a network event. The team can test when to declare an incident, who can revoke access and what evidence to preserve. It can identify which service may lose visibility, what fallback exists and who can authorize an emergency change. Teams can also clarify who handles regulatory and customer notifications while the scope is uncertain.

The Canadian Centre for Cyber Security recommends practising for incidents that may unfold within hours, with isolation steps approved in advance and manual alternatives tested for critical functions.[14] Joint Australian and international guidance warns that external content can carry instructions designed to steer an agent. This is known as indirect prompt injection.[13] These are general recommendations. Operators can test them against their own systems and response roles.

CISA, FBI and international partners’ September 2026 guidance for service providers emphasizes clear, timely outage communications that preserve operational security and containment.[22] Test who approves an update, when it is sent and which backup channel remains if containment changes service availability.

Test a short rehearsal around one critical service domain, separate from live production changes. Agree service-specific response and recovery tolerances with the service owner before the exercise; one target will not fit every service. Record decisions, elapsed time against each tolerance, service impact, missing information and fallback. The next review can check whether those gaps have closed.

**Composite scenario: response exercise.** During a planned maintenance window, an assistant reads hostile instructions in a supplier bulletin while analyzing alarms. It proposes a change that could remove visibility from a network domain. The SOC and NOC decide whether the proposed change is approved and who can stop the assistant. They also consider how to preserve the bulletin and logs, and what monitoring remains if they isolate the connector. The same questions apply to a compromised integration or service account.

The rehearsal shows the CISO and CTO what worked, what was unclear and which service alternative remains untested. That is a stronger basis for funding than a list of tools.

## Move 4: A funded roadmap beats a collection of tools

The first three moves reveal gaps in authority, control effectiveness and response. Leaders can use those findings to decide what to fund and what risk they can accept. A credible board paper names the service at risk, proposed work, required resources and remaining risk.

A 12-month roadmap is easier to govern with three or four priorities. For each, name an executive owner and an operational lead. Set milestones, dependencies on suppliers or legacy systems, maintenance-window limits and the decision leaders must make. A board case is stronger when the cost of delay is clear in operator terms: customer-data exposure, reduced network control, slower containment, missed regulatory duties or loss of service.

Measures should show whether risk is changing, not how many tools were purchased. Useful indicators include named owners and data paths for high-impact uses, tested access revocation, clear containment authority, exercised service alternatives and closed exercise findings. A tool count can rise while access and response stay the same.

A policy is not proof. For high-impact uses, show that controls work under live-service conditions; an independent review can add confidence. The board needs the evidence, the service impact if controls fail, the accountable executive and the conditions that reopen the decision. Keep acceptance within the operator’s approved risk appetite.

Regulation belongs in this roadmap, but it need not delay action. Legal and Compliance can track binding obligations by market and separate them from consultation drafts. Where duties overlap with identity, supplier assurance, incident reporting or continuity, existing governance may be enough; a separate AI approval board is not always needed.

At an executive review, the CISO and CTO can present the priorities, owners, service constraints and evidence gaps. The request might be funding for an identity boundary, time for a continuity test, and regular review of outcomes and residual risk. The paper should identify which accountable service executive accepts the remaining risk until later work is complete.

**Composite scenario: funding decision.** An exercise finds that a supplier identity can reach two operational domains and that one service fallback is untested. The supplier’s patch schedule delays the permanent fix until an agreed window. The CISO and CTO present linked choices: fund an interim identity boundary, test continuity with Network Operations, and name who accepts the residual risk until then. The board sees the trade-off, not just a product request.

## Keep the sequence, adjust the pace

At the end, the CISO and CTO should be able to show a service-linked inventory, tested access limits, exercise evidence of decisions and gaps, and a funded plan with named owners for residual risk. Restrict excessive production access as soon as the risk is clear; the wider review need not wait. Chapter 5 turns those findings into an executive decision.
