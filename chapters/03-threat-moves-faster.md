# Chapter 3: The Threat Moves Faster Than the Operator Can Respond

A threat does not have to outrun every security tool. It only has to move faster than the organization can make a safe decision.

That is the uncomfortable part for a service provider. A SOC can see an alert. The NOC can see that a planned change is underway. Identity teams can revoke a credential. The supplier may have information about the platform. But if no one knows who can authorize containment, the operator loses time while the network keeps carrying traffic and the attacker keeps working.

Chapter 2 asked where exposure can enter and spread. This chapter asks a different question: **when activity is moving, can the operator detect it, decide what to do, and act before the next material step, without creating a second incident through unsafe containment?**

## The clock is getting shorter, but not every attack is autonomous

AI has already made it easier to find weaknesses, develop malicious code and target many organizations at once.[14]
Agentic AI goes further by linking separate stages of an attack with less human direction.[14]
That does not mean every attacker is using an agent, or that every attack now unfolds at machine speed.[14]
We need to be precise.

In an October 2026 bulletin, the Canadian Centre for Cyber Security says attacks are not yet fully autonomous. Humans still choose targets, set objectives and oversee the operation, while more work between those decisions can be delegated to machines.[14]

The same bulletin describes activity attributed to Storm-0940 using an agentic framework. In some cases, the activity moved from target selection to privileged access to cloud systems in less than three hours.[14]
The bulletin is not telecom-specific. It is a warning about the speed at which an adversary can move through ordinary weaknesses, not proof that a telco has been attacked this way.

CERT-In reported a related pattern in October 2026. In a financially motivated campaign against Indian entities, the agency said agentic tooling compressed the time from initial access to impact from days to a few hours. It also reported parallel agent operations and repeat attacks within days when remediation was incomplete.[11]
Those observations do not establish a universal attacker timeline. They do show why “we will fix it in the next window” is a dangerous default when exploitation is confirmed.

The important point is not simply faster scanning. It is the shrinking interval between one step and the next. A stolen identity can be reused. A tool can search broadly. A partial fix can leave another route open. When the attacker can repeat actions quickly, defenders may need to contain first and understand fully in parallel.

That is a different operating problem from having good detection. A dashboard can show the event. It cannot, by itself, decide whether to revoke the identity, isolate the host, block the supplier connection, or keep a service running in a reduced mode.

## The operator has more than one clock

Incident response is often described as a technical sequence: detect, investigate, contain, recover. In practice, those activities overlap. The NOC may be confirming whether an alarm matches a real network change. The SOC may be deciding whether the activity is malicious. IAM may need to disable an account. Service assurance may be estimating which customers or services could be affected. Legal, regulatory and communications teams may already be working against notification deadlines.

At the same time, the network cannot wait for every team to finish its analysis. Nor can the operator treat every system as disposable. A management platform may support several network domains. An identity may be shared across automation jobs. A supplier connection may be needed to restore a service even as the supplier helps investigate it. Availability changes the containment decision.

A useful way to think about the gap is to separate four clocks:

- **Detection:** How long before someone recognizes that the event may be malicious?
- **Decision:** How long before an authorized person chooses a containment action?
- **Action:** How long before teams execute it safely and confirm the result?
- **Continuity and recovery:** How long before affected services can run safely again?

A fast SOC does not guarantee a fast response if the decision clock is slow. A quick isolation does not mean the response is successful if it breaks a critical workflow or removes the telemetry needed to understand what happened. The measures have to be connected.

This is where NOC and SOC coordination matters. The SOC understands the evidence and the likely attack path. The NOC understands which systems are carrying live operations, what maintenance is in progress, and what a particular isolation could do to service. Neither view is sufficient alone. Each needs a clear route to the other, with someone empowered to decide when there is no time for a long discussion.

## A telecom breach has several timelines

The South Korean Ministry of Science and ICT’s investigation into the 2025 SK Telecom breach is a useful reminder that the response clock includes more than containment. The Ministry reports that SK Telecom detected abnormally large outbound traffic at 11:20 p.m. on 18 April 2025, then notified KISA at 4:46 p.m. on 20 April, beyond the statutory 24-hour reporting window.[15]

That is a reporting timeline, not a measurement of how long the company took to contain the intrusion. The distinction matters. The government’s public-private investigation team was established on 23 April and conducted forensic inspections across all 42,605 SK Telecom servers through 27 June. Its final findings identified 28 infected servers.[15]
Establishing the full scope took sustained work across the operator and government investigators.

The customer response had its own operational demands. In its preliminary findings, the Ministry encouraged subscribers to replace their USIM cards or use a protection service, and urged the operator to expand service channels and add a reservation system so more customers could be protected promptly.[16]
These reports are useful here for their breach-response timeline, not as an example of a network outage. They show how an incident can create a second workload: protecting customers, handling enquiries and changing business operations while the technical investigation is still under way.

There is no single clock. The initial signal, statutory notification, technical scoping and customer protection each have different owners and deadlines. If those responsibilities are not connected before an incident, the organization may be trying to create a response structure at the same time it is trying to contain an attacker.

## Containment is a service decision

For an ordinary office system, “isolate it” may sound straightforward. In a provider environment, the same action can have different consequences depending on the system’s role. Cutting a compromised supplier connection may slow recovery. Disabling a shared identity may stop a legitimate monitoring workflow. Isolating a management host may reduce an attacker’s access but also remove a source of operational visibility.

That does not mean the operator should wait. It means the available actions should be designed and authorized in advance. The Canadian Cyber Centre recommends deciding ahead of time who can isolate an account, application, network or service, and practising for incidents that unfold within hours rather than days.[14]
For critical infrastructure, it also recommends identifying the minimum functions that must continue, defining pre-authorized isolation steps, and testing safe manual or alternative operation.[14]

Those are practical questions for a telco. Which identities can the SOC revoke immediately without NOC approval? Which systems can be isolated while the network remains stable? If a tool or supplier connection must be stopped, what is the fallback? Who can authorize a change outside the normal maintenance window, and who records the decision? Which services must not be interrupted, and what reduced mode is acceptable?

“Call the incident commander” is not enough if the commander has no authority to act. “Follow the change process” is not enough if the process assumes there is time to schedule a meeting. The emergency route has to be legitimate, documented and rehearsed. It should preserve the evidence and service context needed for the next decision.

## A composite NOC/SOC scenario

Consider a composite scenario, not a reported incident. During a planned maintenance window, the SOC sees unusual privileged calls from an identity used by a network-management integration. The calls are consistent with the work in progress, but the volume and destinations are not. The NOC confirms that a change is active and warns that disabling the shared identity could interrupt monitoring for more than one network domain. A supplier says a software update may explain the behavior, but cannot confirm that immediately.

The threat is uncertain. The service impact is not. The operator now has to choose between waiting for more evidence, revoking the identity, or isolating the integration path and accepting reduced visibility while the incident is investigated. If the identity is compromised, each minute of delay may give the attacker more reach. If the operator disables too much, the response itself could hide faults or interfere with planned work.

A prepared organization does not ask the SOC analyst to resolve this alone. The SOC validates the evidence and identifies the access path. The NOC explains service dependencies and available fallback. The incident lead uses pre-agreed criteria to choose a bounded action. IAM or platform operations carries it out. The supplier provides technical facts, but does not make the operator’s risk decision. Customer, legal and regulatory leads work in parallel on impact and notification, rather than waiting for the forensic picture to be complete.

The first action might be to revoke a scoped token and pause the affected automation, not shut down an entire management environment. If that is not enough, a defined escalation path can authorize a broader isolation and the corresponding service fallback. The decision, evidence and service impact are logged. The NOC confirms what continues to work. The SOC checks whether the hostile activity has stopped and whether another identity or path remains active.

That is not a perfect answer to every incident. It is a way to make the first decision faster without pretending that availability does not matter. The exact actions must reflect the operator’s architecture and service obligations. A playbook copied from another company will not know which system is safe to stop.

## Use automation to shorten the safe work

AI can help defenders keep up. It can correlate alerts, summarize the affected identities and systems, retrieve the right runbook, draft a regulator update, or identify which teams need to join the response. Those tasks reduce time spent assembling context. They do not need authority to make a network-impacting decision.

Some response actions can be automated when their scope is narrow, their effect is understood, and they are reversible or readily recoverable. An operator might pre-authorize revoking a short-lived credential tied to one agent run, with an alert to the NOC and a recorded reason. AI can gather evidence and recommend the next step, but a named human owner should decide on actions that could affect customers or network continuity. Any automated action should fail within a limit the operator has already accepted.

The same principle applies when AI is on the attacker’s side. Defenders should not wait for proof that a specific intrusion used AI before preparing for shorter timelines. An attacker can use automation without announcing it. The response plan should be based on what the activity can do, how quickly it can move, and what the operator must keep running.

## The question for leadership

A CISO or CTO should be able to answer a few questions without assembling a committee during an incident. Who can authorize account, application or supplier isolation at night? Which actions are pre-approved? What service dependencies must be checked first? Who has authority to accept a temporary reduction in service? Who notifies regulators and customers while technical scoping continues? When was the fallback last tested?

The answers expose whether response speed is really a SOC metric or an operating-model capability. If the same people must debate roles, service impact and approval every time, the next incident will start with avoidable delay. If one team can act without knowing what it will interrupt, the response can become its own outage.

Chapter 1 explained why risk has changed. Chapter 2 mapped where exposure can enter and spread. Chapter 3 has shown why time, authority and service continuity now have to be managed together. Chapter 4 turns that into four practical moves a service-provider CISO or CTO can start in the next twelve months.

## Sources

[11] https://cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02 — CERT-In Advisory CIAD-2026-0049, 15 October 2026
[14] https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-agentic-artificial-intelligence-accelerating-cyber-attacks — Cyber threat bulletin: Agentic artificial intelligence is accelerating cyber attacks, Canadian Centre for Cyber Security, 26 October 2026
[15] https://www.msit.go.kr/eng/bbs/view.do?bbsSeqNo=42&nttSeqNo=1139 — MSIT Releases Final Investigation Results on SK Telecom Data Breach, Ministry of Science and ICT, July 2025
[16] https://www.msit.go.kr/eng/bbs/view.do?bbsSeqNo=42&mId=4&mPid=2&nttSeqNo=1111&pageIndex=&sCode=eng&searchOpt=ALL&searchTxt= — MSIT Releases First Investigation Results on SKT Data Breach, Ministry of Science and ICT, 29 April 2025
