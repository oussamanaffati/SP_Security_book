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

For a supplier feature, ask what changes when the model provider, data access, retention, processing location or supplier access changes. Can the operator verify or restrict each change without disrupting a needed service? Separate operator-tested boundaries from supplier assurances, and state the service trade-off where notice or restriction is unavailable.

**Distinguish feature disablement from supplier exit.** Turning off an AI feature may leave the surrounding management product and supplier support in place; ending the contract may still leave no tested way to continue service. Ask management which dependency the proposed work addresses and what continuity evidence remains open. Protect portability or continuity capacity when supplier dependency makes that work material.

## Show why the board is part of the operating model

In the governance model recommended here, the board sets risk appetite, resources and assurance expectations; management selects tools and approves operational changes. The service owner supplies impact, tolerance, dependencies and fallback evidence; Security, Engineering, Procurement and Legal provide threat, technical, supplier, cost and regulatory evidence as relevant. A service executive makes the residual-risk decision only when delegated authority covers the affected services and the exposure is within approved appetite. If no role has that delegation, or exposure exceeds appetite, escalate; visibility alone is not acceptance.

**One appetite, service-specific thresholds.** An enterprise appetite gives the board a consistent basis for funding and challenge, but one threshold can hide different service consequences. Revoking the NOC assistant’s account may remove alarm visibility; delaying a live-core patch leaves exposure while a supported change is prepared. A separate appetite for every product or platform can create parallel rules, incomparable reporting and repeated approvals. The useful choice is one enterprise appetite translated into a small, service-specific set of impact and escalation thresholds.

Use the same board reporting fields across services, but let each service owner supply its dependencies, tolerable impact and fallback. For the shared edge/core account, show which domains and operational views a restriction would affect. For the deferred patch, show which interim controls and service conditions make waiting tolerable, and which change requires escalation. A single “high” label cannot answer either question.

Building this comparison takes service mapping and owner time, but lets leaders compare priorities without claiming that service impacts are uniform. Each threshold should name a measurable impact and observable fallback, not only a “high/medium/low” label. If evidence is insufficient to define one, report the gap and fund the mapping rather than quietly treating it as tolerance.

Routine reporting and event-driven review do different jobs. The agreed board cadence shows trends, funding progress and assurance; it should not be the only route for a material change. A supplier changes retention or access, a revocation test fails, a safe window slips or a service fallback changes: each can make the previous decision stale. Define the signal that reopens the decision, the evidence management needs and the threshold for board escalation. Sending every technical change to directors can turn oversight into operational approval; waiting for the next board pack can leave management relying on an outdated boundary. Set the response interval from service tolerance and delegated authority, not a universal notification clock. Report exceptions through the normal board cycle unless they change appetite, resources or assurance sooner.

Funding one priority sets a sequence; it does not settle the exposures deferred to a later cycle. Management should show which services remain affected, what treatment is feasible and when the evidence or service conditions require a new decision.

The UK Cyber Governance Code calls for senior ownership of cyber risk, integration with enterprise risk management, a defined risk appetite and assurance that resources address those risks. It also recommends formal reporting at least quarterly with metrics and tolerances, and at least annual exercises with relevant internal and external stakeholders.
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

**Choose where board oversight sits.** A separate AI committee gives directors dedicated time, but adds an agenda and can divide attention from cyber, network resilience, procurement and enterprise risk. Folding the work into an existing cyber or risk committee connects it to service resilience; it can also bury agent-enabled workflows if the agenda, expertise or reporting is weak. A standing agenda item is often the least costly test, but only if directors receive service-level evidence rather than product demonstrations or a count of tools.

Before creating a new committee, ask whether the existing body can challenge the operator’s highest-impact uses: service and supplier dependencies, identity/data/action reach, observed control tests, fallback, material changes, open exceptions, resource displacement and overdue corrective actions. If the evidence is missing, improve the reporting and ownership first; another committee cannot repair an absent inventory or untested control. If the existing committee repeatedly lacks time or relevant network, supplier, operational or legal expertise, or a binding duty requires a separate structure, a dedicated committee may be justified. Its charter should state which decisions it oversees, what it reports to the full board, who supplies service evidence and where operational acceptance remains. Under the model above, it should not become a product-approval body or substitute for the delegated service executive.

Compare director and secretariat time, external expertise, reporting duplication and the risk that a new forum delays decisions against the value of focused challenge. Start within existing governance when it can surface material service risks and close actions. Add a standing agenda or separate committee when evidence shows a persistent oversight gap, material workload or an applicable duty requires it; verify that the new forum improves decision quality rather than moving the same unresolved items.

An official summary from the Australian Cyber Security Centre and the Australian Institute of Company Directors asks whether frontier AI changes attack-speed assumptions and supplier risk. It also asks whether an operator could keep its most important services running during a serious incident. This is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational operator, prepare a short view by market: the duties that apply, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.
The draft offers a telecom-specific governance signal: it proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities. That proposal is not a current obligation for every operator. Use it to test whether the existing governance body can see AI-enabled service risk; do not create a new committee solely because a consultation proposes one.
Describe something as a regulatory requirement only when it is in force and applies to the entity. Directors need to know what is binding, what is changing, and who is tracking the difference.

**Make funding market-specific.** When a priority workflow spans markets, show applicable duties, affected services, local effort and evidence for each data, action and fallback boundary. A shared service may reduce duplicated support, while local processing or exclusion may add reconciliation work or constrain a regional view. Fund a market only when its route is supported, and keep the service-risk decision with an executive whose delegation covers it.

## Bring evidence the board can test

A board paper needs enough detail to support challenge, without making directors reconstruct the whole architecture. For each move, show the evidence and the decision it is meant to support.

The starting point is the set of AI-enabled workflows with the greatest potential service impact. For each, the paper can show what it can read, change or trigger, who owns it, which supplier and identity are involved, what is logged, what service is affected and who can suspend it. Gaps should be reported as gaps, not as green status.

Where a consequential service decision depends on joined operational records, Chapter 2’s source-contract check can provide one narrow evidence point: whether sources, freshness and conflicts are surfaced in the output. Report its scope and limits. It does not prove the identity boundary, tool restrictions or the agent’s general accuracy.

The access review should make authority visible: which priority identities are separate from shared accounts, which tools are read-only, which actions remain in normal network change control, and whether revocation has been tested. A count of AI systems cannot show whether their authority is controlled.

Exercise results add another kind of evidence. Did the SOC know who could revoke the identity? Did the NOC know what service might lose visibility? Could the operator move to an alternative mode? Were legal, customer and supplier contacts available? Report which decisions were unclear and whether owners closed the gaps. A June 2026 cross-sector statement by Five Eyes cyber-agency leaders says boards should ensure controls work under incident pressure, not merely exist. An exercise without corrective action is an event, not assurance.

For each board claim, identify the evidence level, service path and limitation, including whether visibility and fallback were covered. If a live integration cannot be tested safely, report the boundary that remains unknown and the decision it constrains; do not label it passed.

**Choose the assurance model to match the evidence gap.** Supplier material can describe intended behavior or controls the provider operates, but it cannot by itself show the operator’s deployed permissions or target result. Management-led testing sees the service context and the real dependency path, but uses scarce engineering and NOC time and may not challenge its own assumptions. Independent review can test whether the scope, evidence chain and conclusions withstand challenge; it is more expensive, depends on supplier access and still cannot prove behavior that the reviewer never observed.

For a high-impact workflow with a shared identity or supplier-managed hop, consider funding an independent challenge of the evidence plan and results. The operator retains test and fallback control; the delegated service executive retains the risk decision. For a low-impact, read-only task with inspectable targets and clear ownership, management review may be proportionate. The board need not fund external assessment for every feature.

Budget the reviewer, supplier participation, engineering, safe test environment or window, and NOC backfill. If live runtime evidence is unavailable, name the remaining uncertainty and withhold deployment until there is a safer evidence path or an authorized, time-bounded service decision. Recommission assurance when a material change, failed test or service dependency alters the claim the board relies on.

Security work competes for engineers, maintenance windows and supplier capacity. If a control must wait for a platform upgrade, show the interim measure, its tested effect and the next decision trigger. CISA and the Canadian Centre for Cyber Security’s guidance on metered AI services notes that token consumption can affect cost, performance and availability. For a critical workflow, include the fallback if service degrades or becomes unavailable. If a regulatory deadline changes the sequence, show its date and tracking lead.

The dashboard must distinguish work in progress, a control tested effective, exposure accepted under defined conditions, and unresolved exposure without a valid decision. The worked dashboard keeps these states distinct; an owner or completion marker alone is not proof of control effectiveness.

## Ask for decisions, not general support

**Portfolio choice when capacity cannot fund everything.** For an educational planning exercise, assume the operator can protect two substantial technical work packages and one cross-functional exercise in the next cycle; the composites establish no such capacity limit or budget. The choice is not to pick the most visible AI product. It is to fund the evidence and changes that can reduce the greatest service exposure without using an unsafe window.

The four board decisions address different constraints: whether to protect capacity for shared-account migration; how to preserve service if a supplier feature cannot be separated from its product release; whether a task-bounded NOC pilot merits recurring support after its operating gate; and whether local exposure justifies readiness funding for an earlier patch. Service-owner evidence and local capacity determine which can proceed.

The composites do not establish a local operator’s service impact, affected deployment, cost or capacity. If local evidence confirms broad shared-account reach and an affected, reachable patch path, a defensible provisional sequence is to protect the identity-boundary test and patch-applicability check, with supplier-separability work sized to whether it could change the release decision. Keep the NOC value pilot bounded until its authority boundary is proven. A failed containment test or a patch that is not locally affected changes the order. Protect the exercise with NOC/SOC backfill and supplier participation.

Confirm local engineering, supplier, NOC backfill and safe-window constraints, and what work can run in parallel; do not assume the composites share suppliers, staff or windows. The board should see which funded dependency reduces uncertainty and what service risk remains while work waits.

**Fund the bottleneck, not an AI label.** When an exercise or pilot identifies a delay, classify it as unclear authority, supplier dependence, engineering/test capacity or manual workload. Match funding to that constraint: a delegated trigger and deputy, supplier support, engineering time or NOC backfill. Wider automation is not a substitute for an unclear containment decision or a tested fallback. Estimate cost and displaced work locally, then check whether the remedy changed the bottleneck; do not fund one on assumption alone.

**Make the investment case from a service-impact chain.** Compare the proposed work with the strongest feasible alternative and work displaced. State the service and dependency, consequence if work waits or fails, service-owner tolerance and fallback, confirmed and unknown evidence, and the uncertainty this tranche will resolve. If Finance and Operations can substantiate a loss range, show its method and assumptions; otherwise, describe service and response consequences without unsupported dollar values. Name what the investment changes and what remains dependent. Technical confirmation of reach does not confer service-risk authority or promise zero risk.

**Fund operation after the project closes.** Separate one-time delivery from recurring access reviews, supplier-change evidence, logging, reviewer and shift capacity, fallback practice, and version/reach checks; estimate from local work rather than a generic percentage. Assign the run-budget owner, operational lead, technical-evidence owner and review trigger. Fund shared-platform work centrally, service-specific operation with the service owner, and useful supplier notice or support through the contract. Supplier assurance is not operator verification or an independent fallback. If recurring capacity is unfunded, narrow use to what the team can sustain, keep the pilot bounded or defer handoff.

### Stage funding at an evidence gate

When scope, cost or a safe window is uncertain, fund a bounded design/test tranche with supplier time and NOC backfill rather than treating full delivery as settled. It delays benefit but buys a later decision; upfront deployment funding commits before readiness is known; withholding work preserves budget but may leave exposure or manual effort in place. Maintain an authorized interim treatment while evidence is gathered.

Release implementation capacity only after the operational gate shows a supported route, acceptable service impact and fallback, with local effort and displaced work estimated. If the gate fails, withhold deployment spend; fund corrective evidence, mapping, containment or an alternative only when it could change the decision. If discovery expands scope or effort, management returns with affected services, tolerances, dependencies, estimate basis and displaced work, and recommends whether to increase, narrow or pause. Name the gaps and treatment that remain.

Give reserved capacity an owner and review point. Reallocate it when a dependency slips, evidence removes the need for an expedited route or no credible window exists; approval is not a mandate to spend. Reopen when service, dependency, evidence or appetite changes. Funding is not residual-risk acceptance: the delegated service executive decides whether the remaining exposure is tolerable within their authority.

## Board decision: shared edge/core account

One shared account reaches edge nodes and parts of the core; service dependencies, target enforcement, migration support, fallback and cost remain unknown.

**Decision sought.** Protect capacity to assess and, if supported, migrate to target-native identities. If that route cannot meet the required window, compare a tested gateway interim with a time-limited shared-account exception. Funding the design is not authorization to deploy either route.

Bring back the affected-service map, supportable path, local effort and displaced work, service-owner tolerance and fallback, and the evidence that would change the recommendation. Reopen if account reach, supplier support, service dependency or fallback changes.

If mapping shows different service tolerances, report each consequence and fallback separately. A decision for the combined path belongs to an executive only if that executive’s delegation covers every affected service; otherwise, separate the scope or escalate the authority gap. The board can fund the mapping and resolve resource or appetite questions.

## Board decision: supplier diagnostic feature

A routine update enabled the supplier feature, which reads topology and proposes actions; direct execution is not established.

**Decision sought.** Protect capacity to verify whether the feature can be disabled independently of the product release while preserving the required service view. If separation is unsupported, fund a supplier-supported pause or rollback path and its NOC fallback rather than assuming a workaround. This is a continuity and release choice, not approval to enable; estimate the supplier, engineering and NOC effort and displaced work.

Use the evidence to determine whether dependency ends at the AI feature or extends to the management product and service-support path. Fund portability or exit work only when that broader dependency materially affects service continuity; a feature switch and contract termination do not answer the same question. Reopen if a release changes the feature path, disablement no longer preserves the service view, or supplier support or fallback changes. If the feature remains in use while its boundary or fallback is unverified, the delegated service executive owns a time-bounded continuity decision; funding the work does not accept the residual risk.

## Board decision: NOC assistant

The composite establishes neighboring-domain data reach and a proposed visibility-reducing change that was not carried out. It provides no task-benefit or service-outcome result.

**Decision sought.** Protect a task-bounded read/draft pilot only after its authority boundary and service view pass the operating gate. Fund task-value measurement and recurring reviewer, backfill and fallback capacity. Release scale-up funding only for the tested task and scope; if the local benefit does not justify the review and continuity cost, keep the workflow at draft or manual. Broader users, data or actions need a separate decision.

Record temporary service-risk choices under the exception process later in this chapter. The dashboard below reports portfolio status; it does not replace the service decision.

**Compact dashboard: distinguish delivery from risk reduction.** Use local thresholds. This portfolio view summarizes service evidence; it does not replace the operational record.

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

The next supported window is three weeks away; the case does not establish whether the deployed version is affected or reachable.

**Decision sought.** Protect readiness capacity for the earliest supplier-supported change while local exposure and fallback are verified. Release it only if the supported route is safer than waiting; this reserves an option, not authority to change production. If evidence supports the scheduled window, keep it and reallocate unused capacity. Management should bring the version and reach evidence, service tolerance and fallback, local effort and displaced work, and the delegated executive’s recommendation. If no supported route meets service tolerance, escalate the resource or authority gap. Reopen if exposure, supplier support, timing or service conditions change.

## Make an exception expire in practice

A service-risk review date is not an access expiry. The exception record should distinguish the service decision from target-enforced expiry, session handling and fallback. Record the affected service and reach, decision authority, evidence and unknowns, interim treatment, review date and early-review trigger. Renewal requires a fresh decision; a model, supplier or project change does not extend the exception automatically.

At review, management states what changed, whether the service owner still considers the impact tolerable and the fallback viable, whether the interim treatment remains supported, and which dependency blocks closure. Name the next decision and evidence owner; reopen sooner if a control fails, the window slips or service conditions change.

If evidence is missing at review, use the previously authorized restriction or manual fallback only if it remains safe for the service. If that would disrupt service, escalate before the review point passes to an executive whose authority covers the full impact. Under the recommended model, directors resolve resource, appetite or assurance gaps; management does not extend an exposure silently when a fresh service decision is required.

## The decision to carry forward

AI does not make every workflow unsafe. The risk is a mismatch between the authority granted and the operator’s ability to see its reach, contain its effects and recover the service. A shipped feature or a positive average pilot is not proof that the operational boundary is safe. A priority earns support when the task’s authority boundary is evidenced, a service-safe containment and recovery route is known, and remaining uncertainty is explicit. Where safe testing is unavailable, limit or withhold the relevant authority; use a read/draft or manual route only if it preserves the service. Under the governance model recommended here, continuing exposure goes to the delegated service executive within authority and appetite; otherwise it is escalated. Funding the work does not accept the risk. Choose three or four priorities that close the most consequential gaps, and name what would make you reopen them: changed reach, weaker evidence, supplier dependence or service tolerance.
