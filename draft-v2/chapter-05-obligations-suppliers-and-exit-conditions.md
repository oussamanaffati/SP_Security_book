# Chapter 5: Obligations, Suppliers and Exit Conditions

**Illustrative scenario: a supplier diagnostic feature enabled by a routine update.** It reads topology and proposes actions. The situation does not establish direct execution, its identity, or whether it can be disabled independently.

The first decision is therefore wider than “enable or reject the feature.” The operator needs to know which duties apply, which supplier paths matter to the service, and what remains possible if the feature or its provider is unavailable. A data region is only one part of that picture.

## Start with the obligation that applies

A multinational operator rarely has one cybersecurity rulebook. Requirements can depend on the country, the legal entity, the service, the data being processed and the operator’s role. An obligation map should identify those boundaries before a supplier feature is expanded or a service path is moved across them.

Several European instruments can touch the same workflow, but they answer different questions. The European Union’s NIS2 Directive (Directive (EU) 2022/2555) includes in-scope providers of public electronic communications networks and services in its cybersecurity framework; national implementation and entity status still matter. The General Data Protection Regulation (GDPR) applies to personal-data processing within its territorial and material scope. Its records-of-processing and security duties do not, by themselves, establish a universal requirement to retain every prompt and response.

The European Union’s Artificial Intelligence Act (AI Act) is phased and role-dependent. One relevant high-risk category covers systems intended to be safety components in the management or operation of critical digital infrastructure. That is narrower than treating every AI system used by a telecom operator as high-risk. Intended purpose and the Act’s criteria need to be checked for the particular system and role.

The United Kingdom (UK) illustrates why a legal rule and its implementation guide must stay distinct. The Electronic Communications (Security Measures) Regulations 2022 have been in force since 1 October 2022. They impose proportionate security duties on in-scope providers of public electronic communications networks and services, except micro-entities.

The Telecommunications Security Code of Practice v1.1 was issued on 14 July 2026 and gives technical guidance to Tier 1 and Tier 2 providers. It is guidance, not a statutory instrument or the only compliance route. Tier 3 providers are not expected to follow its measures, but remain subject to statutory duties unless they are micro-entities.

In the United States, one relevant federal statute is the Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA). The Cybersecurity and Infrastructure Security Agency (CISA) says the final CIRCIA rule is still in progress as of 16 November 2026. Covered-entity reporting will not begin until that rule takes effect; voluntary reporting is encouraged in the meantime. Check the final rule for covered-entity scope; other federal, state, sector or contractual reporting duties may apply now.

| Instrument | What it establishes | What still needs local review |
|---|---|---|
| NIS2 | An EU cybersecurity framework that includes in-scope public electronic communications providers. | National transposition, entity status, service scope and applicable reporting triggers. |
| GDPR | Processing records and risk-appropriate security when GDPR applies to the processing. | Controller/processor roles, the actual data path, lawful processing and retention. |
| AI Act | A phased set of duties tied to system purpose, classification and role. | Whether this system meets a statutory category and which duties apply at the relevant date. |
| UK telecom security rules | Binding, proportionate telecom-security duties for in-scope public providers; the Code gives detailed guidance. | Provider status, territory, turnover tier and any exemption. |
| CIRCIA | Provides for mandatory reporting by covered entities under a final rule that is not yet effective as of 16 November 2026. | Future covered-entity scope and any separate reporting duties that already apply. |

This table is a starting map, not legal advice. Use counsel to confirm the current text, transposition and applicability for each service and entity. Do not copy a deadline from one market into another, and do not treat a consultation, government code, industry standard and statute as interchangeable.

Keep the record operational. Name the entity and service, the applicable rule and the trigger. Record who owns the decision and notification, what evidence to preserve, and the last date it was checked. If a supplier changes processing location, service role or support path, the map may need review. The legal answer should follow the deployed workflow, not the product’s category label.

## Follow the dependency beyond the data region

A supplier dependency is not limited to where prompts are stored. The service may rely on a model provider, a cloud platform, a connector, an identity service, a telemetry or logging store, supplier support, an update channel and a management API. A provider may host the model while the operator controls the target identity; another service may control the connector but not the network action. The contracts and technical paths should describe the same arrangement.

“Private” or “sovereign” can be useful labels, but they answer only part of the question. Who administers the service? Who can change the model or connector? Which subcontractors process data? Can the operator keep working during an outage? Location matters for jurisdiction and data handling, but it does not prove that the service can be controlled, observed or replaced.

When a supplier supports a consequential workflow, bring together Procurement, Legal, Security, Network Engineering, the service owner and platform team. Each should establish a different part of the dependency.

| Dependency | Evidence to obtain | Decision it changes |
|---|---|---|
| Identity and support | Named supplier principals, access scope, approval route, session duration and revocation behavior. | Whether the supplier can reach a target, and how support can continue after a credential is restricted. |
| Data and records | Processing locations, subprocessors, retention, training use, logs, backups and deletion evidence. | Whether the data route is allowed and whether incident review can reconstruct the relevant path. |
| Model, connector and updates | Version/change notice, feature separation, release testing, rollback and responsibility for downstream behavior. | Whether a routine update can alter access or service behavior without a new review. |
| Availability and recovery | Service dependencies, outage notification, support coverage, manual mode and restoration conditions. | What the operator can safely continue when the external service is unavailable. |
| Portability and exit | Exportable configuration and records, replacement path, credential closure, deletion process and transition assistance. | Whether the operator can leave or change the supplier without losing service control or evidence. |

These are procurement questions, not claims that every supplier will accept every term. Seek the strongest practical notice, audit, evidence and transition rights while the operator still has leverage. Where a contract cannot guarantee a technical outcome, record that limit and test the operator-controlled part. A clause promising deletion does not show that a copy was removed; a statement that access is supervised does not prove the target sees a distinct, revocable identity.

The supplier diagnostic situation makes the distinction concrete. Its presence is established, and the scenario says it reads topology and proposes actions. Direct execution is not established. The operator should not describe it as a network-changing agent. The absence of evidence for direct execution does not prove that its data path, disablement or downstream effect is safe.

Ask the supplier to identify the feature’s runtime identity, destinations, logs and independent disablement. Compare those statements with the operator’s deployed records. Chapter 4 covers the technical test. Here the question is whether the release and contract leave the operator able to make that test and act on its result.

## Buy an exit that preserves the service

“Exit” is often treated as a contract clause. For a network operator, it is first a service-continuity condition. Can the NOC still see the alarms? Can Engineering recover the last known configuration? Can the operator revoke supplier access without removing its only support path? Can a trained team carry out the task manually while a replacement is assessed?

The answer may be different for the AI feature and the surrounding management platform. Disabling a feature may leave the platform and supplier support in place. Ending the platform contract may remove an entire operational view. A service may also depend on the supplier for updates, integration knowledge or access to a supported fix. Those are separate decisions; one switch rarely proves a complete exit.

Set an exit trigger before a failure forces the choice. Triggers may include a material change to supplier access or data use, missing required logs, a failed boundary test, repeated outages, or a change in legal applicability. End of support for the deployed version is another trigger. Name who verifies the trigger, who may pause new actions, who checks service impact and who can accept temporary degraded operation.

Then define what “leave” means for that service. It may mean disable the AI feature while retaining the platform; block a connector while preserving independent alarm reads; move to an operator-controlled tool; or return to a manual process. For each route, list the configuration, service records and audit data to export. Define which identities and sessions must close, and which data to delete or retain under an approved process. If these are only supplier assurances, say so. Do not report the exit as tested until the operator has exercised the relevant path.

An alternative provider is not automatically a fallback. It may use the same cloud, identity provider, network route, telemetry store or subcontractor. A manual procedure is not a fallback if the NOC cannot see authoritative state or if the trained staff are not available on the shifts that need it. Map common dependencies and rehearse the service mode that remains when one of them fails.

A complete exit test may be unsafe in production. That is a reason to use a lower-risk test, a controlled maintenance window or a documented simulation with its limitations, not a reason to claim the exit is ready. If the operator cannot test a live cutover, verify export and credential closure in a controlled environment, rehearse the manual service route, and record which live dependencies remain unproven. Keep broader authority disabled until the untested step is safe to exercise.

## Proceed within a boundary, not on hope

A read-only summary over an approved, task-limited data set may proceed when the effective identity is attributable, the supplier route is known and the target enforces the read boundary. The operator must be able to pause or isolate the feature without losing the service’s required support path. Logs must identify the call, and the NOC must retain an independent service view. The operator should record what remains unknown and what change would reopen the decision.

If the operator cannot identify the data destination, the effective identity, the applicable legal role or the independent service fallback, do not expand the feature’s access. Narrow the data, keep the output as a draft, or hold the feature off while the platform’s required functions remain available. If the feature cannot be separated from a product release, compare a supported pause or rollback with the service and security consequence of delaying that release. Do not assume either that the AI feature can be disabled or that the whole platform must be withdrawn.

For this supplier-feature situation, require a clear release and support path. Keep write authority outside the feature unless a target-enforced boundary is proven. Preserve the service view during investigation or rollback. Revisit the choice when the identity, target path, fallback and support arrangement are evidenced.

A legal duty sets a floor and a supplier contract sets expectations. Neither, by itself, shows who can disable a connector at 02:00, whether existing sessions terminate, or whether the NOC can still manage the service afterward. That is the operator’s responsibility to map, test and fund.

Chapter 6 uses those service and supplier constraints to choose a small set of funded priorities, rather than treating every control as equally urgent.

<!-- Non-reader-facing claim/source map. Exact source texts, evidence classes and limits are in research/claim-ledger.md, research/research-map.md and research/draft-v2-source-map.md.
P1.S1-S2, P15.S2-S3, P25: Author-supplied supplier-diagnostic composite; a routine update enables a feature that reads topology and proposes actions; direct execution, runtime identity, target authority and independent disablement are not established. Illustrative only.
P4.S2: T8 (NIS2 Directive; in-scope EU public electronic communications providers; national implementation/entity status still matter). P4.S3-S4: T9 (GDPR Articles 30/32; processing records and risk-appropriate security within scope; no universal prompt-retention claim).
P5: T10 (EU Artificial Intelligence Act; phased, purpose/role-specific criteria; Annex III critical-digital-infrastructure category is limited to intended safety-component use, not all telecom AI).
P6: T22 / LAW-1 (UK Electronic Communications (Security Measures) Regulations 2022; statutory duties, in-scope public providers and micro-entity exemption).
P7: T22 / LAW-2 (UK Telecommunications Security Code of Practice v1.1; official guidance, Tier 1/2 scope, Tier 3 qualification and legal relevance).
P8: T6 / LAW-3 (CISA CIRCIA status page, directly read 16 Nov 2026; final rule still in progress; mandatory reporting does not start until effective; voluntary reports encouraged).
Table 1: T8, T9, T10, T22/LAW-1, T22/LAW-2 and T6/LAW-3, with the same scope limits above. Table 2: author-derived supplier dependency/evidence questions, not claims about a specific contract.
P2-P3, P9-P14, P15.S1/S4-S5, P16-P24, P26-P27: Author analysis and recommendations on jurisdiction mapping, supplier dependency, contracting, exit, bounded use and service continuity; no unverified operator practice, contract term, cost, or exit outcome asserted.
-->