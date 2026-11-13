# Chapter 3: The Threat Moves Faster Than the Operator Can Respond

The response gap is not just detection time. It is also the time needed to authorize containment without disrupting service.

The SOC may see an alert while the NOC sees a planned change. IAM may be able to revoke a credential, and a supplier may hold platform details. Without a clear decision path, an attacker may retain access while the operator assesses service impact.

Chapter 2 mapped where exposure can enter and spread. The operator needs to detect activity, decide and act before the attacker reaches its next objective, without creating a second incident through unsafe containment.

## Threat activity can accelerate without being fully autonomous

The Canadian Centre for Cyber Security’s 26 October 2026 bulletin is cross-sector evidence, not a telecom incident or a universal attack timeline. It says attacks are not yet fully autonomous: humans still choose targets, set objectives and oversee operations.[14] For some activity attributed by the bulletin to Storm-0940, the time from target selection to privileged cloud access was less than three hours.[14]

In a 15 October 2026 advisory, CERT-In reported that tools using AI agents shortened the time from initial access to impact from days to a few hours in a financially motivated campaign against Indian entities. The advisory did not identify those organizations as telecom operators; it also reported parallel agent operations and repeat attacks within days after incomplete remediation.[11]

A separate 4 November advisory from CERT-In’s finance-sector incident-response team reported attacks against Indian BFSI entities timed to holidays, weekends and other low-monitoring windows, including after incomplete remediation.[20] This financial-sector evidence supports testing off-hours decision authority and escalation, not a claim about telco incidents.

Neither report establishes an operator response deadline. When exploitation is confirmed, the operator should not assume it can wait for the next routine maintenance window; it needs a tested emergency path to a safe containment decision.

Detection and response are different capabilities. A dashboard can show an event, but people still need authority and context to decide whether to revoke an identity, isolate a host, block a supplier connection or keep a service running in reduced mode.

## Response runs on several timelines

Incident response is often described as a technical sequence: detect, investigate, contain, recover. In practice, workstreams overlap. The NOC checks whether an alarm matches a real network change; the SOC assesses whether the activity is malicious; IAM may need to disable an account. Service assurance estimates customer and service impact, while legal, regulatory and communications teams work against their own deadlines.

At the same time, the network cannot wait for every team to finish its analysis. Nor can the operator treat every system as disposable. A management platform may support several network domains. An identity may be shared across automation jobs. A supplier connection may be needed to restore a service even as the supplier helps investigate it. Availability changes the containment decision.

Measure four response intervals:

- **Detection:** How long before someone recognizes that the event may be malicious?
- **Decision:** How long before an authorized person chooses a containment action?
- **Action:** How long before teams execute it safely and confirm the result?
- **Continuity and recovery:** How long before affected services can run safely again?

A fast SOC does not guarantee a fast response if approval is slow. Quick isolation is not success if it breaks a critical workflow or removes telemetry needed to understand the incident. For each exercise, record time to detect, authorize, execute safely and restore service. The service owner should set tolerances for each interval before the exercise, based on continuity needs, safe containment options and applicable notification deadlines. One threshold will not fit every service domain.

CERT-In’s April 2026 advisory recommends tabletop exercises for five simultaneous incidents rather than a single incident, explicitly modelling AI-driven scenarios.[28] That recommendation is Indian cross-sector guidance, not a telco standard or universal target. For an operator, the test is whether NOC, SOC, IAM and service teams can still make timely, service-safe decisions when their attention is split.

The SOC assesses the evidence and likely attack path; the NOC knows which systems carry live operations, what maintenance is under way, and what isolation could do to service. Agree who resolves a conflict between those views and who can authorize the next step when there is no time for a long discussion.

## The SK Telecom response had distinct timelines

The South Korean Ministry of Science and ICT (MSIT) investigation into SK Telecom’s 2025 breach shows that response includes more than containment. MSIT reports that SK Telecom detected abnormally large outbound traffic at 11:20 p.m. on 18 April 2025 and notified KISA at 4:46 p.m. on 20 April; the Ministry said this exceeded the statutory 24-hour reporting window.[15]

That is a reporting timeline, not a measure of containment time. The public-private investigation team was established on 23 April and inspected all 42,605 SK Telecom servers through 27 June; its final findings identified 28 infected servers.[15]
Establishing the full scope took sustained work across the operator and government investigators.

The customer response had its own operational demands. In its preliminary findings, the Ministry encouraged subscribers to replace their USIM cards or use a protection service, and urged the operator to expand service channels and add a reservation system so more customers could be protected promptly.[16]
These reports describe a breach-response timeline, not a network outage. They show how an incident can create a second workload: protecting customers, handling enquiries and changing business operations while the technical investigation continues.

CISA, the FBI, and partner agencies recommend a service-outage communications plan with triggers, escalation paths, and templates for status pages, customer and partner notices, and regulatory communications.[22] They advise frequent updates on what is known, unknown and under investigation, while protecting operational security and aligning with law-enforcement and containment efforts.[22] The guidance does not describe the SK Telecom breach; for an operator, it can inform planning when defensive isolation changes service availability.

The practical lesson is to assign owners for notification, forensic scoping and customer protection who can work in parallel while containment continues.

## Containment is a service decision

For an ordinary office system, “isolate it” may sound straightforward. In a provider environment, the same action can have different consequences depending on the system’s role. Cutting a compromised supplier connection may slow recovery. Disabling a shared identity may stop a legitimate monitoring workflow. Isolating a management host may reduce an attacker’s access but also remove a source of operational visibility.

That does not mean the operator should wait. It means the available actions should be designed and authorized in advance. The Canadian Cyber Centre recommends deciding in advance who may isolate an account, application, network or service, and practising incidents that unfold within hours rather than days. It also recommends identifying essential functions, defining pre-authorized isolation steps and testing safe manual or alternative operations.[14]

For a provider, translate that guidance into clear criteria: what evidence is enough, which actions the SOC can take alone, when the NOC or service owner must approve, and what fallback keeps essential services running.

The emergency route needs a real mandate, service context and a record of the decision. An incident-commander title cannot substitute for authority, just as a change process built for scheduled work cannot handle every urgent isolation.

## A composite NOC/SOC scenario

Consider a composite scenario, not a reported incident. During a planned maintenance window, the SOC sees unusual privileged calls from an identity used by a network-management integration. The calls are consistent with the work in progress, but the volume and destinations are not. The NOC confirms that a change is active and warns that disabling the shared identity could interrupt monitoring for more than one network domain. A supplier says a software update may explain the behavior, but cannot confirm that immediately.

The threat is uncertain. The service impact is not. The operator must choose: wait for more evidence, revoke the identity, or isolate the integration path and accept reduced visibility. If compromised, the identity may leave an access path open until revoked; isolate too much, and containment may hide faults or disrupt planned work.

The SOC validates the evidence and identifies the access path, while the NOC explains service dependencies and available fallback. The incident lead uses pre-agreed criteria to choose a proportionate first action; IAM or platform operations carries it out. The supplier provides technical facts but does not make the operator’s risk decision. Customer, legal and regulatory teams work in parallel on impact and notification, before the forensic picture is complete.

The first action might be to revoke a scoped token and pause the affected automation, not shut down an entire management environment. If that is not enough, a defined escalation path can authorize a broader isolation and the corresponding service fallback. The decision, evidence and service impact are logged. The NOC confirms what continues to work. The SOC checks whether the hostile activity has stopped and whether another identity or path remains active.

Pre-agreed choices will not cover every incident. They can shorten the first decision while keeping service impact within agreed limits. Actions must reflect the operator’s architecture and service obligations. A playbook from another company cannot identify which local system is safe to stop.

## Use automation where its impact is limited

CISA’s August 2026 Logging Reference Architecture (LRA) targets U.S. Federal Civilian Executive Branch (FCEB) agencies; it is not a telco-specific standard.[34] It says AI-assisted techniques can support incident triage, scoping, timeline reconstruction and summarization.[34] Actions with material operational, legal or privacy consequences should remain subject to human review and established incident criteria.[34] For an operator, use AI to assemble incident context and evidence, not to make a network-impacting decision on its own.

Limited, reversible automation still has a role. An operator might pre-authorize revocation of a short-lived credential tied to one agent run, with a NOC alert and a recorded reason. The accountable service owner should decide any action that could affect customers or network continuity, and accept its temporary impact. Automated actions should stay within tested limits that leadership has accepted.

The operator does not need to establish that an intrusion used AI before preparing for shorter response windows. Plans should reflect what an attacker can do, how quickly it may act, and which services the operator must keep running.

## The question for leadership

A CISO or CTO should know the answers to four questions before an incident begins:

- Which actions are pre-approved, and who can authorize broader containment after hours?
- Which service dependencies and fallbacks must be checked before isolating an identity or supplier connection?
- Who owns regulator and customer notifications while technical scoping continues?
- Who accepts temporary service impact, sets the conditions for restoring service, and confirms when the fallback was last exercised?

If these answers are unclear, teams will debate roles and impact while the incident unfolds. Containment without service context can create a second service incident.

Chapter 1 explained why risk has changed. Chapter 2 mapped where exposure can enter and spread. This chapter connected response time, decision authority and service continuity. Chapter 4 turns those concerns into four practical moves for a service-provider CISO or CTO over the next twelve months.
