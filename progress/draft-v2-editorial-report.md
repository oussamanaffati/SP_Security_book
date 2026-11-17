# Draft v2 editorial report

**Date:** 17 November 2026
**Status:** Expanded manuscript for author review; not publication-ready.
**Active file:** [`../draft-v2/manuscript.md`](../draft-v2/manuscript.md)
**Canonical sources:** `draft-v2/introduction.md` and the six `draft-v2/chapter-*.md` files. `outline-v3.md` remains the governing structure.

## Counts

- **Prose:** 9,025 words, excluding headings, table rows and hidden HTML comments.
- **Visible manuscript:** 9,559 word tokens, including title, subtitle, contents, headings and tables.
- **Per-component prose:** Introduction 489; Chapter 1 877; Chapter 2 808; Chapter 3 1,458; Chapter 4 1,824; Chapter 5 1,536; Chapter 6 2,033.
- **Chapter 6 visible tokens:** 2,065.

Counts use `re.findall(r"\b\w+(?:[-’]\w+)*\b")`; list items count separately. Prose excludes headings, table rows and HTML comments. The visible count is about 1,895 tokens above the user-provided approximate 7,664-word baseline. That is a same-scope comparison including headings and tables; no page target is asserted.

## Substantive changes

### Chapters 3–4: one operational story, from routine work to recovery

Chapter 3 explains why the fictional NOC assistant is useful, what alarm, ticket and neighboring-domain data it receives, which connectors it uses, and how a shared identity reaches farther than triage requires. A stale ticket note leads a reviewer to submit an alarm-routing request; the target accepts and queues it, while completion remains unknown. The chapter distinguishes a proposal, submission, target acceptance and completed state change, and explains what runtime, connector and target logs can and cannot establish.

Chapter 4 continues that same scenario. It covers detection and correlation, containment choices and their service costs, why an independent alarm view changes whether the broad identity can safely be revoked, and what the NOC can do in degraded mode. It distinguishes preventing new authenticated requests, restricting existing sessions, cancelling or accounting for accepted/queued work, and verifying target state. If the target cannot cancel accepted work, the team blocks further writes where it can, tracks the operation, and treats it as capable of completing until evidence shows otherwise. Restoration starts with the independent service view and returns only the smallest tested capability.

The scenario is fictional and educational. Its identity, connector scopes, target behavior, event records, queue state and alarm-view assumptions are not an operator incident, observed test or measured outcome.

### Chapter 6: a defensible resource choice

The chapter chooses among independent NOC alarm visibility, a supported live-core patch, separation of the shared edge/core identity and review of a supplier diagnostic feature. It states hypothetical capacity and service constraints, separates work that can start in parallel from work competing for a single assumed production window, and identifies the residual exposure while identity separation waits. The interim assistant write block is conditional on verified target or gateway enforcement and absence of a bypass. The chapter explains why the patch gets the window under those assumptions, why identity migration is the plausible rejected alternative, and what new evidence would reverse the order. No budget, ROI, probability, successful result or operator programme is invented. The closing recommendation is an example, not a universal NOC project prescription.

### Chapters 1–2 and voice

Chapter 1 restores the reasoning from deployment claims to approval, measurement and investment decisions while keeping activity, productivity, service quality and security effectiveness separate. The introduction and Chapter 1 were adjusted toward the user-provided style: concrete subjects, plain verbs, conversational transitions, and a clear line between what a source reports and what it does not establish.

Chapter 2 distinguishes the two ENISA datasets and uses the FBI-CISA disclosure to derive conditional local priorities—identity attribution, access scope and event coverage—without guessing at the intrusion path or attributing it to AI. The Singapore disclosure’s reported technical-data exfiltration and its stated limits remain together.

## Whole-manuscript review and verification

One complete read of the regenerated manuscript checked continuity, transitions, repetition, voice and technical consistency. The introduction now describes one NOC scenario across Chapters 3–4 and a shorter supplier-feature example in Chapter 5. The scenario’s setup, evidence limits and recovery path remain coherent. Credential revocation is not treated as session termination or queue cancellation. The conclusion asks each reader to choose their own first consequential workflow; the NOC is an example.

No new external source was added or re-fetched; current claim-ledger dispositions were retained. Source-map paragraph anchors and Chapter 3’s internal source map were updated. The editorial check found no remaining “supplied situation” / “these added details” wording or “at the start of Chapter 4” meta-reference. No successive reviewer rounds were launched.

Mechanical checks passed: seven canonical components appear exactly once, table of contents links match headings, source-map anchors are in range, both manuscript tables have consistent columns, README links resolve, and `git diff --check` passes. The reader-facing assembly contains no hidden audit comments, numeric citations, TODO/TBD/FIXME placeholders, Sources heading, reader-facing “composite” terminology or the removed ENISA member-count digression.

## Self-critique and limitations

The strongest improvement is that the manuscript now demonstrates decisions and trade-offs instead of only naming them. The style sample makes the introduction and opening chapter more natural without flattening the technical distinctions. The NOC scenario and the Chapter 6 capacity assumptions remain dense in places; that density carries information the reader needs to reason about authority, service impact and sequencing. It should not be removed merely to make the prose shorter. This is an internal editorial read, not independent, human, operator or legal validation.

No PDF was generated: Python ReportLab is available, but no page renderer was available for visual inspection. No layout or page count is claimed. Operator-specific service scope, legal applicability, staffing, supplier rights, costs and fallback readiness still require local verification.

## Git status

The manuscript revision `22043db85f492250ec89acd9c79898c2c2dea3e3` was pushed to `main`. A fresh live-ref read and fetch confirmed `origin/main` at that commit; every changed-file blob matched local, and ahead/behind was 0/0. The status, editorial report and work-log publication record are in a separate documentation-only follow-up commit.