# Chapter 4: Prove Safe Authority and Service-Safe Response

A diagram can show where an agent is supposed to stop. It cannot prove that the target will stop it.

Chapter 3 followed an identity to the network target. Now the question is what the operator can observe and control when a workflow misbehaves. A design review shows where approval is meant to happen. A benchmark tests a model on defined tasks; a lab tests an API in one configuration; a tabletop shows how people respond. Each helps in a different way. None, on its own, proves that the live service is safe or recoverable.

## The assistant stops. Does its authority?

**Illustrative scenario: an assistant that can narrow the Network Operations Center (NOC) view.** The assistant summarizes alarms, drafts ticket updates, reads data from a neighboring domain and opens supplier cases. It once proposed a change that could reduce the NOC’s visibility; that change was not executed. The situation does not say which identity, connector or target it used, or whether it could write directly to the network.

**Assumptions for the example.** The assistant uses one shared service identity through connectors to the ticket system and alarm platform. That identity also authorizes neighboring-domain reads and supplier-case submissions. The proposed visibility change would alter alarm routing. The identity can be revoked only as a whole, and no independent alarm-read path has been verified. These assumptions make the choice concrete; they are not part of the supplied situation.

The intended job sounds modest: collect alarms, summarize them and prepare a ticket or supplier case for an operator. But the service identity is also allowed to read neighboring-domain data, submit supplier cases and, under the exercise assumption, request a change to the monitoring view. The authority now exceeds the summarization task. A model proposing the change is not the same as a target accepting it. The operator must find out where the request stopped.

A stop command at the assistant may prevent the runtime from starting another tool call. It does not necessarily revoke the connector’s credential, terminate a session already opened at the ticket or monitoring system, or cancel a request already accepted and waiting in a queue. Those components have separate state. The assistant can report “stopped” while the target still has a valid session or a pending operation.

Start with event identifiers that link the runtime, connector and target logs. They should tell you whether the target accepted the request, which identity presented it, whether a session remains open and whether work is queued. Revoke the credential at its source, close target-side sessions, and cancel or account for accepted requests. Then compare the target’s current state with the authoritative network and alarm records. The assistant’s “stopped” message cannot answer those questions.

The alarm view changes the choice. If operators can read authoritative alarms through a separate, tested path, they can revoke the assistant’s broad identity without going blind. If the same identity supplies both the assistant and the only NOC alarm view, revocation may remove the very information needed to manage the service. That does not justify leaving write authority open. It means the team must first establish an independent view or make an explicit service decision about the temporary loss of visibility.

The team can disable the assistant and revoke its identity. That blocks future use of the principal, but may interrupt alarm reads and supplier cases; live sessions and queued work still need attention. If the target separates permissions and the NOC has a reliable view, block write and case submissions while keeping reads. Or leave the assistant at read-and-draft and have a person submit changes through the normal process. That keeps some support in place, but still requires a narrow identity and visible source records.

With these assumptions, do not let the assistant change alarm routing or submit supplier cases through the shared identity. Keep it out of the action path until Network Operations has an independent alarm view. Then revoke the broad credential and close the target sessions. The CISO advises on containment; the NOC and network engineers confirm service state and alternatives. Without an independent view, the service executive and incident lead must weigh lost visibility against evidence of misuse and choose a supported mode. An unauthorized target action requires containment. It does not make the loss of visibility harmless.

Before turning the assistant back on, give alarm reads and ticket drafts separate, task-limited identities. Keep configuration changes in the existing human-approved process. In a safe test, verify that the target denies a prohibited monitoring change, that the intended read path still works, and that revocation ends active sessions and pending work. If the target cannot separate these permissions, keep submissions outside the assistant. Reconsider only when logs, permission tests and an independent NOC view show a narrower path that can be recovered safely.

## Test what the network enforces

A convincing demonstration is not proof that the live path is controlled. The connector may still hold broad credentials; an approver may not see the exact target and action; a mock API may refuse a request that the production target accepts under another identity. Test the intended path with the identity and target that make the final decision.

Compare a request that should pass with one that should fail. An alarm-read identity should return approved data but be denied a change to alarm routing. The logs should show which identity called the target, what it accepted or refused, and whether network or monitoring state changed. Try the denied request through alternate connectors and service accounts too. One blocked route does not prove the boundary if another still reaches the target.

Test the stop with work in flight. Start an approved request, stop the runtime and revoke its credential. Then see whether the connector retries, the target session survives or queued work completes. Stopping one component does not stop the next automatically. Record the software, identity, target and conditions tested; a later connector or policy change may invalidate the result.

The O-RAN study in Chapter 3 and the AgentDojo benchmark can help teams choose test cases. One exposed access-control weaknesses in a research testbed; the other demonstrated indirect prompt injection in simulated tool environments. Neither establishes how often those weaknesses occur in a carrier network or whether a particular operator blocks them. Use them to ask better questions, not to claim that your control passed.

Every test has limits. A paper review may reveal an omitted identity. A benchmark probes only its defined tasks; a lab shows behavior in that environment. Production observation can support a bounded live result, but only if the conditions and denominator are recorded. A tabletop shows how people decide and communicate. These forms of evidence answer different questions; none covers them all.

## Make recovery part of the decision

When a workflow is isolated, someone must check what changed in the network and what the NOC can still see. The incident lead coordinates containment; the service owner understands the impact and restoration constraints. The executive accountable for the service decides within their delegated authority. If that authority does not cover the service, or the remaining risk exceeds appetite, escalate it. Do not let a committee or approval screen stand in for an authorized decision.

A fallback works only if the people who need it can see authoritative service state, have the right permissions and know what to do. “A human can take over” is not enough. Before the assistant becomes operationally important, confirm the alarm source, manual change route, supplier support and on-call roles. A fallback that depends on the same identity, connector or supplier is not independent.

Restore only the smallest useful capability at first. Here, that could mean bringing back alarm reads under a new, narrow identity while keeping monitoring changes and supplier submissions outside the assistant. Before re-enabling anything, check target state, active sessions and queued work. Add permissions one at a time. If a denied action succeeds, the caller cannot be identified or the alarm view degrades, return to the last verified state and investigate.

Pausing a risky workflow can cost the team visibility. Leaving broad authority in place can cost security. Separate the action path from the service view whenever possible. If they cannot be separated, state the service impact and agree the fallback before choosing.

Supplier support and legal duties determine whether the operator can maintain that boundary and whether it can leave without disrupting the service. Chapter 5 looks at both.

<!-- Non-reader-facing claim/source map. Exact source details and limits are in research/draft-v2-source-map.md and research/claim-ledger.md.
P3: Author-supplied NOC-assistant situation; alarm summaries, draft ticket updates, neighboring-domain data, supplier cases and proposed visibility-reducing change not executed. It is illustrative, not an incident or test.
P4: Explicit educational assumptions about shared identity, connectors, monitoring target, whole-identity revocation and lack of verified independent alarm path; not facts about an operator.
P6-P11: Author analysis and recommendations conditional on the exercise assumptions; no operator stop, session-revocation or recovery result is asserted.
P15: T19 (AgentDojo simulated benchmark) and T20 (experimental O-RAN testbed); each is limited to its own tested setting.
P1-P2, P5, P12-P14, P16-P21: Author analysis and scope-limited test/response recommendations; no operator test or result asserted.
-->