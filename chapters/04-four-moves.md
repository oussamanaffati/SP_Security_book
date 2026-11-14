# Chapter 4: Four Moves for Service Providers in the Next 12 Months

The same identity may connect an OSS query, a service ticket and an operational action. That shortens the path between information and change, but it can also let a mistake or compromised tool travel farther before a person intervenes. The Canadian Centre for Cyber Security’s cross-sector evidence suggests AI can shorten parts of an attacker’s workflow. For a service provider, the task is to contain both risks without putting continuity at odds with security.

Existing security, network, architecture, supplier and change processes provide a natural starting point. The review is about where agent identities, tools or supplier features fall outside them: which identities can reach which data or tools, which actions need approval, how NOC and SOC teams will rehearse a response, and what remains uncovered.

The sequence is useful because each move answers a different question. Visibility shows where authority exists. Access review tests whether it matches the task. Rehearsal reveals whether the operator can contain failure and maintain service. The roadmap gives owners and resources to close the gaps. These activities can overlap. Where excessive access is already evident, there is little value in waiting for the full inventory before considering a proportionate restriction.

No sequence will eliminate risk. The four moves help test controls and make residual risk visible against the operator’s risk appetite.

## Move 1: Visibility means more than an AI inventory

Two questions frame the work: where can AI reach the operator’s systems or data, and what actions can it take? A joint review can bring together Network Operations, IT, security, architecture, customer care, procurement, privacy and key suppliers. Its scope can include pilots, SaaS features and automation, even when no one calls them AI.

A service-first review is more useful than a model-first list. The relevant areas include OSS/BSS, service assurance, network management, customer identity, field operations, cloud control planes and supplier access. A customer-care summary tool has a different service impact from an assistant that can reach network configuration or subscriber records.

A concise record can capture the owner and purpose, model or supplier, identity, data and tools, affected services, available logs, fallback, relevant markets and who can suspend the use. Record whether context is task-scoped, persistent or not used; for persistent memory, capture the read/write identity, the data owner for permitted content and the platform/supplier owner who can evidence scope and clearing. Link to Chapter 2’s memory check; a prompt/output-retention statement alone does not verify that boundary. Open questions should remain visible rather than being marked complete.

An inventory becomes useful when it links a capability to its service owner, data, identity and available actions. Release notices, procurement reviews and architecture changes can feed the same inventory, so the register remains useful after the initial discovery. When the supplier cannot explain the feature’s identity or reach, record the assurance gap and its owner rather than marking the entry complete.

The Australian Cyber Security Centre’s October 2026 guidance calls for AI asset identification to include services, agents, connectors and unsanctioned applications. It also recommends checking what providers retain in prompts and outputs, whether customer data is used to train models, and where processing occurs. This is cross-sector guidance; local legal duties still need review.

Chapter 2 discusses TRAI’s telecom consultation draft. It is not binding; Legal and Compliance should confirm which inventory and third-party due-diligence duties apply in each market.

Many operators can make the first pass manageable by focusing on uses that could affect a critical service or sensitive data. Project, procurement, cloud and supplier records can help surface them; workflow owners can clarify what remains uncertain.

Use four evidence levels, and state which claim each supports. Level 1, supplier assertion or design documentation, describes intended behavior; it does not prove deployed permissions. Level 2, deployed-configuration review, shows configured identities, data and tools, but may miss runtime or downstream behavior. Level 3, a bounded technical test, shows what happened in the tested path, including allowed and denied requests, revocation and logs; it does not prove untested paths or live-service safety. Level 4, operational exercise or observation, tests who decides, what fallback works and how service is affected; a tabletop cannot prove technical enforcement. More than one level may be needed. These are evidence classes, not a score; report scope, limitations and the next evidence needed to support the decision.

For workflows that join operational records, use Chapter 2’s source-contract check to test whether the output preserves provenance and surfaces conflicts. It supports that data-quality decision, not a claim that the agent is generally accurate or secure.

Ownership is often split. The platform team may administer the feature, Procurement may hold the supplier relationship, and a service executive may carry the impact if it fails. A single “owner” field can hide those differences. Record separately who can suspend the feature, who supplies control evidence and which service may be affected. Chapter 5 defines the acceptance record; the register should link to it rather than repeat its authority test.

**Supplier diagnostic feature.** During a routine software update, a supplier enables an AI diagnostic feature in a network-management product. It is missing from the operator’s AI project register, yet it can read topology and propose actions. The immediate questions are who owns the feature, which identity it uses, and whether proposed actions remain inside the existing change process. Counting products is not enough; the operator needs to know what authority each feature receives.

The decision is not automatically “disable” or “trust the supplier.” If the feature’s access can be bounded, its actions traced and proposals kept within the established change process, the operator may have a basis to retain it with defined conditions. If those controls cannot be evidenced, restricting or disabling the feature may be the more defensible treatment, even if that delays the diagnostic benefit. Record the chosen boundary and the evidence that would justify a different choice.

The operator may also need to separate the decision to install a product release from the decision to enable the new capability. Confirm with the supplier whether the feature can be disabled independently, what other changes or functions are coupled to it, and how the change can be reversed. If those choices are coupled, delaying the release may carry its own operational cost, while accepting the feature without a verified boundary leaves uncertainty. Record which functions are coupled, what the delay affects and what evidence is needed before activation.

That makes inventory a lifecycle control, not a one-time audit. The supplier release path, cloud service terms and product change notices determine whether an operator learns about a new capability before or after it enters service. Procurement and technical owners can agree which changes require reassessment, particularly changes to identity, accessible data, connected tools, the ability to propose or trigger actions, model provider, prompt/output retention or processing location. Chapter 2 sets out the data-flow questions to ask when those supplier details change.

Before onboarding or renewal, Procurement and Legal can seek material-change notice and evidence commitments tied to those triggers, where commercially feasible. If a supplier cannot provide them, assess whether an operator-verifiable restriction or delayed enablement is feasible. Compare the service dependencies and diagnostic benefits each option affects, and estimate the transition effort. If notice is late or absent, record the assurance gap, affected service and event that will force reassessment; a stable product name is not evidence that its authority has stayed the same.

**Worked register: supplier diagnostic feature.** “Unknown” is a valid register value; it marks a decision the available evidence cannot yet support.

| Field | Illustrative entry |
|---|---|
| Capability and trigger | AI diagnostic feature enabled through a routine update to a network-management product; absent from the AI project register. |
| Purpose and known reach | Reads topology and proposes actions. No wider data access or direct execution is established by the scenario. |
| Owners and contacts | Operational feature owner: **not identified**. Supplier contact: **to be recorded**. Service-impact owner: **to be confirmed**. |
| Identity and path | Identity, connector and target-system permissions: **not yet verified**. Trace them end to end before treating the boundary as known. |
| Authority boundary | Proposal is subject to the existing change process, but whether configuration or workflow technically enforces that boundary is **unverified**. |
| Evidence and control state | Record the level, claim supported, scope, result, limitations and next evidence. Use Move 2’s safe-environment or supported-window guidance for a bounded write-path test. No test result is assumed here. |
| Stop and fallback | Independent feature disablement, effect on the rest of the product, and the operational fallback are **not established**. Confirm before deciding whether restriction is safe. |
| Decision and acceptance record | Retain only under evidenced limits, restrict/disable if limits cannot be established, or defer enablement pending supplier evidence. Link any continuing-exposure decision to Chapter 5’s residual-risk record; no acceptance or authority is assumed here. |

The entry stays open until the operator verifies the identity, reach, independent disablement and a service fallback; when a bounded test is used, retain its expected and observed results before marking the boundary verified.

**Supplier data-flow decision.** The known facts are that the feature reads topology and proposes actions. The available information does not establish whether topology leaves the operator’s environment, where processing occurs, or whether prompts and outputs are retained or used for training. Keep those facts unknown until evidence closes them.

| Decision question | Evidence to request or verify | If the answer remains unknown |
|---|---|---|
| What enters the feature? | Identify topology fields, identifiers and context sent with a request; compare them with the enabled configuration and the task’s need. | Restrict the available data if the boundary is independently enforceable. Do not describe the feature as least-privilege based only on its intended purpose. |
| Where is it processed and kept? | Record processing location, prompt/output retention, training use and deletion terms. Distinguish contractual or supplier assurance from settings the operator can inspect. | Do not assume data stays local or leaves the environment. Treat destination and retention as assurance gaps; request evidence or delay enablement. |
| Who can access it? | Establish supplier support access, any subprocessors in the processing path, and what access or activity records can be reviewed. | Keep the access path unresolved. Ask whether the feature can be disabled separately and what product or service function that would affect. |
| What is the safe operating choice? | Compare a verified restriction, independent disablement or deferred enablement with diagnostic benefit, manual workload, supplier dependency and the supported change path. | If reach and fallback cannot be bounded, establish whether a supported pause or rollback is safe; if neither is available, escalate the service consequence before continued use. |

Do not describe the current feature as controlled while identity, data path, downstream action, independent disablement and fallback remain unknown. First establish whether the feature can be disabled without reversing the rest of the update. If it can, retain the product release but hold the feature until a Level 2 configuration review and Level 3 test confirm data scope, denied write paths, attributable logs and revocation. If it cannot, check whether an operator-enforced boundary can limit data and block writes; test that boundary before relying on it.

If neither separate disablement nor a verifiable target-side boundary is available, compare a supported rollback or pause with time-limited use under explicit controls. A pause can delay diagnostics and return work to the NOC; continued use leaves scope unknown. Continue only if evidence bounds the exposure and the service owner confirms diagnostic value and fallback. Document any continuing exposure under Chapter 5’s authority model; if scope cannot be bounded or no authorized decision-maker is available, escalate rather than treating schedule pressure as acceptance. Compare lost diagnostic benefit and manual NOC work with supplier and engineering effort, change-window limits and service risk. No cost or saving is established here.

Evidence of broader collection or an unseen write path strengthens the case to pause or roll back. Independent disablement, safe fallback and tests showing allowed and denied actions may support restricted use. Verify the target-system result, principal in the logs, revocation and NOC visibility. If a safe test is unavailable, keep the boundary unverified and do not count it as risk reduction.

Inventory shows where to look. Access review shows whether an agent has more authority than its task requires.

## Move 2: Match authority to the task

The review can start with identities and tools that have the greatest potential service impact. An assistant that can read subscriber records, open a change request or reach a network-management API deserves closer scrutiny than one limited to public guidance.

The core questions are what data the agent can read, what actions it can take, and whether its access can be stopped without disabling a surrounding service.

Where the platform allows it, the agent can use a dedicated identity rather than an employee account or broad shared-service permissions. Access can be limited to the data and tools needed for the task. Short-lived credentials issued only when needed may help. Logs should show which identity acted, what tool it called and what happened.

A configuration describes the intended boundary; it does not establish what the deployed integration can reach. For one or two high-impact uses, trace an allowed and an out-of-scope request from the agent identity through the connector to the target system. Confirm that the excluded access is refused, logs identify the action and principal, and revocation closes the relevant path. Include any persistent memory as a separate read/write path and apply Chapter 2’s synthetic-marker check for scope and clearing; supplier documentation alone is not an operator test. Test in a suitable environment or supported window without disrupting monitoring or service assurance. If a supplier-managed control cannot be verified directly, record that as an assurance limitation rather than treating the design description as proof.

It helps to distinguish read, recommend and execute. Read-only access is often a sensible start. A low-impact, reversible action may fit within clear limits and monitoring. Actions that could change production, affect customers or interrupt an essential workflow should remain within the operator’s normal authorization and change process. An agent can prepare a change; an authorized person approves and validates it.

A human approval step is effective only if the reviewer can see the evidence behind the recommendation, understand the affected service and decline the action. If the reviewer sees only a generated summary or a pre-filled change request, the approval may become procedural. Control effectiveness depends on whether the person has enough context and authority to make a different decision, not on how many approval boxes appear in the workflow.

CISA and its international partners advise limiting agent access to sensitive data and critical systems, and starting with low-risk uses. This is general guidance, not a telco control standard. Legacy platforms and supplier connections matter as much as modern APIs. If a legacy system cannot support a separate identity, a controlled gateway may help. Until then, read-only access may be safer.

**Illustrative read/recommend/execute authority matrix.** Adapt the boundaries to service impact and the operator’s architecture; the matrix is a decision aid, not a universal policy.

| Level | What the agent may do | Boundary and evidence | Decision consequence |
|---|---|---|---|
| **Read** | Retrieve only the data needed for the stated task. | Enforce read-only rights at the target or controlled connector; test an in-scope and out-of-scope request, confirm the principal in logs, and check retention and data destination. | If the task needs neighboring-domain data, use a separately authorized, time-bounded path where feasible. If the source or identity cannot be verified, do not treat “read-only” as low risk by default. |
| **Recommend** | Produce a draft, diagnosis or proposed action without submitting a change. | Include source records and enough service context for a qualified operator to verify the reasoning. Confirm the recommendation cannot invoke a hidden write path or trigger downstream execution. | This can preserve analytical value while keeping the decision with the service team, but it still influences triage and can misdirect work if the evidence is incomplete. |
| **Execute** | Perform a narrowly defined action only where the operator has deliberately delegated it. | Scope the target and parameters; set preconditions and limits; test stop, audit and rollback; preserve the normal change process for material service-impacting actions. | If action cannot be bounded, observed or reversed safely, keep the workflow at recommendation-only. Any delegated execution needs a named owner and a service fallback. |

The level should follow the consequence, not the product label. A ticket update may be low impact in one workflow and operationally significant in another. Before moving a use from read to recommendation or execution, the service owner should see test evidence that the new boundary holds and understand what work becomes slower or manual if the agent is restricted. Security validates identity and control behavior; widening authority depends on the tested boundary and the service impact of restriction.

**Shared edge/core service account.** Chapter 1 establishes that one account reaches edge nodes and parts of the core. Moving to separate access may reduce reach and improve attribution, but the operator still has to identify dependent workflows and prove the new boundary after the change.

Separating that access can improve attribution and limit the path between edge and core, but the boundary also has to be operated. Account ownership, credential rotation, supplier support and rollback determine whether it remains effective. A gateway may help where a legacy platform cannot issue a distinct identity; it also adds a dependency that needs monitoring and recovery planning. If separation must wait, narrow the access only if the platform can enforce and log that scope; otherwise, keep the full reach visible and agree the supplier-supported change path.

Treat the edge fix as a migration, not just an access edit. Map dependent workflows and agree the supplier change and rollback before the window; use the gate below to decide whether the service is ready and whether the new boundary is proven.

**Illustrative change gate: edge access.** Use this record to decide whether the identity migration is ready, not as a substitute for the operator’s change process. Values marked for local confirmation still require operator evidence.

| Gate | What the team must establish | Decision if evidence is missing |
|---|---|---|
| Baseline and service impact | Name affected edge/core services, dependent workflows and monitoring. Map the old identity’s reachable targets and logs; the service owner sets impact and tolerance. | Do not assume removal is safe. Map the path and fallback before choosing scope. |
| Change readiness | Confirm supplier-supported steps, participation, test/window, effort and rollback condition. The change lead confirms staff, communications and authority to pause. | Keep the work open; compare a later supported window with an interim restriction already shown to work. |
| Post-change proof | Verify the new identity reaches only the intended edge path, the old identity is denied core access, and logs, monitoring and essential workflows remain usable. | A completed ticket or configuration push is not proof. Failed or inconclusive checks leave the boundary unverified. |
| Rollback and review | Confirm rollback restores service and whether it restores broad access. Link any temporary exposure to Chapter 5’s decision record and a review trigger. | If rollback restores the shared path, mark the migration incomplete and keep the exception visible. |

This gate makes cost visible without inventing a budget. Estimate supplier engineering, network and identity work, test capacity, NOC backfill and the maintenance window from local evidence. Compare that effort with the cost of continuing broad access and the service consequences of a failed change. If the permanent fix cannot proceed, a narrower interim treatment helps only when its boundary and service effect are evidenced. Link any continuing exposure to Chapter 5’s decision record.

Permissions matter only if teams can contain a failure without losing the surrounding service. That takes rehearsal.

## Move 3: Rehearsal tests the response before an incident

A policy alone may not tell the night shift who can revoke a compromised identity. A tabletop can expose that gap before an incident does. Its value is in testing decisions and service impact, not demonstrating an AI product.

A tabletop does not prove that a technical control works. It can establish who has authority, what information is needed and which services may be affected. A bounded technical validation is still needed to confirm that revocation blocks the relevant tool paths and that monitoring remains available. Run that test in a suitable environment or supported change window, not as an unplanned experiment on a live core. If no safe test is available, label the boundary unverified, restrict action authority and plan the manual fallback before relying on it.

Bring the SOC and NOC, identity and platform owners, service assurance, change management and business continuity into the exercise. Legal, communications, procurement and a supplier contact can join when the scenario needs them. Center it on a decision that could affect a service.

A rehearsal can make the authority boundary explicit. The operator can pre-authorize suspension of a dedicated agent identity under defined conditions, while requiring service-owner input when revocation would also remove NOC visibility or supplier-case handling. That distinction is not a reason to delay containment when misuse is confirmed. Start the fallback with the containment action; the NOC should not have to choose under pressure between leaving access active and making a broad change.

The Canadian Centre for Cyber Security recommends practising for incidents that may unfold within hours, with isolation steps approved in advance and manual alternatives tested for critical functions. CISA, ASD ACSC and partner agencies’ joint guidance also warns that external content can carry instructions designed to steer an agent, a risk known as indirect prompt injection. These are general recommendations. Operators can test them against their own systems and response roles.

A separate CISA CI Fortify tabletop package presents a hypothetical telecommunications outage and asks teams to examine isolation, third-party dependencies and manual operations. It is a U.S. critical-infrastructure exercise template, not an AI-specific scenario or a reported incident. Operators can add an agent identity or tool failure to test those continuity decisions.

CISA, FBI and international partners’ September 2026 guidance for service providers emphasizes clear, timely outage communications that preserve operational security and containment. An exercise can clarify who approves an update, when it is sent and which backup channel remains if containment changes service availability.

Set the exercise’s success criteria before starting: which access must be stopped, what service or visibility must remain, who may authorize containment, and what response or recovery tolerances apply. A fast revocation is not a pass if it hides alarms or removes the only recovery path. A short rehearsal can focus on one critical service domain, separate from live production changes. Tolerances are best set with the service owner; one target will not fit every service. Record decisions, elapsed time, service impact, missing information and fallback. A later review can establish whether the gaps have closed.

**NOC assistant exercise.** Chapter 1 establishes broad service-account reach and a proposed visibility-reducing change. Use these facts for a bounded tabletop, then validate control behavior in a safe environment or supported window. Test whether the SOC and NOC can contain the path without losing essential visibility, while keeping network changes in normal change control. The exercise tests authority and continuity, not a product.

| Stage | Exercise prompt | Evidence of a useful response |
|---|---|---|
| Establish the normal path | The assistant summarizes alarms and drafts a ticket. Ask what identity and data path the teams expect. | Identify the service, principal, connector, logs and operational owner. |
| Review broader access | The account can open vendor cases and read neighboring-domain data. Which scopes does the task need? | Separate required reads, recommendations and actions; identify any temporary expansion trigger. |
| Proposed visibility-reducing change | What evidence, containment and fallback are needed? Keep the proposal in normal change control. | NOC explains service impact; SOC provides threat evidence; service owner identifies fallback. |
| Test stop and fallback | Tabletop revocation, then separately validate identity and downstream behavior in a safe test or supported window. | Test new and existing access, principal logs, target result and essential monitoring. |
| Close open gaps | Assign interim treatment, retest, review trigger and supplier dependency. | Record the disposition; failed tests or changed service conditions reopen the issue. |

The decision should compare a tested separation of read and action rights with a temporary restriction that returns work to NOC staff. Separation depends on identity design and supplier support; restriction can slow diagnostics and case handling. If neither boundary is proven, keep action authority restricted unless a time-limited exception is accepted through Chapter 5’s process. Exercise findings can support capacity or supplier requests, but only technical validation shows whether a control works.

## Move 4: A funded roadmap beats a collection of tools

The first three moves reveal gaps in authority, control effectiveness and response. Leaders can use those findings to decide what to fund and what risk they can accept. A credible board paper names the service at risk, proposed work, required resources and remaining risk.

A 12-month roadmap should hold three or four priorities, not every desirable control. Give each a sponsor, delivery lead, target window, dependencies, cost estimate and decision gate. Show supplier and legacy-system constraints. Explain the cost of delay in operator terms: customer-data exposure, reduced network control, slower containment, missed duties or lost service.

Priority should follow service risk, not AI novelty. Compare affected services, identity/tool reach, control effectiveness and the safety of change. A high-impact gap with a long supplier dependency may need an interim treatment and an accelerated supplier plan; a lower-impact use with a reversible change may wait. Make the basis visible without pretending one score can rank every use.

**Compare competing work with the same evidence.** When fixes compete for engineering capacity or a maintenance window, use four questions before ranking them:

| Question | Evidence to bring | Trade-off the decision must show |
|---|---|---|
| What service and path are exposed? | Affected service, identity, reachable systems or data, existing controls and gaps. Mark unverified reach as unknown. | Service consequence if the path is misused or stays open. |
| What risk does the treatment reduce? | The boundary changed and a test or observation of the result. | Prevention, detection, containment or recovery; do not count them as equivalent. |
| What does implementation cost? | Engineering/test effort, supplier charges, backfill and window needs, transition/exit cost; show estimate basis and uncertainty. | Risk reduced versus displaced work, lost diagnostic value, recurring dependency and new operational risk. |
| What remains open? | Supplier commitment, supported procedure, rollback, fallback and reassessment trigger. | Whether exposure fits appetite and delegation, or must be escalated before deferral. |

Where a proposal also claims operator efficiency, Chapter 1’s NOC-assistant benefit check measures time to a validated result, review/rework, service quality, cost and dependency. Use those operator results alongside this risk comparison, not in place of it.

The shared edge/core account and deferred patch window show why a simple ranking is not yet defensible. The account reaches edge nodes and parts of the core; a supplier change and safe window are needed. A fixed patch release exists, but the next suitable window is three weeks away. These facts do not establish comparative service impact, interim-control effectiveness or effort. Do not rank by labels such as “core” or by release availability; obtain the missing impact, fallback, support and effort evidence.

**When capacity permits only one change.** If staffing or a supported window allows only one change this cycle, compare affected services and fallback, reach and threat, supported options, supplier lead time, rollback, effort and deferral cost. Mark each point verified, assumed or unknown. A temporary restriction counts only when a safe test shows its effect; monitoring is not prevention.

Escalate any exposure outside appetite or beyond delegated authority, and show which other work would move. If both remain within appetite, sequence them using tested interim controls, continuity impact and deferral cost, then record the review trigger through Chapter 5’s decision process. Missing critical evidence keeps the choice open; a booked window is not remediation.

An interim treatment should name the path it is meant to constrain and the evidence that it does so. A narrower identity may reduce reach; additional monitoring may help detect misuse but does not prevent access. Those controls have different effects and should not be reported as equivalent. If a restriction slows diagnostics or shifts work back to manual operations, record that service cost alongside the exposure it reduces.

Measures should show whether risk is changing, not how many tools were purchased. Useful indicators include named owners and data paths for high-impact uses, tested access revocation, clear containment authority, exercised service alternatives and closed exercise findings. A tool count can rise while access and response stay the same.

A policy is not proof. For high-impact uses, board assurance should focus on observed control behavior under service conditions, independent review where justified, and unresolved service impact. A purchase, policy or successful staging test alone does not show that the production boundary works.

Regulation belongs in this roadmap, but it need not delay action. Legal and Compliance can track binding obligations by market and separate them from consultation drafts. Where duties overlap with identity, supplier assurance, incident reporting or continuity, existing governance may be enough; a separate AI approval board is not always needed.

At an executive review, the CISO and CTO should connect each funding or change-window request to the exposure it will reduce, the work it will displace and the evidence that will show progress. State what would reopen the choice if delivery slips or conditions change.

**Deferred patch window.** The next safe window is three weeks away. The roadmap must show the service cost of an earlier change and the exposure of waiting, then identify evidence that would reopen the choice if threat, interim controls or service conditions change.

Chapter 3 separates threat and reach checks from change readiness. Apply that distinction here. The fixed release and three-week window are the known timing facts; they do not establish whether the deployed live-core version is affected, whether the relevant path is reachable, or whether an interim restriction works. Security and platform teams verify version and reach. The control owner and NOC test any restriction and its effect on monitoring and service. The service owner supplies impact and fallback evidence. Engineering and the supplier confirm the earliest supported window, test requirements and rollback. A public threat signal can raise urgency, but it cannot prove local exposure or make an unsupported live-core change safe.

Compare three routes. Ask the supplier and Engineering to bring forward the earliest supported change; it can shorten exposure but needs capacity, may incur expedite costs and can displace other work. Keep the scheduled window and rely only on controls already shown to reduce the reachable path; this preserves planned test and rollback conditions but leaves some exposure and may consume NOC/SOC effort or restrict a service function. Temporarily narrow or suspend affected access only if a Level 3 test demonstrates that the restriction denies the relevant path under tested conditions and preserves an adequate fallback; this can reduce reach sooner but may disrupt dependent services. Estimate supplier, engineering, test, backfill and rollback effort from local evidence; no cost figure is established here.

On the available facts, ask the supplier and Engineering for the earliest supported change, but do not execute it early until local version, reach and service impact justify the added cost and the test/rollback path remains sound. Keep the scheduled window as the fallback. During the wait, rely on an interim restriction only after a Level 3 test shows that the relevant path is denied under test conditions while required service visibility remains available. If no effective restriction exists, do not describe waiting as controlled. Bring the change forward when local evidence confirms a reachable affected version or credible threat evidence materially raises urgency, and the supplier can support the earlier path safely. If no safe earlier path exists and the service cannot tolerate continued exposure, escalate for a service-specific restriction. Any remaining exposure needs the Chapter 5 decision record; escalate if it exceeds appetite or no executive has authority over the affected services.

Reopen the choice if the deployed version or reachable path changes, a restriction fails, supplier support changes, the window slips, new threat evidence changes urgency or service impact/fallback changes. Before and after the change, verify the targeted version, denied access path, attributable logs, monitoring, service health and rollback. Until the supported change is applied and those results are recorded, a booked window is a schedule commitment, not risk reduction.

**Illustrative planning sequence for the next 12 months.** These are decision stages, not prescribed dates or universal deadlines. Place them against the operator’s change calendar, supplier commitments and service priorities. Completing a deliverable is not evidence of risk reduction.

| Stage | Lead, decision and dependency | Evidence required to proceed or close |
|---|---|---|
| **Establish the baseline** | Security lead with service/platform teams maps the supplier diagnostic, NOC assistant and edge-account paths; obtain supplier, product and identity records. | Known/unknown identities, data, actions and reach; identify gaps needing immediate restriction. A baseline is not proof of control effectiveness. |
| **Before widening authority** | Identity/platform, Network Engineering, NOC and supplier plan read/action boundaries and edge migration; test capacity and a supported window are prerequisites. | Configuration review, allowed/denied tests, attributable logs and revocation result. Without safe testing, keep treatment interim and mark the boundary unverified. |
| **Before relying on containment** | Incident-response lead with SOC/NOC, service assurance, change management and supplier rehearses the NOC assistant and fallback; map identities first. | Local decision/timing results plus technical revocation and visibility tests. Keep tabletop claims separate from technical evidence. |
| **At portfolio review** | CTO/CISO sponsors and resource leads sequence work, dependencies and capacity; patch and edge migration need supported windows. | Separate delivery from tested risk reduction; report service impact, test results, dependencies and triggers. Count patching after effectiveness checks. |

Before agreeing a stage, estimate network and identity engineering, NOC/SOC backfill, supplier work, test environments and change windows. Show the estimate basis and which work would move; if unknown, mark it pending rather than inventing a budget or implying that the work costs nothing.

Reopen a stage when a dependency fails, access expands, a test fails or service conditions change. Shared identities or supplier paths that cross service domains need a decision at the authority boundary; escalate when delegated authority does not cover the full impact.

## Keep the sequence, adjust the pace

Use the sequence as a portfolio plan, not a calendar. Restrict clearly excessive production access before the full review when the restriction is safe; Chapter 5 turns the remaining evidence and service choices into an executive decision.
