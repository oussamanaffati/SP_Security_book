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

When leadership asks its chief information security officer (CISO) to pause a workflow that uses artificial intelligence (AI), the request may be sensible. The network team may still need the same data feed, supplier console or alert path to see what is happening to a service. Leaving the workflow in place without a proven boundary creates another risk. This is the practical tension at the centre of the book: a pause can reduce one exposure and remove visibility or support needed to operate the service.

The answer is not to ban every model or to trust a supplier’s assurance. It is to understand the whole workflow. What data can it read? Which identity and connector does it use? What can it recommend, draft or change? Where does the target enforce permission? What remains visible when the workflow is stopped, and who can restore the service?

That is a service-provider security question, not only an AI question. An operator’s decision sits inside a service with dependencies, operating teams, suppliers, jurisdictions and supported change paths. A control that looks simple in a product demonstration may be difficult to remove from a live operating process. Conversely, a production label does not tell a CISO what a system can change, how widely it is used, or whether it has improved security.

This book does not claim that autonomous agents are the leading cause of telecom incidents. Public evidence shows different stages of deployment and different kinds of reported outcome. Public incident disclosures establish serious telecom targeting, but the sources reviewed here do not establish AI use in the named events. Those limits matter. A productivity claim is not proof of security effectiveness. A threat report is not proof of local exposure. A successful test supports only the path and conditions it actually exercised.

The chapters follow the decisions a CISO or chief technology officer (CTO) needs to make. Chapter 1 separates deployment stage, authority and outcome. Chapter 2 examines telecom intrusion evidence without assuming an AI cause. Chapter 3 follows identity, data, tools and permission to the network target. Chapter 4 asks what has been tested and whether the operator can contain and recover without losing the service view. Chapter 5 connects legal duties to supplier dependencies and exit. Chapter 6 turns those decisions into a small investment agenda for the next twelve months.

Read the book in order if you are building a common risk view. Each chapter uses the evidence and decisions established before it. If you are preparing a particular decision, start with the relevant chapter. Then return to Chapter 6 to make the service owner, evidence gate, dependency, cost, displaced work, fallback and residual risk explicit. The examples attributed to operators remain bounded by what their sources say. The four composites are illustrative prompts, not reported incidents, customer stories, or tests that were performed.

The aim is practical. A telecom CISO should finish able to distinguish a live deployment from a demonstration or plan. They should trace what a workflow can read and change, then decide what authority to permit or restrict. They should be able to test service-safe containment and recovery, and identify consequential supplier and jurisdictional dependencies. Finally, they should choose three or four priorities to explain to the chief executive officer (CEO) or board. The final decision should name what is known, what remains uncertain, who owns the service and the risk, and what evidence would change the recommendation.

# Chapter 1: What Is Actually Deployed?

Deutsche Telekom’s February 2026 release says its Radio Access Network (RAN) Guardian Agent is live in production in Germany. The company reports that it autonomously triggered more than 100 remediation actions in its first month, during Christmas-market events. It also says the time to manage major events fell from hours to around a minute.

That is a useful claim. It names an operator, a workflow, a geography and an action. It is also the beginning of the conversation, not the end. The release does not say how many events sit behind the time comparison or how it measured the time. It gives no success, override or rollback rate for the actions. “More than 100 actions” tells us activity occurred. On its own, it does not tell us how often the actions were right, what service outcome followed, or whether the result would hold across the network.

A CISO should not dismiss the example because the measurement is incomplete. Nor should a production label turn it into proof of network-wide autonomy, better service or lower security risk. The useful question is narrower: what exactly is being used, where, with what authority, and what does the evidence show?

## Start with the workflow, not the AI label

“AI” is not a unit of deployment. An operator may encounter very different AI jobs: gathering operational data for a summary, suggesting a next step, or triggering a remediation action. Each needs its own evidence and authority limit.

A practical way to describe any claimed use is with verbs: gather, classify, summarize, recommend, approve, change, verify. Then identify the person or system responsible at each step. Does the tool only present information? Does a human approve the proposed action? Can it issue a command itself? Which system enforces that command, and what service could be affected?

This is more useful than asking whether a product is “agentic.” The label does not tell you whether the workflow can read operational data, write to a network target, or merely prepare a recommendation for someone else. It also does not tell you what happens when the data are incomplete or the recommendation is wrong.

The deployment stage and the action authority are separate questions. A system can be deployed to gather operational data and recommend next steps without a source establishing that it changes network state. A commercial-network validation can happen while real-time application is still being developed.

For this chapter, use the stage words plainly. An **announcement** describes a plan or intention. A **proof of concept** shows a design or workflow in a demonstration. A **pilot** tests a bounded use in a limited setting. **Limited production** means live use in a defined part of the operation. **Production** means the operator says the system is in live use, but the footprint still needs to be stated. **Scaled** should mean a documented spread across a defined set of sites, users or operations—not a stronger adjective attached to “production.” These are working labels, not a universal industry standard. Each describes stage, not effectiveness.

## The number is only as useful as its measure

One New Zealand says it has deployed Network Concierge to help analyze network-related customer complaints. The agent gathers performance data, alarms and past incidents, then gives a customer-service representative a summary and suggested next step. One NZ reports an 80 percent reduction in analysis time.

That figure describes analysis time, as the operator reports it. It is not a restoration-time measure, and it does not by itself show that complaints were resolved faster or that service quality improved. The release does not state the case count, baseline, observation period, comparison method or answer-quality rate. Without those details, the percentage is a local claim worth asking about, not a productivity result that can be compared with another operator’s.

The same release describes a separate generator-placement tool. One NZ says it was put to the test during severe weather in the South Island and that deeper integration with incident-management and field-force workflows is being explored. Keep that use case separate: guidance on where to send mobile generators is not evidence that the system controlled the network or restored service.

Orange France offers a different kind of scale claim. Its release says Mon Assistant IA (MAIA) was deployed to 3,000 sales advisers and was supporting nearly one million conversations per month. The adviser remains in control and validates proposed responses. Those numbers tell us the reported deployment reach and conversation volume. They do not tell us how often advisers used it, whether answers were correct, how much time was saved, or whether customer outcomes changed. Orange does not provide those measures in the release.

SK Telecom’s AI-RAN Parameter Recommender makes another useful distinction. The operator says the recommender was applied to its commercial network and systematically validated. It recommends base-station parameters; the same release says real-time application was still being developed. That is evidence of validation in a commercial-network setting, not evidence that the system was autonomously changing parameters across the live network. “On the commercial network” and “in autonomous production” are not interchangeable descriptions.

Put these claims in one column called “AI deployed” and the differences disappear. Keep the workflow, stage and measure beside each other. A production remediation action, a reduction in analysis time, conversation volume and commercial-network validation are four different kinds of evidence. They are not a sequence of increasing maturity. None of these examples demonstrates reduced cyber risk or independently measured return on investment.

It is easy to let these measures blur together. Adoption is not effectiveness. A count of conversations, actions, advisers or sites measures reach or activity. A productivity claim needs a defined task and a defensible comparison, including the human review and rework that remain. A service-quality claim needs a service measure, such as correctness or customer impact, not just tool usage. A security claim needs evidence about the control or threat outcome. A return on investment (ROI) claim needs costs and benefits measured on a comparable basis. A result in one category does not prove a result in another.

“Production” is still important. When an operator says “production,” it is a claim that the system has crossed beyond a presentation or a test. It does not tell a buyer or board how widely the system is used, what it can change, how often it fails, or whether staff can stop it. It also does not show whether its benefits exceed its costs. Those are separate claims. Ask for separate evidence.

## A claim check for the next meeting

When a supplier or executive says “we have deployed AI,” write down the answer to these questions:

1. **Which workflow?** Name the operational task, service domain and people who use it.
2. **What stage and footprint?** Is it announced, demonstrated, piloted, live in a bounded operation, or scaled? How many sites, users or cases are actually covered?
3. **What authority?** Does it gather information, recommend, prepare an approved change, or execute one? Which target enforces the action?
4. **Who is making the claim?** The operator, supplier, analyst, survey respondent or telemetry provider? Is the result independently measured or self-reported?
5. **What does the metric count?** State the unit, denominator, baseline, period and comparison method. Include errors, overrides, rework and service impact where relevant.
6. **Which outcome does it support?** Adoption, productivity, service quality, security effectiveness, revenue or net ROI? Do not let evidence for one stand in for another.

If the answer to a material question is missing, record it as unknown. Do not turn missing evidence into a negative finding, and do not fill the gap with a stronger label. That is the difference between taking a deployment seriously and treating a claim as proof.

# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort to counter intrusion activity against the telecommunications sector. It said all four major operators had been targeted. The operation had spanned more than eleven months and involved over 100 cyber defenders.

That is a serious account of coordinated threat response. The duration and defender count describe the operation’s scale, not how many threats were stopped or what service impact was avoided. The report does not attribute the activity to AI, nor establish that AI was not used. Those are separate claims. It tells us about targeting and the defensive operation; we should not make it carry a conclusion about the attackers’ tools.

This distinction is easy to lose when a threat briefing starts with a technology label. “AI-enabled attack” sounds like a separate class of event, perhaps one that demands a separate response. The label can hide questions that matter to an operator. Which service or system was reached? What identity or access path was involved? What did the intruder do? What information or control was exposed? What could the operator see and safely change during the investigation?

A United States disclosure gives the threat picture more detail. In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported a compromise of multiple telecommunications companies’ networks. They attributed the activity to actors affiliated with the People’s Republic of China (PRC). The agencies said the access enabled theft of customer call-record data and access to private communications of a limited number of individuals, primarily people involved in government or political activity. They also reported copying certain information subject to United States law-enforcement requests. An earlier October statement from the FBI and CISA confirmed an investigation into unauthorized access to commercial telecom infrastructure and described assistance to affected companies and potential victims. Neither statement attributes the activity to AI.

The disclosed access matters whether or not AI was involved. Nor does the disclosure establish every detail an operator would want for a post-incident review. A public statement is not a forensic image, a complete intrusion timeline or a measure of how long an adversary remained undetected. It is evidence of what the issuing agencies chose to state at that time. Keep both halves of that sentence: the disclosed access matters, and the undisclosed details remain unknown.

## Count the right thing

Even the word *incident* can conceal different evidence. The European Union Agency for Cybersecurity (ENISA) counted 30 cybersecurity incidents in its 2024 open-source intelligence (OSINT) overview. A separate ENISA annual summary contained 188 significant-incident reports submitted by national authorities. Those reports include service outages and system failures as well as malicious actions, human error and natural phenomena. The two figures come from different collection systems and answer different questions. They cannot be added into a single incident count or compared as rates.

That distinction matters in an executive room. The OSINT overview can show that publicly reported cyber activity exists; it is not a census of every telecom intrusion. The authority-submitted dataset describes significant continuity-impact events under a reporting framework; it is not a catalogue of hostile campaigns. The report’s own Member State total is inconsistent between sections, so there is no reason to repeat that disputed number in a board paper. None of these limits erases the incidents. They tell us what conclusions the data can carry.

Now ask what an AI label adds. A threat actor may use an AI service during a campaign without the service being involved in a specific telecom intrusion. A model may assist with a task without causing access, persistence or impact. A report may describe a system as “AI-enabled” without showing whether AI changed the outcome. These are different claims, and they need different evidence.

A simple proof ladder can keep the claims separate. First, is AI mentioned at all? If not, the incident account is silent; silence is neither proof of use nor proof of non-use. Second, is there evidence that a named actor used an AI tool somewhere in a broader campaign? That establishes a reported tool-use observation, not its role in a particular operator incident. Third, can investigators connect the tool to a specific action in the intrusion, using evidence from that event rather than a general capability claim? Finally, what did that use change: the task performed, the time or scale, the access obtained, or the operational consequence? A report that reaches one rung does not automatically reach the next.

This is not a forensic standard or a new threat taxonomy. It is a way to stop a weak inference from becoming a budget decision. The test is not whether an attacker could use AI. The test is what the source establishes about this actor, this operation and this target, and what the operator needs to do whether or not the label is true.

## Prepare for the path, not the headline

For a service provider, the practical work begins with the systems and relationships that can turn access into service impact. Which management, identity, supplier or remote-support paths can reach sensitive network functions? Which customer, signaling, location or operational data sets would matter if read or altered? Where can responders obtain authoritative state while an investigation is under way? Which changes can be made without destroying evidence or creating a second outage? These are local questions. A public incident disclosure rarely answers them for your estate.

That does not mean AI is irrelevant to the threat model. It means the AI question should be attached to a concrete step. Ask whether the evidence connects an AI tool to a specific step in the incident, or merely records that a tool was used somewhere in the broader activity. If an operator-side workflow called an external model or agent, could your logs connect the principal and input to the destination and resulting action? Then ask which detection or response decision would change. If none would, the AI label may be descriptive rather than operationally useful.

The inverse is also important. Do not wait for proof of AI use before fixing a known exposure. A credential that can reach a management interface, an unobserved supplier path or an internet-facing system with a supported fix is relevant on its own. Attribution can improve understanding, but uncertainty about an attacker’s tools does not remove a defender’s responsibility for the path and service at risk.

When the next briefing calls an event “AI-enabled,” ask four questions before changing the risk rating:

- What happened to the telecom target, and which source establishes it?
- What evidence connects AI to this specific operation, rather than to the actor or campaign in general?
- Which step or consequence did AI demonstrably change?
- What exposure or response action matters even if the AI attribution is later withdrawn?

If the first answer is clear and the second is not, brief the incident as a telecom intrusion and state the attribution gap. That is not minimizing the threat. It is a more defensible way to prepare for it.

# Chapter 3: Follow Authority to the Network Target

A radio application does not need to call itself an AI agent to create a network-control risk. A 2024 peer-reviewed study built an experimental Open Radio Access Network (O-RAN) H-Release environment and found missing access-control permissions for xApps, applications deployed on an O-RAN controller. The researchers demonstrated three attacks through application programming interfaces (APIs) and the E2 interface, including attacks that disrupted RAN components. That is a lab result, not evidence that the same path is present in a carrier’s production network. It points to a useful question for any automation: which identity can reach which target, through which interface? What can the target be persuaded or authorized to do?

These applications are not automatically AI agents, and this study did not test a large language model (LLM)-based agent. It matters here because it shows how authority can cross a software boundary and reach radio functions. The weakness was not a model making a poor recommendation. It was inadequate control over what an application could access through interfaces used to manage the network.

That distinction becomes essential when a workflow includes a language model. Reasoning about a configuration does not, by itself, grant a model a network identity. The surrounding runtime calls tools. Those tools may use a service account, delegated token or connector credential. The application programming interface (API) accepts or rejects a request. The target system applies its own authorization and state-change rules. The service sees the result.

The authority is in that chain, not in the product name.

## Separate influence from permission

A model can be influenced by data it reads without that data having a credential. A tool can hold a credential without every model output being executable. A target can reject a request even when a model and connector agree on what should happen. These are separate boundaries, and a useful review keeps them separate.

The peer-reviewed AgentDojo benchmark helps explain the first boundary. In simulated tool environments, the researchers tested how instructions hidden in third-party data could influence a tool-using agent’s behavior. The work demonstrates an indirect prompt-injection mechanism: data returned by a tool can be interpreted as instructions and can redirect later tool use. It does not test telecom systems, estimate how often this happens in operators, or show that a prompt injection can change network state by itself.

For a telecom workflow, the practical question is what authority is available after the data is read. If a workflow can retrieve a ticket, summarize it, and recommend an action, that is different from one that can invoke a write-capable API. If the model proposes a change, the proposal is not the change. Human approval is meaningful only when the reviewer can see the target and operation. The execution identity must not bypass that decision through another route.

This is why “human in the loop” is not a permission model. It describes a role in a process. It does not tell us whether approval happens before execution, whether the reviewer sees the exact request, which credentials perform it, or whether the target enforces the intended limit.

Zero Trust and identity governance answer different questions here. The United States National Institute of Standards and Technology (NIST) describes Zero Trust as moving protection away from static network perimeters toward users, assets and resources. NIST Special Publication 800-207 is an architecture publication, not a telecom rule. Identity governance helps answer who owns an account and how its privileges change. A model may interpret data and propose a tool call. None of those labels, alone or together, proves that a connector cannot act beyond the target’s policy. Name the enforcement point at each hop.

## Trace one real workflow

Do not begin with a list of models or a vendor’s architecture slide. Choose one workflow that matters to a service. Then follow the request all the way to the target. A table can make the gaps visible:

| Trace point | What the operator needs to establish |
|---|---|
| Request | Who or what initiates the workflow, and who owns the operational purpose? |
| Principal | Which human or non-human identity executes each step? What credentials or delegated tokens are used, and who can change them? |
| Context | Which records, telemetry or retrieved content enter the workflow? Who controls them, and which inputs should be treated as untrusted? |
| Tool and interface | Which connector, function or API is called? Is the operation read, recommend, draft or write? What targets and parameters are in scope? |
| Target | Which system makes the final authorization decision? What network state can the accepted operation change? |
| Service | Which service depends on that state, who owns its impact assessment, and where is the workflow’s authority recorded? |

The map should not end at “the model has access to operations support systems (OSS)” or “a human approves changes.” Those phrases are too broad to defend. Name the identity and permission at each hop. A workflow may read from one domain, call an API in another and affect a service owned by a third team. This does not prove that every carrier has such a path. It is a reason to trace the path in the operator’s environment rather than assume it stops at the model boundary.

Record the action level explicitly. *Read* means the workflow can retrieve information. *Recommend* means it returns a proposed action. *Draft* means it prepares a change for a separate system or person to submit. *Execute* means the workflow can submit a state-changing request under its own or a delegated credential; the target may still accept or reject it. The labels are not maturity grades. They describe different consequences and different evidence requirements.

The target matters because a successful tool call is not the same as a successful or safe service outcome. The API may accept a syntactically valid request; the network may apply it; the affected service may still be degraded. Conversely, a blocked API call may be logged by the connector but not by the target. A map that stops at the assistant’s response cannot answer what changed in the network.

CISA and international partners make a useful cross-sector recommendation: start with low-risk, non-sensitive use cases and avoid broad or unrestricted access, especially to sensitive data and critical systems. That is guidance, not a telecom-specific control standard. In an operator, “low risk” must be judged against the service, target, permitted action and fallback—not the familiarity of the model or the apparent simplicity of the task.

The map is complete when the operator can name the principal, data path, tool, target-side decision, possible state change and affected service. Anything missing is an evidence gap, not a reason to assume the workflow is safe or unsafe. Only then can the operator decide which boundary to test and which service limits must govern a response.

# Chapter 4: Prove Safe Authority and Service-Safe Response

A diagram can show where an agent is supposed to stop. It cannot prove that the target will stop it.

That difference matters when a workflow moves from recommendation to action. A design review may show a human approval step. A benchmark may show that a model resists a class of prompt injection. A lab may show that an API rejects a request. An exercise may show that a network operations centre (NOC) knows whom to call. Each is useful evidence. None, on its own, proves that the whole operator workflow is safe or that the service can be restored when something goes wrong.

The practical question is not whether a system “passed testing.” It is what exact claim the test supports, under which conditions, and what remains untested.

## Test the path that can change the network

Start with one workflow and the action it might perform. Chapter 3 mapped the identities and interfaces. Now test the actual path: the principal that runs the action, the credential it uses, the connector and API in between, and the target’s own authorization decision. A model’s answer is not the point of control if another component can still submit a change.

Test both sides of the boundary. The allowed operation should work within its stated scope. A similar operation against the wrong target, outside the permitted range, or without the required approval should fail at the enforcement point. The record should show not only what the assistant displayed, but which identity made the request, what the target accepted or rejected, and what state changed.

Then test the parts that are easy to miss in a clean demonstration. Does a delegated token remain usable after the user’s session ends? Can a queued action run after the interface says “stop”? Does a retry submit the request again? Do another connector or service account provide a second route to the same target? Can the operator distinguish a model proposal, an API submission, a target-side rejection and a completed state change in the logs?

These are not assumptions about every product. They are questions for the implementation in front of you. A stop button is evidence only if its effect is observed at the component that holds authority, including any sessions or work already in flight.

For each test, write down the expected result before running it. Name the software and policy versions, identity, target, action, data conditions and approval path. Keep the request and target-side evidence. Record what happened, what could not be observed, and what was not tested. If the evidence came from a mock API or isolated lab, say so. It can establish behavior in that lab; it does not establish production behavior on a different network or with another credential path.

This is where evidence labels become useful. A paper review can expose a missing control. A benchmark can probe a defined set of tasks and failure modes. A lab test can establish behavior in the tested configuration. A production observation can show what happened in a bounded live workflow, if the operator records the relevant denominator and conditions. A tabletop can test decisions and communication. These forms answer different questions; they are not a ladder where one automatically replaces the others.

NIST’s tool-use workshop synthesis identifies several dimensions: what actions a tool permits, its access patterns, reversibility, monitoring and the autonomy it enables. It is expert discussion, not a consensus standard or a production test. That is a useful prompt for an operator. A read-only action with good monitoring and straightforward reversal is not the same risk as a write action with broad reach, hidden sessions and an uncertain recovery path.

A benchmark can help find a weakness, too, but it cannot certify the operator’s controls. AgentDojo demonstrates indirect prompt-injection mechanisms in simulated tool environments. The O-RAN xApp study demonstrates access-control and interface weaknesses in a research testbed. Neither study establishes how often the same weakness occurs in a carrier network or whether a particular operator’s control blocks it. Use this work to choose test cases, not to claim that your own boundary has passed.

## A stop is not a recovery plan

When a test reveals unexpected authority, the first instinct may be to disable the entire workflow. Sometimes that is the right immediate containment. But stopping a workflow and preserving service are separate decisions. Disabling a connector may remove a route for harmful changes; it may also remove a useful view or handoff. Revoking one token may leave another valid. Pausing an agent may not cancel actions already accepted by the target.

The operator needs a pre-agreed response that states who can stop new actions, who can revoke credentials, who confirms the network state, and who decides when the workflow can resume. Incident command may coordinate the event, but the service owner supplies impact and restoration constraints. The executive accountable for the affected service accepts residual service risk only within delegated authority and appetite. These roles should be clear before pressure makes every decision slower.

Use the NOC-assistant composite as a bounded rehearsal prompt, not as a reported incident or test result. It raises questions about data from a neighboring domain and reduced NOC visibility. Do not assume that the assistant changed network state. Ask what the team would need to establish. Was the data boundary crossed? Could the assistant act, or only present information? Which identity made any downstream request? If the assistant is paused, can the NOC still see authoritative alarms and target state?

The purpose is not to rehearse a dramatic “kill switch” moment. It is to find the point where security containment and service operations meet. A security operations centre (SOC) analyst may identify suspicious activity. The platform team may be able to revoke a token. The NOC may know whether the affected alarms are available through another path. The service owner may know which actions cannot wait for the next change window. Those facts need to reach the person authorized to choose among isolation, narrower restrictions, manual operation or continued observation.

A service-safe response exercise should therefore include the people who can answer those questions, not only the team that owns the model. Use the actual escalation routes and after-hours cover. State what evidence is available, what is missing, what can be stopped immediately, and which changes require normal approval or an emergency change process. Do not invent a universal response-time target: set local tolerances from service obligations, operational capability and the consequences of delay.

## Make restoration part of the test

Rollback is often treated as the final line in a change plan. For an agentic workflow, it needs to be tested as an operational state transition. What is the known-good state? Can the team identify which target changes were accepted? Who confirms that dependent services have returned to their expected condition? What happens if a reversal is itself unsafe, unsupported or outside the approved window?

A non-production demonstration can show that a button or API call exists. It does not prove that the production system has the same dependencies, that the right people are available, or that a service can tolerate the reversal. Where production testing is not safe, record that limitation. Use a lab or controlled window to reduce uncertainty, then define the production evidence and operating conditions still needed before expanding authority.

The same discipline applies to fallback. “A human can take over” is not enough if the person cannot see the state, lacks the permissions, or has no supported manual procedure. Check that the fallback path is current and that the people expected to use it know where the authoritative information comes from. A safe design keeps the operator able to work when the model, connector, supplier service or network link is unavailable.

Repeat the relevant tests when the authority path changes. Examples include new tools, a different identity, a model or connector update, a new target API, or a change to approval and stop behavior. The exact trigger depends on the operator’s change process. The principle is simple: evidence about one version and one path does not silently cover a different one.

A useful test record is concise. It states what was intended and observed, what evidence supports the result, what was not tested, who owns the gap, and what condition would permit broader use. “Passed” without those details is not an assurance statement. Neither is “human approved” without showing what the person saw and what identity actually executed the action.

The CISO should ask for two separate outcomes. First, evidence that the authority boundary works for the tested actions and paths. Second, evidence that the operator can detect, decide, contain and restore without creating an avoidable service failure. A narrow test may justify a narrow permission. It does not justify broad autonomy by implication.

The result is not a certificate of safety. It is an operating decision: what may run, what needs approval, what must stop if conditions change, and what remains to be proven.

# Chapter 5: Obligations, Suppliers and Exit Conditions

In the supplier-diagnostic composite, a routine update enables a feature that reads topology and proposes actions. The composite does not establish direct execution, the feature’s identity, or whether it can be disabled independently.

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

The supplier diagnostic feature makes the distinction concrete. Its presence is established, and the composite says it reads topology and proposes actions. Direct execution is not established. The operator should not describe it as a network-changing agent. The absence of evidence for direct execution does not prove that its data path, disablement or downstream effect is safe.

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

For the supplier-feature composite, require a clear release and support path. Keep write authority outside the feature unless a target-enforced boundary is proven. Preserve the service view during investigation or rollback. Revisit the choice when the identity, target path, fallback and support arrangement are evidenced.

A legal duty sets a floor and a supplier contract sets expectations. Neither, by itself, shows who can disable a connector at 02:00, whether existing sessions terminate, or whether the NOC can still manage the service afterward. That is the operator’s responsibility to map, test and fund.

# Chapter 6: The Next 12 Months: A Defensible Operator Agenda

Pausing an agent can reduce an access risk while removing a data feed or supplier path that supports service operations. Leaving it unbounded is not a safe alternative. This chapter turns the trade-off into a portfolio decision: which work deserves priority, which evidence would justify expansion, and what the operator must retain if a workflow is stopped.

That is the decision this book has been building toward. The task is not to predict how many agents every operator will deploy, or to prove that agents are already the leading cause of telecom incidents. The task is to decide what to permit, what to keep bounded, what to stop, and what evidence would change that choice. The useful output is a small, funded portfolio tied to services, not a catalogue of products.

## Start with the service decision

A proposal to “accelerate AI adoption” does not tell the board what it is approving. A useful decision names the workflow, its stage, and the service it touches. It also identifies the authority it has, the supplier paths it depends on, and the conditions under which management will pause or expand it.

Keep three questions separate.

**What service outcome is worth pursuing?** A workflow may help an operations team interpret alarms, summarize evidence or prepare a change. The business case must state what a better outcome means for that service and how the operator will compare it with the current process. Faster output is not automatically better output. The work may move from the person who created a recommendation to a reviewer who must verify it or an engineer who must correct it. The NOC team must operate the result across shifts.

**What security control has been demonstrated?** The security case asks whether the intended identity and target boundary prevent an unauthorized action. It asks whether that action leaves an attributable record. It also asks whether the operator can stop or reverse the action within the tested scope. A deployment announcement, a productivity result, a model benchmark and a target-side denial test answer different questions. Do not use one as a substitute for another.

**Can the service continue when the workflow is constrained?** A pause is only a safe control if the operator understands its effect on visibility, support, queued work and recovery. If the workflow provides an operational view that no other team can obtain, disabling it may create a service risk. That does not justify leaving excessive authority in place. It means the service owner must decide how to preserve the view while the authority is narrowed or removed.

A portfolio should make these three answers visible next to one another. It should not hide a weak security case inside a strong business case, or a missing fallback inside a promised efficiency gain.

## Choose three or four priorities from four candidate areas

The four rows are candidate work areas, not a default package or universal ranking. Choose three or four only when local service evidence supports them; combine related work only when each has a clear owner and evidence gate. For any row left out, record the residual risk, accountable owner and trigger that would reopen it. Supplier and jurisdiction conditions remain release gates for every selected workflow they affect, even when they do not receive a separate budget line. A provider change or difficult exit can matter as much as a target permission.

Compare candidate priorities on the same evidence: service consequence, effective authority and reach, urgency, supplier dependencies, readiness to test and recover, full-life cost, capacity and the specific work displaced. Do not invent scores or give unlike measures false precision. Order first by consequence and urgency. Use dependencies, readiness and safe capacity to sequence or narrow the work. A high-consequence gap with weak evidence calls for funded discovery or a narrower scope, not automatic deferral.

| Priority | Accountable management owner | Evidence gate | Dependency and work displaced |
|---|---|---|---|
| Map the high-consequence workflows that are live or planned. | One named service executive is accountable for scope; the CISO advises on risk and sets evidence criteria. | For each selected workflow: stage, effective identity, data, connector, target, read/change authority, service effect, stop path and material unknowns. | Requires time from network engineering, platform, identity, data and operations teams. Name the specific architecture, access-review or reliability task that will move, using its local title or work-item identifier. |
| Bound and test authority at the target before expanding it. | One service executive is accountable for release; the platform owner leads testing; the CISO advises on assurance. | Evidence of allowed and denied actions at the target, correct identity attribution, logs, active-session and queued-work handling, bypass conditions, revocation and recovery. | Depends on a safe test route and, where needed, supplier support. Name the specific planned change, test window or reliability task that this engineering capacity will displace. |
| Rehearse service-safe containment and recovery. | One service executive is accountable; NOC, SOC, incident leadership and the service owner support delivery. | The team can preserve an independent service view, invoke a tested fallback, constrain the suspect path, communicate service effects, restore safely and verify the result against local tolerance. | Uses NOC/SOC and engineering time, shift cover, supplier participation and an exercise or restoration window. Identify the exercise or operational task that will move, with its local name and window. |
| Set supplier, jurisdiction and exit conditions for the selected workflows. | One service executive is accountable for continuity and release; Procurement and Legal lead contract work; the CISO advises on security and residual risk. | Applicable obligations are identified for the entity, service and role; data and support paths are known; material changes are notified; access and logs are attributable; export, termination and fallback are credible. | Requires focused legal, procurement, architecture and supplier capacity. Record the contract review or supplier-validation task that will move, using its local name or work-item identifier; limit scope to workflows that can affect priority services. |

### A hypothetical choice under a capacity limit

Assume, only for this decision exercise, that an operator can staff three of the four candidate work areas this planning cycle. No budget or cost estimate is assumed. The NOC-assistant composite raises questions about neighboring-domain data and reduced NOC visibility, but does not establish that the assistant changed network state. The supplier-diagnostic composite describes a feature enabled by a routine update that reads topology and proposes actions; it does not establish direct execution. Now add two explicit planning assumptions: the operator is considering expanding the NOC assistant, while the diagnostic feature is not planned for enablement this cycle.

On those assumptions, select workflow mapping, target-boundary testing and a service-safe containment exercise. Map the assistant’s actual identity, data and service path first. Test whether the target blocks any prohibited action before expanding authority. Rehearse a pause that preserves an independent NOC view and a supported route to service state. Defer the broader supplier-and-exit review as a separate workstream, but keep feature-specific identity, logging, disablement, fallback and applicable-duty checks as release gates before the diagnostic feature is enabled. The omitted work is delayed, not accepted as safe: name its accountable owner, record the residual risk, and set a reopening trigger.

Change the order if local evidence changes the premise. A verified supplier path to a sensitive target may move boundary work ahead of expansion. The same applies if the diagnostic feature enters a planned service workflow. Move the relevant supplier and authority work ahead of a lower-consequence selected task. If the NOC view remains unavailable without the assistant, fund the independent view before considering expansion. These are conditional choices, not facts about an operator or measured results.

Name one accountable executive for each priority. The delivery team may be cross-functional; accountability is not. The CISO advises on security risk and evidence. The service executive accepts service residual risk only within delegated authority and appetite. If an unresolved security issue exceeds that authority or conflicts with service tolerance, use the operator’s escalation route. Do not transfer acceptance to a committee or imply that board visibility settles it. Procurement and Legal establish the contract and jurisdiction facts they control. If no one can make the service decision within delegated authority, escalate rather than let a pilot expand by default.

Do not wait for a complete inventory to correct excess access that is already clear. Make the supported change while the wider inventory continues. The inventory should expose unknowns, not delay a control improvement the operator can already justify.

The second and third priorities are related but not interchangeable. A test may show that a target rejects a prohibited action. It does not show that the NOC can maintain its view, reach a supplier, or restore the service when the workflow is isolated. An exercise may show that teams communicate well. It does not prove that the target boundary blocks a prohibited call. Fund both forms of assurance where the service consequence justifies them.

Supplier work should follow the workflows that matter. A long questionnaire is not an exit plan. The operator needs to know which supplier identities, updates, data routes, support arrangements and service dependencies would change if the model, connector or cloud service became unavailable or unacceptable. Contract language helps only when the provider can use the rights in practice and the service has a workable alternative.

## Sequence by evidence, not by a vendor calendar

A twelve-month agenda needs a sequence, but it does not need an artificial deadline for every control. Service change windows, supplier support and regulatory conditions differ. Order the work by the evidence one decision needs from another.

Start by selecting a small number of workflows whose service consequence, change authority or supplier dependence warrants attention. Record what is known and what remains unknown. Do not use market adoption percentages or a supplier roadmap to decide which local service deserves the first review.

Then close clearly excessive authority and test the narrowest meaningful boundary that can be exercised safely. Where production denial would create service risk, keep write access denied and use an approved non-service-affecting route, replay or other safe method. If the real target behavior cannot be verified, record it as unknown and hold the workflow at its last verified scope. A test is not improved by placing live service at unnecessary risk.

Next, rehearse the response around the service itself. The team should know which view remains available if the workflow is paused, which independent role can act, and how existing sessions and queued work are handled. It should also know who can reach the supplier and how the operator will check that service has recovered. If the fallback depends on the same identity, connector or supplier that is under review, it is not an independent fallback.

Before widening scope or delegating a new action, establish the supplier and jurisdiction conditions relevant to that workflow. If a material condition remains unknown, keep the scope bounded or take the service-specific risk to an authorized executive. Decide which changes require notice and retesting, how logs and evidence will be obtained, how processing and support are bounded, and what happens if the operator needs to leave. A production label is not a reason to defer these questions. It makes them more consequential.

At each gate, management has three honest choices: expand within the tested scope; keep the workflow bounded while gathering evidence; or stop and return to a supported manual process. The third choice is not automatically safest. If stopping would remove service visibility or essential support, the service executive must account for that consequence and choose a supported alternative before the operational view disappears. If no safe alternative is available, the risk and the decision authority should be explicit.

## Treat the agenda as a choice about capacity

The work has a cost even when no new software is purchased. Engineering time, test environments, supplier participation, NOC/SOC backfill, legal review, training, monitoring and recovery arrangements all draw on existing capacity. The full-life cost may also include integration, model or connector changes, compute, licensing, correction effort and exit. Unknown values remain unknown until the operator measures or negotiates them. They are not zero.

For each selected priority, record the full-life cost categories, the basis for any estimate and what remains unknown. Record capacity by function and change window, then name the specific work that will move and who owns that trade-off. “Reliability work” is not enough if a particular change, exercise or maintenance window will be deferred. The service executive must understand the consequence. If the review finds no specific work displaced, say so; do not assume that capacity is free. A paper that promises extra assurance while assuming all existing work continues has not made an investment decision.

Do not promise a return on investment unless the operator has a credible local baseline, a comparison method, a quality measure and the full cost of operation. More importantly, do not let an efficiency result stand in for evidence of security control effectiveness. A workflow can produce accepted output faster and still have an unverified action path. A target can enforce a strong boundary while the service case for broad rollout remains weak. These are separate decisions.

A useful business case measures the result that matters to the service and includes the review, correction and operating effort that the workflow creates. A useful security case states which authority is reduced or controlled, what test demonstrates that effect, what remains untested, and how the operator will detect and recover from failure. A service case states what happens when the workflow, supplier or support path is unavailable. Put all three beside the cost and the displaced work.

## Keep board oversight distinct from management ownership

The board should oversee risk appetite, resources, escalation and assurance. Management should deliver the work and accept residual risk within delegated authority. A board update is not a service acceptance decision. Nor should directors be asked to approve a technical boundary that management has not tested.

The CISO can bring a concise recommendation naming the services in scope, the supporting evidence, and any uncertain boundary. It should also name displaced work and the residual risk. The CTO or service executive should confirm the service consequence, the operational tolerance and the fallback. If the recommendation exceeds delegated authority or the approved risk appetite, management should escalate the choice rather than imply that visibility alone has settled it.

A one-page board paper can summarize the same decision record for each selected priority. Leave unknowns visible; do not replace them with invented estimates. It should answer:

- **Decision and ownership:** Which three or four locally justified priorities, scope and capacity should management approve? What service does each cover, who is its accountable executive, and what security advice does the CISO provide?
- **Evidence and scope:** What target, response or supplier evidence is required? What remains unknown, and what is explicitly out of scope?
- **Value, cost and displacement:** What local service outcome is sought? What are the full-life cost basis and unknowns, capacity by function/window, specific displaced work and its consequence?
- **Fallback and reassessment:** How will visibility and recovery be preserved? Who accepts residual service risk within what authority? What evidence or change could expand, hold, narrow, stop or escalate the work?

The ask should be specific. “Approve our AI strategy” gives the board little to decide and leaves management ownership blurred. “Authorize people and change capacity to map these workflows, test target boundaries, and rehearse service-safe containment. Keep write authority bounded until the evidence gate passes.” This gives management a clear mandate. It also makes the trade-off visible: some other work must move, and the cost of that decision belongs in the paper.

## What should change the order

For each priority, name the local evidence or change that reopens the decision, who reviews it, and which actions it may trigger.

A verified reachable path to a sensitive target may move boundary correction ahead of expansion. A supplier change affecting support, access or data handling may move dependency review forward. An exercise that exposes a shared fallback identity may require a different operational path before the next test. For each change, record the evidence, decision owner and action: expand, hold, narrow, stop or escalate.

A legal change may alter applicability or ownership. Record the affected entity and service, then have Legal verify the obligation before changing the scope.

Threat reporting also matters, but an AI label alone should not move a work package to the top. A credible report about an adversary technique is a reason to compare it with local exposure, telemetry and service impact. It is not proof that the operator is affected or that a particular response time is required. Prepare for observed techniques and prioritize urgent work when local evidence supports it.

If the evidence does not change, do not expand simply because the project has a milestone or a supplier has announced a new capability. Hold at the approved scope, state the residual risk, and say what evidence is needed next. Conversely, do not use “we have not seen an incident” as proof that the control boundary works. The decision should turn on service consequence and evidence, not optimism or alarm.

## The decision to take into the next year

A defensible operator agenda is not a promise to automate more. It is a decision about which workflows merit attention, what evidence could justify wider authority, and how the service remains visible and supportable when a workflow stops.

For the next twelve months, choose three or four priorities that local consequence and capacity justify. Leave unknown cost or control behavior visible rather than turning it into a confident estimate.

The CISO and CTO do not need to approve or reject “AI” as a category. They need to decide what each consequential workflow may see and change, how the service remains supportable if it is stopped, and who may accept the risk that remains. Management owns that service decision; the board oversees appetite, resources and assurance.
