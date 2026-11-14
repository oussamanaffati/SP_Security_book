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

Translate these boundaries into service-specific thresholds: which impacts require escalation, what evidence supports a decision and what changes reopen it. A supplier reach change, failed revocation test, new threat evidence or slipped window can trigger a review. Directors should challenge whether thresholds reflect service consequences without approving each operational recheck.

Routine reporting and event-driven review do different jobs. The agreed board cadence shows trends, funding progress and assurance; it should not be the only route for a material change. A supplier changes retention or access, a revocation test fails, a safe window slips or a service fallback changes: each can make the previous decision stale. Define the signal that reopens the decision, the evidence management needs and the threshold for board escalation. If every technical change goes straight to directors, oversight becomes operational approval. If all changes wait for the next board pack, management may rely on an outdated boundary. Set the response interval from service tolerance and delegated authority, not a universal notification clock. Report exceptions through the normal board cycle unless they change appetite, resources or assurance sooner.

Funding one priority sets a sequence; it does not settle the exposures deferred to a later cycle. Management should show which services remain affected, what treatment is feasible and when the evidence or service conditions require a new decision.

The UK Cyber Governance Code calls for senior ownership of cyber risk, integration with enterprise risk management, a defined risk appetite and assurance that resources address those risks. It also recommends formal reporting at least quarterly with metrics and tolerances, and at least annual exercises with relevant internal and external stakeholders.
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

An official summary from the Australian Cyber Security Centre and the Australian Institute of Company Directors asks whether frontier AI changes attack-speed assumptions and supplier risk. It also asks whether an operator could keep its most important services running during a serious incident. This is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational operator, prepare a short view by market: the duties that apply, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.
The draft offers a telecom-specific governance signal: it proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities. That proposal is not a current obligation for every operator. It does sharpen a useful board question: which existing body owns AI-related service risk, and what evidence does it review?
Describe something as a regulatory requirement only when it is in force and applies to the entity. Directors need to know what is binding, what is changing, and who is tracking the difference.

## Bring evidence the board can test

A board paper needs enough detail to support challenge, without making directors reconstruct the whole architecture. For each move, show the evidence and the decision it is meant to support.

The starting point is the set of AI-enabled workflows with the greatest potential service impact. For each, the paper can show what it can read, change or trigger, who owns it, which supplier and identity are involved, what is logged, what service is affected and who can suspend it. Gaps should be reported as gaps, not as green status.

Where a consequential service decision depends on joined operational records, Chapter 2’s source-contract check can provide one narrow evidence point: whether sources, freshness and conflicts are surfaced in the output. Report its scope and limits. It does not prove the identity boundary, tool restrictions or the agent’s general accuracy.

The access review should make authority visible: which priority identities are separate from shared accounts, which tools are read-only, which actions remain in normal network change control, and whether revocation has been tested. A count of AI systems cannot show whether their authority is controlled.

Exercise results add another kind of evidence. Did the SOC know who could revoke the identity? Did the NOC know what service might lose visibility? Could the operator move to an alternative mode? Were legal, customer and supplier contacts available? Report which decisions were unclear and whether owners closed the gaps. A June 2026 cross-sector statement by Five Eyes cyber-agency leaders says boards should ensure controls work under incident pressure, not merely exist. An exercise without corrective action is an event, not assurance.

Chapter 4 defines the evidence levels. For each board claim, name the level, service path and limitation, including whether visibility and fallback were covered. If a live integration cannot be tested safely, report the boundary that remains unknown and the decision it constrains; do not label it passed.

Security work competes for engineers, maintenance windows and supplier capacity. If a control must wait for a platform upgrade, show the interim measure, its tested effect and the next decision trigger. CISA and the Canadian Centre for Cyber Security’s guidance on metered AI services notes that token consumption can affect cost, performance and availability. For a critical workflow, include the fallback if service degrades or becomes unavailable. If a regulatory deadline changes the sequence, show its date and tracking lead.

The dashboard must distinguish work in progress, a control tested effective, exposure accepted under defined conditions, and unresolved exposure without a valid decision. The worked dashboard keeps these states distinct; an owner or completion marker alone is not proof of control effectiveness.

## Ask for decisions, not general support

A request for “continued support” leaves the choice unclear. A board paper is stronger when it puts a specific decision in front of directors.

1. **Set priority outcomes.** The first decision is which three or four outcomes the operator will pursue over the next twelve months, beginning with services and workflows whose consequences are greatest.
2. **Name delivery leads.** Each move needs an executive sponsor and an operational lead across security, network, IT, procurement or service continuity as required.
3. **Protect delivery capacity.** Staff time, planned change windows and supplier engagement all compete with other operational work. If the board will not fund everything, it should see what moves later and what risk remains open.
4. **Set assurance and escalation.** Agree what evidence management will provide and which service impacts, failed tests or changed dependencies require an earlier review.

The comparison should include the strongest feasible alternative. Retaining the shared edge/core account preserves the current arrangement but retains cross-domain reach; separation needs a supplier change and safe window. Show service impact, fallback and displaced work under both paths. If the reach crosses service domains, route the decision to an executive whose delegation covers the full impact; technical confirmation of reach does not confer service-risk authority.

The investment case should state what the money buys. It cannot guarantee that an incident will not happen. It should improve the operator’s ability to identify consequential uses, restrict unnecessary authority, contain an incident while maintaining service through a tested fallback, meet applicable duties and restore services. Some costs are people and change capacity, not software. Directors should understand both the risk the plan is meant to reduce and the work it will displace.

If Finance and Operations can substantiate a loss range, show the assumptions. If they cannot, explain service impact, response dependency and regulatory exposure without an unsupported monetary value. The decision remains real: fund the work now, choose another sequence or resource an interim treatment.

### Stage funding without approving the exposure

When the supplier cost, engineering effort or safe test window is still unknown, avoid presenting one fixed budget as if the delivery path were settled. The board can fund design and test capacity first, including supplier time and NOC backfill, while keeping authority at its current or more restricted level. Management then returns with the tested boundary, service impact, rollback path and an implementation estimate before asking for deployment funding.

This staged route limits the chance of funding a design that cannot be deployed safely, but it requires another decision and may delay the diagnostic benefit. Full funding at once can reserve scarce supplier or engineering capacity, but commits before the evidence is complete. Withholding all funds avoids new spend and leaves the current exposure and manual workload in place. Where current reach creates a material service concern, do not wait for the next budget decision to apply a safe interim restriction. Release the larger implementation budget only when local testing shows what the change permits, denies and does to service visibility; if the test fails, return with a safer restriction or a revised delivery path.

## Board decision: NOC assistant

Use the NOC assistant described in Chapter 1 as the worked board decision. Its service account can reach neighboring-domain data, open vendor cases and propose a visibility-reducing change; that does not mean the proposed change has been carried out. Replace bracketed fields with evidence from the operator’s environment.

**Decision sought.** Protect engineering and supplier capacity to separate the assistant’s read path from its authority to open vendor cases or propose changes. Permit bounded interim use only if its restrictions can be tested.

**Service and exposure.** The affected service domain and dependencies are **[name and evidence]**. The deployed identity path, data scope, action path and ability to disable actions are **[verified, assumed or unknown]**. The facts above describe possible authority, not a completed network change.

**Options.**

| Option | Service effect and trade-off | Evidence gate |
|---|---|---|
| **A. Keep the shared account** | Avoids immediate change and preserves workflow, but retains broad reach and weak attribution. Deferral is a service-risk choice, not a neutral schedule decision. | Verify permissions and service impact; apply Chapter 5’s authority model and record the trigger that reopens deferral. |
| **B. Restrict or pause actions** | Retain only verified read/draft use if separable. Manual vendor cases and changes add NOC work; a full pause may also remove useful visibility. | At connector and target, prove actions are refused, read scope is limited, principal is logged and fallback preserves service view. |
| **C. Separate identities** | Can improve attribution and suspend action without removing alarm reads; needs engineering, supplier work and a supported window. | Test allowed/denied paths, existing-session revocation, downstream effects, audit correlation, change control and service fallback. |

**Management recommendation.** Prefer Option B only if a Level 3 test confirms that read/draft use is separate. In parallel, plan Option C against a supported supplier path. If the boundary cannot be enforced or verified, pause the capability where service-safe and take the unresolved scope and service consequence to the service executive. Set the first review at the next supplier/test milestone; if the boundary fails, return to the pause option and reassess service impact.

**Resources and assumptions.** Engineering effort **[estimate and basis]**; supplier work and recurring/usage charges **[scope, cost basis and commitment]**; transition or exit cost **[estimate or state unknown/not applicable]**; NOC manual-work impact **[measure or state not yet measured]**; next supported test/change opportunity **[date and constraints]**. If these are unknown, the paper should say so. A missing estimate is not a reason to imply that work is cost-free or operationally neutral.

**Residual-risk decision record.** Complete this after comparing the options and evidence. It records a conditional management decision; it does not make an untested control effective.

| Record field | Operator-specific entry |
|---|---|
| Service and path | **[services/dependencies]**; **[identity, data and action reach: verified, assumed or unknown]**. |
| Choice and delivery | **[option; strongest alternative/reason]**; **[delivery/control/evidence leads]**; **[supplier dependency and date]**. |
| Evidence and limits | **[Chapter 4 level, test scope/result]**; **[limitations and unverified claims]**. |
| Service impact and cost | **[reach remaining]**; **[visibility/fallback]**; **[NOC workload, continuity impact and effort/cost basis or unknown]**. |
| Decision authority | **[service executive with delegation across affected services]**; **[appetite or escalation path]**. |
| Conditions and review | **[permitted scope, expiry/date]**; **[trigger, next evidence and review lead]**. |

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

A dashboard should show **[operator threshold]**, trend and affected service. Do not average away a high-consequence exception: completed actions can rise while reach stays unchanged. Report delivery and evidence that exposure or response dependency changed.

## Board challenge: deferred patch window

Chapter 4 carries the full patch decision. Here, compare the earliest supported change, waiting with tested controls, and temporary restriction. For each, show service impact, supplier/engineering effort, work displaced and evidence that would change the recommendation. In this scenario, the next safe window is three weeks away.

If version, reach or local impact is unknown, say so. Count a temporary restriction only when its effect on reach and service is evidenced; a changed target date is not a control. State what new threat, failed test or service change reopens the plan.

## Keep the case defensible

Compliance alone does not show that a service can recover, and a platform request must name the control gap. Do not promise “zero risk” or “future-proof.” Show what the investment changes, which dependencies remain and what management must still decide.

## The next twelve months

In the first board cycle, set priority services and run an exercise. Quarterly reviews should show which access limits and service alternatives were tested, what gaps remain and which decisions need to reopen. By year-end, leaders should know which AI-enabled uses can affect services and how response controls perform. Fund work that improves those answers. No plan promises an invulnerable network. The credible commitment is to know which systems can act, limit their authority and test how service continues when a safeguard fails.
