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

<!--
P1-P40: Author analysis and synthesis based on Chapters 1–5 and the current claim-ledger dispositions; no new empirical or sector-prevalence claim. The opening service-visibility tension is an analytic argument, not a measured cause of incidents. No operator composite is expanded or presented as observed practice.
Table 1: Author-derived portfolio, roles and evidence gates, not a report of a carrier’s staffing, budget or practice.
No costs, ROI, staffing counts, risk scores, deployment results or operator interviews are invented.
-->