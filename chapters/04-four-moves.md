# Chapter 4: Four Moves for Service Providers in the Next 12 Months

The same identity may connect an OSS query, a service ticket and an operational action. That shortens the path between information and change, but it can also let a mistake or compromised tool travel farther before a person intervenes. The Canadian Centre for Cyber Security’s cross-sector evidence suggests AI can shorten parts of an attacker’s workflow. For a service provider, the task is to contain both risks without putting continuity at odds with security.

Existing security, network, architecture, supplier and change processes provide a natural starting point. The review is about where agent identities, tools or supplier features fall outside them: which identities can reach which data or tools, which actions need approval, how NOC and SOC teams will rehearse a response, and what remains uncovered.

The sequence is useful because each move answers a different question. Visibility shows where authority exists. Access review tests whether it matches the task. Rehearsal reveals whether the operator can contain failure and maintain service. The roadmap gives owners and resources to close the gaps. These activities can overlap. Where excessive access is already evident, there is little value in waiting for the full inventory before considering a proportionate restriction.

No sequence will eliminate risk. The four moves help test controls and make residual risk visible against the operator’s risk appetite.

## Move 1: Visibility means more than an AI inventory

A model list does not show what the system can do. AI may arrive as a feature in a network-management product, customer-service platform or supplier portal. The feature may use a supplier identity to read service data or trigger a workflow. The product may keep the same name.

Two questions frame the work: where can AI reach the operator’s systems or data, and what actions can it take? A joint review can bring together Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation, even when no one calls them AI.

A service-first review is more useful than a model-first list. The relevant areas include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. A customer-care summary tool has a different service impact from an assistant that can reach network configuration or subscriber records.

A concise record can capture the owner and purpose, model or supplier, identity, data and tools, affected services, available logs, fallback, relevant markets and who can suspend the use. Open questions should remain visible rather than being marked complete.

An inventory becomes useful when it links a capability to its service owner, data, identity and available actions. A product count alone will not show that. A supplier feature may change through an update even when the product name stays the same. Release notices, procurement reviews and architecture changes can feed the same inventory, so the register remains useful after the initial discovery. When the supplier cannot explain the feature’s identity or reach, that uncertainty is a risk to resolve or explicitly accept, not a reason to mark the entry complete.

The Australian Cyber Security Centre’s October 2026 guidance calls for AI asset identification to include services, agents, connectors and unsanctioned applications. It also recommends checking what providers retain in prompts and outputs, whether customer data is used to train models, and where processing occurs. This is cross-sector guidance; local legal duties still need review.

In October 2026, TRAI, India’s telecom regulator, published draft guidelines on AI use in telecommunications. They also propose an AI inventory and third-party due diligence, as discussed in Chapter 2. The document remains a consultation draft, not a final rule.

The draft does not prescribe a global inventory. It highlights a practical gap: supplier features and product capabilities can escape the project register. Legal and Compliance can confirm what applies in each market.

Many operators can make the first pass manageable by focusing on uses that could affect a critical service or sensitive data. Project, procurement, cloud and supplier records can help surface them; workflow owners can clarify what remains uncertain.

The evidence behind an inventory entry also matters. A product description or supplier statement can explain intended behavior, but may not show the identity and access paths actually deployed. Record whether a claim comes from documentation, configuration review or an operator test. That distinction helps the owner decide whether the assurance is proportionate to the service consequence, and prevents an unknown from quietly becoming a verified control.

Ownership is often split. The platform team may administer the feature, Procurement may hold the supplier relationship, and a service executive may carry the impact if it fails. A single “owner” field can hide those differences. Record who can change or suspend the capability, who can provide evidence, and who can accept the service-level residual risk. If that last role is unknown, the exposure is unowned, not accepted.

**Composite scenario: supplier feature.** A supplier enables an AI diagnostic feature in a network-management product during a routine software update. It is absent from the operator’s AI project register, yet it can read topology and propose actions. The immediate questions are who owns the feature, which identity it uses, and whether proposed actions remain inside the existing change process. This is the difference between counting AI products and understanding their authority.

The decision is not automatically “disable” or “trust the supplier.” If the feature’s access can be bounded, its actions traced and proposals kept within the established change process, the operator may have a basis to retain it with defined conditions. If those controls cannot be evidenced, restricting or disabling the feature may be the more defensible treatment, even if that delays the diagnostic benefit. The accountable service owner should understand the residual risk and when the decision will be revisited.

The operator may also need to separate the decision to install a product release from the decision to enable the new capability. Confirm with the supplier whether the feature can be disabled independently, what other changes or functions are coupled to it, and how the change can be reversed. If those choices are coupled, delaying the release may carry its own operational cost, while accepting the feature without a verified boundary leaves uncertainty. The service executive owns that residual decision; Procurement and engineering provide the evidence and options.

That makes inventory a lifecycle control, not a one-time audit. The supplier release path, cloud service terms and product change notices determine whether an operator learns about a new capability before or after it enters service. Procurement and technical owners can agree which changes require reassessment, particularly changes to identity, accessible data, connected tools or the ability to propose or trigger actions. If notice is late or absent, record the assurance gap and its owner; a stable product name is not evidence that its authority has stayed the same.

**Illustrative completed register: supplier diagnostic feature.** This entry uses only the supplied composite situation. “Unknown” is a valid register value: it shows which decision cannot yet be supported by evidence.

| Field | Illustrative entry |
|---|---|
| Capability and trigger | AI diagnostic feature enabled through a routine update to a network-management product; absent from the AI project register. |
| Purpose and known reach | Reads topology and proposes actions. No wider data access or direct execution is established by the scenario. |
| Owner | Operational feature owner: **not identified**. Supplier contact: **to be recorded**. Accountable service executive: **to be named before acceptance**. |
| Identity and path | Identity, connector and target-system permissions: **not yet verified**. Trace them end to end before treating the boundary as known. |
| Authority boundary | Proposal is subject to the existing change process, but whether configuration or workflow technically enforces that boundary is **unverified**. |
| Evidence and control state | Supplier documentation may describe design; deployed identity, data scope, action limits and logs still require configuration review or a bounded test. No test result is assumed here. |
| Stop and fallback | Independent feature disablement, effect on the rest of the product, and the operational fallback are **not established**. Confirm before deciding whether restriction is safe. |
| Decision and residual risk | Retain only under evidenced limits, restrict/disable if limits cannot be established, or defer enablement pending supplier evidence. If use continues with an assurance gap, name the delegated service-risk owner, conditions and reassessment trigger. |

This register makes the decision gap concrete: the feature’s purpose is known, but its deployed identity, path, disable behavior and fallback are not. Do not treat a supplier description as proof of those controls. The service executive needs either verified boundaries and an operating fallback or an explicit treatment for the unresolved exposure.

Inventory shows where to look. Access review shows whether an agent has more authority than its task requires.

## Move 2: Match authority to the task

The review can start with identities and tools that have the greatest potential service impact. An assistant that can read subscriber records, open a change request or reach a network-management API deserves closer scrutiny than one limited to public guidance.

The core questions are what data the agent can read, what actions it can take, and whether its access can be stopped without disabling a surrounding service.

Where the platform allows it, the agent can use a dedicated identity rather than an employee account or broad shared-service permissions. Access can be limited to the data and tools needed for the task. Short-lived credentials issued only when needed may help. Logs should show which identity acted, what tool it called and what happened.

A configuration describes the intended boundary; it does not establish what the deployed integration can reach. For one or two high-impact uses, trace an allowed and an out-of-scope request from the agent identity through the connector to the target system. Confirm that the excluded access is refused, logs identify the action and principal, and revocation closes the relevant path. Test in a suitable environment or supported window without disrupting monitoring or service assurance. If a supplier-managed control cannot be verified directly, record that as an assurance limitation rather than treating the design description as proof.

It helps to distinguish read, recommend and execute. Read-only access is often a sensible start. A low-impact, reversible action may fit within clear limits and monitoring. Actions that could change production, affect customers or interrupt an essential workflow should remain within the operator’s normal authorization and change process. An agent can prepare a change; an authorized person approves and validates it.

A human approval step is effective only if the reviewer can see the evidence behind the recommendation, understand the affected service and decline the action. If the reviewer sees only a generated summary or a pre-filled change request, the approval may become procedural. Control effectiveness depends on whether the person has enough context and authority to make a different decision, not on how many approval boxes appear in the workflow.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses. This is general guidance, not a telco control standard. Legacy platforms and supplier connections matter as much as modern APIs. If a legacy system cannot support a separate identity, a controlled gateway may help. Until then, read-only access may be safer.

**Illustrative read/recommend/execute authority matrix.** Adapt the boundaries to service impact and the operator’s architecture; the matrix is a decision aid, not a universal policy.

| Level | What the agent may do | Boundary and evidence | Decision consequence |
|---|---|---|---|
| **Read** | Retrieve only the data needed for the stated task. | Enforce read-only rights at the target or controlled connector; test an in-scope and out-of-scope request, confirm the principal in logs, and check retention and data destination. | If the task needs neighboring-domain data, use a separately authorized, time-bounded path where feasible. If the source or identity cannot be verified, do not treat “read-only” as low risk by default. |
| **Recommend** | Produce a draft, diagnosis or proposed action without submitting a change. | Include source records and enough service context for a qualified operator to verify the reasoning. Confirm the recommendation cannot invoke a hidden write path or trigger downstream execution. | This can preserve analytical value while keeping the decision with the service team, but it still influences triage and can misdirect work if the evidence is incomplete. |
| **Execute** | Perform a narrowly defined action only where the operator has deliberately delegated it. | Scope the target and parameters; set preconditions and limits; test stop, audit and rollback; preserve the normal change process for material service-impacting actions. | If action cannot be bounded, observed or reversed safely, keep the workflow at recommendation-only. Any delegated execution needs a named owner and a service fallback. |

The level should follow the consequence, not the product label. A ticket update may be low impact in one workflow and operationally significant in another. Before moving a use from read to recommendation or execution, the service owner should see test evidence that the new boundary holds and understand what work becomes slower or manual if the agent is restricted. Security can validate identity and control behavior; the accountable service executive decides whether the remaining exposure is acceptable.

**Composite scenario: edge access.** In the supplied composite situation, the network team had chosen an edge platform before review found a shared service account that could reach both edge nodes and parts of the core. Fixing the access required a maintenance window and a supplier configuration change. Mapping identity and tool access earlier could have made the available rollback options clearer before deployment.

Separating that access may improve attribution and limit the path between edge and core, but the new boundary still has to be operated. Account ownership, credential rotation, supplier support and rollback all affect control effectiveness. A gateway can help where a legacy platform cannot issue a distinct identity, but it adds a dependency that also needs monitoring and recovery planning. If the intended boundary cannot yet be enforced, the operator might limit the agent to reading or recommendations. That can reduce exposure while a durable fix is planned. The residual risk still needs an owner.

The edge fix is a migration, not just an access edit. Before the maintenance window, identify workflows that still depend on the shared account, agree the supplier change and rollback boundary, and define what evidence will show that the new identity reaches only its intended systems. During the change, verify service monitoring and confirm that the old account no longer reaches the core. If rollback restores broad access, record it as a temporary residual-risk exception with an owner and review trigger; do not mark the boundary complete.

Permissions matter only if teams can contain a failure without losing the surrounding service. That takes rehearsal.

## Move 3: Rehearsal tests the response before an incident

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

A tabletop does not prove that a technical control works. It can establish who has authority, what information is needed and which services may be affected. A bounded technical validation is still needed to confirm that revocation blocks the relevant tool paths and that monitoring remains available. That test belongs in a suitable test environment or supported change window, not as an unplanned experiment on a live core. If the operator cannot test safely, the assurance limitation should remain visible in the risk decision.

Bring the SOC and NOC, identity and platform owners, service assurance, change management and business continuity into the exercise. Legal, communications, procurement and a supplier contact can join when the scenario needs them. Center it on a decision that could affect a service.

A rehearsal can make the authority boundary explicit. The operator can pre-authorize suspension of a dedicated agent identity under defined conditions, while requiring service-owner input when revocation would also remove NOC visibility or supplier-case handling. That distinction is not a reason to delay containment when misuse is confirmed. It ensures the team knows what fallback starts with the containment action and who owns the service consequence. If one identity carries both automation and monitoring access, the NOC should not be left to choose under pressure between leaving access active and making a broad change.

The Canadian Centre for Cyber Security recommends practising for incidents that may unfold within hours, with isolation steps approved in advance and manual alternatives tested for critical functions. CISA, ASD ACSC and partner agencies’ joint guidance also warns that external content can carry instructions designed to steer an agent, a risk known as indirect prompt injection. These are general recommendations. Operators can test them against their own systems and response roles.

A separate CISA CI Fortify tabletop package presents a hypothetical telecommunications outage and asks teams to examine isolation, third-party dependencies and manual operations. It is a U.S. critical-infrastructure exercise template, not an AI-specific scenario or a reported incident. Operators can add an agent identity or tool failure to test those continuity decisions.

CISA, FBI and international partners’ September 2026 guidance for service providers emphasizes clear, timely outage communications that preserve operational security and containment. An exercise can clarify who approves an update, when it is sent and which backup channel remains if containment changes service availability.

Set the exercise’s success criteria before starting: which access must be stopped, what service or visibility must remain, who may authorize containment, and what response or recovery tolerances apply. A fast revocation is not a pass if it hides alarms or removes the only recovery path. A short rehearsal can focus on one critical service domain, separate from live production changes. Tolerances are best set with the service owner; one target will not fit every service. Record decisions, elapsed time, service impact, missing information and fallback. A later review can establish whether the gaps have closed.

**Composite scenario: NOC assistant.** Chapter 1 supplies the composite. Here the question is whether the SOC and NOC can contain the broad identity without losing essential visibility, while keeping any proposed network change inside normal change control.

Exercise findings should not all become generic training actions. Separate unclear authority, technical control failure and a service fallback that cannot be proven. Each finding needs an accountable owner, an interim treatment, a residual-risk decision and evidence that will close it. A revised procedure can clarify who acts, but cannot prove revocation works; a successful revocation test does not prove the NOC retains visibility. Where closure depends on supplier work or a safe change window, keep the gap open until the relevant test succeeds.

**Illustrative SOC/NOC exercise: the NOC assistant.** Use the existing assistant scenario as a bounded tabletop, followed by technical validation in a safe environment. The purpose is to test authority and service continuity, not to demonstrate a product or simulate a new incident.

| Stage | Exercise prompt | Evidence of a useful response |
|---|---|---|
| Establish the normal path | The assistant summarizes alarms and drafts a ticket update. Ask the NOC and SOC what identity and data path they expect. | Teams identify the service, principal, connector, logs and owner without relying on the product name alone. |
| Introduce the broader access already in the scenario | The assistant’s service account can open vendor cases and read neighboring-domain data. Ask which access is required for the task and which can be restricted. | Participants distinguish read, recommendation and action authority, and identify who may approve temporary scope expansion. |
| Present the proposed visibility-reducing change | The assistant proposes a change that would reduce NOC visibility. Ask what evidence is needed, who can stop the identity, and what remains open if they do not. | NOC explains service impact; SOC explains threat evidence; the service owner identifies the authorized containment choice and fallback. The proposal remains subject to normal change control. |
| Test the stop and fallback | Tabletop the revocation decision, then, separately, verify the identity and downstream tool behavior in a suitable test or supported change window. | Technical evidence shows whether new and existing access is stopped, whether logs identify the principal and downstream result, and whether essential monitoring remains available. The tabletop alone is not recorded as technical proof. |
| Close the decision | Assign any unresolved access, supplier or fallback gap. State the interim control, residual-risk owner, review trigger and evidence needed to close it. | The decision is traceable; a failed test, expanded access or changed service condition returns the issue for reassessment. |

The decision should compare a tested separation of read and action rights with the temporary restriction that returns work to NOC staff. The first depends on identity design and supplier support; the second can slow diagnostics and case handling. If neither boundary is yet proven, the service executive owns the interim exposure within delegated authority and the record names the test or change that will reopen it. The exercise results give the CISO and CTO evidence for capacity or supplier requests; a tabletop alone is not proof that the control works.

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

Threat urgency and change readiness are related, but they are not the same decision. New evidence about exploitation may justify seeking an earlier supported window; it does not establish that an untested live-core change is safe. The service team and supplier provide the change and rollback evidence. If no safe earlier option is available, the service executive must decide whether verified interim controls keep the remaining exposure within appetite or whether the affected use or access needs further restriction.

A roadmap should distinguish delivery status from risk status. Booking a maintenance window is not remediation; the exposure remains until the supported change is applied and its effectiveness is checked. If the window slips or the threat evidence changes, the service owner needs to revisit acceptance rather than carrying it forward automatically.

**Illustrative 30/90/180/365-day roadmap.** These are planning waypoints after the executive mandate, not universal deadlines. Move them to fit the operator’s change calendar, supplier commitments and service priorities. A date is not evidence of risk reduction.

| Waypoint | Accountable lead and contributors | Deliverable and dependency | Evidence of completion and effect |
|---|---|---|---|
| **Day 30** | CISO or delegated security lead, with service and platform owners; Procurement obtains supplier facts. | Identify priority workflows and complete the register for the supplier diagnostic feature and the NOC assistant. Record the edge/core account’s actual reach and flag anything not yet verified. Depends on access to product, identity and supplier records. | Named service and operational owners; known versus unknown identities, data and actions; decision on which gaps need immediate restriction. Completion means a decision-ready baseline, not that controls are effective. |
| **Day 90** | Identity/platform lead with Network Engineering, NOC and supplier engineers. | Agree the first access-boundary changes: separate read from action where supported, constrain the diagnostic feature, and plan the edge-account migration. Depends on supplier configuration options, test environment and a supported window. | Configuration evidence plus allowed/denied-path tests, attributable logs and verified revocation. If a boundary cannot yet be tested safely, record the limitation and interim treatment rather than marking it closed. |
| **Day 180** | Incident-response lead with SOC, NOC, service assurance, change management and the relevant supplier. | Run the structured NOC-assistant exercise and test fallback/containment paths; close or assign the technical and authority gaps. Depends on the identities being sufficiently mapped and operational fallback being defined. | Exercise decisions and timestamps against locally agreed tolerances; separate evidence from tabletop discussion; technical test showing what revocation stops and what visibility remains; owners and review triggers for open findings. |
| **Day 365** | CTO/CISO sponsors, accountable service executives and portfolio/resource owners. | Review whether priority controls reduced exposure, whether delayed work remains acceptable, and what capacity or supplier commitment is needed for the next cycle. The patch window and any edge migration remain subject to safe supported change. | Report delivery separately from risk reduction: completed work, test result, residual risk by service, unresolved dependencies, acceptance authority and reassessment triggers. A patch is counted as risk reduction only after deployment and effectiveness checks. |

The role column is not a funding estimate. Before each waypoint, add operator-specific needs for network and identity engineering, NOC/SOC backfill, supplier work, test environments and change windows. State the estimate’s basis and which work would move; if unknown, mark it pending rather than inventing a budget or implying that the work costs nothing.

At each waypoint, the decision owner should be able to change course when a dependency fails, access expands, a control test fails or service conditions change. If several service domains share an identity or supplier path, the accountable owner needs authority over the full impact; where no such delegated owner exists, escalate instead of letting the delivery lead accept risk by default.

## Keep the sequence, adjust the pace

Together, the four moves give the CISO and CTO a service-linked inventory, evidence about access limits and rehearsal outcomes, and a funded plan with named owners for residual risk. Where excessive production access is already clear, a proportionate response can precede the wider review. Chapter 5 turns those findings into an executive decision.
