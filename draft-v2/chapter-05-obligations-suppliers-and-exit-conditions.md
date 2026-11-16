# Chapter 5: Obligations, Suppliers and Exit Conditions

**Illustrative scenario: a supplier diagnostic feature enabled by a routine update.** It reads topology and proposes actions. The example does not tell us whether it can execute them, which identity it uses or whether the operator can disable it on its own.

So the first decision is not simply whether to enable the feature. The operator needs to know which duties apply, how the supplier connects to the service and what the team can still do if the feature or provider is unavailable. Data location is only one part of the picture.

## Start with the obligation that applies

An operator working across borders is unlikely to have one rulebook. Requirements depend on the country, legal entity, service, data and the operator’s role. Map those boundaries before expanding a supplier feature or moving a service path across them.

Several European laws may apply to one workflow, but they answer different questions. The European Union’s NIS2 Directive (Directive (EU) 2022/2555) includes in-scope providers of public electronic communications networks and services in its cybersecurity framework. National implementation and the entity’s status still matter. The General Data Protection Regulation (GDPR) applies to personal-data processing within its territorial and material scope. Its record-keeping and security duties do not, by themselves, require every prompt and response to be retained.

The European Union’s Artificial Intelligence Act (AI Act) is being phased in, and its duties depend on the system and the operator’s role. One relevant high-risk category covers systems intended as safety components in managing or operating critical digital infrastructure. That does not make every AI system used by a telecom operator high-risk. Check the system’s intended purpose against the Act’s criteria.

The United Kingdom (UK) shows why a binding rule must be distinguished from its implementation guide. The Electronic Communications (Security Measures) Regulations 2022 have been in force since 1 October 2022. They impose proportionate security duties on in-scope providers of public electronic communications networks and services, except micro-entities.

Issued on 14 July 2026, the Telecommunications Security Code of Practice v1.1 gives technical guidance to Tier 1 and Tier 2 providers. It is not a statutory instrument or the only route to compliance. Tier 3 providers are not expected to follow its measures, but remain subject to statutory duties unless they are micro-entities.

In the United States, one relevant federal statute is the Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA). As of 16 November 2026, the Cybersecurity and Infrastructure Security Agency (CISA) says its final rule is still in progress. Mandatory reporting by covered entities will begin only when the rule takes effect; CISA encourages voluntary reporting in the meantime. The final rule will define which entities are covered. Other federal, state, sector or contractual duties may apply now.

| Instrument | What it establishes | What still needs local review |
|---|---|---|
| NIS2 | An EU cybersecurity framework that includes in-scope public electronic communications providers. | National transposition, entity status, service scope and applicable reporting triggers. |
| GDPR | Processing records and risk-appropriate security when GDPR applies to the processing. | Controller/processor roles, the actual data path, lawful processing and retention. |
| AI Act | A phased set of duties tied to system purpose, classification and role. | Whether this system meets a statutory category and which duties apply at the relevant date. |
| UK telecom security rules | Binding, proportionate telecom-security duties for in-scope public providers; the Code gives detailed guidance. | Provider status, territory, turnover tier and any exemption. |
| CIRCIA | Provides for mandatory reporting by covered entities under a final rule that is not yet effective as of 16 November 2026. | Future covered-entity scope and any separate reporting duties that already apply. |

Use the table as a starting map, not legal advice. Ask counsel to confirm the current text, national implementation and applicability to each service and entity. A deadline in one market does not automatically apply in another. Nor are a consultation, government code, industry standard and statute interchangeable.

Make the record useful to the people who run the service. Name the entity, service, applicable rule and reporting trigger. Note who owns the decision and notification, what evidence to preserve and when the entry was last checked. Revisit it if a supplier changes processing location, service role or support path. The legal answer follows the deployed workflow, not the product label.

## Follow the dependency beyond the data region

Supplier dependency goes beyond where prompts are stored. A workflow may rely on a model provider, cloud platform, connector, identity service, logging store, support team, update channel or management API. One provider may host the model while the operator controls the target identity; another may control the connector but not the network action. The contract should match the way the service actually works.

“Private” and “sovereign” can be useful labels, but they do not settle the practical questions. Who administers the service or can change the model and connector? Which subcontractors process data? Can the operator keep working through an outage? Location matters for jurisdiction and data handling; it does not show that the service can be controlled, observed or replaced.

If a supplier supports a consequential workflow, bring Procurement, Legal, Security, Network Engineering, the service owner and platform team into the same discussion. Each sees a different part of the dependency.

| Dependency | Evidence to obtain | Decision it changes |
|---|---|---|
| Identity and support | Named supplier principals, access scope, approval route, session duration and revocation behavior. | Whether the supplier can reach a target, and how support can continue after a credential is restricted. |
| Data and records | Processing locations, subprocessors, retention, training use, logs, backups and deletion evidence. | Whether the data route is allowed and whether incident review can reconstruct the relevant path. |
| Model, connector and updates | Version/change notice, feature separation, release testing, rollback and responsibility for downstream behavior. | Whether a routine update can alter access or service behavior without a new review. |
| Availability and recovery | Service dependencies, outage notification, support coverage, manual mode and restoration conditions. | What the operator can safely continue when the external service is unavailable. |
| Portability and exit | Exportable configuration and records, replacement path, credential closure, deletion process and transition assistance. | Whether the operator can leave or change the supplier without losing service control or evidence. |

These are questions to negotiate, not terms every supplier will accept. Seek practical rights to notice, audit, evidence and transition while the operator still has leverage. A contract cannot guarantee every technical outcome, so record the limits and test what the operator controls. A promise to delete data does not show that a copy is gone. “Supervised access” does not prove that the target sees a separate, revocable identity.

Return to the diagnostic feature. The example establishes that it reads topology and proposes actions, but not that it executes them. Do not describe it as a network-changing agent. At the same time, lack of evidence for direct execution does not make its data path, disablement or downstream effects safe.

Ask the supplier which identity the feature uses, where it connects, what it logs and whether it can be disabled separately. Check those answers against the deployed service. Chapter 4 explains how to test the path; here, the question is whether the release and contract let the operator run that test and act on the result.

## Buy an exit that preserves the service

Exit is often treated as a contract clause. For an operator, it is first about keeping the service running: the NOC must still see alarms, Engineering must be able to recover the last known configuration, and supplier access must be revocable without losing the only support path. The operator also needs a trained team to do the work manually while it assesses a replacement.

The AI feature and its management platform may need different exit plans. Disabling the feature may leave the platform and supplier support intact. Ending the platform contract could remove an entire operational view. The service may also depend on the supplier for updates, integration knowledge or a supported fix. These are separate decisions; one switch rarely completes the exit.

Set the exit trigger before a failure forces the decision. It might be a material change in supplier access or data use, missing logs, a failed boundary test, repeated outages, a legal change or the end of support for the deployed version. Decide who verifies the trigger, who can pause new actions, who checks service impact and who may accept temporary degraded operation.

Define what leaving means for the service. The operator might disable the AI feature but keep the platform, block a connector while preserving independent alarm reads, move to its own tool or return to a manual process. For each option, say what configuration, service records and audit data must be exported, which identities and sessions must be closed, and what data must be deleted or retained. Separate contractual promises from what has actually been tested. Do not call the exit tested until the operator has exercised the relevant path.

An alternative provider is not automatically a fallback. It may use the same cloud, identity provider, network route, telemetry store or subcontractor. A manual procedure is not a fallback if the NOC cannot see authoritative state or if the trained staff are not available on the shifts that need it. Map common dependencies and rehearse the service mode that remains when one of them fails.

A full exit test may be unsafe in production. Use a lower-risk test, a controlled maintenance window or a documented simulation, and state what it cannot show. If a live cutover is not safe to test, verify export and credential closure in a controlled environment, rehearse the manual route and record which live dependencies remain unproven. Keep broader authority disabled until the untested step can be exercised safely.

## Decide whether the feature is ready

Start with a read-only summary. It still needs approved, task-limited data, an attributable identity, a known supplier route and a read limit enforced by the target. The operator must be able to pause the feature without losing required support. Logs should identify each call, and the NOC should keep an independent service view. Record what is still unknown and what change would reopen the decision.

If the data destination, effective identity, legal role or independent fallback is unknown, do not expand access. Narrow the data, keep the output as a draft or hold the feature while preserving the platform functions the service needs. If the feature cannot be separated from a product release, weigh a supported pause or rollback against the service and security cost of delaying it. Do not assume that the feature can be disabled on its own—or that the whole platform must be withdrawn.

For this feature, require a clear release and support path. Keep write access outside it unless tests show that the target enforces the boundary. Preserve the service view during investigation or rollback. Revisit the decision when the identity, target path, fallback and support arrangements are clear.

A legal duty sets a floor and a supplier contract sets expectations. Neither, by itself, shows who can disable a connector at 02:00, whether existing sessions terminate, or whether the NOC can still manage the service afterward. That is the operator’s responsibility to map, test and fund.

These obligations and supplier dependencies narrow the choices. Chapter 6 asks where to spend limited capacity over the next year.

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