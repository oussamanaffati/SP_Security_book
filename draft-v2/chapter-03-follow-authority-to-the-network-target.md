# Chapter 3: Follow Authority to the Network Target

A radio application does not need to call itself an AI agent to create a network-control risk. A 2024 peer-reviewed study built an experimental Open Radio Access Network (O-RAN) H-Release environment and found missing access-control permissions for xApps, applications deployed on an O-RAN controller. The researchers demonstrated three attacks through application programming interfaces (APIs) and the E2 interface, including attacks that disrupted RAN components. That is a lab result, not evidence that the same path is present in a carrier’s production network. It points to a useful question for any automation: which identity can reach which target, through which interface? What can the target be persuaded or authorized to do?

These applications are not automatically AI agents, and this study did not test a large language model (LLM)-based agent. It matters here because it shows how authority can cross a software boundary and reach radio functions. The weakness was not a model making a poor recommendation. It was inadequate control over what an application could access through interfaces used to manage the network.

That distinction becomes essential when a workflow includes a language model. Reasoning about a configuration does not, by itself, grant a model a network identity. The surrounding runtime calls tools. Those tools may use a service account, delegated token or connector credential. The application programming interface (API) accepts or rejects a request. The target system applies its own authorization and state-change rules. The service sees the result.

The authority is in that chain, not in the product name.

## Separate influence from permission

A model can be influenced by data it reads without that data having a credential. A tool can hold a credential without every model output being executable. A target can reject a request even when a model and connector agree on what should happen. These are separate boundaries, and a useful review keeps them separate.

The peer-reviewed AgentDojo benchmark helps explain the first boundary. In simulated tool environments, the researchers tested how instructions hidden in third-party data could influence a tool-using agent’s behavior. The work demonstrates an indirect prompt-injection mechanism: data returned by a tool can be interpreted as instructions and can redirect later tool use. It does not test telecom systems, estimate how often this happens in operators, or show that a prompt injection can change network state by itself.

For a telecom workflow, the practical question is what authority is available after the data is read. If a workflow can retrieve a ticket, summarize it, and recommend an action, that is different from one that can invoke a write-capable API. If the model proposes a change, the proposal is not the change. Human approval is meaningful only when the reviewer can see the target and operation. The execution identity must not bypass that decision through another route.

This is why “human in the loop” is not a permission model. It describes a role in a process. It does not tell us whether approval happens before execution, whether the reviewer sees the exact request, which credentials perform it, or whether the target enforces the intended limit.

Zero Trust and identity governance answer different questions here. The United States National Institute of Standards and Technology (NIST) describes Zero Trust as moving protection away from static network perimeters toward users, assets and resources. NIST Special Publication 800-207 is an architecture publication, not a telecom rule. Identity governance helps answer who owns an account and how its privileges change. A model may interpret data and propose a tool call. None of those labels, alone or together, proves that a connector cannot act beyond the target’s policy. Name the enforcement point at each hop.

## Trace one real workflow

Do not begin with a list of models or a vendor’s architecture slide. Choose one workflow that matters to a service. Then follow the request all the way to the target. A table can make the gaps visible:

| Trace point | What the operator needs to establish |
|---|---|
| Request | Who or what initiates the workflow, and who owns the operational purpose? |
| Principal | Which human or non-human identity executes each step? What credentials or delegated tokens are used, and who can change them? |
| Context | Which records, telemetry or retrieved content enter the workflow? Who controls them, and which inputs should be treated as untrusted? |
| Tool and interface | Which connector, function or API is called? Is the operation read, recommend, draft or write? What targets and parameters are in scope? |
| Target | Which system makes the final authorization decision? What network state can the accepted operation change? |
| Service | Which service depends on that state, who owns its impact assessment, and where is the workflow’s authority recorded? |

The map should not end at “the model has access to operations support systems (OSS)” or “a human approves changes.” Those phrases are too broad to defend. Name the identity and permission at each hop. A workflow may read from one domain, call an API in another and affect a service owned by a third team. This does not prove that every carrier has such a path. It is a reason to trace the path in the operator’s environment rather than assume it stops at the model boundary.

Record the action level explicitly. *Read* means the workflow can retrieve information. *Recommend* means it returns a proposed action. *Draft* means it prepares a change for a separate system or person to submit. *Execute* means the workflow can submit a state-changing request under its own or a delegated credential; the target may still accept or reject it. The labels are not maturity grades. They describe different consequences and different evidence requirements.

The target matters because a successful tool call is not the same as a successful or safe service outcome. The API may accept a syntactically valid request; the network may apply it; the affected service may still be degraded. Conversely, a blocked API call may be logged by the connector but not by the target. A map that stops at the assistant’s response cannot answer what changed in the network.

CISA and international partners make a useful cross-sector recommendation: start with low-risk, non-sensitive use cases and avoid broad or unrestricted access, especially to sensitive data and critical systems. That is guidance, not a telecom-specific control standard. In an operator, “low risk” must be judged against the service, target, permitted action and fallback—not the familiarity of the model or the apparent simplicity of the task.

The map is complete when the operator can name the principal, data path, tool, target-side decision, possible state change and affected service. Anything missing is an evidence gap, not a reason to assume the workflow is safe or unsafe. Only then can the operator decide which boundary to test and which service limits must govern a response.

<!-- Non-reader-facing source/claim map. Exact passages, evidence classes, source links and limits are in research/research-map.md and research/draft-v2-source-map.md.
P1.S2-S4: T20 (peer-reviewed experimental O-RAN H-Release study; three lab attacks tied to xApp access-control/E2 issues; not a carrier production deployment; disclosed Trend Micro/NSTC support). P2.S1-S4: T20 (xApp/controller context and access-control mechanism; the study did not test LLM-based agents).
P6.S1-S4: T19 (NeurIPS benchmark; simulated tool environments and indirect prompt-injection mechanism; not telecom, not an operator incident, not a network-control frequency/effectiveness estimate). No tool-count metric used because source text conflicts.
P9.S1-S3: T2 (NIST SP 800-207 Zero Trust architecture framing; voluntary architecture publication, not telecom regulation). P9.S4-S7: author distinction among identity governance, model interpretation and target enforcement.
P14.S1-S2: O8 (CISA multi-agency guidance recommends low-risk/non-sensitive starts and avoiding broad access to sensitive data/critical systems; cross-sector guidance, not a telco standard).
All remaining material is author analysis and a locally applied authority-mapping aid; it does not claim operator-wide paths, deployments, incidents or test results.
-->