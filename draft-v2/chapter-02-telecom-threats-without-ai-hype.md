# Chapter 2: Telecom Threats Without the AI Hype

In February 2026, Singapore’s Cyber Security Agency described Operation CYBER GUARDIAN, a national effort against intrusion activity targeting the telecommunications sector. It said all four major operators had been targeted. The operation lasted more than eleven months and involved over 100 cyber defenders.

Those figures show the scale of the defensive effort, not how many attacks it stopped or outages it prevented. The account documents serious telecom targeting and a large response, but does not attribute the operation to AI.

In November 2024, the Federal Bureau of Investigation (FBI) and Cybersecurity and Infrastructure Security Agency (CISA) reported that actors affiliated with the People’s Republic of China (PRC) had compromised multiple telecommunications companies’ networks. The agencies said the intruders stole customer call-record data, accessed private communications belonging to a limited number of people—mainly those involved in government or politics—and copied some information subject to United States law-enforcement requests. An October FBI-CISA statement had already confirmed unauthorized access to commercial telecom infrastructure and assistance for affected companies and potential victims. The public disclosures do not report AI use in this activity. They also leave the forensic timeline and duration of undetected access unclear.

## Count the right thing

The European Union Agency for Cybersecurity (ENISA) counted 30 cybersecurity incidents in an open-source intelligence (OSINT) overview. A separate annual summary contained 188 significant-incident reports submitted by national authorities. That set also includes service outages, system failures, human error and natural phenomena. The collections draw on different inputs and definitions; they are not a combined total or comparable rates.

The OSINT overview shows publicly reported cyber activity, not every telecom intrusion. The authority-submitted reports capture continuity-impact events under a reporting framework, not just hostile campaigns. They answer different questions. Keep that distinction in executive briefings; neither figure estimates an operator’s local exposure.

## Put the threat report to work

An AI label matters only when evidence connects AI to this incident. Then ask what it changed: the task, scale, timing, access or consequence. A tool used elsewhere in a campaign is not enough.

That uncertainty does not stop the operator from acting. Map the management, identity, supplier and remote-support paths into sensitive network functions. Identify the customer, signaling, location and operational records that would matter if read or altered. Make sure responders can see authoritative service state during an investigation, and know which changes preserve evidence without causing a second outage. Public disclosures cannot answer those local questions for you.

Would knowing AI was involved change a decision? Where an external model or agent is called, can logs connect the requesting identity and input to the destination, tool call and result? If that information would not change detection or response, the label may describe the event without helping the operator act.

Do not wait for proof of AI use before correcting a known exposure. A credential that reaches a management interface, an unobserved supplier path or an exposed system with a supported fix matters on its own. Attribution can refine the investigation; it does not remove the operator’s responsibility for a path already at risk.

At the next briefing, ask what happened to the telecom target, what ties AI to the operation, and whether that attribution changes the response. If the intrusion is clear but the AI link is not, report the intrusion and say that the link remains unconfirmed.

Threat reports set the context. The operator’s next question is local: which identity and target can turn access into service impact?

<!-- Non-reader-facing source/claim map. Exact source passages, links, evidence classes and limits are in research/claim-ledger.md and research/research-map.md.
P1-P2: O4 / AI-1 (Singapore CSA disclosure: four major operators targeted; operation spanned more than eleven months and involved over 100 defenders; published account does not attribute AI). The separate IMDA advisory remains unresolved and is not used.
P3: O23 / AI-1 (Nov 2024 compromise and disclosed data access); O6 / AI-1 (Oct 2024 investigation and response support). Public-disclosure limits do not establish a forensic timeline or AI role.
P4-P5: O20 / EN-1 / AI-EN20 (30-incident OSINT dataset); O21 / EN-2 / AI-EN21 (188 authority-submitted significant-incident dataset and event categories). The datasets have different methods and are not rates or a unified attack count. The Member State count discrepancy is retained in research notes only; it is not used in this chapter.
All remaining content is author analysis and preparation advice; no telecom event is attributed to AI beyond what sources establish.
-->