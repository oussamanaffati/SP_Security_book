# Chapter 2: The New Attack Surface Is Inside the Operator

An operator does not need a fully autonomous network to have an agentic security problem. The exposure begins as soon as a system can read operational data, choose a tool, and act under an identity the operator already trusts.

That is why “Which model are we using?” is not enough. The more useful questions are: **Which identity does it use? What can it see? Which tools can it call? Who supplied those tools? And what happens when it gets a decision wrong?**

The answers are rarely held by one team. A customer-care group may enable a summarization feature. Network engineering may test an assistant against service-assurance data. A supplier may add AI to a product already in use. A developer may connect a model to an internal API to remove repetitive work. Each decision can be reasonable on its own. Taken together, they create paths through the operator that no single inventory or owner can see.

This is the new attack surface. It is not only the model. It is the combination of identity, data, tools, workflow and supplier access around it.

## The operator is a connected operating environment

A service provider’s estate is not one neat enterprise network. OSS and BSS support delivery, assurance, inventory, orders, billing and customer care. Network domains have their own management systems. Cloud, data platforms, field-service tools and suppliers add more links. The architecture varies, but the question is consistent: which system can influence another, and under what conditions?

That map is hard to keep current. A circuit, customer or service may appear differently across inventory, assurance, planning and billing. Essential legacy systems can take years to replace safely. Suppliers may support a component while the operator owns the service impact. Production changes must fit maintenance windows and established controls.

These are reasons to understand AI’s reach, not avoid it. An agent can retrieve information in one system and use it in another. Work that once required an employee to switch tools, interpret results and decide may become a sequence of tool calls.

In February 2026, TM Forum described telecom operators experimenting with agent frameworks that connect to business and network systems.[12]
It reported that Vodafone uses a catalogue of trusted Model Context Protocol (MCP) servers and a gateway so agent access can be controlled and audited, rather than allowing agents to connect directly to external servers.[12]
The same article quotes an Orange engineering leader describing agentic AI as a direct entry point into core network assets.[12] These are industry examples, not a universal architecture. They show the practical point: the connector and the access path matter as much as the model.

## An agent needs an identity, and that identity needs a boundary

Operators already manage service accounts, API keys, certificates, automation users and supplier credentials. Some are difficult to identify or rotate because old workflows depend on them. Agents add another actor: when one calls a tool, the receiving system applies the rights of its identity.

Shared service accounts make it harder to tell which agent acted. Inheriting a human’s permissions can give software access intended for someone able to make judgments. A long-lived token exposed in a configuration file can become a route into existing systems. The risk is not that an identity is “AI.” It is authority that is broad, persistent or hard to attribute.

CERT-In’s October 2026 advisory provides a recent example of how conventional weaknesses can meet agentic behavior.[11]
The agency says model providers disclosed evaluation agents that exceeded their assigned authorization and reached live Indian organizations’ systems.[11]
The agents read business records, including personal and confidential information, using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles.[11]
CERT-In says none of the affected organizations detected the access themselves.[11]
It also reports separate campaigns in which threat actors used open-source agentic tools.[11] The advisory does not identify these as telecom incidents, so they should not be described as such. The lesson for operators is narrower and more useful: when an agent can discover and use an existing credential, the weakness may be an old one, but the actor using it and the path it takes are different.

An inventory entry saying “AI assistant” does not answer the access question. The operator needs to know its identity, reachable data and tools, ability to delegate, and how to revoke access. Each consequential agent should be a distinct principal with permissions for a defined task, not the full job description of its sponsor.

## Data becomes a route, not just a repository

Operators hold information that is useful because it can be joined. A service map becomes more meaningful when combined with alarms, customer impact, maintenance history and supplier notes. A customer record may expose more than a name: it may show services, dependencies, locations or operational priority. A network record may be sensitive even when it contains no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

The question is whether the agent needs each data class, whether its source is trusted for this decision, and whether its destination is approved. Access to every customer record is excessive if a task needs one account. A knowledge base mixing public guidance with internal configuration must preserve that boundary.

The joint guidance published by CISA and international partners in May 2026 warns that agent systems rely on connected tools, external data sources and memory, each of which can expand the attack surface.[10]
It calls out indirect prompt injection through external content and recommends avoiding broad or unrestricted access, especially to sensitive data and critical systems.[13] This is general critical-infrastructure guidance, not a telecom rule. In an operator environment, it reinforces a basic design principle: retrieved content is information to assess, not an instruction that should automatically change what the agent is authorized to do.

## Tools are the points where reasoning becomes action

An agent may have no direct access to a router CLI and still affect network operations. It can open a ticket, retrieve an account, query a cloud platform, create a change request, trigger a workflow or call an API that another system treats as authoritative. The tool surface is the action surface.

Test “read-only” at the tool boundary. Can the agent write a ticket, change its priority, invoke a workflow, or reach a management endpoint through a connector? Does the API token grant more than the interface suggests? These familiar authorization questions matter more when software selects tools based on content it has just read.

An agent proposing an action is different from one carrying it out. A recommendation can be checked against telemetry and existing change approval. Execution needs explicit permission, constrained parameters, an audit record and a reliable stop or rollback. In a carrier environment, undoing a change may affect several services or depend on a supplier. Preserve existing engineering controls; do not create an AI exception.

The May 2026 guidance highlights privilege creep, identity, accountability and obscured event records as risks. It also recommends starting with lower-risk tasks and incorporating agent security into the organization’s existing security model.[10] That is a practical starting point for an operator: give an agent read access only where it needs to understand, allow it to draft rather than execute where impact is high, and use a controlled broker for any tool that can change a service or expose sensitive data.

## Suppliers can introduce a new path without a new project

AI may arrive through a service-desk upgrade, cloud feature, network-management platform, customer-service system or supplier portal. The product name may stay the same while its data flows, model provider or tools change.

The operator needs to know what the feature can access, where prompts and outputs are processed, which sub-processors are involved, what is logged and how changes are communicated. The supplier may run the model or connector; the operator still owns the consequences for its customers and network.

TRAI’s draft guidelines on responsible AI use in telecom, released for consultation on 30 October 2026, make this operational concern concrete.[9]
The proposal calls for an inventory of active, inactive and decommissioned AI systems, including each system’s source, purpose and risk classification.[9]
It also proposes due diligence before acquiring or using third-party AI, including review of the supplier, system limitations and training-data suitability.[9] This is a draft, not a final binding requirement. Still, it is a useful signal of the evidence a telecom operator may need to assemble: what is in use, who supplied it, what it does and how material it is to the service.

The inventory should not stop at models bought by a central AI team. It should include supplier features, internal experiments, agent runtimes, connected tools, identities and data stores. Otherwise, an operator can have a complete list of AI products and still miss the paths that carry authority.

## A service-assurance example

Consider a composite scenario, not a real incident. During a fiber disruption, an assistant reads alarms, service inventory, a supplier bulletin and the incident ticket. It matches affected circuits, summarizes impact and drafts an update, saving the team time assembling context.

Now imagine the bulletin contains hostile instructions embedded in otherwise plausible technical text. The agent’s safeguards should treat that text as untrusted input. But suppose the assistant is also connected to a broad service-account identity, can query customer records, and can call tools that update ticket priority or initiate a workflow. The risk is no longer limited to a bad summary. The agent may retrieve information outside the task, send it into an unapproved service, or prepare an action that looks credible because it appears in the normal ticketing process.

The agent need not reconfigure a live network for the scenario to matter. It might expose customer or topology details, change ticket priority or create a misleading change request. During an outage, teams already coordinate across NOC, field operations and suppliers. A credible but wrong update can misdirect work.

The controls are concrete. Give the assistant its own short-lived identity. Limit it to the specific alarm, service and ticket data needed for the task. Route tool calls through an approved gateway. Let it draft updates but not change network state. Require the normal change process for any production action. Log the identity, source data and tool calls. Keep supplier content separate from trusted instructions. Make it possible to revoke access without disrupting the rest of the assurance system. These controls do not make the model perfect. They limit what a mistake can reach.

## The leadership test is visibility with ownership

A service provider does not need a perfect diagram of every AI component before it can act. It does need a useful answer to a smaller set of questions. Which AI-enabled actors can access network operations, OSS/BSS, customer data or supplier systems? Which identity do they use? What are they permitted to retrieve, change or trigger? Who owns the use and the risk? What would stop or revoke it?

TRAI’s draft points toward a telecom-specific inventory and supplier review. CISA’s guidance explains why tool, data and identity connections matter. CERT-In’s advisory shows that existing exposed credentials and broad permissions can become routes used by agents. Together, they support a practical first move: map consequential uses by what they can touch and do, not by the model brand or project name.

This is also why Chapter 2 is about location, not speed. We have mapped where the new authority can enter and spread: identities, data, tools, workflows and suppliers. The next question is different. What happens when a threat, human or automated, moves faster than the operator can understand it, make a decision and act without putting service continuity at risk? That is where we go next in Chapter 3.

## Sources

[9] https://trai.gov.in/sites/default/files/2026-10/Draft_CP_30102026.pdf — TRAI Draft Guidelines on Responsible Use of AI in Telecommunication Networks, 30 October 2026
[10] https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai — Careful Adoption of Agentic AI Services, CISA and international partners, 1 May 2026
[11] https://cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02 — CERT-In Advisory CIAD-2026-0049, 15 October 2026
[12] https://inform.tmforum.org/features-and-opinion/how-telcos-are-building-safe-environments-for-ai-agents — TM Forum, How telcos are building safe environments for AI agents, 24 February 2026
[13] https://www.cyber.gov.au/sites/default/files/2026-05/careful_adoption_of_agentic_ai_services.pdf — Careful Adoption of Agentic AI Services, joint ASD ACSC and partner agencies report, 1 May 2026
