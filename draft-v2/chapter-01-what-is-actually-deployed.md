# What Is Actually Deployed?

Deutsche Telekom’s February 2026 release says its RAN Guardian Agent is live in production in Germany. The company reports that it autonomously triggered more than 100 remediation actions in its first month, during Christmas-market events. It also says the time to manage major events fell from hours to around a minute.

That is a useful claim. It names an operator, a workflow, a geography and an action. It is also the beginning of the conversation, not the end. The release does not say how many events sit behind the time comparison or how it measured the time. It gives no success, override or rollback rate for the actions. “More than 100 actions” tells us activity occurred. On its own, it does not tell us how often the actions were right, what service outcome followed, or whether the result would hold across the network.

A CISO should not dismiss the example because the measurement is incomplete. Nor should a production label turn it into proof of network-wide autonomy, better service or lower security risk. The useful question is narrower: what exactly is being used, where, with what authority, and what does the evidence show?

## Start with the workflow, not the AI label

“AI” is not a unit of deployment. An operator may encounter very different AI jobs: gathering operational data for a summary, suggesting a next step, or triggering a remediation action. Each needs its own evidence and authority limit.

A practical way to describe any claimed use is with verbs: gather, classify, summarize, recommend, approve, change, verify. Then identify the person or system responsible at each step. Does the tool only present information? Does a human approve the proposed action? Can it issue a command itself? Which system enforces that command, and what service could be affected?

This is more useful than asking whether a product is “agentic.” The label does not tell you whether the workflow can read operational data, write to a network target, or merely prepare a recommendation for someone else. It also does not tell you what happens when the data are incomplete or the recommendation is wrong.

The deployment stage and the action authority are separate questions. A system can be deployed to gather operational data and recommend next steps without a source establishing that it changes network state. A commercial-network validation can happen while real-time application is still being developed. And a pilot can operate at a real event without being a routine, scaled service.

For this chapter, use the stage words plainly. An **announcement** describes a plan or intention. A **proof of concept** shows a design or workflow in a demonstration. A **pilot** tests a bounded use in a limited setting. **Limited production** means live use in a defined part of the operation. **Production** means the operator says the system is in live use, but the footprint still needs to be stated. **Scaled** should mean a documented spread across a defined set of sites, users or operations—not a stronger adjective attached to “production.” These are working labels, not a universal industry standard. Each describes stage, not effectiveness.

## The number is only as useful as its measure

One New Zealand says it has deployed Network Concierge to help analyze network-related customer complaints. The agent gathers performance data, alarms and past incidents, then gives a customer-service representative a summary and suggested next step. One NZ reports an 80 percent reduction in analysis time.

That figure describes analysis time, as the operator reports it. It is not a restoration-time measure, and it does not by itself show that complaints were resolved faster or that service quality improved. The release does not state the case count, baseline, observation period, comparison method or answer-quality rate. Without those details, the percentage is a local claim worth asking about, not a productivity result that can be compared with another operator’s.

The same release describes a separate generator-placement tool. One NZ says it was put to the test during severe weather in the South Island and that deeper integration with incident-management and field-force workflows is being explored. Keep that use case separate: guidance on where to send mobile generators is not evidence that the system controlled the network or restored service.

Orange France offers a different kind of scale claim. Its release says Mon Assistant IA (MAIA) was deployed to 3,000 sales advisers and was supporting nearly one million conversations per month. The adviser remains in control and validates proposed responses. Those numbers tell us the reported deployment reach and conversation volume. They do not tell us how often advisers used it, whether answers were correct, how much time was saved, or whether customer outcomes changed. Orange does not provide those measures in the release.

SK Telecom’s AI-RAN Parameter Recommender makes another useful distinction. The operator says the recommender was applied to its commercial network and systematically validated. It recommends base-station parameters; the same release says real-time application was still being developed. That is evidence of validation in a commercial-network setting, not evidence that the system was autonomously changing parameters across the live network. “On the commercial network” and “in autonomous production” are not interchangeable descriptions.

Put these claims in one column called “AI deployed” and the differences disappear. Keep the workflow, stage and measure beside each other instead: a production remediation action, a reduction in analysis time, conversation volume and commercial-network validation are four different kinds of evidence, not a sequence of increasing maturity. None of these examples demonstrates reduced cyber risk or independently measured return on investment.

It is easy to let these measures blur together. Adoption is not effectiveness. A count of conversations, actions, advisers or sites measures reach or activity. A productivity claim needs a defined task and a defensible comparison, including the human review and rework that remain. A service-quality claim needs a service measure, such as correctness or customer impact, not just tool usage. A security claim needs evidence about the control or threat outcome. An ROI claim needs costs and benefits measured on a comparable basis. A result in one category does not prove a result in another.

“Production” is still important. When an operator says “production,” it is a claim that the system has crossed beyond a presentation or a test. But it does not tell a buyer or board how widely the system is used, what it can change, how often it fails, whether staff can stop it, or whether its benefits exceed its costs. Those are separate claims. Ask for separate evidence.

## A claim check for the next meeting

When a supplier or executive says “we have deployed AI,” write down the answer to these questions:

1. **Which workflow?** Name the operational task, service domain and people who use it.
2. **What stage and footprint?** Is it announced, demonstrated, piloted, live in a bounded operation, or scaled? How many sites, users or cases are actually covered?
3. **What authority?** Does it gather information, recommend, prepare an approved change, or execute one? Which target enforces the action?
4. **Who is making the claim?** The operator, supplier, analyst, survey respondent or telemetry provider? Is the result independently measured or self-reported?
5. **What does the metric count?** State the unit, denominator, baseline, period and comparison method. Include errors, overrides, rework and service impact where relevant.
6. **Which outcome does it support?** Adoption, productivity, service quality, security effectiveness, revenue or net ROI? Do not let evidence for one stand in for another.

If the answer to a material question is missing, record it as unknown. Do not turn missing evidence into a negative finding, and do not fill the gap with a stronger label. That is the difference between taking a deployment seriously and treating a claim as proof.

<!-- Non-reader-facing sentence audit map. Exact primary-source passages, source classes and limitations are recorded in research/claim-ledger.md.
P1.S1-S3, P2.S4-S7: O1 / OP-1 (RAN Guardian production scope, first-month autonomous-action count, event-management-time claim and absent denominator/method/error/override/rollback details).
P4.S2: O1 / OP-1 (remediation actions); O9 / OP-3 (data gathering, summary and suggested next step).
P7.S2: O9 / OP-3 (deployed read-and-recommend workflow); P7.S3: O18 / OP-8 (commercial-network validation, with real-time application still future work); P7.S4: O19 / OP-10 (event-assurance/O&M work described as a pilot).
P9.S1-S3, P10.S3: O9 / OP-3 (Network Concierge deployment, workflow, operator-reported analysis-time metric, and missing sample/baseline/period/comparison/quality details).
P11.S1-S3: O9 / OP-3 (separate generator-placement workflow, severe-weather test and future deeper integration; no network-control or restored-service result established).
P12.S2-S6: O13 / OP-5 (MAIA deployment, conversation volume, adviser validation; quality/time/cost outcomes not reported).
P13.S2-S3: O18 / OP-8 (commercial-network application, systematic validation, recommendation task, and real-time application still in development).
P14.S1-S3: O1 / OP-1; O9 / OP-3; O13 / OP-5; O18 / OP-8. These are stage/outcome distinctions, not comparative performance claims.
All other statements are working definitions, questions, editorial analysis or evidence rules rather than claims of measured operator outcomes. -->
