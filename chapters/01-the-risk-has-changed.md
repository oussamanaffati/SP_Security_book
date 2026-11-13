# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

For a service provider, a cyber incident can quickly become more than an IT problem. If a mobile network or core service fails, customers lose connectivity, businesses lose services they depend on, and public services may lose an important channel. The operator has to restore service while it is still working out what happened.

Service providers are moving more workloads toward the edge, on telco cloud or public cloud.[5]
Each move changes where data lives, which systems connect, and who is responsible for securing them.

For each AI-enabled use, the operator needs to know what the system can access and change, and whether an unsafe action can be stopped and reversed.

Operators are evaluating AI for customer care, service assurance, fraud management and internal operations. A summarization tool presents a different risk profile from an agent that can call other tools, change records or trigger a workflow. In service assurance, for example, access to alarms and tickets is not the same as authority to change a network configuration. Those actions can affect service continuity.

AI changes who can act inside the operator, not just how teams detect threats.[3]

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. Dependence varies by country, but disruption can reach organizations the operator does not control.

ENISA’s 2026 NIS360 assessment places telecommunications among the EU’s most mature and critical sectors and defines criticality by digitalization, socioeconomic impact and how quickly consequences are felt across sector interconnections.[2]

For digital infrastructure, ENISA identifies legacy and budget constraints as barriers to timely remediation, especially in telecommunications.[2]
ENISA reports that 60% of surveyed companies across telecoms, core internet and trust services prioritize identified risks, define treatment plans and monitor progress.[2]
The report also says consistent exercises of response and recovery arrangements remain an area of focus across digital infrastructure, particularly for high-impact scenarios.[2]

Operators already have security programs, but controls do not remove all risk. The accountable service or process owner should understand and accept the residual risk. Security work must continue while the network stays in service.

In practice, “patch it now” can be the right security answer and still not be an operational plan. A network change may need a maintenance window, rollback, vendor coordination and agreement across engineering, operations and security. Some systems have been in service for years; replacing them is a long-term program, not a quick fix.

The board needs to decide how much planned unavailability is acceptable to reduce exposure and what rollback or alternative service is required. Operators need service-specific outage limits and a clear path for systems that no longer have vendor support.

Then there is the business. Operators are investing in coverage, capacity, spectrum, cloud, fiber and customer experience. Security competes for the same people, time and budget. The CISO or CTO needs to make the decision clear: which service is at risk, what could happen, and what needs to be funded or changed. A list of controls alone will not answer those questions.

For an AI-enabled process that can affect a live service, budget for testing, monitoring and safe rollback. Otherwise, the business case understates continuity risk.

## Recent telco cases require careful attribution

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos.[1]
In one instance, the actor used a zero-day exploit to bypass a perimeter firewall; in another, it used rootkits to maintain access and evade detection.[1]
The whole-of-government response, conducted in partnership with the telcos, spanned more than eleven months and involved over 100 cyber defenders across agencies.[1]
The actor reached parts of the telco networks, with limited access to critical systems in one case.[1]
The operation also involved exfiltration of a small amount of primarily network-related technical data.[1]
Authorities reported no evidence at that point that sensitive or personal customer data had been accessed or exfiltrated, or that service had been disrupted.[1]

The disclosure shows the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government.[1]
The disclosure does not report AI use.[1]
Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

On 10 November 2026, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.[6]
Cisco’s advisory describes an unauthenticated remote file-read risk and lists fixed software releases.[7]

On 8 November 2026, Malbear Labs published its account of an exposed operational workspace.[8]
The researchers describe a largely autonomous, AI-enabled intrusion lasting more than two weeks against an unnamed European telecom provider and organizations it hosts.[8]
They report a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.[8]

Cisco’s 13 November advisory says Cisco has no direct evidence of active exploitation.[7]
Malbear Labs links that exploitation to the intrusion it describes, but neither official notice confirms the connection.[6][7][8]
The victim is unnamed, and public sources reviewed here do not independently confirm every reported outcome.[8]
The confirmed vulnerability still matters to operators: a known, patchable weakness in a carrier platform can create an entry point.[6][7]
Malbear Labs says an operator directed the reported activity while an agent carried out much of it.[8]

The Singapore response began when telcos notified IMDA and CSA, then continued through a joint response to contain the breach and expand monitoring.[1]
Those notification links and escalation paths need to be clear before an incident. They cannot be improvised once the response is under way.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. That is the change. Software is exercising delegated authority across connected systems.

Consider a service-assurance assistant. It may begin by summarizing a ticket, then gain access to network-management data, open a vendor case or trigger a configuration workflow. An error in a summary is inconvenient. An incorrect production change could disrupt service or require rollback. This is an illustrative scenario, not a reported incident. Read access and authority to change the network need different controls.

In May 2026, CISA and the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), alongside other U.S. and international partners, published a joint guide to securing agentic AI.[3]
It identifies four risks: a larger attack surface, privilege creep, behavior that departs from intended goals, and event records that are hard to interpret.[3]

The guide recommends starting with low-risk, non-sensitive use cases, avoiding broad access to sensitive data or critical systems, and accounting for agentic AI in the organization’s security model and risk posture.[3]
It addresses cross-sector critical-infrastructure risks, not a telco-specific standard.[3]
The same concerns matter where a provider’s customer services meet network and operational processes.

An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. For high-impact uses, assurance should test that permissions match the task, logs capture tool calls, and revocation works without interrupting service.

A supplier feature or software update can introduce an AI capability outside a project labeled “AI.” The operator’s risk inventory may not reflect its access to data or workflows. Responsibility may span the team enabling the feature and the team that owns the data or process it touches.

## Response speed is part of the risk

The Canadian Centre for Cyber Security’s 26 October 2026 bulletin on agentic AI reports that, in some cases, activity moved from target selection to privileged access to cloud systems in less than three hours.[14]
It cautions that cyber attacks are not yet fully autonomous: humans still choose targets, set objectives and oversee operations.[14]
The bulletin is cross-sector; it does not connect its findings to either telecom case described above.[14][1][8]

The issue for operators is the time they have to make a safe decision while limiting service impact. They still need to preserve service, test changes across complex estates, coordinate teams and meet local obligations.

The constraints are practical as well as technical: legacy systems can slow remediation, and response exercises need to test how teams work together.[2]
No operator can close every gap at once.

If an external threat or internal agent can change a critical workflow faster than normal approvals, the board should ask how quickly the operator can detect and contain it. Can the team do so without extending service impact? Who can stop the change? Security, Network, IT, Operations, Procurement, Legal and business leaders need to decide this together.

## Regulation does not replace operational ownership

Service providers face cybersecurity and privacy laws, communications-sector rules, resilience expectations, reporting duties, supplier contracts and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law.[4]
Duties vary by service and country, so a multinational operator cannot assume that one compliance answer fits every market.

Compliance alone does not decide which agent may change a network configuration, what evidence is needed before its authority expands, or who accepts the residual risk when a supplier’s AI feature reaches a critical workflow. The executive accountable for the affected service should accept that risk against the operator’s stated appetite, with input from the workflow owner and CISO, and record the decision and rationale.

An early step is to extend existing security, architecture, change and supplier-risk reviews. Include each machine identity, the data it can reach, the actions it can take, and how to reverse them. Operators cannot wait for certainty. They can still identify each use’s owner and impact, and define evidence required before its authority expands.

## Set boundaries before expanding use

Operators have real reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

A sensible first use is a bounded task with limited service impact. Map the data, identities and tools it touches. Define approval points, monitor actions and test that access can be revoked before expanding its authority.

“Low risk” depends on the operator. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator must set the boundary.

The boundary is not simply “AI for the business” versus “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

## What must change in the next twelve months

A CISO or CTO does not need to settle every technical question this quarter. Three shifts can start now.

**Treat AI as part of the attack surface and operating model.** Track the identity, data, tools, supplier, owner and actions around each consequential use. If you do not know where it is used, you cannot decide where its authority should grow.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans must reflect the service, not just the system under investigation.

**Keep accountability in step with autonomy.** Name who approves each use, who owns the risk, what limits apply and how an unsafe action can be detected and reversed. Vendor assurance does not replace operator ownership.

A CISO or CTO can use these questions to choose three or four priorities for the next twelve months and explain them to the CEO and board. The first is to understand where delegated authority can enter and how far it can reach. Chapter 2 maps those systems, suppliers, data and workflows.
