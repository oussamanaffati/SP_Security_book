# Chapter 4: Four Moves for Service Providers in the Next 12 Months

The same identity may connect an OSS query, a service ticket and an operational action. That shortens the path between information and change, but it can also let a mistake or compromised tool travel farther before a person intervenes. Some cross-sector evidence suggests AI can shorten parts of an attacker’s workflow.[14] For a service provider, the task is to contain both risks without putting continuity at odds with security.

Existing security, network, architecture, supplier and change processes provide a natural starting point. The review is about where agent identities, tools or supplier features fall outside them: which identities can reach which data or tools, which actions need approval, how NOC and SOC teams will rehearse a response, and what remains uncovered.

The sequence is useful because each move answers a different question. Visibility shows where authority exists. Access review tests whether it matches the task. Rehearsal reveals whether the operator can contain failure and maintain service. The roadmap gives owners and resources to close the gaps. These activities can overlap. Where excessive access is already evident, there is little value in waiting for the full inventory before considering a proportionate restriction.

No sequence will eliminate risk. The four moves help test controls and make residual risk visible against the operator’s risk appetite.

## Move 1: Visibility means more than an AI inventory

A model list does not show what the system can do. AI may arrive as a feature in a network-management product, customer-service platform or supplier portal. The feature may use a supplier identity to read service data or trigger a workflow. The product may keep the same name.

Two questions frame the work: where can AI reach the operator’s systems or data, and what actions can it take? A joint review can bring together Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation, even when no one calls them AI.

A service-first review is more useful than a model-first list. The relevant areas include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. A customer-care summary tool has a different service impact from an assistant that can reach network configuration or subscriber records.

A concise record can capture the owner and purpose, model or supplier, identity, data and tools, affected services, available logs, fallback, relevant markets and who can suspend the use. Open questions should remain visible rather than being marked complete.

An inventory becomes useful when it links a capability to its service owner, data, identity and available actions. A product count alone will not show that. A supplier feature may change through an update even when the product name stays the same. Release notices, procurement reviews and architecture changes can feed the same inventory, so the register remains useful after the initial discovery. When the supplier cannot explain the feature’s identity or reach, that uncertainty is a risk to resolve or explicitly accept, not a reason to mark the entry complete.

The Australian Cyber Security Centre’s October 2026 guidance calls for AI asset identification to include services, agents, connectors and unsanctioned applications.[25] It also recommends checking what providers retain in prompts and outputs, whether customer data is used to train models, and where processing occurs.[25] This is cross-sector guidance; local legal duties still need review.

In October 2026, TRAI, India’s telecom regulator, published draft guidelines on AI use in telecommunications. The consultation proposal calls for an inventory of active, inactive and decommissioned systems, with each system’s source, purpose and risk classification, and due diligence before third-party AI is acquired or used.[9] The document is a consultation draft, not a final rule.

The draft does not prescribe a global inventory. It highlights a practical gap: supplier features and product capabilities can escape the project register. Legal and Compliance can confirm what applies in each market.

Many operators can make the first pass manageable by focusing on uses that could affect a critical service or sensitive data. Project, procurement, cloud and supplier records can help surface them; workflow owners can clarify what remains uncertain.

The evidence behind an inventory entry also matters. A product description or supplier statement can explain intended behavior, but may not show the identity and access paths actually deployed. Record whether a claim comes from documentation, configuration review or an operator test. That distinction helps the owner decide whether the assurance is proportionate to the service consequence, and prevents an unknown from quietly becoming a verified control.

Ownership is often split. The platform team may administer the feature, Procurement may hold the supplier relationship, and a service executive may carry the impact if it fails. A single “owner” field can hide those differences. Record who can change or suspend the capability, who can provide evidence, and who can accept the service-level residual risk. If that last role is unknown, the exposure is unowned, not accepted.

**Composite scenario: supplier feature.** A supplier enables an AI diagnostic feature in a network-management product during a routine software update. It is absent from the operator’s AI project register, yet it can read topology and propose actions. The immediate questions are who owns the feature, which identity it uses, and whether proposed actions remain inside the existing change process. This is the difference between counting AI products and understanding their authority.

The decision is not automatically “disable” or “trust the supplier.” If the feature’s access can be bounded, its actions traced and proposals kept within the established change process, the operator may have a basis to retain it with defined conditions. If those controls cannot be evidenced, restricting or disabling the feature may be the more defensible treatment, even if that delays the diagnostic benefit. The accountable service owner should understand the residual risk and when the decision will be revisited.

The operator may also need to separate the decision to install a product release from the decision to enable the new capability. Confirm with the supplier whether the feature can be disabled independently, what other changes or functions are coupled to it, and how the change can be reversed. If those choices are coupled, delaying the release may carry its own operational cost, while accepting the feature without a verified boundary leaves uncertainty. The service executive owns that residual decision; Procurement and engineering provide the evidence and options.

That makes inventory a lifecycle control, not a one-time audit. The supplier release path, cloud service terms and product change notices determine whether an operator learns about a new capability before or after it enters service. Procurement and technical owners can agree which changes require reassessment, particularly changes to identity, accessible data, connected tools or the ability to propose or trigger actions. If notice is late or absent, record the assurance gap and its owner; a stable product name is not evidence that its authority has stayed the same.

Inventory shows where to look. Access review shows whether an agent has more authority than its task requires.

## Move 2: Match authority to the task

The review can start with identities and tools that have the greatest potential service impact. An assistant that can read subscriber records, open a change request or reach a network-management API deserves closer scrutiny than one limited to public guidance.

The core questions are what data the agent can read, what actions it can take, and whether its access can be stopped without disabling a surrounding service.

Where the platform allows it, the agent can use a dedicated identity rather than an employee account or broad shared-service permissions. Access can be limited to the data and tools needed for the task. Short-lived credentials issued only when needed may help. Logs should show which identity acted, what tool it called and what happened.

A configuration describes the intended boundary; it does not establish what the deployed integration can reach. For one or two high-impact uses, trace an allowed and an out-of-scope request from the agent identity through the connector to the target system. Confirm that the excluded access is refused, logs identify the action and principal, and revocation closes the relevant path. Test in a suitable environment or supported window without disrupting monitoring or service assurance. If a supplier-managed control cannot be verified directly, record that as an assurance limitation rather than treating the design description as proof.

It helps to distinguish read, recommend and execute. Read-only access is often a sensible start. A low-impact, reversible action may fit within clear limits and monitoring. Actions that could change production, affect customers or interrupt an essential workflow should remain within the operator’s normal authorization and change process. An agent can prepare a change; an authorized person approves and validates it.

A human approval step is effective only if the reviewer can see the evidence behind the recommendation, understand the affected service and decline the action. If the reviewer sees only a generated summary or a pre-filled change request, the approval may become procedural. Control effectiveness depends on whether the person has enough context and authority to make a different decision, not on how many approval boxes appear in the workflow.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses.[10] This is general guidance, not a telco control standard. Legacy platforms and supplier connections matter as much as modern APIs. If a legacy system cannot support a separate identity, a controlled gateway may help. Until then, read-only access may be safer.

**Composite scenario: edge access.** In an engagement, the network team had already chosen an edge platform when a review found a shared service account that could reach both edge nodes and parts of the core. Fixing the access required a maintenance window and a supplier configuration change. Mapping identity and tool access earlier could have made the available rollback options clearer before deployment.

Separating that access may improve attribution and limit the path between edge and core, but the new boundary still has to be operated. Account ownership, credential rotation, supplier support and rollback all affect control effectiveness. A gateway can help where a legacy platform cannot issue a distinct identity, but it adds a dependency that also needs monitoring and recovery planning. If the intended boundary cannot yet be enforced, the operator might limit the agent to reading or recommendations. That can reduce exposure while a durable fix is planned. The residual risk still needs an owner.

The edge fix is a migration, not just an access edit. Before the maintenance window, identify workflows that still depend on the shared account, agree the supplier change and rollback boundary, and define what evidence will show that the new identity reaches only its intended systems. During the change, verify service monitoring and confirm that the old account no longer reaches the core. If rollback restores broad access, record it as a temporary residual-risk exception with an owner and review trigger; do not mark the boundary complete.

Permissions matter only if teams can contain a failure without losing the surrounding service. That takes rehearsal.

## Move 3: Rehearsal tests the response before an incident

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

A tabletop does not prove that a technical control works. It can establish who has authority, what information is needed and which services may be affected. A bounded technical validation is still needed to confirm that revocation blocks the relevant tool paths and that monitoring remains available. That test belongs in a suitable test environment or supported change window, not as an unplanned experiment on a live core. If the operator cannot test safely, the assurance limitation should remain visible in the risk decision.

Bring the SOC and NOC, identity and platform owners, service assurance, change management and business continuity into the exercise. Legal, communications, procurement and a supplier contact can join when the scenario needs them. Center it on a decision that could affect a service.

Possible scenarios include a supplier feature misusing an agent identity, a threat actor steering an assistant through hostile content, or an agent changing a service workflow during a network event. The team can test when to declare an incident, who can revoke access and what evidence to preserve. It can identify which service may lose visibility, what fallback exists and who can authorize an emergency change. Teams can also clarify who handles regulatory and customer notifications while the scope is uncertain.

The Canadian Centre for Cyber Security recommends practising for incidents that may unfold within hours, with isolation steps approved in advance and manual alternatives tested for critical functions.[14] Joint Australian and international guidance warns that external content can carry instructions designed to steer an agent. This is known as indirect prompt injection.[13] These are general recommendations. Operators can test them against their own systems and response roles.

A separate CISA CI Fortify tabletop package presents a hypothetical telecommunications outage and asks teams to examine isolation, third-party dependencies and manual operations.[29] It is a U.S. critical-infrastructure exercise template, not an AI-specific scenario or a reported incident.[29] Operators can add an agent identity or tool failure to test those continuity decisions.

CISA, FBI and international partners’ September 2026 guidance for service providers emphasizes clear, timely outage communications that preserve operational security and containment.[22] An exercise can clarify who approves an update, when it is sent and which backup channel remains if containment changes service availability.

Set the exercise’s success criteria before starting: which access must be stopped, what service or visibility must remain, who may authorize containment, and what response or recovery tolerances apply. A fast revocation is not a pass if it hides alarms or removes the only recovery path. A short rehearsal can focus on one critical service domain, separate from live production changes. Tolerances are best set with the service owner; one target will not fit every service. Record decisions, elapsed time, service impact, missing information and fallback. A later review can establish whether the gaps have closed.

**Composite scenario: NOC assistant.** The test described in Chapter 1 shows how a summarization task can become an authority question: a broader service account let the assistant open vendor cases, read neighboring-domain data and propose a change that would reduce NOC visibility. The rehearsal can test separate identities for reading and acting, and confirm that any network change remains in the normal approval process.

Containment options depend on how those permissions are connected. If reading and acting use separate identities, the operator may be able to stop the action path while preserving read-only alarm visibility. If both depend on a broad account, revoking it may also interrupt the NOC’s information or supplier workflow. The exercise should establish who can authorize a narrower stop, whether revocation affects existing sessions as well as new requests, and what manual fallback remains. Keeping visibility may preserve service awareness but leave some authority active; shutting the path may remove both. The service owner needs evidence to choose, not just a generic “isolate the agent” instruction.

A meaningful exercise looks beyond whether someone can revoke an account. It establishes which access stops, what happens to alarm visibility and vendor-case handling, what audit evidence remains, and what fallback the NOC can use. The SOC can assess the threat and evidence; the NOC and service owner can explain the operational consequence of isolation. The supplier can provide facts about its feature; the operator retains the decision on acceptable service impact and residual risk. If the fallback is untested, the exercise has exposed an assurance gap rather than proved the control effective.

Exercise findings should not all become generic training actions. Separate unclear authority, technical control failure and a service fallback that cannot be proven. Each finding needs an accountable owner, an interim treatment, a residual-risk decision and evidence that will close it. A revised procedure can clarify who acts, but cannot prove revocation works; a successful revocation test does not prove the NOC retains visibility. Where closure depends on supplier work or a safe change window, keep the gap open until the relevant test succeeds.

The rehearsal shows the CISO and CTO what worked, what was unclear and which service alternative remains untested. That is a stronger basis for funding than a list of tools.

## Move 4: A funded roadmap beats a collection of tools

The first three moves reveal gaps in authority, control effectiveness and response. Leaders can use those findings to decide what to fund and what risk they can accept. A credible board paper names the service at risk, proposed work, required resources and remaining risk.

A 12-month roadmap with three or four priorities is easier to govern. Each priority can have an executive sponsor and an operational lead. Where those roles differ, the operational lead owns delivery and evidence, while the accountable service executive owns acceptance of residual service risk. Milestones should reflect dependencies on suppliers or legacy systems, maintenance-window limits and the decisions leaders need to make. A board case is stronger when the cost of delay is clear in operator terms: customer-data exposure, reduced network control, slower containment, missed regulatory duties or loss of service.

Priority should follow the service risk, not the novelty of the AI. An operator can compare which services are affected, how far an identity or tool can reach, how effective the existing controls are, and how difficult it will be to make a change safely. A high-impact gap with a long supplier dependency may need an interim treatment and an explicit acceptance decision; a lower-impact use with a reversible change may be handled differently. The point is to make the basis for sequencing visible, not to force every use into a universal score.

An interim treatment should name the path it is meant to constrain and the evidence that it does so. A narrower identity may reduce reach; additional monitoring may help detect misuse but does not prevent access. Those controls have different effects and should not be reported as equivalent. If a restriction slows diagnostics or shifts work back to manual operations, record that service cost alongside the exposure it reduces.

Measures should show whether risk is changing, not how many tools were purchased. Useful indicators include named owners and data paths for high-impact uses, tested access revocation, clear containment authority, exercised service alternatives and closed exercise findings. A tool count can rise while access and response stay the same.

A policy is not proof. For high-impact uses, assurance depends on evidence that controls work under live-service conditions; an independent review can add confidence. The board’s decision rests on that evidence, the service impact if controls fail, the accountable executive and the conditions that would reopen the decision. Residual-risk acceptance remains within the operator’s approved risk appetite.

Regulation belongs in this roadmap, but it need not delay action. Legal and Compliance can track binding obligations by market and separate them from consultation drafts. Where duties overlap with identity, supplier assurance, incident reporting or continuity, existing governance may be enough; a separate AI approval board is not always needed.

At an executive review, the CISO and CTO can present the priorities, owners, service constraints and evidence gaps. The request might be funding for an identity boundary, time for a continuity test, and regular review of outcomes and residual risk. The paper should identify which accountable service executive accepts the remaining risk until later work is complete.

**Composite scenario: patch window.** Security has the advisory and fixed version for a live core platform, but the network team needs a maintenance window, rollback plan and supplier confirmation. The next available window is three weeks away. The residual risk is accepted at the service level, documented and reviewed. The roadmap makes that decision visible, including who owns it and when it will be revisited, rather than promising a patch date that operations cannot safely meet.

That decision has two sides. Applying the fix sooner may shorten exposure, while changing a live platform outside its planned window may create service risk. Waiting preserves the planned maintenance and rollback conditions but leaves the vulnerability in scope for longer. The decision record should explain the service impact, the evidence about the threat, what controls (if any) remain effective during the wait, and what would cause the owner to reconsider. The security team identifies and advises on risk; the accountable service executive owns acceptance of the residual risk within appetite.

A roadmap should distinguish delivery status from risk status. Booking a maintenance window is not remediation; the exposure remains until the supported change is applied and its effectiveness is checked. If the window slips or the threat evidence changes, the service owner needs to revisit acceptance rather than carrying it forward automatically.

## Keep the sequence, adjust the pace

Together, the four moves give the CISO and CTO a service-linked inventory, evidence about access limits and rehearsal outcomes, and a funded plan with named owners for residual risk. Where excessive production access is already clear, a proportionate response can precede the wider review. Chapter 5 turns those findings into an executive decision.
