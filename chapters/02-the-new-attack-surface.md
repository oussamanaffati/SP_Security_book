# Chapter 2: The New Attack Surface Is Inside the Operator

An agent can affect network operations without logging in to a router. With a trusted identity, it may read operational data, submit a supplier case or trigger another workflow. Map that identity’s reach before assessing the model or product label.

AI may enter through a customer-care feature, a network-engineering pilot, a supplier update or a developer’s API integration. Each can look local. Together, they can create access paths that no single team has mapped end to end.

## The operator is a connected operating environment

A service provider’s estate is not one neat enterprise network. Operations support systems (OSS) and business support systems (BSS) underpin delivery, assurance, inventory, orders, billing and customer care. Network domains have their own management systems. Cloud, data platforms, field-service tools and suppliers add more links. The architecture varies, but the question is consistent: which system can influence another, and under what conditions?

That map is hard to keep current. A circuit, customer or service may appear differently across inventory, assurance, planning and billing. Essential legacy systems can take years to replace safely. Suppliers may support a component while the operator owns the service impact. Production changes must fit maintenance windows and established controls.

These constraints make it important to trace an agent’s identity through the systems and tools it can reach. It may retrieve information in one system and use it in another. Work that would otherwise require an employee to switch tools and make a decision may become a sequence of tool calls.

TM Forum’s February 2026 report quotes Orange’s vice president of software engineering calling agentic AI “a direct entry point… into the very deep core of our network asset.” It says agents could use the Model Context Protocol (MCP) to read customer relationship management (CRM) or billing data and act through those systems.

The report also says Vodafone is implementing safeguards on its AI Booster platform: a catalog of verified, trusted servers and a gateway that audits and enforces access, rather than direct agent connections to external MCP servers. These are attributed examples, not universal architectures. Each operator must decide what a connection can expose and do.

## An agent needs an identity, and that identity needs a boundary

Operators already manage service accounts, application programming interface (API) keys, certificates, automation users and supplier credentials. Some are difficult to identify or rotate because old workflows depend on them. Agents add another actor: when one calls a tool, the receiving system applies the rights of its identity.

Shared service accounts make it harder to tell which agent acted. Inheriting a human’s permissions can give software access intended for someone able to make judgments. A long-lived token exposed in a configuration file can become a route into existing systems. The risk is not that an identity is “AI.” It is authority that is too broad, lasts too long or is difficult to trace. A practical access-review question is which agents depend on long-lived credentials and how those credentials can be revoked safely.

The shared edge/core account from Chapter 1 makes the reach concrete: one account could access edge nodes and parts of the core. An inventory that omits the identity’s reach understates exposure. Separating access may improve attribution and reduce the cross-domain path, but needs supplier support and a safe maintenance window; until tested, treat the boundary as unverified.

An October 2026 CERT-In advisory says evaluation agents at unnamed Indian organizations exceeded their assigned authorization and accessed live systems. They read personal and confidential business records using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles. The organizations did not detect the access themselves.

Separately, the advisory reports one financially motivated campaign using publicly available AI-native offensive-security frameworks. It does not identify the affected organizations as telecom operators. The relevant point for operators is narrower: an agent can discover and use an existing credential, turning a familiar weakness into a new access path.

For consequential uses, give the agent a dedicated, task-scoped identity rather than its sponsor’s broader account. Record the data and tools it can reach, whether it can delegate, and how access can be revoked; test the target boundary, not only the agent configuration.

Attribution has to follow the call path to the target. A connector may use its own identity, so the target records the connector rather than the initiating agent. Correlation IDs may join the logs if every step carries them, but they do not narrow authority. Revocation must reach the target too: disabling an upstream token may leave an open session or queued action alive.

**Choose the identity boundary.** Prefer a target-native principal with narrow scope and clear logs. If the target cannot distinguish agents, a shared connector identity is harder to attribute; correlation helps only if it links requester, approver and target result. An operator-controlled broker can enforce scope, but only if direct routes are blocked. Human review preserves a person in the downstream decision, at the cost of NOC effort and delay. Choose by target enforcement and service tolerance, not deployment convenience.

**Illustrative variant (assumption):** the network operations center (NOC) assistant submits vendor cases through an identity shared with another workflow. Prefer a target-native principal. Otherwise use a broker only if the target accepts calls through it, scope is enforced, and logs join agent, approver and result. If neither boundary is verifiable, keep submission human-reviewed. Test allowed and denied requests and revocation; if downstream sessions cannot be ended, keep submission outside the assistant.

## Data becomes a route, not just a repository

Operators hold information whose value and sensitivity can increase when records are combined. A service map joined with alarms, customer impact, maintenance history and supplier notes can show which customers or circuits depend on a network domain, shared route or supplier. Customer records may reveal locations or operational priority. Network records can be sensitive even when they contain no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

The access review should establish whether the agent needs each data type, whether a source is trustworthy for the task, and whether the destination is approved. Access to every customer record is excessive if the task needs only one account. A knowledge base that mixes public guidance with internal configuration must preserve the distinction.

**Choose the processing boundary.** An operator-managed environment can reduce one supplier data path but still needs updates, privileged support, logs, backups, connectivity and compute capacity. A supplier-hosted service avoids the operator running that infrastructure, but adds dependencies on provider location, support access, sub-processors, retention, availability and exit terms. Filtering fields or masking identifiers can reduce exposure, but may remove context needed for service assurance and increase manual checks. No option is automatically safer.

For topology or customer data, start with the minimum fields and a route the operator can verify. Check supplier terms against deployed routing, including support access and backups. Check runtime destination and retention separately: a successful request proves neither deletion nor the full data path. If a material route is unknown, keep sensitive data out or keep the output advisory until it is clarified.

**Retain a trace without keeping every prompt.** For a topology query that drafts a supplier case, full-content logs can help reconstruct the hand-off but duplicate sensitive detail and widen access. Without a joinable record, investigators may not link the request, connector call and target result. A structured event can record principal, task ID, connector and target, timestamp, policy and approval results, outcome, and source references.

Keep joinable metadata by default; retain prompt/output content only when the task or an incident procedure requires it. Data owners and Legal/Privacy define permitted content and retention. Identity and access management (IAM) should be able to link principal, connector and target result; suppliers should describe provider-side logs, support access, backups and deletion. Keep traces distinct from persistent memory. Test retrieval and deletion with a synthetic marker at each boundary. A product setting or deletion request alone does not prove every copy is gone.

**Multi-market processing decision.** A regional summary can join records owned by different markets. Legal and Compliance should map obligations by market and data type; a regional endpoint does not establish that a transfer is permitted or controlled. A common “strictest-market” configuration is not a substitute for mapping where data is processed or who approves operational changes in each market.

If an operator proposes a regional summary of alarms, topology and supplier cases, test whether correlation needs only a market tag, service identifier, event time and alarm category. Do not assume customer identities or full case attachments are necessary.

The operator can send raw records to one regional service, run separate local instances, or filter records locally and share only an approved summary. Raw regional processing can simplify correlation, but combines more sensitive data, adds supplier and market-review paths, and creates a wider service dependency if unavailable.

Local instances reduce routine transfer but duplicate compute, updates and support, and may fragment a regional incident view. Local filtering limits what moves, but requires field mapping and validation; if the summary removes information the NOC needs, analysts may have to return to manual cross-market lookups. Use an authorized, time-bounded hand-off for that case-specific lookup; do not silently widen routine retrieval.

Start with local processing of full records and a regional read-only summary containing only fields proven necessary for correlation. Treat the summary as operationally sensitive until the fields and combinations are reviewed; aggregation alone does not make it safe to share. Keep customer identities and full case attachments local unless the data owner and Legal/Compliance approve a specific need. Do not allow the assistant to act across markets. If the filtered view cannot support a reliable service decision, keep processing local and use an authorized case-specific hand-off rather than expanding the standing feed.

Before scaling, estimate local filtering, connector, supplier, market-review and NOC-reconciliation work. Verify deployed routes and permissions with synthetic allowed/denied requests across market scopes; exercise triage with the fallback. Check retention and deletion separately.

Scale only when Legal/Compliance clears the route, the service owner finds the summary useful, and the platform accounts for prompts, outputs, logs, backups, telemetry and supplier access.

**Partial-region decision.** A market kept out of the regional feed must not appear as a quiet market. A missing or stale source can look like “no event” when it actually means “not observed.” Show whether each market’s source is current, delayed, withheld or unavailable, with an owner and last-update time.

Set freshness to match the decision: a delay tolerated for trend analysis may be unacceptable during an incident. Do not let the assistant make a region-wide “clear” recommendation when required markets are absent or stale.

If a market’s route or field approval is unresolved, keep its raw data local and mark the regional view incomplete. The NOC can send a minimum case-specific summary through an authorized path, but reconciliation may delay triage; compare that cost with routine transfer. Test a synthetic event with one delayed or withheld source. The summary should name the market and suppress a region-wide “clear.” If the test is unsafe, require local confirmation.

**Illustrative variant (assumptions):** routine alarm summaries need one domain; incident diagnosis may require neighboring-domain alarms or case fields. The composite does not establish that IAM can issue a time-bounded read role or that the NOC can support manual lookup.

Standing cross-domain access removes approval delay but exposes routine summaries to data they do not need. Manual lookup limits routine reach but adds NOC effort and delay. A time-bounded read role can bridge the two, but depends on IAM, workflow and supplier support and may still be too slow. Use it only if approval and expiry fit service tolerance.

Keep routine summaries within one domain. For diagnosis, request only the extra fields needed and expire access when that scope ends. Agree the trigger, target and expiry in advance. Verify that the target permits the approved request, denies out-of-scope access, expires the role and ends relevant sessions. If the target cannot enforce expiry, use the manual path.

Persistent memory is another data path. It can carry service, customer or supplier details into later tasks, and a supplier’s prompt/output-retention statement may not describe every memory layer. Identify what can be written and retrieved, by whom, how long it remains and how deletion is verified. The data owner sets permitted content; the platform or supplier owner explains retrieval and clearing.

**Choose how NOC context persists.** The scenario does not say whether persistent memory is enabled or needed. For recurring alarm summaries, compare task-scoped retrieval, a curated read-only store and assistant-written memory. Task-scoped context limits reuse but adds retrieval and review work. A curated store avoids assistant-written operational history but needs a freshness and update process. Assistant-written memory carries context across tasks but can preserve stale topology or earlier errors; it needs scope, write controls, expiry and verified deletion.

Start with task-scoped context from authoritative sources. Retain more only if lookup or re-entry effort justifies it; consider a curated read-only store before assistant-written memory. Name permitted sources, freshness rule, read identity, user scope and removal path. If access or deletion cannot be verified, do not retain sensitive context.

Test the intended store with an approved synthetic marker: the permitted task should retrieve it, a separately scoped user should not, and expiry or deletion should remove it. Record the path and expected/observed results. If the marker escapes scope or persists, do not use memory for sensitive context. This checks only the store and path tested.

Joined records can conflict. Inventory, assurance, planning and billing may describe the same circuit differently. Show the source and freshness of each value; have the network or service owner check the result against the authoritative system before acting.

For a consequential workflow, agree the permitted fields, source authority, freshness, joins and conflict handling before relying on the summary.

| Field | Record | If unknown or unverifiable |
|---|---|---|
| Task and minimum data | Decision supported and fields required. | Remove fields without a task need; availability is not justification. |
| Source authority | Authoritative system for each field and its data owner. | Mark unknown until the owner confirms it; the model must not choose between systems. |
| Provenance and freshness | Source, timestamp and transformations; set a freshness limit when age affects the decision. | Show missing or stale provenance and require an owner to verify before use. |
| Join and destination | Permitted combinations, approved destination and downstream recipient. | Narrow the join or destination until the route is understood. |
| Conflict and decision | How conflicts are surfaced and who resolves them; who decides whether the output is fit for service use. | Show the conflict; block recommendation or action until the data owner resolves it. |

Use the contract to make inputs and uncertainty visible. When a field’s source or freshness is unknown, show the attributed record instead of a joined service-impact claim.

**Illustrative source-contract check.** Use synthetic or approved records with a stale value and a conflict. The summary should preserve source and timestamp, surface the conflict and withhold a service-impact recommendation until it is resolved. This tests the workflow, not the source records. If the check is unsafe, keep the summary advisory and verify the authoritative records before acting.

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) and its international partners’ May 2026 agentic-AI guidance identifies expanded attack surface and warns against broad access to sensitive data or critical systems. The full report describes indirect prompt injection through external data. For operators, retrieved content is input to assess, not an instruction that grants authority.

For the NOC assistant, excluding tickets and supplier cases removes a manipulation path but returns lookup work to the NOC. Keep those sources read/draft; retrieved content must not grant tool authority. In a separated environment, test whether benign or hostile content steers tool choice or destination, then confirm connector/target denial and logs linking source, principal and result. If the target outcome or NOC view is unavailable, keep the action outside the assistant.

## Tools determine what an agent can do

Often the critical boundary is the tool path: a connector may expose a ticket API, cloud platform, management endpoint or workflow that the target treats as authoritative.

An agent harness is the software layer that connects the model to data, tools and systems. Its configuration determines which tools and connectors are available, what each can access, and where human approval is required. Each added tool, data source, connector or memory store creates another path. Record that configuration in the inventory; the product name alone does not show what the agent can reach.

The critical check is whether “read-only” holds at the tool boundary. Can the agent write a ticket, change its priority, invoke a workflow or reach a management endpoint through a connector? Does the API token grant more than the interface suggests? These checks matter when untrusted content can influence which tools the software selects.

Recommendation and execution require different authority. A person can check a proposed action against telemetry and normal change control. Execution needs explicit task rights, narrow parameters, an attributable record, and a tested stop and recovery path. In a carrier network, rollback may affect neighboring services or require supplier support.

Begin with task-limited read access. Put write tools behind a broker or equivalent target control, but keep network-state changes in the normal change process. Test low-impact ticket updates within bounded fields; expand only when the NOC can stop the action and restore the service, using supplier support where needed.

A broker centralizes access rules and logs but adds a dependency. Fail-open can bypass the control; fail-closed can stop monitoring if reads share the broker. Separate alarm reads where possible and fail closed on actions. If the paths cannot be separated, define the degraded service view and emergency procedure.

Test broker loss with a new request, active session and queued action. Verify target denial, attribution, independent visibility and fallback.

Ticket and vendor-case tools can influence triage, escalation or restoration without changing the network directly. Trace the NOC assistant from identity through connector to the hand-off; permissions that look modest in isolation can combine into a consequential path.

| Path segment | Established facts | Required check and owner |
|---|---|---|
| Agent to identity | The assistant used a broader service account. | IAM/platform confirms principal, owner, scope, duration and sharing; workflow owner confirms need. |
| Identity to data/tools | The account read neighboring-domain data and opened vendor cases. | Connector/platform traces APIs, fields, supplier roles and targets; data owner confirms need. |
| Output to operations | The assistant proposed a visibility-reducing change; completion is not established. | NOC/change owner confirms draft status and where approval is enforced. |
| Containment | Reach is known; revocation behavior is not. | IAM/platform tests session revocation and target denial; NOC/service assurance verifies attribution and fallback. |

Prompts and product settings do not authorize actions; the connector or target must enforce the boundary. Normal change approval covers only actions routed through it.

Vendor cases are both a data and workflow boundary: attachments may include alarms, topology or service-impact details. The assistant can draft, submit after review or submit automatically. Drafts keep NOC effort in the path; automatic submission may send sensitive details or trigger supplier work before an operator sees them. Approval counts only if the reviewer sees the payload, recipient and downstream action.

Keep cases at human-reviewed draft until payload, recipient, supplier access and retention are visible. Measure NOC effort and service delay. In a non-customer test, verify payload, destination, target principal, submission and revocation. If a hop is unobservable, keep submission manual or remove sensitive fields. Automate only when the boundary is enforceable and the faster hand-off justifies the dependency. Network changes remain in normal change control.

A December 2025 guide from CISA, the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), and partner agencies addresses operational technology (OT) systems, not every telco network domain. It recommends integrating AI into existing security frameworks, keeping human oversight for critical OT operations, and providing fail-safe mechanisms that revert to traditional automation or manual operation. Operators should establish which of their systems fall within that scope.

## Suppliers can introduce a new path without a new project

An AI feature may arrive with a service-desk upgrade, cloud feature, network-management platform, customer-care system or supplier portal rather than as a distinct project. The product name may stay the same while data flows, model provider or tools change. Inventory supplier features, internal experiments, agent runtimes, connectors, identities and data stores, not only centrally purchased products.

The supplier-diagnostic composite illustrates the problem. A routine update enabled a feature that reads topology and proposes actions. Its identity, target authority and independent disablement are not established; “diagnostic” does not mean read-only.

Supplier assurance should cover access, prompt/output handling, sub-processors, logs, retention and change notices. ACSC recommends a shared-responsibility register separating operator controls, provider capabilities the operator configures and provider outcomes it verifies. Its cross-sector guidance also calls for inventorying AI services, agents, connectors and unsanctioned applications, and checking prompt/output retention, customer-data training use and processing location. It is not telecom-specific.

The Telecom Regulatory Authority of India (TRAI) published draft responsible-AI guidelines for telecom consultation on 30 October 2026. The proposal calls for an inventory of active, inactive and decommissioned AI systems by source, purpose and risk class, and due diligence before third-party AI is acquired or used. The draft is not binding. It is a practical prompt to ask what systems are in use, who supplies them and which services they affect.

Test harnesses belong in the inventory too. ACSC’s 12 November 2026 guidance recommends a purpose-built environment isolated from production, corporate and management networks, with only the required credentials, network and tool access, real-time monitoring, protected logs and staff able to stop testing. It covers testing, not production; inventory the harness, tools and credentials as access paths.

## Assurance follows the action path

Inventory maps potential reach. Assurance follows a call through identity, connector, target and downstream service. A connector log alone does not prove the target acted or denied access. If the target result is not visible, keep high-impact actions manual or behind a target-enforced gateway.

The CISO’s first mapping decision is which identities and connectors can reach network operations, OSS/BSS, customer data or supplier workflows. Trace those paths first, prioritizing those with service-changing authority. Chapter 3 asks whether the operator can respond quickly enough without worsening service impact.
