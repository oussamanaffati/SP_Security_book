# Service Provider Security in the AI Era

## A Practical Guide to AI, Agents, and Service Continuity for Telecom CISOs and CTOs

## Contents

- [Introduction](#introduction)
- [Chapter 1: What Is Actually Deployed?](#chapter-1-what-is-actually-deployed)
- [Chapter 2: Telecom Threats Without the AI Hype](#chapter-2-telecom-threats-without-the-ai-hype)
- [Chapter 3: Follow Authority to the Network Target](#chapter-3-follow-authority-to-the-network-target)
- [Chapter 4: Prove Safe Authority and Service-Safe Response](#chapter-4-prove-safe-authority-and-service-safe-response)
- [Chapter 5: Obligations, Suppliers and Exit Conditions](#chapter-5-obligations-suppliers-and-exit-conditions)
- [Chapter 6: The Next 12 Months: A Defensible Operator Agenda](#chapter-6-the-next-12-months-a-defensible-operator-agenda)

# Introduction

When leadership asks its chief information security officer (CISO) to pause a workflow that uses artificial intelligence (AI), the request may be sensible. The network team may still need the same data feed, supplier console or alert path to see what is happening to a service. Leaving the workflow in place without a proven boundary creates another risk. A pause can reduce one exposure and remove visibility or support needed to operate the service. That is the practical tension at the centre of this book.

The answer is not to ban every model or to trust a supplier’s assurance. It is to understand the whole workflow. What data can it read? Which identity and connector does it use? What can it recommend, draft or change? Where does the target enforce permission? What remains visible when the workflow is stopped, and who can restore the service?

That is a service-provider security question, not only an AI question. An operator’s decision sits inside a service with dependencies, operating teams, suppliers, jurisdictions and supported change paths. A control that looks simple in a product demonstration may be difficult to remove from a live operating process. A production label does not tell a CISO what a system can change, how widely it is used, or whether it has improved security.

This book does not claim that autonomous agents are the leading cause of telecom incidents. The sources reviewed here report different deployment stages and outcomes. They establish serious telecom targeting, but do not establish AI use in the incidents discussed. Those limits matter: productivity is not proof of security effectiveness, a threat report is not proof of local exposure, and a test supports only the path and conditions it exercised.

The chapters follow the decisions a CISO or chief technology officer (CTO) needs to make. Chapter 1 separates deployment stage, authority and outcome. Chapter 2 examines telecom intrusion evidence without assuming an AI cause. Chapter 3 follows identity, data, tools and permission to the network target. Chapter 4 asks what has been tested and whether the operator can contain and recover without losing the service view. Chapter 5 connects legal duties to supplier dependencies and exit. Chapter 6 turns those decisions into a small investment agenda for the next twelve months.

Chapters 3 and 4 work through two illustrative operational situations in detail. Each is introduced where it matters, and any added educational assumption is separated from the situation’s stated facts. Chapter 5 uses a shorter supplier-feature example. These situations are not reported incidents or successful tests. They help make the choices visible without pretending that every operator has the same systems or constraints.

Read the book in order if you are building a common risk view. Each chapter uses decisions established before it. If you are preparing a particular decision, start with the relevant chapter, then return to Chapter 6 to select priorities, assign ownership, record the evidence and capacity required, and decide what would change the recommendation.

The aim is practical. A telecom CISO should finish able to distinguish a live deployment from a demonstration or plan; trace what a workflow can read and change; test service-safe containment and recovery; identify consequential supplier and jurisdiction dependencies; and select three or four priorities to explain to the chief executive officer (CEO) or board. The final decision should say what is known, what remains uncertain, who owns the service and the risk, and what evidence would change the recommendation.

# Chapter 1: What Is Actually Deployed?

Deutsche Telekom’s February 2026 release says its Radio Access Network (RAN) Guardian Agent is live in production in Germany. The company reports that it autonomously triggered more than 100 remediation actions in its first month, during Christmas-market events. It also says the time to manage major events fell from hours to around a minute.

That is a useful, specific claim: an operator names a live workflow, a place, an action count and a time comparison. The release does not give the event sample, measurement method, success or rollback rate. Treat the figures as company-reported operating results, not proof of network-wide autonomy, better service or lower security risk.

## Look at the task, not the label

One NZ says its Network Concierge gathers network performance data, alarms and past incidents, then gives a customer-service representative a summary and suggested next step. The operator reports an 80 percent reduction in analysis time. That is a claim about analysis, not restoration time. The release gives no case count, baseline or answer-quality measure, so the figure cannot tell us whether customers got service restored sooner.

The same release describes a separate generator-placement tool used during severe weather to help engineers decide where to send mobile generators. It is a different workflow from complaint analysis, and it is not evidence that an AI system controlled the network or restored service.

Orange France says Mon Assistant IA was deployed to 3,000 sales advisers and supported nearly one million conversations per month. The adviser remains in control and validates proposed responses. Those figures describe reported reach and activity. They do not measure time saved, answer quality or customer outcomes.

SK Telecom’s AI-RAN Parameter Recommender was applied to its commercial network and systematically validated. It recommends base-station parameters; the same release says real-time application was still being developed. Commercial-network validation is not autonomous production control.

These examples answer different questions. Deployment describes where a system is used. Activity counts actions, users or conversations. Productivity measures a task against a credible baseline, including review and rework. Service quality needs a measure of correctness or customer impact. Security effectiveness requires evidence that a control or threat outcome changed. Return on investment (ROI) compares costs and benefits on a common basis. A result in one category does not prove a result in another.

## Ask what “production” means here

“Production” matters, but it is not a measure of scope or effectiveness. An operator may use a system live in one workflow while its footprint, authority and failure behavior remain unclear. Keep the stage and the action separate: a system may gather information, recommend, prepare a change for approval or submit an action itself. Ask which system enforces the action and what service it could affect.

For a deployment claim, write down five things: the workflow and service; its stage and footprint; the identity and actions it can use; who is making the claim; and what the metric counts. Ask for a denominator, baseline, period and comparison method when the result depends on measurement. If a material detail is missing, mark it unknown. Do not turn a plan into a live deployment or an activity count into an outcome.

A production label is a starting point for that conversation. It tells the CISO to ask for the path, the permission and the result—not to assume them.

Chapter 1 gives us a way to judge claims. Chapter 2 applies the same discipline to threat reporting: serious telecom intrusions deserve action, but an AI label should not outrun what the source establishes.

# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort against intrusion activity targeting the telecommunications sector. It said all four major operators had been targeted. The operation lasted more than eleven months and involved over 100 cyber defenders.

Those figures describe the scale of the defensive operation, not the number of threats stopped or service impact avoided. The published account does not attribute the activity to AI. It supports a serious assessment of telecom targeting and organized response; it does not support a claim about the attackers’ AI use.

A United States disclosure gives a different view of the threat. In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported a compromise of multiple telecommunications companies’ networks. They attributed the activity to actors affiliated with the People’s Republic of China (PRC). The agencies said the access enabled theft of customer call-record data, access to private communications of a limited number of individuals, primarily people involved in government or political activity, and copying certain information subject to United States law-enforcement requests. An October statement from the FBI and CISA had confirmed an investigation into unauthorized access to commercial telecom infrastructure and assistance to affected companies and potential victims. These disclosures do not establish AI use in the named activity. Their public scope also does not provide a complete forensic timeline or show how long access went undetected.

## Count the right thing

The European Union Agency for Cybersecurity (ENISA) published an open-source intelligence (OSINT) overview counting 30 cybersecurity incidents. A separate ENISA annual summary contained 188 significant-incident reports submitted by national authorities. That reporting set includes service outages and system failures as well as malicious actions, human error and natural phenomena. The two collections have different inputs and definitions. They are neither a combined count nor comparable rates.

The OSINT overview shows publicly reported cyber activity; it is not a census of all telecom intrusions. The authority-submitted reports describe continuity-impact events under a reporting framework; they are not a catalogue of hostile campaigns. The figures answer different questions. Keep that distinction when briefing executives, and do not use either number to estimate an operator’s local exposure.

## Prepare for the path, not the headline

An AI label should change the assessment only when evidence ties AI to a step that matters. Did a named actor use an AI service somewhere in a broader campaign, or did investigators connect that use to this specific telecom intrusion? Did it change the task, scale, timing, access or consequence? A report that documents general tool use does not establish that the tool caused a particular intrusion or changed its outcome.

That distinction need not delay practical work. Map the management, identity, supplier and remote-support paths that can reach sensitive network functions. Know which customer, signaling, location or operational records matter if read or altered. Make sure responders can obtain authoritative service state during an investigation, and identify which changes can preserve evidence without creating a second outage. Public disclosures rarely answer those local questions.

Attach the AI question to a concrete step in the operator’s own workflow. If an external model or agent is called, can the logs connect the requesting principal and input to the destination, tool call and resulting action? Would evidence of AI use change a detection or response decision? If not, the label may be descriptive rather than operationally useful.

Do not wait for proof of AI use before correcting a known exposure. A credential that reaches a management interface, an unobserved supplier path or an exposed system with a supported fix matters on its own. Attribution can refine the investigation; it does not remove the operator’s responsibility for a path already at risk.

When the next briefing calls an event “AI-enabled,” ask what happened to the telecom target, what evidence connects AI to this operation, what that use changed, and what action remains necessary even if the attribution is withdrawn. If the intrusion is clear but the AI link is not, brief it as a telecom intrusion and state the attribution gap.

Knowing which threats are reported still leaves the operator with a local question: which identity, connector and target can turn access into service impact? Chapter 3 follows that path.

# Chapter 3: Follow Authority to the Network Target

A radio application does not need to call itself an AI agent to create a network-control risk. A 2024 peer-reviewed study built an experimental Open Radio Access Network (O-RAN) H-Release environment and found missing access-control permissions for xApps, applications deployed on an O-RAN controller. The researchers demonstrated three attacks through application programming interfaces (APIs) and the E2 interface, including attacks that disrupted radio access network (RAN) components. This was a lab result, not evidence that the same path exists in a carrier’s production network. Its value is the question it leaves with the operator: which identity can reach which target, through which interface, and what can that target do?

These applications were not automatically AI agents, and the study did not test a large language model (LLM)-based agent. The weakness was not a model making a poor recommendation. It was inadequate control over what an application could reach through network-management interfaces. The same distinction matters when a language model is added to an operational workflow. The model may reason about a change. A runtime calls a tool. The tool uses a credential. An API accepts or rejects the request. The target applies its own permissions and changes—or does not change—the network.

The authority is in that chain, not in the product name.

## Follow one identity to its target

**Illustrative scenario: a shared account across edge and core.** In this supplied situation, one service account can reach edge nodes and parts of the core. Remediation depends on supplier configuration and a safe maintenance window. The situation does not establish that an AI agent used the account, which commands it accepted, or whether the target supports separate identities.

For this walkthrough, add two educational assumptions. Assume a maintenance assistant reads edge alarms and configuration, then prepares a supplier-supported change through an operator connector. The connector authenticates with the shared account. The intended job is limited to the edge service. The same account can also reach part of the core. No local test has yet shown that the target will distinguish an edge request from a core request. These added details make the decision concrete; they are not facts about an operator or part of the supplied situation.

Now trace the call. The assistant reads alarm and configuration data. Its runtime sends a request to the maintenance connector. The connector presents the service account to a target API. The target sees that account, not necessarily the assistant, the person who requested the work, or the edge-only purpose. If the API accepts a core operation under the same identity, the account’s effective authority is broader than the assistant’s task. A human approval screen does not narrow that authority unless the approval is bound to the exact target and operation, and the target enforces it.

This is why “human in the loop” is not a permission model. It describes a role in a process. It does not tell us whether approval happens before execution, whether the reviewer sees the exact request, which credentials perform it, or whether the target enforces the intended limit.

The first choice is to keep using the account as it is. That avoids a rushed migration and preserves the supplier’s current support route. It also leaves edge and core reach joined under one principal. If something goes wrong, logs may show that the service account acted without showing which workflow or person initiated the request. Under the educational assumption, giving an agent this credential would also let its task inherit reach it does not need. I would not do that.

A gateway can be an interim boundary. It helps only if every route to the target passes through it, the target accepts no bypass route, and the gateway can deny core operations while allowing the required edge work. The operator must test what happens when the gateway fails. Fail-closed behavior can interrupt support; fail-open behavior can restore the broad path. A diagram showing the gateway is not proof that it controls the target.

Separate target-native identities are the better end state when the platform and supplier support them. An edge identity can then have edge permissions, while a distinct core identity is issued only to the workflow that needs it. Migration takes engineering and supplier time. Running old and new identities in parallel makes it easier to find missing permissions, but extends the period of broad access. Disabling the old account first reduces overlap but may interrupt monitoring or supplier support. A staged move uses more change effort, but lets the operator verify each workflow before retiring the shared principal.

Under the stated assumptions, my recommendation is to keep the assistant out of the write path and plan a supplier-supported move to separate target identities. Do not count an untested gateway as a control. The CISO should set the condition: no agent write access through the shared principal until its scope is proven. Network Engineering and the supplier should confirm which target-native identities are supported and schedule a safe migration. The service executive owns any period in which current support must remain broad. Keep the existing support path only for its currently authorized purpose while the service owner and supplier establish the transition; do not broaden it to the assistant. If a gateway is proposed as temporary protection, first test allowed edge requests, denied core requests, alternate routes, logs, revocation and behavior on gateway loss in a safe environment. Keep an independent emergency route for the service, and verify that it does not simply recreate the same broad access.

The recommendation changes if the target cannot support separate identities, if a tested gateway blocks every alternate route without breaking required support, or if the maintenance path has different service dependencies than assumed. It also changes if local logs show that the account can already perform a sensitive core action. That finding calls for immediate scope reduction or an authorized service decision, not a longer inventory project. The facts that matter are the target’s actual permissions, the routes that reach it, and the service consequences of each restriction.

## From influence to permission

An agent can be influenced by data it reads without that data having a credential. A tool can hold a credential without every model output being executable. A target can reject a request even when a model and connector agree on what should happen. Keep those boundaries separate.

The peer-reviewed AgentDojo benchmark helps explain the first boundary. In simulated tool environments, researchers tested how instructions hidden in third-party data could influence a tool-using agent. The work demonstrates an indirect prompt-injection mechanism: data returned by a tool can be interpreted as instructions and can redirect later tool use. It does not test telecom systems, estimate how often the mechanism occurs in operators, or show that an injection changes network state by itself.

For an operator, the point is not to decide whether retrieved content is “trusted” in the abstract. It is to ask what the workflow can do after reading it. A ticket summary is different from a tool call that can submit a change. A proposal is not an executed action. If the workflow can act, the target must still enforce the limit when the model or runtime is wrong.

Zero Trust and identity governance answer related but different questions. The United States National Institute of Standards and Technology (NIST) describes Zero Trust as moving protection away from static network perimeters toward users, assets and resources. NIST Special Publication 800-207 is an architecture publication, not a telecom rule. Identity governance helps show who owns an account and how its privileges change. Neither label proves that a connector cannot act beyond the target’s policy. Name the enforcement point.

The same discipline applies to any workflow map. Identify who starts the task, the identity used at each step, the records it reads, the connector it calls, the target that decides, and the service affected. If the target sees only a shared connector account, say so. If a log records a request but not the final network state, the result remains unknown. That is not an argument that every carrier has the same path. It is a reason to trace the path in the operator’s own environment.

Chapter 3 has shown where authority can travel. The next question is harder: when the operator stops the workflow, does the authority stop too—and can the network team still see the service?

# Chapter 4: Prove Safe Authority and Service-Safe Response

A diagram can show where an agent is supposed to stop. It cannot prove that the target will stop it.

Chapter 3 followed an identity to the network target. Here we ask what the operator can actually observe and control when a workflow misbehaves. A design review can show an approval step. A benchmark can test a model on a defined set of tasks. A lab can show an API rejecting a request in that configuration. A tabletop can reveal who calls whom. Each helps answer a different question. None proves, by itself, that the live service is safe or recoverable.

## The assistant stops. Does its authority?

**Illustrative scenario: an assistant that can narrow the Network Operations Center (NOC) view.** In this supplied situation, an assistant summarizes alarms and drafts ticket updates. It can read data from a neighboring domain and open supplier cases. It once proposed a change that could reduce the NOC’s visibility, but the change was not executed. The situation does not establish which identity, connector or target the assistant used, or whether it had direct network-write access.

For this walkthrough, add educational assumptions. Assume the assistant uses one shared service identity through connectors to the ticket system and an alarm/monitoring platform. Assume that same identity authorizes the neighboring-domain reads and supplier-case submissions. Assume the proposed visibility change would alter an alarm-routing setting, and that the identity can be revoked only as a whole; no independent alarm-read path has yet been verified. These details make the decision concrete, but they are not facts about an operator or the supplied situation.

The intended job sounds modest: collect alarms, summarize them and prepare a ticket or supplier case for an operator. But the service identity is also allowed to read neighboring-domain data, submit supplier cases and, under the exercise assumption, request a change to the monitoring view. The authority now exceeds the summarization task. A model proposing the change is not the same as a target accepting it. The operator must find out where the request stopped.

A stop command at the assistant may prevent the runtime from starting another tool call. It does not necessarily revoke the connector’s credential, terminate a session already opened at the ticket or monitoring system, or cancel a request already accepted and waiting in a queue. Those components have separate state. The assistant can report “stopped” while the target still has a valid session or a pending operation.

To verify a stop, start with the event identifiers that join the runtime, connector and target logs. Check whether the target accepted a request, which principal presented it, whether a session remains active, and whether the target has queued work. Revoke the credential where it is issued, terminate target-side sessions, and cancel or account for accepted requests. Then read the target’s resulting state and compare it with authoritative network and alarm records. A message in the assistant window is not proof that the target denied the call or returned to its prior state.

The alarm view changes the choice. If operators can read authoritative alarms through a separate, tested path, they can revoke the assistant’s broad identity without going blind. If the same identity supplies both the assistant and the only NOC alarm view, revocation may remove the very information needed to manage the service. That does not justify leaving write authority open. It means the team must first establish an independent view or make an explicit service decision about the temporary loss of visibility.

There are three practical responses. The team can disable the whole assistant and revoke its identity; that blocks future use of the principal, but may interrupt alarm reads and supplier-case handling, and still requires checking sessions and queued work. It can block only the write or case-submission path while preserving read access; that is preferable when the target enforces separate permissions and the NOC has a reliable view. Or it can keep the assistant at read-and-draft while a person submits changes through the normal process; this retains some support but still requires a narrow identity and visible source records.

Under the stated assumptions, I would not allow the assistant to change alarm routing or submit supplier cases through the shared identity. I would keep it out of the action path, have Network Operations establish an independent alarm view, and then revoke the broad credential and end its target sessions. The CISO advises whether the available evidence justifies containment; the NOC and network engineers establish service state and alternatives. If the independent view cannot be established, the service executive and incident lead must weigh the visibility loss against the evidence of misuse and choose a supported operating mode. A confirmed unauthorized target action is a reason to contain the path; it is not a reason to pretend that visibility loss is harmless.

Before enabling the assistant again, give it separate, task-limited identities for alarm reads and ticket drafts. Keep configuration changes in the existing human-approved change path. In a safe test, show that a prohibited monitoring write is denied at the target, that read access still works through its intended route, and that revocation ends active sessions and pending work. If the target cannot separate those permissions, keep submission outside the assistant. The recommendation changes only when target logs, permission tests and an independent NOC view demonstrate a narrower, recoverable path.

## Test what the network enforces

This is why a product demonstration is not an assurance result. The model may return a convincing answer while a connector still holds broad credentials. A user may click approve without seeing the exact target and operation. A mock API may reject a request while the production target accepts it under a different identity. Test the path the operator intends to use, with the identity and target that make the final decision.

A useful test compares an allowed request with a request that should fail. For example, an alarm-read request should return the approved data; a request to change alarm routing should be denied to the read identity. The operator should see which principal called the target, what the target accepted or refused, and whether any network or monitoring state changed. Repeat the denial test through alternate connectors and service accounts. If an alternate route reaches the same target, the first denial does not establish the boundary.

Test the stop while work is in flight. Let an approved request begin, then stop the runtime and revoke its credential. Check whether the connector retries, whether the target session survives, and whether queued work completes. A successful stop at one component does not imply a stop at the next. Record the tested software, identity, target and conditions so a later connector or policy change does not inherit evidence from a path it no longer uses.

The O-RAN study in Chapter 3 and the AgentDojo benchmark can help teams choose test cases. One exposed access-control weaknesses in a research testbed; the other demonstrated indirect prompt injection in simulated tool environments. Neither establishes how often those weaknesses occur in a carrier network or whether a particular operator blocks them. Use them to ask better questions, not to claim that your control passed.

A test result has a boundary. A paper review can reveal an omitted identity. A benchmark can probe a model on its stated tasks. A lab can establish behavior in that lab. A production observation can show a bounded live result if the operator records the conditions and denominator. A tabletop can test decisions and communication. These are different kinds of evidence, not rungs on a ladder where one replaces the others.

## Make recovery part of the decision

When the operator isolates a workflow, someone must confirm what changed in the network and what the NOC can still see. The incident lead can coordinate containment, but the service owner knows the impact and restoration constraints. The executive accountable for the affected service decides within the authority delegated to that role. If that authority does not cover the affected services or the remaining risk exceeds appetite, escalate rather than letting a committee or an approval screen appear to accept it.

A fallback is real only if the people expected to use it can reach authoritative state, have the required permissions and know the procedure. “A human can take over” is not enough. Check the alarm source, the manual change route, supplier support and the on-call roles before the assistant becomes operationally important. If the fallback relies on the same identity, connector or supplier under review, it is not independent.

Restoration should return the smallest useful capability first. In the scenario above, that might mean restoring alarm reads through a new, narrow identity while leaving monitoring changes and supplier submissions outside the assistant. Confirm target state, active sessions and queued work before re-enabling anything. Add permissions one at a time. If a denied action succeeds, logs cannot identify the caller, or the alarm view degrades, return to the last verified state and investigate the path.

The central trade-off is practical. Pausing a risky workflow can also remove visibility or support needed to operate the service. The answer is not to keep broad authority because it is convenient, nor to shut everything down without understanding the operational effect. Separate the action path from the view where possible. Where they cannot be separated, make the service consequence explicit and agree the fallback before relying on either choice.

Chapter 3 mapped how an identity could reach the target. This chapter showed how to test that boundary and make a stop observable. Chapter 5 turns to the supplier and legal conditions that determine whether those controls can be maintained, supported and exited.

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

# Chapter 6: The Next 12 Months: A Defensible Operator Agenda

Pausing an agent can reduce an access risk while removing a feed or supplier path the network team needs to see the service. Leaving it unbounded is not a safe alternative. The decision for the next year is narrower and more useful: which work will make a consequential workflow safer to use, what evidence would justify expansion, and what service capability must remain if the workflow is stopped?

The aim is not to predict how many agents operators will deploy or to claim that agents cause most telecom incidents. It is to produce a small, funded portfolio tied to local services. A product roadmap is not a portfolio. Neither is a list of controls without an owner, capacity or a service decision.

## Choose the priorities from local evidence

Start with four candidate work areas:

1. **Map consequential workflows.** Identify what is live or planned, which service it touches, what data it reads, and which identity, connector and target it uses.
2. **Bound and test target authority.** Demonstrate what the target permits and denies, how it attributes calls, and what happens to sessions or queued work when access is revoked.
3. **Rehearse service-safe containment and recovery.** Show how the operator preserves an authoritative service view, limits a suspect path, and restores the smallest safe capability.
4. **Set supplier, jurisdiction and exit conditions.** Know which rules apply to the entity and service, what supplier paths and changes matter, and what service can continue if the provider or feature becomes unavailable.

These are work areas, not necessarily separate projects. One test can support more than one only if the identities, connectors, target and service conditions align; otherwise, it does not establish control for another workflow.

Choose three or four only if local service evidence and capacity support them. Compare the candidates on service consequence, effective reach, urgency, dependencies, readiness to test and recover, full-life cost, available capacity and the specific work that would move. Do not turn unlike measures into a precise score. Prioritize a high-consequence gap or urgent exposure; use readiness and safe capacity to decide whether to test, narrow or sequence the work. A material unknown about a high-consequence path calls for funded discovery, not automatic deferral. If two priorities compete for one safe window, service consequence—not project maturity—sets the order. If three work areas address the material local risks, do not add a fourth just to complete the list; if all four matter and capacity exists, fund all four rather than creating an artificial cap.

Record each selected priority once in the board brief below. Use that brief as the portfolio’s decision record, not an extra committee layer. Mark local names, evidence, budget and work-item details clearly; an unknown stays unknown until someone verifies it.

Supplier and legal conditions apply to the workflows they affect even when work area four is not selected as a separate project. If a workflow cannot pass a relevant supplier-access, data, support or legal check, keep it bounded. A separate release check does not require a broad supplier-transformation programme.

## A hypothetical three-of-four choice

Assume, only for this exercise, that the operator can staff three of the four work areas this planning cycle. No budget, cost estimate or staffing level is asserted. The NOC situation in Chapter 4 raises the question of whether the assistant can affect the alarm view; the supplied situation says the proposed change was not executed. The supplier feature in Chapter 5 reads topology and proposes actions, but direct execution is not established. Add two planning assumptions: the operator is considering expanding the NOC workflow, while the supplier feature is not planned for enablement this cycle.

Under those assumptions, choose workflow mapping, target-boundary testing and service-safe containment. First map the actual identity and path for the planned NOC expansion. Then test what the relevant targets permit before increasing its authority. Rehearse a pause that keeps an independent alarm view available. Defer a broad supplier-and-exit review as a separate workstream, but do not enable or expand the supplier feature until its identity, logging, disablement, support, fallback and applicable legal checks are complete. The omitted work is delayed, not deemed safe; its reopening trigger belongs in the decision record.

This choice changes if the premises change. If the supplier feature enters a planned service workflow, or local evidence shows it can reach a sensitive target, move the supplier and target-boundary work ahead of a lower-consequence task. If the alarm view cannot be maintained without the assistant, fund and verify an independent view before considering expansion. If a clear excess permission is already known, close it through a supported change while the wider inventory continues. These are conditional management choices, not claims about operator practice or measured outcomes.

The example also shows why capacity belongs in the decision. Selecting three areas does not make the fourth disappear. Network engineers, platform staff, security, NOC and security operations centre (SOC) teams, Procurement and Legal already have work. Name the particular local change, access review, exercise, maintenance window or contract task that will move. “Reliability work” is not specific enough for the service executive to understand the trade-off. If no work moves, explain how the added effort is funded rather than assuming capacity is free.

## Sequence the year by what the decision needs

Use a simple sequence, adjusted to real maintenance windows and supplier support rather than an arbitrary calendar:

- **First, select the workflows and map their actual paths.** Record what is known, what is not, and why the service matters. Do not let adoption figures or a vendor calendar choose the first service.
- **Next, reduce clear excess authority and test the boundary safely.** If production denial could disrupt service, use a safe test route. Until target behavior is verified, keep the workflow at its last verified scope.
- **Then, rehearse the service response.** Confirm which alarm view and manual route remain, how active sessions and queued work are handled, who can act, and how restoration will be checked.
- **Before expanding, resolve the supplier and legal conditions that apply.** If a material dependency remains unknown, hold the scope or bring the service-specific choice to an authorized executive.

At each point, management can expand within the tested scope, keep the workflow bounded while gathering evidence, or stop and use a supported manual process. Stopping is not automatically safest if it removes service visibility. If no independent view or support route is ready, state the consequence and make a service decision before removing the only operational path—unless evidence of misuse requires immediate containment. In either case, check target state rather than treating the assistant’s stop message as proof.

## Put one decision in front of the board

The board should oversee risk appetite, resources, escalation and assurance. Management should own delivery and service risk within delegated authority. The CISO provides distinct security advice; a board update or an approval button does not itself establish that a target boundary works or that the service can recover. Approval to fund mapping and testing does not approve expansion of a workflow’s production authority.

A one-page decision brief can ask directors to approve capacity for three or four locally justified priorities. For each, it should state four things:

- **Scope and ownership:** Which service and workflow are included, who is the accountable executive, and what is the CISO’s separate advice?
- **Evidence and limits:** Which target requests should pass or fail, what log or resulting state proves it, what remains unknown, and what is out of scope?
- **Investment and trade-off:** What is the full-life cost and its basis, what is still unknown, which functions and windows provide capacity, and what specific work moves with what consequence? Use fields such as `[local budget]`, `[work-item ID]` and `[change window]` when those values are not yet set.
- **Service and risk decision:** What fallback preserves the operational view and recovery, who may accept the remaining risk within delegated authority, and what evidence or change will trigger reassessment?

Do not promise return on investment (ROI) without a local baseline, a comparison method, a quality measure and full operating cost. A faster workflow may still require correction and supervision. A successful target-denial test is a security result, not a productivity result. Keep those decisions separate. Classify cost figures as supplier quotes, internal estimates or unknown, and separate one-time, recurring and exit costs where the operator can. If a value is missing, name who will obtain it or write `[estimate pending]`; do not turn a blank into zero or use it to delay the first local decision.

The management ask is simple: authorize the selected capacity, keep write scope bounded until the target test and service fallback are demonstrated, and return for a decision if those conditions change. Do not ask directors to approve AI as a category.

## What should change the order

Reopen a priority when evidence changes the service decision. A newly verified route to a sensitive target may move boundary correction forward. A supplier change to identity, data handling, support or update behavior may bring dependency review forward. An exercise that exposes a shared fallback identity may require a different recovery path before expansion. A legal change requires Legal to check the affected entity and service before the scope is revised.

Threat reporting can prompt a local comparison, but an AI label alone does not set the priority. Compare the reported technique with local exposure, telemetry and service consequence. If the evidence does not change, do not expand because a project reached a milestone or a supplier announced a feature. Hold at the approved scope and state what evidence is still needed. Absence of a reported incident is not proof that the boundary works.

At the next planning meeting, decide whether to fund the three or four priorities your local evidence supports. In the worked example, that means mapping the proposed NOC expansion, testing target permissions and rehearsing an independent alarm view; write access stays out until those results are known. Do not enable or expand the supplier feature until its release checks pass. Put the accountable owner and displaced work in the brief.
