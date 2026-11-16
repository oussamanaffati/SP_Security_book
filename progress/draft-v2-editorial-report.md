# Draft v2 editorial report

**Date:** 16 November 2026
**Status:** Six-chapter manuscript for author review. Not publication-ready.

## Deliverable and counts

- Reader-facing manuscript: [`../draft-v2/manuscript.md`](../draft-v2/manuscript.md)
- Canonical components: `draft-v2/introduction.md` and `draft-v2/chapter-01-*.md` through `chapter-06-*.md`
- Governing architecture: [`../outline-v3.md`](../outline-v3.md)

The assembled manuscript contains **10,661 word tokens**, including title, subtitle, contents, headings and tables. The prose contains **9,630 words and 666 sentences**; mean sentence length is **14.46 words**, maximum **30**, with none over 30. Counts use `re.findall(r"\b\w+(?:[-’]\w+)*\b")`; prose excludes headings, table rows and HTML comments; list items count separately; sentence boundaries use terminal punctuation and closing quotation marks. These are editorial diagnostics, not a length target.

## What changed

### Chapter 6 now makes selection explicit

Before:
> “The four rows describe areas of work, not a universal ranking or a requirement to fund four separate packages.”

After:
> “The four rows are candidate work areas, not a default package or universal ranking.”

The Chapter 6 worked choice now shows how to select three of four candidate areas under a clearly hypothetical capacity constraint. It prioritizes mapping, target-boundary testing and a service-safe containment exercise for a contemplated NOC-assistant expansion, while deferring broad supplier/exit review because the diagnostic feature is assumed not to be enabled this cycle. Feature-specific supplier checks remain release gates; the omission is delayed work with an owner, residual risk and reopening trigger, not a finding of safety. No company-specific costs, projects or outcomes are invented.

### The work displaced is a recordable trade-off, not a category

The table now asks the operator to identify the specific local work by title, work-item identifier or window. Examples of fields include “the specific planned change, test window or reliability task” and “the contract review or supplier-validation task” that would move. These are instructions for locally completed fields, not claims about any operator’s current projects.

### The board brief and ending are shorter

The board-paper prompt now has four fields: decision and ownership; evidence and scope; value, cost and displacement; fallback and reassessment. The ending no longer repeats the full owner/evidence/cost/trigger list. It asks the reader to choose three or four priorities that local consequence and capacity justify, leave unknowns visible, and distinguish management ownership from board oversight.

The trigger section now asks for one local reopening condition, review owner and possible action per priority; examples cover a reachable target path, supplier change, fallback weakness and legal change. The final opening was also changed so Chapter 6 develops the visibility/support tension as a portfolio decision rather than repeating the introduction’s opening scenario.

### Whole-book corrections

The introduction expands “artificial intelligence (AI)” and keeps the service-visibility tension explicit as an analytic argument, not a measured cause of incidents. Chapter 3 expands “application programming interface (API)” and spells out “United States” at first use. In earlier editing, chapter headings and contents links were normalized; acronym expansions and source-map anchors were corrected; the Singapore telecom operation remains attributed to the public Cyber Security Agency disclosure without an AI-causation claim. The separate IMDA advisory remains unresolved and unused.

## Review and verification

Two whole-book passes were completed: a reader/argument pass for chapter boundaries, sequence, voice and repeated material; and a final continuous read of the assembled manuscript for evidence limits, acronyms, source mapping, structure, cadence and repetition.

Two separate-context Chapter 6 critiques were performed by **GPT-6-Luna**. The first advised against a commit because the local selection rule and decision record were incomplete. After revision, the second found no High-severity defect and recommended commit. It raised two Medium concerns: the four table rows could still read like a default package, and the table/board prompt/ending repeated too many fields. It also raised Low concerns about how to name displaced work and repeated trigger language. Those points were addressed as described above. Both critiques used the same available model; they are not human or independent-model reviews. Grok was not used. No human, operator, legal-counsel or external legal review is claimed.

Mechanical checks on the final assembly found:
- all seven reader-facing components appear exactly once and internal HTML audit comments are omitted;
- all contents links match the actual headings;
- four tables have consistent columns;
- 66 source-map anchor tokens checked, with zero out-of-range paragraph/sentence references;
- no reader-facing `## Sources` section, numeric citation, TODO/TBD/FIXME marker or exact duplicate paragraph block.

## Limits and remaining publication work

The manuscript adds no new external cost, ROI, incident, deployment or operator-practice claim. It uses the current claim-ledger dispositions; it does not certify every historical repository claim. The selected priorities, costs, staffing, specific displaced work, change windows, service tolerances, supplier rights and legal applicability must be filled with each operator’s evidence. Remaining evidence limitations include unresolved source/date or methodology issues already recorded in the ledger, including Heavy Reading date relationships, ENISA geography-count differences and incomplete operator metrics. The text does not use those disputed figures to support its argument.

The earlier renderer preflight found ReportLab and pypdf but no page-rendering executable; no renderable PDF was produced or visually inspected. The user has now requested a push after commit; remote verification is pending. Local commit status will be recorded after verification.
