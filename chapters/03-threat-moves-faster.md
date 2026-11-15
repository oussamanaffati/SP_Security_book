# Chapter 3: The Threat Can Move Faster Than the Operator Can Safely Respond

A fast alert does not make containment safe. The SOC may see suspicious activity while the NOC sees a planned change; IAM may be able to revoke a credential, and a supplier may hold platform details. Without a clear decision path, an attacker may retain access while the operator checks service impact.

## Threat activity can accelerate without being fully autonomous

The Canadian Centre for Cyber Security’s 26 October 2026 bulletin is cross-sector evidence, not a telecom incident or a universal attack timeline. It says attacks are not yet fully autonomous: humans still choose targets, set objectives and oversee operations. For some activity it attributes to Storm-0940, the period from target selection to privileged cloud access was under three hours.

In a 15 October 2026 advisory, CERT-In reported that tools using AI agents shortened the time from initial access to impact from days to a few hours in a financially motivated campaign against Indian entities. The advisory did not identify those organizations as telecom operators; it also reported parallel agent operations and repeat attacks within days after incomplete remediation.

A separate 4 November advisory from CERT-In’s finance-sector incident-response team reported attacks against Indian banking, financial services and insurance (BFSI) entities timed to holidays, weekends and other low-monitoring windows, including after incomplete remediation. This financial-sector evidence supports testing off-hours decision authority and escalation, not a claim about telco incidents.

Neither report establishes an operator response deadline. Faster adversary activity does not make every emergency change safe on a live service.

Chapter 1’s live-core patch decision supplies a second clock: the fixed version is known, but the supported change is three weeks away. The three-week interval is specific to this patch decision, not a universal benchmark. Separate time to confirm affected services and interim protections from the lead time for a production change; they call for different actions. If exposure changes, reassess interim protection and change readiness; an unsupported emergency change is not automatically safer.

Keep four tracks moving in parallel. Security and platform teams verify the deployed version, reachable path and affected services. The control owner and NOC/service assurance test interim restrictions against monitoring, supplier access and customer work. Engineering and the supplier confirm the fixed release, earliest supported window, testing and rollback. A scheduled window is not mitigation, and a known fixed version does not prove local exposure. Reassess if threat, reach, control result or service conditions change.

## Response runs on several timelines

Incident response is often described as a technical sequence: detect, investigate, contain, recover. In practice, workstreams overlap. The NOC checks whether an alarm matches a real network change; the SOC assesses whether the activity is malicious; IAM may need to disable an account. Service assurance estimates customer and service impact, while legal, regulatory and communications teams work against their own deadlines.

At the same time, the network cannot wait for every team to finish its analysis. Nor can the operator treat every system as disposable. A management platform may support several network domains. An identity may be shared across automation jobs. A supplier connection may be needed to restore a service even as the supplier helps investigate it. Availability changes the containment decision.

It helps to separate four response intervals:

- **Detection:** from the first relevant signal to recognition that the activity may be malicious.
- **Decision:** from that recognition to an authorized containment choice.
- **Action:** from the decision to safe execution and confirmation of the result.
- **Continuity and recovery:** from containment to the safe restoration of affected services.

Isolation can break a critical workflow or remove telemetry needed to understand the incident. Set objectives for each interval against service tolerance; report service impact and the reason for delay, not elapsed time alone. A single total will not show whether the constraint was context, authority, supplier access or fallback.

Use the SOC/NOC exercise to find the delay. If no tested option meets service tolerance, the executive with delegation for that service decides whether to continue in a bounded mode. Do not report an unsafe or incomplete response as “on target.”

**Set an objective for safe containment, not one network-wide clock.** A single target is easy to report but can count an unsafe isolation as success and hide different service tolerances. No target avoids a false promise but hides where investment is needed. Service-specific objectives cover detection, decision, action and recovery, including which service view or function must remain available.

For an exercise using the existing NOC assistant, assume the broad account can be revoked only as a whole and no independent alarm-read path has been verified. A dashboard that measures only time to disable the account could show a fast response while leaving the NOC without the visibility needed to manage the network. Treat threat-speed reports as stress cases for exercises, not as a universal service deadline.

Under that assumption, containment counts only when the target blocks the disallowed path, active sessions are stopped or bounded, and the NOC retains its alarm view or a tested fallback. Measure from first signal to safe restoration, separating recognition, authorized decision and target-confirmed action. If every available stop removes essential visibility, fix the design before tightening the response target.

Fund the exercise: NOC/SOC backfill, supplier participation, identity/platform work and logs that link the signal to the target result. Rehearse off-hours and split attention; report elapsed time with service impact, manual work and the reason for delay. Keep statutory reporting deadlines separate from internal containment targets. Consider faster bounded actions only after independent alarm visibility and narrow revocation have been tested. Adjust the objective when the service, fallback or tested control changes, not simply because a threat report describes a faster attacker.

CERT-In’s April 2026 advisory recommends tabletop exercises for five simultaneous incidents, explicitly modelling AI-driven scenarios. This is Indian cross-sector guidance, not a telco standard or universal target. For an operator, the question is whether NOC, SOC, IAM and service teams can still make timely, service-safe decisions when attention is split.

**Choose a command model for shared dependencies.** When incidents share a management platform or compete for NOC, engineering or supplier capacity, the operator can use one central lead, separate teams or a federated model. A central lead aligns priorities but can become a bottleneck and may miss service-specific tolerance. Separate teams move locally but can isolate a shared platform or consume the same scarce specialist twice. A federated model coordinates common priorities and resource conflicts while service leads act within pre-authorized limits. It works only with clear arbitration and deputies.

The coordinator maintains the common picture and resolves resource conflicts; it does not direct every technical action. Service leads explain the impact of isolation and the available fallback. A cross-service decision goes to an executive with authority across the affected services; coordination alone does not confer authority to accept service risk. Prioritize by service consequence and tested alternatives, not alert count or a single severity label.

Exercise the model with on-call roles, deputies and supplier contacts, including when the primary decision-maker is unavailable. Record whether delays came from shared visibility, service impact or staff/supplier capacity. Change the decision route if coordination stalls; fund coverage if capacity is the constraint; define arbitration and fallback when services compete for the same dependency. Do not grant broad action authority to compensate for missing staff or cross-service delegation.

## The SK Telecom response had distinct timelines

The Ministry of Science and ICT (MSIT) investigation into SK Telecom’s 2025 breach separates detection from reporting. MSIT says SK Telecom detected abnormally large outbound traffic at 11:20 p.m. on 18 April 2025 and notified the Korea Internet & Security Agency (KISA) at 4:46 p.m. on 20 April, exceeding the statutory 24-hour reporting window.

That is the reporting clock, not the containment clock. A public-private team began its investigation on 23 April and inspected all 42,605 servers through 27 June; the final findings identified 28 infected servers. The inspection period does not establish when containment occurred.

**Run reporting clocks beside the technical response.** The SK Telecom timeline is a reminder that notification has its own deadline. Complete forensic scope may take longer than a reporting trigger, and a single global “incident confirmed” time may not start every market’s clock. Map triggers and recipients by service, data type and jurisdiction; do not borrow another market’s rule.

Prepare the notification path before an incident. Keep the first signal, each applicable threshold, containment actions and customer impact on separate timestamps. If a notice is due before scope is complete, state what is confirmed, what remains unknown, which services or data are under review, what protective action is underway and when the next update will follow. Do not wait for attribution if it is not required, and do not present a suspected effect as confirmed. Exercise translation, regulator contacts and customer-care capacity; a template alone is not readiness.

The customer response had its own operational demands. In its preliminary findings, the Ministry encouraged subscribers to replace their USIM cards or use a protection service, and urged the operator to expand service channels and add a reservation system so more customers could be protected promptly.
These reports describe a breach-response timeline, not a network outage. They show how an incident can create a second workload: protecting customers, handling enquiries and changing business operations while the technical investigation continues.

Customer protection runs alongside forensic scoping. Waiting for every affected record may delay useful advice; speaking earlier can trigger enquiries before the operator knows who is affected. Contact and replacement channels need capacity, not just approved text. When evidence and duties support action, issue a staged factual notice: affected service or data categories, what remains unknown, what customers should do and when the next update will follow. Revisit it as facts change; do not imply broader impact than the evidence supports.

**Test the communication path under service failure.** If an outage affects the operator’s app, messaging or data service, a notice sent only through that service may not reach affected customers. An external status page or partner channel may be reachable but has its own availability, authentication and update dependencies. Contact centres and retail channels may reach customers through staff, but can saturate and displace other service work. No single channel should be assumed to reach every affected customer.

Choose channels from the services and markets at risk, applicable duties, customer preferences and tested reach. Name who can activate them and where approved facts come from; keep updates consistent if one system fails. In an exercise, disable the primary channel and test alternate authentication, reach and staffing. Include language and market needs, suppliers and displaced work. If alternate reach is unverified, report a continuity gap.

CISA, the FBI, and partner agencies recommend a service-outage communications plan with triggers, escalation paths, and templates for status pages, customer and partner notices, and regulatory communications. They advise frequent updates on what is known, unknown and under investigation, while protecting operational security and aligning with law-enforcement and containment efforts. The guidance does not describe the SK Telecom breach; for an operator, it can inform planning when defensive isolation changes service availability.


## Containment is a service decision

At a service provider, containment changes both attacker access and the ability to restore service. Blocking a supplier connection may delay repair; disabling a shared identity may stop monitoring; isolating a management host can remove operational visibility.

**Supplier support during containment (illustrative assumption):** the shared account is being used for supplier support during an incident, and supplier engineers are needed for a supported configuration change. The composite establishes edge/core reach and supplier dependence for remediation; the active session, misuse and a separate support identity are assumptions.

The operator can revoke all supplier access, keep the broad session active under observation, or switch to a separate, supervised identity limited to the target and task. Full revocation may delay repair and may not end existing sessions or queued actions. Keeping the broad path preserves support but not least authority; observation alone may not identify who caused a target action. A narrow identity preserves needed support only if the target enforces scope, logs the supplier principal and ends sessions at expiry. Set up the alternative before an incident; it consumes supplier, engineering and NOC time.

Do not keep the broad session only because the supplier is useful. Pre-authorize a trigger and fallback from service-impact tests, then use the stop when the trigger is met; do not wait for full forensic attribution. Continue support only through a target-verified, time-bounded identity for a named user, target and task. If no safe alternative is available, the delegated service executive makes a time-bounded service decision.

Before relying on the alternate, confirm that the target permits the intended task and denies others, identifies the supplier principal in logs, and ends sessions at revocation. Confirm that the NOC retains alarms and exercise the manual route if one exists. Estimate supplier response, engineering effort, NOC backfill and any delayed repair. A supplier’s statement that access is “supervised” is not proof of target enforcement.

The Canadian Centre for Cyber Security recommends deciding in advance who may isolate an account, application, network or service, and practising incidents that unfold within hours rather than days. It also recommends identifying essential functions, pre-authorized isolation steps and safe manual or alternative operation.

Put those criteria in the response playbook: triggers, service effects, authorized actions and fallback.

A job title on the rota is not a mandate. Pre-authorize by service effect. A narrow, reversible restriction on a dedicated identity can be pre-authorized only when its trigger, target denial, session behavior and alarm view or fallback are known. A domain-wide action, one that removes supplier support, or an action affecting several services needs an impact assessment and an executive with authority for those services. If no delegation spans them, escalate.

Set the trigger, scope, duration, expiry and restoration authority for each action; require target verification and NOC visibility. Rehearse with on-call teams, suppliers and deputies. If the right person cannot act, fix the response design.

## The NOC assistant makes authority visible

The NOC assistant introduced in Chapter 1 makes one question concrete: can the operator stop its broad service identity without losing essential alarm visibility?

Before an incident, verify that action rights can be stopped independently of alarm reads and supplier-case handling. Name the fallback and the person authorized to invoke it. Keep proposed network changes within normal change control.

**Illustrative live-incident decision card: NOC assistant.** Adapt the authority locally. A tabletop tests the decision path, not the technical behavior.

| Decision | Confirm |
|---|---|
| Scope | Identify principal, connector, tool and target. Separate a proposal from an action executed at the target. Include a memory path only if the workflow uses one. |
| Contain | Compare pre-authorized revocation, a tested narrow restriction and controlled continuation. Check sessions, queued actions, alarm visibility, supplier access and fallback. Route the decision by service impact and delegated authority. |
| Verify and restore | Confirm target denial, session state, essential alarms and restoration conditions. Return only a tested scope. |

If misuse is suspected, a fluent summary or ticket proves neither a downstream call nor a successful stop. Preserve the identifiers and source records needed to connect principal, connector and target activity; include session or queued-action state and relevant memory records only when they affect the decision. If a pre-authorized stop trigger is met, act while preserving what is safe in parallel. Verify denial at the target and check that NOC visibility remains. Missing records leave scope unknown; they do not prove that no action occurred.

Before an incident, map connector identifiers to target logs and test revocation against existing sessions and queued work. Keep any incident copy in an approved restricted store, separate from operational context. Do not treat an assistant summary or supplier assurance as proof of downstream state.

**Separate forensic preservation from operational memory.** If the workflow used persistent context during suspected compromise, quarantine it from live retrieval and preserve a restricted copy or relevant logs when permitted. Do not reuse it blindly or purge material needed for the investigation. Continue with manual handling or task-scoped context from authoritative sources if that can meet the service need. Restore memory only after its read/write identities and retained copies are understood, permitted retrieval works, cross-scope access is denied, and expiry or deletion is verified. If persistent memory was not used, do not let this check delay restoration of unrelated capability.

**Stage restoration while investigation continues.** Restore the minimum tested read/draft function; do not restore broad action rights simply to reduce manual work. Confirm the previous principal is disabled or rotated, downstream sessions and queued actions are ended or bounded, the allowed read and denied action paths behave as expected, essential alarms remain available, and a manual fallback is ready. Keep memory excluded until its scope and clearing are verified.

Reintroduce permissions or data sources one at a time. If a denied action succeeds, the path cannot be attributed, NOC visibility degrades or new evidence widens the suspected access, return to the last verified state. Full actor attribution need not be complete, but an unresolved path that could restore the suspected authority blocks restoration of that capability. If no safe fallback exists, make a separate authorized decision about the degraded service mode.

## Use automation where its impact is limited

CISA’s August 2026 Logging Reference Architecture (LRA) targets U.S. Federal Civilian Executive Branch (FCEB) agencies; it is not a telco-specific standard. It says AI-assisted techniques can support incident triage, scoping, timeline reconstruction and summarization. Actions with material operational, legal or privacy consequences should remain subject to human review and established incident criteria. For an operator, use AI to assemble incident context and evidence, not to make a network-impacting decision on its own.

For the NOC assistant, use a read/draft summary only if reviewers can trace its claims to source events and see missing feeds. A summary is a map to evidence, not evidence itself. Check timestamps and source references before relying on claims that change severity or scope. If inputs are hidden, missing feeds are invisible or hypotheses blend with recorded events, use manual review. Test traceability and the fallback when the assistant is unavailable. Passing supports read/draft use, not a network change.

For an operator, limit automatic containment to narrow, reversible, logged actions. Automatic revocation may suit a short-lived agent identity only if it does not support essential monitoring and downstream sessions have been tested. Revoking a shared credential may remove visibility operators need. Define the permitted action and service conditions in advance.

Prepare for shorter attacker action windows without waiting to prove AI was used. Decide what can be stopped safely, who may stop it and which service functions must remain available.

## The question for leadership

Executives do not approve every operational stop. They set service tolerances, delegate reversible actions within them, and fund NOC/SOC coverage, supplier participation and exercises. Any action that crosses services or removes an essential function needs authority spanning those services. Before the next incident, exercise one path from alert to safe stop and service restoration. If no one can show who decides, what remains visible and how service recovers, fix that path now.
