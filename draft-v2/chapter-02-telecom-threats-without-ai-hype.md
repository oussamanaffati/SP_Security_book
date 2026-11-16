# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort to counter intrusion activity against the telecommunications sector. It said all four major operators had been targeted. The operation had spanned more than eleven months and involved over 100 cyber defenders.

That is a serious account of coordinated threat response. The duration and defender count describe the operation’s scale, not how many threats were stopped or what service impact was avoided. The report does not attribute the activity to AI, nor establish that AI was not used. Those are separate claims. It tells us about targeting and the defensive operation; we should not make it carry a conclusion about the attackers’ tools.

This distinction is easy to lose when a threat briefing starts with a technology label. “AI-enabled attack” sounds like a separate class of event, perhaps one that demands a separate response. The label can hide questions that matter to an operator. Which service or system was reached? What identity or access path was involved? What did the intruder do? What information or control was exposed? What could the operator see and safely change during the investigation?

A United States disclosure gives the threat picture more detail. In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported a compromise of multiple telecommunications companies’ networks. They attributed the activity to actors affiliated with the People’s Republic of China (PRC). The agencies said the access enabled theft of customer call-record data and access to private communications of a limited number of individuals, primarily people involved in government or political activity. They also reported copying certain information subject to United States law-enforcement requests. An earlier October statement from the FBI and CISA confirmed an investigation into unauthorized access to commercial telecom infrastructure and described assistance to affected companies and potential victims. Neither statement attributes the activity to AI.

The disclosed access matters whether or not AI was involved. Nor does the disclosure establish every detail an operator would want for a post-incident review. A public statement is not a forensic image, a complete intrusion timeline or a measure of how long an adversary remained undetected. It is evidence of what the issuing agencies chose to state at that time. Keep both halves of that sentence: the disclosed access matters, and the undisclosed details remain unknown.

## Count the right thing

Even the word *incident* can conceal different evidence. The European Union Agency for Cybersecurity (ENISA) counted 30 cybersecurity incidents in its 2024 open-source intelligence (OSINT) overview. A separate ENISA annual summary contained 188 significant-incident reports submitted by national authorities. Those reports include service outages and system failures as well as malicious actions, human error and natural phenomena. The two figures come from different collection systems and answer different questions. They cannot be added into a single incident count or compared as rates.

That distinction matters in an executive room. The OSINT overview can show that publicly reported cyber activity exists; it is not a census of every telecom intrusion. The authority-submitted dataset describes significant continuity-impact events under a reporting framework; it is not a catalogue of hostile campaigns. The report’s own Member State total is inconsistent between sections, so there is no reason to repeat that disputed number in a board paper. None of these limits erases the incidents. They tell us what conclusions the data can carry.

Now ask what an AI label adds. A threat actor may use an AI service during a campaign without the service being involved in a specific telecom intrusion. A model may assist with a task without causing access, persistence or impact. A report may describe a system as “AI-enabled” without showing whether AI changed the outcome. These are different claims, and they need different evidence.

A simple proof ladder can keep the claims separate. First, is AI mentioned at all? If not, the incident account is silent; silence is neither proof of use nor proof of non-use. Second, is there evidence that a named actor used an AI tool somewhere in a broader campaign? That establishes a reported tool-use observation, not its role in a particular operator incident. Third, can investigators connect the tool to a specific action in the intrusion, using evidence from that event rather than a general capability claim? Finally, what did that use change: the task performed, the time or scale, the access obtained, or the operational consequence? A report that reaches one rung does not automatically reach the next.

This is not a forensic standard or a new threat taxonomy. It is a way to stop a weak inference from becoming a budget decision. The test is not whether an attacker could use AI. The test is what the source establishes about this actor, this operation and this target, and what the operator needs to do whether or not the label is true.

## Prepare for the path, not the headline

For a service provider, the practical work begins with the systems and relationships that can turn access into service impact. Which management, identity, supplier or remote-support paths can reach sensitive network functions? Which customer, signaling, location or operational data sets would matter if read or altered? Where can responders obtain authoritative state while an investigation is under way? Which changes can be made without destroying evidence or creating a second outage? These are local questions. A public incident disclosure rarely answers them for your estate.

That does not mean AI is irrelevant to the threat model. It means the AI question should be attached to a concrete step. Ask whether the evidence connects an AI tool to a specific step in the incident, or merely records that a tool was used somewhere in the broader activity. If an operator-side workflow called an external model or agent, could your logs connect the principal and input to the destination and resulting action? Then ask which detection or response decision would change. If none would, the AI label may be descriptive rather than operationally useful.

The inverse is also important. Do not wait for proof of AI use before fixing a known exposure. A credential that can reach a management interface, an unobserved supplier path or an internet-facing system with a supported fix is relevant on its own. Attribution can improve understanding, but uncertainty about an attacker’s tools does not remove a defender’s responsibility for the path and service at risk.

When the next briefing calls an event “AI-enabled,” ask four questions before changing the risk rating:

- What happened to the telecom target, and which source establishes it?
- What evidence connects AI to this specific operation, rather than to the actor or campaign in general?
- Which step or consequence did AI demonstrably change?
- What exposure or response action matters even if the AI attribution is later withdrawn?

If the first answer is clear and the second is not, brief the incident as a telecom intrusion and state the attribution gap. That is not minimizing the threat. It is a more defensible way to prepare for it.

<!-- Non-reader-facing source/claim map. Exact source passages, links, evidence classes and limits are in research/claim-ledger.md and research/research-map.md.
P1.S1-S3, P2.S1-S3: O4 / AI-1 (Singapore CSA disclosure only: all four major operators targeted; operation spanned more than eleven months and involved over 100 defenders; the account does not mention AI. The separate IMDA advisory remains unresolved and is not used here).
P4.S2-S5: O23 / AI-1 (Nov 2024 compromise and disclosed data access). P4.S6: O6 / AI-1 (Oct 2024 investigation and response support). P4.S7: neither statement attributes AI. P5.S1-S5: public-disclosure scope limits; analysis of O6/O23, not additional incident findings.
P6.S2, P7.S2: O20 / EN-1 / AI-EN20 (separate 30-incident OSINT dataset). P6.S3-S4, P7.S3-S4: O21 / EN-2 / AI-EN21 (188 authority-submitted dataset, incident types and unreconciled Member State count). P6.S5-S6, P7.S1/S5-S6: author comparison limits; not comparable rates or a cyberattack total.
P3; P8-P19: author analysis and recommended evidentiary discipline; no telecom attack is attributed to AI and no additional measured incident outcome is asserted.
-->