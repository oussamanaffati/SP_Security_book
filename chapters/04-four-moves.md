# Chapter 4: Four Moves for Service Providers in the Next 12 Months

A service-provider security plan should start with a harder question than “Which products use AI?” Which identity reaches which service, what can it do, and what happens to the NOC if it is stopped? Those are the four moves in this chapter: find consequential paths, limit authority, rehearse a safe stop, then fund supported changes.

Existing security, supplier and change processes are a starting point, not a complete map. Routine releases, pilots and SaaS features can sit outside them. Start with paths that could affect a critical service or sensitive data; a complete inventory is not a reason to leave known excess reach untouched.

## Move 1: Visibility means more than an AI inventory

Ask where AI can reach and what it can do. Review OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. Include pilots, SaaS features and automation even when no one calls them AI. Bring Network Operations, IT and security together with the service, procurement and supplier teams relevant to each path.

For each use, record the service and purpose, supplier or model, identity, data and tools, action rights, logs, market, suspension path and fallback. Note whether context is task-scoped or persistent; Chapter 2 owns the detailed read/write and clearing test. A prompt/output-retention statement does not establish the memory boundary.

Use release notices, procurement reviews and architecture changes to keep the view current. If a supplier cannot explain deployed identity or reach, do not mark the path verified.

An official page summary of the Australian Signals Directorate’s Australian Cyber Security Centre (ACSC) October 2026 guidance says asset identification should include AI services, agents, connectors and unsanctioned applications. It also calls for checks on prompt/output retention, training use and processing regions. This is cross-sector guidance, not a telecom requirement; local duties still need review.

TRAI’s 30 October 2026 telecom consultation draft is not binding; Legal and Compliance should confirm which inventory and third-party due-diligence duties apply in each market.

Prioritize uses that can affect a critical service or sensitive data. Project, procurement, IAM, configuration and runtime records are leads, not proof of absence: each is limited by its scope and coverage. Cross-check intended purpose against deployed or observed access. A release notice can show that the supplier diagnostic feature exists; target identity and logs help establish what it can reach and did. IAM data can expose the shared account’s edge/core reach, while service teams show which workflows depend on it.

Distinguish **confirmed**, **inferred** and **unknown**. An empty register or log is meaningful only within its verified scope and period. Four evidence classes help keep claims precise: supplier/design statements, configuration review, bounded technical tests and operational exercises. Each supports different claims; a tabletop tests coordination, not target enforcement. Chapter 2 covers source, freshness and conflict rules for joined operational data.

For retrieved supplier or customer content, Chapter 2’s source-to-target test is the primary check. Record the source, connector and target; a prompt filter or supplier statement does not show that the target refuses out-of-scope actions.

**Treat supplier changes as a security gate.** A routine update can add capability without changing the product name. Keep a baseline for identity, data, connectors, action rights, processing and retention, support access, logs and disablement. Recheck when one of those or the service view changes; carry prior findings forward only for properties that remain unchanged. Seek advance notice where feasible. If deployed state cannot be compared with the baseline, the earlier review is stale. Count a restriction only when its enforcement is verified.

If a release also carries a security fix, verify local version and reach, then obtain the supplier’s supported separation, backport, mitigation, test and rollback options. Confirm service impact and fallback before bringing a change forward. After deployment, check the fix, feature state, target permissions, logs, NOC visibility and rollback. Estimate supplier, engineering and NOC effort locally.

**Worked decision: supplier diagnostic feature.** The composite establishes that a routine update enabled an AI diagnostic feature that reads topology and proposes actions, and that the feature was missing from the operator’s AI project register. Direct execution is not established.

**Educational assumptions for this decision:** Operations Engineering owns the feature; the only evidence in hand is supplier design material; a separate feature switch is claimed but untested; manual diagnosis is possible during a supported window if the NOC receives planned backfill. These assumptions make the decision complete for learning; replace them with operator evidence before use.

| Option | Trade-off | Gate |
|---|---|---|
| Enable as shipped | Keeps the diagnostic capability, but leaves the path and service effect unverified. | Supplier design material alone is not enough. |
| Keep the product release; hold the feature off | Preserves other functions if the switch truly isolates the feature. | Test that it blocks runtime calls and downstream actions; confirm supported rollback and NOC visibility. |
| Pause or roll back the combined release | Avoids an unbounded feature, but may delay diagnosis or a fix and return work to the NOC. | Confirm supplier support, service impact, backfill and a safe window. Do not assume a workaround exists. |

Under these assumptions, keep the product release only if target-level testing shows that the switch independently stops runtime calls and downstream actions, and the supplier supports rollback. Until then, hold the feature off; if that is not possible, seek a supported pause or rollback after checking service impact and fallback.

If the package contains a fix that should not wait, verify the local version and reachable path, then compare supported separation or backport with delaying the fix. The recommendation changes if testing finds a wider data/action path, disablement fails or the fallback cannot preserve NOC visibility. A bounded read/draft path with attributable logs, effective revocation and acceptable fallback may justify a limited pilot for that task only. Reopen if the release or fallback changes.

Inventory shows where to look. Access review shows whether an agent has more authority than its task requires.

## Move 2: Match authority to the task

Start with identities whose reach could affect essential services or sensitive data. Ask what the agent can read, what it can change and what fails if it is stopped. Use a dedicated, task-scoped identity where the platform supports it; short-lived credentials can reduce standing access.

Configuration describes intended boundaries, not necessarily deployed reach. For a high-impact path, trace an allowed and a prohibited request from identity through connector to target. Check target denial, principal-linked logs, revocation, active sessions, queued work and NOC visibility. Treat persistent memory as a separate read/write path and test its scope and clearing. Use a suitable environment or supported window, not a live production experiment.

Keep customer-impacting changes in normal authorization and change control. Human approval matters only when the reviewer can see source records and service impact and can reject the proposal. A pre-filled change request is not a meaningful check by itself.

**Decide when a recommendation may become a pre-authorized action.** In the NOC-assistant composite, the assistant proposed a visibility-reducing change; it was not executed. Keep it as a draft in the normal change path. Any future standard-action envelope should name the task, target, parameters and service conditions; incident-time containment remains separate.

Before pre-authorizing that envelope, test permitted and prohibited parameters, stale or conflicting inputs, duplicate or interrupted requests, attribution, stop and rollback in a safe environment or supported window. Recovery means the NOC has its required feeds, alarms, history and ticket state, not merely that configuration was reverted. Estimate review, engineering and manual-recovery effort locally. If approval is not the bottleneck, wider authority will not solve it.

**Build the stop path outside the assistant.** A platform pause may stop new runs but leave issued credentials, active sessions or queued calls. Identity revocation may stop new access but also remove alarm reads or supplier-case handling when one principal is shared. A target-side deny can block a prohibited action, but a broad deny may interrupt a service. Test each control separately; an inactive screen does not prove the downstream path has stopped.

The composite establishes neighboring-domain reach, supplier-case handling and a proposed visibility-reducing change. **Educational assumption:** a bounded pilot can use a separate identity for alarm reads and an independently denied action path. Verify new calls stop, active sessions and queued work are bounded, alternate routes receive the target’s intended response, and required alarms remain visible or move to a tested fallback. Give the on-duty NOC a stop route independent of the assistant and the supplier. If that path cannot be tested safely, keep the workflow at draft or within a verified restriction.

**Do not treat reviewer capacity as unlimited.** The composite does not establish a review backlog. In a planning exercise, assume a surge exceeds the on-duty team’s capacity. Reviewing every output can delay triage; letting the assistant assign itself a low-risk tier can miss service context. Set review priority by service impact and test the queue with representative or synthetic inputs. Track age, corrections, missing context, shift capacity and fallback. If the queue exceeds local tolerance, pause proposals or actions and use the tested manual path; do not widen authority to compensate for a staffing gap.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses. This is general guidance, not a telco control standard. Legacy targets and supplier connections can constrain identity design. When a target cannot issue a separate identity, a controlled gateway may be an interim option, but test every relevant route and failure mode before counting it as a boundary.

**Illustrative read/recommend/execute authority matrix.** Adapt the boundaries to service impact and the operator’s architecture; the matrix is a decision aid, not a universal policy.

| Level | What the agent may do | Boundary check | Decision consequence |
|---|---|---|---|
| **Read** | Retrieve only task-required data. | Enforce read-only at the target or controlled connector. Test allowed/denied requests; confirm principal in logs; verify retention and destination. | Neighboring-domain data needs separate, time-bound authorization. Unverified source or identity means read-only is not low risk. |
| **Recommend** | Draft a diagnosis or action; do not submit changes. | Show source records and service context. Test that no hidden write path or downstream trigger exists. | Keeps the choice with the operator, but incomplete evidence can misdirect triage. |
| **Execute** | Perform only a narrow, deliberately delegated action. | Scope target/parameters; set limits; test stop, audit and rollback; preserve normal change control. | If the action is unbounded, cannot be observed or cannot be reversed, keep it at recommendation; define a fallback before delegation. |

Set authority by service consequence, not product label. Before moving from read to recommendation or execution, test the new boundary and understand what work becomes slower or manual if the agent is restricted.

For temporary cross-domain reads, use Chapter 2’s target-enforced expiry and session test. Renewing read access does not authorize write actions.

**Shared edge/core service account.**

**Worked choice: gateway interim or target-native identities.** The composite establishes edge and partial core reach, but not whether the target supports separate identities or a gateway. For this comparison, assume the target cannot be separated in the current window and an operator-controlled gateway is possible but untested.

Keeping the shared account preserves current operations but leaves cross-domain reach and weak attribution. A gateway may narrow the path sooner, but only if every relevant route passes through it. A bypass defeats the restriction; fail-closed behavior can interrupt support, while fail-open can restore broad access. A target-native identity is the durable option when the platform and supplier support it, but migration needs a safe window and rollback.

Use a gateway only as an interim control after a bounded test confirms the allowed edge workflow, denied core access, no alternate route, attributable logs, revocation and safe behavior on gateway loss. Test an independent emergency path and estimate supplier, engineering and NOC effort locally. If the gateway is unverified or fails, do not count it as reduced reach. If migration must wait, keep the shared account within its current scope under an executive decision covering the affected services; escalate if service tolerance or authority is exceeded. Reopen the choice if reach, gateway behavior, supplier support or service dependencies change.

Choose the cutover only after confirming parallel identities, workflow-by-workflow migration and a workable rollback. Testing a new identity alongside the old one exposes missing permissions but prolongs overlap; disabling the old one first reduces overlap but can interrupt supplier support or monitoring; moving one workflow at a time limits blast radius but uses more NOC and engineering time. Prefer staged preparation, distinct identities and logs, and a locally justified end to any overlap. Verify that the old identity and sessions are disabled after cutover. Rollback that restores the shared account restores its broad reach; treat it as a separate service decision.

**Illustrative change gate: edge access.** Use this gate to decide whether migration is ready; it does not replace the operator’s change process.

| Gate | Check | If unresolved |
|---|---|---|
| Service impact | Map dependent services, monitoring and fallback before removing reach. | Do not assume removal is safe; narrow the change or delay it. |
| Change readiness | Confirm supported steps, supplier role, test window, staff and rollback. | Wait for a supported path; use only a tested interim restriction. |
| Target result | Confirm edge access works, core access is denied, logs and essential workflows remain. | A completed ticket or configuration push is not proof. |
| Rollback | Confirm restoration and whether rollback reactivates broad access. | If it does, treat rollback as a separate service decision, not a neutral return. |

Access limits matter only if the NOC can operate through a failure. Rehearse the stop and fallback.

## Move 3: Rehearsal tests the response before an incident

Use a tabletop to test authority, hand-offs and service impact; use technical validation to test enforcement, sessions and monitoring. Neither substitutes for the other. Choose the least disruptive format that answers the open question, and do not turn a policy question into a live-core experiment. Bring NOC/SOC, identity/platform, service assurance and change teams; add legal, communications, procurement or a supplier when the scenario requires them.

The Canadian Centre for Cyber Security recommends practising incidents that unfold within hours, pre-authorizing isolation steps and testing manual alternatives. Joint ASD ACSC and partner-agency guidance warns that external content can steer an agent through indirect prompt injection. CISA’s CI Fortify package offers a hypothetical telecom-outage exercise on isolation, third-party dependency and manual operation; it is not AI-specific or incident evidence. CISA, FBI and international partners’ service-provider guidance adds outage communications that preserve operational security and align with containment. These are cross-sector guidance and exercise material, not operator results.

Before the exercise, set the service conditions: what access must stop, what NOC view and fallback must remain, who can authorize the action, and which local response or recovery tolerance applies. A fast revocation is not a pass if it hides alarms or removes the only recovery path.

**NOC assistant exercise.** Use the composite’s established account reach and proposed visibility change as the decision; test authority and continuity in the tabletop, then validate revocation separately.

| Stage | Exercise prompt | Decision to test |
|---|---|---|
| Normal path | The assistant summarizes alarms and drafts a ticket. | Identify the service, principal, connector and normal change path. |
| Broader access | The account can open supplier cases and read neighboring-domain data. | Decide which scopes the task needs; separate read, recommendation and action. |
| Proposed visibility change | The assistant proposes a change that could remove an operational view. | Identify the authorized stop, service impact, independent alarm view and fallback. |
| Verify | Validate revocation separately in a safe test or supported window. | Confirm target denial, sessions/queued work, principal logs and essential monitoring. |

Route each finding to the right fix: a target that accepts a prohibited request needs a technical restriction and retest; unclear authority needs a primary, deputy and rehearsed trigger; lost alarms or supplier handling needs an independent view or staffed manual path; a missing supplier answer needs a narrower, observable scope. Rank by service consequence and the strength of any tested interim treatment. Put the necessary work into the roadmap; use Move 4’s pilot gate before widening read/draft use.

## Move 4: Turn priorities into controlled operational change

Choose three or four funded changes for the next 12 months. Rank service consequence, safe implementation, supplier support and available NOC/engineering capacity. Put each against a supported window, its key dependencies and a local cost estimate; show what work moves and the service cost of waiting.

**Compare competing work with the same evidence.** Prioritize service impact and safe implementation, not AI novelty: a high-impact gap with a long supplier dependency may need interim treatment, while a reversible lower-impact change may wait. Use these four operational questions when fixes compete for capacity or a maintenance window:

| Question | Evidence to bring | Trade-off the decision must show |
|---|---|---|
| What service and path are exposed? | Affected service, identity, reachable systems or data, existing controls and gaps. Mark unverified reach as unknown. | Service consequence if the path is misused or stays open. |
| What risk does the treatment reduce? | The boundary changed and a test or observation of the result. | Prevention, detection, containment or recovery; do not count them as equivalent. |
| What does implementation cost? | Engineering/test effort, supplier charges, backfill and window needs, transition/exit cost; show estimate basis and uncertainty. | Risk reduced versus displaced work, lost diagnostic value, recurring dependency and new operational risk. |
| What remains open? | Supplier commitment, supported procedure, rollback, fallback and reassessment trigger. | Service effect of delay; refer appetite or delegation questions to the delegated executive and, when necessary, board-level escalation. |

When two changes need the same window, combining them can reduce service disturbance and supplier call-outs, but makes fault isolation and rollback harder. Separate windows simplify observation but use more capacity and may leave one exposure open longer. Combine only if each change has an independent success test and rollback; otherwise sequence by verified service impact and keep the second within a tested interim boundary. Reorder if the first change alters the next test, service tolerance or interim control.

### Sequence the funded work

Align these stages with the operator’s change calendar, supplier commitments and service priorities. Completing a deliverable is not evidence of risk reduction.

| Stage | Lead, decision and dependency | Evidence required to proceed or close |
|---|---|---|
| **Establish the baseline** | Security and platform teams map the supplier-feature, NOC-assistant and edge-account paths and verify the deferred patch’s deployed version and reach. Gather supplier, product and identity records. | Known/unknown identity, data, actions and service reach; patch applicability; immediate restriction needs. A baseline is not proof of control. |
| **Before widening authority** | Identity/platform, Network Engineering, NOC and supplier plan boundaries and edge migration; confirm test capacity and a supported window. | Configuration review, allow/deny tests, attributable logs, revocation. Without safe testing, retain interim controls and mark the boundary unverified. |
| **Before relying on containment** | Incident-response lead with SOC/NOC, service assurance, change management and supplier rehearses the NOC assistant and fallback; map identities first. | Local decision/timing results plus technical revocation and visibility tests. Keep tabletop claims separate from technical evidence. |
| **Portfolio review** | CTO/CISO sponsors and resource leads sequence work at a cadence the operator sets; reopen sooner if a dependency or service condition changes. Patch and edge migration need supported windows. | Separate delivery from tested risk reduction; report impact, tests, dependencies and triggers. Count patching after effectiveness checks. |

Estimate engineering, NOC/SOC backfill, supplier, test and window effort locally; state what work will move and mark unknown costs rather than inventing them. Chapter 5 covers board-level reserve and reallocation choices. Reopen a stage if a dependency, access path, test result or service condition changes; escalate any decision beyond the authority covering the affected services.

### Gate pilot expansion on evidence

**Set the pilot’s scale-up gate before seeing the result.** A supplier demonstration is not enough to justify broader use. The NOC-assistant composite establishes summaries and draft ticket updates, not time savings, quality or service outcomes. Define the task cohort, current workflow, acceptable service effect and operator-accepted result. Set local thresholds for permitted data and identity, source traceability, target denial, review capacity and fallback; do not invent a universal accuracy or time-saving percentage.

**Choose the pilot mode for the question you need answered.** These modes provide different evidence; “pilot” is not one standard test.

- **Synthetic validation** tests target denial and handling of missing, stale or conflicting inputs without exposing live service data. It does not establish live performance or service impact.
- **Historical replay** compares summaries with known cases and exposes correction or coverage gaps, but may miss live timing and changing dependencies. Protect the records and preserve their original context.
- **Shadow processing** reveals live timing and review effort without authorizing changes, but still processes data and may have side effects. Limit data and stop if visibility or service degrades.
- **Bounded live read/draft use** tests the real workflow but consumes review and backfill capacity. Use it only after the identity/data boundary, source trail, independent stop and manual fallback are verified; keep proposals in normal change control.

**Test the target boundary, not just the simulation.** A test proves only the principal, connector, policy, target, logging path and revocation mechanism it actually exercised. Name those elements; a mock target, different identity or simulated policy cannot establish production enforcement.

Use synthetic or approved historical data when it answers the question. If live evidence is necessary, control data handling and side effects; use a non-service-affecting target action where available. When a production denial test is unsafe, keep write access denied and continue only at the last verified read/draft scope or through a manual path that preserves the service view. Treat production behavior as unknown and hold expansion until a safe, supported test is available. If the service cannot operate under that restriction, take the service decision to an executive with authority over its impact.

There are three choices: expand when task quality, source coverage, review capacity, control and service conditions meet the pre-set gate; keep the pilot bounded while gathering representative results; or stop and return to manual work when quality, impact or effort misses the threshold. A positive average is not enough. Compare difficult cases, corrections, review effort, supplier charges and displaced work, not only mean response time.

Test source coverage separately from average quality. Use synthetic or safely replayed inputs with missing, stale and conflicting feeds. The assistant should show the gap and preserve links to source records; it must not turn an unobserved service area into “clear.” A retrospective trend may tolerate a visible gap; live incident triage may need manual confirmation. If connectors do not expose freshness or completeness, keep the workflow bounded until they do.

**Treat reviewer disagreement as a signal.** Track corrections by cause: missing or stale source, wrong service attribution, unsupported inference, unsafe action or presentation. If reviewers disagree about service safety, define the reference decision before expansion; absent that rule, keep the output at draft. Separate cosmetic defects from disagreements about impact, authority or source sufficiency, and compare patterns across shifts as well as review workload.

When scale-up is justified, widen one dimension at a time: users, data scope or action rights, then retest the changed boundary.

### Transfer the pilot into routine service

**Make routine operation a separate decision.** A staffed pilot does not prove that the NOC can support a workflow across shifts, supplier updates or incidents. Before handoff, ensure day, night and weekend teams can inspect the source trail, pause the workflow, invoke fallback and reach supplier support within local tolerance. Fund ongoing engineering, supplier and reviewer effort. Retest when model, data, connector, service, market or usage volume changes; without funded run support, the pilot stays a pilot.

**Keep the fallback operational.** A manual route is not independent if it relies on the same identity, connector or supplier. For the NOC-assistant composite, assume for this exercise that the service identity is suspect; do not reuse it just because its password still works. A separate emergency role helps only if it is target-limited, time-bounded, logged and tested, with a path to invoke and revoke it and an alarm view that remains available. After use, reconcile actions, verify service and ticket state, revoke temporary access, then restore ordinary access through change control.

Exercise the transition on relevant shifts. If the team cannot use the manual route within service tolerance, fund backfill and repair, narrow the task or keep the pilot staffed. Retest after changes to the workflow, identity provider, target permissions or on-call pattern. For interim protection, distinguish a restriction that reduces reach from monitoring that only improves detection.

### Revisit a delayed change

**Deferred patch window.** In the composite, the next supported window is three weeks away. That timing does not establish that the deployed live-core version is affected, the path is reachable or an interim restriction works. Verify version and reach locally; test any restriction against NOC visibility and service; ask the supplier and Engineering for the earliest supported change, test requirements and rollback. A threat signal can change urgency, but cannot prove local exposure or make an unsupported live-core change safe.

Compare three routes: bring forward the earliest supported change, keep the booked window with only a tested interim restriction, or temporarily narrow affected access when a test shows the path is denied and service visibility remains. Each may consume engineering, supplier and NOC capacity; estimate local effort and displaced work rather than inventing a cost.

On the available facts, ask for the earliest supported change but do not execute early until local version, reach, service impact and test/rollback readiness justify it. Keep the scheduled window as fallback. If no effective restriction exists, do not describe waiting as controlled. Bring the change forward when local evidence shows a reachable affected version or materially increased urgency and the supplier can support it safely. If the service cannot tolerate the remaining exposure, route the service-specific choice to an executive with authority over the affected services.

Reopen the choice if version, reach, restriction, supplier support, window or service conditions change. After deployment, verify the targeted version, denied path, logs, monitoring, service health and rollback. A calendar slot does not reduce exposure.
