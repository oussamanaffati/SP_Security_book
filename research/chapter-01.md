# Chapter 1 research notes — 13 November 2026

## Search window
This cycle treated “recent” as the previous 12 months (13 November 2025–13 November 2026), consistent with the book workflow’s recency rule and the requested 2025–2026 period. The search focused on primary material from cyber authorities and regulators, then checked the source pages/document text where retrieval allowed.

## Sources used

1. **Singapore CSA/IMDA, Operation CYBER GUARDIAN (9 February 2026).** Official disclosure reports a deliberate UNC3886 campaign targeting all four major Singapore telcos; a zero-day used to bypass a perimeter firewall in one instance; rootkits used for persistence/evasion in another; and a coordinated response lasting over eleven months with 100+ defenders. It says the actor reached parts of telco systems, including limited access to critical systems in one case, but authorities had found no evidence at that point of customer-record exfiltration or service disruption. The chapter explicitly says this incident is not evidence of AI use. Source: https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector/

2. **ENISA, NIS360 2026 (May 2026).** The EU agency assesses telecoms as among the most mature and critical NIS sectors. It also describes structural challenges including legacy constraints in vulnerability remediation, uneven risk follow-through, and the need for consistent testing of response/recovery. The chapter avoids treating sector-level findings as uniform facts about every operator. Source: https://www.enisa.europa.eu/sites/default/files/2026-05/ENISA%20NIS360%202026.pdf

3. **ASD ACSC and partner agencies, Careful Adoption of Agentic AI Services (1 May 2026).** Joint guidance identifies risks associated with agentic AI such as privilege/identity, structural and accountability issues; recommends integration with established security governance, cautious initial use, constrained access to sensitive/critical systems, and continued visibility and oversight. It is general critical-infrastructure guidance, not telecom-specific. Source: https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services

4. **European Commission, NIS2 Directive policy page.** Used for background on NIS2 applying to electronic communications providers and the framework for cybersecurity risk management and incident reporting. This is policy context, not a new 2025–26 development. Source: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive

## Research limits
- No evidence in the Singapore disclosure that the UNC3886 campaign used AI; the manuscript explicitly avoids making that claim.
- The recent sources support the operator’s criticality, operational constraints, and agentic-system risks; they do not by themselves prove that AI has already accelerated every class of external threat. The draft frames attacker acceleration as a strategic concern and cautions against overstating current evidence.
- The chapter is a first manuscript draft. It still needs operator interviews and region-specific regulatory examples before publication.

## 13 November 2026 chapter revision: current evidence and voice review

### New current evidence
5. **CISA, Known Exploited Vulnerabilities alert (10 November 2026).** CISA added CVE-2026-20320, a Cisco BroadWorks XXE vulnerability, to the KEV catalog based on evidence of active exploitation. This confirms exploitation of the vulnerability, not the details of the AI-linked campaign described by Malbear Labs. Source: https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog

6. **Cisco PSIRT, BroadWorks security advisory (first published 19 August 2026; updated 12 November 2026).** Cisco describes an unauthenticated remote file-read risk in the OCI XML parser, states fixed software is available, and notes active exploitation as of November. Source: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt

7. **Malbear Labs, “Operation Snowball” (8 November 2026).** The research team says it found an exposed operational workspace with session transcripts and other artifacts describing a largely autonomous AI-enabled campaign against an unnamed European telecom provider and hosted organizations. The campaign narrative and reported impact are the researchers’ claims, not an official attribution by CISA or Cisco. The chapter therefore explicitly separates the confirmed active exploitation of CVE-2026-20320 from Malbear Labs’ AI-campaign analysis, notes the victim is unnamed, and avoids presenting every reported outcome as independently verified. Source: https://malbearlabs.com/posts/operation-snowball-inside-an-autonomous-ai-intrusion-campaign

### Voice references checked
- **Oussama Naffati, Cisco Blog, “A Glimpse Into Cisco Mobile Infrastructure Security Developments,” 24 November 2025.** Read the full article. Observable style cues: direct opening, simple section transitions, operator context before solution detail, clear distinction between live and in-development work, and explicit limits on what the post is (not a launch or roadmap). The chapter’s edge-workload paragraph uses a verified point from this post and cites it.
  Source: https://blogs.cisco.com/security/a-glimpse-into-cisco-mobile-infrastructure-security-developments
- **Cisco Live BRKSEC-2325, “Overcoming Challenges in the New Encrypted World for Service Providers Networks” (2024).** Read the official session PDF. Its opening states the scope and exclusions plainly, then frames why SP network security matters and focuses on use cases. Used as a style/structure reference, not as evidence for this manuscript’s factual claims. Source: https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2024/pdf/BRKSEC-2325.pdf
- **Cisco Live BRKSEC-2763, “5G Security: Why & How?” (2026).** Read the official session PDF. Its opening states clearly what attendees should and should not expect, favors non-theoretical operator use cases, and frames investment around risk prioritization. Used as a style/structure reference, not as evidence for the manuscript’s factual claims. Source: https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2026/pdf/BRKSEC-2763.pdf

### Revision decisions and caveats
- Tightened the chapter body from 2,442 to 2,016 words (17.44% shorter), removed em dashes from the manuscript body, and recast transitions in a more direct, personal but senior voice.
- Added a client-reported edge-workload formulation and a supplier-delivered AI feature example; retained the operator-grounded maintenance-window, rollback and vendor-coordination constraints.
- Added the November 2026 BroadWorks/CVE-2026-20320 development as a carefully attributed example; retained the Singapore case to distinguish an official, AI-unattributed campaign from the separately reported AI-enabled case.
- Improved the bridge: Chapter 1 explains why risk changed; Chapter 2 explicitly maps where this authority enters and reaches.
- Hard self-critique: the revision is more direct and less polished-sounding, and it now has timely operator-specific urgency. The Malbear Labs story is dramatic and rests on the research group’s account of exposed materials; the public record reviewed here does not establish that every claimed consequence was independently validated. Attribution caveats must remain. More SP leader interviews would still improve the voice and regional texture.

### Manuscript inline-citation key
- [1] Singapore CSA/IMDA Operation CYBER GUARDIAN — https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector/
- [2] ENISA NIS360 2026 — https://www.enisa.europa.eu/sites/default/files/2026-05/ENISA%20NIS360%202026.pdf
- [3] ASD ACSC and partner agencies, Careful Adoption of Agentic AI Services — https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services
- [4] European Commission NIS2 policy page — https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
- [5] Cisco blog style reference — https://blogs.cisco.com/security/a-glimpse-into-cisco-mobile-infrastructure-security-developments
- [6] CISA KEV entry for CVE-2026-20320 — https://www.cisa.gov/news-events/alerts/2026/11/10/cisa-adds-six-known-exploited-vulnerabilities-catalog
- [7] Cisco PSIRT BroadWorks advisory — https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt
- [8] Malbear Labs Operation Snowball — https://malbearlabs.com/posts/operation-snowball-inside-an-autonomous-ai-intrusion-campaign
