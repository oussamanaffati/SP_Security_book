# Chapter 1: The Risk Has Changed. Service Providers Feel It First.

Let’s begin with the operator’s reality. A cyber incident is never just an IT problem. If a mobile network or a core service fails, the impact moves quickly beyond the operator. Customers lose connectivity. Businesses lose services they rely on. Public services may lose a channel they need. And the operator has to restore service while it is still finding out what happened.

When talking to service provider clients, a recurring theme we hear is the push to move workloads closer to the edge.[5] New services need lower latency. Operators are looking for new revenue. That is the business reality. But every move toward the edge changes where data lives, which systems connect, and who has to secure them.

AI adds another question. Not just “Can we detect this faster?” Ask instead: **what new actors can take action in our environment, with whose authority, and what happens if they get it wrong?**

This is not a prediction about a fully autonomous network tomorrow. It is about decisions operators are making now as AI moves into customer care, service assurance, fraud management and internal operations. Some will summarize. Others will call tools, change records or trigger workflows. That difference matters when the product is continuity.

That is the argument of this book: **AI is not just another detection tool. It changes the shape of risk inside the operator, while giving adversaries new ways to increase the pace and scale of their activity.** If we treat AI only as a better detector, we improve one part of security and miss the wider change.

## An operator is part of the country’s operating system

Networks carry emergency calls, support payments, connect hospitals and keep businesses running. Dependence varies by country, but disruption can reach organizations the operator does not control.

ENISA’s 2026 NIS360 assessment places telecom among the EU’s most mature and critical sectors. Criticality reflects the impact of disruption, dependencies between sectors and how quickly consequences are felt. ENISA also notes legacy-related delays in vulnerability remediation, uneven follow-through on identified risks and the need for regular response and recovery exercises.[2]

The sector is not starting from zero. But a strong baseline does not mean every risk is closed. The work has to continue while the network stays up.

In practice, “patch it now” can be the right security answer and still not be an operational plan. A network change may need a maintenance window, a rollback path, vendor coordination and agreement across engineering, operations and security. Some systems have been in service for years. Replacing them is a program, not a Tuesday afternoon task.

Then there is the business. Operators are investing in coverage, capacity, spectrum, cloud, fiber and customer experience. Security competes for the same people, time and budget. A CISO or CTO needs to explain why a security decision matters in terms the business can act on, not just present another list of controls.

This is why an AI use case cannot be judged in the abstract. An assistant that summarizes a public document is one thing. An agent that reads network data, opens a vendor case and can trigger a production workflow is another. The questions are simple: what can it see, what can it change, and can we reverse the change without affecting service?

## A warning from the network floor

In February 2026, Singapore’s CSA and IMDA disclosed a campaign against all four major telcos. The actor used a zero-day to bypass a perimeter firewall and rootkits to evade detection. The coordinated response lasted more than eleven months and involved over 100 defenders. The actor reached parts of the telco networks, including some critical systems, but authorities reported no evidence at that point of customer-data theft or service disruption.[1]

This is the environment operators already face: persistent adversaries, complex networks, stealthy access and response that crosses the line between company and state. The Singapore disclosure did not say AI was involved. We should not label every sophisticated attack “AI-powered.” The reality is serious enough without that.

Now consider a more recent case. On 10 November, CISA added a Cisco BroadWorks vulnerability (CVE-2026-20320) to its Known Exploited Vulnerabilities catalog, citing evidence of active exploitation.[6] Cisco says the flaw could let an unauthenticated attacker read sensitive files and that fixed software was available from August.[7]

Two days earlier, Malbear Labs published an account of an exposed operational workspace that it says documented a largely autonomous AI-enabled intrusion lasting more than two weeks. The researchers say the target was an unnamed European telecom provider and organizations hosted on its infrastructure. They describe a custom harness using a jailbroken DeepSeek model and say the agent exploited the BroadWorks flaw, adapted when tools were blocked, and continued with limited operator check-ins.[8]

We need to separate what is confirmed from what is reported. CISA and Cisco confirm active exploitation of the BroadWorks flaw. The link between that exploitation and the AI-enabled campaign is Malbear Labs’ analysis; the official notices do not confirm that link. The victim is unnamed, and I found no public independent confirmation of every outcome in the report. Treat those details accordingly. The operator lesson is still clear: an existing, patchable weakness in a carrier platform can become the entry point for an operation that researchers say was directed by a person but carried out largely by an agent. That is a new level of urgency, not a reason to overstate the evidence.

Resilience is not a product you install. The Singapore response depended on operators notifying authorities, then coordinating containment, investigation and monitoring. That takes relationships, clear escalation paths and decisions made before all the facts are known. Those capabilities cannot be bought once an incident is under way.

## AI changes who can act

AI systems still depend on software, infrastructure, data and suppliers. An agent can go further: interpret a goal, retrieve information, call tools, hand off work and take action without a person approving every step. That is the change. Software is exercising delegated authority across connected systems.

Consider a service-assurance assistant. It starts by summarizing a ticket. Then it gets access to network-management data, can open a vendor case, and can recommend or trigger a configuration workflow. A mistake in a summary is inconvenient. A mistake in a production workflow may affect service. This is an illustrative scenario, not a reported incident. It shows why access to information and authority to change the network must be treated differently.

Joint guidance published in May 2026 by Australia’s cyber security center and partner agencies, including CISA, NSA and the UK NCSC, warns about privilege, identity, structural and accountability risks in agentic AI. The agencies recommend using existing security frameworks, beginning with low-risk tasks, avoiding broad access to critical systems, and keeping oversight and visibility.[3] This guidance is not telecom-specific. Its message matters even more where a company operates customer services alongside network and operational processes.

In practice, an agent can act faster than the review process around it. It may inherit permissions intended for a service account. It may use a supplier tool or data source whose risk changes. It may generate activity that looks routine unless the operator can see which identity acted and what it was allowed to do. These are governance questions, but they have operational consequences.

AI can also arrive through a supplier feature or a software update, not just through a project called “AI.” One team enables a capability. Another team owns the data it can reach. A vendor changes what happens behind an interface. Meanwhile, the asset and risk inventory may still show the old product name. That is the ground-level problem: authority and dependencies can change faster than the documentation.

## The speed gap is a leadership risk

The reported operation suggests an agent can lower the effort needed to sustain some hostile activity.[8] But not every attacker is running autonomous campaigns, and this case does not show that AI explains every increase in cyber risk. The gap is adaptation speed. Adversaries can experiment quickly; operators must test against complex estates, preserve service, coordinate teams and meet jurisdictional duties.

ENISA’s 2026 assessment places telecom among the most mature and critical sectors, but finds remediation and risk follow-through uneven. Legacy and inconsistent exercises remain constraints.[2] Even capable operators cannot close every gap at once. AI may put more pressure on those limits.

Here is the board-level question: **could hostile activity, combined with autonomous capabilities inside our own environment, outpace how we approve, monitor and contain change?** This is about the operating model. Can Security, Network, IT, Operations, Procurement, Legal and the business make a decision together before a critical workflow is involved?

## Regulation is the floor

Service providers already manage cybersecurity and privacy laws, communications-sector rules, resilience expectations, incident reporting, contractual duties and, in some markets, national-security requirements. In Europe, NIS2 brings electronic communications providers into a shared framework for cybersecurity risk management and incident reporting, implemented through national law.[4] The details vary by service and country. A multinational operator cannot assume that one compliance answer fits every market.

Compliance does not decide which agent can change a network configuration, what evidence is needed before autonomy expands, or who accepts the residual risk when a supplier’s AI feature reaches a critical workflow. Those are operational decisions. They need an owner and a record.

Two mistakes are common. Create a separate AI process that duplicates governance but misses high-impact deployments, or assume old policies cover every new capability. Extend security, architecture, change-management and supplier-risk processes to cover machine identities, delegated authority, data access, autonomy and reversibility. That is practical. Operators cannot wait for certainty, but they should know who owns each use, what it can affect, and what must be true before its authority grows.

## The decision is not “AI or no AI”

Operators have real reasons to use AI: improve customer experience, automate repetitive work and run complex networks more efficiently. Competitors and suppliers will keep moving. Waiting for perfect certainty can push experiments into less visible channels.

The answer is not blanket approval or prohibition. Start with bounded tasks. Know the data, identities and tools involved. Set approval points. Watch what the system does and make access reversible. The 2026 multi-agency guidance recommends this cautious progression, especially for sensitive data and critical systems.[3]

“Low risk” depends on the operator. A workflow may touch subscriber identity, billing, network configuration, emergency communications or a privileged supplier. Other uses, such as summarizing public information or helping an analyst organize evidence without system access, may be easier to contain. The operator must set the boundary.

Do not divide the world into “AI for the business” and “AI for security.” A customer agent may access sensitive data. A security copilot can be over-privileged. A network-optimization assistant can affect the controls protecting the network. Ownership follows access and impact, not the team that bought the feature.

## What must change in the next twelve months

A CISO or CTO does not need to solve every technical question this quarter. Three shifts matter now.

**Treat AI as part of the attack surface and operating model.** Track the identity, data, tools, supplier, owner and actions around each consequential use. If you do not know where it is used, you cannot decide where its authority should grow.

**Design for service continuity.** Containment, rollback, customer impact and regulatory notification can pull in different directions. Response plans must reflect the service, not just the system under investigation.

**Keep accountability in step with autonomy.** Name who approves each use, who owns the risk, what limits apply and how an unsafe action can be detected and reversed. Vendor assurance does not replace operator ownership.

The book will help readers choose three or four priorities for the next twelve months and defend them to the CEO and board. First, we need to know where this new authority can enter and how far it can reach. Chapter 1 explains why risk has changed. Chapter 2 maps where that change lands: the operator’s systems, suppliers, data and workflows.

## Sources

[1] https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector — Operation CYBER GUARDIAN: Singapore CSA and IMDA, 9 February 2026
[2] https://www.enisa.europa.eu/sites/default/files/2026-05/ENISA%20NIS360%202026.pdf — ENISA NIS360 2026
[3] https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services — Careful adoption of agentic AI services, 1 May 2026 (ASD ACSC and partners)
[4] https://digital-strategy.ec.europa.eu/en/policies/nis2-directive — European Commission: NIS2 Directive
[5] https://blogs.cisco.com/security/a-glimpse-into-cisco-mobile-infrastructure-security-developments — Oussama Naffati, A Glimpse Into Cisco Mobile Infrastructure Security Developments, 24 November 2025
[6] https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog — CISA Adds Six Known Exploited Vulnerabilities to Catalog, 10 November 2026
[7] https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt — Cisco BroadWorks Out-of-Band Blind XML External Entity Injection Vulnerability, advisory updated 12 November 2026
[8] https://malbearlabs.com/posts/operation-snowball-inside-an-autonomous-ai-intrusion-campaign — Malbear Labs, Operation Snowball: Inside an Autonomous AI Intrusion Campaign, 8 November 2026
