# Chapter 5: Board Decisions Before the Next Incident

Before the next incident, the board needs a business decision, not a technology pitch. It must choose which service risk to reduce first, what work fits engineering and change capacity, and who owns the remaining risk while services continue. Directors need the likely service and customer impact. Management should show what is known and unknown, what evidence supports each option, and how it will reduce exposure over the next twelve months.

Chapter 4 set out the operating moves. This chapter turns their evidence into choices for the CEO and board.

## Speak in service-provider consequences

Board conversations are more effective when they begin with the service, not the tool. Depending on the operator and market, services may support emergency communications, payment services, public agencies, hospitals, enterprises and consumers. The UK Cyber Governance Code notes that cyber incidents can disrupt business continuity and damage customer trust.
Network criticality alone does not prove national impact. Describe affected services, their dependencies and likely consequences; state where evidence is incomplete.

State the service at stake, relevant workflow, current access, proposed action and remaining exposure. Mark missing facts and the evidence needed to close each gap; do not dramatize uncertainty.

A generic statement such as “AI is a major new threat” gives the board no decision. The NOC assistant described in Chapter 1 links alarm summaries to neighboring-domain data, supplier cases and NOC visibility. The board question is whether to protect capacity for a safer authority boundary, not which model to buy.

That choice has a capacity cost. Identity separation uses engineering and supplier time that may displace other network work; leaving capacity unprotected maintains broader access. The board can protect delivery capacity; management applies the authority model below to any continuing exposure.

If the operator relies on a legacy management platform, an external supplier or a narrow maintenance window, explain how that changes the response plan. A broad statement about “the network” is less useful than a clear account of which domain, service and recovery path are involved.

Chapter 4’s supplier-feature review gives the board a focused test: what changes when the model provider, data access, retention, processing location or supplier access changes? Can the operator verify or restrict each change without disrupting a needed service? Separate operator-tested boundaries from supplier assurances, and state the service trade-off where notice or restriction is unavailable.

**Distinguish feature disablement from supplier exit.** Turning off an AI feature may leave the surrounding management product and supplier support in place; ending the contract may still leave no tested way to continue service. Ask management which dependency the proposed work addresses and what continuity evidence remains open. Chapter 4 owns the operational feature-off and release gates; the board protects portability or continuity capacity when supplier dependency makes that work material.

## Show why the board is part of the operating model

The board sets risk appetite, resources and assurance expectations. It does not select a model, approve a firewall rule or accept operational service risk. Management owns those choices. The service owner supplies impact, tolerance, dependencies and fallback evidence; Security, Engineering, Procurement and Legal provide threat, technical, supplier, cost and regulatory evidence as relevant. The service executive with delegated authority across all affected services accepts residual service risk only within approved appetite. If no such authority exists, or exposure is outside appetite, escalate rather than treating it as accepted.

**One appetite, service-specific thresholds.** An enterprise appetite gives the board a consistent basis for funding and challenge, but one threshold can hide different service consequences. Revoking the NOC assistant’s account may remove alarm visibility; delaying a live-core patch leaves exposure while a supported change is prepared. A separate appetite for every product or platform creates parallel rules, incomparable reporting and repeated approvals. The useful choice is one enterprise appetite translated into a small, service-specific set of impact and escalation thresholds.

Use the same board reporting fields across services, but let each service owner supply its dependencies, tolerable impact and fallback. For the shared edge/core account, show which domains and operational views a restriction would affect. For the deferred patch, show which interim controls and service conditions make waiting tolerable, and which change requires escalation. A single “high” label cannot answer either question. Keep the authority model above: directors set appetite, resources and assurance; management makes service decisions within its delegation rather than sending every operational recheck to the board.

Building this comparison takes service mapping and owner time, but lets leaders compare priorities without claiming that service impacts are uniform. Each threshold should name a measurable impact and observable fallback, not only a “high/medium/low” label. If evidence is insufficient to define one, report the gap and fund the mapping rather than quietly treating it as tolerance.

Routine reporting and event-driven review do different jobs. The agreed board cadence shows trends, funding progress and assurance; it should not be the only route for a material change. A supplier changes retention or access, a revocation test fails, a safe window slips or a service fallback changes: each can make the previous decision stale. Define the signal that reopens the decision, the evidence management needs and the threshold for board escalation. If every technical change goes straight to directors, oversight becomes operational approval. If all changes wait for the next board pack, management may rely on an outdated boundary. Set the response interval from service tolerance and delegated authority, not a universal notification clock. Report exceptions through the normal board cycle unless they change appetite, resources or assurance sooner.

Funding one priority sets a sequence; it does not settle the exposures deferred to a later cycle. Management should show which services remain affected, what treatment is feasible and when the evidence or service conditions require a new decision.

The UK Cyber Governance Code calls for senior ownership of cyber risk, integration with enterprise risk management, a defined risk appetite and assurance that resources address those risks. It also recommends formal reporting at least quarterly with metrics and tolerances, and at least annual exercises with relevant internal and external stakeholders.
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

**Choose where board oversight sits.** A separate AI committee gives directors dedicated time, but adds an agenda and can divide attention from cyber, network resilience, procurement and enterprise risk. Folding the work into an existing cyber or risk committee connects it to service resilience; it can also bury agent-enabled workflows if the agenda, expertise or reporting is weak. A standing agenda item is often the least costly test, but only if directors receive service-level evidence rather than product demonstrations or a count of tools.

Before creating a new committee, ask whether the existing body can challenge the operator’s highest-impact uses: service and supplier dependencies, identity/data/action reach, observed control tests, fallback, material changes, open exceptions, resource displacement and overdue corrective actions. If the evidence is missing, improve the reporting and ownership first; another committee cannot repair an absent inventory or untested control. If the existing committee repeatedly lacks time or relevant network, supplier, operational or legal expertise, or a binding duty requires a separate structure, a dedicated committee may be justified. Its charter should state which decisions it oversees, what it reports to the full board, who supplies service evidence and where operational acceptance remains. It must not become a product-approval body or substitute for the delegated service executive.

Compare director and secretariat time, external expertise, reporting duplication and the risk that a new forum delays decisions against the value of focused challenge. Start within existing governance when it can surface material service risks and close actions. Add a standing agenda or separate committee when evidence shows a persistent oversight gap, material workload or an applicable duty requires it; verify that the new forum improves decision quality rather than moving the same unresolved items.

An official summary from the Australian Cyber Security Centre and the Australian Institute of Company Directors asks whether frontier AI changes attack-speed assumptions and supplier risk. It also asks whether an operator could keep its most important services running during a serious incident. This is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational operator, prepare a short view by market: the duties that apply, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.
The draft offers a telecom-specific governance signal: it proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities. That proposal is not a current obligation for every operator. Use it to test whether the existing governance body can see AI-enabled service risk; do not create a new committee solely because a consultation proposes one.
Describe something as a regulatory requirement only when it is in force and applies to the entity. Directors need to know what is binding, what is changing, and who is tracking the difference.

**Fund a supportable cross-market rollout.** In this educational case, a centrally managed NOC assistant is proposed for several markets with potentially different data, retention or approval rules. Use the market-by-market duty view above and ask management for affected services, local effort and boundary evidence. Chapter 2 owns the data and access design; Chapter 4 owns operational tests and fallback. A shared platform can reduce duplicated support, but use it only where the per-market boundary is proven; otherwise fund local review or keep that market out of scope. Delegated local executives retain each service-risk decision.

## Bring evidence the board can test

A board paper needs enough detail to support challenge, without making directors reconstruct the whole architecture. For each move, show the evidence and the decision it is meant to support.

The starting point is the set of AI-enabled workflows with the greatest potential service impact. For each, the paper can show what it can read, change or trigger, who owns it, which supplier and identity are involved, what is logged, what service is affected and who can suspend it. Gaps should be reported as gaps, not as green status.

Where a consequential service decision depends on joined operational records, Chapter 2’s source-contract check can provide one narrow evidence point: whether sources, freshness and conflicts are surfaced in the output. Report its scope and limits. It does not prove the identity boundary, tool restrictions or the agent’s general accuracy.

The access review should make authority visible: which priority identities are separate from shared accounts, which tools are read-only, which actions remain in normal network change control, and whether revocation has been tested. A count of AI systems cannot show whether their authority is controlled.

Exercise results add another kind of evidence. Did the SOC know who could revoke the identity? Did the NOC know what service might lose visibility? Could the operator move to an alternative mode? Were legal, customer and supplier contacts available? Report which decisions were unclear and whether owners closed the gaps. A June 2026 cross-sector statement by Five Eyes cyber-agency leaders says boards should ensure controls work under incident pressure, not merely exist. An exercise without corrective action is an event, not assurance.

Chapter 4 defines the evidence levels. For each board claim, name the level, service path and limitation, including whether visibility and fallback were covered. If a live integration cannot be tested safely, report the boundary that remains unknown and the decision it constrains; do not label it passed.

**Choose the assurance model to match the evidence gap.** Supplier material can describe intended behavior or controls the provider operates, but it cannot by itself show the operator’s deployed permissions or target result. Management-led testing sees the service context and the real dependency path, but uses scarce engineering and NOC time and may not challenge its own assumptions. Independent review can test whether the scope, evidence chain and conclusions withstand challenge; it is more expensive, depends on supplier access and still cannot prove behavior that the reviewer never observed.

For a high-impact workflow with a shared identity or supplier-managed hop, management can request funding for independent challenge of the test design and results while the operator retains control of the test, service fallback and risk decision. The board can protect assurance capacity without selecting operational tests. Ask the reviewer to examine the path from agent identity through connector to target, the allowed and denied requests, revocation, logs and service impact. The NOC and service owner confirm whether the test preserved the required operational view. For a low-impact read-only task with inspectable targets and clear ownership, management review may be proportionate; the board need not fund an external assessment for every feature.

Price the reviewer, supplier participation, engineering effort, safe test environment or window, and NOC backfill before setting the scope. If production testing is unsafe or a supplier will not expose a managed hop, an independent document review can improve confidence in the design but cannot prove runtime enforcement. Keep the deployment restricted until operator-verifiable evidence or an effective alternative boundary exists. Recommission assurance when a material change, failed test or service dependency alters the claim the board relies on.

Security work competes for engineers, maintenance windows and supplier capacity. If a control must wait for a platform upgrade, show the interim measure, its tested effect and the next decision trigger. CISA and the Canadian Centre for Cyber Security’s guidance on metered AI services notes that token consumption can affect cost, performance and availability. For a critical workflow, include the fallback if service degrades or becomes unavailable. If a regulatory deadline changes the sequence, show its date and tracking lead.

The dashboard must distinguish work in progress, a control tested effective, exposure accepted under defined conditions, and unresolved exposure without a valid decision. The worked dashboard keeps these states distinct; an owner or completion marker alone is not proof of control effectiveness.

## Ask for decisions, not general support

**Portfolio choice when capacity cannot fund everything.** For an educational planning exercise, assume the operator can protect two substantial technical work packages and one cross-functional exercise in the next cycle; the composites establish no such capacity limit or budget. The choice is not to pick the most visible AI product. It is to fund the evidence and changes that can reduce the greatest service exposure without using an unsafe window.

The board decisions below cover the shared edge/core account, supplier diagnostic feature, NOC assistant and deferred patch. Chapter 4 owns the operational evidence gates; use those results and service-owner input to compare funding and residual exposure.

If only two technical packages fit, sequence them using service-owner impact and tolerance evidence. A provisional first tranche could prioritize the edge-account boundary test and patch-applicability check, with a smaller supplier-separability enquiry; keep the NOC value pilot bounded until authority is proven. A reachable high-impact patch path or failed containment test can change the order. Protect the cross-functional exercise with NOC/SOC backfill and supplier participation.

Before comparing estimates, confirm local engineering, supplier, NOC backfill and safe-window constraints, and what work can run in parallel. The composites establish no shared suppliers, staff or windows, so estimates must be local. Chapter 4 owns safe sequencing; the board should see which funded dependency reduces uncertainty and what service risk remains while work waits.

**Fund the bottleneck, not an AI label.** When an exercise or pilot shows delay, classify it as unclear authority, supplier dependence, engineering/test capacity or manual workload. Match the funding to that constraint: a delegated trigger and deputy, supplier support, engineering time or NOC backfill. Wider automation is not a substitute for an unclear containment decision or a tested fallback. Estimate cost and displaced work locally, then check whether the chosen remedy changed the bottleneck. The composite reports no exercise finding or measured response improvement.

**Make the investment case from a service-impact chain.** Compare the proposed work with the strongest feasible alternative and the work displaced. State the service and dependency, the consequence if work waits or fails, the service owner’s tolerance and fallback, what evidence is confirmed or still unknown, and the uncertainty this funding tranche will resolve. Technical confirmation of reach does not confer service-risk authority.

If Finance and Operations can substantiate a loss range, show the method and assumptions. Otherwise, describe the service and response consequences without unsupported dollar values. Be clear about what the investment changes and which dependencies remain; no budget promises zero risk. Distinguish delivery progress from verified risk reduction, and identify any applicable duty only when Legal has confirmed it applies.

**Fund operation after the project closes.** A project budget can establish an identity, boundary test or pilot; it does not keep the control effective. Estimate one-time delivery separately from recurring access reviews, supplier-change evidence, logging, reviewer and shift capacity, fallback practice and version/reach checks. Assign the run-budget owner, operational lead, technical evidence owner and review trigger.

Fund shared-platform work centrally, service-specific operation with the service owner, and negotiated supplier support or notice through the contract where useful. Supplier assurance does not replace operator verification or an independent fallback. Base recurring estimates on local work, not a generic AI percentage. If run capacity is unfunded, narrow the use to what the team can sustain, keep the pilot bounded or defer the handoff. The board funds both delivery and continuing assurance; management remains accountable for the service decision and evidence.

### Stage funding at an evidence gate

When scope, cost or a safe window is uncertain, fund a bounded design/test tranche, including supplier time and NOC backfill, rather than treating full delivery as settled. That buys a later decision but delays benefit; funding deployment upfront reserves capacity but commits before readiness is known; withholding work preserves budget but may leave exposure or manual effort in place. Maintain an authorized interim treatment while evidence is gathered.

Release implementation capacity only after local evidence supports a route: affected service and reach, tested interim-control effect, service-owner tolerance and fallback, supplier-supported change, effort and displaced work. If the gate fails, do not release the original deployment spend; fund only corrective evidence, containment, a supported alternative or service mapping that changes the decision. The service executive still decides whether current exposure is tolerable.

If discovery expands scope or effort, management returns with newly affected services, tolerances, estimate basis, dependencies and displaced work, plus a recommendation to increase, narrow or pause. Name the gaps and treatment that remain; neither scope reduction nor budget growth should happen silently.

Give reserved capacity an owner and review point. Retain only what supports the next verified step; release or reallocate the rest when a dependency slips, evidence removes the need for an expedited route, or no credible window exists. Do not spend because the reserve was approved or roll it forward without a new choice. Reopen when service, dependency, evidence or appetite changes, and report the remaining exposure even when the project is smaller.

## Board decision: shared edge/core account

The composite establishes that one shared account reaches edge nodes and parts of the core. It does not establish service dependencies, target permissions, supported migration, fallback or cost. Chapter 4 owns migration options, cutover and technical evidence.

**Decision sought.** Protect capacity for service mapping, supplier-supported design and a bounded test. Apply the staged-funding framework above: implementation funding returns as a separate decision when local evidence identifies a supported, service-tolerable route and its cost/displacement. If work is deferred, the delegated service executive states the interim treatment, tolerance and review trigger.

Management returns with the affected-service map, supported route, service-owner fallback and tolerance, evidence limits, local estimate and displaced work. Reopen if account reach, supplier support, service dependency or fallback changes. Chapter 4 details target-native identities, any interim gateway, rollback and cutover gates.

If mapping shows that the shared path spans services with different tolerances, report each consequence and fallback separately and identify an executive with authority for the combined reach. No executive can accept another service’s exposure by proxy; if no delegation covers the full path, escalate the authority gap. The board funds mapping and resolves resource or appetite questions, not the operational choice.

## Board decision: supplier diagnostic feature

The composite establishes that a routine product update enabled a supplier AI diagnostic feature that reads topology and proposes actions; direct execution is not established. Chapter 4 holds the worked operational release decision and its educational assumptions. No operator test result, measured benefit, cost or service outcome is a case fact.

**Decision sought.** Protect a bounded tranche for supplier data-path and support-access evidence, a feature-off/target-boundary test, NOC continuity and an estimate. This funds a decision, not enablement. Management selects the operational route within the authority model above and returns with the service owner’s impact/fallback view, supplier commitments and local effort estimate.

If a supplier-managed hop cannot be inspected directly, fund the narrowest independent review or operator-controlled boundary test that can answer the material question. If neither route proves the relevant boundary, keep the feature restricted. Use the results to decide whether the dependency ends at the AI feature or extends to the management product and service-support path. Consider portability or exit work when that dependency materially affects service continuity; a feature switch and a contract termination clause answer different questions.

## Board decision: NOC assistant

The Chapter 1 scenario shows a service account that can reach neighboring-domain data, open vendor cases and propose a visibility-reducing change; the proposal was not carried out. It establishes no deployed permissions, target enforcement, test result, service outcome, cost or pilot result.

**Decision sought.** Protect a bounded review and assurance tranche to map the account’s actual reach and service dependencies, determine whether useful read workflows can remain while change authority is bounded, and scope any supplier, engineering and NOC capacity required. Chapter 4 owns the operational tests and evidence. Funding this work does not approve rollout.

**Release and oversight gate.** Before a pilot or scale-up decision, management returns with service-specific impact and fallback, evidence scope and limits, local effort and displaced work, and the delegated service executive’s recommendation. Expand only for the tested task and service when source coverage and reviewer workload meet local thresholds, the target boundary is verified, and essential NOC visibility is preserved. Restrict or stop the affected scope if a boundary fails or the service cannot sustain review and fallback. Broader users, data or actions require a separate decision; the scenario supplies no pilot result.

Record temporary service-risk choices under the exception process later in this chapter. The dashboard below reports portfolio status; it does not replace the service decision.

**Compact dashboard: distinguish delivery from risk reduction.** Use locally defined thresholds; these are reporting fields, not benchmark values. Chapter 4 holds technical evidence; board reporting states scope, result, limits and the decision blocked.

| Board view | Delivery status | Evidence of risk reduction | Board challenge or trigger |
|---|---|---|---|
| Priority-service coverage | Workflows mapped and owners named. | Evidence scope, identity/action boundary and material unknowns shown by service. | A register entry alone is not control evidence. |
| Authority boundary | Control change or access review delivered. | Test result reported for its stated scope, with unresolved paths visible. | Untested or wider paths remain open; delivery is not risk reduction. |
| Service resilience | Exercise and corrective-action status. | Containment, fallback and restoration evidence against local tolerance. | A tabletop alone cannot prove target enforcement. |
| Supplier dependency | Notice, change commitments and dependencies tracked. | Continuity and exit claims supported at the stated evidence level. | Contract terms or supplier assurance alone do not prove operation. |
| Pilot and exceptions | Scope, funding gate and review status. | Service-specific thresholds, conditions and decision owner; use the exception process below. | Untested, expired or failed scope stays visible; results do not generalize across services. |

Track delegated-authority exposure and response capacity as separate signals. For authority, show verified read/change reach and where it is enforced. For response, show time to detect, decide, contain and restore against local tolerance, with service impact and fallback. A tight boundary does not ensure fast recovery; fast response does not reduce reach. Trend by priority service; never combine the signals into one AI-risk score or let delivery status hide a high-consequence exception. State which decision missing evidence blocks.

Report status by service, market and task, with the tested identity, evidence scope (target-side or simulated), material unknowns, owner and next decision. Green means the defined gate passed for that scope; amber names the unresolved condition and date; red names the failed tolerance, boundary or fallback and immediate action. “Not tested” remains distinct from “passed.”

## Board challenge: deferred patch window

Chapter 4 owns the applicability check, interim-control test, change readiness and technical validation. The three-week window is a scheduling fact, not evidence of local exposure or safe delay; the composite establishes no deployed version, reachable path, test result, expedite cost or board action.

**Decision sought.** Protect conditional readiness capacity for verification and, only if local evidence shows a reachable affected path without an adequate tested interim control, an earlier supported change. This preserves supplier, engineering and NOC capacity but may displace planned maintenance; it does not approve an early production change. If local evidence shows no affected path or a tested control supports the planned window, retain the normal release process and release or reallocate the reserve at review.

Management returns with version and reach evidence, interim-control limits, service-owner tolerance and fallback, the earliest supported window and rollback, and local effort/displacement. The delegated service executive decides whether deferral or an earlier change fits appetite. If no safe earlier route exists and continued exposure exceeds tolerance, escalate the resource or authority gap and use only a verified restriction. Reopen when reach, threat evidence, control effectiveness, supplier support, window or service conditions change. A booked window is not risk reduction.

## Make an exception expire in practice

A service-risk review date is not an access expiry. Chapter 2 owns the cross-domain access decision; Chapter 4 covers target-enforced expiry, session handling and operational fallback. A board exception records the affected service and reach, decision authority, evidence and unknowns, interim treatment, review date, and the conditions that bring the decision forward. Renewal is a fresh decision, not a calendar task; a model update, supplier renewal or project status does not renew it.

At review, management explains what changed, whether the service owner still considers the impact and fallback tolerable, whether the interim treatment remains supported, and what supplier or resource dependency blocks closure. State the next decision and its evidence owner. If a material change, failed control, slipped window or changed fallback makes the previous basis stale, reopen the decision rather than waiting for the review date.

If the review point arrives without evidence to renew, do not continue automatically. Use the previously authorized restriction or manual fallback if it remains service-safe. If that would disrupt service, escalate before the decision lapses to an executive whose authority covers the full impact. The board can resolve a resource, appetite or assurance gap; it does not convert an undocumented extension into accepted risk.

## The next twelve months

In the first board cycle, set priority services and run an exercise. Quarterly reviews should show which access limits and service alternatives were tested, what gaps remain and which decisions need to reopen. By year-end, leaders should know which AI-enabled uses can affect services and how response controls perform. Fund work that improves those answers. No plan promises an invulnerable network. The credible commitment is to know which systems can act, limit their authority and test how service continues when a safeguard fails.
