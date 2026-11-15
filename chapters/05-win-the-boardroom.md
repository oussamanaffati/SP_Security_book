# Chapter 5: Board Decisions Before the Next Incident

Before the next incident, the board needs a business decision, not an AI product pitch. Which services get capacity first, and what network work must move to make that possible? The CISO and CTO should show the service consequence, the supported change and the work it displaces. The board should protect priorities and resources, not select a model.

## Speak in service-provider consequences

Start with the service, not the tool. Depending on operator and market, that may mean emergency communications, payment services, public agencies, hospitals, enterprises or consumers. The UK Cyber Governance Code notes that cyber incidents can disrupt business continuity and damage customer trust.

Network criticality alone does not prove national impact. Give the affected service and dependencies, workflow and current access, proposed action, likely consequence and what remains unverified.

A generic statement such as “AI is a major new threat” gives the board no decision. The NOC assistant described in Chapter 1 links alarm summaries to neighboring-domain data, supplier cases and NOC visibility. The board question is whether to protect capacity for a safer authority boundary, not which model to buy.

That choice has a capacity cost. Identity separation uses engineering and supplier time that may displace other network work; leaving capacity unprotected maintains broader access. The board can protect engineering and supplier capacity. Management applies the delegated-authority rule below to any exposure that remains.

If the operator relies on a legacy management platform, an external supplier or a narrow maintenance window, explain how that changes the response plan. A broad statement about “the network” is less useful than a clear account of which domain, service and recovery path are involved.

For a supplier feature, ask what changes when the model provider, data access, retention, processing location or supplier access changes. Can the operator verify or restrict each change without disrupting a needed service? Separate operator-tested boundaries from supplier assurances, and state the service trade-off where notice or restriction is unavailable.

**Distinguish feature disablement from supplier exit.** Turning off an AI feature may leave the surrounding management product and supplier support in place; ending the contract may still leave no tested way to continue service. Ask management which dependency the proposed work addresses and what the continuity plan still needs to prove. Protect portability or continuity capacity when supplier dependency makes that work material.

## Show why the board is part of the operating model

The governance model I recommend gives the board three jobs: set appetite, allocate resources and require assurance. Management chooses tools and approves operational changes. The service owner provides impact, tolerance, dependencies and fallback. Only a service executive with delegated authority over every affected service may accept residual risk, and only within approved appetite. Escalate if delegation is missing or appetite would be exceeded. Board visibility alone is not acceptance.

**One appetite, service-specific thresholds.** An enterprise appetite gives the board a consistent basis for funding and challenge, but one threshold can hide different service consequences. The NOC assistant’s proposed visibility-reducing change raises a continuity question; the deferred live-core patch raises a different one about urgency and the supported window. A separate appetite for every product or platform can create parallel rules, incomparable reporting and repeated approvals. Translate one enterprise appetite into a small set of service-specific impact and escalation thresholds.

Use the same board reporting fields across services, but let each service owner supply its dependencies, tolerable impact and fallback. For the shared edge/core account, show which domains and operational views a restriction would affect. For the deferred patch, show which interim controls and service conditions make waiting tolerable, and which change requires escalation. A single “high” label cannot answer either question.

This mapping takes service-team time, but lets leaders set priorities without pretending service impacts are uniform. Define each threshold by a measurable impact and observable fallback, not a high/medium/low label. If local information cannot support one, report the gap and fund the mapping; do not mistake missing data for tolerance.

Routine reporting and event-driven review serve different purposes. The board’s agreed cadence shows trends, funding progress and assurance. It cannot be the only route for a material change: a supplier changes retention or access, a revocation test fails, a window slips or a fallback changes. Each can make the previous decision stale. Set the trigger, the service facts management must bring and the threshold for board escalation. Do not send every technical change to directors; that turns oversight into operational approval. Nor should management wait for the next pack when the change affects appetite, resources or assurance. Set the response interval from service tolerance and delegated authority, not a universal clock.

Funding sets the order of work; it does not resolve exposure in the next tranche. Show which services remain affected and what change would reopen the decision.

The UK Cyber Governance Code recommends formal reporting at least quarterly with metrics and tolerances, and at least annual exercises with relevant internal and external stakeholders. That is UK guidance, not a universal legal requirement. For service providers, use existing governance to keep service impact, appetite and assurance visible.

**Choose where board oversight sits.** A separate AI committee gives directors dedicated time, but adds another agenda and can pull attention from cyber, network resilience, procurement and enterprise risk. An existing cyber or risk committee connects the issue to service resilience, but the work can disappear if agenda time, expertise or reporting is weak. Start with a standing agenda item, provided directors see service-level facts rather than product demonstrations or tool counts.

Before creating a committee, test whether the current body can challenge the operator’s highest-impact uses. Directors need a clear view of service and supplier dependencies, identity/data/action reach, control results, fallback, material changes, resource trade-offs and overdue fixes. If reporting is weak, fix it first; a new committee cannot create an inventory or prove a control.

Create a separate forum only when the existing body repeatedly lacks time or relevant expertise, or a binding duty requires one. Weigh director and secretariat time, outside expertise, duplicate reporting and delay against the value of focused challenge. Give its charter a clear remit: which decisions it oversees, what goes to the full board, what service information it needs and where operational risk decisions sit. Confirm that it improves decisions rather than moving unresolved items to another agenda; it must not approve products or replace the delegated service executive.

An official summary from the Australian Cyber Security Centre and the Australian Institute of Company Directors asks whether frontier AI changes attack-speed assumptions and supplier risk. It also asks whether an operator could keep its most important services running during a serious incident. This is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released on 11 December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to a measurable, outcome-oriented baseline across IT and OT. Use that frame in the board ask: fund demonstrated outcomes, not AI-branded products.

For a multinational operator, bring one short view per market: applicable duties, reporting thresholds, deadlines and the team tracking them. Separate binding requirements from consultations or emerging guidance. TRAI’s 30 October 2026 telecom AI draft remains a consultation, not a final rule.
The draft proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities. These are proposals, not current duties. Use them to test whether existing governance can see AI-enabled service risk; do not create a committee solely because the consultation proposes one.
Treat a duty as binding only when it is in force and applies to the entity; have Legal confirm applicability.

**Make funding market-specific.** When a priority workflow crosses markets, show applicable duties, affected services, local effort and which data, action and fallback boundaries are validated in each market. Shared services can reduce duplicated support; local processing or exclusion can add reconciliation work or narrow a regional view. Fund rollout only in markets where the route is supported, and leave the service-risk decision with an executive whose delegation covers all affected services.

## Bring evidence the board can test

A board paper should show the decision and the service facts needed to challenge it, not make directors reconstruct the architecture.

For each priority, show the affected service, the decision requested, the current access or operating condition, and what has been verified. Distinguish target-tested controls from supplier assurance, mapped paths from unknowns, and delivery from demonstrated risk reduction. Counting inventory entries or completed work does not show that a control works.

For joined operational records, Chapter 2’s source-contract check shows only whether sources, freshness and conflicts appear in the output. It does not test identity boundaries, tool restrictions or general model accuracy.

An exercise should report whether responders could revoke access without losing necessary NOC visibility, which fallback worked and what decisions remained unclear. The cross-sector June 2026 Five Eyes cyber-agency statement says boards should ensure controls work under incident pressure, not merely exist. Track exercise findings to closure before citing them as assurance. If a live integration cannot be tested safely, state what remains unverified and which decision that gap blocks. Do not report it as passed.

**Choose the assurance model to match the gap.** Supplier material describes intended behavior and provider-run controls; it cannot show the operator’s deployed permissions or target result. Management testing sees real service paths, but consumes scarce engineering and NOC time and may miss its own assumptions. Independent review can challenge scope and conclusions, but costs more, depends on supplier access and cannot test behavior it cannot observe.

For a high-impact workflow with a shared identity or supplier-managed hop, fund an independent challenge of the test plan and results. The operator keeps control of testing and fallback; the delegated service executive makes the risk decision. For a low-impact, read-only task with inspectable targets and clear authority, management review is proportionate. The board need not fund external assessment for every feature.

Budget for the reviewer, supplier participation, engineering, a safe test environment or window, and NOC backfill. If live behavior cannot be tested safely, state what remains unknown and withhold deployment until a safe test path exists or an authorized, time-bounded service decision is made. Recheck after a material change, failed test or changed dependency.

Security competes for the same engineers, maintenance windows and supplier capacity as the rest of the network. When an upgrade delays a control, show the interim measure and what it has actually changed. Cross-sector guidance from CISA and the Canadian Centre for Cyber Security notes that token-based AI services can affect cost, performance and availability. For a critical workflow, show the fallback if service degrades or disappears. If a regulatory deadline changes the order, state the date and who tracks it.

Show four states separately: work in progress; a control tested and passed for its scope; exposure accepted under defined conditions; and unresolved exposure without a valid decision. A completed action or named owner does not prove that the control works.

## Ask for decisions, not general support

**Portfolio choice when capacity cannot fund everything.** For this planning exercise, assume the operator can protect capacity for two substantial technical work packages and one cross-functional exercise next cycle. The composites say nothing about actual staff or budget. The board is choosing which changes can reduce service exposure without forcing an unsafe window, not which AI product is most visible.

The board faces four different decisions: whether to protect capacity for shared-account migration; how to preserve service if a supplier feature cannot be separated from its product release; whether a task-bounded NOC pilot merits recurring support; and whether local exposure justifies readiness funding for an earlier patch. Local service facts and available capacity set the order.

The composites say nothing about a particular operator’s service impact, affected deployment, cost or staffing. If local checks confirm broad shared-account reach and an affected, reachable patch path, protect the identity-boundary test and patch-applicability check first. Size supplier-separability work by whether it could change the release decision. Keep the NOC pilot bounded until its authority boundary is proven. Reorder if the containment test fails or the deployed version is not affected. Reserve exercise capacity with NOC/SOC backfill and supplier participation.

Confirm local engineering, supplier, NOC backfill and safe-window constraints, including which work can run in parallel. Do not assume the composites share suppliers, teams or maintenance windows. Show which dependency each tranche addresses and what service risk remains while work waits.

**Fund the bottleneck, not an AI label.** When an exercise or pilot finds a delay, identify the bottleneck: unclear authority, supplier dependence, engineering/test capacity or manual workload. Fund that constraint: a pre-authorized trigger with a deputy, supplier support, engineering time or NOC backfill. More automation will not fix unclear containment or an untested fallback. Estimate cost and displaced work locally, then check whether the remedy moved the bottleneck. Do not fund it on assumption alone.

**Make the investment case from a service-impact chain.** Compare the proposed work with the best feasible alternative and the work it displaces. Start with the service and dependency. What happens if the work waits or fails? State the service owner’s tolerance and fallback, what is confirmed, what remains unknown and what the tranche will resolve. Use a dollar range only if Finance and Operations can substantiate it; show the method and assumptions. Otherwise, describe service and response consequences without invented figures. Be explicit about what the investment changes and what remains dependent.

**Fund operation after the project closes.** Separate one-time delivery from recurring access reviews, supplier-change checks, logging, reviewer and shift capacity, fallback practice, and version/reach verification. Estimate the run cost from local work, including which budget funds it. Supplier assurance does not replace an operator test or an independent fallback. Without recurring capacity, narrow the scope, keep the pilot bounded or defer handoff.

### Stage funding at an evidence gate

When scope, cost or a safe window is uncertain, fund a bounded design/test tranche with supplier time and NOC backfill. It buys a later decision but delays benefit. Upfront deployment funding commits before readiness is known; withholding work preserves budget but may leave exposure or manual effort in place. Keep only an authorized interim treatment while evidence is gathered.

Release implementation capacity only after the operational gate confirms a supported route, acceptable service impact and fallback, and a local estimate of effort and displaced work. If the gate fails, hold deployment funding. Pay for a test, mapping, containment or alternative only when the result could change the decision. If discovery expands scope or effort, return with affected services, tolerances, dependencies, estimate basis and displaced work; recommend an increase, reduction or pause. State the gaps and interim treatment.

Name who reviews reserved capacity and when. Reallocate it when a dependency slips, new findings remove the need for an expedited route or no credible window exists; approval is not a mandate to spend. Reopen when service, dependency or appetite changes.

## Board decision: shared edge/core account

In the shared-account composite, one account reaches edge nodes and parts of the core; service dependencies, target enforcement, migration support, fallback and cost remain unknown.

Protect capacity to assess and, if supported, migrate to target-native identities. If that route cannot meet the required window, compare a tested gateway interim with a time-limited shared-account exception. Funding the design is not authorization to deploy either route.

Bring back the affected-service map, the supported path, local effort and displaced work, service-owner tolerance and fallback, plus the trigger that would change the recommendation. Reopen if account reach, supplier support, service dependency or fallback changes.

If the map shows different service tolerances, report each consequence and fallback. One executive may decide for the combined path only if that person’s delegation covers every affected service; otherwise split the scope or escalate the authority gap. The board can fund mapping and resolve resource or appetite questions.

## Board decision: supplier diagnostic feature

In the supplier-feature composite, a routine update enabled a diagnostic feature that reads topology and proposes actions; direct execution is not established.

Fund the work to verify whether the feature can be disabled independently of the product release without losing the required service view. If separation is unsupported, fund a supplier-supported pause or rollback path and its NOC fallback rather than assuming a workaround. This is a continuity and release choice, not approval to enable; estimate the supplier, engineering and NOC effort and displaced work.

Determine whether dependency ends at the AI feature or extends to the management product and service-support path. Fund portability or exit work only when that broader dependency materially affects continuity; a feature switch and contract termination are different decisions. Reopen if a release changes the feature path, disablement no longer preserves the service view, or supplier support or fallback changes. If the feature stays in use with its boundary or fallback unverified, obtain a time-bounded decision from the delegated service executive.

## Board decision: NOC assistant

The composite establishes neighboring-domain data reach and a proposed visibility-reducing change that was not carried out; it gives no task-benefit or service-outcome result.

Fund a task-bounded read/draft pilot only after its authority boundary and service view pass the operating gate. Include capacity for task-value measurement, reviewers, backfill and fallback. Release scale-up funding only for the tested task and scope; if the local benefit does not justify the review and continuity cost, keep the workflow at draft or manual. Broader users, data or actions need a separate decision.

Put any temporary service-risk decision in the exception process below. The dashboard reports the portfolio; it does not approve a service exception.

**Compact dashboard: distinguish delivery from risk reduction.** Use local thresholds. This portfolio view summarizes service evidence; it does not replace the operational record.

| Board view | Delivery status | Evidence of risk reduction | Board challenge or trigger |
|---|---|---|---|
| Priority-service coverage | Workflows mapped and owners named. | Evidence scope, identity/action boundary and material unknowns shown by service. | A register entry alone is not control evidence. |
| Authority boundary | Control change or access review delivered. | Test result reported for its stated scope, with unresolved paths visible. | Untested or wider paths remain open; delivery is not risk reduction. |
| Service resilience | Exercise and corrective-action status. | Containment, fallback and restoration evidence against local tolerance. | A tabletop alone cannot prove target enforcement. |
| Supplier dependency | Notice, change commitments and dependencies tracked. | Continuity and exit claims supported at the stated evidence level. | Contract terms or supplier assurance alone do not prove operation. |
| Pilot and exceptions | Scope, funding gate and review status. | Service-specific thresholds, conditions and decision owner; use the exception process below. | Untested, expired or failed scope stays visible; results do not generalize across services. |

Track delegated-authority exposure and response capacity as separate signals. For authority, show verified read/change reach and where it is enforced. For response, show time to detect, decide, contain and restore against local tolerance, with service impact and fallback. A tight boundary does not ensure fast recovery; fast response does not reduce reach. Trend by priority service; never combine the signals into one AI-risk score or let delivery status hide a high-consequence exception. State which decision cannot yet be made.

Report status by service, market and task. Green means the local gate passed for that scope; amber names the unresolved condition and date; red names the failed tolerance, boundary or fallback and the immediate action. Keep “not tested” distinct from “passed.”

## Board challenge: deferred patch window

In the deferred-patch composite, the next supported window is three weeks away. Local version and reach remain unverified.

Reserve readiness capacity for the earliest supplier-supported change while local exposure and fallback are checked. Release it only when an earlier supported route is safer than waiting; this reserves capacity, not permission to modify production. Keep the scheduled window if local findings support it and reallocate unused capacity. Bring back version and reach findings, service tolerance and fallback, local effort and displaced work, plus the delegated executive’s recommendation. Escalate if no supported route meets service tolerance. Reopen if exposure, supplier support, timing or service conditions change.

## Make an exception expire in practice

A service-risk review date is not an access expiry. Keep the service decision separate from target-enforced expiry, session handling and fallback. Each exception needs an affected service and reach, decision authority, basis and unknowns, interim treatment, review date and early-review trigger. Renewal is a fresh decision; a model, supplier or project change does not extend it automatically.

At review, decide whether the accepted impact, fallback and interim treatment still fit local tolerance. If they do not, route the issue to an executive with authority over every affected service before the review date. Directors resolve resource, appetite and assurance gaps; management must not extend an exception without a fresh decision.
