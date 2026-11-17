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

<!-- Non-reader-facing source/claim map. Exact primary-source passages, source classes and limitations are in research/claim-ledger.md.
P1-P2: O1 / OP-1 (RAN Guardian production scope, first-month action count, event-management-time claim and absent sample/method/error/override/rollback details).
P3-P4: O9 / OP-3 (Network Concierge workflow and operator-reported analysis-time figure; no case denominator, baseline or quality result; separate generator-placement workflow and no network-control/restoration result).
P5: O13 / OP-5 (MAIA reach, conversation volume and adviser validation; no productivity, security or customer outcome reported).
P6: O18 / OP-8 (commercial-network validation, recommendation task and real-time application still in development).
All remaining content is author synthesis and decision guidance; no additional performance, security-effectiveness or ROI claim is asserted.
-->