# Introduction

When a chief information security officer (CISO) is asked to pause a workflow that uses artificial intelligence (AI), the request often makes sense on paper. The operations team may still need the data feed, supplier console or alert path to understand what is happening to the service. Stopping the workflow can remove that visibility. Leaving it running without a clear boundary creates a different risk.

This is the practical tension we see with service providers today. Once a workflow becomes part of live operations, it is no longer sitting beside the service. It is part of how the service is run.

The board and the chief technology officer (CTO) do not need another discussion about agents. They need to know what a workflow can read and change, which identity and connector it uses, which system enforces that authority, and what remains visible if the workflow is stopped. They also need to know who owns the decision when security and service continuity pull in opposite directions.

The public record shows serious targeting of telecom networks. It does not show that AI caused the incidents discussed here. Operators are deploying systems at very different stages. Productivity gains are not the same as security effectiveness. A threat report is not a local exposure assessment. A test covers only the path and conditions that were exercised.

This book follows the decisions a telecom CISO or CTO has to make. Chapter 1 asks what is actually deployed. Chapter 2 looks at the threat picture without adding AI where the evidence does not support it. Chapters 3 and 4 follow authority from identity and data to the network target, then examine whether the operator can contain and recover without losing the service view. Chapter 5 covers the legal and supplier conditions that limit the options. Chapter 6 turns those decisions into a small set of priorities that management can defend over the next twelve months.

Chapters 3 and 4 follow one fictional NOC assistant from routine use through detection, containment and restoration. Chapter 5 uses a shorter supplier-feature example. These are educational scenarios, not incident reports, observed tests or measured results. Their assumptions are stated where each begins.

Read the chapters in order to build a shared view of the risk; each one builds on decisions made earlier. If you are preparing for a specific decision, start with the relevant chapter, then return to Chapter 6 to choose priorities, assign ownership and decide what evidence or capacity is needed.

By the end, a telecom CISO should be able to tell a live deployment from a demonstration or plan, trace what a workflow can read and change, plan a safe stop and recovery, assess supplier dependencies, and choose three or four priorities for the CEO or board. For each, the CISO should be able to explain what is known, what is not, who owns the service and risk, and what new evidence would change the decision.

<!--
P1-P8: Author framing and synthesis of the six-chapter argument; no new empirical claim. The service-visibility tension is an analytic argument, not a measured incident cause.
P4: Claims about deployment-stage differences and AI attribution are bounded by Chapters 1-2 and their current source maps/claim-ledger dispositions.
P5-P7: Chapter order, one fictional NOC scenario followed across Chapters 3-4 and shorter supplier example, aligned to outline-v3.md; no additional operator practice asserted.
P8: Reader promise, aligned to outline-v3.md; no new outcome asserted.
-->