# Introduction

When leadership asks its chief information security officer (CISO) to pause a workflow that uses artificial intelligence (AI), the request may make sense. The network team may still depend on its data feed, supplier console or alert path to see the service. If no one checks those dependencies first, the team could lose visibility or support. But leaving the workflow running without a proven boundary creates another risk. That tension sits at the centre of this book.

Neither response is enough. Start with the workflow itself. What data does it read, which identity and connector does it use, and what can it recommend or change? Check where the target enforces permission. Then ask what the team can still see if the workflow stops, and who can restore the service.

That makes this a service-provider security problem, not just an AI problem. A decision sits inside a live service, with people, suppliers and dependencies that may still be needed when a workflow stops. A control that looks easy in a demonstration can be hard to remove from operations. And “in production” says little about what the system can change, how widely it is used or whether security improved.

The sources in this book show serious telecom targeting, but do not establish AI as the cause of the incidents discussed. The systems themselves are at different stages. Keep three distinctions in view: productivity is not security effectiveness, a threat report is not a local risk assessment, and a test supports only the path it exercised.

The argument moves from claims to decisions. Chapter 1 asks what is actually in use; Chapter 2 tests what threat reports do and do not say. Chapters 3 and 4 trace how a workflow reaches a network target, and what happens when it is stopped. Chapter 5 looks at legal and supplier conditions, including exit. Chapter 6 turns those choices into a twelve-month investment agenda.

Chapters 3 and 4 work through two illustrative operational situations. Chapter 5 looks briefly at a supplier feature. These are examples, not incident reports or test results. Any details added for the walkthroughs are marked as assumptions; operators do not all have the same systems or constraints.

Read the chapters in order to build a shared risk view; each one builds on decisions made earlier. If you are preparing for a specific decision, start with the relevant chapter, then return to Chapter 6 to choose priorities, assign ownership and decide what evidence or capacity is needed.

By the end, a telecom CISO should be able to tell a live deployment from a demonstration or plan, trace what a workflow can read and change, plan a safe stop and recovery, assess supplier dependencies, and choose three or four priorities for the chief executive officer (CEO) or board. For each, the CISO should be able to say what is known, what is not, who owns the service and risk, and what new evidence would change the decision.

<!--
P1-P8: Author framing and synthesis of the six-chapter argument; no new empirical claim. The service-visibility tension is an analytic argument, not a measured incident cause.
P4: Claims about deployment-stage differences and AI attribution are bounded by Chapters 1-2 and their current source maps/claim-ledger dispositions.
P5-P7: Chapter order, two fully developed illustrative situations and shorter supplier example, aligned to outline-v3.md; no additional operator practice asserted.
P8: Reader promise, aligned to outline-v3.md; no new outcome asserted.
-->