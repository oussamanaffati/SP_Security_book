# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

A cyber incident at a service provider can become a service incident quickly. When a mobile network, core platform or management system is affected, customers may lose connectivity, businesses may lose services they depend on, and public services may lose an important channel. The operator has to restore service while it is still establishing what happened and how far the impact reaches.

That responsibility is familiar. What has changed is how many systems can act, how quickly activity can move between them, and whether decision authority still matches ownership of the service.

Operators are moving workloads toward the edge, onto telco cloud and into public cloud.[5] Each move changes where data resides, which systems connect, and who is responsible for securing them. AI features are also appearing in customer care, service assurance, fraud management and internal operations. A tool that summarizes an alarm is different from an agent that can query inventory, open a supplier case or trigger a workflow. The key question is what it can reach and do, and what happens to the service if it gets that wrong.

AI changes who can act inside the operator, not just how teams detect threats.[3] That shift deserves attention from the CISO and CTO because it touches the operating model: identities, suppliers, change processes, service continuity and the people accountable for residual risk.

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. The degree of dependence varies by country and service, but an outage can affect organizations the operator does not control. This is one reason a service provider’s security decisions cannot be separated from its continuity obligations.

ENISA’s 2026 NIS360 assessment places telecommunications among the EU’s most mature and critical sectors. It defines criticality through digitalization, socioeconomic impact and how quickly consequences can spread across sector interconnections.[2] The report also identifies legacy systems and budget constraints as barriers to timely remediation, particularly in telecommunications.[2]

Those findings should not be read as a claim that every operator has the same risk profile. They describe a familiar tension: a control may be well understood, while the safe path to implement it depends on a long-lived platform, a supplier, a change window and the service owner’s tolerance for disruption. ENISA reports that 60% of surveyed companies across telecoms, core internet and trust services prioritize identified risks, define treatment plans and monitor progress.[2] It also says that consistent exercises of response and recovery arrangements remain an area of focus across digital infrastructure, particularly for high-impact scenarios.[2]

A security control reduces risk; it does not remove all of it. The relevant service or process owner needs to understand the residual risk, how it compares with the operator’s risk appetite, and what assurance supports the decision. This is not a paperwork exercise. It is how security, engineering and operations make an explicit choice while keeping the network in service.

Consider patching a live core platform. “Patch it now” may be the right security instinct, but it is not always an operational plan. Security may have the advisory and the fixed version. The network team still needs a maintenance window, a rollback plan and supplier confirmation that the change is supported. In one case, the next suitable window was three weeks away. The residual risk was accepted at the service level, documented and reviewed. The useful conversation was not a generic demand to patch faster. It was about the exposure during that interval, the compensating measures, the service impact of an emergency change, and who owned the decision to wait.

That is a more credible basis for board oversight than a single remediation target applied to every system. The board should understand which service is exposed, what the plausible consequences are, what can be done before the permanent fix, and when the decision will be reviewed. Service-specific outage limits and a path for systems that are no longer supported matter as much as the patch itself.

Operators are also investing in coverage, capacity, spectrum, cloud, fiber and customer experience. Security competes for the same people, time and budget. The CISO and CTO need to make the trade-off visible: which service is at risk, what could happen, what evidence is available, and what needs to be funded or changed. A list of controls alone rarely answers those questions.

For an AI-enabled process that can affect a live service, the business case should include testing, monitoring and a safe way to pause or reverse actions. Otherwise, the apparent efficiency gain leaves out a material continuity cost.

## Recent telco cases require careful attribution

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos.[1] In one instance, the actor used a zero-day exploit to bypass a perimeter firewall; in another, it used rootkits to maintain access and evade detection.[1] The whole-of-government response, conducted in partnership with the telcos, lasted more than eleven months and involved over 100 cyber defenders across agencies.[1]

The actor reached parts of the telco networks, with limited access to critical systems in one case. The operation also involved exfiltration of a small amount of primarily network-related technical data.[1] Authorities reported no evidence at that point that sensitive or personal customer data had been accessed or exfiltrated, or that service had been disrupted.[1]

The disclosure illustrates the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government. It does not report AI use.[1] Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

A separate set of public claims from November 2026 needs the same care. On 10 November, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation.[6] Cisco’s advisory describes an unauthenticated remote file-read risk and lists fixed software releases.[7]

On 8 November, Malbear Labs published its account of an exposed operational workspace.[8] The researchers describe a largely autonomous, AI-enabled intrusion lasting more than two weeks against an unnamed European telecom provider and organizations it hosts. They report a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.[8]

Cisco’s 13 November advisory says Cisco has no direct evidence of active exploitation.[7] Malbear Labs links exploitation of the vulnerability to the intrusion it describes, but neither official notice confirms that connection.[6][7][8] The victim is unnamed, and public sources reviewed here do not independently confirm every reported outcome.[8] The vulnerability itself remains relevant to operators: a known, patchable weakness in a carrier platform can create an entry point.[6][7]

These distinctions matter. The researchers’ account may be important, but it should not be presented as an independently confirmed telecom incident or proof that AI was responsible for every reported action. The Singapore disclosure, meanwhile, offers a documented example of sustained response without an AI claim. Both cases support disciplined preparation, not inflated conclusions.

In Singapore, the response began when telcos notified IMDA and CSA, then continued through a joint effort to contain the breach and expand monitoring.[1] Notification paths and escalation relationships are easier to use when they are clear before an incident. They are difficult to improvise while technical teams are trying to preserve service and establish scope.

## Edge transformation is a security decision too

Moving workloads closer to users and network functions can make a strong business case: lower latency, better service performance and new operating models. Security questions can arrive later, once the platform choice and deployment plan are already in motion. That sequence can make a manageable design issue expensive to correct.

In one engagement, the network team had already chosen an edge platform when a review found a shared service account that could reach both edge nodes and parts of the core. Fixing the access path required a maintenance window and a supplier configuration change. The issue was not that the edge platform was inherently unsafe. It was that identity and tool access had not been mapped early enough to shape the design.

A timely map would not have removed every constraint, but it could have made the options clearer before deployment: which identities needed access, which paths were essential, which should be separated, and how to roll back safely if the change affected service. This is a useful pattern across cloud and edge programs. The earlier identity and operational dependencies are understood, the less painful it is to narrow access or reverse a decision later.

For each AI-enabled use, the operator needs to understand what the system can access and change, whether an unsafe action can be stopped, and how the service continues during containment. A summarization tool presents a different risk profile from an agent that can call tools, alter records or trigger a workflow. In service assurance, access to alarms and tickets is not the same as authority to change a network configuration.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. The change is delegated authority across connected systems.

We tested an assistant that read alarms and drafted ticket updates. It worked well for summarization. The risk changed when it was connected to a broader service account that could also open vendor cases. In a simulated incident, it pulled data from a neighboring domain and proposed a change that would have reduced NOC visibility. The scenario was a test, not a production incident. It made one point concrete: read access and authority to act should not share an identity simply because one assistant performs both tasks. Nor should the normal change process be bypassed because a request comes from an AI tool.

In May 2026, CISA and the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), alongside other U.S. and international partners, published a joint guide to securing agentic AI.[3] It identifies four risks: a larger attack surface, privilege creep, behavior that departs from intended goals, and event records that are hard to interpret.[3] The guide recommends starting with low-risk, non-sensitive use cases, avoiding broad access to sensitive data or critical systems, and accounting for agentic AI in the organization’s security model and risk posture.[3] It addresses cross-sector critical-infrastructure risks, not a telco-specific standard.[3]

Those concerns apply where a provider’s customer services meet network and operational processes. An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. For high-impact uses, assurance should establish whether permissions match the task, logs capture tool calls, and access can be revoked without interrupting service.

A supplier feature or software update can introduce an AI capability outside a project labeled “AI.” An operator may not know that a network-management product can now read topology or propose actions. The important questions are practical: who owns the feature, which identity does it use, what data can it reach, and do proposed actions stay inside the existing change process? Visibility after the fact is better than none, but it is slower and more expensive than understanding the capability before it is enabled.

## Response speed is part of the risk

The Canadian Centre for Cyber Security’s 26 October 2026 bulletin on agentic AI reports that, in some cases, activity moved from target selection to privileged access to cloud systems in less than three hours.[14] It cautions that cyber attacks are not yet fully autonomous: humans still choose targets, set objectives and oversee operations.[14] The bulletin is cross-sector; it does not connect its findings to either telecom case described above.[14][1][8]

The operator’s concern is not a universal response clock. It is the time available to make a safe decision while limiting service impact. Teams still need to preserve service, test changes across complex estates, coordinate with suppliers and meet local obligations. Legacy systems can slow remediation, and response exercises need to test how teams work together.[2] No operator can close every gap at once.

If an external threat or internal agent can change a critical workflow faster than normal approvals, the CISO and CTO should be able to explain how quickly the operator can detect and contain it, and what service might be affected by containment. Who can stop the change? Can the team do so without losing the visibility needed to manage the network? Security, Network, IT, Operations, Procurement, Legal and business leaders may all hold part of the answer.

## Regulation does not replace operational ownership

Service providers face cybersecurity and privacy laws, communications-sector rules, resilience expectations, reporting duties, supplier contracts and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law.[4] Duties vary by service and country, so a multinational operator cannot assume that one compliance answer fits every market.

Compliance does not decide which agent may change a network configuration, what evidence is needed before its authority expands, or who accepts the residual risk when a supplier’s AI feature reaches a critical workflow. The executive accountable for the affected service should own that decision, with input from the workflow owner and CISO. The rationale, safeguards and review conditions should be recorded against the operator’s stated risk appetite.

A practical way forward is to extend existing security, architecture, change and supplier-risk reviews. Include each machine identity, the data it can reach, the actions it can take, and how those actions can be reversed. Operators do not need perfect certainty before they begin. They can identify the owner and service impact of each consequential use, then define what evidence is needed before its authority expands.

## Set boundaries before expanding use

Operators have good reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

A bounded task with limited service impact can be a sensible place to start. The relevant question is not whether a use is “AI for the business” or “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

“Low risk” depends on the operator and service. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator’s existing risk governance can set the boundary, monitor the use and require stronger assurance as authority grows.

## What must change in the next twelve months

A CISO or CTO does not need to settle every technical question at once. The useful starting point is to make three shifts visible in the operator’s existing plans.

**Treat AI as part of the attack surface and operating model.** For consequential uses, know the identity, data, tools, supplier, owner and actions involved. If the operator does not know where a capability is used, it cannot make a grounded decision about how much authority it should have.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans should reflect the service and its dependencies, not only the system under investigation.

**Keep accountability in step with autonomy.** Identify who approves the use, who owns its risk, what limits apply and how an unsafe action can be detected and reversed. Supplier assurance supports the operator’s decision; it does not replace operator ownership.

These shifts can help a CISO or CTO select three or four priorities for the next twelve months and explain them to the CEO and board. The first is to understand where delegated authority can enter and how far it can reach. Chapter 2 maps those systems, suppliers, data and workflows.
