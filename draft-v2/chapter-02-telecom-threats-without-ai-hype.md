# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort against intrusion activity targeting the telecommunications sector. It said all four major operators had been targeted. The operation lasted more than eleven months and involved over 100 cyber defenders.

Those figures describe the scale of the defensive operation, not the number of threats stopped or service impact avoided. The published account does not attribute the activity to AI. It supports a serious assessment of telecom targeting and organized response; it does not support a claim about the attackers’ AI use.

A United States disclosure gives a different view of the threat. In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported a compromise of multiple telecommunications companies’ networks. They attributed the activity to actors affiliated with the People’s Republic of China (PRC). The agencies said the access enabled theft of customer call-record data, access to private communications of a limited number of individuals, primarily people involved in government or political activity, and copying certain information subject to United States law-enforcement requests. An October statement from the FBI and CISA had confirmed an investigation into unauthorized access to commercial telecom infrastructure and assistance to affected companies and potential victims. These disclosures do not establish AI use in the named activity. Their public scope also does not provide a complete forensic timeline or show how long access went undetected.

## Count the right thing

The European Union Agency for Cybersecurity (ENISA) published an open-source intelligence (OSINT) overview counting 30 cybersecurity incidents. A separate ENISA annual summary contained 188 significant-incident reports submitted by national authorities. That reporting set includes service outages and system failures as well as malicious actions, human error and natural phenomena. The two collections have different inputs and definitions. They are neither a combined count nor comparable rates.

The OSINT overview shows publicly reported cyber activity; it is not a census of all telecom intrusions. The authority-submitted reports describe continuity-impact events under a reporting framework; they are not a catalogue of hostile campaigns. The figures answer different questions. Keep that distinction when briefing executives, and do not use either number to estimate an operator’s local exposure.

## Prepare for the path, not the headline

An AI label should change the assessment only when evidence ties AI to a step that matters. Did a named actor use an AI service somewhere in a broader campaign, or did investigators connect that use to this specific telecom intrusion? Did it change the task, scale, timing, access or consequence? A report that documents general tool use does not establish that the tool caused a particular intrusion or changed its outcome.

That distinction need not delay practical work. Map the management, identity, supplier and remote-support paths that can reach sensitive network functions. Know which customer, signaling, location or operational records matter if read or altered. Make sure responders can obtain authoritative service state during an investigation, and identify which changes can preserve evidence without creating a second outage. Public disclosures rarely answer those local questions.

Attach the AI question to a concrete step in the operator’s own workflow. If an external model or agent is called, can the logs connect the requesting principal and input to the destination, tool call and resulting action? Would evidence of AI use change a detection or response decision? If not, the label may be descriptive rather than operationally useful.

Do not wait for proof of AI use before correcting a known exposure. A credential that reaches a management interface, an unobserved supplier path or an exposed system with a supported fix matters on its own. Attribution can refine the investigation; it does not remove the operator’s responsibility for a path already at risk.

When the next briefing calls an event “AI-enabled,” ask what happened to the telecom target, what evidence connects AI to this operation, what that use changed, and what action remains necessary even if the attribution is withdrawn. If the intrusion is clear but the AI link is not, brief it as a telecom intrusion and state the attribution gap.

Knowing which threats are reported still leaves the operator with a local question: which identity, connector and target can turn access into service impact? Chapter 3 follows that path.

<!-- Non-reader-facing source/claim map. Exact source passages, links, evidence classes and limits are in research/claim-ledger.md and research/research-map.md.
P1-P2: O4 / AI-1 (Singapore CSA disclosure: four major operators targeted; operation spanned more than eleven months and involved over 100 defenders; published account does not attribute AI). The separate IMDA advisory remains unresolved and is not used.
P3: O23 / AI-1 (Nov 2024 compromise and disclosed data access); O6 / AI-1 (Oct 2024 investigation and response support). Public-disclosure limits do not establish a forensic timeline or AI role.
P4-P5: O20 / EN-1 / AI-EN20 (30-incident OSINT dataset); O21 / EN-2 / AI-EN21 (188 authority-submitted significant-incident dataset and event categories). The datasets have different methods and are not rates or a unified attack count. The Member State count discrepancy is retained in research notes only; it is not used in this chapter.
All remaining content is author analysis and preparation advice; no telecom event is attributed to AI beyond what sources establish.
-->