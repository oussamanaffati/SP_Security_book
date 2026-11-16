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

<!-- Non-reader-facing source/claim map. Exact primary-source passages, source classes and limitations are in research/claim-ledger.md.
P1-P2: O1 / OP-1 (RAN Guardian production scope, first-month action count, event-management-time claim and absent sample/method/error/override/rollback details).
P3: O9 / OP-3 (Network Concierge workflow and operator-reported analysis-time figure; no case denominator, baseline or quality result).
P4: O9 / OP-3 (separate generator-placement workflow and severe-weather use; no network-control/restoration result established).
P5: O13 / OP-5 (MAIA reach, conversation volume and adviser validation; no productivity, security or customer outcome reported).
P6: O18 / OP-8 (commercial-network validation, recommendation task and real-time application still in development).
P7-P11: Author synthesis and evidence distinctions; no comparative performance, security-effectiveness or ROI claim.
-->