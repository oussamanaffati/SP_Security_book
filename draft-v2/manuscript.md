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

When leadership asks its chief information security officer (CISO) to pause a workflow that uses artificial intelligence (AI), the request may make sense. The network team may still depend on its data feed, supplier console or alert path to see the service. If no one checks those dependencies first, the team could lose visibility or support. But leaving the workflow running without a proven boundary creates another risk. That tension sits at the centre of this book.

Neither response is enough. Start with the workflow itself. What data does it read, which identity and connector does it use, and what can it recommend or change? Check where the target enforces permission. Then ask what the team can still see if the workflow stops, and who can restore the service.

This is a service-provider security problem. A decision sits inside a live service, with people, suppliers and dependencies that may still be needed when a workflow stops. A control that looks easy in a demonstration can be hard to remove from operations. And “in production” says little about what the system can change, how widely it is used or whether security improved.

The sources in this book show serious telecom targeting, but do not establish AI as the cause of the incidents discussed. The systems themselves are at different stages. Keep three distinctions in view: productivity is not security effectiveness, a threat report is not a local risk assessment, and a test supports only the path it exercised.

The argument moves from claims to decisions. Chapter 1 asks what is actually in use; Chapter 2 tests what threat reports do and do not say. Chapters 3 and 4 trace how a workflow reaches a network target, and what happens when it is stopped. Chapter 5 looks at legal and supplier conditions, including exit. Chapter 6 turns those choices into a twelve-month investment agenda.

Chapters 3 and 4 work through two illustrative operational situations. Chapter 5 looks briefly at a supplier feature. These are examples, not incident reports or test results. Any details added for the walkthroughs are marked as assumptions; operators do not all have the same systems or constraints.

Read the chapters in order to build a shared risk view; each one builds on decisions made earlier. If you are preparing for a specific decision, start with the relevant chapter, then return to Chapter 6 to choose priorities, assign ownership and decide what evidence or capacity is needed.

By the end, a telecom CISO should be able to tell a live deployment from a demonstration or plan, trace what a workflow can read and change, plan a safe stop and recovery, assess supplier dependencies, and choose three or four priorities for the chief executive officer (CEO) or board. For each, the CISO should be able to say what is known, what is not, who owns the service and risk, and what new evidence would change the decision.

# Chapter 1: What Is Actually Deployed?

In February 2026, Deutsche Telekom said its Radio Access Network (RAN) Guardian Agent had gone live in Germany. The company reported more than 100 autonomous remediation actions in its first month, during Christmas-market events. It also reported that managing major events fell from hours to about a minute.

The release gives more detail than a simple “in production” announcement: it names the workflow, location, action count and time comparison. It does not give the event sample, measurement method, success rate or rollback rate. Treat the numbers as company-reported results, not proof of network-wide autonomy, better service or improved security.

## Look at the task, not the label

One NZ’s Network Concierge gathers performance data, alarms and past incidents, then gives a customer-service representative a summary and suggested next step. The operator reports an 80 percent reduction in analysis time, not restoration time. The release gives no case count, baseline or measure of answer quality, so we cannot tell whether customers got service sooner.

The same release describes a separate generator-placement tool used during severe weather to help engineers decide where to send mobile generators. It is a different workflow from complaint analysis, and it is not evidence that an AI system controlled the network or restored service.

Orange France says Mon Assistant IA was deployed to 3,000 sales advisers and supported nearly one million conversations per month. The adviser remains in control and validates proposed responses. Those figures describe reported reach and activity. They do not measure time saved, answer quality or customer outcomes.

SK Telecom’s AI-RAN Parameter Recommender was applied to its commercial network and systematically validated. It recommends base-station parameters; the same release says real-time application was still being developed. Commercial-network validation is not autonomous production control.

These examples measure different things. Deployment tells us where a system is used. Activity is a count of actions, users or conversations. Productivity compares effort with a credible baseline, including review and rework. Service quality is about correctness and customer impact; security effectiveness is about whether a control or threat outcome changed. Return on investment (ROI) compares costs and benefits on the same basis. No one measure stands in for another.

## Ask what “production” means here

“Production” matters, but it tells us neither the system’s reach nor its effectiveness. It may be live in one workflow while its footprint, authority and failure behavior remain unclear. Separate the stage from the action: does the system gather information, recommend a change, prepare one for approval or submit it itself? Then ask which system enforces the action and which service it could affect.

Start with the workflow and service. Is the system a demonstration, a pilot or in live use? How widely is it used? Then ask which identity and actions it has, who is reporting the result and what the metric counts. For a measured claim, ask for the denominator, baseline, period and comparison method. Mark important gaps as unknown. A plan is not a live deployment, and an activity count is not an outcome.

Use the same discipline with threat claims. The next chapter asks what public disclosures say about telecom intrusions—and what they leave unknown.

# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort against intrusion activity targeting the telecommunications sector. It said all four major operators had been targeted. The operation lasted more than eleven months and involved over 100 cyber defenders.

Those figures show the scale of the defensive effort, not how many attacks it stopped or outages it prevented. The account documents serious telecom targeting and a large response, but does not attribute the operation to AI.

In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported that actors affiliated with the People’s Republic of China (PRC) had compromised multiple telecommunications companies’ networks. The agencies said the intruders stole customer call-record data, accessed private communications belonging to a limited number of people—mainly those involved in government or politics—and copied some information subject to United States law-enforcement requests. An October FBI-CISA statement had already confirmed unauthorized access to commercial telecom infrastructure and assistance for affected companies and potential victims. The public disclosures do not report AI use in this activity. They also leave the forensic timeline and duration of undetected access unclear.

## Count the right thing

The European Union Agency for Cybersecurity (ENISA) counted 30 cybersecurity incidents in an open-source intelligence (OSINT) overview. A separate annual summary contained 188 significant-incident reports submitted by national authorities. That set also includes service outages, system failures, human error and natural phenomena. The collections draw on different inputs and definitions; they are not a combined total or comparable rates.

The OSINT overview shows publicly reported cyber activity, not every telecom intrusion. The authority-submitted reports capture continuity-impact events under a reporting framework, not just hostile campaigns. Because the collections answer different questions, neither estimates an operator’s local exposure.

## Put the threat report to work

An AI label matters only when evidence connects AI to this incident. Then ask what it changed: the task, scale, timing, access or consequence. A tool used elsewhere in a campaign is not enough.

That uncertainty does not stop the operator from acting. Map the management, identity, supplier and remote-support paths into sensitive network functions. Identify the customer, signaling, location and operational records that would matter if read or altered. Make sure responders can see authoritative service state during an investigation, and know which changes preserve evidence without causing a second outage. Public disclosures cannot answer those local questions for you.

Would knowing AI was involved change a decision? Where an external model or agent is called, can logs connect the requesting identity and input to the destination, tool call and result? If that information would not change detection or response, the label may describe the event without helping the operator act.

Do not wait for proof of AI use before correcting a known exposure. A credential that reaches a management interface, an unobserved supplier path or an exposed system with a supported fix matters on its own. Attribution can refine the investigation; it does not remove the operator’s responsibility for a path already at risk.

At the next briefing, ask what happened to the telecom target, what ties AI to the operation, and whether that attribution changes the response. If the intrusion is clear but the AI link is not, report the intrusion and say that the link remains unconfirmed.

Threat reports set the context. The operator’s next question is local: which identity and target can turn access into service impact?

# Chapter 3: Follow Authority to the Network Target

A radio application can create a network-control risk without being called an AI agent. In a 2024 peer-reviewed study, researchers built an experimental Open Radio Access Network (O-RAN) H-Release environment and found missing access controls for xApps, applications deployed on an O-RAN controller. They demonstrated three attacks through application programming interfaces (APIs) and the E2 interface, including attacks that disrupted radio access network (RAN) components. This was a lab result, not proof that a carrier’s production network has the same path. It leaves a practical question: which identity can reach which target, through which interface, and what can that target do?

The study did not test a large language model (LLM)-based agent; the applications were not automatically AI agents. The weakness was not bad model advice, but insufficient control over what an application could reach through network-management interfaces. That distinction still matters when a language model joins an operational workflow. It may reason about a change, but a runtime must call a tool, the tool must use a credential, and an API must accept the request before the target can alter the network.

What matters is the authority each step in that chain carries.

## Follow one identity to its target

**Illustrative scenario: a shared account across edge and core.** One service account can reach edge nodes and parts of the core. Remediation depends on the supplier’s configuration and a safe maintenance window. The situation does not say whether an AI agent used the account, which commands the target would accept, or whether separate identities are supported.

**Assumptions for the example.** A maintenance assistant reads edge alarms and configuration, then prepares a supplier-supported change through an operator connector. The connector uses the shared account. Its intended task is limited to the edge service, although that account can also reach part of the core. No local test has shown whether the target distinguishes an edge request from a core request. These added details make the trade-off concrete; they are not part of the supplied situation.

Follow the request from the alarm data to the target. The assistant reads the data; its runtime passes a request to the maintenance connector, which presents the shared account to a target API. The target sees the account, not necessarily the assistant, the person who asked for the work or the edge-only purpose. If it accepts a core operation under that identity, the account can do more than the assistant’s task requires. An approval screen narrows nothing unless it names the exact target and operation and the target enforces that limit.

This is why “human in the loop” is not a permission model. It describes a role in a process. It does not tell us whether approval happens before execution, whether the reviewer sees the exact request, which credentials perform it, or whether the target enforces the intended limit.

Keeping the account as it is avoids a rushed migration and preserves the supplier’s current support route. But edge and core remain joined under one principal. If something goes wrong, logs may show that the account acted without showing which workflow or person started the request. Giving the assistant this credential would also give its edge task reach into the core.

A gateway can buy time, but only if every route to the target passes through it, there is no bypass, and it can block core operations while allowing the edge work. Test what happens when it fails. A fail-closed gateway may interrupt support; a fail-open one may restore the broad path. Drawing the gateway on a diagram does not prove that it controls the target.

Use separate target identities if the platform supports them: an edge identity for edge work and a different core identity for workflows that need it. The move takes engineering and supplier time. Running old and new accounts in parallel can expose missing permissions, but extends the overlap. Retiring the old account first shortens that period, yet may interrupt monitoring or supplier support. A staged migration takes longer; it lets the team check each workflow before removing the shared account.

Given these assumptions, keep the assistant out of the write path. Network Engineering and the supplier should confirm which identities the platform supports and plan a safe move. The CISO sets the boundary: no agent write access through the shared account until the target enforces the intended limit. The service executive owns any period when support must remain broad; until then, keep the existing route for its authorized purpose, not the assistant. A gateway may help in the meantime, but test it first: edge requests should pass, core requests should fail, alternate routes should not bypass it, and logs and revocation should work even if the gateway fails. Keep an emergency route, but make sure it does not recreate the same broad access.

Revisit this recommendation if the target cannot support separate identities, if a tested gateway blocks every alternate route without disrupting required support, or if the maintenance path has different service dependencies. Local logs may also show that the account can already perform a sensitive core action. If so, reduce its scope or make an authorized service decision now; do not let a longer inventory delay the response. The deciding facts are the target’s permissions, the routes into it and how each restriction affects the service.

## From influence to permission

Data can influence an agent without carrying a credential. A tool can hold a credential without making every model output executable. And a target can reject a request even when the model and connector agree. These are separate boundaries.

The peer-reviewed AgentDojo benchmark illustrates the first boundary. Researchers used simulated tool environments to test how instructions hidden in third-party data could influence an agent. They demonstrated an indirect prompt-injection mechanism: data returned by a tool can be treated as instructions and redirect later tool use. The benchmark does not test telecom systems, measure how often this happens at operators or show that an injection changes network state by itself.

For an operator, the point is not to decide whether retrieved content is “trusted” in the abstract. It is to ask what the workflow can do after reading it. A ticket summary is different from a tool call that can submit a change. A proposal is not an executed action. If the workflow can act, the target must still enforce the limit when the model or runtime is wrong.

Zero Trust and identity governance answer different questions. The United States National Institute of Standards and Technology (NIST) describes Zero Trust as moving protection away from static network perimeters toward users, assets and resources. Its Special Publication 800-207 describes an architecture; it is not a telecom rule. Identity governance helps establish who owns an account and how its privileges change. Neither label shows that a connector stays within the target’s policy. Identify the enforcement point.

Apply the same discipline to the workflow map. Follow who starts the task, which identity it uses, what records it reads, which connector it calls, what target decides and which service could be affected. If the target sees only a shared account, say so. If logs show a request but not the resulting network state, the outcome is unknown. Operators do not all have the same path; each needs to trace its own.

Tracing authority is only half the story. When the workflow stops, does the target stop too—and can the NOC still see the service?

# Chapter 4: Prove Safe Authority and Service-Safe Response

A diagram can show where an agent is supposed to stop. It cannot prove that the target will stop it.

Chapter 3 followed an identity to the network target. Now the question is what the operator can observe and control when a workflow misbehaves. A design review shows where approval is meant to happen. A benchmark tests a model on defined tasks; a lab tests an API in one configuration; a tabletop shows how people respond. Each helps in a different way. None, on its own, proves that the live service is safe or recoverable.

## The assistant stops. Does its authority?

**Illustrative scenario: an assistant that can narrow the Network Operations Center (NOC) view.** The assistant summarizes alarms, drafts ticket updates, reads data from a neighboring domain and opens supplier cases. It once proposed a change that could reduce the NOC’s visibility; that change was not executed. The situation does not say which identity, connector or target it used, or whether it could write directly to the network.

**Assumptions for the example.** The assistant uses one shared service identity through connectors to the ticket system and alarm platform. That identity also authorizes neighboring-domain reads and supplier-case submissions. The proposed visibility change would alter alarm routing. The identity can be revoked only as a whole, and no independent alarm-read path has been verified. These assumptions make the choice concrete; they are not part of the supplied situation.

The intended job sounds modest: collect alarms, summarize them and prepare a ticket or supplier case for an operator. But the service identity is also allowed to read neighboring-domain data, submit supplier cases and, under the exercise assumption, request a change to the monitoring view. The authority now exceeds the summarization task. A model proposing the change is not the same as a target accepting it. The operator must find out where the request stopped.

A stop command at the assistant may prevent the runtime from starting another tool call. It does not necessarily revoke the connector’s credential, terminate a session already opened at the ticket or monitoring system, or cancel a request already accepted and waiting in a queue. Those components have separate state. The assistant can report “stopped” while the target still has a valid session or a pending operation.

Start with event identifiers that link the runtime, connector and target logs. They should tell you whether the target accepted the request, which identity presented it, whether a session remains open and whether work is queued. Revoke the credential at its source, close target-side sessions, and cancel or account for accepted requests. Then compare the target’s current state with the authoritative network and alarm records. The assistant’s “stopped” message cannot answer those questions.

The alarm view changes the choice. If operators can read authoritative alarms through a separate, tested path, they can revoke the assistant’s broad identity without going blind. If the same identity supplies both the assistant and the only NOC alarm view, revocation may remove the very information needed to manage the service. That does not justify leaving write authority open. It means the team must first establish an independent view or make an explicit service decision about the temporary loss of visibility.

The team can disable the assistant and revoke its identity. That blocks future use of the principal, but may interrupt alarm reads and supplier cases; live sessions and queued work still need attention. If the target separates permissions and the NOC has a reliable view, block write and case submissions while keeping reads. Or leave the assistant at read-and-draft and have a person submit changes through the normal process. That keeps some support in place, but still requires a narrow identity and visible source records.

With these assumptions, do not let the assistant change alarm routing or submit supplier cases through the shared identity. Keep it out of the action path until Network Operations has an independent alarm view. Then revoke the broad credential and close the target sessions. The CISO advises on containment; the NOC and network engineers confirm service state and alternatives. Without an independent view, the service executive and incident lead must weigh lost visibility against evidence of misuse and choose a supported mode. An unauthorized target action requires containment. It does not make the loss of visibility harmless.

Before turning the assistant back on, give alarm reads and ticket drafts separate, task-limited identities. Keep configuration changes in the existing human-approved process. In a safe test, verify that the target denies a prohibited monitoring change, that the intended read path still works, and that revocation ends active sessions and pending work. If the target cannot separate these permissions, keep submissions outside the assistant. Reconsider only when logs, permission tests and an independent NOC view show a narrower path that can be recovered safely.

## Test what the network enforces

A convincing demonstration is not proof that the live path is controlled. The connector may still hold broad credentials; an approver may not see the exact target and action; a mock API may refuse a request that the production target accepts under another identity. Test the intended path with the identity and target that make the final decision.

Compare a request that should pass with one that should fail. An alarm-read identity should return approved data but be denied a change to alarm routing. The logs should show which identity called the target, what it accepted or refused, and whether network or monitoring state changed. Try the denied request through alternate connectors and service accounts too. One blocked route does not prove the boundary if another still reaches the target.

Test the stop with work in flight. Start an approved request, stop the runtime and revoke its credential. Then see whether the connector retries, the target session survives or queued work completes. Stopping one component does not stop the next automatically. Record the software, identity, target and conditions tested; a later connector or policy change may invalidate the result.

The O-RAN study in Chapter 3 and the AgentDojo benchmark can help teams choose test cases. One exposed access-control weaknesses in a research testbed; the other demonstrated indirect prompt injection in simulated tool environments. Neither establishes how often those weaknesses occur in a carrier network or whether a particular operator blocks them. Use them to ask better questions, not to claim that your control passed.

Every test has limits. A paper review may reveal an omitted identity. A benchmark probes only its defined tasks; a lab shows behavior in that environment. Production observation can support a bounded live result, but only if the conditions and denominator are recorded. A tabletop shows how people decide and communicate. These forms of evidence answer different questions; none covers them all.

## Make recovery part of the decision

When a workflow is isolated, someone must check what changed in the network and what the NOC can still see. The incident lead coordinates containment; the service owner understands the impact and restoration constraints. The executive accountable for the service decides within their delegated authority. If that authority does not cover the service, or the remaining risk exceeds appetite, escalate it. Do not let a committee or approval screen stand in for an authorized decision.

A fallback works only if the people who need it can see authoritative service state, have the right permissions and know what to do. “A human can take over” is not enough. Before the assistant becomes operationally important, confirm the alarm source, manual change route, supplier support and on-call roles. A fallback that depends on the same identity, connector or supplier is not independent.

Restore only the smallest useful capability at first. Here, that could mean bringing back alarm reads under a new, narrow identity while keeping monitoring changes and supplier submissions outside the assistant. Before re-enabling anything, check target state, active sessions and queued work. Add permissions one at a time. If a denied action succeeds, the caller cannot be identified or the alarm view degrades, return to the last verified state and investigate.

Pausing a risky workflow can cost the team visibility. Leaving broad authority in place can cost security. Separate the action path from the service view whenever possible. If they cannot be separated, state the service impact and agree the fallback before choosing.

Supplier support and legal duties determine whether the operator can maintain that boundary and whether it can leave without disrupting the service. Chapter 5 looks at both.

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

Treat the table as a starting map. Ask counsel to confirm the current text, national implementation and applicability to each service and entity. A deadline in one market does not automatically apply in another. A consultation, government code, industry standard and statute are not interchangeable.

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

Raise these points while the operator still has leverage, but expect suppliers to resist some requests. Contracts cannot guarantee technical outcomes; test the controls the operator can influence. A deletion clause alone does not show that every copy is gone, and “supervised access” does not prove that the target sees a separate, revocable identity.

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

Legal duties set the floor; the contract sets supplier expectations. But they cannot show who can disable a connector at 02:00, whether existing sessions terminate or whether the NOC can still manage the service. The operator has to map, test and fund those capabilities.

These obligations and supplier dependencies narrow the choices. Chapter 6 asks where to spend limited capacity over the next year.

# Chapter 6: The Next 12 Months: A Defensible Operator Agenda

Spend next year’s limited capacity first on workflows that need safer limits and a better recovery path. Let service impact, not the AI label, set the order. The NOC must still see the service if a workflow is stopped.

Start with the services an agent could touch. Supplier roadmaps cannot decide what your teams can fund or which risks management can accept. Those are local decisions.

## Choose the priorities from local evidence

Start with four candidate work areas:

1. **Map consequential workflows.** Identify what is live or planned, which service it touches, what data it reads, and which identity, connector and target it uses.
2. **Bound and test target authority.** Demonstrate what the target permits and denies, how it attributes calls, and what happens to sessions or queued work when access is revoked.
3. **Rehearse containment and recovery.** Show how the team can limit a suspect path without losing its view of the service, then restore the smallest useful capability.
4. **Set supplier, jurisdiction and exit conditions.** Know which rules apply to the entity and service, what supplier paths and changes matter, and what service can continue if the provider or feature becomes unavailable.

Treat these as four lines of work, not automatically four separate projects. One test may help with more than one only when the identities, connectors, target and service conditions match. Otherwise, it does not prove that the other workflow is controlled.

Choose three or four only when local evidence and capacity support them. Weigh service impact, reach, urgency, dependencies, readiness, cost over the system’s life and the work that would be delayed. Do not turn unlike measures into one score. Put high-consequence gaps and urgent exposures first. Use readiness to decide whether to test, narrow or sequence the work. When a path is unclear and the consequence high, fund discovery. If priorities compete for one safe window, protect the service facing greater harm. The number is not a target: choose fewer if they cover the risks, all four if each matters and the teams can deliver.

Use the board brief below to record the decision. Fill in local owners, evidence, budget and work items; mark unknown facts until someone verifies them.

Supplier and legal checks still apply to the workflows they affect, even when they are not a separate project. Keep access within the agreed boundary until the relevant data, support and legal conditions are checked. This need not become a company-wide supplier programme.

## A hypothetical three-of-four choice

Assume teams can staff three of the four areas this cycle. That is a capacity constraint, not a budget or headcount estimate. In the Chapter 4 situation, the assistant proposed a change that could narrow the alarm view; it was not executed. The supplier feature reads topology and proposes actions, but whether it can execute them is unknown. For planning, assume the operator is considering expanding the NOC workflow but not enabling the supplier feature this cycle.

On that basis, choose workflow mapping, target testing and containment that preserves service visibility. First trace the identity and path for the planned NOC expansion. Test what the target permits before granting more authority. Then rehearse a pause that leaves an independent alarm view. A broader review of supplier access and exit can wait, but do not enable or expand the feature until its identity, logging, disablement, support, fallback and legal duties have been checked. Deferring the review does not make the feature safe; state when to revisit it.

Reorder the work when an assumption changes. Bring supplier and target testing forward if the feature enters a live service path or can reach a sensitive target. If the assistant is the only way to see alarms, fund an independent view first. Remove any known excessive permission through a supported change while the wider inventory continues.

The choice is credible only if the teams have time. Network Engineering, platform operations, Security, the NOC, the security operations centre (SOC), Procurement and Legal all have existing commitments. Name the change, access review, exercise, maintenance window or contract task that will move. “Reliability work” is too vague for the service executive to weigh. If nothing moves, explain how the extra effort is funded; capacity is not free.

## A practical order for the next year

Fit the sequence to real maintenance windows and supplier support, not an arbitrary calendar:

- **First, select the workflows and map their actual paths.** Record what is known, what is not, and why the service matters. Do not let adoption figures or a vendor calendar choose the first service.
- **Next, reduce clear excess authority and test the boundary safely.** If production denial could disrupt service, use a safe test route. Until target behavior is verified, keep the workflow at its last verified scope.
- **Then, rehearse the service response.** Confirm which alarm view and manual route remain, how active sessions and queued work are handled, who can act, and how restoration will be checked.
- **Before expanding, resolve the supplier and legal conditions that apply.** If a material dependency remains unknown, hold the scope or bring the service-specific choice to an authorized executive.

As work progresses, management can expand within the tested scope, hold the current boundary while gathering evidence, or stop and use a supported manual process. A stop is not automatically safer if it removes the service view. If no independent view or support route is ready, make the service consequence explicit before removing the only operational path—unless evidence of misuse requires immediate containment. Either way, check the target; the assistant’s stop message is not proof.

## Put one decision in front of the board

The board oversees risk appetite, resources, escalation and assurance. Management owns delivery and service risk within its delegated authority. The CISO gives separate security advice. A board update or approval button cannot prove that the target enforces a boundary or that the service can recover. Funding a map and test does not approve more production authority.

Use a one-page brief to ask directors for capacity to fund three or four locally justified priorities. For each one, answer four questions:

- **What are we funding?** Name the service and workflow, the accountable executive and the CISO’s separate advice.
- **What will count as proof?** State which target requests should pass or fail, what log or resulting state will show it, and what remains unknown or out of scope.
- **What will it cost and displace?** Give the full cost over the system’s life, its basis, capacity and change windows, and name the work that will move. Use `[local budget]`, `[work-item ID]` and `[change window]` where details are not yet set.
- **How will the service keep running?** Name the fallback, who may accept risk within their authority, and what change or evidence will trigger a new decision.

Do not promise return on investment (ROI) without a local baseline, a fair comparison, a quality measure and the full operating cost. A faster workflow may still need correction and supervision. A target-denial test measures security, not productivity. Keep those results separate. Label each figure as a supplier quote, internal estimate or unknown; show one-time, recurring and exit costs separately where possible. For a missing value, name who will obtain it or write `[estimate pending]`. A blank is not zero, and it need not delay the first local decision.

Ask management to fund the selected work, keep write access within the tested boundary, and prove that the service fallback works before expansion. Return for a new decision if those conditions change. Do not ask directors to approve “AI” as a category.

## What should change the order

Reopen a priority when new evidence changes the service decision. A newly confirmed route to a sensitive target may bring boundary work forward. A supplier change to identity, data handling, support or updates may require an earlier review. If an exercise finds that the fallback shares an identity with the system under review, reassess the recovery path before expanding. Legal should check any change in the rules against the affected entity and service.

Threat reports can prompt a local check, but an AI label alone does not set the priority. Compare the reported technique with local exposure, telemetry and service impact. Do not expand simply because a project reached a milestone or a supplier announced a feature. Keep the approved scope and say what evidence is still missing. A lack of reported incidents does not show that the boundary works.

At the next planning meeting, put the proposed NOC expansion on the table. Ask for a workflow map, tested target permissions and a rehearsed independent alarm view before granting write access. Hold the supplier feature until its release checks pass; record the accountable owner and displaced work in the brief.
