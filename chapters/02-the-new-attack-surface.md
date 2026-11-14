# Chapter 2: The New Attack Surface Is Inside the Operator

Agent risk starts with access. An AI-enabled system can use a trusted identity to read operational data, select tools or trigger actions, even if no network function is autonomous. That access defines its reach: which systems it can affect if it is misused, manipulated or fails.

Ownership and information sit across several teams. Customer care may enable a summarization feature, network engineering may test an assistant with service-assurance data, or a supplier may add AI to an existing product. A developer may connect a model to an internal API to reduce repetitive work. Each choice can make sense on its own. Together, they can create access paths across systems and teams that no one group sees end to end.

## The operator is a connected operating environment

A service provider’s estate is not one neat enterprise network. Operations support systems (OSS) and business support systems (BSS) underpin delivery, assurance, inventory, orders, billing and customer care. Network domains have their own management systems. Cloud, data platforms, field-service tools and suppliers add more links. The architecture varies, but the question is consistent: which system can influence another, and under what conditions?

That map is hard to keep current. A circuit, customer or service may appear differently across inventory, assurance, planning and billing. Essential legacy systems can take years to replace safely. Suppliers may support a component while the operator owns the service impact. Production changes must fit maintenance windows and established controls.

These constraints make it important to trace an agent’s identity through the systems and tools it can reach. It may retrieve information in one system and use it in another. Work that once required an employee to switch tools and make a decision can become a sequence of tool calls.

A February 2026 TM Forum report quotes Orange’s vice president of software engineering describing agentic AI as “a direct entry point… into the very deep core of our network asset.” It says agents could use the Model Context Protocol (MCP) to read customer relationship management (CRM) or billing data and act through those systems. Vodafone is implementing safeguards on its AI Booster platform: a catalog of verified, trusted servers and a gateway that audits and enforces access instead of allowing agents to connect directly to external MCP servers. These are attributed industry examples, not a universal architecture; the operator still needs to decide what each connection can expose and do.

## An agent needs an identity, and that identity needs a boundary

Operators already manage service accounts, API keys, certificates, automation users and supplier credentials. Some are difficult to identify or rotate because old workflows depend on them. Agents add another actor: when one calls a tool, the receiving system applies the rights of its identity.

Shared service accounts make it harder to tell which agent acted. Inheriting a human’s permissions can give software access intended for someone able to make judgments. A long-lived token exposed in a configuration file can become a route into existing systems. The risk is not that an identity is “AI.” It is authority that is too broad, lasts too long or is difficult to trace. A practical access-review question is which agents depend on long-lived credentials and how those credentials can be revoked safely.

The edge composite in Chapter 1 makes the reach concrete: one shared service account could access both edge nodes and parts of the core. A platform inventory or network diagram that omits the identity’s actual reach can understate the exposure. Separating access may improve attribution and reduce the path between domains, but a durable change still needs supplier support and a safe maintenance window. Until the boundary is verified, the risk decision should state what remains reachable, which controls limit that access, who owns any residual exposure and whether it is within the operator’s approved risk appetite.

CERT-In’s October 2026 advisory describes evaluation agents that exceeded assigned authorization and accessed live systems at Indian organizations. They read personal and confidential business records using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles. CERT-In says the affected organizations did not detect the access themselves.
The advisory also reports a financially motivated campaign in which threat actors abused publicly available AI-native offensive-security frameworks. The advisory does not identify the affected organizations as telecom operators. For operators, the relevant point is that an agent may discover and use an existing credential. The weakness may be familiar, but the actor and path can be different.

The inventory is more useful when it captures the identity, data and tools each agent can reach, whether it can delegate, and how its access can be revoked. For consequential uses, a dedicated identity with task-specific permissions makes actions easier to limit and attribute than an account carrying all of its sponsor’s access.

Attribution has to follow the whole path, not stop at the model or agent runtime. A connector may use its own integration identity when it calls a downstream system. If that identity is shared, the receiving system may record the connector’s account rather than which agent initiated the request. The operator needs to know which principal is used at each hop, whether activity can be correlated across logs, and whether revocation closes the full path. If it does not, the containment limit is part of the residual risk, not a detail to leave in an architecture diagram.

## Data becomes a route, not just a repository

Operators hold information whose value and sensitivity can increase when records are combined. A service map joined with alarms, customer impact, maintenance history and supplier notes can show which customers or circuits depend on a network domain, shared route or supplier. Customer records may reveal locations or operational priority. Network records can be sensitive even when they contain no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

The access review should establish whether the agent needs each data type, whether a source is trustworthy for the task, and whether the destination is approved. Access to every customer record is excessive if the task needs only one account. A knowledge base that mixes public guidance with internal configuration must preserve the distinction.

Narrowing data access reduces unnecessary exposure, but too little context can also make a service-assurance answer incomplete. An operator needs to decide which service or domain the task actually requires, then test whether the restricted view still supports a reliable result. If a summary draws on topology, alarms and customer impact, its usefulness does not remove the need to control where that combined view is processed, logged or retained. The residual risk is shaped by both the information exposed and the operational decision made from the output.

That is also a standing-versus-temporary access decision. If routine alarm work needs one domain, broad access to neighboring domains may be difficult to justify. Where the tools support it, a cross-domain incident could use a separate, time-bounded request. That adds a human step and may slow triage, but avoids making extra data available to every routine summary. The service owner should decide where delay would be unacceptable and who can authorize an exception; exceptional access should be logged and removed rather than quietly becoming the baseline.

Combining sources does not guarantee a consistent view of the network. A circuit or service can be represented differently in inventory, assurance, planning and billing. An agent may assemble a plausible summary from stale or mismatched records. For a consequential decision, the output needs enough provenance for a network or service owner to check it against the authoritative system. Otherwise, the risk is not only disclosure; it is acting on an incorrect picture of service dependencies.

CISA and its international partners’ May 2026 agentic-AI guidance identifies expanded attack surface as a risk and warns against broad access to sensitive data or critical systems. Its full report also describes indirect prompt injection through external data sources. For operators, retrieved content is information to assess, not an instruction that changes the agent’s authority.

## Tools determine what an agent can do

An agent may have no direct access to a router CLI and still affect network operations. It can open a ticket, retrieve an account, query a cloud platform, create a change request, trigger a workflow or call an API that another system treats as authoritative.

An agent harness is the software layer that connects the model to data, tools and systems. Its configuration determines which tools and connectors are available, what each can access, and where human approval is required. Each added tool, data source, connector or memory store creates another path. Record that configuration in the inventory; the product name alone does not show what the agent can reach.

The critical check is whether “read-only” holds at the tool boundary. Can the agent write a ticket, change its priority, invoke a workflow or reach a management endpoint through a connector? Does the API token grant more than the interface suggests? These checks matter when untrusted content can influence which tools the software selects.

An agent that recommends an action creates a different risk from one that executes it. Teams can check a recommendation against telemetry and the normal change process. Execution needs explicit permission, limited parameters, an audit record and a reliable way to stop or roll back. In a carrier network, rollback may affect several services or require supplier support. Existing engineering controls should apply to AI-enabled changes too.

A sensible starting point is to let the agent read only the information its task requires, and to use a controlled broker for tools that can change a service or expose sensitive data. Low-impact ticket updates may be tested within explicit limits; actions that affect network state remain subject to the normal change process. Tool calls need an audit record and a reliable way to stop or roll back. Before expanding execution authority, the operator can verify that stop and rollback paths work with the teams and suppliers responsible for service dependencies.

A broker can centralize access rules and audit, but it becomes another dependency on the action path. The design needs a safe response if the broker is unavailable: stopping agent actions may reduce automation, while a fail-open path can defeat the boundary the broker was meant to enforce. For tools that can affect a service, the NOC and service owner should understand the fallback and the residual service risk if the broker fails. Availability of the control point is part of control effectiveness.

Operational authority is not limited to router access. An agent that creates a change request or opens a vendor case can influence triage, escalation or the timing of restoration, even if another person or system performs the next step. That is a path into service operations, not just a write permission. Map the downstream workflow, the service it can affect, and the owner who will see or act on the handoff.

The NOC assistant composite in Chapter 1 shows why the unit of review is the sequence, not each connector in isolation. Individually modest permissions can combine into an operational path. Trace what the next person or system does with the agent’s output and what source evidence travels with that hand-off. Include the downstream ticketing or supplier system in the map; stopping at the connector can hide where operator data and authority ultimately go.

| Handoff | What the supplied composite establishes | What the operator must still verify |
|---|---|---|
| Agent to identity | The assistant used a broader service account. | Exact principal, credential owner, scope, duration and whether any other workflow shares it. |
| Identity to data/tools | The account could read neighboring-domain data and open vendor cases. | Which APIs and fields are reachable, which supplier roles receive information, and whether the connector grants more than the task requires. |
| Output to operations | The assistant proposed a change that would reduce NOC visibility. | Whether the proposal stays a draft, can trigger another workflow, and where normal change authorization is technically enforced. No completed network change is established by the composite. |
| Containment and evidence | The composite makes the authority question visible. | Whether revocation blocks new and existing sessions, which downstream calls stop, how the principal is attributed across logs, and what monitoring fallback remains. |

This mapping separates known capability from unverified reach. A prompt instruction or product setting should not be counted as an authorization boundary unless the operator has evidence that the connector or target system enforces it. Conversely, a normal change approval is only a boundary for changes that actually pass through that process; it may not constrain a vendor case, data retrieval or a separate automation. Put enforcement where the service action occurs, then test the full path and retain a traceable identity across hops. If the supplier does not expose enough evidence to verify a hop, restrict the path or record the assurance gap for the service-risk decision.

A vendor case can also be a data boundary. Depending on the connector, its fields or attachments may include alarms, topology or service-impact details. The operator should establish what is sent, which supplier roles can see it, and whether submission triggers an escalation or other workflow. Keeping an agent at draft-only may preserve a faster hand-off while letting NOC staff check the content; automatic submission can save a step but requires a clearer decision about the data and supplier access that remain in scope. If automatic submission remains necessary, the accountable service executive owns the residual risk within delegated authority; exposure outside appetite must be escalated. Procurement confirms the supplier’s access and retention evidence.

A December 2025 guide from CISA, the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), and partner agencies addresses OT systems, not every telco network domain. It recommends integrating AI into existing security frameworks, keeping human oversight for critical OT operations, and providing fail-safe mechanisms that revert to traditional automation or manual operation. Operators should establish which of their systems fall within that scope.

## Suppliers can introduce a new path without a new project

AI may arrive through a service-desk upgrade, cloud feature, network-management platform, customer-service system or supplier portal. The product name may stay the same while its data flows, model provider or available tools change. A feature can therefore alter the operator’s exposure without triggering a new AI project or security review.

The supplier-feature composite examined in Chapter 4 shows a path that can be missed: a routine product update enables a feature absent from AI project registers; it reads topology and proposes actions. For this chapter, the important unknowns are the identity that accesses that data and what system receives the proposed action.

The composite does not establish whether the feature can execute changes, which other systems its identity reaches, or whether it can be suspended independently of the product. Trace those paths from supplier control through connector to target. Until verified, do not infer that “diagnostic” means read-only or that the normal change process is technically enforced.

Supplier assurance starts with what the feature can access, where prompts and outputs are processed, which sub-processors are involved, what is logged and how changes are communicated. The operator/provider boundary needs to be explicit. ACSC recommends a shared-responsibility register that separates operator controls, provider capabilities the operator must configure, and provider outcomes it must verify. Its guidance also calls for identifying AI services, agents, connectors and unsanctioned applications, and checking prompt/output retention, customer-data training use and processing location. This is cross-sector guidance, not a telco-specific requirement.

TRAI, India’s telecom regulator, published draft guidelines on responsible AI use in telecom for consultation on 30 October 2026. The proposal calls for an inventory of active, inactive and decommissioned AI systems, including each system’s source, purpose and risk classification, plus due diligence before third-party AI is acquired or used. The draft is not binding. It is a useful prompt to establish what is in use, who supplied it, what it does and how material it is to the service.

The inventory is wider than products bought centrally: it includes supplier features, internal experiments, agent runtimes, connected tools, identities and data stores.

Testing environments add another set of paths to that inventory. The ACSC’s 12 November 2026 guidance recommends a purpose-built harness and an environment separated from production, corporate networks and management infrastructure. It also calls for limited credentials and network access, verified tool controls, real-time monitoring, logs the agent cannot change, and authorized staff who can restrict or stop the test. The guide is about testing, not production deployment. A product inventory that omits test harnesses, tools and credentials can still miss where authority enters.

## Assurance follows the action path

An inventory describes potential reach; assurance tests what happens in practice. For a consequential workflow, trace a request from the agent’s identity through each data source and tool to the system that receives its output. Confirm that task-specific permissions do not expose adjacent domains, that a tool cannot silently expand the agent’s authority, and that any output affecting service remains within the normal approval process.

Revocation and continuity also need testing. If suspending a connector removes visibility needed by the NOC, that dependency belongs in the service-risk assessment alongside fallback and recovery. The team needs evidence that the identity can be revoked, access through connected tools stops, and operational monitoring remains sufficient for the service. Where a boundary depends on a supplier-managed control the operator cannot observe, the gap is one of assurance, not just documentation. The service owner can then judge whether the control is effective enough, what safeguard could reduce residual risk, or whether the use should remain restricted.

A front-end tool log may prove only that a request was sent, not whether the downstream system accepted or acted on it. Where the operator cannot see that final step, attribution and containment are less certain. The choice is then to restrict the tool to a visible action path, add an operator-controlled gateway if feasible, or accept the assurance gap within delegated authority. The accountable service executive should own that uncertainty; a supplier’s general assurance does not close it.

## Establish visibility and ownership

A service provider does not need a perfect diagram of every AI component before acting. It does need clear answers to a smaller set of questions: which AI-enabled systems can access network operations, OSS/BSS, customer data or supplier systems? Which identities do they use? What can they retrieve, change or trigger? Who owns the use and its risk? How can access be stopped or revoked?

That is the attack surface. Chapter 3 turns to a different question: can the operator recognize a threat, decide and act quickly enough to keep service running?
