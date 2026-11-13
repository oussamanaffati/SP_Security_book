# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

For a service provider, a cyber incident is never only an IT problem. If a mobile network or core service fails, customers lose connectivity, businesses lose services they depend on, and public services may lose an important channel. The operator must restore service while it is still working out what happened.

Service providers are moving more workloads closer to users, often called edge computing.[5] New services need lower latency, and operators are looking for new revenue. Each move changes where data lives, which systems connect, and who is responsible for securing them.

AI raises a different security question. Which systems can act, what authority do they have, and what happens if they make a mistake? Detection speed still matters. So does the ability to limit and reverse an action.

Operators are evaluating AI for customer care, service assurance, fraud management and internal operations. A tool that summarizes information has a different risk from one that can call other tools, change records or trigger a workflow. In service assurance, for example, access to alarms and tickets is not the same as authority to change a network configuration. Those actions can affect service continuity.

AI is not just another detection tool. It changes risk inside the operator and may give adversaries new ways to increase the pace and scale of activity. Treating AI only as a better detector improves one part of security while missing the wider change.

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. Dependence varies by country, but disruption can reach organizations the operator does not control.

ENISA’s 2026 NIS360 assessment places telecom among the EU’s most mature and critical sectors. Criticality reflects the impact of disruption, dependencies between sectors and how quickly consequences are felt. ENISA also notes legacy-related delays in vulnerability remediation, uneven follow-through on identified risks and the need for regular response and recovery exercises.[2]

Operators already have security programs, but controls do not remove all risk. The remaining risk must be understood and accepted by the right owner. Security work must continue while the network stays in service.

In practice, “patch it now” can be the right security answer and still not be an operational plan. A network change may need a maintenance window, a rollback path, vendor coordination and agreement across engineering, operations and security. Some systems have been in service for years. Replacing them is a program, not a Tuesday afternoon task.

Then there is the business. Operators are investing in coverage, capacity, spectrum, cloud, fiber and customer experience. Security competes for the same people, time and budget. A CISO or CTO needs to explain why a security decision matters in terms the business can act on, not just present another list of controls.

An AI use case must be judged by its access and impact. An assistant that summarizes a public document is different from an agent that reads network data, opens a vendor case and triggers a production workflow. Ask what it can see and change, how effective the safeguards are, and whether the action can be reversed without harming service.

## A warning from the network floor

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos. The actor used a zero-day to bypass a perimeter firewall and rootkits to evade detection. The coordinated response lasted more than eleven months and involved over 100 defenders. The actor reached parts of the telco networks, including some critical systems, but authorities reported no evidence at that point of customer-data theft or service disruption.[1]

The disclosure shows the demands operators already face: persistent adversaries, complex networks, stealthy access and response involving both companies and government. It did not say AI was involved. Calling every sophisticated attack “AI-powered” would overstate the evidence. The confirmed activity is serious on its own.

On 10 November 2026, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation.[6] Cisco says the flaw could let an unauthenticated attacker read sensitive files and that fixed software was available from August 2026.[7]

Two days earlier, Malbear Labs published an account of an exposed operational workspace that it says documented a largely autonomous AI-enabled intrusion lasting more than two weeks. The researchers say the target was an unnamed European telecom provider and organizations hosted on its infrastructure. They describe a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.[8]

The evidence has different levels of confidence. CISA and Cisco confirm active exploitation of the BroadWorks flaw. Malbear Labs makes the link between that exploitation and the AI-enabled campaign; the official notices do not confirm it. The victim is unnamed, and the public sources reviewed here do not independently confirm every reported outcome. The operational lesson is still important: a known, patchable weakness in a carrier platform can create an entry point. Malbear Labs says an operator directed the reported activity while an agent carried out much of it. That account deserves attention, but it should not be presented as independently confirmed fact.

Resilience is not a product you install. The Singapore response depended on operators notifying authorities, then coordinating containment, investigation and monitoring. That takes relationships, clear escalation paths and decisions made before all the facts are known. Those capabilities cannot be bought once an incident is under way.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. That is the change. Software is exercising delegated authority across connected systems.

Consider a service-assurance assistant. It may begin by summarizing a ticket, then gain access to network-management data, open a vendor case or trigger a configuration workflow. An error in a summary is inconvenient. An incorrect production change could disrupt service or require rollback. This is an illustrative scenario, not a reported incident. Read access and authority to change the network need different controls.

Joint guidance published in May 2026 by Australia’s cyber security center and partner agencies, including CISA, NSA and the UK NCSC, warns about privilege, identity, structural and accountability risks in agentic AI. The agencies recommend using existing security frameworks, beginning with low-risk tasks, avoiding broad access to critical systems, and keeping oversight and visibility.[3] This guidance is not telecom-specific. Its message matters even more where a company operates customer services alongside network and operational processes.

An agent may act faster than the review process around it. It may inherit a service account’s permissions or use a supplier tool whose risk has changed. Without reliable logs, its actions may look routine. Operators need to know which identity acted, what authority it used, and whether controls actually limited the action. These governance questions have direct operational consequences.

AI can also arrive through a supplier feature or a software update, not just through a project called “AI.” One team enables a capability. Another team owns the data it can reach. A vendor changes what happens behind an interface. Meanwhile, the asset and risk inventory may still show the old product name. That is the ground-level problem: authority and dependencies can change faster than the documentation.

## Response speed is part of the risk

The reported operation suggests an agent may reduce the effort needed to sustain some hostile activity.[8] It does not show that every attacker uses autonomous campaigns or that AI explains every increase in cyber risk. The strategic concern is the speed gap. Adversaries can experiment quickly; operators must test changes across complex estates, preserve service, coordinate teams and meet local obligations.

The constraints are practical as well as technical: legacy systems can slow remediation, and response exercises need to test how teams work together. No operator can close every gap at once. AI may put more pressure on those limits.[2]

The board-level question is whether hostile activity, combined with autonomous capabilities inside the operator, could outpace its ability to approve, monitor and contain change. Can Security, Network, IT, Operations, Procurement, Legal and business leaders make decisions together before a critical workflow is affected?

## Regulation does not assign operational ownership

Service providers already manage cybersecurity and privacy laws, communications-sector rules, resilience expectations, incident reporting, contractual duties and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law.[4] The details vary by service and country. A multinational operator cannot assume that one compliance answer fits every market.

Compliance alone does not decide which agent may change a network configuration, what evidence is needed before its authority expands, or who accepts the residual risk when a supplier’s AI feature reaches a critical workflow. These decisions need a named owner and a record of the rationale.

Avoid two extremes: a separate AI process that duplicates governance but misses high-impact deployments, and the assumption that existing policies cover every new capability. Extend security, architecture, change-management and supplier-risk processes to cover machine identities, delegated authority, data access, autonomy and reversibility. Operators cannot wait for certainty. They can still identify each use’s owner and impact, and define evidence required before its authority expands.

## Set boundaries before expanding use

Operators have real reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

Use bounded tasks first. Identify the data, identities and tools involved. Set approval points, monitor actions, and make access reversible. The 2026 multi-agency guidance recommends cautious adoption, especially for sensitive data and critical systems.[3]

“Low risk” depends on the operator. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator must set the boundary.

Do not divide the world into “AI for the business” and “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

## What must change in the next twelve months

A CISO or CTO does not need to settle every technical question this quarter. Three shifts can start now.

**Treat AI as part of the attack surface and operating model.** Track the identity, data, tools, supplier, owner and actions around each consequential use. If you do not know where it is used, you cannot decide where its authority should grow.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans must reflect the service, not just the system under investigation.

**Keep accountability in step with autonomy.** Name who approves each use, who owns the risk, what limits apply and how an unsafe action can be detected and reversed. Vendor assurance does not replace operator ownership.

The aim is to help readers choose three or four priorities for the next twelve months and explain them credibly to the CEO and board. The first step is to understand where delegated authority can enter and how far it can reach. This chapter has explained why the risk is changing. Chapter 2 maps where that change lands: the operator’s systems, suppliers, data and workflows.
