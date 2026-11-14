# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

An alarm summary becomes a different security problem when the same service account can also reach neighboring-domain data, open vendor cases and propose a change that would reduce NOC visibility. This is the supplied composite NOC scenario, not a production incident. It gives this book its central question: as software gains access to operator workflows, do boundaries and decision authority keep pace with the consequences for service?

A cyber incident at a service provider can become a service incident quickly. When a mobile network, core platform or management system is affected, customers may lose connectivity, businesses may lose services they depend on, and public services may lose an important channel. The operator has to restore service while it is still establishing what happened and how far the impact reaches.

That responsibility is familiar. What has changed is how many systems can act, how quickly activity can move between them, and whether decision authority still matches ownership of the service.

A 2025 Cisco article describes edge compute for mobile-network workloads.[5] A workload placed on edge compute, an operator cloud or a public cloud changes where its data resides, which systems connect and who is responsible for securing it. AI features are also appearing in customer care, service assurance, fraud management and internal operations. A tool that summarizes an alarm is different from an agent that can query inventory, open a supplier case or trigger a workflow. The key question is what it can reach and do, and what happens to the service if it gets that wrong.

AI changes who can act inside the operator, not just how teams detect threats.[3] Detection tools help surface activity; an agent may hold a trusted identity, select tools and move information into a workflow. Those are related but different investment problems. The CISO and CTO need to decide what authority can be delegated, how external threats can be contained without unsafe service changes, and who owns the consequences for the service.

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. The degree of dependence varies by country and service, but an outage can affect organizations the operator does not control. This is one reason a service provider’s security decisions cannot be separated from its continuity obligations.

ENISA’s 2026 NIS360 assessment places telecommunications among the EU’s most mature and critical sectors. It defines criticality through digitalization, socioeconomic impact and how quickly consequences can spread across sector interconnections.[2] The report also identifies legacy systems and budget constraints as barriers to timely remediation, particularly in telecommunications.[2]

Those findings should not be read as a claim that every operator has the same risk profile. They describe a familiar tension: a control may be well understood, while the safe path to implement it depends on a long-lived platform, a supplier, a change window and the service owner’s tolerance for disruption. ENISA reports that 60% of surveyed companies across telecoms, core internet and trust services prioritize identified risks, define treatment plans and monitor progress.[2] It also says that consistent exercises of response and recovery arrangements remain an area of focus across digital infrastructure, particularly for high-impact scenarios.[2]

A security control reduces risk; it does not remove all of it. The relevant service or process owner needs to understand the residual risk, how it compares with the operator’s risk appetite, and what assurance supports the decision. This is not a paperwork exercise. It is how security, engineering and operations make an explicit choice while keeping the network in service.

That choice is rarely a simple contest between “secure” and “available.” A change can reduce the chance of compromise while increasing the chance of an outage during implementation. A shared identity can simplify support while making attribution and containment harder. The useful decision is which treatment is proportionate to the service risk, what residual exposure remains, and who has the authority and evidence to accept it.

**Composite scenario: patch window.** The supplied situation concerns a live-core platform with a known fixed version. Safe deployment still depends on a maintenance window, rollback plan and supplier confirmation; the next suitable window is three weeks away. The service-level residual risk is accepted, documented and reviewed. That interval is specific to the composite, not a universal operator patching benchmark. The decision weighs exposure while waiting against the service risk of an unsupported emergency change, and asks what interim controls are actually available.

Good risk acceptance is not a declaration that a system is safe. It records the service and exposure, the controls in place and the assurance behind them, who accepts the residual risk, and what event will reopen the decision. Here, a confirmed maintenance window, supplier support, or a material change in exploitation evidence could alter the balance. Review should follow the service and threat, not an arbitrary patch deadline.

A broad statement such as “low tolerance for cyber risk” does not settle a live-service trade-off. For the board, risk appetite has to translate into decision rights and service outcomes: which impacts trigger escalation, who can accept residual exposure within delegated authority, and what evidence reopens the decision. Directors do not need to approve every maintenance window. They do need confidence that management has named the owner and can explain the consequences of waiting or changing.

That is a more credible basis for board oversight than a single remediation target applied to every system. The board should understand which service is exposed, what the plausible consequences are, what can be done before the permanent fix, and when the decision will be reviewed. Service-specific outage limits and a path for systems that are no longer supported matter as much as the patch itself.

Operators are also investing in coverage, capacity, spectrum, cloud, fiber and customer experience. Security competes for the same people, time and budget. The CISO and CTO need to make the trade-off visible: which service is at risk, what could happen, what evidence is available, and what needs to be funded or changed. A list of controls alone rarely answers those questions.

Funding choices have operational consequences. If identity separation or response exercises receive capacity, other work may move. If they do not, the exposure remains. The CISO and CTO can show which work would be delayed and which service-level owner carries the residual risk. A decision to defer investment is a resource choice; it is not, by itself, acceptance of the risk by an accountable owner.

Technical severity is one input to prioritization, not the decision by itself. A weakness affecting a service with limited dependencies may call for a different treatment from the same weakness in a platform that supports several customer-facing services. The operator has to consider the threat, the exposure, the service impact, existing control effectiveness and the cost and risk of remediation. The result may be a change, a stronger interim control, a reduced use of the affected capability, or a documented acceptance of residual risk within appetite. Those choices should have an accountable service owner and a review point.

For an AI-enabled process that can affect a live service, the business case should include testing, monitoring and a safe way to pause or reverse actions. Otherwise, the apparent efficiency gain leaves out a material continuity cost.

## Recent telco cases require careful attribution

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos.[1] In one instance, the actor used a zero-day exploit to bypass a perimeter firewall; in another, it used rootkits to maintain access and evade detection.[1] The whole-of-government response, conducted in partnership with the telcos, lasted more than eleven months and involved over 100 cyber defenders across agencies.[1]

The actor reached parts of the telco networks, with limited access to critical systems in one case. The operation also involved exfiltration of a small amount of primarily network-related technical data.[1] Authorities reported no evidence at that point that sensitive or personal customer data had been accessed or exfiltrated, or that service had been disrupted.[1]

That distinction matters. Network information, customer data, service availability and operational control are separate risk dimensions. “No evidence of customer-data access or service disruption” does not erase the confirmed theft of technical data. A board update is more useful when it states what is known and what remains unknown.[1]

The disclosure illustrates the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government. It does not report AI use.[1] Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

A separate set of public claims from November 2026 needs the same care. On 10 November, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation.[6] Cisco’s advisory describes an unauthenticated remote file-read risk and lists fixed software releases.[7]

On 8 November, Malbear Labs published its account of an exposed operational workspace.[8] The researchers describe a largely autonomous, AI-enabled intrusion lasting more than two weeks against an unnamed European telecom provider and organizations it hosts. They report a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.[8]

Cisco’s 13 November advisory says Cisco has no direct evidence of active exploitation.[7] Malbear Labs links exploitation of the vulnerability to the intrusion it describes, but neither official notice confirms that connection.[6][7][8] The victim is unnamed, and public sources reviewed here do not independently confirm every reported outcome.[8] The vulnerability itself remains relevant to operators: a known, patchable weakness in a carrier platform can create an entry point.[6][7]

These distinctions matter. The researchers’ account may be important, but it should not be presented as an independently confirmed telecom incident or proof that AI was responsible for every reported action. The Singapore disclosure, meanwhile, offers a documented example of sustained response without an AI claim. Both cases support disciplined preparation, not inflated conclusions.

In Singapore, the response began when telcos notified IMDA and CSA, then continued through a joint effort to contain the breach and expand monitoring.[1] Notification paths and escalation relationships are easier to use when they are clear before an incident. They are difficult to improvise while technical teams are trying to preserve service and establish scope.

## Edge transformation is a security decision too

Moving workloads closer to users and network functions can make a strong business case: lower latency, better service performance and new operating models. Security questions can arrive later, once the platform choice and deployment plan are already in motion. That sequence can make a manageable design issue expensive to correct.

**Composite scenario: edge access.** In the supplied situation, the network team selected an edge platform before security review. The shared service account can reach edge nodes and parts of the core; remediation requires a maintenance window and supplier configuration change. The platform is not inherently unsafe. The sequence makes identity design a service-change decision, with options and rollback harder to resolve after selection.

A timely map would not have removed every constraint, but it could have made the options clearer before deployment: which identities needed access, which paths were essential, which should be separated, and how to roll back safely if the change affected service. This is a useful pattern across cloud and edge programs. The earlier identity and operational dependencies are understood, the less painful it is to narrow access or reverse a decision later.

The decision is not simply whether the edge platform is “secure.” It is which identities must cross which boundaries, how the access will be attributed, and what happens if the shared path needs to be suspended. Separation can add engineering and supplier work; leaving a broad identity in place leaves a wider path to manage. Those costs should be compared before rollout, when the architecture still offers choices. If the shared access remains, its owner, control effectiveness and review conditions should be explicit.

For each AI-enabled use, the operator needs to understand what the system can access and change, whether an unsafe action can be stopped, and how the service continues during containment. A summarization tool presents a different risk profile from an agent that can call tools, alter records or trigger a workflow. In service assurance, access to alarms and tickets is not the same as authority to change a network configuration.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. The change is delegated authority across connected systems.

The NOC composite at the opening makes the distinction concrete: read access and authority to act should not share a service identity simply because one assistant performs both tasks. A proposed network change remains within the normal change process.

In May 2026, CISA and the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), alongside other U.S. and international partners, published a joint guide to securing agentic AI.[3] It identifies four risks: a larger attack surface, privilege creep, behavior that departs from intended goals, and event records that are hard to interpret.[3] The guide recommends starting with low-risk, non-sensitive use cases, avoiding broad access to sensitive data or critical systems, and accounting for agentic AI in the organization’s security model and risk posture.[3] It addresses cross-sector critical-infrastructure risks, not a telco-specific standard.[3]

Those concerns apply where a provider’s customer services meet network and operational processes. An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. For high-impact uses, assurance should establish whether permissions match the task, logs capture tool calls, and access can be revoked without interrupting service.

**Composite scenario: supplier diagnostic feature.** A supplier enables an AI diagnostic feature through a routine update to a network-management product. The feature is absent from the operator’s AI project register; it can read topology and propose actions. It enters through an existing product update, not a separately registered AI project.

This does not make “stop every update” the answer. The operator needs advance notice of material capability changes and a way to decide whether product release and feature activation can be separated. If they can, verify the feature’s identity and reach before activation. If they cannot, compare the service cost of delaying the release with the residual risk of enabling an unverified action path. Ownership of the product and ownership of the affected service may sit in different teams; both need to be represented before a decision is made.

## Two risk questions, not one

AI changes risk along two tracks, and each needs different evidence. The first is internal authority: what an AI-enabled system can read, change or trigger through the identities and tools it has been given. That risk exists even if no attacker uses AI. The second is response speed: whether a threat can move from access to impact faster than the operator can detect it, agree a proportionate response and act without causing unacceptable service disruption.

An inventory can help expose delegated authority, but it does not prove that response is fast enough. A threat-intelligence report may describe compressed attack stages, but it does not show whether a particular operator can safely contain them. These questions meet when an external actor reaches an identity or workflow that already has broad authority. The security program needs visibility into both the path that can be abused and the service’s ability to interrupt it.

That distinction matters when investments compete. Better detection may help teams correlate activity, but it does not narrow an agent’s identity or tool permissions. Restricting authority may reduce exposure, but it does not make containment fast or preserve the service by itself. Continuity work can reduce the cost of containment without preventing misuse. A proposal should say which path it changes, which service outcome should improve, what other capability remains unfunded, and what evidence will show the difference. An efficiency benefit also needs measurement in the actual operating workflow; it should not be assumed from a product demonstration.

Chapters 2 and 3 treat those questions separately.

## Response speed is part of the risk

The Canadian Centre for Cyber Security’s 26 October 2026 bulletin on agentic AI reports that, in some cases, activity moved from target selection to privileged access to cloud systems in less than three hours.[14] It cautions that cyber attacks are not yet fully autonomous: humans still choose targets, set objectives and oversee operations.[14] The bulletin is cross-sector; it does not connect its findings to either telecom case described above.[14][1][8]

The operator’s concern is not a universal response clock. It is the time available to make a safe decision while limiting service impact. Teams still need to preserve service, test changes across complex estates, coordinate with suppliers and meet local obligations. Legacy systems can slow remediation, and response exercises need to test how teams work together.[2] No operator can close every gap at once.

When an external threat or internal agent can change a critical workflow faster than normal approvals, the executive discussion needs to cover how quickly the operator can detect and contain it, and what service could be affected by containment. Who can stop the change? Can the team do so without losing the visibility needed to manage the network? Security, Network, IT, Operations, Procurement, Legal and business leaders may each hold part of the answer.

## Regulation does not replace operational ownership

Service providers face cybersecurity and privacy laws, communications-sector rules, resilience expectations, reporting duties, supplier contracts and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law.[4] Duties vary by service and country, so a multinational operator cannot assume that one compliance answer fits every market.

Compliance does not decide which agent may change a network configuration, what evidence is needed before its authority expands, or who accepts the residual risk when a supplier’s AI feature reaches a critical workflow. The executive accountable for the affected service should own that decision, with input from the workflow owner and CISO. The rationale, safeguards and review conditions should be recorded against the operator’s stated risk appetite.

Existing security, architecture, change and supplier-risk reviews are usually the simplest place to start. Those reviews can account for each machine identity, the data it can reach, the actions it can take and how those actions can be reversed. Operators do not need perfect certainty before they begin. They can identify the owner and service impact of each consequential use, then define what evidence is needed before its authority expands.

## Set boundaries before expanding use

Operators have good reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

A bounded task with limited service impact can be a sensible place to start. The relevant question is not whether a use is “AI for the business” or “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

“Low risk” depends on the operator and service. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator’s existing risk governance can set the boundary, monitor the use and require stronger assurance as authority grows.

## Three shifts for the next twelve months

The next-year discussion does not need to settle every technical question. It can focus on three shifts within the operator’s existing plans.

**Treat AI as part of the attack surface and operating model.** For consequential uses, know the identity, data, tools, supplier, owner and actions involved. If the operator does not know where a capability is used, it cannot make a grounded decision about how much authority it should have.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans should reflect the service and its dependencies, not only the system under investigation.

**Keep accountability in step with autonomy.** Identify who approves the use, who owns its risk, what limits apply and how an unsafe action can be detected and reversed. Supplier assurance supports the operator’s decision; it does not replace operator ownership.

These shifts can help a CISO or CTO select three or four priorities for the next twelve months and explain them to the CEO and board. The first is to understand where delegated authority can enter and how far it can reach. Chapter 2 maps those systems, suppliers, data and workflows.
