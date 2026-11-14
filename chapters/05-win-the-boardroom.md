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

## Show why the board is part of the operating model

The board sets risk appetite, resources and assurance expectations. It does not select a model, approve a firewall rule or accept operational service risk. Management owns those choices. The service owner supplies impact, tolerance, dependencies and fallback evidence; Security, Engineering, Procurement and Legal provide threat, technical, supplier, cost and regulatory evidence as relevant. The service executive with delegated authority across all affected services accepts residual service risk only within approved appetite. If no such authority exists, or exposure is outside appetite, escalate rather than treating it as accepted.

**One appetite, service-specific thresholds.** An enterprise appetite gives the board a consistent basis for funding and challenge, but one threshold can hide different service consequences. Revoking the NOC assistant’s account may remove alarm visibility; delaying a live-core patch leaves exposure while a supported change is prepared. A separate appetite for every product or platform creates parallel rules, incomparable reporting and repeated approvals. The useful choice is one enterprise appetite translated into a small, service-specific set of impact and escalation thresholds.

Use the same board reporting fields across services, but let each service owner supply its dependencies, tolerable impact and fallback. For the shared edge/core account, show which domains and operational views a restriction would affect. For the deferred patch, show which interim controls and service conditions make waiting tolerable, and which change requires escalation. A single “high” label cannot answer either question. Keep the authority model above: directors set appetite, resources and assurance; management makes service decisions within its delegation rather than sending every operational recheck to the board.

Building this comparison takes service mapping and owner time, but lets leaders compare priorities without claiming that service impacts are uniform. Each threshold should name a measurable impact and observable fallback, not only a “high/medium/low” label. If evidence is insufficient to define one, report the gap and fund the mapping rather than quietly treating it as tolerance.

Routine reporting and event-driven review do different jobs. The agreed board cadence shows trends, funding progress and assurance; it should not be the only route for a material change. A supplier changes retention or access, a revocation test fails, a safe window slips or a service fallback changes: each can make the previous decision stale. Define the signal that reopens the decision, the evidence management needs and the threshold for board escalation. If every technical change goes straight to directors, oversight becomes operational approval. If all changes wait for the next board pack, management may rely on an outdated boundary. Set the response interval from service tolerance and delegated authority, not a universal notification clock. Report exceptions through the normal board cycle unless they change appetite, resources or assurance sooner.

Funding one priority sets a sequence; it does not settle the exposures deferred to a later cycle. Management should show which services remain affected, what treatment is feasible and when the evidence or service conditions require a new decision.

The UK Cyber Governance Code calls for senior ownership of cyber risk, integration with enterprise risk management, a defined risk appetite and assurance that resources address those risks. It also recommends formal reporting at least quarterly with metrics and tolerances, and at least annual exercises with relevant internal and external stakeholders.
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

**Choose where board oversight sits.** A separate AI committee gives directors dedicated time, but adds another agenda and can split attention from cyber, network resilience, procurement and enterprise risk. Folding AI into an existing risk or cyber committee uses current governance and connects decisions to service resilience; it can also bury agent-enabled workflows if the agenda, expertise or reporting is weak. Start with existing governance when it can show material service uses, supplier dependencies, tested boundaries and open decisions. Add a standing AI review or a separate committee when workload, applicable regulation or a persistent oversight gap justifies the extra layer. Check committee terms, the evidence directors receive, overdue actions and market-specific duties before choosing.

An official summary from the Australian Cyber Security Centre and the Australian Institute of Company Directors asks whether frontier AI changes attack-speed assumptions and supplier risk. It also asks whether an operator could keep its most important services running during a serious incident. This is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational operator, prepare a short view by market: the duties that apply, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.
The draft offers a telecom-specific governance signal: it proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities. That proposal is not a current obligation for every operator. Use it to test whether the existing governance body can see AI-enabled service risk; do not create a new committee solely because a consultation proposes one.
Describe something as a regulatory requirement only when it is in force and applies to the entity. Directors need to know what is binding, what is changing, and who is tracking the difference.

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

A request for “continued support” leaves the choice unclear. A board paper is stronger when it puts a specific decision in front of directors.

1. **Set priority outcomes.** The first decision is which three or four outcomes the operator will pursue over the next twelve months, beginning with services and workflows whose consequences are greatest.
2. **Name delivery leads.** Each move needs an executive sponsor and an operational lead across security, network, IT, procurement or service continuity as required.
3. **Protect delivery capacity.** Staff time, planned change windows and supplier engagement all compete with other operational work. If the board will not fund everything, it should see what moves later and what risk remains open.
4. **Set assurance and escalation.** Agree what evidence management will provide and which service impacts, failed tests or changed dependencies require an earlier review.

**Fund the bottleneck revealed by the exercise.** For an educational board discussion based on the NOC assistant, assume an off-hours exercise found that responders waited because the containment trigger and deputy authority were unclear, while NOC staff were already handling manual alarm work. This is a decision assumption, not a reported exercise result. The board is choosing between additional on-call and backfill, supplier standby, more automation, or no new capacity.

On-call coverage and backfill can reduce the wait for a qualified operator, but create recurring staffing cost and may displace maintenance or other service work. Supplier standby brings platform knowledge when the supplier is the bottleneck, but adds contract cost and dependence; it does not establish that the supplier identity or target path is safe. Broader automation may reduce execution delay, but needs engineering and testing and can remove service visibility if the stop is too broad. No new spend preserves the current budget but leaves the response gap in place. These options solve different causes; funding the wrong one buys activity, not a faster safe decision.

Under the assumption above, protect a named deputy and NOC backfill, and revise the pre-authorized trigger before buying broader automation. Keep any automated stop narrow and limited to a path already tested at the target. Add supplier standby only if exercise evidence shows the delay depends on supplier availability or expertise. Management should provide local cost and displacement estimates; no cash figure or response improvement is established here.

Make the next exercise a funding check. Test the same service decision off-hours with the named deputy, with and without supplier participation, and record which interval improved, what service view was lost and how much manual work moved. If time remains in technical execution after authority and coverage are fixed, fund the relevant engineering or automation test. If the delay remains an approval question, do not solve it with more staff or a wider agent permission. The board protects resources and challenges the evidence; management keeps operational stop authority within its delegation.

The comparison should include the strongest feasible alternative. Retaining the shared edge/core account preserves the current arrangement but retains cross-domain reach; separation needs a supplier change and safe window. Show service impact, fallback and displaced work under both paths. If the reach crosses service domains, route the decision to an executive whose delegation covers the full impact; technical confirmation of reach does not confer service-risk authority.

The investment case should state what the money buys. It cannot guarantee that an incident will not happen. It should improve the operator’s ability to identify consequential uses, restrict unnecessary authority, contain an incident while maintaining service through a tested fallback, meet applicable duties and restore services. Some costs are people and change capacity, not software. Directors should understand both the risk the plan is meant to reduce and the work it will displace.

If Finance and Operations can substantiate a loss range, show the assumptions. If they cannot, explain service impact, response dependency and regulatory exposure without an unsupported monetary value. The decision remains real: fund the work now, choose another sequence or resource an interim treatment.

### Stage funding without approving the exposure

When the supplier cost, engineering effort or safe test window is still unknown, avoid presenting one fixed budget as if the delivery path were settled. The board can fund design and test capacity first, including supplier time and NOC backfill, while keeping authority at its current or more restricted level. Management then returns with the tested boundary, service impact, rollback path and an implementation estimate before asking for deployment funding.

This staged route limits the chance of funding a design that cannot be deployed safely, but it requires another decision and may delay the diagnostic benefit. Full funding at once can reserve scarce supplier or engineering capacity, but commits before the evidence is complete. Withholding all funds avoids new spend and leaves the current exposure and manual workload in place. Where current reach creates a material service concern, do not wait for the next budget decision to apply a safe interim restriction. Release the larger implementation budget only when local testing shows what the change permits, denies and does to service visibility; if the test fails, return with a safer restriction or a revised delivery path.

Apply the staged approach to the shared edge/core account. It reaches edge nodes and parts of the core. The operator still needs to map affected services and dependencies, confirm supplier support, estimate effort and demonstrate a safe rollback. On these facts, protect capacity for service mapping and a supported design/test, not a production cutover. That buys a decision-ready path, not immediate reduction in reach; until a safe restriction is verified, the existing cross-domain access remains. Before releasing implementation funds, ask management to bring service-owner impact and fallback evidence, supplier-supported options, the effort and displaced-work basis, and allowed/denied and rollback results. If evidence shows the reach crosses service tolerance or no safe split exists, route interim exposure through the delegated service executive and revisit the funding path.

## Board decision: NOC assistant

Use the NOC assistant described in Chapter 1 as the worked board decision. Its service account can reach neighboring-domain data, open vendor cases and propose a visibility-reducing change; the proposal was not carried out. **Educational assumptions, not case facts:** treat the affected service as one network-service-assurance domain; assume supplier design material describes a separate action setting but no runtime test has verified it; assume only Level 1 design evidence is available. The NOC can continue alarm review and vendor-case handling manually during a supported test window, but needs temporary backfill. Target permissions, session persistence, revocation, supplier activity records, implementation effort and fallback impact remain unverified. No service outcome or monetary cost is supplied. Replace these assumptions with local evidence before using the paper.

**Decision sought.** Protect network/identity engineering, supplier support and NOC backfill for a bounded configuration review and target test. Do not fund production rollout on design documentation alone. This is a request for delivery capacity and assurance, not for the board to accept operational service risk.

**Service and exposure.** **Educational assumption:** the affected service is a network-service-assurance domain with dependencies on neighboring-domain topology and supplier case handling. The account’s read and proposal capabilities are established in the scenario; whether adjacent-domain access is necessary, how the target enforces change approval, whether sessions persist after revocation and what visibility is lost on disablement remain unknown. The proposed change was not executed.

**Options.**

| Option | Service effect and trade-off | Evidence gate |
|---|---|---|
| **A. Keep the shared account** | Avoids immediate change; preserves workflow but leaves broad reach and weak attribution. Deferral is a service-risk decision, not a neutral delay. | Verify permissions and service impact; apply Chapter 5’s authority model and record the trigger that reopens deferral. |
| **B. Restrict or pause actions** | Retain only verified read/draft use if separable. Manual vendor cases and changes add NOC work; a full pause may also remove useful visibility. | At connector and target, prove actions are refused, read scope is limited, principal is logged and fallback preserves service view. |
| **C. Separate identities** | Can improve attribution and suspend action without removing alarm reads; needs engineering, supplier work and a supported window. | Test allowed/denied paths, existing-session revocation, downstream effects, audit correlation, change control and service fallback. |

**Management recommendation.** Under these assumptions, prefer Option B only after a Level 3 test proves that the action path can be stopped without losing essential alarm reads, and that the target denies disallowed requests and records the principal. Until then, do not widen the assistant’s authority; use a service-safe restriction or pause if the existing action path cannot be bounded. Plan Option C against a supported supplier path. If testing proves separate read/draft use, retain that scope within normal change control. If it fails, compare a supported feature pause or product rollback with the service value of the release and the manual NOC workload. Reopen the choice if the test fails, the service owner identifies a tighter tolerance, or supplier support changes.

**Resources and assumptions.** **Educational planning assumption:** the configuration review and target test require network/platform and identity engineering, supplier support and temporary NOC backfill. No cash figure or effort estimate is assumed because the supplier scope and local change window are not established. Management returns with an estimate basis, recurring charges, manual-work impact and displaced work before seeking production implementation funding. The board can protect design/test capacity now; it is not approving the cutover or accepting the exposure.

**Residual-risk decision record.** Complete this after comparing the options and evidence. It records a conditional management decision; it does not make an untested control effective.

| Record field | Operator-specific entry |
|---|---|
| Service and path | **Educational assumption:** one service-assurance domain; adjacent-data need and target permissions remain unknown. |
| Choice and delivery | Option B test first; plan Option C if separation works. Ops Engineering/IAM and supplier test; service owner supplies impact/fallback. |
| Evidence and limits | **Educational assumption:** Level 1 design docs only. No Level 2 review or Level 3 test yet; denial, logging, revocation and fallback unverified. |
| Service impact and cost | **Educational assumption:** manual alarm review and cases require NOC backfill; actual workload, service impact and cash cost remain unknown. |
| Decision authority | Delegated service executive decides within appetite; escalate beyond authority. Board sets appetite, resources and assurance, not operational risk. |
| Conditions and review | Restrict actions until denial, attribution, revocation and NOC visibility pass. Reopen on failure, scope change, lost visibility or supplier delay. |

The dashboard below rolls these service decisions up for portfolio review.

**Compact dashboard: distinguish delivery from risk reduction.** Set thresholds locally; the examples below are not industry benchmarks.

| Outcome | Delivery progress | Demonstrated risk reduction | Limitation or decision trigger |
|---|---|---|---|
| Priority workflow visibility | Register entry completed and owner assigned. | Identity, data and downstream actions independently checked against deployed configuration. | “Documented” without verified reach remains incomplete. |
| Read/action boundary | Design approved or configuration changed. | Negative-path and revocation tests show disallowed actions fail and permitted reads remain observable. | Failed or unsafe test leaves exposure open; restrict use or escalate. |
| Retrieved-content path (where used) | Workflow and source map recorded. | Bounded test sends untrusted, out-of-scope content through the workflow; connector/target denies it and logs source, principal, tool call and result. | One test does not prove general resistance; unobservable supplier paths remain open assurance gaps. |
| Response readiness | Exercise held and actions assigned. | SOC/NOC contain, invoke fallback and capture evidence; corrective actions are retested. | Attendance or a tabletop alone does not prove technical control effectiveness. |
| Supplier control | Notice route and material-change triggers recorded. | Operator verification covers data, retention, supplier access, action limits and memory scope; keep supplier assurance separate. | Contract terms alone do not prove isolation or deletion; missing evidence or usable restriction remains open. |
| Residual-risk governance | Decision records and review dates are current. | Each open exception shows decision state, conditions, expiry and trigger. | Triggered or expired exceptions return to management. |

Keep delegated-authority exposure and response capacity as separate dashboard signals. For authority, show verified read/change reach and where the target enforces the boundary. For response, show time to detect, decide, contain and restore against local service tolerances, with impact and fallback. A tight boundary does not guarantee fast recovery; fast response does not reduce an agent’s reach. Show trends by priority service. Do not roll both into one AI risk score or let delivery progress hide a high-consequence exception. Where evidence is missing, state the decision it blocks.

## Board challenge: deferred patch window

Chapter 4 carries the full patch decision. Here, compare the earliest supported change, waiting with tested controls, and temporary restriction. For each, show service impact, supplier/engineering effort, work displaced and evidence that would change the recommendation. In this scenario, the next safe window is three weeks away.

If version, reach or local impact is unknown, say so. Count a temporary restriction only when its effect on reach and service is evidenced; a changed target date is not a control. State what new threat, failed test or service change reopens the plan.

## Keep the case defensible

Compliance alone does not show that a service can recover, and a platform request must name the control gap. Do not promise “zero risk” or “future-proof.” Show what the investment changes, which dependencies remain and what management must still decide.

## The next twelve months

In the first board cycle, set priority services and run an exercise. Quarterly reviews should show which access limits and service alternatives were tested, what gaps remain and which decisions need to reopen. By year-end, leaders should know which AI-enabled uses can affect services and how response controls perform. Fund work that improves those answers. No plan promises an invulnerable network. The credible commitment is to know which systems can act, limit their authority and test how service continues when a safeguard fails.
