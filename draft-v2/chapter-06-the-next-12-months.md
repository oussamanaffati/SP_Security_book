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

<!-- Non-reader-facing claim/source map. Exact evidence classes and limits are in the chapter maps and claim ledger.
P1-P32: Author analysis and synthesis based on Chapters 1-5 and current claim-ledger dispositions; no new empirical or sector-prevalence claim. The visibility/support tension is analytic, not a measured incident cause.
P11-P14: Chapter 4 NOC-assistant situation and Chapter 5 supplier-feature situation; the planning constraints and three-of-four decision are explicitly hypothetical. No costs, budget, staffing, deployment, ROI or outcome is asserted.
No illustrative situation is presented as observed operator practice.
-->