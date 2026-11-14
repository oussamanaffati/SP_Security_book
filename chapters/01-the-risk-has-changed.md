# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

An alarm assistant should help the network operations center (NOC) see more, not less. Here, the same service account that supports alarm summaries can reach neighboring-domain data, open vendor cases and propose a change that would reduce NOC visibility. The facts establish a proposal, not a completed network change. The operator must choose whether to keep the account as configured, restrict the assistant to a verified read/draft role, or pause its action path while testing the boundary.

Keeping the shared account avoids immediate change work but leaves broad reach and weak attribution. Separating read from action may require supplier and engineering support; pausing may push alarm review and case handling back to NOC staff. Keep a read/draft path only if the target systems refuse disallowed actions, logs identify the actor, and an alternative NOC view survives revocation. Otherwise, pause the action path until those conditions are shown. Verify the boundary in a safe environment and estimate the NOC workload before choosing.

A cyber incident at a service provider can become a service incident quickly. When a mobile network, core platform or management system is affected, customers may lose connectivity, businesses may lose services they depend on, and public services may lose an important channel. The operator has to restore service while it is still establishing what happened and how far the impact reaches.

That responsibility is familiar. What has changed is how many systems can act, how quickly activity can move between them, and whether decision authority still matches ownership of the service.

A 2025 Cisco article describes edge compute for mobile-network workloads. A workload placed on edge compute, an operator cloud or a public cloud changes where its data resides, which systems connect and who is responsible for securing it. AI capabilities may be embedded in products for customer care, service assurance, fraud management and internal operations. A tool that summarizes an alarm is different from an agent that can query inventory, open a supplier case or trigger a workflow. The key question is what it can reach and do, and what happens to the service if it gets that wrong.

AI changes who can act inside the operator, not just how teams detect threats. Detection tools help surface activity; an agent may hold a trusted identity, select tools and move information into a workflow. Those are related but different investment problems. The CISO and CTO need to decide what authority can be delegated, how external threats can be contained without unsafe service changes, and who owns the consequences for the service.

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. The degree of dependence varies by country and service, but an outage can affect organizations the operator does not control. This is one reason a service provider’s security decisions cannot be separated from its continuity obligations.

ENISA’s 2026 NIS360 assessment places telecommunications among the EU’s most mature and critical sectors. It defines criticality through digitalization, socioeconomic impact and how quickly consequences can spread across sector interconnections. The report also identifies legacy systems and budget constraints as barriers to timely remediation, particularly in telecommunications.

Those findings should not be read as a claim that every operator has the same risk profile. They describe a familiar tension: a control may be well understood, while the safe path to implement it depends on a long-lived platform, a supplier, a change window and the service owner’s tolerance for disruption. ENISA reports that 60% of surveyed companies across telecoms, core internet and trust services prioritize identified risks, define treatment plans and monitor progress. It also says that consistent exercises of response and recovery arrangements remain an area of focus across digital infrastructure, particularly for high-impact scenarios.

A control changes the balance between compromise risk and service risk. The operator has to compare both. A change that closes a path but creates an unsafe maintenance event may not improve the service’s overall position.

That choice is rarely a simple contest between “secure” and “available.” A change can reduce the chance of compromise while increasing the chance of an outage during implementation. A shared identity can simplify support while making attribution and containment harder. The useful decision is which treatment gives the service the better overall position, with the operational cost and the remaining exposure both visible.

The live-core patch decision developed in Chapter 4 starts with a difficult interval: the platform has a known fixed version, but safe deployment depends on a maintenance window, rollback plan and supplier confirmation. The next suitable window is three weeks away. That is a scheduling fact, not evidence that service risk has been accepted. The service executive compares local impact and tested interim controls with an earlier supported change or temporary restriction under Chapter 5’s authority model. This interval belongs to the case, not to a universal patching benchmark.

The balance changes if the supplier confirms an earlier safe window, if interim controls can be demonstrated, or if exploitation evidence materially changes. Chapter 4 develops the operational comparison and verification; this chapter uses the case to show why a schedule alone does not settle a service decision.

“Low tolerance for cyber risk” does not settle a live-service trade-off. Management still has to compare the service impact of waiting with the impact of an unsafe change. Chapter 5 shows how the board can challenge that choice without taking operational ownership.

Operators also invest in coverage, capacity, spectrum, cloud, fiber and customer experience. Security competes for the same engineering time, change windows and budget. A credible proposal states what work would move, which service or customer impact it would avoid, and what evidence shows the change is safe. Deferring security investment may preserve capacity for another objective, but it also leaves a path open; the board should see both sides rather than treating delay as free.

Technical severity is a starting point, not the decision. The same weakness may call for different treatment depending on the service dependencies, threat, exposure, control effectiveness and safe-remediation cost. The realistic choices may be an immediate change, a stronger interim control, reduced use of the affected capability or deferral. Compare the exploitation risk while waiting with the outage risk of changing, then name the service outcome that would make the proposed investment worthwhile. Chapter 4 turns that comparison into an implementation sequence.

For an AI-enabled process that can affect a live service, the business case should include testing, monitoring and a safe way to pause or reverse actions. Otherwise, the apparent efficiency gain leaves out a material continuity cost.

## Recent telco cases require careful attribution

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos. In one instance, the actor used a zero-day exploit to bypass a perimeter firewall; in another, it used rootkits to maintain access and evade detection. The whole-of-government response, conducted in partnership with the telcos, lasted more than eleven months and involved over 100 cyber defenders across agencies.

The actor reached parts of the telco networks, with limited access to critical systems in one case. The operation also involved exfiltration of a small amount of primarily network-related technical data. Authorities reported no evidence at that point that sensitive or personal customer data had been accessed or exfiltrated, or that service had been disrupted.

For leadership, keep the impact categories separate: network information, customer data, service availability and operational control. Confirmed exfiltration of technical data remains material even though authorities reported no evidence of customer-data access or service disruption. State both the finding and the limits of the investigation.

The disclosure illustrates the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government. It does not report AI use. Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

A separate set of public claims from November 2026 needs the same care. On 10 November, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation. Cisco’s advisory describes an unauthenticated remote file-read risk and lists fixed software releases.

On 8 November, Malbear Labs published its account of an exposed operational workspace. The researchers describe a largely autonomous, AI-enabled intrusion lasting more than two weeks against an unnamed European telecom provider and organizations it hosts. They report a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.

CISA’s 10 November KEV entry cites evidence of active exploitation; Cisco’s 13 November advisory says Cisco has no direct evidence of active exploitation. These are separate statements about the vulnerability, not confirmation of Malbear Labs’ claimed link to its intrusion. The victim is unnamed, and public sources reviewed here do not independently confirm every reported outcome.

The KEV entry is evidence of exploitation somewhere, not proof that a particular operator runs an affected release or exposes a reachable path. The local decision needs four facts: deployed version, reachable exposure, effectiveness of any interim controls, and the earliest supported fix with rollback. Security and platform teams establish the first two; control owners evidence the interim measures; engineering and the supplier confirm safe change conditions. Chapter 5 sets out the acceptance boundary. A KEV listing warrants action, not an unsupported live-core change.

In Singapore, the response began when telcos notified IMDA and CSA, then continued through a joint effort to contain the breach and expand monitoring. Notification paths and escalation relationships are easier to use when they are clear before an incident. They are difficult to improvise while technical teams are trying to preserve service and establish scope.

## Edge transformation is a security decision too

Moving workloads closer to users and network functions can make a strong business case: lower latency, better service performance and new operating models. Security questions can arrive later, once the platform choice and deployment plan are already in motion. That sequence can make a manageable design issue expensive to correct.

The edge platform was selected before security review. Its shared service account can reach edge nodes and parts of the core; remediation requires a maintenance window and supplier configuration change. This does not make the platform inherently unsafe. It shows how an early identity choice can narrow later options: once the platform is selected, separation and rollback become service-change work rather than design choices.

An earlier map would not remove supplier or maintenance constraints, but it would expose them before platform selection. That is the executive value of early security review: preserve options while they are cheaper to change. Chapter 2 traces the identity paths; Chapter 4 addresses implementation.

The decision is not simply whether the edge platform is “secure.” It is which identities must cross which boundaries, how to attribute each action and how to contain access without losing service. Separating identities adds engineering and supplier work; leaving the shared identity preserves support simplicity but leaves a wider path to manage. Compare those costs before rollout, while architecture and fallback are still adjustable.

For each AI-enabled use, the operator needs to understand what the system can access and change, whether an unsafe action can be stopped, and how the service continues during containment. A summarization tool presents a different risk profile from an agent that can call tools, alter records or trigger a workflow. In service assurance, access to alarms and tickets is not the same as authority to change a network configuration.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. The change is delegated authority across connected systems.

The NOC assistant at the opening makes the distinction concrete: do not give read-only summaries and network changes the same identity simply because one assistant supports both. Keep a proposed change in the operator’s normal change path, and verify that the target system—not just the prompt—enforces that boundary.

In May 2026, CISA and the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), alongside other U.S. and international partners, published a joint guide to securing agentic AI. It identifies four risks: a larger attack surface, privilege creep, behavior that departs from intended goals, and event records that are hard to interpret. The guide recommends starting with low-risk, non-sensitive use cases, avoiding broad access to sensitive data or critical systems, and accounting for agentic AI in the organization’s security model and risk posture. It addresses cross-sector critical-infrastructure risks, not a telco-specific standard.

Those concerns apply where a provider’s customer services meet network and operational processes. An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. For high-impact uses, assurance should establish whether permissions match the task, logs capture tool calls, and access can be revoked without interrupting service.

A public operator example shows that this is not only a future architecture question. In February 2026, Deutsche Telekom reported that its RAN Guardian Agent was live in production in Germany. The company said it had autonomously triggered more than 100 remediation actions at Christmas-market events during its first month and cut the time needed to manage major events from hours to around a minute. These are company-reported figures, not an independent evaluation. The reported outcome is network-event management, not cyber incident response or proof of security-control effectiveness. The announcement described MINDR, a separate multi-domain system, as having first production releases planned for later in 2026. It did not publish RAN Guardian’s action boundaries, rollback or failure rates, or a service-quality baseline. For the CISO and CTO, the useful question is what actions were delegated, how their effects were verified and what service evidence showed the result was safe.

The supplier diagnostic feature returns in Chapter 4 as a decision problem: a routine product update can add a capability without a separate AI project. The investment is not only the cost of reviewing it. If disabling the feature delays operations or release cannot be separated from activation, compare that service cost with the exposure of enabling an unverified identity or action path.

## Two risk questions, not one

AI changes risk along two tracks, and each needs different evidence. The first is internal authority: what an AI-enabled system can read, change or trigger through the identities and tools it has been given. That risk exists even if no attacker uses AI. The second is response speed: whether a threat can move from access to impact faster than the operator can detect it, agree a proportionate response and act without causing unacceptable service disruption.

An inventory can help expose delegated authority, but it does not prove that response is fast enough. A threat-intelligence report may describe compressed attack stages, but it does not show whether a particular operator can safely contain them. These questions meet when an external actor reaches an identity or workflow that already has broad authority. The security program needs visibility into both the path that can be abused and the service’s ability to interrupt it.

When budgets compete, invest where local service evidence identifies the constraint. If the main uncertainty is the reach of a high-impact identity, prioritize mapping and boundary tests; if reach is known but response exercises miss service tolerance, prioritize response authority and fallback. Invest in detection when local evidence shows teams lack the signal or context to act. These are not substitutes: detection does not narrow permissions, identity controls do not accelerate response, and continuity does not prevent misuse. Mapping draws engineering and supplier time; exercises need NOC/SOC backfill; detection requires integration and ongoing tuning. For each choice, name the service outcome, displaced work, evidence for the limitation and what would change the order. Measure efficiency in the operating workflow, not from a demo.

A faster threat does not automatically justify faster automated containment. In a service provider, blocking an identity or isolating a management path can also remove the NOC’s view of a fault or interrupt service dependencies. More automation may shorten time to act, but it adds integration work and can create service impact when the system lacks the right context. Keeping every decision manual avoids some automatic-action risk but may leave too little time to compare service effects. Start with actions whose scope is narrow and reversal is known; keep changes to shared or core services under NOC and service-owner control. Measure time to safe containment, not just alert receipt or playbook start, alongside service impact, review effort, rollback and fallback. If exercises show approval is the delay, refine authority for bounded actions before expanding automatic execution. Chapter 3 develops the containment decision and continuity tests.

**NOC assistant benefit check.** The scenario establishes alarm summaries and draft ticket updates, not time saved or output quality. Before funding expansion, compare the current and assisted workflows on a similar task mix and service conditions, using approved representative or synthetic inputs. Measure time to an operator-accepted result, including review, corrections and hand-offs; the time to a generated answer is not the service outcome.

| Decision question | Compare | Evidence before expansion |
|---|---|---|
| Does it improve the task? | Current and assisted time from alarm receipt to an operator-accepted summary or ticket update, including review, corrections and hand-offs. | Baseline and assisted results for a similar task mix and service conditions; use approved representative or synthetic inputs. |
| Is the result usable? | Missing or misleading context, corrections, escalations and manual fallback. | Operational review of whether the output supports the decision; no performance threshold is assumed here. |
| What is the full cost? | Supplier/model charges, review effort, broader identity or data scope, supplier hand-offs and fallback workload. | Estimate basis, which teams absorb the work and which costs remain unknown. |
| Does authority stay bounded? | Whether the assistant remains read/draft and whether the target can reject a disallowed action. | Test the path, actor logs and revocation before expansion; efficiency alone does not authorize execution. |

No operator trial or measured result is established here. Keep the assistant advisory until the comparison shows a net service benefit without removing necessary review or broadening authority beyond a tested boundary.

Chapters 2 and 3 treat those questions separately.

## Response speed is part of the risk

The Canadian Centre for Cyber Security’s cross-sector evidence on attack speed reinforces the risk, but it is not a telecom incident or an operator response target. Chapter 3 examines what the bulletin reports and how the operator should translate that signal into response readiness.

The operator’s concern is not a universal response clock. It is the time available to make a safe decision while limiting service impact. Teams still need to preserve service, test changes across complex estates, coordinate with suppliers and meet local obligations. Legacy systems can slow remediation, and response exercises need to test how teams work together. No operator can close every gap at once.

When an external threat or internal agent can change a critical workflow faster than normal approvals, the executive discussion needs to cover how quickly the operator can detect and contain it, and what service could be affected by containment. Who can stop the change? Can the team do so without losing the visibility needed to manage the network? Security, Network, IT, Operations, Procurement, Legal and business leaders may each hold part of the answer.

## Regulation does not replace operational ownership

Service providers face cybersecurity and privacy laws, communications-sector rules, resilience expectations, reporting duties, supplier contracts and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law. Duties vary by service and country, so a multinational operator cannot assume that one compliance answer fits every market.

Compliance cannot decide which agent may change a network configuration or what evidence is enough before its authority expands. Make those choices through the operator’s existing service and change governance. Chapter 5 shows how the board can challenge the resulting decision without replacing operational ownership.

Existing security, architecture, change and supplier-risk reviews are usually the simplest place to start. Those reviews can account for each machine identity, the data it can reach, the actions it can take and how those actions can be reversed. Operators do not need perfect certainty before they begin. They can identify the owner and service impact of each consequential use, then define what evidence is needed before its authority expands.

## Set boundaries before expanding use

Operators have good reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

A bounded task with limited service impact can be a sensible place to start. The relevant question is not whether a use is “AI for the business” or “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

“Low risk” depends on the operator and service. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator’s existing risk governance can set the boundary, monitor the use and require stronger assurance as authority grows.

Do not confuse the safest pilot with the first risk to treat. The NOC assistant may be a candidate for a bounded read/draft value test, but the shared edge/core account calls for identity review before expanding automation to that platform. Those choices can run in parallel only if staff and test capacity allow. If they compete for the same people or change window, prioritize the unverified path with the larger service reach and keep the pilot inside a scope that preserves NOC visibility. Record different success evidence: measured operator benefit for the pilot; verified reach, revocation and service fallback for the access review. A positive pilot result does not clear another identity path.

## Three shifts for the next twelve months

The next-year discussion does not need to settle every technical question. It can focus on three shifts within the operator’s existing plans.

**Treat AI as part of the attack surface and operating model.** For consequential uses, know the identity, data, tools, supplier, owner and actions involved, including whether task context persists into later runs. If the operator does not know where a capability is used, it cannot make a grounded decision about how much authority it should have.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans should reflect the service and its dependencies, not only the system under investigation.

**Keep accountability in step with autonomy.** As the workflow gains access or action rights, tighten its permitted scope, test the stop path and show operators how to recover. Supplier assurance informs the choice; it cannot establish how the operator’s own service behaves.

These shifts can help a CISO or CTO select three or four priorities for the next twelve months and explain them to the CEO and board. First, understand where delegated authority can enter and how far it can reach; Chapter 2 maps the identities, data, suppliers and workflows. Chapter 3 tests safe response, Chapter 4 turns the gaps into four operational moves, and Chapter 5 converts evidence into funded decisions and board oversight. Use this sequence to choose priorities that fit the operator’s service and change capacity.
