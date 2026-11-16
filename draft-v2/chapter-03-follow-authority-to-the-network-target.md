# Chapter 3: Follow Authority to the Network Target

A radio application can create a network-control risk without being called an AI agent. In a 2024 peer-reviewed study, researchers built an experimental Open Radio Access Network (O-RAN) H-Release environment and found missing access controls for xApps, applications deployed on an O-RAN controller. They demonstrated three attacks through application programming interfaces (APIs) and the E2 interface, including attacks that disrupted radio access network (RAN) components. This was a lab result, not proof that a carrier’s production network has the same path. It leaves a practical question: which identity can reach which target, through which interface, and what can that target do?

The study did not test a large language model (LLM)-based agent; the applications were not automatically AI agents. The weakness was not bad model advice, but insufficient control over what an application could reach through network-management interfaces. That distinction still matters when a language model joins an operational workflow. It may reason about a change, but a runtime must call a tool, the tool must use a credential, and an API must accept the request before the target can alter the network.

What matters is the authority each step in that chain carries.

## Follow one identity to its target

**Illustrative scenario: a shared account across edge and core.** One service account can reach edge nodes and parts of the core. Remediation depends on the supplier’s configuration and a safe maintenance window. The situation does not say whether an AI agent used the account, which commands the target would accept, or whether separate identities are supported.

**Assumptions for the example.** A maintenance assistant reads edge alarms and configuration, then prepares a supplier-supported change through an operator connector. The connector uses the shared account. Its intended task is limited to the edge service, although that account can also reach part of the core. No local test has shown whether the target distinguishes an edge request from a core request. These added details make the trade-off concrete; they are not part of the supplied situation.

Follow the request from the alarm data to the target. The assistant reads the data; its runtime passes a request to the maintenance connector, which presents the shared account to a target API. The target sees the account, not necessarily the assistant, the person who asked for the work or the edge-only purpose. If it accepts a core operation under that identity, the account can do more than the assistant’s task requires. An approval screen narrows nothing unless it names the exact target and operation and the target enforces that limit.

This is why “human in the loop” is not a permission model. It describes a role in a process. It does not tell us whether approval happens before execution, whether the reviewer sees the exact request, which credentials perform it, or whether the target enforces the intended limit.

Keeping the account as it is avoids a rushed migration and preserves the supplier’s current support route. But edge and core remain joined under one principal. If something goes wrong, logs may show that the account acted without showing which workflow or person started the request. Giving the assistant this credential would also give its edge task reach into the core.

A gateway can buy time, but only if every route to the target passes through it, there is no bypass, and it can block core operations while allowing the edge work. Test what happens when it fails. A fail-closed gateway may interrupt support; a fail-open one may restore the broad path. Drawing the gateway on a diagram does not prove that it controls the target.

Use separate target identities if the platform supports them: an edge identity for edge work and a different core identity for workflows that need it. The move takes engineering and supplier time. Running old and new accounts in parallel can expose missing permissions, but extends the overlap. Retiring the old account first shortens that period, yet may interrupt monitoring or supplier support. A staged migration takes longer; it lets the team check each workflow before removing the shared account.

Given these assumptions, keep the assistant out of the write path. Network Engineering and the supplier should confirm which identities the platform supports and plan a safe move. The CISO sets the boundary: no agent write access through the shared account until the target enforces the intended limit. The service executive owns any period when support must remain broad; until then, keep the existing route for its authorized purpose, not the assistant. A gateway may help in the meantime, but test it first: edge requests should pass, core requests should fail, alternate routes should not bypass it, and logs and revocation should work even if the gateway fails. Keep an emergency route, but make sure it does not recreate the same broad access.

Revisit this recommendation if the target cannot support separate identities, if a tested gateway blocks every alternate route without disrupting required support, or if the maintenance path has different service dependencies. Local logs may also show that the account can already perform a sensitive core action. If so, reduce its scope or make an authorized service decision now; do not let a longer inventory delay the response. The deciding facts are the target’s permissions, the routes into it and how each restriction affects the service.

## From influence to permission

Data can influence an agent without carrying a credential. A tool can hold a credential without making every model output executable. And a target can reject a request even when the model and connector agree. These are separate boundaries.

The peer-reviewed AgentDojo benchmark illustrates the first boundary. Researchers used simulated tool environments to test how instructions hidden in third-party data could influence an agent. They demonstrated an indirect prompt-injection mechanism: data returned by a tool can be treated as instructions and redirect later tool use. The benchmark does not test telecom systems, measure how often this happens at operators or show that an injection changes network state by itself.

For an operator, the point is not to decide whether retrieved content is “trusted” in the abstract. It is to ask what the workflow can do after reading it. A ticket summary is different from a tool call that can submit a change. A proposal is not an executed action. If the workflow can act, the target must still enforce the limit when the model or runtime is wrong.

Zero Trust and identity governance answer different questions. The United States National Institute of Standards and Technology (NIST) describes Zero Trust as moving protection away from static network perimeters toward users, assets and resources. Its Special Publication 800-207 describes an architecture; it is not a telecom rule. Identity governance helps establish who owns an account and how its privileges change. Neither label shows that a connector stays within the target’s policy. Identify the enforcement point.

Apply the same discipline to the workflow map. Follow who starts the task, which identity it uses, what records it reads, which connector it calls, what target decides and which service could be affected. If the target sees only a shared account, say so. If logs show a request but not the resulting network state, the outcome is unknown. Operators do not all have the same path; each needs to trace its own.

Tracing authority is only half the story. When the workflow stops, does the target stop too—and can the NOC still see the service?

<!-- Non-reader-facing source/claim map. Exact source links, evidence classes and limitations remain in research/draft-v2-source-map.md and research/claim-ledger.md.
P1-P2: T20, peer-reviewed experimental O-RAN H-Release study; lab attacks through APIs/E2 and service disruption in testbed, not a carrier deployment; the study did not test an LLM agent.
P4-P5: Author-supplied shared edge/core account situation plus clearly labeled educational assumptions; the account’s exact commands, target enforcement and AI use are not established.
P6-P12: Author analysis/recommendations; choices and trade-offs are conditional on local target and supplier evidence.
P14: T19, peer-reviewed AgentDojo benchmark in simulated tools; not telecom or an operator incident.
P16: T2, NIST SP 800-207 framing; voluntary architecture publication, not telecom regulation.
All remaining content is author analysis and advice; it does not assert universal carrier paths, practices or outcomes.
-->