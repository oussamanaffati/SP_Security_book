# Chapter 5: Board Decisions Before the Next Incident

A CISO does not earn board support by saying AI is important. Directors need to set priorities, name accountable owners, fund the work and decide what residual risk they are prepared to accept while the network continues to change.

This is a business and service-continuity discussion, not a technology pitch. The board needs to understand possible effects on services, customers and regulatory obligations; what is known and unknown; and which decisions can reduce exposure over the next twelve months.

Chapter 4 set out four moves: identify AI-enabled workflows with material access, limit their authority, rehearse response and fund the roadmap. This chapter translates that plan into choices a CEO and board can make.

## Speak in service-provider consequences

Start with the service, not the tool. A network operator may support emergency communications, payment services, public agencies, hospitals, major enterprises and consumers. The UK Cyber Governance Code notes that cyber incidents can disrupt business continuity and damage customer trust.[18]
The exact dependency varies by country and operator. Do not claim national impact just because a network is important. Identify which service or customer group depends on the system in question, and how an incident could affect them.

A useful board statement covers five points: the service at stake; the system or workflow that could affect it; current access and controls; the proposed action; and the residual risk afterward. If information is incomplete, say so and name the next step to close the gap. Do not make uncertainty sound more dramatic than the evidence supports.

For example, “AI is a major new threat” does not tell the board what to decide. “This service-assurance workflow can read alarms and subscriber-linked service data. It cannot change network configuration today. We have not yet proved that we can isolate its supplier connection without losing operational visibility. We will assess the dependency and agree a safe test plan before the next change window” gives directors a service, a control boundary, a gap and a next step without implying that isolation is simple.

Avoid presenting every possible harm as if it is equally likely. Put the most important service dependencies first. If the operator relies on a legacy management platform, an external supplier, or a narrow maintenance window, explain how that changes the response plan. A broad statement about “the network” is less useful than a clear account of which domain, service and recovery path are involved.

## Show why the board is part of the operating model

The board is not there to choose a model or approve a firewall rule. It is there to set direction, risk appetite, ownership and assurance. The CISO and CTO should give directors a clear way to ask whether the operator’s controls match its service obligations.

The UK government’s Cyber Governance Code of Practice recommends that boards agree senior ownership of cyber risks, align them with enterprise risk management, define risk appetite and gain assurance that resources address those risks.[18]
The Code also recommends at least quarterly formal reporting with suitable metrics and tolerances, and at least annual incident exercises involving relevant internal and external stakeholders.[18]
It is UK guidance, not a universal legal requirement. Its value here is the operating principle: cyber risk belongs in existing governance, with visible owners and a reporting cadence.

CISA’s Cross-Sector Cybersecurity Performance Goals 2.0, released in December 2025 for critical-infrastructure owners and operators, adds governance, accountability and risk management to its measurable, outcome-oriented baseline.[19]
CISA describes the goals as a baseline for guiding investment, benchmarking progress and reducing risk measurably across IT and OT environments.[19]
That is a useful way to frame the ask: fund outcomes and evidence, not a collection of AI-branded products.

For a multinational service provider, regulation needs the same discipline. Bring a short jurisdiction-by-jurisdiction view of applicable duties, reporting thresholds, accountable owners and dates. Separate binding requirements from consultations or emerging guidance. TRAI’s October 2026 AI guidelines are a draft consultation, not a final rule.[9]
Do not tell the board “the regulator requires this” unless the requirement is in force and applies to that entity. The board needs to know what is binding, what is changing, and who is tracking the difference.

## Bring evidence the board can test

A board pack should be short enough to discuss and specific enough to challenge. Four types of information make the four moves tangible.

First, show the AI-enabled workflows with the greatest potential service impact and what each can read, change or trigger. Include the owner, supplier, identity, affected service, logging and who can suspend it. Report gaps as gaps, not as green status.

Second, show changes to access. Which priority identities are separate from shared accounts? Which tools are read-only? Which actions follow the normal network change process? Has revocation been tested? Counting AI systems does not prove that their authority is controlled.

Third, report what the exercise revealed. Did the SOC know who could revoke the identity? Did the NOC know what service might lose visibility? Could the operator move to an alternative mode? Were legal, customer and supplier contacts available? Report decision gaps and whether owners closed them. An exercise without corrective action is an event, not assurance.

Fourth, show the roadmap and its constraints. Security work competes for engineers, maintenance windows and supplier capacity. Put those dependencies beside the milestone. If a control must wait for a platform upgrade, state the interim measure and who accepts the remaining risk. If a regulatory deadline changes the sequence, show the date and accountable owner.

Do not bring a dashboard of unexplained red, amber and green indicators. Define each measure and the decision it should trigger. Measures should show whether exposure is better controlled: priority uses with named owners, tested access revocation, exercised service alternatives, overdue remediation or risks past their review date. More deployments do not mean better security.

## Ask for decisions, not general support

“Please support our cybersecurity program” is not a decision. Ask for the choices the board can actually make.

1. **Approve the priorities.** Confirm the three or four outcomes the operator will pursue over the next twelve months, starting with services and workflows that carry the greatest consequence.
2. **Name accountable owners.** Give each move an executive sponsor and an operational lead across security, network, IT, procurement or service continuity as required.
3. **Protect capacity.** Approve the staff time, planned change windows and supplier engagement needed to deliver the first tranche. If the board will not fund everything, show what moves later and what risk stays open.
4. **Set the assurance cadence.** Agree what evidence returns each quarter, what triggers an earlier escalation, and which executive owns acceptance of residual risk.

The investment case should state what the money buys. It cannot guarantee that an incident will not happen. It should improve the operator’s ability to see consequential uses, restrict unnecessary authority, respond safely, meet applicable duties and restore services. Some costs are people and change capacity, not software. Directors should understand both the risk the plan is meant to reduce and the work it will displace.

Never invent a financial loss estimate to make the case sound stronger. If Finance and Operations can substantiate a range, show the assumptions. If they cannot, explain the service impact, response dependency and regulatory exposure without pretending those have a precise price. The decision is still real: invest now, accept the residual risk, or choose a different sequence.

## A composite board illustration

The following is a composite illustration, not a real board exchange. A provider has reviewed several AI-enabled workflows. One assistant can read service alarms and draft recommendations. It cannot apply network changes, but it uses a supplier connection that has not yet been tested for isolation. A tabletop also shows that the NOC and SOC do not share a clear after-hours decision owner.

**CEO:** “Are you telling us an AI agent will take down the network?”

**CISO:** “No. We have no evidence to make that claim. We have evidence that this workflow can read operational data, and we have not proved that its supplier path can be isolated without affecting visibility. Our exercise found a gap in who can authorize that step at night.”

**CTO:** “We are asking you to approve the first phase: assign the decision owner, test isolation and fallback in a controlled window, and fund the access review for the other high-impact workflows. At the next quarterly review, we will report the test result, the remaining risk and the next service domain in sequence.”

That answer is credible because it is bounded. It does not promise zero risk or predict an outage. It gives the board evidence, a decision and a point at which to check progress.

## Language that weakens the case

Avoid “AI will cause a national outage.” It is an unsupported prediction unless the evidence establishes that specific scenario. Avoid “we are compliant, so we are safe.” Compliance is not a substitute for knowing what an agent can access or how a service will recover. Avoid “we need a platform” before explaining the control gap it would close. Avoid “zero risk” and “future-proof”; neither is an honest commitment in a network that depends on legacy systems, suppliers and continuous service.

Use language the operator can support with evidence: name the service, access path, test results, unresolved questions and decision needed. That is more useful than a dramatic claim.

## The next twelve months

The board need not wait for a major incident to create urgency. In the next 90 days, the CISO and CTO can agree priority services, name owners, bring initial findings to the risk committee and schedule an exercise. In later quarters, they can narrow access, test service alternatives, close exercise gaps and return with decisions about remaining risk.

At the end of the year, leadership should be able to identify the AI-enabled uses with material access to services, name their owners, describe what response has been tested and state what risk remains and who accepts it.

Fund the work needed to answer those questions and review progress each quarter. Do not promise an invulnerable network. Commit to understanding what can act, limiting its authority and protecting service when something goes wrong.
