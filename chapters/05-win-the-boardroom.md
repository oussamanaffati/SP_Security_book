# Chapter 5: Board Decisions Before the Next Incident

Before the next incident, the board needs a business decision, not a technology pitch: which service risk to reduce first, what work can be done within engineering and change capacity, and who owns the remaining risk while services continue.

Directors need the likely service and customer impact, what is known and unknown, and which decisions can reduce exposure over the next twelve months.

Chapter 4 set out the operating moves. This chapter turns their evidence into choices a CEO and board can make.

## Speak in service-provider consequences

Board conversations are more effective when they begin with the service, not the tool. Depending on the operator and market, services may support emergency communications, payment services, public agencies, hospitals, enterprises and consumers. The UK Cyber Governance Code notes that cyber incidents can disrupt business continuity and damage customer trust.[18]
Network criticality alone does not prove national impact. Describe affected services, their dependencies and likely consequences; state where evidence is incomplete.

Put the service at stake, the relevant system or workflow, its current access and controls, the proposed action and residual risk into the board statement. If information is incomplete, state what is missing and who will close the gap. Avoid dramatizing uncertainty beyond the evidence.

A generic statement such as “AI is a major new threat” gives the board no decision. The NOC assistant test described in Chapter 1 is more useful: summarization worked, but a broader service account could open vendor cases, pull data from a neighboring domain and propose a change that would reduce NOC visibility. The board discussion can then focus on ownership, identity boundaries and whether the normal change process still applies.

The board-level question is whether the operator has capacity to separate the identities and test how containment affects NOC visibility. If that work cannot happen immediately, the service executive needs to own the residual exposure, with a clear review condition. The requested decision is about service impact, delivery capacity and risk ownership, not model selection.

If the operator relies on a legacy management platform, an external supplier or a narrow maintenance window, explain how that changes the response plan. A broad statement about “the network” is less useful than a clear account of which domain, service and recovery path are involved.

The supplier-enabled diagnostic in Chapter 4 offers another board-level test: who reviews capabilities introduced through routine updates, what evidence the supplier provides about identity and reach, and what operational benefit would be lost if the feature were restricted. Directors can ask whether contract terms, product configuration and existing change controls give the operator meaningful leverage. If not, the service executive should make the residual exposure and limitation in supplier assurance visible, rather than treating the product as covered simply because it was already approved.

## Show why the board is part of the operating model

The board’s role is to set direction, risk appetite, ownership and assurance, not select a model or approve a firewall rule. The CISO and CTO should equip directors to ask whether controls match the operator’s service obligations.

That separation matters when residual risk remains. A service executive with delegated authority owns acceptance within the approved appetite. If the exposure falls outside that boundary, it should be escalated with treatment options and the service consequences of each, not treated as accepted because it appears in a report. The board’s oversight is to test whether appetite, escalation thresholds, resources and assurance are adequate, without taking over routine engineering decisions.

Risk appetite becomes usable only when management translates it into service-level decision rights. A board statement cannot by itself tell an executive which exposures can be accepted, which must be escalated, or what evidence supports the decision. The board should challenge whether those boundaries reflect different service consequences and whether they leave room for safe operational change. A decision to fund one priority before another sets a sequence; it does not, on its own, mean that every deferred exposure has been accepted. The accountable service executive still owns each residual risk within delegated authority.

The UK Cyber Governance Code calls for senior ownership of cyber risk, integration with enterprise risk management, a defined risk appetite and assurance that resources address those risks.[18] It also recommends formal reporting at least quarterly with metrics and tolerances, and at least annual exercises with relevant internal and external stakeholders.[18]
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

An official summary from the Australian Cyber Security Centre and the Australian Institute of Company Directors asks whether frontier AI changes attack-speed assumptions and supplier risk.[26] It also asks whether an operator could keep its most important services running during a serious incident.[26] This is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.[19]
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.[19]
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational operator, prepare a short view by market: the duties that apply, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.[9]
The draft offers a telecom-specific governance signal: it proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities.[9] That proposal is not a current obligation for every operator. It does sharpen a useful board question: which existing body owns AI-related service risk, and what evidence does it review?
Describe something as a regulatory requirement only when it is in force and applies to the entity. Directors need to know what is binding, what is changing, and who is tracking the difference.

## Bring evidence the board can test

A board paper needs enough detail to support challenge, without making directors reconstruct the whole architecture. For each move, show the evidence and the decision it is meant to support.

The starting point is the set of AI-enabled workflows with the greatest potential service impact. For each, the paper can show what it can read, change or trigger, who owns it, which supplier and identity are involved, what is logged, what service is affected and who can suspend it. Gaps should be reported as gaps, not as green status.

The access review should make authority visible: which priority identities are separate from shared accounts, which tools are read-only, which actions remain in normal network change control, and whether revocation has been tested. A count of AI systems cannot show whether their authority is controlled.

Exercise results add another kind of evidence. Did the SOC know who could revoke the identity? Did the NOC know what service might lose visibility? Could the operator move to an alternative mode? Were legal, customer and supplier contacts available? Report which decisions were unclear and whether owners closed the gaps. A June 2026 cross-sector statement by Five Eyes cyber-agency leaders says boards should ensure controls work under incident pressure, not merely exist.[23] An exercise without corrective action is an event, not assurance.

The roadmap should show its dependencies as well as its milestones. Security work competes for engineers, maintenance windows and supplier capacity. If a control must wait for a platform upgrade, state the interim measure and who accepts the remaining risk. For a critical workflow that depends on a metered AI service, include the possible effects of token consumption on cost, performance and availability, and the fallback if the service is degraded or unavailable.[21] If a regulatory deadline changes the sequence, show the date and accountable owner.

A red, amber and green dashboard is useful only when each measure is defined and linked to a decision. Named owners for priority uses, successful access-revocation and fallback tests, and overdue remediation or risks past review date can show whether exposure is better controlled. More deployments do not mean better security.

One distinction is easy to lose in a dashboard: a residual risk accepted within appetite is not the same as an untested control or an exposure with no owner. Acceptance should remain visible against the service, accountable executive, rationale, supporting assurance and conditions for review. A failed test or changed threat picture can reopen the decision; a named owner should not turn an unresolved control gap green by itself.

Aggregation helps directors see patterns, but it can hide a material exception on one service. Report trends at a useful level, while preserving service-level exposures that exceed appetite, lack an owner or depend on untested controls. A board should be able to distinguish accepted risk, work in progress and assurance still missing without reviewing every technical finding. The point of the summary is to make escalation and resource choices possible, not to make unlike risks look uniform.

## Ask for decisions, not general support

A request for “continued support” leaves the choice unclear. A board paper is stronger when it puts a specific decision in front of directors.

1. **Set priority outcomes.** The first decision is which three or four outcomes the operator will pursue over the next twelve months, beginning with services and workflows whose consequences are greatest.
2. **Make ownership explicit.** Each move needs an executive sponsor and operational lead across security, network, IT, procurement or service continuity as required.
3. **Protect delivery capacity.** Staff time, planned change windows and supplier engagement all compete with other operational work. If the board will not fund everything, it should see what moves later and what risk remains open.
4. **Set assurance and escalation.** Agree what evidence management will provide and what changes require earlier escalation. Require management to name the owner for each residual risk, the authority delegated to that owner and the conditions that trigger escalation.

The comparison should include the strongest feasible alternative, not just the preferred investment. In the edge-access example discussed earlier, retaining the shared account preserves the existing arrangement but leaves cross-domain reach; separating the access requires a supplier configuration change and a safe maintenance window. The paper should show the service impact and residual exposure under each path, and identify who can accept that risk. The board can set priorities and resources without taking residual-risk ownership away from management.

The investment case should state what the money buys. It cannot guarantee that an incident will not happen. It should improve the operator’s ability to identify consequential uses, restrict unnecessary authority, contain an incident while maintaining service through a tested fallback, meet applicable duties and restore services. Some costs are people and change capacity, not software. Directors should understand both the risk the plan is meant to reduce and the work it will displace.

If Finance and Operations can substantiate a loss range, show the assumptions. If they cannot, say so and explain the service impact, response dependency and regulatory exposure without putting an unsupported monetary value on them. The decision remains real: invest now, accept the residual risk within the stated appetite, or choose a different sequence.

## The decision behind an accepted patch window

Chapter 4 describes a live core platform with a fixed version available, but a safe change still depends on a maintenance window, a rollback plan and supplier confirmation. The next window is three weeks away. At the service level, the residual risk is accepted, documented and reviewed.

The board does not need to direct the engineering change. It does need to understand which service carries the exposure, who owns the acceptance, how the decision fits the operator’s risk appetite, and when it will be reviewed. If the residual risk is outside that appetite, the executive discussion turns to what capacity or supplier engagement could change the timetable. The decision is about service risk and ownership, not a generic demand to “patch faster.”

That review should distinguish the vulnerability’s presence from the operator’s actual exposure and from control effectiveness during the wait. If those facts are unknown, management should say so rather than describing the risk as controlled. A board asking for faster remediation should ask what engineering capacity and supplier confirmation would make a safe window possible, not treat a changed date as a control. If management proposes a temporary restriction, it should show evidence that the restriction reduces exposure and explain the service effect. The board can resource or prioritize the work; the service executive remains accountable for acceptance within delegated authority. Exposure outside appetite must be escalated, not carried forward by default.

## Keep the case defensible

Compliance does not prove that a service will recover, and a platform request needs a named control gap. Do not promise “zero risk” or “future-proof” on networks that depend on legacy systems, suppliers and continuous service. Keep board language within the evidence: state what is known, what remains uncertain and what decision is needed.

## The next twelve months

The first board cycle can focus on priority services, named owners and an exercise. Quarterly reviews can show which access limits and service alternatives were tested, what gaps remain and who owns the residual risk.

By year-end, leaders should be able to explain which AI-enabled uses can affect services, which response controls have been tested, what residual risk remains and who accepts it within delegated authority. Fund the work that improves those answers. No plan can promise an invulnerable network. The credible commitment is to know which systems can act, limit their authority and test how services continue and recover when a safeguard fails.
