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

<!-- Non-reader-facing claim/source map. Exact evidence classes and limits are in the chapter maps and claim ledger.
P1-P32: Author analysis and synthesis based on Chapters 1-5 and current claim-ledger dispositions; no new empirical or sector-prevalence claim. The visibility/support tension is analytic, not a measured incident cause.
P11-P14: Chapter 4 NOC-assistant situation and Chapter 5 supplier-feature situation; the planning constraints and three-of-four decision are explicitly hypothetical. No costs, budget, staffing, deployment, ROI or outcome is asserted.
No illustrative situation is presented as observed operator practice.
-->