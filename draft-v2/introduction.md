# Introduction

When leadership asks its chief information security officer (CISO) to pause a workflow that uses artificial intelligence (AI), the request may be sensible. The network team may still need the same data feed, supplier console or alert path to see what is happening to a service. Leaving the workflow in place without a proven boundary creates another risk. This is the practical tension at the centre of the book: a pause can reduce one exposure and remove visibility or support needed to operate the service.

The answer is not to ban every model or to trust a supplier’s assurance. It is to understand the whole workflow. What data can it read? Which identity and connector does it use? What can it recommend, draft or change? Where does the target enforce permission? What remains visible when the workflow is stopped, and who can restore the service?

That is a service-provider security question, not only an AI question. An operator’s decision sits inside a service with dependencies, operating teams, suppliers, jurisdictions and supported change paths. A control that looks simple in a product demonstration may be difficult to remove from a live operating process. Conversely, a production label does not tell a CISO what a system can change, how widely it is used, or whether it has improved security.

This book does not claim that autonomous agents are the leading cause of telecom incidents. Public evidence shows different stages of deployment and different kinds of reported outcome. Public incident disclosures establish serious telecom targeting, but the sources reviewed here do not establish AI use in the named events. Those limits matter. A productivity claim is not proof of security effectiveness. A threat report is not proof of local exposure. A successful test supports only the path and conditions it actually exercised.

The chapters follow the decisions a CISO or chief technology officer (CTO) needs to make. Chapter 1 separates deployment stage, authority and outcome. Chapter 2 examines telecom intrusion evidence without assuming an AI cause. Chapter 3 follows identity, data, tools and permission to the network target. Chapter 4 asks what has been tested and whether the operator can contain and recover without losing the service view. Chapter 5 connects legal duties to supplier dependencies and exit. Chapter 6 turns those decisions into a small investment agenda for the next twelve months.

Read the book in order if you are building a common risk view. Each chapter uses the evidence and decisions established before it. If you are preparing a particular decision, start with the relevant chapter. Then return to Chapter 6 to make the service owner, evidence gate, dependency, cost, displaced work, fallback and residual risk explicit. The examples attributed to operators remain bounded by what their sources say. The four composites are illustrative prompts, not reported incidents, customer stories, or tests that were performed.

The aim is practical. A telecom CISO should finish able to distinguish a live deployment from a demonstration or plan. They should trace what a workflow can read and change, then decide what authority to permit or restrict. They should be able to test service-safe containment and recovery, and identify consequential supplier and jurisdictional dependencies. Finally, they should choose three or four priorities to explain to the chief executive officer (CEO) or board. The final decision should name what is known, what remains uncertain, who owns the service and the risk, and what evidence would change the recommendation.

<!--
P1-P7: Author framing and synthesis of the six-chapter argument; no new empirical claim. The service-visibility tension is an analytic argument, not a measured incident cause.
P4: Claims about deployment-stage differences and AI attribution are bounded by Chapters 1-2 and their current source maps/claim-ledger dispositions.
P5-P6: Reading-order description and composite-use boundary, aligned to outline-v3.md and the four author-supplied composites.
P7: Reader promise, aligned to outline-v3.md; no new operator outcome asserted.
-->