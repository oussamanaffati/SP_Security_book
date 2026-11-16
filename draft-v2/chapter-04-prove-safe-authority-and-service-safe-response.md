# 4. Prove Safe Authority and Service-Safe Response

A diagram can show where an agent is supposed to stop. It cannot prove that the target will stop it.

That difference matters when a workflow moves from recommendation to action. A design review may show a human approval step. A benchmark may show that a model resists a class of prompt injection. A lab may show that an API rejects a request. An exercise may show that the NOC knows whom to call. Each is useful evidence. None, on its own, proves that the whole operator workflow is safe or that the service can be restored when something goes wrong.

The practical question is not whether a system “passed testing.” It is what exact claim the test supports, under which conditions, and what remains untested.

## Test the path that can change the network

Start with one workflow and the action it might perform. Chapter 3 mapped the identities and interfaces. Now test the actual path: the principal that runs the action, the credential it uses, the connector and API in between, and the target’s own authorization decision. A model’s answer is not the point of control if another component can still submit a change.

Test both sides of the boundary. The allowed operation should work within its stated scope. A similar operation against the wrong target, outside the permitted range, or without the required approval should fail at the enforcement point. The record should show not only what the assistant displayed, but which identity made the request, what the target accepted or rejected, and what state changed.

Then test the parts that are easy to miss in a clean demonstration. Does a delegated token remain usable after the user’s session ends? Can a queued action run after the interface says “stop”? Does a retry submit the request again? Do another connector or service account provide a second route to the same target? Can the operator distinguish a model proposal, an API submission, a target-side rejection and a completed state change in the logs?

These are not assumptions about every product. They are questions for the implementation in front of you. A stop button is evidence only if its effect is observed at the component that holds authority, including any sessions or work already in flight.

For each test, write down the expected result before running it. Name the software and policy versions, identity, target, action, data conditions and approval path. Keep the request and target-side evidence. Record what happened, what could not be observed, and what was not tested. If the evidence came from a mock API or isolated lab, say so. It can establish behavior in that lab; it does not establish production behavior on a different network or with another credential path.

This is where evidence labels become useful. A paper review can expose a missing control. A benchmark can probe a defined set of tasks and failure modes. A lab test can establish behavior in the tested configuration. A production observation can show what happened in a bounded live workflow, if the operator records the relevant denominator and conditions. A tabletop can test decisions and communication. These forms answer different questions; they are not a ladder where one automatically replaces the others.

NIST’s tool-use workshop synthesis identifies several dimensions: what actions a tool permits, its access patterns, reversibility, monitoring and the autonomy it enables. It is expert discussion, not a consensus standard or a production test. That is still a useful prompt for an operator: a read-only action with good monitoring and straightforward reversal is not the same risk as a write action with broad reach, hidden sessions and an uncertain recovery path.

A benchmark can help find a weakness, too, but it cannot certify the operator’s controls. AgentDojo demonstrates indirect prompt-injection mechanisms in simulated tool environments. The O-RAN xApp study demonstrates access-control and interface weaknesses in a research testbed. Neither study establishes how often the same weakness occurs in a carrier network or whether a particular operator’s control blocks it. Use this work to choose test cases, not to claim that your own boundary has passed.

## A stop is not a recovery plan

When a test reveals unexpected authority, the first instinct may be to disable the entire workflow. Sometimes that is the right immediate containment. But stopping a workflow and preserving service are separate decisions. Disabling a connector may remove a route for harmful changes; it may also remove a useful view or handoff. Revoking one token may leave another valid. Pausing an agent may not cancel actions already accepted by the target.

The operator needs a pre-agreed response that states who can stop new actions, who can revoke credentials, who confirms the network state, and who decides when the workflow can resume. Incident command may coordinate the event, but the service owner supplies impact and restoration constraints. The executive accountable for the affected service accepts residual service risk only within delegated authority and appetite. These roles should be clear before pressure makes every decision slower.

Use the NOC-assistant composite as a bounded rehearsal prompt, not as a reported incident or test result. It raises questions about data from a neighboring domain and reduced NOC visibility. Do not assume that the assistant changed network state. Ask what the team would need to establish: whether the data boundary was crossed, whether the assistant could act or only present information, which identity made any downstream request, and whether the NOC can still see authoritative alarms and target state if the assistant is paused.

The purpose is not to rehearse a dramatic “kill switch” moment. It is to find the point where security containment and service operations meet. A SOC analyst may identify suspicious activity. The platform team may be able to revoke a token. The NOC may know whether the affected alarms are available through another path. The service owner may know which actions cannot wait for the next change window. Those facts need to reach the person authorized to choose among isolation, narrower restrictions, manual operation or continued observation.

A service-safe response exercise should therefore include the people who can answer those questions, not only the team that owns the model. Use the actual escalation routes and after-hours cover. State what evidence is available, what is missing, what can be stopped immediately, and which changes require normal approval or an emergency change process. Do not invent a universal response-time target: set local tolerances from service obligations, operational capability and the consequences of delay.

## Make restoration part of the test

Rollback is often treated as the final line in a change plan. For an agentic workflow, it needs to be tested as an operational state transition. What is the known-good state? Can the team identify which target changes were accepted? Who confirms that dependent services have returned to their expected condition? What happens if a reversal is itself unsafe, unsupported or outside the approved window?

A non-production demonstration can show that a button or API call exists. It does not prove that the production system has the same dependencies, that the right people are available, or that a service can tolerate the reversal. Where production testing is not safe, record that limitation. Use a lab or controlled window to reduce uncertainty, then define the production evidence and operating conditions still needed before expanding authority.

The same discipline applies to fallback. “A human can take over” is not enough if the person cannot see the state, lacks the permissions, or has no supported manual procedure. Check that the fallback path is current and that the people expected to use it know where the authoritative information comes from. A safe design keeps the operator able to work when the model, connector, supplier service or network link is unavailable.

Repeat the relevant tests when the authority path changes: new tools, a different identity, a model or connector update, a new target API, or a change to approval and stop behavior. The exact trigger depends on the operator’s change process. The principle is simple: evidence about one version and one path does not silently cover a different one.

A useful test record is concise. It should let a service executive distinguish what was intended, what was observed, what evidence supports the result, what was not tested, who owns the gap, and what condition would permit broader use. “Passed” without those details is not an assurance statement. Neither is “human approved” without showing what the person saw and what identity actually executed the action.

The CISO should ask for two separate outcomes. First, evidence that the authority boundary works for the tested actions and paths. Second, evidence that the operator can detect, decide, contain and restore without creating an avoidable service failure. A narrow test may justify a narrow permission. It does not justify broad autonomy by implication.

The result is not a certificate of safety. It is a defensible operating decision: what may run, what must remain under approval, what will be stopped if conditions change, and what the operator still needs to prove before relying on it.

<!-- Non-reader-facing claim/source map. Exact source details and limits are recorded in research/research-map.md and research/draft-v2-source-map.md.
P1-P9: Author analysis and recommended scope-limited evidence/test practice; no claim that an operator performed a test or observed an outcome.
P10: T12 (NIST workshop synthesis identifies functionality/action, access patterns, risk/reversibility, monitoring and autonomy dimensions; expert discussion, not standard or production test).
P11: T19 (AgentDojo, peer-reviewed benchmark; simulated tool environments and indirect prompt-injection mechanism; not telecom/production); T20 (peer-reviewed experimental O-RAN H-Release testbed; access-control/API/E2 issues and lab attacks; not carrier deployment).
P12-P13, P15-P16: Author analysis and locally scoped response/recovery recommendations; no universal response deadline or operator outcome asserted.
P14: Author-supplied NOC-assistant composite, illustrative only; neighboring-domain data and reduced NOC visibility are exercise prompts, not a reported incident, operator practice or test result.
P17-P23: Author-recommended restoration, fallback, change-trigger and evidence-record practices; no test result or operator outcome asserted.
-->
