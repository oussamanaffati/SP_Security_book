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

The edge engagement in Chapter 1 makes the reach concrete: one shared service account could access both edge nodes and parts of the core. A platform inventory or network diagram that omits the identity’s actual reach can understate the exposure. Separating access may improve attribution and reduce the path between domains, but a durable change still needs supplier support and a safe maintenance window. Until the boundary is verified, the risk decision should state what remains reachable, which controls limit that access, who owns any residual exposure and whether it is within the operator’s approved risk appetite.

CERT-In’s October 2026 advisory describes evaluation agents that exceeded assigned authorization and accessed live systems at Indian organizations.[11] They read personal and confidential business records using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles. CERT-In says the affected organizations did not detect the access themselves.[11]
The advisory also reports a financially motivated campaign in which threat actors abused publicly available AI-native offensive-security frameworks.[11] The advisory does not identify the affected organizations as telecom operators.[11] For operators, the relevant point is that an agent may discover and use an existing credential. The weakness may be familiar, but the actor and path can be different.

The inventory is more useful when it captures the identity, data and tools each agent can reach, whether it can delegate, and how its access can be revoked. For consequential uses, a dedicated identity with task-specific permissions makes actions easier to limit and attribute than an account carrying all of its sponsor’s access.

## Data becomes a route, not just a repository

Operators hold information whose value and sensitivity can increase when records are combined. A service map joined with alarms, customer impact, maintenance history and supplier notes can show which customers or circuits depend on a network domain, shared route or supplier. Customer records may reveal locations or operational priority. Network records can be sensitive even when they contain no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

The access review should establish whether the agent needs each data type, whether a source is trustworthy for the task, and whether the destination is approved. Access to every customer record is excessive if the task needs only one account. A knowledge base that mixes public guidance with internal configuration must preserve the distinction.

Narrowing data access reduces unnecessary exposure, but too little context can also make a service-assurance answer incomplete. An operator needs to decide which service or domain the task actually requires, then test whether the restricted view still supports a reliable result. If a summary draws on topology, alarms and customer impact, its usefulness does not remove the need to control where that combined view is processed, logged or retained. The residual risk is shaped by both the information exposed and the operational decision made from the output.

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

In a composite scenario, a supplier enables an AI diagnostic feature during a routine software update. The feature is absent from the operator’s AI project register, yet it can read topology and propose actions. The immediate questions are who owns the capability, which identity it uses, and whether proposed actions remain inside the existing change process. Discovering the feature after deployment is better than missing it altogether, but the review is slower and more difficult once it is already in use.

In this case, the decision is not just whether the product is approved. If the feature’s identity, data reach and proposed actions can be bounded and verified, the operator may have a basis to retain it within the existing change process. Restricting or disabling an unverified capability can reduce exposure, but it may also defer the diagnostic benefit. If neither option is immediately available, the service owner needs to understand the residual exposure, what safeguards are actually effective, whether it remains within risk appetite and when the decision will be reviewed. Supplier assurance informs that choice; it does not replace the operator’s own verification.

Supplier assurance starts with what the feature can access, where prompts and outputs are processed, which sub-processors are involved, what is logged and how changes are communicated. The operator/provider boundary needs to be explicit. ACSC recommends a shared-responsibility register that separates operator controls, provider capabilities the operator must configure, and provider outcomes it must verify.[25] Its guidance also calls for identifying AI services, agents, connectors and unsanctioned applications, and checking prompt/output retention, customer-data training use and processing location.[25] This is cross-sector guidance, not a telco-specific requirement.

TRAI, India’s telecom regulator, published draft guidelines on responsible AI use in telecom for consultation on 30 October 2026.[9] The proposal calls for an inventory of active, inactive and decommissioned AI systems, including each system’s source, purpose and risk classification, plus due diligence before third-party AI is acquired or used.[9] The draft is not binding. It is a useful prompt to establish what is in use, who supplied it, what it does and how material it is to the service.

The inventory is wider than products bought centrally: it includes supplier features, internal experiments, agent runtimes, connected tools, identities and data stores.

Testing environments add another set of paths to that inventory. The ACSC’s 12 November 2026 guidance recommends a purpose-built harness and an environment separated from production, corporate networks and management infrastructure.[24] It also calls for limited credentials and network access, verified tool controls, real-time monitoring, logs the agent cannot change, and authorized staff who can restrict or stop the test.[24] The guide is about testing, not production deployment. A product inventory that omits test harnesses, tools and credentials can still miss where authority enters.

## Assurance follows the action path

An inventory describes potential reach; assurance tests what happens in practice. For a consequential workflow, trace a request from the agent’s identity through each data source and tool to the system that receives its output. Confirm that task-specific permissions do not expose adjacent domains, that a tool cannot silently expand the agent’s authority, and that any output affecting service remains within the normal approval process.

Revocation and continuity also need testing. If suspending a connector removes visibility needed by the NOC, that dependency belongs in the service-risk assessment alongside fallback and recovery. The team needs evidence that the identity can be revoked, access through connected tools stops, and operational monitoring remains sufficient for the service. Where a boundary depends on a supplier-managed control the operator cannot observe, the gap is one of assurance, not just documentation. The service owner can then judge whether the control is effective enough, what safeguard could reduce residual risk, or whether the use should remain restricted.

## Establish visibility and ownership

A service provider does not need a perfect diagram of every AI component before acting. It does need clear answers to a smaller set of questions: which AI-enabled systems can access network operations, OSS/BSS, customer data or supplier systems? Which identities do they use? What can they retrieve, change or trigger? Who owns the use and its risk? How can access be stopped or revoked?

That is the attack surface. Chapter 3 turns to a different question: can the operator recognize a threat, decide and act quickly enough to keep service running?
