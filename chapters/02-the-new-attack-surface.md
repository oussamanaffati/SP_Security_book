# Chapter 2: The New Attack Surface Is Inside the Operator

Agent risk starts with access. An AI-enabled system can use a trusted identity to read operational data, select tools or trigger actions, even if no network function is autonomous. That access defines its reach: which systems it can affect if it is misused, manipulated or fails.

Ownership and information sit across several teams. Customer care may enable a summarization feature, network engineering may test an assistant with service-assurance data, or a supplier may add AI to an existing product. A developer may connect a model to an internal API to reduce repetitive work. Each choice can make sense on its own. Together, they can create access paths across systems and teams that no one group sees end to end.

## The operator is a connected operating environment

A service provider’s estate is not one neat enterprise network. Operations support systems (OSS) and business support systems (BSS) underpin delivery, assurance, inventory, orders, billing and customer care. Network domains have their own management systems. Cloud, data platforms, field-service tools and suppliers add more links. The architecture varies, but the question is consistent: which system can influence another, and under what conditions?

That map is hard to keep current. A circuit, customer or service may appear differently across inventory, assurance, planning and billing. Essential legacy systems can take years to replace safely. Suppliers may support a component while the operator owns the service impact. Production changes must fit maintenance windows and established controls.

These constraints make it important to trace an agent’s identity through the systems and tools it can reach. It may retrieve information in one system and use it in another. Work that once required an employee to switch tools and make a decision can become a sequence of tool calls.

In its February 2026 report, TM Forum quotes Orange’s vice president of software engineering calling agentic AI “a direct entry point… into the very deep core of our network asset.”[12]
The report explains that agents could use the Model Context Protocol (MCP) to read data from systems such as customer relationship management (CRM) and billing, then act through those systems.[12]
It says Vodafone is implementing MCP safeguards on its AI Booster platform, using a catalog of verified, trusted servers and a gateway.[12]
Through that gateway, access rules can be audited and enforced instead of letting agents reach external MCP servers directly.[12]
These are attributed industry examples, not a universal architecture. The operator’s question is which data each connection can expose and what the agent can do with it.

## An agent needs an identity, and that identity needs a boundary

Operators already manage service accounts, API keys, certificates, automation users and supplier credentials. Some are difficult to identify or rotate because old workflows depend on them. Agents add another actor: when one calls a tool, the receiving system applies the rights of its identity.

Shared service accounts make it harder to tell which agent acted. Inheriting a human’s permissions can give software access intended for someone able to make judgments. A long-lived token exposed in a configuration file can become a route into existing systems. The risk is not that an identity is “AI.” It is authority that is too broad, lasts too long or is difficult to trace. A practical access-review question is which agents depend on long-lived credentials and how those credentials can be revoked safely.

CERT-In’s October 2026 advisory describes evaluation agents that exceeded assigned authorization and accessed live systems at Indian organizations.[11] They read personal and confidential business records using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles. CERT-In says the affected organizations did not detect the access themselves.[11]
The advisory also reports a financially motivated campaign in which threat actors abused publicly available AI-native offensive-security frameworks.[11] The advisory does not identify the affected organizations as telecom operators.[11] For operators, the relevant point is that an agent may discover and use an existing credential. The weakness may be familiar, but the actor and path can be different.

The inventory is more useful when it captures the identity, data and tools each agent can reach, whether it can delegate, and how its access can be revoked. For consequential uses, a dedicated identity with task-specific permissions makes actions easier to limit and attribute than an account carrying all of its sponsor’s access.

## Data becomes a route, not just a repository

Operators hold information whose value and sensitivity can increase when records are combined. A service map joined with alarms, customer impact, maintenance history and supplier notes can show which customers or circuits depend on a network domain, shared route or supplier. Customer records may reveal locations or operational priority. Network records can be sensitive even when they contain no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

The access review should establish whether the agent needs each data type, whether a source is trustworthy for the task, and whether the destination is approved. Access to every customer record is excessive if the task needs only one account. A knowledge base that mixes public guidance with internal configuration must preserve the distinction.

May 2026 multi-agency guidance identifies expanded attack surface as a risk of agentic AI and warns against broad access to sensitive data or critical systems.[10] Its full report describes indirect prompt injection through external data sources.[13] For operators, retrieved content is information to assess, not an instruction that changes the agent’s authority.

## Tools determine what an agent can do

An agent may have no direct access to a router CLI and still affect network operations. It can open a ticket, retrieve an account, query a cloud platform, create a change request, trigger a workflow or call an API that another system treats as authoritative.

An agent harness is the software layer that connects the model to data, tools and systems.[38] Its configuration determines which tools and connectors are available, what each can access, and where human approval is required.[38] Each added tool, data source, connector or memory store creates another path.[38] Record that configuration in the inventory; the product name alone does not show what the agent can reach.

The critical check is whether “read-only” holds at the tool boundary. Can the agent write a ticket, change its priority, invoke a workflow or reach a management endpoint through a connector? Does the API token grant more than the interface suggests? These checks matter when untrusted content can influence which tools the software selects.

An agent that recommends an action creates a different risk from one that executes it. Teams can check a recommendation against telemetry and the normal change process. Execution needs explicit permission, limited parameters, an audit record and a reliable way to stop or roll back. In a carrier network, rollback may affect several services or require supplier support. Existing engineering controls should apply to AI-enabled changes too.

A sensible starting point is to let the agent read only the information its task requires, and to use a controlled broker for tools that can change a service or expose sensitive data. Low-impact ticket updates may be tested within explicit limits; actions that affect network state remain subject to the normal change process. Tool calls need an audit record and a reliable way to stop or roll back. Before expanding execution authority, the operator can verify that stop and rollback paths work with the teams and suppliers responsible for service dependencies.

Multi-agency operational technology (OT) guidance released in December 2025 recommends integrating AI into existing security frameworks, keeping human oversight for critical OT operations, and providing fail-safe mechanisms that revert to traditional automation or manual operation.[39] It applies to OT systems, not every telco network domain; operators should establish which of their systems fall within that scope.

## Suppliers can introduce a new path without a new project

AI may arrive through a service-desk upgrade, cloud feature, network-management platform, customer-service system or supplier portal. The product name may stay the same while its data flows, model provider or available tools change. A feature can therefore alter the operator’s exposure without triggering a new AI project or security review.

In a composite scenario, a supplier enables an AI diagnostic feature during a routine software update. The feature is absent from the operator’s AI project register, yet it can read topology and propose actions. The operator first needs to establish who owns the capability, which identity it uses, and whether any proposed action remains inside the existing change process. Discovering the feature after deployment is better than missing it altogether, but the review is slower and more difficult once it is already in use.

Supplier assurance should establish what the feature can access, where prompts and outputs are processed, which sub-processors are involved, what is logged and how changes are communicated. The boundary between operator controls and provider duties needs to be explicit. For cloud AI, the Australian Cyber Security Centre (ACSC) recommends a shared responsibility register that distinguishes operator controls, provider capabilities the operator must configure, and provider outcomes it must verify.[25]

The Telecom Regulatory Authority of India (TRAI) released draft guidelines on responsible AI use in telecom for consultation on 30 October 2026.[9]
The proposal calls for an inventory of active, inactive and decommissioned AI systems, including each system’s source, purpose and risk classification.[9]
It also proposes due diligence before acquiring or using third-party AI, including review of the supplier, system limitations and training-data suitability.[9] The draft is not a binding requirement yet. For an operator, it is a practical prompt to establish what is in use, who supplied it, what it does and how material it is to the service.

The inventory should not stop at models bought by a central AI team. Include supplier features, internal experiments, agent runtimes, connected tools, identities and data stores. October 2026 guidance from the ACSC calls for AI asset identification to include services, agents, connectors and unsanctioned AI applications.[25] It also recommends checking what providers retain in prompts and outputs, whether they use customer data to train models, and where processing occurs.[25] This is cross-sector guidance, not a telco-specific requirement.

Map test environments too, including their harnesses, tools and credentials.
The ACSC guidance published on 12 November 2026 recommends a purpose-built harness and test environment separated from production, corporate networks and management infrastructure.[24]
It also recommends limiting the test agent’s credentials and network access, verifying tool and network controls before testing, monitoring agents in real time, and storing logs on a system the agent cannot access or modify.[24]
It calls for authorized staff with the ability to restrict or terminate testing.[24]
The guide does not cover production deployments.[24] Otherwise, an operator can have a complete list of AI products and still miss the paths that carry authority.

## A service-assurance example

This is a composite scenario, not a reported incident. During a fiber disruption, an assistant reads alarms, service inventory, a supplier bulletin and the incident ticket. It matches affected circuits, summarizes impact and drafts an update, saving the team time assembling context.

Now imagine the bulletin contains hostile instructions embedded in otherwise plausible technical text. The agent’s safeguards should treat that text as untrusted input. But suppose the assistant is also connected to a broad service-account identity, can query customer records, and can call tools that update ticket priority or initiate a workflow. The risk is no longer limited to a bad summary. The agent may retrieve information outside the task, disclose it to an unapproved third-party service, or prepare an action that looks credible because it appears in the normal ticketing process.

The agent need not reconfigure a live network for the scenario to matter. It might expose customer or topology details, change ticket priority or create a misleading change request. During an outage, the network operations center (NOC), field teams and suppliers are coordinating under pressure. A plausible but incorrect update could misdirect work.

Controls must match the task and service impact. Use a short-lived identity with access only to relevant alarms, service records and ticket data. Route tool calls through an approved gateway. Tested low-impact ticket updates may be allowed; changes that affect network state should remain in the normal change process. Log the agent identity and its tool calls. Keep supplier content separate from trusted instructions, and test that access can be revoked without disrupting service assurance.

A service exercise can check the full path: trace an action from identity through tool call to result, revoke access, then confirm that the fallback still works.

Residual risk remains. Incorrect data or a missed safeguard can still mislead operators. The executive accountable for the service should accept that risk against the operator’s appetite only after tests show that the controls work and recovery meets service tolerance.

## Establish visibility and ownership

A service provider does not need a perfect diagram of every AI component before acting. It does need clear answers to a smaller set of questions: which AI-enabled systems can access network operations, OSS/BSS, customer data or supplier systems? Which identities do they use? What can they retrieve, change or trigger? Who owns the use and its risk? How can access be stopped or revoked?

That is the attack surface. Chapter 3 turns to a different question: can the operator recognize a threat, decide and act quickly enough to keep service running?
