# Chapter 5: Board Decisions Before the Next Incident

Before the next incident, the board needs a business decision, not a technology pitch: which service risk to reduce first, what work can be done within engineering and change capacity, and who owns the remaining risk while services continue.

Directors need the likely service and customer impact, what is known and unknown, and which decisions can reduce exposure over the next twelve months.

Chapter 4 set out the operating moves. This chapter turns their evidence into choices a CEO and board can make.

## Speak in service-provider consequences

Board conversations are more effective when they begin with the service, not the tool. Depending on the operator and market, services may support emergency communications, payment services, public agencies, hospitals, enterprises and consumers. The UK Cyber Governance Code notes that cyber incidents can disrupt business continuity and damage customer trust.[18]
Network criticality alone does not prove national impact. Describe affected services, their dependencies and likely consequences; state where evidence is incomplete.

Put the service at stake, the relevant system or workflow, its current access and controls, the proposed action and residual risk into the board statement. If information is incomplete, state what is missing and who will close the gap. Avoid dramatizing uncertainty beyond the evidence.

A generic statement such as “AI is a major new threat” gives the board no decision. A service-based account is more useful: a service-assurance workflow might read alarms and subscriber-linked service data, but cannot change network configuration. The service owner and supplier manager can map the dependency and agree a safe isolation test before the next change window.

If the operator relies on a legacy management platform, an external supplier or a narrow maintenance window, explain how that changes the response plan. A broad statement about “the network” is less useful than a clear account of which domain, service and recovery path are involved.

## Show why the board is part of the operating model

The board’s role is to set direction, risk appetite, ownership and assurance, not select a model or approve a firewall rule. The CISO and CTO should equip directors to ask whether controls match the operator’s service obligations.

The UK government’s Cyber Governance Code of Practice recommends that boards agree senior ownership of cyber risks, align them with enterprise risk management, define risk appetite and gain assurance that resources address those risks.[18]
The Code also recommends at least quarterly formal reporting with suitable metrics and tolerances, and at least annual incident exercises involving relevant internal and external stakeholders.[18]
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

A guide published by the Australian Cyber Security Centre on 8 September 2026, in partnership with the Australian Institute of Company Directors, asks boards whether frontier AI changes assumptions about attack speed, supplier risk and the ability to keep critical services operating.[26] It is cross-sector guidance, not telco-specific law or evidence of an operator incident. For a service provider, translate those questions into named services, supplier paths and tested fallback.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.[19]
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.[19]
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational operator, prepare a short view by market: the duties that apply, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.[9]
The draft offers a telecom-specific governance signal: it proposes board approval of an internal AI policy and a board-approved committee to oversee implementation for covered entities.[9] That proposal is not a current obligation for every operator. It does sharpen a useful board question: which existing body owns AI-related service risk, and what evidence does it review?
Describe something as a regulatory requirement only when it is in force and applies to the entity. Directors need to know what is binding, what is changing, and who is tracking the difference.

## Bring evidence the board can test

A board pack should be short enough to discuss and specific enough to challenge. For each move, give directors evidence they can test and a decision they can make.

Start with the AI-enabled workflows that could have the greatest service impact. Show what each can read, change or trigger, who owns it, which supplier and identity are involved, what service is affected, what is logged and who can suspend it. Report gaps as gaps, not as green status.

Next, report the access boundaries. Which priority identities are separate from shared accounts? Which tools are read-only? Which actions follow the normal network change process? Has revocation been tested? Counting AI systems does not prove that their authority is controlled.

Then report what the exercise revealed. Did the SOC know who could revoke the identity? Did the NOC know what service might lose visibility? Could the operator move to an alternative mode? Were legal, customer and supplier contacts available? Report decision gaps and whether owners closed them. A June 2026 cross-sector statement by Five Eyes cyber-agency leaders says boards should ensure controls work under incident pressure, not merely exist.[23] An exercise without corrective action is an event, not assurance.

Finally, set out the roadmap and its constraints. Security work competes for engineers, maintenance windows and supplier capacity. Put those dependencies beside the milestone. If a control must wait for a platform upgrade, state the interim measure and who accepts the remaining risk.

For a critical workflow that depends on a metered AI service, show how token consumption could affect cost, performance and availability.[21] State what fallback remains if the service is degraded or unavailable. If a regulatory deadline changes the sequence, show the date and accountable owner.

A red, amber and green dashboard is useful only if each measure is defined and linked to a decision. Measures should show whether exposure is better controlled: named owners for priority uses, successful access-revocation and fallback tests, and overdue remediation or risks past their review date. More deployments do not mean better security.

## Ask for decisions, not general support

“Continued support” is not a decision request. Put a specific choice in front of the board.

1. **Approve the priorities.** Confirm the three or four outcomes the operator will pursue over the next twelve months, starting with services and workflows that carry the greatest consequence.
2. **Assign accountable owners.** Give each move an executive sponsor and an operational lead across security, network, IT, procurement or service continuity as required.
3. **Protect capacity.** Approve the staff time, planned change windows and supplier engagement needed to deliver the first tranche. If the board will not fund everything, show what moves later and what risk stays open.
4. **Set assurance and residual-risk acceptance.** Agree what evidence returns each quarter, what triggers an earlier escalation, and which executive owns acceptance of residual risk within the approved appetite.

The investment case should state what the money buys. It cannot guarantee that an incident will not happen. It should improve the operator’s ability to identify consequential uses, restrict unnecessary authority, contain an incident while maintaining service through a tested fallback, meet applicable duties and restore services. Some costs are people and change capacity, not software. Directors should understand both the risk the plan is meant to reduce and the work it will displace.

If Finance and Operations can substantiate a loss range, show the assumptions. If they cannot, say so and explain the service impact, response dependency and regulatory exposure without putting an unsupported monetary value on them. The decision remains real: invest now, accept the residual risk within the stated appetite, or choose a different sequence.

## A composite board illustration

The following is a composite illustration, not a real board exchange. A provider has reviewed several AI-enabled workflows. One assistant can read service alarms and draft recommendations. It cannot apply network changes, but it uses a supplier connection that has not yet been tested for isolation. A tabletop also shows that the NOC and SOC do not share a clear after-hours decision owner.

**CEO:** “If we isolate this supplier link during a fault, what operational visibility could we lose, and who can authorize the decision after hours?”

**CISO:** “We have not tested that isolation path. The assistant can read alarms and service data, but it cannot change network configuration. The exercise also found no clear after-hours decision owner. We will map the fallback and validate the isolation path before recommending a boundary.”

**CTO:** “We need agreement on the decision owner and capacity for a controlled isolation and fallback test. We will also review the other high-impact workflows. At the next quarterly review, we can report the test result, remaining risk and proposed next priority.”

The exchange gives the board evidence, a decision and a point at which to check progress, without promising zero risk or predicting an outage.

## Keep the case defensible

Compliance does not prove that a service will recover, and a platform request needs a named control gap. Do not promise “zero risk” or “future-proof” on networks that depend on legacy systems, suppliers and continuous service. Keep board language within the evidence: state what is known, what remains uncertain and what decision is needed.

## The next twelve months

Start with priority services, named owners and an exercise. Bring initial findings to the risk committee; quarterly reviews should show which access limits and service alternatives were tested, what gaps remain and who owns the risk.

By year-end, leaders should know which AI-enabled uses can affect service, what response has been tested, and what residual risk remains and who accepts it. Fund the work to improve those answers. No plan can promise an invulnerable network. The credible commitment is to know which systems can act, limit their authority and test how services continue and recover when a safeguard fails.
