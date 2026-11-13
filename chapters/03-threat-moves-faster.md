# Chapter 3: The Threat Moves Faster Than the Operator Can Respond

The response gap is not only detection. An attacker can keep moving while the operator works out who may contain it without disrupting service.

That is the challenge for a service provider. The SOC may see an alert, the NOC may know a planned change is underway, IAM may be able to revoke a credential, and a supplier may hold platform details. If no one knows who can authorize containment, time is lost while the network remains in service and the attacker may continue.

Chapter 2 mapped where exposure can enter and spread. This chapter asks whether the operator can detect activity, decide and act before the attacker reaches its next objective, without creating a second incident through unsafe containment.

## The clock is getting shorter, but not every attack is autonomous

AI can support tasks such as finding weaknesses and targeting organizations. Agentic systems can link attack stages with less human direction.[14] That does not mean every attacker uses an agent or every attack unfolds at machine speed.

The Canadian Centre for Cyber Security’s October 2026 bulletin says attacks are not yet fully autonomous. Humans still choose targets, set objectives and oversee operations, while machines handle more work between those decisions. It describes activity attributed to Storm-0940 moving from target selection to privileged cloud access in under three hours.[14]
This is not telecom-specific evidence. It shows how quickly an adversary can move through familiar weaknesses; it does not show that a telco has been attacked this way.

CERT-In reported a related pattern in October 2026. In a financially motivated campaign against Indian entities, which the advisory does not identify as telecom operators, the agency said agentic tooling compressed the time from initial access to impact from days to a few hours. It also reported parallel agent operations and repeat attacks within days when remediation was incomplete.[11]

On 4 November, CERT-In’s finance-sector response team said an AI-assisted campaign had timed attacks to weekends, holidays and other low-monitoring windows.[20] The advisory concerns financial services, not telecom, but supports testing off-hours decision authority and escalation.

These observations do not establish a universal attacker timeline. They do show why waiting for the next maintenance window may be unsafe when exploitation is confirmed.

The important point is not simply faster scanning. It is the shrinking interval between one step and the next. A stolen identity can be reused. A tool can search broadly. A partial fix can leave another route open. When an attacker can repeat actions quickly, responders may need to contain the immediate path while continuing to investigate.

Detection and response are different capabilities. A dashboard can show an event, but people still need authority and context to decide whether to revoke an identity, isolate a host, block a supplier connection or keep a service running in reduced mode.

## The operator has more than one clock

Incident response is often described as a technical sequence: detect, investigate, contain, recover. In practice, those activities overlap. The NOC may be confirming whether an alarm matches a real network change. The SOC may be deciding whether the activity is malicious. IAM may need to disable an account. Service assurance may be estimating which customers or services could be affected. Legal, regulatory and communications teams may already be working against notification deadlines.

At the same time, the network cannot wait for every team to finish its analysis. Nor can the operator treat every system as disposable. A management platform may support several network domains. An identity may be shared across automation jobs. A supplier connection may be needed to restore a service even as the supplier helps investigate it. Availability changes the containment decision.

Separate four clocks:

- **Detection:** How long before someone recognizes that the event may be malicious?
- **Decision:** How long before an authorized person chooses a containment action?
- **Action:** How long before teams execute it safely and confirm the result?
- **Continuity and recovery:** How long before affected services can run safely again?

A fast SOC does not guarantee a fast response if approval is slow. Quick isolation is not success if it breaks a critical workflow or removes telemetry needed to understand the incident. For each exercise, record time to detect, authorize, execute safely and restore service. The service owner should set tolerances for each clock before the exercise, based on continuity needs, safe containment options and applicable notification deadlines. One threshold will not fit every service domain.

This is where NOC and SOC coordination matters. The SOC understands the evidence and the likely attack path. The NOC understands which systems are carrying live operations, what maintenance is in progress, and what a particular isolation could do to service. Neither view is sufficient alone. Each needs a clear route to the other, with someone empowered to decide when there is no time for a long discussion.

## A telecom breach has several timelines

The South Korean Ministry of Science and ICT’s investigation into the 2025 SK Telecom breach is a useful reminder that the response clock includes more than containment. MSIT reports that SK Telecom detected abnormally large outbound traffic at 11:20 p.m. on 18 April 2025 and notified KISA at 4:46 p.m. on 20 April; the Ministry said this exceeded the statutory 24-hour reporting window.[15]

That is a reporting timeline, not a measurement of how long the company took to contain the intrusion. The distinction matters. The government’s public-private investigation team was established on 23 April and conducted forensic inspections across all 42,605 SK Telecom servers through 27 June. Its final findings identified 28 infected servers.[15]
Establishing the full scope took sustained work across the operator and government investigators.

The customer response had its own operational demands. In its preliminary findings, the Ministry encouraged subscribers to replace their USIM cards or use a protection service, and urged the operator to expand service channels and add a reservation system so more customers could be protected promptly.[16]
These reports describe a breach-response timeline, not a network outage. They show how an incident can create a second workload: protecting customers, handling enquiries and changing business operations while the technical investigation continues.

For response planning, CISA, the FBI and international partners published service-provider guidance in September 2026 on clear, timely outage communications that preserve operational security and containment.[22] The guidance is not an incident report; it is relevant when containment itself changes service availability.

There is no single clock. The initial signal, statutory notification, technical scoping and customer protection each have different owners and deadlines. If those responsibilities are not connected before an incident, the organization may be trying to create a response structure at the same time it is trying to contain an attacker.

## Containment is a service decision

For an ordinary office system, “isolate it” may sound straightforward. In a provider environment, the same action can have different consequences depending on the system’s role. Cutting a compromised supplier connection may slow recovery. Disabling a shared identity may stop a legitimate monitoring workflow. Isolating a management host may reduce an attacker’s access but also remove a source of operational visibility.

That does not mean the operator should wait. It means the available actions should be designed and authorized in advance. The Canadian Cyber Centre recommends deciding in advance who may isolate an account, application, network or service, then practising for incidents that unfold within hours rather than days. For critical infrastructure, it also recommends identifying essential functions, defining pre-authorized isolation steps and testing safe manual or alternative operation.[14]

Translate the guidance into criteria for evidence, service impact, authority and fallback. For a telco, the questions are specific: which identities can the SOC revoke without NOC approval? Which systems can be isolated while the network remains stable? What fallback is available if a supplier connection must be stopped? Who can authorize an emergency change and record the decision? Which services must continue, and what reduced mode is acceptable?

“Call the incident commander” is not enough if the commander has no authority to act. “Follow the change process” is not enough if the process assumes there is time to schedule a meeting. The emergency route has to be legitimate, documented and rehearsed. It should preserve the evidence and service context needed for the next decision.

## A composite NOC/SOC scenario

Consider a composite scenario, not a reported incident. During a planned maintenance window, the SOC sees unusual privileged calls from an identity used by a network-management integration. The calls are consistent with the work in progress, but the volume and destinations are not. The NOC confirms that a change is active and warns that disabling the shared identity could interrupt monitoring for more than one network domain. A supplier says a software update may explain the behavior, but cannot confirm that immediately.

The threat is uncertain. The service impact is not. The operator now has to choose between waiting for more evidence, revoking the identity, or isolating the integration path and accepting reduced visibility while the incident is investigated. If the identity is compromised, each minute of delay may give the attacker more reach. If the operator disables too much, the response itself could hide faults or interfere with planned work.

A prepared organization does not ask the SOC analyst to resolve this alone. The SOC validates the evidence and identifies the access path. The NOC explains service dependencies and available fallback. The incident lead uses pre-agreed criteria to choose a bounded action. IAM or platform operations carries it out. The supplier provides technical facts, but does not make the operator’s risk decision. Customer, legal and regulatory leads work in parallel on impact and notification, rather than waiting for the forensic picture to be complete.

The first action might be to revoke a scoped token and pause the affected automation, not shut down an entire management environment. If that is not enough, a defined escalation path can authorize a broader isolation and the corresponding service fallback. The decision, evidence and service impact are logged. The NOC confirms what continues to work. The SOC checks whether the hostile activity has stopped and whether another identity or path remains active.

Pre-agreed choices cannot cover every incident, but they can speed the first decision without ignoring availability. Actions must reflect the operator’s architecture and service obligations. A playbook from another company cannot identify which local system is safe to stop.

## Use automation where its impact is bounded

AI can help defenders assemble incident context and identify relevant systems, runbooks and teams. These tasks can save time without granting authority to make a network-impacting decision.

Some actions can be automated when their scope is narrow, their effect is understood, and they can be reversed or recovered. For example, an operator might pre-authorize revocation of a short-lived credential tied to one agent run, with a NOC alert and a recorded reason. A named service owner should decide actions that could affect customers or network continuity, and accept any temporary service impact. Automated actions should stay within tested limits that leadership has accepted.

Defenders do not need proof that a specific intrusion used AI before preparing for shorter timelines. Response plans should reflect what the activity can do, how quickly it can move, and what the operator must keep running.

## The question for leadership

A CISO or CTO should be able to answer a few questions without assembling a committee during an incident. Which containment actions are pre-approved, and who can authorize a broader action after hours? Which service dependencies must be checked before isolating an identity or supplier connection? If isolation reduces service, who accepts that impact and sets the return-to-service criteria? Who handles regulator and customer notifications while technical scoping continues? When was the fallback last exercised?

The answers show whether response speed is only a SOC metric or a capability across the operating model. Repeated debate about roles, service impact and approval will create avoidable delay. But a team acting without understanding what it may interrupt can turn containment into a service incident.

Chapter 1 explained why risk has changed. Chapter 2 mapped where exposure can enter and spread. This chapter connected response time, decision authority and service continuity. Chapter 4 turns those concerns into four practical moves for a service-provider CISO or CTO over the next twelve months.
