# Introduction

When leadership asks its chief information security officer (CISO) to pause a workflow that uses artificial intelligence (AI), the request may be sensible. The network team may still need the same data feed, supplier console or alert path to see what is happening to a service. Leaving the workflow in place without a proven boundary creates another risk. A pause can reduce one exposure and remove visibility or support needed to operate the service. That is the practical tension at the centre of this book.

The answer is not to ban every model or to trust a supplier’s assurance. It is to understand the whole workflow. What data can it read? Which identity and connector does it use? What can it recommend, draft or change? Where does the target enforce permission? What remains visible when the workflow is stopped, and who can restore the service?

That is a service-provider security question, not only an AI question. An operator’s decision sits inside a service with dependencies, operating teams, suppliers, jurisdictions and supported change paths. A control that looks simple in a product demonstration may be difficult to remove from a live operating process. A production label does not tell a CISO what a system can change, how widely it is used, or whether it has improved security.

This book does not claim that autonomous agents are the leading cause of telecom incidents. The sources reviewed here report different deployment stages and outcomes. They establish serious telecom targeting, but do not establish AI use in the incidents discussed. Those limits matter: productivity is not proof of security effectiveness, a threat report is not proof of local exposure, and a test supports only the path and conditions it exercised.

The chapters follow the decisions a CISO or chief technology officer (CTO) needs to make. Chapter 1 separates deployment stage, authority and outcome. Chapter 2 examines telecom intrusion evidence without assuming an AI cause. Chapter 3 follows identity, data, tools and permission to the network target. Chapter 4 asks what has been tested and whether the operator can contain and recover without losing the service view. Chapter 5 connects legal duties to supplier dependencies and exit. Chapter 6 turns those decisions into a small investment agenda for the next twelve months.

Chapters 3 and 4 work through two illustrative operational situations in detail. Each is introduced where it matters, and any added educational assumption is separated from the situation’s stated facts. Chapter 5 uses a shorter supplier-feature example. These situations are not reported incidents or successful tests. They help make the choices visible without pretending that every operator has the same systems or constraints.

Read the book in order if you are building a common risk view. Each chapter uses decisions established before it. If you are preparing a particular decision, start with the relevant chapter, then return to Chapter 6 to select priorities, assign ownership, record the evidence and capacity required, and decide what would change the recommendation.

The aim is practical. A telecom CISO should finish able to distinguish a live deployment from a demonstration or plan; trace what a workflow can read and change; test service-safe containment and recovery; identify consequential supplier and jurisdiction dependencies; and select three or four priorities to explain to the chief executive officer (CEO) or board. The final decision should say what is known, what remains uncertain, who owns the service and the risk, and what evidence would change the recommendation.

<!--
P1-P8: Author framing and synthesis of the six-chapter argument; no new empirical claim. The service-visibility tension is an analytic argument, not a measured incident cause.
P4: Claims about deployment-stage differences and AI attribution are bounded by Chapters 1-2 and their current source maps/claim-ledger dispositions.
P5-P7: Chapter order, two fully developed illustrative situations and shorter supplier example, aligned to outline-v3.md; no additional operator practice asserted.
P8: Reader promise, aligned to outline-v3.md; no new outcome asserted.
-->