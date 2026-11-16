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

<!-- Non-reader-facing source/claim map. Exact primary-source passages, source classes and limitations are in research/claim-ledger.md.
P1-P2: O1 / OP-1 (RAN Guardian production scope, first-month action count, event-management-time claim and absent sample/method/error/override/rollback details).
P3: O9 / OP-3 (Network Concierge workflow and operator-reported analysis-time figure; no case denominator, baseline or quality result).
P4: O9 / OP-3 (separate generator-placement workflow and severe-weather use; no network-control/restoration result established).
P5: O13 / OP-5 (MAIA reach, conversation volume and adviser validation; no productivity, security or customer outcome reported).
P6: O18 / OP-8 (commercial-network validation, recommendation task and real-time application still in development).
P7-P10: Author synthesis and evidence distinctions; no comparative performance, security-effectiveness or ROI claim.
-->