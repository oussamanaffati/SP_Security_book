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

When a chief information security officer (CISO) is asked to pause a workflow that uses artificial intelligence (AI), the request often makes sense on paper. The operations team may still need the data feed, supplier console or alert path to understand what is happening to the service. Stopping the workflow can remove that visibility. Leaving it running without a clear boundary creates a different risk.

This is the practical tension we see with service providers today. Once a workflow becomes part of live operations, it is no longer sitting beside the service. It is part of how the service is run.

The board and the chief technology officer (CTO) do not need another discussion about agents. They need to know what a workflow can read and change, which identity and connector it uses, which system enforces that authority, and what remains visible if the workflow is stopped. They also need to know who owns the decision when security and service continuity pull in opposite directions.

The public record shows serious targeting of telecom networks. It does not show that AI caused the incidents discussed here. Operators are deploying systems at very different stages. Productivity gains are not the same as security effectiveness. A threat report is not a local exposure assessment. A test covers only the path and conditions that were exercised.

This book follows the decisions a telecom CISO or CTO has to make. Chapter 1 asks what is actually deployed. Chapter 2 looks at the threat picture without adding AI where the evidence does not support it. Chapters 3 and 4 follow authority from identity and data to the network target, then examine whether the operator can contain and recover without losing the service view. Chapter 5 covers the legal and supplier conditions that limit the options. Chapter 6 turns those decisions into a small set of priorities that management can defend over the next twelve months.

Chapters 3 and 4 follow one fictional NOC assistant from routine use through detection, containment and restoration. Chapter 5 uses a shorter supplier-feature example. These are educational scenarios, not incident reports, observed tests or measured results. Their assumptions are stated where each begins.

Read the chapters in order to build a shared view of the risk; each one builds on decisions made earlier. If you are preparing for a specific decision, start with the relevant chapter, then return to Chapter 6 to choose priorities, assign ownership and decide what evidence or capacity is needed.

By the end, a telecom CISO should be able to tell a live deployment from a demonstration or plan, trace what a workflow can read and change, plan a safe stop and recovery, assess supplier dependencies, and choose three or four priorities for the CEO or board. For each, the CISO should be able to explain what is known, what is not, who owns the service and risk, and what new evidence would change the decision.

# Chapter 1: What Is Actually Deployed?

In February 2026, Deutsche Telekom reported that its Radio Access Network (RAN) Guardian Agent was live in production in Germany. The company said the agent had triggered more than 100 autonomous remediation actions in its first month during Christmas-market events. It also said the time to manage major events had fallen from hours to about a minute.

The claim is specific. It names the operator, workflow, location and action count, and gives a time comparison. It does not give the number of events behind that comparison, the measurement method, or a success, override or rollback rate. The numbers show activity. They do not tell us how often the actions were correct or what happened to service when they were not.

## Look at the task, not the label

One NZ’s Network Concierge gathers network performance data, alarms and past incidents, then gives a customer-service representative a summary and a suggested next step. The operator reported an 80 percent reduction in analysis time. That is analysis time, not restoration time. The release gives no case count, baseline or measure of answer quality, so we cannot tell whether customers got service sooner.

The same release describes a separate tool that helps engineers decide where to place mobile generators during severe weather. That is a different workflow from complaint analysis, and it is not evidence that an AI system controlled the network or restored service.

Orange France says Mon Assistant IA was deployed to 3,000 sales advisers and supported nearly one million conversations per month. The adviser remains in control and validates proposed responses. Those figures describe reported reach and activity. They do not measure time saved, answer quality or customer outcomes.

SK Telecom’s AI-RAN Parameter Recommender was applied to its commercial network and systematically validated. It recommends base-station parameters; the same release says real-time application was still being developed. Commercial-network validation is not autonomous production control.

These examples measure different things. Deployment tells us where a system is used. Activity is a count of actions, users or conversations. Productivity compares effort with a credible baseline, including review and rework. Service quality is about correctness and customer impact; security effectiveness is about whether a control or threat outcome changed. Return on investment (ROI) compares costs and benefits on the same basis. No one measure stands in for another.

That distinction changes what a CISO or CTO should approve. If a production claim is based on RAN Guardian, the reported activity supports a request to understand its permitted action scope, service checks and failure path. The missing denominator and rollback information do not support a broader claim that the system is safe or improves security. If a team is considering a One NZ-style analysis workflow, an observed reduction in analysis time could justify a local productivity assessment, but the baseline must include human review and rework, and answer quality must be checked separately. It would not establish faster restoration. Orange’s conversation volume can inform capacity planning, but not a productivity or customer-quality claim. SK Telecom’s commercial-network validation supports a discussion about how recommendations enter the change process; it does not justify autonomous real-time application while that capability remains in development.

The evidence needed follows the decision. Before expanding authority, ask what actions are allowed and how the network can recover from a bad one. Before funding a productivity case, compare the same task and quality standard before and after, including review effort. Before claiming a service result, measure the customer or network outcome. Before claiming security effectiveness, show what threat or control outcome changed. These records can inform one investment decision, but they cannot be collapsed into a single “AI value” figure.

## Ask what “production” means here

“Production” is a useful signal. It means the operator is saying the system runs in a live workflow. It does not tell us the footprint, what the system can change, which target enforces its authority or what service visibility remains if the workflow stops. For the next decision, ask what the task is, who uses the system, what it reads and changes, where the limit is enforced, and what remains available if it is stopped. Mark any material unknown as unknown.

A demonstration can show that a task is technically possible. A pilot can show how a defined group or service uses it under stated conditions. A production deployment means it is part of an operating workflow, but does not by itself show that it is widely used, reliable or well controlled. Approval should match the stage. A recommendation tool may need a defined human approval path; a system that can submit changes needs target-side limits, attribution and a safe way to stop or reverse its work. Do not approve broader authority because the product label sounds mature.

When someone reports a result, ask who made the claim and what was counted. For a measured claim, ask for the denominator, baseline, period and comparison method. A count of actions may say something about activity; it does not show how many actions were correct, whether service quality improved or whether a security control worked. Mark important gaps as unknown. A plan is not a live deployment, and an activity count is not an outcome.

Use the same discipline with threat claims. The next chapter asks what public disclosures say about telecom intrusions—and what they leave unknown.

# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort against intrusion activity targeting the telecommunications sector. It said all four major operators had been targeted. The operation lasted more than eleven months and involved over 100 cyber defenders. The disclosure also described a small amount of primarily network-related technical data being exfiltrated. It reported no evidence to date that sensitive or personal customer records were accessed or exfiltrated, or that services were disrupted. The public account does not attribute the operation to AI.

Those details answer different questions. The number of defenders and the duration describe the response, not how many attacks it stopped. The technical-data exfiltration establishes a reported consequence, while the stated absence of evidence about customer records and service disruption limits what we can claim. It is serious telecom targeting, but not evidence that AI caused it or that every targeted operator had the same exposure.

In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported that actors affiliated with the People’s Republic of China (PRC) had compromised multiple telecommunications companies’ networks. The agencies said the intruders stole customer call-record data, accessed private communications belonging to a limited number of people—mainly those involved in government or politics—and copied some information subject to United States law-enforcement requests. An October FBI-CISA statement had already confirmed unauthorized access to commercial telecom infrastructure and assistance for affected companies and potential victims. The disclosures do not establish the full forensic timeline or how long the access went undetected; they do not report AI use in this activity.

## Count the right thing

The European Union Agency for Cybersecurity (ENISA) counted 30 cybersecurity incidents in an open-source intelligence (OSINT) overview. A separate annual summary contained 188 significant-incident reports submitted by national authorities. That set also includes service outages, system failures, human error and natural phenomena. The collections use different inputs and definitions; they are not a combined total or comparable rates.

The OSINT overview shows publicly reported cyber activity, not every telecom intrusion. The authority-submitted reports capture continuity-impact events under a reporting framework, not just hostile campaigns. Each dataset can help frame a different question, but neither estimates an operator’s local exposure or tells a CISO which project to fund.

## Turn an observation into a local priority

A supported threat observation becomes useful when it changes a local decision. The FBI-CISA disclosure describes access to communications and call-record data, but does not identify a specific operator’s identity path, initial access mechanism or logging gap. The right response is not to guess which control failed. A concrete first priority is to find out whether your own teams can identify which human or service identity accessed sensitive records, what it queried or exported, and when. Map the systems that hold those records and the management paths that could reach them. Then check whether the records let incident responders follow a query or export back to a principal and whether the service owner can keep the investigation from disrupting network operations.

That check can lead to different investments. If the data owner and security team can already trace sensitive queries to named principals and investigate them through a separate operational view, the next priority may be reducing unnecessary access or correcting a confirmed exposure. If a shared service identity can read several stores and the logs cannot distinguish its callers, invest first in identity separation and attributable records. If only one service lacks reliable event coverage, fix that boundary rather than buying a broad “AI detection” capability that does not address it. These are conditional operator choices, not claims about how the disclosed intrusions occurred.

The Singapore disclosure supports a related but different question. Because the public account reports exfiltration of network-related technical data, an operator can review which engineering and management paths expose such data and whether unusual access can be investigated. The reported absence of evidence about customer-record access and service disruption must remain part of the account. It does not prove that those outcomes are impossible in another network, and it does not justify saying the campaign caused an outage.

The AI label should change the priority only when reliable evidence shows that AI materially changed a task, access path, timing or consequence and that difference would alter the operator’s control or response. Until then, correct known access and visibility gaps on their own merits. If later evidence links AI to a specific step, ask whether it changes the telemetry, response window or access boundary the operator needs. Attribution can refine the work; it is not a reason to postpone a fix for an exposure already confirmed locally.

Threat reports set the context. Local evidence sets the investment: which identity can reach the sensitive target, what the team can see, and which control or service decision would change the exposure. Chapter 3 follows that authority path to the target.

# Chapter 3: Follow Authority to the Network Target

A radio application can create a network-control risk without being called an AI agent. In a 2024 peer-reviewed study, researchers built an experimental Open Radio Access Network (O-RAN) H-Release environment and found missing access controls for xApps, applications deployed on an O-RAN controller. They demonstrated three attacks through application programming interfaces (APIs) and the E2 interface, including attacks that disrupted radio access network (RAN) components. This was a lab result, not proof that a carrier’s production network has the same path. It leaves a practical question: which identity can reach which target, through which interface, and what can that target do?

The study did not test a large language model (LLM)-based agent; the applications were not automatically AI agents. The weakness was not bad model advice, but insufficient control over what an application could reach through network-management interfaces. That distinction still matters when a language model joins an operational workflow. It may reason about a change, but a runtime must call a tool, the tool must use a credential, and an API must accept the request before the target can alter the network.

What matters is the authority each step in that chain carries.

## A useful NOC task, a wider identity

**Illustrative scenario.** Consider a fictional telecom Network Operations Center (NOC) that uses an assistant to summarize alarms, draft ticket updates, read neighboring-domain context and prepare supplier cases. Analysts value it because they can compare information from several consoles without losing the service thread. The assistant is meant to help with triage and documentation, not to change monitoring configuration.

For this educational walkthrough, assume the assistant reads alarm telemetry, ticket text and a neighboring-domain summary. It calls separate alarm, ticket and supplier-case connectors, but those connectors rely on one shared service identity. The identity can read across domains, submit cases and reach a monitoring target that accepts alarm-routing changes; it can also reach edge nodes and part of the core.

A stale ticket note says to suppress duplicate alarms during maintenance. The assistant treats the note as current and drafts a routing change that could hide alarms. The proposal omits the note’s age, so a reviewer submits it through the normal change path. The target acknowledges it as accepted and queued, and a routine change-monitoring alert surfaces the audit record. At this point, completion is unknown. The scenario assumes no independent alarm-read path has yet been verified. These are fictional assumptions, not an incident, an observed test or a measured outcome. The precise connector scopes, target enforcement, event records and queue behavior are not facts about an operator.

The normal path explains both the value and the risk. An analyst asks for a summary of a noisy service issue. The runtime retrieves alarm records, reads the ticket history and adds a neighboring-domain summary. It gives the analyst a short account of what changed and prepares a ticket or supplier case. The analyst spends less time moving between records and can focus on whether the service is affected. That is a plausible operational benefit; this example does not measure it.

The same path crosses several authority boundaries. The request begins with a person, but the runtime decides which tools to call. The connector translates that request into an API call and presents the shared identity. The target may see only that principal, not the original analyst, the summarization task or the reason the data was retrieved. If the target allows the shared identity to change alarm routing, the account’s authority extends beyond triage even when the assistant was intended only to summarize.

This is why data and permission must be examined together. Ticket text can be stale, incomplete or wrong. It can also contain language that looks like an instruction. The model may treat retrieved text as relevant context and turn it into a proposed tool call. That content does not grant permission. But if the connector has a credential that the target accepts for a consequential operation, a mistaken interpretation can become a request the network is allowed to process. A human review step helps only if the reviewer sees the exact target, change, source and freshness of the evidence before submission.

The stages matter. A model-generated change proposal is not a submitted request. A connector call is evidence that something was sent toward the target, but may fail before it arrives or may be retried. A target response marked accepted or queued establishes that the target received and recorded an operation under its own semantics; it does not establish that the operation ran. A completed state change requires evidence from the target’s resulting configuration or state, checked against the service view. Do not collapse these stages into “the assistant changed the network.”

The logs have different limits too. Runtime records may show the prompt, retrieved context and proposed tool call, but not whether the target accepted it. Connector records may identify a credential and request identifier, but not the human intent behind a shared identity. Target audit records may show acceptance and queue status, but omit the ticket text that influenced the model. A configuration snapshot or state query can show a changed value, but not whether alarms still reach the right NOC view. Correlate event identifiers and timestamps across the layers, then compare target state with an independent operational signal. If one link is missing, state exactly what remains unknown.

The recommendation under these assumptions is to keep the assistant at read-and-draft scope and keep configuration changes in the established human change process. Do not give the assistant a shared identity that reaches both edge and core simply because the summarization task is useful. Network Engineering and the platform owner should identify whether the target supports separate, task-limited identities. If it does, test an edge-only read path and a denied core or write request against the actual target. If the platform cannot separate these permissions, a gateway may help only when every route passes through it, it blocks the prohibited operation, and failure does not reopen the broad path or remove required support. A diagram is not proof of enforcement.

Separate target identities reduce the amount of authority carried by each principal, but migration has service consequences. Running old and new identities in parallel can reveal missing permissions, while extending the period in which the broad account remains usable. Retiring the old account first shortens that overlap, but may interrupt monitoring or supplier support. A staged move takes longer and gives each workflow a chance to be checked before the shared account is removed. A temporary restriction can buy time, but it is useful only if the target enforces it and the NOC retains an approved way to operate.

## From influence to permission

Data can influence an agent without carrying a credential. A tool can hold a credential without making every model output executable. And a target can reject a request even when the model and connector agree. These are separate boundaries.

The peer-reviewed AgentDojo benchmark illustrates the first boundary. Researchers used simulated tool environments to test how instructions hidden in third-party data could influence an agent. They demonstrated an indirect prompt-injection mechanism: data returned by a tool can be treated as instructions and redirect later tool use. The benchmark does not test telecom systems, measure how often this happens at operators or show that an injection changes network state by itself.

For an operator, the question is not whether retrieved content is “trusted” in the abstract. It is what the workflow can do after reading it. A ticket summary is different from a tool call that can submit a change. The target must enforce the action limit even when the model or runtime is wrong.

Zero Trust and identity governance answer different questions. The United States National Institute of Standards and Technology (NIST) describes Zero Trust as moving protection away from static network perimeters toward users, assets and resources. Its Special Publication 800-207 describes an architecture; it is not a telecom rule. Identity governance helps establish who owns an account and how its privileges change. Neither label shows that a connector stays within the target’s policy. Identify the enforcement point.

Apply the same discipline to the workflow map. Follow who starts the task, which identity it uses, what records it reads, which connector it calls, what target decides and which service could be affected. If the target sees only a shared account, say so. If logs show a request but not the resulting network state, the outcome is unknown. Operators do not all have the same path; each needs to trace its own.

Chapter 4 follows the accepted, queued request in this scenario. It asks what the team can establish, which parts of the path it can contain, what the NOC can still see and what evidence is needed before restoring even a limited capability.

# Chapter 4: Prove Safe Authority and Service-Safe Response

A diagram can show where an agent is supposed to stop. It cannot prove that the target will stop it.

Chapter 3 followed the NOC assistant from an alarm and a stale ticket note to a request accepted into a target queue. Now the question is what the operator can observe and control. A design review shows where approval is meant to happen. A benchmark tests a model on defined tasks; a lab tests an API in one configuration; a tabletop shows how people respond. Each helps in a different way. None, on its own, proves that the live service is safe or recoverable.

## Detect and reconstruct the action

The change-monitoring alert surfaces the target’s audit record: the alarm-routing request was accepted and queued. That is the first confirmed response, not proof that the routing changed. The incident lead should preserve the request identifier and correlate it across the assistant runtime, connector and target. The runtime may show the ticket text that influenced the proposal; the connector may show which principal sent the request; the target may show receipt, acceptance and queue status. Each log answers a different question.

They may not establish who supplied the misleading instruction, whether the reviewer understood that the ticket note was stale, or which service the target’s status label covers. A shared account can be attributed to a principal without identifying the person or workflow behind it. A successful connector call does not prove the target accepted it, and target acceptance does not prove completion. The team should ask the platform owner what “accepted” and “queued” mean in this target, then verify the current routing configuration and the alarms reaching the NOC. If those records cannot be correlated, say that the operation’s state is unresolved rather than treating the assistant’s explanation as authoritative.

The first response should preserve evidence and prevent more harmful requests. Stopping the runtime can prevent that process from starting another tool call. It does not necessarily invalidate credentials already issued, terminate a session already open at the target, or cancel an operation the target has accepted. Credential revocation is a separate step: it can prevent new authenticated requests under that credential, but it does not by itself end every existing session or remove accepted work. The team must manage those states at the connector and target, then verify what happened.

If the target supports cancellation, use its documented control for the queued operation and confirm the operation’s final status. If it cannot cancel accepted work, do not assume that revocation will stop it. Block further writes through a target-side rule or other independently enforced control if one is available, give the network owner the operation identifier, and monitor the target state until the request is complete, blocked or otherwise accounted for. If no control can guarantee that it will not run, treat it as capable of completing. Avoid an improvised rollback: a second change can deepen a service problem or reverse a legitimate operation. First establish what the target did and what the service requires.

## Choose containment with the service in view

The shared identity makes containment a service decision as well as an access decision. If the target can deny alarm-routing writes while preserving the assistant’s approved reads, and that denial has been verified, the NOC may retain a narrow read path while the response team disables submission. The same can apply to supplier-case submission if it is not required to manage the immediate service. This is less disruptive than revoking the entire principal, but only if the target enforces separate permissions and the write path has no bypass. A connector setting that merely hides a button is not enough.

An independent alarm view changes the choice. If a separate, tested path provides authoritative alarms, the team can revoke the broad identity without losing its service picture. The NOC can continue through that path while the assistant, connector and target sessions are contained. If no independent view has been verified, do not treat the assistant’s own summary as a fallback. Keep a read path only if the target can enforce read-only authority and the response team can verify that it does not also permit the queued change. Otherwise, the whole identity may need to be disabled. That will interrupt cross-domain reads and supplier cases, and may place the NOC in a degraded mode, but keeping a write-capable principal active solely to preserve visibility leaves the risk in place.

The choice depends on the evidence and urgency. A request that is still only a proposal calls for a different response from a target-accepted operation that may execute. If the operation is queued and the target cannot cancel it, containment should address both new requests and the existing queue. If the team finds that the change has already completed, service owners must assess the live routing state before deciding whether to restore the previous configuration. A stop at the assistant is useful, but it is only one action in a larger containment sequence.

## Work in degraded mode, then restore carefully

Under the scenario assumptions, no independent alarm-read path has yet been verified. Network Operations therefore should not claim normal visibility while that path is being established. If an existing manual view or separate telemetry route is available, use it and confirm that it reflects current service state. The NOC can continue triaging the alarms it can verify, updating tickets manually and requesting network changes through the established approval path; a supplier case should use a separately authorized human route where one exists. If no authoritative view is available, state that visibility is degraded, prioritize only the services the team can still verify and escalate decisions that depend on unseen state. The work will take more operator attention, and some diagnostic context may be unavailable. That is a real service cost, not a reason to let the assistant retain unbounded write authority.

Before restoring anything, check the target’s operation record, current routing configuration and live alarm delivery. Verify separately that new requests under the revoked credential are denied, that existing target sessions have been ended or restricted, and that accepted or queued work has been cancelled, blocked or otherwise accounted for. If cancellation is unavailable, retain the operation identifier and continue monitoring until the target state is clear. A successful revocation command is not proof of any of these other conditions.

Restore the smallest useful capability. In this case, that means first establishing an independent NOC view, then testing a new task-limited identity for approved alarm reads. Confirm that the read works, that a prohibited routing change is denied at the target, and that the logs identify the principal and resulting state. Ticket drafting can return after its data sources and approval path are clear. Keep configuration changes and supplier-case submission in the normal human process until separate identities and target-enforced limits are demonstrated. If the platform cannot separate those permissions, do not return the shared identity to the assistant.

A finding could change this recommendation. If target records show that the request never reached the target, the team does not need to restore or roll back a change that did not occur; it still needs to correct the stale-data and permission path. If the queue can be cancelled and the target confirms no state change, the response can move from urgent containment to a bounded redesign. If the independent alarm view fails to provide authoritative state, the service owner must reconsider the degraded-mode plan before restoring read capability. If a target-native identity can enforce reads while denying writes and its logs make the principal attributable, a limited assistant read path becomes reasonable to test. If any write succeeds through that identity, return to the last verified state and keep submissions outside the assistant.

## Test what the network enforces

A convincing demonstration is not proof that the live path is controlled. The connector may still hold broad credentials; an approver may not see the exact target and action; a mock API may refuse a request that the production target accepts under another identity. Test the intended path with the identity and target that make the final decision.

Compare a request that should pass with one that should fail. An alarm-read identity should return approved data but be denied a change to alarm routing. The logs should show which identity called the target, what it accepted or refused, and whether network or monitoring state changed. Try the denied request through alternate connectors and service accounts too. One blocked route does not prove the boundary if another still reaches the target.

Test the stop with work in flight. Start an approved request, stop the runtime and revoke its credential. Then verify separately whether the connector retries, whether new authenticated calls are denied, whether an existing target session remains, whether queued work completes or can be cancelled, and what state the target reaches. Stopping one component does not stop the next automatically. Record the software, identity, target and conditions tested; a later connector or policy change may invalidate the result.

The O-RAN study in Chapter 3 and the AgentDojo benchmark can help teams choose test cases. One exposed access-control weaknesses in a research testbed; the other demonstrated indirect prompt injection in simulated tool environments. Neither establishes how often those weaknesses occur in a carrier network or whether a particular operator blocks them. Use them to ask better questions, not to claim that your control passed.

Every test has limits. A paper review may reveal an omitted identity. A benchmark probes only its defined tasks; a lab shows behavior in that environment. Production observation can support a bounded live result, but only if the conditions and denominator are recorded. A tabletop shows how people decide and communicate. These forms of evidence answer different questions; none covers them all.

## Make recovery part of the decision

When a workflow is isolated, someone must check what changed in the network and what the NOC can still see. The incident lead coordinates containment; the service owner understands the impact and restoration constraints. The executive accountable for the service decides within delegated authority. If that authority does not cover the service, or the remaining risk exceeds appetite, escalate it. An approval screen cannot stand in for an authorized decision.

A fallback works only if the people who need it can see authoritative service state, have the right permissions and know what to do. “A human can take over” is not enough. Confirm the alarm source, manual change route, supplier support and on-call roles before the assistant becomes operationally important. A fallback that depends on the same identity, connector or supplier is not independent.

Pausing a risky workflow can cost the team visibility. Leaving broad authority in place can cost security. Separate the action path from the service view whenever possible. If they cannot be separated, state the service impact and agree the fallback before choosing, unless evidence of imminent misuse requires immediate containment and a deliberate degraded mode.

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

Spend next year’s limited capacity first on workflows that need safer limits and a better recovery path. Let service impact, not the AI label, set the order. If a workflow stops, the NOC must still be able to see the service.

Supplier roadmaps cannot decide what your teams can fund or which risks management can accept. Those are local decisions, grounded in service consequence, authority, evidence and the work that must move.

## Choose priorities from local evidence

Start with four candidate work areas:

1. **Map consequential workflows.** Identify what is live or planned, which service it touches, what data it reads, and which identity, connector and target it uses.
2. **Bound and test target authority.** Show what the target permits and denies, how it attributes calls, and treat response as separate checks: can new authenticated requests be prevented, are existing sessions ended or restricted, are accepted or queued operations cancelled, blocked or accounted for, and has target state been verified?
3. **Rehearse containment and recovery.** Show how the team can limit a suspect path without losing its view of the service, then restore the smallest useful capability.
4. **Set supplier, jurisdiction and exit conditions.** Know which rules apply to the entity and service, what supplier paths and changes matter, and what service can continue if the provider or feature becomes unavailable.

These are work areas, not a default package of four projects. One test may support more than one workflow only when the identities, connectors, target and service conditions match. Otherwise, it does not prove that the other path is controlled.

Choose the number of priorities that local evidence and capacity can support. Weigh service impact, reach, urgency, dependencies, readiness, full-life cost and the work that would be delayed. Do not turn unlike measures into one score. Put high-consequence gaps and urgent exposures first. Use readiness to decide whether to test, narrow or sequence the work. When the path is unclear and the consequence is high, fund discovery. If priorities compete for one safe window, protect the service facing greater harm. The number is not a target: choose fewer if they cover the risks, or all four if each matters and teams can deliver.

Supplier and legal checks still apply to the workflows they affect, even when they are not separate projects. Keep access within the agreed boundary until the relevant data, support and legal conditions are checked. This need not become a company-wide supplier programme.

## A constrained portfolio choice

The following decision is hypothetical. It uses three existing concerns from the book: the shared edge/core identity, the NOC assistant and the deferred live-core patch. It is not an operator plan or a report of a successful control.

Assume the local platform team has confirmed that the live-core service uses the affected version and is reachable, and that a supported patch is available. The next supported change window is three weeks away. The patch example does not establish that any real operator has this exposure; the local confirmation is an explicit planning assumption for this comparison. Also assume that no interim technical control has yet been verified for this path, so the remaining exposure cannot be counted as reduced. The service is high impact and must remain within its approved availability limits. The earlier patch example records service-level acceptance of residual risk but does not identify the accepting role; in this decision, the accountable service executive should own that exception within delegated authority and review it until the change.

For capacity, assume the operator can run three preparation activities at once: NOC/platform owners establish the alarm view, Network Engineering prepares the patch and identity design, and a separate feature owner with Procurement reviews the supplier diagnostic path. Assume the patch, identity work and diagnostic feature have separate supplier arrangements; no shared supplier constrains the order. The patch and the shared edge/core identity migration each require the same single production network change window in this exercise, and cannot safely be combined: they have different service checks and rollback conditions, and coupling them would make it harder to identify which change caused a service problem. The alarm-view work and supplier review do not use that window. Also assume the assistant’s connector route can be held separately from the human change process, but treat that as an interim control only after the target or an enforced gateway confirms the write block and no bypass. These constraints are illustrative, not an industry benchmark.

The first workstream starts the independent alarm view. It must use a path that does not depend on the assistant’s shared identity or the same connector. NOC and platform owners should establish what authoritative state it can show and how a person can use it during degraded operation. Until that path is verified, revoking the shared identity could remove useful reads as well as unsafe actions. This work does not fix the patch exposure, but it gives the response team a safer option if it must isolate the assistant.

In parallel, Network Engineering prepares the supported patch: confirm the deployed version and reach, obtain the vendor-supported change and rollback conditions, and check how the change affects the service and its monitoring. The production window is reserved for the patch under these assumptions because the local exposure is confirmed, the consequence is high and no interim control is verified. This is not a claim that the patch will succeed. Readiness work and the safe change itself still need evidence; an unsupported emergency change is not automatically safer.

The identity split also starts as design and test preparation, but its production migration waits for the next suitable window. The shared identity still reaches edge nodes and part of the core, so the residual exposure remains until the old path is retired or narrowed at the target. The interim treatment is limited: keep the assistant from submitting through that identity, preserve human changes through the existing approved route, and verify that the assistant’s connector cannot bypass the restriction. This reduces the assistant-originated path only. It does not remove the account’s broader reach for other users or supplier support, and it does not patch the live-core system. If the operator cannot separate the assistant’s route from necessary human support, that service consequence must be decided explicitly rather than hidden in the access change.

The supplier diagnostic feature is not given a production expansion in this portfolio. Its known behavior is that it reads topology and proposes actions; its execution authority is not established. The feature owner can review its identity, data path, target and disablement options in parallel, but the review is not counted as a completed control. Until the evidence is available, do not feed its proposals into an execution path or grant it additional data or authority. If the feature is already active, do not assume that withholding expansion removes its existing access; document the remaining path and use a supported restriction only when its service effect and enforcement are verified.

A plausible alternative is to use the only change window for the identity migration first. That would reduce a broad authority path sooner, and it would be the better choice if the assistant could still submit unbounded changes or if the identity had already been used for an unauthorized core operation. Under the stated assumptions, and once the target or enforced gateway confirms that the assistant’s write block has no bypass, its submission path can be held outside the production window while human operations continue. If that verification fails, the identity work moves forward rather than waiting for the patch window. The live-core exposure remains until the supported patch; using the window for identity separation would leave that confirmed exposure in place for another change cycle. The interim restriction is not treated as a substitute for either the patch or the eventual identity split.

The order changes if the facts change. If local version and reach checks show that the patch does not apply, or a supported and tested interim control materially reduces the exposure, use the window for identity separation. If the assistant’s write path cannot be blocked without disabling necessary service support, or logs show that the shared identity can make a core change outside the approved route, containment and identity work move ahead. If the diagnostic feature can write to a sensitive target, its authority review moves forward as well. If patch testing reveals an unacceptable service effect or no supported rollback, do not force the change; return to the service executive with the remaining exposure, available restrictions and the decision required.

The CISO can defend this choice without claiming a universal ranking: establish independent alarm visibility now, prepare both engineering changes in parallel, use the only safe production window for the confirmed live-core patch, and schedule identity separation for the next supported window. Keep the assistant away from the shared write identity and hold the supplier feature to its verified scope. Record the residual exposure during the delay, name the executive authorized to accept it, and reopen the decision when local evidence changes.

## Put one decision in front of the board

The board oversees risk appetite, resources, escalation and assurance. Management owns delivery and service risk within delegated authority. The CISO gives separate security advice. A board update or approval button cannot prove that the target enforces a boundary or that the service can recover. Funding a map and test does not approve more production authority.

Use a one-page brief to ask directors for capacity to fund the priorities justified by local evidence. For each one, answer four questions:

- **What are we funding?** Name the service and workflow, the accountable executive and the CISO’s separate advice.
- **What will count as proof?** State which target requests should pass or fail, what logs or resulting state will show it, and what remains unknown or out of scope.
- **What will it cost and displace?** Give the full cost over the system’s life, its basis, capacity and change windows, and name the work that will move. Use `[local budget]`, `[work-item ID]` and `[change window]` where details are not yet set.
- **How will the service keep running?** Name the fallback, who may accept risk within their authority, and what change or evidence will trigger a new decision.

Do not promise return on investment (ROI) without a local baseline, a fair comparison, a quality measure and the full operating cost. A faster workflow may still need correction and supervision. A target-denial test measures security, not productivity. Keep those results separate. Label each figure as a supplier quote, internal estimate or unknown; show one-time, recurring and exit costs separately where possible. For a missing value, name who will obtain it or write `[estimate pending]`. A blank is not zero, and it need not delay the first local decision.

Ask management to fund the selected work, keep write access within the tested boundary, and prove that the service fallback works before expanding. Return for a new decision if those conditions change. Do not ask directors to approve “AI” as a category.

## What should change the order

Reopen a priority when new evidence changes the service decision. A newly confirmed route to a sensitive target may bring boundary work forward. A supplier change to identity, data handling, support or updates may require an earlier review. If an exercise finds that the fallback shares an identity with the system under review, reassess the recovery path before expanding. Legal should check any change in the rules against the affected entity and service.

Threat reports can prompt a local check, but an AI label alone does not set the priority. Compare the reported technique with local exposure, telemetry and service impact. Do not expand simply because a project reached a milestone or a supplier announced a feature. Keep the approved scope and say what evidence is still missing. A lack of reported incidents does not show that the boundary works.

At the next planning meeting, choose the first consequential workflow whose authority or service dependence you cannot yet explain. Name the evidence that would change your decision, the work that can start now, and the service cost of anything that must wait. The NOC assistant is one example; another operator may need to begin with a management identity, a supplier path, a deferred patch or a different workflow with greater local consequence.
