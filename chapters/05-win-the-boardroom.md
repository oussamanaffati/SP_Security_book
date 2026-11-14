# Chapter 5: Board Decisions Before the Next Incident

Before the next incident, the board needs a business decision, not a technology pitch. It must choose which service risk to reduce first, what work fits engineering and change capacity, and who owns the remaining risk while services continue. Directors need the likely service and customer impact. Management should show what is known and unknown, what evidence supports each option, and how it will reduce exposure over the next twelve months.

Chapter 4 set out the operating moves. This chapter turns their evidence into choices for the CEO and board.

## Speak in service-provider consequences

Board conversations are more effective when they begin with the service, not the tool. Depending on the operator and market, services may support emergency communications, payment services, public agencies, hospitals, enterprises and consumers. The UK Cyber Governance Code notes that cyber incidents can disrupt business continuity and damage customer trust.
Network criticality alone does not prove national impact. Describe affected services, their dependencies and likely consequences; state where evidence is incomplete.

Put the service at stake, the relevant system or workflow, its current access and controls, the proposed action and residual risk into the board statement. If information is incomplete, state what is missing and who will close the gap. Avoid dramatizing uncertainty beyond the evidence.

A generic statement such as “AI is a major new threat” gives the board no decision. The NOC composite introduced in Chapter 1 connects an alarm-summary task to cross-domain data, supplier cases and NOC visibility. The board question is whether to protect capacity for a safer authority boundary, not which model to buy.

That choice also has a capacity cost. Reassigning engineers and supplier time to identity separation may delay other network work; not protecting that capacity leaves the broader access in place. The service executive owns any interim residual exposure within delegated authority. The board can resource the decision without taking over acceptance.

The worked board paper later in this chapter compares those choices against service cost and evidence, rather than asking for open-ended support.

If the operator relies on a legacy management platform, an external supplier or a narrow maintenance window, explain how that changes the response plan. A broad statement about “the network” is less useful than a clear account of which domain, service and recovery path are involved.

The supplier-enabled diagnostic in Chapter 4 offers a board-level test: who reviews new capabilities and what evidence confirms the feature’s identity, data reach and action limits? A broad assurance statement does not close the question. Directors can ask whether contract terms and product configuration give the operator timely notice and a way to verify or restrict changes. If not, management must compare available restrictions and operator checks against the diagnostic benefit that would be lost. Procurement and engineering gather the evidence; the service executive owns the service-level risk.

## Show why the board is part of the operating model

The board’s role is to set direction, risk appetite, ownership and assurance, not select a model or approve a firewall rule. The CISO and CTO should equip directors to test whether controls match service obligations and management has evidence to support its choices.

That separation matters when residual risk remains. A service executive with delegated authority owns acceptance within approved appetite; exposure outside it must be escalated with treatment options and service consequences. The board challenges whether appetite, escalation thresholds, resources and assurance are adequate without taking over routine engineering decisions.

Risk appetite becomes usable when management translates it into service-level decision rights: what can be accepted, what must be escalated and what evidence supports each decision. The board should challenge whether those boundaries reflect different service consequences and leave room for safe operational change. Funding one priority sets a sequence; it does not itself accept every deferred exposure. Each residual risk still needs an authorized service owner.

Acceptance describes a specific set of conditions, not indefinite permission. A material change in a supplier feature’s reach, a failed revocation test, new threat evidence or a maintenance window that slips can reopen the decision. The record should say who can reassess it and when exposure must be escalated beyond delegated authority. The board needs to see material exceptions and trends, not approve each operational review.

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

Board reports should say what “tested” means. A document review, configuration inspection, bounded technical test and operational exercise answer different questions; none proves the whole workflow is controlled. State the scope and limitations of the evidence, including whether service visibility and fallback were part of the test. If a live integration cannot be tested safely, name that assurance gap and its owner instead of summarizing it as passed.

Security work competes for engineers, maintenance windows and supplier capacity. If a control must wait for a platform upgrade, state the interim measure and who accepts the remaining risk. CISA and the Canadian Centre for Cyber Security’s guidance on metered AI services notes that token consumption can affect cost, performance and availability. For a critical workflow that depends on such a service, include the exposure and the fallback if service is degraded or unavailable. If a regulatory deadline changes the sequence, show the date and accountable owner.

A green status must not collapse work in progress, an untested control, residual risk accepted by an authorized service executive within approved appetite and delegated authority, and exposure with no authorized owner. The worked dashboard below keeps these states distinct; an owner or completion marker alone is not proof of control effectiveness.

## Ask for decisions, not general support

A request for “continued support” leaves the choice unclear. A board paper is stronger when it puts a specific decision in front of directors.

1. **Set priority outcomes.** The first decision is which three or four outcomes the operator will pursue over the next twelve months, beginning with services and workflows whose consequences are greatest.
2. **Make ownership explicit.** Each move needs an executive sponsor and operational lead across security, network, IT, procurement or service continuity as required.
3. **Protect delivery capacity.** Staff time, planned change windows and supplier engagement all compete with other operational work. If the board will not fund everything, it should see what moves later and what risk remains open.
4. **Set assurance and escalation.** Agree what evidence management will provide and what changes require earlier escalation. Require management to name the owner for each residual risk, the authority delegated to that owner and the conditions that trigger escalation.

The comparison should include the strongest feasible alternative, not just the preferred investment. In the edge-access example discussed earlier, retaining the shared account preserves the existing arrangement but leaves cross-domain reach; separating the access requires a supplier configuration change and a safe maintenance window. The paper should show the service impact and residual exposure under each path, and identify who can accept that risk. The board can set priorities and resources without taking residual-risk ownership away from management.

The risk owner must have authority over the full reach. In the edge example, the account touched edge nodes and parts of the core. The sponsor for the edge rollout may not be delegated to accept consequences for every affected core service. The board paper should make that boundary visible and route the decision to an executive who can own the cross-service impact; the platform owner confirms technical reach but does not automatically become the service-risk owner.

The investment case should state what the money buys. It cannot guarantee that an incident will not happen. It should improve the operator’s ability to identify consequential uses, restrict unnecessary authority, contain an incident while maintaining service through a tested fallback, meet applicable duties and restore services. Some costs are people and change capacity, not software. Directors should understand both the risk the plan is meant to reduce and the work it will displace.

If Finance and Operations can substantiate a loss range, show the assumptions. If they cannot, say so and explain the service impact, response dependency and regulatory exposure without putting an unsupported monetary value on them. The decision remains real: invest now, accept the residual risk within the stated appetite, or choose a different sequence.

## Worked illustrative board decision: NOC assistant

The following paper uses the existing composite NOC-assistant situation. It is an illustrative decision aid, not a real board exchange or a claim that a production incident occurred. Replace bracketed fields with operator evidence; do not report a placeholder as a fact.

**Decision sought.** Protect engineering and supplier capacity to separate the assistant’s read path from its authority to open vendor cases or propose changes. Approve a bounded interim use only if its restrictions can be tested. This asks the board to set priority and capacity, not to accept service-level residual risk on behalf of management.

**Service and exposure.** The assistant summarizes alarms and drafts ticket updates. In the supplied composite, its broader service account can also reach neighboring-domain data, open vendor cases and propose a change that would reduce NOC visibility. The affected service domain is **[name and dependency]**. The deployed identity path, current scope and ability to disable actions are **[evidence status]**. No outcome beyond those stated facts is assumed.

**Options.**

| Option | Benefit | Cost and residual exposure | Evidence needed before treating it as controlled |
|---|---|---|---|
| **A. Defer separation and retain the current account** | Avoids immediate engineering and supplier change; preserves existing workflow. | Retains broader reach and weaker attribution. This is a deliberate service-risk decision, not a neutral scheduling choice. | Confirm actual permissions, service impact and delegated owner. Escalate if the exposure exceeds appetite; record why delay is chosen and what event reopens it. |
| **B. Restrict or pause the action path while retaining only verified read/draft use** | Can reduce authority sooner and preserve some alarm summarization. | Manual vendor-case creation and change handling may increase NOC workload or delay escalation. If read/action rights cannot be separated, a pause may also remove useful visibility. | Demonstrate at the connector and target that actions are refused, read scope is limited, logs identify the principal, and fallback preserves the necessary service view. |
| **C. Separate identities and test the end-to-end path** | Improves attribution and may let the operator suspend action without removing alarm reads. | Requires platform engineering, supplier engagement and a supported test or change window; the target-system behavior may constrain the design. | Verify allowed and denied paths, existing-session revocation, downstream effects, audit correlation, normal change control and service fallback. |

**Management recommendation.** Prefer Option B as an interim treatment only if a bounded test confirms that read/draft use is genuinely separate. In parallel, implement Option C against an agreed service and supplier plan. If the boundary cannot be enforced or verified, do not label the interim control effective: pause the affected capability where service-safe, or present the actual residual exposure to the accountable service executive for a decision within delegated authority. The board should resource the work and receive evidence of progress and effect; it should not convert a delivery decision into risk acceptance.

**Resources and assumptions.** Engineering effort **[estimate and basis]**; supplier work **[scope, cost and commitment]**; NOC manual-work impact **[measure or state not yet measured]**; next supported test/change opportunity **[date and constraints]**. If these are unknown, the paper should say so. A missing estimate is not a reason to imply that work is cost-free or operationally neutral.

**Residual-risk acceptance record.** Complete this only after the service executive has the evidence needed to decide. The record makes ownership and review conditions explicit; it does not prove that a control works.

| Record field | Illustrative entry or operator-specific value |
|---|---|
| Service and exposure | **[service/domain]**; assistant identity has the access described above. Confirm which neighboring data and supplier workflows are in scope. |
| Treatment and implementation owner | Interim restriction **[verified boundary or pause]**; permanent identity separation **[owner/team]**; supplier dependency **[named contact/commitment]**. |
| Control operator and evidence owner | **[platform/IAM team]** operates the control; **[security assurance or independent tester]** provides evidence. Record technical test scope and limitations, not just a policy or supplier statement. |
| Risk acceptor and authority | **[named service executive]**, under **[delegation/threshold]**. The person must have authority over the affected service consequences; cross-service reach may require escalation. |
| Residual exposure and service cost | **[specific access still possible]**; **[visibility or workflow at risk if restricted]**; **[manual workload or supplier delay, measured or explicitly unknown]**. |
| Conditions and expiry | **[permitted data/action scope]** until **[specific expiry or review date set by the operator]**. Do not carry acceptance forward automatically. |
| Reassessment triggers | Failed revocation or negative-path test; expanded identity/data/tool scope; new threat evidence; loss of NOC visibility; supplier change; or a delayed implementation milestone that changes exposure. |
| Escalation | If the risk exceeds approved appetite, the service owner lacks delegated authority, or the full service footprint has no owner, escalate through **[operator governance path]** before treating the risk as accepted. |

The value of this record is not the form. It forces a choice between keeping capability with proven limits, restricting it at an operational cost, or accepting a defined exposure for a stated period. The board can challenge whether the delegated boundary and resources are adequate; management remains accountable for the service-level decision.

**Compact dashboard: distinguish delivery from risk reduction.** Set thresholds locally; the examples below are not industry benchmarks.

| Outcome | Delivery progress | Demonstrated risk reduction | Limitation or decision trigger |
|---|---|---|---|
| Priority workflow visibility | Register entry completed and owner assigned. | Identity, data and downstream actions independently checked against deployed configuration. | “Documented” without verified reach remains incomplete. |
| Read/action boundary | Design approved or configuration changed. | Negative-path and revocation tests show disallowed actions fail and permitted reads remain observable. | Failed or unsafe test leaves exposure open; restrict use or escalate. |
| Response readiness | Exercise held and actions assigned. | SOC/NOC demonstrate authorized containment, service fallback and evidence capture; corrective actions are retested. | Attendance or a tabletop alone does not prove technical control effectiveness. |
| Supplier control | Contract, release notice or contact route updated. | Operator can identify feature changes, verify action scope and enforce a usable restriction. | Supplier assurance without operator-visible evidence remains a stated gap. |
| Residual-risk governance | Acceptance records reviewed. | Each open exposure has an authorized owner, conditions and current evidence; expired or triggered decisions are reopened. | A named owner alone does not make a failed control green. |

A dashboard should show **[operator threshold]**, trend and affected service for each measure. Do not aggregate away a single high-consequence exception. A rise in “completed actions” can coexist with unchanged reach; the board needs both delivery status and evidence that exposure, service consequence or response dependency has actually changed.

## The decision behind an accepted patch window

Chapter 4 works through the operational choice in the supplied patch-window composite: a fixed version exists, but the next safe change window is three weeks away. The board’s role is to challenge the decision, not to set a patch date or accept risk for management. Ask which service carries the exposure; what evidence shows actual reach and interim-control effectiveness; what engineering or supplier capacity could bring a supported change forward; and who owns acceptance in the meantime.

If those facts are incomplete, management should say so. If it proposes a temporary restriction, it should show evidence that the restriction reduces exposure and explain what service work or visibility it may affect. A changed target date is not a control. The service executive remains accountable for residual-risk acceptance within delegated authority; exposure outside appetite must be escalated.

## Keep the case defensible

Compliance does not prove that a service will recover, and a platform request needs a named control gap. Do not promise “zero risk” or “future-proof” on networks that depend on legacy systems, suppliers and continuous service. Keep board language within the evidence: state what is known, what remains uncertain and what decision is needed.

## The next twelve months

The first board cycle can focus on priority services, named owners and an exercise. Quarterly reviews can show which access limits and service alternatives were tested, what gaps remain and who owns the residual risk.

By year-end, leaders should be able to explain which AI-enabled uses can affect services, which response controls have been tested, what residual risk remains and who accepts it within delegated authority. Fund the work that improves those answers. No plan can promise an invulnerable network. The credible commitment is to know which systems can act, limit their authority and test how services continue and recover when a safeguard fails.
