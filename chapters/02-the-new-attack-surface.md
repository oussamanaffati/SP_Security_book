# Chapter 2: The New Attack Surface Is Inside the Operator

Agent risk starts with access. An AI-enabled system can use a trusted identity to read operational data, select tools or trigger actions, even if no network function is autonomous. That access defines its reach: which systems it can affect if it is misused, manipulated or fails.

AI may enter through a customer-care feature, a network-engineering pilot, a supplier update or a developer’s API integration. Each can look local. Together, they can create access paths across systems that no one team sees end to end.

## The operator is a connected operating environment

A service provider’s estate is not one neat enterprise network. Operations support systems (OSS) and business support systems (BSS) underpin delivery, assurance, inventory, orders, billing and customer care. Network domains have their own management systems. Cloud, data platforms, field-service tools and suppliers add more links. The architecture varies, but the question is consistent: which system can influence another, and under what conditions?

That map is hard to keep current. A circuit, customer or service may appear differently across inventory, assurance, planning and billing. Essential legacy systems can take years to replace safely. Suppliers may support a component while the operator owns the service impact. Production changes must fit maintenance windows and established controls.

These constraints make it important to trace an agent’s identity through the systems and tools it can reach. It may retrieve information in one system and use it in another. Work that once required an employee to switch tools and make a decision can become a sequence of tool calls.

TM Forum’s February 2026 report quotes Orange’s vice president of software engineering calling agentic AI “a direct entry point… into the very deep core of our network asset.” It says agents could use the Model Context Protocol (MCP) to read customer relationship management (CRM) or billing data and act through those systems. The report also says Vodafone is implementing safeguards on its AI Booster platform: a catalog of verified, trusted servers and a gateway that audits and enforces access, rather than direct agent connections to external MCP servers. These are attributed examples, not universal architectures; each operator must decide what a connection can expose and do.

## An agent needs an identity, and that identity needs a boundary

Operators already manage service accounts, API keys, certificates, automation users and supplier credentials. Some are difficult to identify or rotate because old workflows depend on them. Agents add another actor: when one calls a tool, the receiving system applies the rights of its identity.

Shared service accounts make it harder to tell which agent acted. Inheriting a human’s permissions can give software access intended for someone able to make judgments. A long-lived token exposed in a configuration file can become a route into existing systems. The risk is not that an identity is “AI.” It is authority that is too broad, lasts too long or is difficult to trace. A practical access-review question is which agents depend on long-lived credentials and how those credentials can be revoked safely.

The shared edge/core service account described in Chapter 1 makes the reach concrete: one account could access edge nodes and parts of the core. A platform inventory or network diagram that omits the identity’s actual reach can understate exposure. Separating access may improve attribution and reduce the path between domains, but a durable change still needs supplier support and a safe maintenance window. Until the supported change is tested, mark reachable systems and the enforcement boundary as unverified.

An October 2026 CERT-In advisory says evaluation agents at unnamed Indian organizations exceeded their assigned authorization and accessed live systems. They read personal and confidential business records using exposed credentials and connection settings in application configuration, public repositories and permissive cloud roles. The organizations did not detect the access themselves.

Separately, the advisory reports one financially motivated campaign using publicly available AI-native offensive-security frameworks. It does not identify the affected organizations as telecom operators. The relevant point for operators is narrower: an agent can discover and use an existing credential, turning a familiar weakness into a new access path.

For consequential uses, give the agent a dedicated, task-scoped identity rather than its sponsor’s broader account. Record the data and tools it can reach, whether it can delegate, and how access can be revoked; test the target boundary, not only the agent configuration.

Attribution has to follow the whole path, not stop at the model or agent runtime. A connector may use its own integration identity when it calls a downstream system; if that identity is shared, the target may record the connector rather than the initiating agent. An event ID that links logs can improve investigation, but it does not reduce permissions or make a target deny an unauthorized request. Revocation needs the same path view: disabling an upstream token may stop new calls without ending an open target session or queued action.

**Choose how identity crosses each connector.** Identity can cross a connector in four ways. A target-native principal gives the clearest authorization and attribution, but depends on target and supplier support and a narrow token scope. A shared connector identity is simpler, but the target may not distinguish agents; correlation helps only if it reliably joins the originating principal, approver, request and target result. An operator-controlled broker can enforce scope and preserve that mapping, but adds a dependency and a bypass risk if direct routes remain. Human-reviewed access keeps a person in the downstream decision, at the cost of NOC effort and delay. Choose by target enforcement and service tolerance, not deployment convenience.

**Connector decision variant (assumption):** the NOC assistant submits vendor cases through an identity shared with another workflow. Prefer a target-native principal if the platform and supplier support it. Otherwise, use an operator-controlled broker only if the target accepts calls solely through it, the broker enforces scope, and logs link agent, approver, target and result. If neither boundary is verifiable, keep case submission outside the assistant and use the existing human process; event correlation alone is not authorization. Test an allowed and denied request, revoke the identity, and verify sessions and queued actions. If the target cannot expose or terminate downstream sessions, restrict the action path. Include IAM, connector, supplier and NOC effort in the local estimate.

## Data becomes a route, not just a repository

Operators hold information whose value and sensitivity can increase when records are combined. A service map joined with alarms, customer impact, maintenance history and supplier notes can show which customers or circuits depend on a network domain, shared route or supplier. Customer records may reveal locations or operational priority. Network records can be sensitive even when they contain no personal data.

An agent can search a retrieval system, read a ticket, query service inventory and summarize results in a chat window. That can save time, but it may also send information to a supplier service or retain it in logs, prompts, traces or memory after the task ends.

The access review should establish whether the agent needs each data type, whether a source is trustworthy for the task, and whether the destination is approved. Access to every customer record is excessive if the task needs only one account. A knowledge base that mixes public guidance with internal configuration must preserve the distinction.

**Choose the processing boundary.** Keeping a workflow in an operator-managed environment may reduce one supplier data path, but it still needs updates, privileged support, logs, backups and connectivity; it also consumes engineering and compute capacity. A supplier-hosted service can avoid building that path locally, but adds dependence on provider location, support access, sub-processors, retention, availability and exit terms. Restricting fields or masking identifiers is a third route: it can reduce exposure, but may remove context needed for a service-assurance answer and increase manual cross-checks. No option is automatically safer.

For topology or customer data, start with the minimum fields and a route the operator can verify. Check supplier terms against deployed routing, including logs, backups and support access. Verify runtime destination and retention separately; a successful request proves neither deletion nor the full data path. If a material route remains unknown, keep sensitive data out of the workflow or keep its output advisory until a narrower view or evidence closes the gap.

**Retain trace evidence without keeping every prompt.** The NOC-assistant case does not specify trace retention. For decision analysis, consider a task that reads topology and drafts a supplier case. Full content logs can help reconstruct a hand-off but duplicate sensitive detail and broaden access. Without a joinable record, the operator may be unable to link a request to its connector call and target result. A structured event record is a middle route: principal, task/correlation ID, connector and target, timestamp, policy and approval results, outcome, and source references.

Retain joinable metadata in an operator-controlled or verifiable store by default; capture prompt/output content only when the task or an incident procedure requires it. The data owner defines permitted content; Security/IAM needs the identity and target trace; Legal/Privacy confirms purpose, retention and access; the supplier describes provider-side logs, support access, backups and deletion. Keep traces distinct from persistent memory. Test role-based retrieval and deletion with a synthetic marker at each boundary, including provider-side stores. A product setting or deletion request alone is not evidence that every copy is gone. Budget for access control, redaction, retention and investigation support.

**Multi-market processing decision.** A regional summary can join records owned by different markets. Legal and Compliance should map obligations by market and data type; a regional endpoint does not establish that a transfer is permitted or controlled.

**Decision variant (assumptions):** a multi-market service-assurance team wants a regional summary of alarms, topology and supplier cases. Test whether correlation needs only a market tag, service identifier, event time and alarm category; do not assume customer identities or full case attachments are necessary. The composite does not establish a transfer, approval or tested minimum.

The operator can send raw records to one regional service, run separate local instances, or filter records locally and share only an approved summary. Raw regional processing makes correlation simpler, but combines more sensitive data, increases the number of owners and supplier paths to govern, and creates a wider dependency if the service is unavailable. Local instances reduce routine transfer but duplicate compute, updates and support, and may fragment a regional incident view. Local filtering limits what moves, but requires field mapping and validation; if the summary removes information the NOC needs, analysts will return to manual cross-market lookups. That case-specific lookup should use the time-bounded path above, not silently widen routine retrieval.

Start with local processing of full records and a regional read-only summary containing only fields proven necessary for correlation. Treat the summary as operationally sensitive until the fields and combinations are reviewed; aggregation alone does not make it safe to share. Keep customer identities and full case attachments local unless the data owner and Legal/Compliance approve a specific need. Do not allow the assistant to act across markets. If the filtered view cannot support a reliable service decision, keep processing local and use an authorized case-specific hand-off rather than expanding the standing feed.

Before scaling, estimate local filtering, connector, supplier, market-review and NOC-reconciliation work. Evidence should cover deployed routes and permissions, synthetic allowed/denied requests across market scopes, and an operational exercise of triage with fallback. Check retention and deletion separately. Expand only when Legal/Compliance confirms the route, the service owner finds the summary useful, and technical evidence covers prompts, outputs, logs, backups, telemetry and supplier access. If a material path remains unknown, keep that market’s raw data local and revisit when evidence changes.

**Partial-region decision.** A market kept out of the regional feed must not appear as a quiet market. A missing or stale source can look like “no event” when it actually means “not observed.” Require the summary to show, for each market, whether its source is current, delayed, withheld or unavailable, with an owner and last-update time. The freshness limit is a service decision: a delay tolerated for retrospective trend analysis may be unacceptable during an incident. Do not let the assistant make a region-wide “clear” recommendation when required markets are absent or stale.

If one market’s route or field approval remains unresolved, keep its raw data local and mark the regional view as incomplete. The local NOC can use approved sources and send a minimum, case-specific summary through an authorized path. This adds reconciliation work and may delay triage; the service owner should weigh that cost against widening routine transfer. Test with a synthetic event and a delayed or withheld source. The result should name the missing market and suppress any unsupported region-wide “clear.” If the test is unsafe, require local confirmation. This verifies missing-source handling, not legal permission or every data route.

Narrowing data access reduces unnecessary exposure, but too little context can make a service-assurance answer incomplete. Decide which service or domain the task needs, then test whether the restricted view still supports a reliable answer. If it does not, request the minimum additional context through a separate, traceable path and keep the output advisory until the expanded scope is justified.

**Decision variant (assumptions):** routine alarm summaries need one network domain; incident diagnosis may require neighboring-domain alarms or case fields. Assume IAM can issue a time-bounded read role and the NOC can support manual lookup. The composite does not establish either capability.

Standing cross-domain access avoids an approval delay but exposes routine summaries to data they do not need and weakens attribution. Manual lookup keeps the assistant inside its usual domain, at the cost of NOC hand-offs and delay; any details returned to the assistant still need approval. A separate time-bounded read role limits routine reach, but requires IAM, workflow and supplier support and can still delay triage if approval is unclear. Estimate that work before scaling.

Keep routine summaries within one domain. For an incident, request only the extra fields needed for the service decision and remove the privilege when that scope expires. The data owner confirms the fields; the service owner sets acceptable delay and fallback; the delegated service executive approves an exception within authority. If the current approval path cannot meet service tolerance, prepare a pre-authorized route before an incident.

Test that the target allows the approved request and denies an out-of-scope one; expiry must block new calls and end relevant sessions, with logs showing agent, approver, target and fields accessed. Exercise the manual hand-off and confirm NOC visibility. If the target cannot enforce expiry, use the manual path. Pre-authorize a read role only if an exercise shows approval delay exceeds service tolerance; fix its fields, target, trigger, deputy and expiry.

Persistent memory is a separate data path, not an invisible part of the model. It can spare teams from re-entering context, but may carry service, customer or supplier details into later tasks. A supplier’s prompt/output-retention statement does not necessarily describe every memory layer. Record what can be written and read, which identities and workflows can retrieve it, the retention and deletion behavior, and who can verify those boundaries: the data owner sets permitted content, while the platform or supplier owner provides evidence of scope and clearing.

**Choose how NOC context persists.** The composite does not specify whether persistent memory is enabled or needed. For recurring alarm summaries, compare three options. Task-scoped context retrieves approved records for each task; it limits reuse but still needs prompt/log checks and can add retrieval and review work. A curated, read-only store avoids assistant-written operational history but needs an owner for source freshness, indexing and updates. Assistant-written memory carries context across tasks, but can also preserve stale topology or earlier errors; it needs separate write controls, scope, expiry and verified deletion. These are different operating models, not equivalent settings.

Start with task-scoped context from authoritative sources. Retain more only if observed lookup or re-entry effort justifies it; consider a curated read-only store before assistant-written memory. Name the data owner, sources, freshness rule, read identity, permitted users and removal owner. Include update and review work in the cost. If access scope or deletion cannot be verified, do not retain sensitive context.

For a consequential workflow, test with an approved synthetic marker in a safe environment: confirm retrieval in the permitted scope, denial from a separately scoped task or user, and expiry/deletion. Record expected and observed results, principal and log source. Any cross-scope retrieval or failure to clear means no sensitive persistent memory; use task-scoped or manual handling. This verifies only the tested store and path, not general model behavior or every data source.

Combining sources does not guarantee a consistent view of the network. A circuit or service can be represented differently in inventory, assurance, planning and billing. An agent may assemble a plausible summary from stale or mismatched records. For a consequential decision, the output needs enough provenance for a network or service owner to check it against the authoritative system. Otherwise, the risk is not only disclosure; it is acting on an incorrect picture of service dependencies.

A source contract makes the data boundary testable. Before a consequential workflow relies on joined records, the data owner and workflow owner should agree what the agent may use and how it must handle uncertainty.

| Field | Record | If unknown or unverifiable |
|---|---|---|
| Task and minimum data | Decision supported and fields required. | Remove fields without a task need; availability is not justification. |
| Source authority | Authoritative system for each field and its data owner. | Mark unknown until the owner confirms it; the model must not choose between systems. |
| Provenance and freshness | Source, timestamp and transformations; set a freshness limit when age affects the decision. | Show missing or stale provenance and require an owner to verify before use. |
| Join and destination | Permitted combinations, approved destination and downstream recipient. | Narrow the join or destination until the route is understood. |
| Conflict and decision | How conflicts are surfaced and who resolves them; who decides whether the output is fit for service use. | Show the conflict; block recommendation or action until the data owner resolves it. |

This contract does not validate source accuracy or the agent’s reasoning. It makes inputs and uncertainty visible. If a field’s source or freshness is unknown, display the attributed record rather than present a joined service-impact claim.

**Illustrative source-contract check.** Use synthetic or approved records with one stale value and one intentional conflict. Confirm that the summary preserves source and timestamp, surfaces the conflict, and withholds a service-impact recommendation until the data owner resolves it. The service owner then decides whether the corrected output fits the operational decision. Record expected and observed results and test limits. This checks provenance handling for one workflow, not source-system accuracy or general model behavior. If a safe test is unavailable, keep the summary advisory and verify authoritative records before acting.

CISA and its international partners’ May 2026 agentic-AI guidance identifies expanded attack surface as a risk and warns against broad access to sensitive data or critical systems. Its full report also describes indirect prompt injection through external data sources. For operators, retrieved content is information to assess, not an instruction that changes the agent’s authority.

For the NOC assistant, excluding tickets and supplier cases removes one manipulation path but returns lookup work to the NOC. Read/draft use preserves context; retrieved content must never grant tool authority. On the current facts, keep these sources read/draft and deny related actions at the connector or target. In a separated test environment, check whether benign and hostile content changes tool choice or destination, then verify target denial and logs linking source, principal and result. If target outcomes or NOC visibility cannot be verified, keep actions outside the assistant and use the manual path. Expand only when those boundaries and fallback are demonstrated.

## Tools determine what an agent can do

An agent may have no direct access to a router CLI and still affect network operations. It can open a ticket, retrieve an account, query a cloud platform, create a change request, trigger a workflow or call an API that another system treats as authoritative.

An agent harness is the software layer that connects the model to data, tools and systems. Its configuration determines which tools and connectors are available, what each can access, and where human approval is required. Each added tool, data source, connector or memory store creates another path. Record that configuration in the inventory; the product name alone does not show what the agent can reach.

The critical check is whether “read-only” holds at the tool boundary. Can the agent write a ticket, change its priority, invoke a workflow or reach a management endpoint through a connector? Does the API token grant more than the interface suggests? These checks matter when untrusted content can influence which tools the software selects.

Recommendation and execution require different authority. A person can check a proposed action against telemetry and normal change control. Execution needs explicit task rights, narrow parameters, an attributable record, and a tested stop and recovery path. In a carrier network, rollback may affect neighboring services or require supplier support.

Begin with task-limited read access. Put write tools behind a broker or equivalent target control, but keep network-state changes in the normal change process. Test low-impact ticket updates within bounded fields; expand only after the stop path, recovery and service fallback have been verified with responsible teams and suppliers.

A broker centralizes access rules and audit but becomes another dependency. Fail-open preserves the workflow while bypassing the control; fail-closed protects writes but may stop monitoring if reads share the broker. For NOC use, separate alarm reads where possible and fail closed on actions. If the paths cannot be separated, define the degraded service view and emergency authority; manual handling may add workload and delay. Test broker loss with a new request, an active session and a queued action. Verify target denial, attribution, independent visibility and fallback. If the target result is unobservable, treat the action path as unverified and keep high-impact actions outside it.

Ticket and vendor-case tools can influence triage, escalation or restoration even when another person or system performs the next step. Map the downstream action, affected service and receiving owner.

For the NOC assistant, trace the sequence from identity through connector to operational hand-off. Individually modest permissions can combine into a consequential path; preserve the source evidence across each hop.

| Path segment | Established facts | Required check and owner |
|---|---|---|
| Agent to identity | The assistant used a broader service account. | IAM/platform confirms principal, owner, scope, duration and sharing; workflow owner confirms need. |
| Identity to data/tools | The account read neighboring-domain data and opened vendor cases. | Connector/platform traces APIs, fields, supplier roles and targets; data owner confirms need. |
| Output to operations | The assistant proposed a visibility-reducing change; completion is not established. | NOC/change owner confirms draft status and where approval is enforced. |
| Containment | Reach is known; revocation behavior is not. | IAM/platform tests session revocation and target denial; NOC/service assurance verifies attribution and fallback. |

Prompts and product settings do not authorize actions unless the connector or target enforces them. Normal change approval governs only actions that pass through that route. If a supplier hop is unobservable, mark reach unknown and restrict use; route the remaining service decision through Chapter 5.

Vendor cases create both a data and workflow boundary. Fields and attachments may include alarms, topology or service-impact details. The NOC assistant can prepare a draft, submit after review or submit automatically. Drafts preserve a review step but keep NOC effort in the path; automatic submission saves a step but may send details or trigger supplier work before an operator sees them. Approval is meaningful only when the reviewer sees the exact payload, recipient and downstream action.

Keep submission at human-reviewed draft until payload, recipient, supplier roles, retention and downstream workflow are visible. Measure NOC review effort and service delay; do not assume either is negligible. In an approved non-customer test, verify the payload, destination, target principal, submission and revocation. If the path cannot be observed, keep submission manual or remove sensitive fields. Automate only when the operator can enforce those fields, verify supplier access and retention, and show that the faster hand-off justifies the remaining dependency. Network changes stay in the normal change process.

A December 2025 guide from CISA, the Australian Signals Directorate’s Australian Cyber Security Centre (ASD ACSC), and partner agencies addresses OT systems, not every telco network domain. It recommends integrating AI into existing security frameworks, keeping human oversight for critical OT operations, and providing fail-safe mechanisms that revert to traditional automation or manual operation. Operators should establish which of their systems fall within that scope.

## Suppliers can introduce a new path without a new project

AI can arrive through a service-desk upgrade, cloud feature, network-management platform, customer-care system or supplier portal, without a new project or security review. The product name may stay the same while data flows, model provider or tools change. Inventory supplier features, internal experiments, agent runtimes, connectors, identities and data stores, not only centrally purchased products.

The supplier diagnostic feature from Chapter 4 is the attack-surface example: a routine update enabled a feature that reads topology and proposes actions. Its identity, target authority and independent disablement are unknown; “diagnostic” does not mean read-only. Chapter 4 handles the decision and assurance plan.

Supplier assurance starts with access, prompt/output processing, sub-processors, logging, retention and change notices. The operator/provider boundary must be clear. ACSC recommends a shared-responsibility register separating operator controls, provider capabilities the operator configures and provider outcomes it verifies. Its cross-sector guidance also calls for inventorying services, agents, connectors and unsanctioned applications, and checking prompt/output retention, customer-data training use and processing location; it is not a telecom-specific requirement.

The Telecom Regulatory Authority of India (TRAI) published draft responsible-AI guidelines for telecom consultation on 30 October 2026. The proposal calls for an inventory of active, inactive and decommissioned AI systems by source, purpose and risk class, and due diligence before third-party AI is acquired or used. The draft is not binding. It is a practical prompt to ask what systems are in use, who supplies them and which services they affect.

Testing environments add paths to the inventory. The ACSC’s 12 November 2026 guidance recommends a purpose-built harness isolated from production, corporate and management networks. It calls for limited credentials and network access, verified tool controls, real-time monitoring, protected logs and authorized staff able to stop the test. This guidance covers testing, not production; inventory the harness, tools and credentials as access paths.

## Assurance follows the action path

Inventory maps potential reach; assurance tests an actual path. For a consequential workflow, follow the identity through sources and tools to the target and downstream action. Test permissions, target enforcement, revocation, logs, NOC visibility and fallback.

A connector log may show a request without proving the target acted or denied it. If the target result is invisible, do not claim end-to-end attribution or containment. Keep actions on a target-visible route or add an operator-controlled gateway; if neither is feasible without harming continuity, keep the action manual and route the service-risk decision through Chapter 5.

## Establish visibility and ownership

Do not wait for a perfect AI inventory. Start with high-consequence paths into network operations, OSS/BSS, customer data and suppliers: who owns each, which identity it uses, what it can retrieve or trigger, and how access can be stopped.

That is the attack surface. Chapter 3 turns to a different question: can the operator recognize a threat, decide and act quickly enough to keep service running?
