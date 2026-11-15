# Chapter 1: The Risk Has Changed. Service Providers Need More Than Detection.

In this illustrative NOC-assistant case, the NOC wants a clearer view of alarms. The assistant summarizes them, but its account also reaches neighboring-domain data and can open supplier cases. It proposes a change that would reduce the NOC’s view of the network. No change is carried out.

Keeping the account unchanged avoids immediate work but leaves broad reach and weak attribution. Separating read from action may require supplier and engineering support; pausing may push alarm review and case handling back to NOC staff. Keep read-only or draft-only use only if target systems deny disallowed actions, logs identify the actor, and an alternative NOC view survives revocation. Otherwise, pause the action path until those conditions are demonstrated. Test the boundary safely and estimate the NOC workload before choosing.

The other recurring examples are also illustrative composites, not reports of operator outcomes: the shared edge/core account, supplier diagnostic feature and deferred patch.

A cyber incident at a service provider is also a service-continuity problem. If a mobile network, core platform or management system is affected, customers may lose connectivity and organizations may lose services that depend on it. The operator may have to restore service while still establishing what happened and how far the impact reaches.

Delegated authority can cross identities and workflows faster than the operator can trace the path, contain misuse or restore service. External threats create a separate, related speed problem.

A 2025 Cisco article describes edge compute for mobile-network workloads. Whether a workload runs at the edge, in an operator cloud or in a public cloud affects where its data sits, which systems it connects to and which suppliers are involved. Possible AI use cases include customer care, service assurance, fraud management and internal operations. A summary tool and an agent that queries inventory, opens supplier cases or triggers workflows do not carry the same authority. Before enabling the latter, map what it can read and change, and what the operator must keep running if it is stopped.

The CISO and CTO must decide what authority to delegate, how to stop a threat without breaking service, and which executive can authorize that trade-off.

## Networks support services beyond the operator

The degree of dependence varies by country and service, but an outage may affect organizations the operator does not control. That broader impact is why security decisions must account for continuity obligations as well as the operator’s own systems.

ENISA’s 2026 NIS360 assessment places telecommunications among the EU’s most mature and critical sectors. It defines criticality through digitalization, socioeconomic impact and how quickly consequences can spread across sector interconnections. The report also identifies legacy systems and budget constraints as barriers to timely remediation, particularly in telecommunications.

Those findings should not be read as a claim that every operator has the same risk profile. They describe a familiar tension: a control may be well understood, while the safe path to implement it depends on a long-lived platform, a supplier, a change window and the service owner’s tolerance for disruption. ENISA reports that 60% of surveyed companies across telecoms, core internet and trust services prioritize identified risks, define treatment plans and monitor progress. It also says that consistent exercises of response and recovery arrangements remain an area of focus across digital infrastructure, particularly for high-impact scenarios.

Each option changes the service and security trade-off. Closing an access path can reduce compromise exposure; an unsafe change can increase outage risk. A shared identity may simplify support but weaken attribution. Severity alone does not rank these choices. Compare exposure while waiting with service impact and the safety and local cost of a supported change, tested interim control, narrower use or deferral.

Security competes with network growth, service-quality work and customer investment for engineering time, change windows and budget. Name what must move, state the service outcome the investment should protect, and include testing, monitoring and a safe pause or rollback. A general statement of “low tolerance for cyber risk” does not settle the trade-off.

The live-core patch case makes the trade-off concrete: a fixed version is known, but the next supported window is three weeks away.

## Recent telco cases require careful attribution

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos. In one instance, the actor used a zero-day exploit to bypass a perimeter firewall; in another, it used rootkits to maintain access and evade detection. The whole-of-government response, conducted in partnership with the telcos, lasted more than eleven months and involved over 100 cyber defenders across agencies.

The actor reached parts of the telco networks, with limited access to critical systems in one case. The operation also involved exfiltration of a small amount of primarily network-related technical data. Authorities reported no evidence at that point that sensitive or personal customer data had been accessed or exfiltrated, or that service had been disrupted.

For leadership, keep the impact categories separate: network information, customer data, service availability and operational control. Confirmed exfiltration of technical data remains material even though authorities reported no evidence of customer-data access or service disruption. State both the finding and the limits of the investigation.

The disclosure illustrates the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government. It does not report AI use. Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

A separate set of public claims from November 2026 needs the same care. On 10 November, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation. Cisco’s advisory describes an unauthenticated remote file-read risk and lists fixed software releases.

On 8 November, Malbear Labs published its account of an exposed operational workspace. The researchers describe a largely autonomous, AI-enabled intrusion lasting more than two weeks against an unnamed European telecom provider and organizations it hosts. They report a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.

CISA’s 10 November KEV entry cites evidence of active exploitation; Cisco’s 13 November advisory says Cisco has no direct evidence of active exploitation. These are separate statements about the vulnerability, not confirmation of Malbear Labs’ claimed link to its intrusion. The victim is unnamed, and public sources reviewed here do not independently confirm every reported outcome.

The KEV entry is evidence of exploitation somewhere; it does not show whether this operator runs an affected release or exposes a reachable path. Establish the deployed version, reachability, any effective interim control and the earliest supported fix. Security and platform teams verify the local path; Engineering and the supplier confirm change conditions and rollback. A KEV listing warrants action, not an unsupported live-core change.

Leaders should fund the time and supplier access needed to verify the local path before choosing a fix.

In Singapore, the response began when telcos notified IMDA and CSA, then continued through a joint effort to contain the breach and expand monitoring. Notification paths and escalation relationships are easier to use when they are clear before an incident. They are difficult to improvise while technical teams are trying to preserve service and establish scope.

## Edge transformation is a security decision

Operators may place workloads closer to users or network functions to meet service needs or support new operating models. Security review can come after platform selection and deployment planning. By then, a manageable design issue may be expensive to correct.

**Platform selection or retrofit.** In this edge-platform case, selection came before security review. Its shared service account reaches edge nodes and parts of the core; remediation now depends on supplier configuration and a safe window.

Before selection, the CISO, CTO, Architecture, Network Operations and Procurement should agree what evidence is required for rollout. They have three routes: require target-native identities and attributable logs before contract, choosing another platform if the supplier cannot prove them; select conditionally with funded, supplier-supported remediation and limited production reach; or accept the current design and its broad path. The first route may narrow vendor choice and delay procurement, but preserves leverage. Conditional selection keeps the option open and needs an owner, deadline, budget and interim boundary. Acceptance is fastest, but shifts the work to a later service-change window and leaves less leverage over the supplier.

For a selected platform, do not treat it as a sunk cost that makes broad access inevitable. Evaluate a supplier-supported migration and a tested interim boundary; if no safe boundary can be supported, compare retrofit with replacement, including migration and continuity impact.

For each AI-enabled use, the operator needs to understand what the system can access and change, whether an unsafe action can be stopped, and how the service continues during containment. A summarization tool presents a different risk profile from an agent that can call tools, alter records or trigger a workflow. In service assurance, access to alarms and tickets is not the same as authority to change a network configuration.

## AI changes who can act

An AI workflow may only summarize or recommend. An agent may also retrieve information, call tools, hand off work or take actions without a person approving each step. The security distinction is authority across connected systems, not the AI label.

In May 2026, CISA and the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), alongside other U.S. and international partners, published a joint guide to securing agentic AI. It identifies four risks: a larger attack surface, privilege creep, behavior that departs from intended goals, and event records that are hard to interpret. The guide recommends starting with low-risk, non-sensitive use cases, avoiding broad access to sensitive data or critical systems, and accounting for agentic AI in the organization’s security model and risk posture. It addresses cross-sector critical-infrastructure risks, not a telco-specific standard.

Those concerns apply where a provider’s customer services meet network and operational processes. An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. For high-impact uses, assurance should establish whether permissions match the task, logs capture tool calls, and access can be revoked without interrupting service.

A public operator example shows that this is not only a future architecture question. In February 2026, Deutsche Telekom reported that its RAN Guardian Agent was live in production in Germany. The company said it had autonomously triggered more than 100 remediation actions at Christmas-market events during its first month and cut the time needed to manage major events from hours to around a minute. These are company-reported figures, not an independent evaluation.

The reported outcome is network-event management, not cyber incident response or proof of security-control effectiveness. The announcement described MINDR, a separate multi-domain system, as having first production releases planned for later in 2026. It did not publish RAN Guardian’s action boundaries, rollback or failure rates, or a service-quality baseline. For the CISO and CTO, the useful question is what actions were delegated, how their effects were verified and what service evidence showed the result was safe.

In the supplier-feature composite, a routine update may add an AI feature without a separate project. If the feature cannot be separated from the release, disabling it may delay operations. Management needs evidence that it can be disabled without losing required service visibility; leadership then weighs the continuity, supplier and resourcing trade-offs.

## Two risk questions, not one

AI changes risk along two tracks, and each needs different evidence. The first is internal authority: what an AI-enabled system can read, change or trigger through the identities and tools it has been given. That risk exists even if no attacker uses AI. The second is response speed: whether a threat can move from access to impact faster than the operator can detect it, agree a proportionate response and act without causing unacceptable service disruption.

An inventory can help expose delegated authority, but it does not prove that response is fast enough. A threat-intelligence report may describe compressed attack stages, but it does not show whether a particular operator can safely contain them. These questions meet when an external actor reaches an identity or workflow that already has broad authority. The security program needs visibility into both the path that can be abused and the service’s ability to interrupt it.

When budgets compete, invest where local service evidence identifies the constraint. If the main uncertainty is the reach of a high-impact identity, prioritize mapping and boundary tests; if reach is known but response exercises miss service tolerance, prioritize response authority and fallback. Invest in detection when local evidence shows teams lack the signal or context to act. These investments are not substitutes: detection does not narrow permissions, identity controls do not by themselves ensure timely response, and continuity does not prevent misuse.

Mapping draws engineering and supplier time; exercises need NOC/SOC backfill; detection requires integration and ongoing tuning. For each choice, name the service outcome, displaced work, evidence for the limitation and what would change the order. Measure efficiency in the operating workflow, not from a demo.

**Fund role readiness, not awareness alone.** General AI awareness can give employees shared language, but it does not prove that an on-call operator can distinguish a proposal from a target action, that IAM can stop downstream sessions, or that a service owner knows when a restriction exceeds tolerance. A dedicated central team can build deep expertise, yet may become a bottleneck or be absent on nights and weekends. Role-based preparation for the named NOC, SOC, IAM, platform, service-owner and supplier contacts takes scarce shift time and backfill, but tests the decisions that keep service running.

Use the existing workflow to define capability: the NOC names the service view and fallback; the SOC establishes the evidence and affected path; IAM verifies the principal, revocation and sessions; Engineering and the supplier confirm target behavior and rollback. In the recommended governance model, the service executive decides within delegated authority. Train those roles and deputies across shifts. The exercise should test whether they can locate the relevant identity, verify target behavior, choose authorized containment and preserve the service view. Fund training or backfill where the exercise shows a gap; broad awareness alone will not fix it.

A faster threat does not automatically justify faster automated containment. In a service provider, blocking an identity or isolating a management path can also remove the NOC’s view of a fault or interrupt service dependencies. More automation may shorten time to act, but it adds integration work and can create service impact when the system lacks the right context.

Keeping every decision manual avoids some automatic-action risk but may leave too little time to compare service effects. Start with actions whose scope is narrow and reversal is known. Keep changes to shared or core services under NOC and service-owner control. Measure time to safe containment, not just alert receipt or playbook start, alongside service impact, review effort, rollback and fallback. If exercises show approval is the delay, refine authority for bounded actions before expanding automatic execution.

## Response speed is part of the risk

The operator’s concern is not a universal response clock. It is the time available to make a safe decision while limiting service impact. Teams must preserve service, test changes across complex estates, coordinate with suppliers and meet local obligations. Legacy constraints can slow remediation. Exercises should test whether teams can coordinate under pressure; operators must sequence the work around service and change windows.

When an external threat or internal agent can change a critical workflow faster than normal approvals, the executive discussion needs to cover how quickly the operator can detect and contain it, and what service could be affected by containment. Who can stop the change? Can the team do so without losing the visibility needed to manage the network? Security, Network, IT, Operations, Procurement, Legal and business leaders may each hold part of the answer.

## Regulation does not decide who can act

Depending on market and service, a provider may face cybersecurity and privacy laws, communications-sector rules, resilience and reporting duties, supplier contracts, and national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law. Duties vary by service and country, so a multinational operator cannot assume that one compliance answer fits every market.

Regulation sets obligations; it does not decide who may grant an agent authority or what evidence is needed before that authority expands. Use existing service and change governance to translate the applicable duty into access boundaries, operational evidence and board oversight. Keep binding duties distinct from proposals.

## Set boundaries before expanding use

Operators may use AI to improve customer service, automate repetitive work or support network operations. A policy that waits for perfect certainty can leave teams without a governed path for low-impact experiments.

A bounded task with limited service impact can be a sensible place to start. The relevant question is not whether a use is “AI for the business” or “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Assign accountability according to access and service impact, not which team bought the feature.

“Low risk” depends on the operator and service. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator’s existing risk governance can set the boundary, monitor the use and require stronger assurance as authority grows.

For the NOC assistant, a useful task-value pilot cannot show that its account is bounded. Operators need separate evidence for the authority boundary and fallback before deciding whether to expand or fund routine use.

The first decision is not whether to use AI. It is which service an AI-enabled workflow can affect, what evidence shows its reach and how much disruption the service can tolerate. Before granting more authority, trace the identity through its data and tools and name the fallback if the path is stopped.
