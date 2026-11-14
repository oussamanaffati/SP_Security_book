# Chapter 3: The Threat Moves Faster Than the Operator Can Respond

The response gap is not one clock. It includes detection, decision, safe action and restoration. An operator can identify an event quickly and still lose time resolving who can authorize containment without disrupting service.

The security operations center (SOC) may see an alert while the NOC sees a planned change. Identity and access management (IAM) may be able to revoke a credential, and a supplier may hold platform details. Without a clear decision path, an attacker may retain access while the operator assesses service impact.

Chapter 2 mapped where exposure can enter and spread. The operator needs to detect activity, decide and act before the attacker reaches its next objective, without creating a second incident through unsafe containment.

## Threat activity can accelerate without being fully autonomous

The Canadian Centre for Cyber Security’s 26 October 2026 bulletin is cross-sector evidence, not a telecom incident or a universal attack timeline. It says attacks are not yet fully autonomous: humans still choose targets, set objectives and oversee operations. For some activity attributed by the bulletin to Storm-0940, the time from target selection to privileged cloud access was less than three hours.

In a 15 October 2026 advisory, CERT-In reported that tools using AI agents shortened the time from initial access to impact from days to a few hours in a financially motivated campaign against Indian entities. The advisory did not identify those organizations as telecom operators; it also reported parallel agent operations and repeat attacks within days after incomplete remediation.

A separate 4 November advisory from CERT-In’s finance-sector incident-response team reported attacks against Indian BFSI entities timed to holidays, weekends and other low-monitoring windows, including after incomplete remediation. This financial-sector evidence supports testing off-hours decision authority and escalation, not a claim about telco incidents.

Neither report establishes an operator response deadline. Faster adversary activity does not make every emergency change safe on a live service.

Chapter 1’s composite patch-window scenario shows the second clock. Security has the advisory and fixed version, but the network team needs a maintenance window, rollback plan and supplier confirmation. The next available window is three weeks away; the residual risk is accepted at the service level, documented and reviewed. Waiting leaves the vulnerability in scope for longer. Changing a live core platform without the required support and rollback conditions could create service risk of its own.

Speed alone is not the measure. The operator needs a clear view of the threat and exposure, which controls remain effective while the change is prepared, who owns residual risk and what evidence would reopen the decision. The planned date should be reviewed if threat or exposure changes, while any emergency change still needs a supported rollback and service-impact assessment.

Detection and response are different capabilities. A dashboard can show an event, but people still need authority and context to decide whether to revoke an identity, isolate a host, block a supplier connection or keep a service running in reduced mode.

## Response runs on several timelines

Incident response is often described as a technical sequence: detect, investigate, contain, recover. In practice, workstreams overlap. The NOC checks whether an alarm matches a real network change; the SOC assesses whether the activity is malicious; IAM may need to disable an account. Service assurance estimates customer and service impact, while legal, regulatory and communications teams work against their own deadlines.

At the same time, the network cannot wait for every team to finish its analysis. Nor can the operator treat every system as disposable. A management platform may support several network domains. An identity may be shared across automation jobs. A supplier connection may be needed to restore a service even as the supplier helps investigate it. Availability changes the containment decision.

It helps to separate four response intervals:

- **Detection:** from the first relevant signal to recognition that the activity may be malicious.
- **Decision:** from that recognition to an authorized containment choice.
- **Action:** from the decision to safe execution and confirmation of the result.
- **Continuity and recovery:** from containment to the safe restoration of affected services.

A fast SOC does not guarantee a fast response if approval is slow. Quick isolation is not success if it breaks a critical workflow or removes telemetry needed to understand the incident. An exercise is more informative when it compares the time to detect, authorize, act safely and restore service with tolerances agreed in advance by the service owner. Those tolerances depend on continuity needs, available containment options and applicable notification deadlines; one target will not fit every service domain. Record the service impact and the reason for each delay as well as elapsed time. Otherwise, one overall response figure cannot show whether the constraint is missing evidence, unclear authority, a supplier dependency or an untested fallback.

**Illustrative response-gap review.** Use this after an exercise or incident review to link a delay to a fix. The table sets no universal time target.

| Interval | Diagnostic question | Evidence needed before closing the gap |
|---|---|---|
| Detection | Did the right team receive a usable alert with the identity, source and affected service visible? | Trace a representative event from source to SOC/NOC; record where context or routing was missing and confirm the corrected alert path. |
| Decision | Was the delay caused by missing service context, unclear authority or no agreed containment trigger? | Name the decision owner and conditions; exercise the choice with the service impact and available options in view. A procedure or tabletop alone does not prove technical containment. |
| Action | Did permissions, an existing session, supplier access or a supported change window delay the chosen action? | Verify the action and revocation path end to end in a safe test or supported window; record supplier and engineering dependencies, plus rollback evidence. |
| Continuity and recovery | Did containment remove monitoring, a supplier workflow or another path needed to restore service? | Have NOC/service assurance demonstrate the fallback and service owner compare restoration evidence with the locally agreed tolerance. |

For every gap, assign an owner, interim treatment, required supplier or engineering effort, and a retest. A response target that rewards speed alone can encourage unsafe isolation. If no tested option meets the service tolerance, show the trade-off to the accountable service executive and record the residual risk rather than marking the response “on target.”

CERT-In’s April 2026 advisory recommends tabletop exercises for five simultaneous incidents rather than a single incident, explicitly modelling AI-driven scenarios. That recommendation is Indian cross-sector guidance, not a telco standard or universal target. For an operator, the test is whether NOC, SOC, IAM and service teams can still make timely, service-safe decisions when their attention is split.

The SOC assesses the evidence and likely attack path; the NOC knows which systems carry live operations, what maintenance is under way, and what isolation could do to service. Agree who resolves a conflict between those views and who can authorize the next step when there is no time for a long discussion.

## The SK Telecom response had distinct timelines

The South Korean Ministry of Science and ICT (MSIT) investigation into SK Telecom’s 2025 breach shows that response includes more than containment. MSIT reports that SK Telecom detected abnormally large outbound traffic at 11:20 p.m. on 18 April 2025 and notified KISA at 4:46 p.m. on 20 April; the Ministry said this exceeded the statutory 24-hour reporting window.

That is a reporting timeline, not a measure of containment time. The public-private investigation team was established on 23 April and inspected all 42,605 SK Telecom servers through 27 June; its final findings identified 28 infected servers.
The inspection end date is not a containment timeline. Keep initial notification, containment and forensic scoping as separate measures; the public findings do not make them interchangeable.

The customer response had its own operational demands. In its preliminary findings, the Ministry encouraged subscribers to replace their USIM cards or use a protection service, and urged the operator to expand service channels and add a reservation system so more customers could be protected promptly.
These reports describe a breach-response timeline, not a network outage. They show how an incident can create a second workload: protecting customers, handling enquiries and changing business operations while the technical investigation continues.

CISA, the FBI, and partner agencies recommend a service-outage communications plan with triggers, escalation paths, and templates for status pages, customer and partner notices, and regulatory communications. They advise frequent updates on what is known, unknown and under investigation, while protecting operational security and aligning with law-enforcement and containment efforts. The guidance does not describe the SK Telecom breach; for an operator, it can inform planning when defensive isolation changes service availability.

The practical lesson is to assign owners for notification, forensic scoping and customer protection who can work in parallel while containment continues.

## Containment is a service decision

Containment decisions at a service provider have more than one consequence. Cutting a compromised supplier connection may slow recovery. Disabling a shared identity may stop a legitimate monitoring workflow. Isolating a management host may reduce an attacker’s access but also remove a source of operational visibility.

That does not mean the operator should wait. It means the available actions should be designed and authorized in advance. The Canadian Cyber Centre recommends deciding in advance who may isolate an account, application, network or service, and practising incidents that unfold within hours rather than days. It also recommends identifying essential functions, defining pre-authorized isolation steps and testing safe manual or alternative operations.

For a provider, translate that guidance into clear criteria: what evidence is enough, which actions the SOC can take alone, when the NOC or service owner must approve, and what fallback keeps essential services running.

The emergency route needs a real mandate, service context and a record of the decision. An incident-commander title cannot substitute for authority, just as a change process built for scheduled work cannot handle every urgent isolation.

## The NOC assistant makes authority visible

The Chapter 1 NOC-assistant composite sets up this response question: can the operator disable the assistant’s broad service account without losing essential visibility? It is illustrative, not a production incident.

Before an incident, verify whether action rights can be stopped independently of alarm reads and vendor-case handling. Name the fallback, who can invoke it, and who owns any temporary exposure. A network change still follows normal change control.

**Illustrative live-incident decision card: NOC assistant.** Adapt this to the operator’s incident authority and map the role names to local equivalents before use. It is not an authorization by itself, and a tabletop cannot prove that its technical steps work.

Use the response-gap review earlier in this chapter after an exercise or incident to assign follow-up; this card supports live containment, not post-event scoring.

| Decision point | Evidence and question | Role that contributes or decides |
|---|---|---|
| Establish what happened | Which identity and tool acted? Is there evidence of an unauthorized request or only a proposed change? Preserve source alarms, connector records and target-system events. | SOC leads evidence assessment; platform/IAM teams identify the principal and session scope. |
| Bound the authority | Can the operator stop action rights separately from alarm reads and vendor-case handling? Does revocation terminate existing sessions as well as block new calls? | Identity and platform owners verify the path; supplier supplies product facts and limitations. |
| Protect service visibility | What NOC view or supplier workflow disappears if the identity is suspended? What manual or alternate source remains, and who can run it? | NOC and service assurance provide current operational impact; service owner confirms critical dependencies. |
| Choose containment | If the action identity is separate and the pre-agreed trigger is met, use the narrow stop and verify it. If authority is shared, compare broad revocation, a technically enforceable narrower restriction, and a short period of continued operation under explicit controls. | Incident commander coordinates; the accountable service executive authorizes consequences within delegated authority. Exposure outside appetite is escalated. |
| Verify and recover | Confirm downstream requests are denied, logs remain attributable, and NOC visibility/fallback works. Re-enable only after the owner and control operator confirm the boundary and restoration conditions. | IAM/platform teams prove the control effect; NOC/service owner confirm service state; incident lead records the decision and residual risk. |

A proposed change is not evidence that the target system acted. If only the proposal is known, preserve it and verify whether a downstream call occurred before broad revocation; where unauthorized execution is confirmed, use the pre-authorized stop. This distinction can avoid losing service visibility in response to an output that has not changed network state.

The options are not equivalent. Broad revocation may cut off an unwanted path quickly but also remove monitoring or supplier handling. A narrower control preserves more service function only if it is independently enforced and tested. Continued use avoids that immediate operational change but leaves authority active. The decision record should say which option was chosen, what evidence was missing, who accepted the service impact or residual exposure, and what event requires a new decision. This is how the response clock is shortened without pretending that all services can be safely isolated in the same way.

## Use automation where its impact is limited

CISA’s August 2026 Logging Reference Architecture (LRA) targets U.S. Federal Civilian Executive Branch (FCEB) agencies; it is not a telco-specific standard. It says AI-assisted techniques can support incident triage, scoping, timeline reconstruction and summarization. Actions with material operational, legal or privacy consequences should remain subject to human review and established incident criteria. For an operator, use AI to assemble incident context and evidence, not to make a network-impacting decision on its own.

Limited automation can support containment when its authority is narrow, its effect is reversible and it records what it did. A short-lived agent identity may be suitable for automatic revocation if it is separate from identities needed for essential monitoring. Shared credentials change that calculation: the same action may remove visibility operators need to assess the incident. The service owner can set which actions are pre-authorized and which require human judgment, based on service impact, control effectiveness and risk appetite.

The operator does not need to establish that an intrusion used AI before preparing for shorter response windows. Plans should reflect what an attacker can do, how quickly it may act, and which services the operator must keep running.

## The question for leadership

A useful executive discussion settles who may use pre-approved containment, who can authorize a broader action after hours, and which service dependencies could be affected by isolating an identity or supplier connection. It also assigns customer and regulator communications while the technical scope is uncertain. The accountable owner for each affected service decides whether temporary impact fits the operator’s risk appetite and what conditions allow restoration.

These decisions depend on the service, not a generic organization chart. If ownership or the safe next step is unclear, teams will debate roles and impact while the incident unfolds. Containment without service context can create a second service incident.

Chapter 1 explained why risk has changed. Chapter 2 mapped where exposure can enter and spread. This chapter connected response time, decision authority and service continuity. Chapter 4 turns those concerns into four practical moves for a service-provider CISO or CTO over the next twelve months.
