# Draft v2 source map

**Purpose:** Internal claim-to-source map for the active introduction and six chapter files in `draft-v2/`. The assembled `manuscript.md` reproduces the reader-facing text in reading order and omits internal HTML audit comments. Paragraph numbers count prose paragraphs after headings and exclude HTML audit comments. Sentence numbering follows punctuation in the current draft. Exact source passages, evidence classes and limitations are maintained in `research/claim-ledger.md`; this map preserves the manuscript anchors and direct primary links. The prose does not carry inline citations or a reader-facing Sources section.

## Introduction

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P4.S2 | O1 / OP-1; O9 / OP-3; O13 / OP-5; O18 / OP-8 | Links in Chapter 1 above | Synthesis only: these examples represent different reported stages and outcomes, not comparative performance, sector prevalence or security effectiveness. |
| P4.S3 | AI-1; O4, O6, O23 | Links in Chapter 2 below | The readable named incident sources do not establish AI use; this is not proof of non-use. |
| P1-P3, P4.S1/S4-S7, P5-P7 | Author framing; outline-v3 reader promise and narrative arc | No new source claim | Service-visibility tension is an analytic argument, not a measured incident cause. Reading path, example boundaries and reader promise add no new operator outcome. |

## Chapter 1 — What Is Actually Deployed?

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S1–S3; P2.S4–S7 | O1 / OP-1 | [Deutsche Telekom RAN Guardian/MINDR announcement](https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/2/mindr-ai-agents-in-telekom-network) | Bounded company-reported production use, first-month action count and event-management-time claim. Missing event denominator, error/override/rollback and service-quality method. |
| P4.S2 | O1 / OP-1; O9 / OP-3 | Same DT source; [One NZ Network Concierge](https://media.one.nz/networkconcierge) | Contrasts remediation with data gathering, summary and recommendation; no comparative performance inference. |
| P7.S2–S3 | O9 / OP-3; O18 / OP-8 | One NZ source; [SK Telecom AI-RAN recommender](https://news.sktelecom.com/208077) | One NZ recommendation workflow is distinct from network-state control; SKT source reports commercial-network validation while real-time application remained future work. |
| P9.S1–S3; P10.S3; P11.S1–S3 | O9 / OP-3 | One NZ source | Operator-reported analysis-time result and separate generator-placement workflow; baseline, sample, quality, error/override and service outcome are not reported. |
| P12.S2–S6 | O13 / OP-5 | [Orange France MAIA/Sharlie release](https://www.orange.com/en/press-release/orange-france-launches-two-new-artificial-intelligence-services-to-enhance-customer-relations-444308) | MAIA reach and conversation volume are operator-reported adoption/volume, not measured quality, productivity, security or ROI; Sharlie capacity is prospective. |
| P13.S2–S3 | O18 / OP-8 | SK Telecom source | Operator/vendor-reported validation on a commercial network; no cell denominator, KPI lift or scale claim. |
| P14.S1–S5 | O1 / OP-1; O9 / OP-3; O13 / OP-5; O18 / OP-8 | Links above | Synthesis of stage and evidence distinctions, not comparative operator performance. |

## Chapter 2 — Telecom Threats Without the AI Hype

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S1–S3; P2.S1–S5 | O4 / AI-1 | [Singapore CSA Operation CYBER GUARDIAN disclosure](https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector/) | Four major operators targeted; operation over eleven months; more than 100 defenders. The source does not attribute the activity to AI. Duration/defender count are response scale, not effectiveness. The source was directly reviewed in the earlier audit; browser recheck returned CloudFront 403. |
| P4.S2–S5; P4.S7; P5.S1–S5 | O23 / AI-1 | [FBI/CISA original CISA statement URL](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-peoples-republic-china-prc-targeting-commercial-telecommunications); [official FBI counterpart](https://www.fbi.gov/news/press-releases/joint-statement-from-fbi-and-cisa-on-the-peoples-republic-of-china-targeting-of-commercial-telecommunications-infrastructure) | Compromised telecom networks and disclosed data access; no AI attribution. CISA URL now returns Page Not Found; FBI page was Cloudflare-blocked in browser. Exact passage remains from prior direct review and is recorded in the claim ledger. |
| P4.S6–S7; P5.S1–S5 | O6 / AI-1 | [FBI/CISA October 2024 statement](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-prc-activity-targeting-telecommunications) | U.S. government investigation into unauthorized access and response support; no public AI attribution. Full page body was directly read in this pass. |
| P6.S2; P7.S2 | O20 / EN-1 / AI-EN20 | [ENISA 2024 OSINT overview PDF](https://www.enisa.europa.eu/sites/default/files/2025-03/5-ENISA_2024%20Telco%20threat%20landscape_March%202025.pdf) | 30-incident OSINT collection; not a census or cyberattack rate. Geography discrepancy is unresolved and omitted. |
| P6.S3–S4; P7.S3–S4 | O21 / EN-2 / AI-EN21 | [ENISA 2024 authority-report summary](https://www.enisa.europa.eu/sites/default/files/2025-07/ENISA_Telecom_Security_Incidents_2024_en_1.pdf) | 188 authority-submitted significant-incident reports, including non-malicious causes; distinct scope from OSINT collection. Geography discrepancy is unresolved and omitted. Do not compare as a rate or add as a cyberattack total. |
| P3; P6.S5–S6; P7.S1, S5–S6; P8–P19 | Author analysis/recommendation | No additional source claim | Definitions, evidentiary ladder, local questions and decision rule. They do not assert AI use in a named telecom incident or add incident measurements. |

## Chapter 3 — Follow Authority to the Network Target

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S2–S4; P2.S1–S4 | T20 | [IEEE paper DOI](https://doi.org/10.1109/OJCOMS.2024.3364840); [author PDF](https://faculty.csie.ntust.edu.tw/~smcheng/papers/J39_2402_Security%20Threats%20to%20xApps%20Access%20Control%20and%20E2%20Interface%20in%20O-RAN.pdf) | Peer-reviewed experimental O-RAN H-Release study; missing xApp access permissions and three lab attacks through APIs/E2, with service disruption in the testbed. Not a carrier production deployment or an LLM-agent test. Authors disclose Trend Micro and Taiwan NSTC support. |
| P6.S1–S4 | T19 | [AgentDojo, NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf) | Peer-reviewed benchmark demonstrating indirect prompt-injection mechanisms in simulated tool environments. No telecom systems, operator incident or network-control frequency/effectiveness estimate. Tool-count figures conflict in the paper and are not quoted. |
| P9.S1–S3 | T2 | [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Voluntary architecture publication; the source frames Zero Trust around users, assets and resources rather than static network perimeters. Not a telecom rule. Identity-governance distinction and application to target mapping are author analysis. |
| P14.S1–S2 | O8 | [CISA and international partners, Careful Adoption of Agentic AI Services](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai) | Cross-sector multi-agency guidance recommends low-risk/non-sensitive starts and avoiding broad or unrestricted access to sensitive data and critical systems. Not a telco-specific control standard. |
| P3–P5, P7–P8, P9.S4–S7, P10–P13, P15; authority-map table | Author analysis/recommendation | No additional source claim | Workflow definitions, distinction among identity/data/tool/target/service, local mapping aid and action-level categories. No operator-wide path, deployment, incident or test result is asserted. |

## Chapter 4 — Prove Safe Authority and Service-Safe Response

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P10 | T12 | [NIST, Lessons Learned from the Consortium: Tool Use in Agent Systems](https://www.nist.gov/news-events/news/2025/08/lessons-learned-consortium-tool-use-agent-systems) | NIST reports an expert workshop synthesis (~140 experts) proposing multiple tool-use taxonomy dimensions, including functionality/action, access patterns, risk/reversibility, monitoring and autonomy. Expert discussion, not a consensus standard or production test. |
| P11.S2 | T19 | [AgentDojo, NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf) | Peer-reviewed benchmark showing indirect prompt-injection mechanisms in simulated tool environments. No telecom systems, operator incident or production control-effectiveness estimate; conflicting tool counts omitted. |
| P11.S3 | T20 | [IEEE paper DOI](https://doi.org/10.1109/OJCOMS.2024.3364840); [author PDF](https://faculty.csie.ntust.edu.tw/~smcheng/papers/J39_2402_Security%20Threats%20to%20xApps%20Access%20Control%20and%20E2%20Interface%20in%20O-RAN.pdf) | Peer-reviewed experimental O-RAN H-Release study; access-control/API/E2 weaknesses and lab attacks. Not a carrier production deployment or an LLM-agent test; authors disclose Trend Micro and Taiwan NSTC support. |
| P14 | Author-supplied composite | `research/chapter-04.md` (historical composite record) | NOC-assistant situation is illustrative only; neighboring-domain data and reduced NOC visibility are exercise prompts, not empirical evidence or a reported operator test. |
| P1-P9, P12-P13, P15-P23 | Author analysis/recommendation | No external source claim | Locally scoped testing, containment, service-owner role, restoration, fallback, change-trigger and evidence-record guidance. No operator test, deadline or outcome is asserted. |

## Chapter 5 — Obligations, Suppliers and Exit Conditions

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S1-S2; P15.S2-S3; P25 | Author-supplied composite | `research/chapter-04.md` (historical composite record) | A routine update enables a topology-reading/action-proposal feature. Direct execution, runtime identity, target authority and independent disablement are not established. Illustrative only. |
| P4.S2; Table 1 (NIS2 row) | T8 | [EU NIS2 Directive 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng) | Directive scope includes public electronic communications network/service providers subject to its criteria; member-state implementation and entity/service status remain essential. Official text was directly re-read in this pass. |
| P4.S3-S4; Table 1 (GDPR row) | T9 | [GDPR 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | Articles 30 and 32 support processing records and risk-appropriate security where GDPR territorial and material scope is met; not an unqualified full-visibility or universal prompt-retention claim. Source text is documented in the research map. |
| P5; Table 1 (AI Act row) | T10 | [EU AI Act 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) | Phased and role/purpose dependent. The high-risk category for critical digital infrastructure is tied to intended safety-component use; not every AI system at a telecom operator is automatically high-risk. Primary text re-read in this pass. |
| P6; Table 1 (UK telecom security rules row) | T22 / LAW-1 | [UK Electronic Communications (Security Measures) Regulations 2022](https://www.legislation.gov.uk/uksi/2022/933/contents); [official XML](https://www.legislation.gov.uk/uksi/2022/933/data.xml) | Binding, proportionate duties for in-scope public network/service providers; micro-entity exemption. The consolidated page returned an empty body in the current browser; the statutory passage relies on the earlier direct official XML review recorded in LAW-1. Applicability remains provider-specific. |
| P7; Table 1 (UK telecom security rules row) | T22 / LAW-2 | [Telecommunications Security Code of Practice v1.1 page](https://www.gov.uk/government/publications/revised-telecommunications-security-code-of-practice-2026-version-11); [official Code v1.1 PDF](https://assets.publishing.service.gov.uk/media/6a4fac891228eb26a4cab6de/Web_Accessible_-_COP.pdf) | Official guidance issued 14 July 2026; detailed measures target Tier 1/2 providers, Tier 3 are not expected to follow those measures, and the Code has relevant legal effects without being the Regulations or the only compliance route. GOV.UK page and PDF were directly read. |
| P8; Table 1 (CIRCIA row) | T6 / LAW-3 | [CISA CIRCIA status page](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia) | Directly read 16 Nov 2026: CISA says rulemaking continues and mandatory CIRCIA reporting begins only when the final rule takes effect; voluntary reporting is encouraged meanwhile. Not a statement about other reporting duties. |
| P2-P3, P9-P14, P15.S1/S4-S5, P16-P24, P26; Table 2 | Author analysis/recommendation | No external source claim | Jurisdiction map, supplier dependency questions, contract and exit conditions, bounded-use gate and service-continuity advice. No specific operator practice, negotiated contract, cost, test or exit result is asserted. |

## Chapter 6: The Next 12 Months: A Defensible Operator Agenda

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1-P43; Table 1; four board-paper prompts | Author analysis/synthesis; outline-v3 §6 and Chapters 1-5 | No new external source claim; earlier factual claims remain mapped in their chapter sections above | Candidate areas and governance are author recommendations, not a universal sector ranking or observed operator programme. The capacity-limited worked choice is explicitly hypothetical and uses only the existing NOC-assistant and supplier-diagnostic composites. No cost, budget, ROI, staffing or deployment result is asserted. |
| P39 | AI-1; Chapter 2 evidence boundary | `research/claim-ledger.md` §8 and Chapter 2 map above | Treat threat reporting as a reason to compare local exposure; do not infer AI use in a telecom incident or a universal response time. |
| P38 | Chapter 5 legal-scope map (T6, T8, T9, T10, T22) | Primary links are listed in the Chapter 5 section above | Reassessment trigger only; does not add a legal interpretation or claim that a particular change applies to every operator. |

## Update rule

Add each chapter after drafting and ledger review. Where a sentence is author analysis rather than sourced fact, mark it as such; where a claim is omitted or qualified, keep the exact reason visible. When whole-book edits alter paragraph anchors, update this map in the same commit as the manuscript change.
