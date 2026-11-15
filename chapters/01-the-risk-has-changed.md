# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

Four recurring operational examples—the NOC assistant, shared edge/core account, supplier diagnostic feature and deferred patch—are illustrative composites, not reports of operator outcomes.

In this NOC scenario, an alarm assistant should help the network operations center (NOC) see more, not less. The same service account that supports alarm summaries can reach neighboring-domain data, open vendor cases and propose a change that would reduce NOC visibility. The proposal was not carried out. The operator must choose whether to keep the account as configured, restrict the assistant to a verified read/draft role, or pause its action path while testing the boundary.

Keeping the shared account avoids immediate change work but leaves broad reach and weak attribution. Separating read from action may require supplier and engineering support; pausing may push alarm review and case handling back to NOC staff. Keep a read/draft path only if the target systems refuse disallowed actions, logs identify the actor, and an alternative NOC view survives revocation. Otherwise, pause the action path until those conditions are shown. Verify the boundary in a safe environment and estimate the NOC workload before choosing.

A cyber incident at a service provider can become a service incident quickly. When a mobile network, core platform or management system is affected, customers may lose connectivity, businesses may lose services they depend on, and public services may lose an important channel. The operator has to restore service while it is still establishing what happened and how far the impact reaches.

That responsibility is familiar. What has changed is how many systems can act, how quickly activity can move between them, and whether decision authority still matches ownership of the service.

A 2025 Cisco article describes edge compute for mobile-network workloads. A workload placed on edge compute, an operator cloud or a public cloud changes where its data resides, which systems connect and who is responsible for securing it. AI capabilities may be embedded in products for customer care, service assurance, fraud management and internal operations. A tool that summarizes an alarm is different from an agent that can query inventory, open a supplier case or trigger a workflow. The key question is what it can reach and do, and what happens to the service if it gets that wrong.

AI changes who can act inside the operator, not just how teams detect threats. Detection tools help surface activity; an agent may hold a trusted identity, select tools and move information into a workflow. Those are related but different investment problems. The CISO and CTO need to decide what authority can be delegated, how external threats can be contained without unsafe service changes, and who owns the consequences for the service.

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. The degree of dependence varies by country and service, but an outage can affect organizations the operator does not control. This is one reason a service provider’s security decisions cannot be separated from its continuity obligations.

ENISA’s 2026 NIS360 assessment places telecommunications among the EU’s most mature and critical sectors. It defines criticality through digitalization, socioeconomic impact and how quickly consequences can spread across sector interconnections. The report also identifies legacy systems and budget constraints as barriers to timely remediation, particularly in telecommunications.

Those findings should not be read as a claim that every operator has the same risk profile. They describe a familiar tension: a control may be well understood, while the safe path to implement it depends on a long-lived platform, a supplier, a change window and the service owner’s tolerance for disruption. ENISA reports that 60% of surveyed companies across telecoms, core internet and trust services prioritize identified risks, define treatment plans and monitor progress. It also says that consistent exercises of response and recovery arrangements remain an area of focus across digital infrastructure, particularly for high-impact scenarios.

A control shifts risk; it does not remove it. Closing an access path may reduce compromise exposure, while an unsafe change can increase outage risk. A shared identity may simplify support but weaken attribution. Severity alone does not rank these choices: compare exposure while waiting with service impact and the safety and cost of remediation, including a supported change, tested interim control, narrower use or deferral.

Security competes with network growth, service-quality work and customer investment for engineering time, change windows and budget. Name the work that would move and the service outcome the investment should protect; include testing, monitoring and a safe pause or rollback in the estimate. A stated “low tolerance for cyber risk” does not settle that service trade-off. Chapter 4 sets out the operational sequence; Chapter 5 shows how the board challenges funding and residual risk without taking operational ownership.

The live-core patch case makes the trade-off concrete: a fixed version is known, but the next supported window is three weeks away.

## Recent telco cases require careful attribution

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos. In one instance, the actor used a zero-day exploit to bypass a perimeter firewall; in another, it used rootkits to maintain access and evade detection. The whole-of-government response, conducted in partnership with the telcos, lasted more than eleven months and involved over 100 cyber defenders across agencies.

The actor reached parts of the telco networks, with limited access to critical systems in one case. The operation also involved exfiltration of a small amount of primarily network-related technical data. Authorities reported no evidence at that point that sensitive or personal customer data had been accessed or exfiltrated, or that service had been disrupted.

For leadership, keep the impact categories separate: network information, customer data, service availability and operational control. Confirmed exfiltration of technical data remains material even though authorities reported no evidence of customer-data access or service disruption. State both the finding and the limits of the investigation.

The disclosure illustrates the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government. It does not report AI use. Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

A separate set of public claims from November 2026 needs the same care. On 10 November, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation. Cisco’s advisory describes an unauthenticated remote file-read risk and lists fixed software releases.

On 8 November, Malbear Labs published its account of an exposed operational workspace. The researchers describe a largely autonomous, AI-enabled intrusion lasting more than two weeks against an unnamed European telecom provider and organizations it hosts. They report a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.

CISA’s 10 November KEV entry cites evidence of active exploitation; Cisco’s 13 November advisory says Cisco has no direct evidence of active exploitation. These are separate statements about the vulnerability, not confirmation of Malbear Labs’ claimed link to its intrusion. The victim is unnamed, and public sources reviewed here do not independently confirm every reported outcome.

The KEV entry is evidence of exploitation somewhere, not proof that a particular operator runs an affected release or exposes a reachable path. The local decision needs four facts: deployed version, reachable exposure, effectiveness of any interim controls, and the earliest supported fix with rollback. Security and platform teams establish the first two; control owners evidence the interim measures; engineering and the supplier confirm safe change conditions. A KEV listing warrants action, not an unsupported live-core change.

For the board, request the time and supplier access needed to verify the local path, then use Chapter 5’s reporting and acceptance framework for the decision.

In Singapore, the response began when telcos notified IMDA and CSA, then continued through a joint effort to contain the breach and expand monitoring. Notification paths and escalation relationships are easier to use when they are clear before an incident. They are difficult to improvise while technical teams are trying to preserve service and establish scope.

## Edge transformation is a security decision too

Moving workloads closer to users and network functions can make a strong business case: lower latency, better service performance and new operating models. Security questions can arrive later, once the platform choice and deployment plan are already in motion. That sequence can make a manageable design issue expensive to correct.

**Platform selection or retrofit.** In this edge-platform case, selection came before security review. Its shared service account reaches edge nodes and parts of the core; remediation now depends on supplier configuration and a safe window.

Before selecting a platform that can reach production services, the CISO, CTO, Architecture, Network Operations and Procurement should decide what evidence is a condition of selection or rollout. Compare three routes: require demonstrated target-native identities and attributable logs before contract, choosing another platform if the supplier cannot prove them; select conditionally with a funded, supplier-supported remediation and a limit on production reach; or accept the current design and its broad path. The first may narrow vendor choice and delay procurement, but preserves negotiation leverage. Conditional selection keeps options open but needs an owner, deadline, budget and interim boundary. Acceptance is fastest, but transfers the work to a later service-change window and leaves less leverage over the supplier.

For the platform already selected, do not treat it as a sunk cost that makes broad access inevitable. Chapter 4 owns supported migration and interim-boundary tests; Chapter 5 owns the funding and service-risk choice. If no safe boundary can be supported, compare replacement with retrofit, including migration and continuity impact.

For each AI-enabled use, the operator needs to understand what the system can access and change, whether an unsafe action can be stopped, and how the service continues during containment. A summarization tool presents a different risk profile from an agent that can call tools, alter records or trigger a workflow. In service assurance, access to alarms and tickets is not the same as authority to change a network configuration.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. The change is delegated authority across connected systems.

The NOC assistant at the opening makes the distinction concrete: do not give read-only summaries and network changes the same identity simply because one assistant supports both. Keep a proposed change in the operator’s normal change path, and verify that the target system—not just the prompt—enforces that boundary.

In May 2026, CISA and the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), alongside other U.S. and international partners, published a joint guide to securing agentic AI. It identifies four risks: a larger attack surface, privilege creep, behavior that departs from intended goals, and event records that are hard to interpret. The guide recommends starting with low-risk, non-sensitive use cases, avoiding broad access to sensitive data or critical systems, and accounting for agentic AI in the organization’s security model and risk posture. It addresses cross-sector critical-infrastructure risks, not a telco-specific standard.

Those concerns apply where a provider’s customer services meet network and operational processes. An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. For high-impact uses, assurance should establish whether permissions match the task, logs capture tool calls, and access can be revoked without interrupting service.

A public operator example shows that this is not only a future architecture question. In February 2026, Deutsche Telekom reported that its RAN Guardian Agent was live in production in Germany. The company said it had autonomously triggered more than 100 remediation actions at Christmas-market events during its first month and cut the time needed to manage major events from hours to around a minute. These are company-reported figures, not an independent evaluation. The reported outcome is network-event management, not cyber incident response or proof of security-control effectiveness. The announcement described MINDR, a separate multi-domain system, as having first production releases planned for later in 2026. It did not publish RAN Guardian’s action boundaries, rollback or failure rates, or a service-quality baseline. For the CISO and CTO, the useful question is what actions were delegated, how their effects were verified and what service evidence showed the result was safe.

A routine supplier update can add an AI feature without a separate project. If the feature cannot be separated from the release, disabling it may delay operations. Chapter 4 owns that service decision; Chapter 5 the board’s funding for evidence and continuity.

## Two risk questions, not one

AI changes risk along two tracks, and each needs different evidence. The first is internal authority: what an AI-enabled system can read, change or trigger through the identities and tools it has been given. That risk exists even if no attacker uses AI. The second is response speed: whether a threat can move from access to impact faster than the operator can detect it, agree a proportionate response and act without causing unacceptable service disruption.

An inventory can help expose delegated authority, but it does not prove that response is fast enough. A threat-intelligence report may describe compressed attack stages, but it does not show whether a particular operator can safely contain them. These questions meet when an external actor reaches an identity or workflow that already has broad authority. The security program needs visibility into both the path that can be abused and the service’s ability to interrupt it.

When budgets compete, invest where local service evidence identifies the constraint. If the main uncertainty is the reach of a high-impact identity, prioritize mapping and boundary tests; if reach is known but response exercises miss service tolerance, prioritize response authority and fallback. Invest in detection when local evidence shows teams lack the signal or context to act. These are not substitutes: detection does not narrow permissions, identity controls do not accelerate response, and continuity does not prevent misuse. Mapping draws engineering and supplier time; exercises need NOC/SOC backfill; detection requires integration and ongoing tuning. For each choice, name the service outcome, displaced work, evidence for the limitation and what would change the order. Measure efficiency in the operating workflow, not from a demo.

**Fund role readiness, not awareness alone.** General AI awareness can give employees shared language, but it does not prove that an on-call operator can distinguish a proposal from a target action, that IAM can stop downstream sessions, or that a service owner knows when a restriction exceeds tolerance. A dedicated central team can build deep expertise, yet may become a bottleneck or be absent on nights and weekends. Role-based preparation for the named NOC, SOC, IAM, platform, service-owner and supplier contacts takes scarce shift time and backfill, but tests the decisions that keep service running.

Use existing workflows to define the capability: the NOC identifies the service view and fallback; SOC establishes the evidence and affected path; IAM verifies principal, revocation and sessions; Engineering and the supplier confirm target behavior and a supported rollback; the authorized service executive decides within delegation. Train only the people who hold those roles and their deputies, then exercise them across shifts. Measure whether they can find the relevant identity, verify what happened at the target, choose an authorized containment path and preserve the service view. Attendance or a quiz is not evidence that the operational decision works. Fund the role-based exercise when prior tests show missing authority, skill or hand-off; keep broad awareness as a baseline, not a substitute. No training outcome or staffing level is established for the composites.

A faster threat does not automatically justify faster automated containment. In a service provider, blocking an identity or isolating a management path can also remove the NOC’s view of a fault or interrupt service dependencies. More automation may shorten time to act, but it adds integration work and can create service impact when the system lacks the right context. Keeping every decision manual avoids some automatic-action risk but may leave too little time to compare service effects. Start with actions whose scope is narrow and reversal is known; keep changes to shared or core services under NOC and service-owner control. Measure time to safe containment, not just alert receipt or playbook start, alongside service impact, review effort, rollback and fallback. If exercises show approval is the delay, refine authority for bounded actions before expanding automatic execution. Chapter 3 develops the containment decision and continuity tests.

## Response speed is part of the risk

The Canadian Centre for Cyber Security’s cross-sector evidence on attack speed reinforces the risk, but it is not a telecom incident or an operator response target. Chapter 3 examines what the bulletin reports and how the operator should translate that signal into response readiness.

The operator’s concern is not a universal response clock. It is the time available to make a safe decision while limiting service impact. Teams still need to preserve service, test changes across complex estates, coordinate with suppliers and meet local obligations. Legacy systems can slow remediation, and response exercises need to test how teams work together. No operator can close every gap at once.

When an external threat or internal agent can change a critical workflow faster than normal approvals, the executive discussion needs to cover how quickly the operator can detect and contain it, and what service could be affected by containment. Who can stop the change? Can the team do so without losing the visibility needed to manage the network? Security, Network, IT, Operations, Procurement, Legal and business leaders may each hold part of the answer.

## Regulation does not replace operational ownership

Service providers face cybersecurity and privacy laws, communications-sector rules, resilience expectations, reporting duties, supplier contracts and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law. Duties vary by service and country, so a multinational operator cannot assume that one compliance answer fits every market.

Regulation sets obligations; it does not decide who may grant an agent authority or what evidence is needed before that authority expands. Use existing service and change governance. Chapters 2–4 cover access and operational evidence; Chapter 5 covers board oversight and the distinction between binding duties and proposals.

## Set boundaries before expanding use

Operators have good reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

A bounded task with limited service impact can be a sensible place to start. The relevant question is not whether a use is “AI for the business” or “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

“Low risk” depends on the operator and service. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator’s existing risk governance can set the boundary, monitor the use and require stronger assurance as authority grows.

For the NOC assistant, Chapter 4 defines the operational gate and fallback; Chapter 5 turns that evidence into a funding choice. A value pilot can test task benefit, but it does not reduce account reach.

## Three shifts for the next twelve months

The next-year discussion does not need to settle every technical question. It can focus on three shifts within the operator’s existing plans.

**Treat AI as part of the attack surface and operating model.** For consequential uses, know the identity, data, tools, supplier, owner and actions involved, including whether task context persists into later runs. If the operator does not know where a capability is used, it cannot make a grounded decision about how much authority it should have.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans should reflect the service and its dependencies, not only the system under investigation.

**Keep accountability in step with autonomy.** As the workflow gains access or action rights, tighten its permitted scope, test the stop path and show operators how to recover. Supplier assurance informs the choice; it cannot establish how the operator’s own service behaves.

These shifts can help a CISO or CTO select three or four priorities for the next twelve months and explain them to the CEO and board. First, understand where delegated authority can enter and how far it can reach; Chapter 2 maps the identities, data, suppliers and workflows. Chapter 3 tests safe response, Chapter 4 turns the gaps into four operational moves, and Chapter 5 converts evidence into funded decisions and board oversight. Use this sequence to choose priorities that fit the operator’s service and change capacity.
