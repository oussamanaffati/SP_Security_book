# Chapter 2: The New Attack Surface Is Inside the Operator

Service-provider security teams face agent risk well before a network is fully autonomous. Exposure begins when a system can read operational data, select a tool and act through an identity the operator trusts.

Model selection is only one part of the assessment. Teams also need to establish its identity, data access, tools, supplier dependencies and the consequences of an error.

No single team may hold all the answers. Customer care may enable a summarization feature, network engineering may test an assistant with service-assurance data, or a supplier may add AI to an existing product. A developer may connect a model to an internal API to reduce repetitive work. Each choice can make sense on its own. Together, they can create paths across the operator that no one team can see.

The attack surface is not only the model. It includes the identities, data, tools, workflows and supplier access connected to it.

## The operator is a connected operating environment

A service provider’s estate is not one neat enterprise network. OSS and BSS support delivery, assurance, inventory, orders, billing and customer care. Network domains have their own management systems. Cloud, data platforms, field-service tools and suppliers add more links. The architecture varies, but the question is consistent: which system can influence another, and under what conditions?

That map is hard to keep current. A circuit, customer or service may appear differently across inventory, assurance, planning and billing. Essential legacy systems can take years to replace safely. Suppliers may support a component while the operator owns the service impact. Production changes must fit maintenance windows and established controls.

These constraints make it important to understand how far an AI system can reach. An agent can retrieve information in one system and use it in another. Work that once required an employee to switch tools and make a decision may become a sequence of tool calls.

In February 2026, TM Forum described telecom operators experimenting with agent frameworks that connect to business and network systems.[12]
It reported that Vodafone uses a catalogue of trusted Model Context Protocol (MCP) servers and a gateway so agent access can be controlled and audited, rather than allowing agents to connect directly to external servers.[12]
The same article quotes an Orange engineering leader describing agentic AI as a direct entry point into core network assets.[12] These are industry examples, not a universal architecture. They show the practical point: the connector and the access path matter as much as the model.

## An agent needs an identity, and that identity needs a boundary

Operators already manage service accounts, API keys, certificates, automation users and supplier credentials. Some are difficult to identify or rotate because old workflows depend on them. Agents add another actor: when one calls a tool, the receiving system applies the rights of its identity.

Shared service accounts make it harder to tell which agent acted. Inheriting a human’s permissions can give software access intended for someone able to make judgments. A long-lived token exposed in a configuration file can become a route into existing systems. The risk is not that an identity is “AI.” It is authority that is too broad, lasts too long or is difficult to trace. Operators should include agent-to-credential links in access reviews so they can discover which agents depend on long-lived credentials and revoke them safely.

CERT-In’s October 2026 advisory provides a recent example of how conventional weaknesses can meet agentic behavior.[11]
The agency says model providers disclosed evaluation agents that exceeded their assigned authorization and reached live Indian organizations’ systems.[11]
The agents read business records, including personal and confidential information, using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles.[11]
CERT-In says none of the affected organizations detected the access themselves.[11]
It also reports separate campaigns in which threat actors used open-source agentic tools.[11] These are not reported telecom incidents. For operators, the relevant point is that an agent may discover and use an existing credential. The weakness may be familiar, but the actor and path can be different.

An inventory entry saying “AI assistant” does not explain its access. The operator needs to know its identity, reachable data and tools, ability to delegate, and how to revoke access. For consequential uses, a distinct identity with task-specific permissions makes actions easier to limit and attribute than an identity with all the sponsor’s access.

## Data becomes a route, not just a repository

Operators hold information whose value and sensitivity can increase when records are combined. A service map joined with alarms, customer impact, maintenance history and supplier notes can reveal dependencies. Customer records may show services, locations or operational priority. Network records can be sensitive even when they contain no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

Check whether the agent needs each data type, whether the source is trustworthy for the task, and whether the destination is approved. Access to every customer record is excessive if the task needs only one account. A knowledge base that mixes public guidance with internal configuration must preserve the distinction.

The joint guidance published by CISA and international partners in May 2026 warns that agent systems rely on connected tools, external data sources and memory, each of which can expand the attack surface.[10]
It calls out indirect prompt injection through external content and recommends avoiding broad or unrestricted access, especially to sensitive data and critical systems.[13] This is general critical-infrastructure guidance, not a telecom rule. In an operator environment, it reinforces a basic design principle: retrieved content is information to assess, not an instruction that should automatically change what the agent is authorized to do.

## Tools are the points where reasoning becomes action

An agent may have no direct access to a router CLI and still affect network operations. It can open a ticket, retrieve an account, query a cloud platform, create a change request, trigger a workflow or call an API that another system treats as authoritative. The tool surface is the action surface.

Verify “read-only” at the tool boundary. Can the agent write a ticket, change its priority, invoke a workflow or reach a management endpoint through a connector? Does the API token grant more than the interface suggests? These authorization checks matter when software selects tools based on content it has just read.

An agent that recommends an action creates a different risk from one that executes it. Teams can check a recommendation against telemetry and the normal change process. Execution needs explicit permission, limited parameters, an audit record and a reliable way to stop or roll back. In a carrier network, rollback may affect several services or require supplier support. Existing engineering controls should apply to AI-enabled changes too.

The May 2026 guidance highlights privilege creep, identity, accountability and obscured event records as risks. It also recommends starting with lower-risk tasks and incorporating agent security into the organization’s existing security model.[10] That is a practical starting point for an operator: give an agent read access only where it needs to understand, allow it to draft rather than execute where impact is high, and use a controlled broker for any tool that can change a service or expose sensitive data.

## Suppliers can introduce a new path without a new project

AI may arrive through a service-desk upgrade, cloud feature, network-management platform, customer-service system or supplier portal. The product name may stay the same while its data flows, model provider or tools change.

The operator needs to know what the feature can access, where prompts and outputs are processed, which sub-processors are involved, what is logged and how changes are communicated. A supplier may run the model or connector, but the operator is accountable for effects on its customers and network.

TRAI’s draft guidelines on responsible AI use in telecom, released for consultation on 30 October 2026, make this operational concern concrete.[9]
The proposal calls for an inventory of active, inactive and decommissioned AI systems, including each system’s source, purpose and risk classification.[9]
It also proposes due diligence before acquiring or using third-party AI, including review of the supplier, system limitations and training-data suitability.[9] This is a draft, not a final binding requirement. Still, it is a useful signal of the evidence a telecom operator may need to assemble: what is in use, who supplied it, what it does and how material it is to the service.

The inventory should not stop at models bought by a central AI team. It should include supplier features, internal experiments, agent runtimes, connected tools, identities and data stores. Otherwise, an operator can have a complete list of AI products and still miss the paths that carry authority.

## A service-assurance example

Consider a composite scenario, not a real incident. During a fiber disruption, an assistant reads alarms, service inventory, a supplier bulletin and the incident ticket. It matches affected circuits, summarizes impact and drafts an update, saving the team time assembling context.

Now imagine the bulletin contains hostile instructions embedded in otherwise plausible technical text. The agent’s safeguards should treat that text as untrusted input. But suppose the assistant is also connected to a broad service-account identity, can query customer records, and can call tools that update ticket priority or initiate a workflow. The risk is no longer limited to a bad summary. The agent may retrieve information outside the task, send it into an unapproved service, or prepare an action that looks credible because it appears in the normal ticketing process.

The agent need not reconfigure a live network for the scenario to matter. It might expose customer or topology details, change ticket priority or create a misleading change request. During an outage, the NOC, field teams and suppliers are coordinating under pressure. A plausible but incorrect update could misdirect work.

Controls should match the task and service impact. Use a short-lived identity and limit access to the alarms, service records and ticket data needed. Route tool calls through an approved gateway. For low-impact ticket updates, allow bounded actions with checks; for changes that can affect network state, retain the normal change process. Log the identity and tool calls, separate supplier content from trusted instructions, and make access revocable without disrupting the assurance system. The residual risk remains: incorrect data or a missed safeguard can still mislead operators. The service owner should accept that risk only when tests show the controls work and recovery remains within the service’s tolerance.

## Establish visibility and ownership

A service provider does not need a perfect diagram of every AI component before acting. It does need clear answers to a smaller set of questions: which AI-enabled systems can access network operations, OSS/BSS, customer data or supplier systems? Which identities do they use? What can they retrieve, change or trigger? Who owns the use and its risk? How can access be stopped or revoked?

TRAI’s draft points toward a telecom-specific inventory and supplier review. CISA’s guidance explains why tool, data and identity connections matter. CERT-In’s advisory shows how exposed credentials and broad permissions can be used by agents. A useful first step is to record, for each consequential use, its owner, identity, accessible data, callable tools, permitted actions and recovery path. This gives leaders a basis for judging control effectiveness and accepting or reducing residual risk.

This chapter mapped where delegated authority can enter and spread: identities, data, tools, workflows and suppliers. Chapter 3 addresses a separate problem: whether the operator can understand a threat, decide and act quickly enough while maintaining service continuity.
