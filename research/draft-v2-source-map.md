# Draft v2 source map

**Purpose:** Internal claim-to-source map for the active introduction and six chapter files in `draft-v2/`. The assembled `manuscript.md` reproduces the reader-facing text in reading order and omits internal HTML audit comments. Paragraph numbers count prose paragraphs after headings and exclude HTML audit comments; list items count as individual paragraphs. Exact source passages, evidence classes and limitations remain in `research/claim-ledger.md`. The prose uses no inline citation numbers or reader-facing Sources section.

## Introduction

| Draft anchor | Claim/source IDs | Support and limit |
|---|---|---|
| P1-P3 | Author framing | Service-visibility tension is an analytic argument, not a measured incident cause. No empirical claim is added. |
| P4 | AI-1; O1/O9/O13/O18; O4/O6/O23 | Deployment and incident statements are bounded by Chapters 1-2; no AI attribution is inferred beyond the sources. |
| P5-P8 | Author synthesis; outline-v3 | Chapter order, two developed illustrative situations, supplier example and reader promise. No operator outcome asserted. |

## Chapter 1 — What Is Actually Deployed?

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1-P2 | O1 / OP-1 | [Deutsche Telekom RAN Guardian/MINDR announcement](https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/2/mindr-ai-agents-in-telekom-network) | Company-reported production scope, first-month action count and event-management-time claim. No event denominator, measurement method, success/rollback rate or service-quality measure is provided. |
| P3 | O9 / OP-3 | [One NZ Network Concierge](https://media.one.nz/networkconcierge) | Operator-reported workflow and analysis-time reduction; no case count, baseline or answer-quality measure. |
| P4 | O9 / OP-3 | Same One NZ source | Separate generator-placement workflow; no network-control or service-restoration result established. |
| P5 | O13 / OP-5 | [Orange France MAIA/Sharlie release](https://www.orange.com/en/press-release/orange-france-launches-two-new-artificial-intelligence-services-to-enhance-customer-relations-444308) | MAIA deployment/reach and conversation volume are adoption/activity claims, not measured productivity, quality, security or ROI. |
| P6 | O18 / OP-8 | [SK Telecom AI-RAN recommender](https://news.sktelecom.com/208077) | Commercial-network validation; it recommends parameters and real-time application remained in development. No network-wide autonomous-control result. |
| P7-P10 | Author analysis | No additional source claim | Distinguishes deployment, activity, productivity, service quality, security effectiveness and ROI. |

## Chapter 2 — Telecom Threats Without the AI Hype

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1-P2 | O4 / AI-1 | [Singapore CSA Operation CYBER GUARDIAN disclosure](https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector/) | Four major operators targeted; operation lasted more than eleven months and involved over 100 defenders. The published account does not attribute AI. Scale measures the defensive operation, not prevented threats or avoided impact. Separate IMDA advisory remains unresolved and unused. |
| P3 | O23 and O6 / AI-1 | [FBI/CISA November statement](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-peoples-republic-china-prc-targeting-commercial-telecommunications); [official FBI counterpart](https://www.fbi.gov/news/press-releases/joint-statement-from-fbi-and-cisa-on-the-peoples-republic-of-china-targeting-of-commercial-telecommunications-infrastructure); [FBI/CISA October statement](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-prc-activity-targeting-telecommunications) | Disclosed compromise, data access and investigative support; named activity is not attributed to AI. Public statements are not a complete forensic timeline. CISA pages had retrieval limitations recorded in the ledger; exact text was previously directly reviewed. |
| P4-P5 | O20 / EN-1 / AI-EN20; O21 / EN-2 / AI-EN21 | [ENISA 2024 OSINT overview](https://www.enisa.europa.eu/sites/default/files/2025-03/5-ENISA_2024%20Telco%20threat%20landscape_March%202025.pdf); [ENISA 2024 authority-report summary](https://www.enisa.europa.eu/sites/default/files/2025-07/ENISA_Telecom_Security_Incidents_2024_en_1.pdf) | One dataset counts 30 OSINT incidents; the other 188 authority-submitted significant-incident reports, including non-malicious causes. Different collection methods/scopes; not combined or comparable as rates. Member State count discrepancy stays in research notes only and is not used in reader-facing text. |
| P6-P11 | Author analysis/recommendation | No additional source claim | AI-attribution reasoning and operator preparation. No incident is attributed to AI beyond what the sources establish. |

## Chapter 3 — Follow Authority to the Network Target

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1-P2 | T20 | [IEEE paper DOI](https://doi.org/10.1109/OJCOMS.2024.3364840); [author PDF](https://faculty.csie.ntust.edu.tw/~smcheng/papers/J39_2402_Security%20Threats%20to%20xApps%20Access%20Control%20and%20E2%20Interface%20in%20O-RAN.pdf) | Peer-reviewed experimental O-RAN H-Release study; missing xApp access permissions and lab attacks through APIs/E2, including service disruption in the testbed. Not a carrier production deployment or LLM-agent test. Authors disclose Trend Micro and Taiwan NSTC support. |
| P4-P5 | Author-supplied shared edge/core situation; `research/chapter-04.md` | No external source | Existing situation: one shared account reaches edge nodes and parts of core; remediation depends on supplier configuration and a safe maintenance window. It does not establish AI use, commands, target enforcement, identity separation or test result. Maintenance assistant, edge-only task, connector/API path and target behavior are explicitly educational assumptions. |
| P6-P12 | Author analysis/recommendation | No external source | Identity-to-target reasoning, choices and conditional recommendation; no operator path, gateway, migration or test is claimed. |
| P14 | T19 | [AgentDojo, NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf) | Peer-reviewed benchmark of indirect prompt-injection mechanisms in simulated tool environments. Not telecom, operator incident or network-control frequency/effectiveness estimate. Conflicting tool counts are not quoted. |
| P16 | T2 | [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Voluntary architecture publication, not telecom regulation. Target-mapping advice is author analysis. |
| P3, P13, P15, P17-P18 | Author analysis | No additional source claim | No universal carrier path, incident or outcome asserted. |

## Chapter 4 — Prove Safe Authority and Service-Safe Response

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P3 | Author-supplied NOC-assistant situation; `research/chapter-04.md` | No external source | The situation states alarm summaries, draft ticket updates, neighboring-domain data, supplier cases and a proposed visibility-reducing change that was not executed. It does not establish identity, connector, target, permission model or direct write access. Illustrative, not an incident or test. |
| P4 | Educational assumptions | No external source | Shared service identity, ticket/alarm connectors, identity scope, proposed alarm-routing write, whole-identity revocation and no verified independent alarm-read path are explicitly assumed, not operator facts. |
| P6-P11 | Author analysis/recommendation | No external source | Conditional response and testing advice; session, queued-work and recovery checks are recommended, not reported test results. |
| P15 | T19; T20 | [AgentDojo, NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf); [IEEE O-RAN study](https://doi.org/10.1109/OJCOMS.2024.3364840) | Each source is limited to its own simulated benchmark or experimental testbed; neither establishes carrier production effectiveness. |
| P1-P2, P5, P12-P14, P16-P21 | Author analysis/recommendation | No external source claim | No operator test, incident response or service outcome asserted. |

## Chapter 5 — Obligations, Suppliers and Exit Conditions

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1; P15; P25 | Author-supplied supplier-feature situation; `research/chapter-04.md` | No external source | Routine update enables a topology-reading/action-proposal feature. Direct execution, runtime identity, target authority and independent disablement are not established. Illustrative only. |
| P4; Table 1 (NIS2 and GDPR rows) | T8; T9 | [EU NIS2 Directive 2022/2555](https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng); [GDPR 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | NIS2 scope and national implementation/entity status matter. GDPR Articles 30/32 support records and risk-appropriate security within territorial/material scope; no universal prompt-retention claim. |
| P5; Table 1 (AI Act row) | T10 | [EU AI Act 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) | Phased and role/purpose dependent; the critical-digital-infrastructure category is tied to intended safety-component use, not all telecom AI. |
| P6; Table 1 (UK Regulations row) | T22 / LAW-1 | [UK Electronic Communications (Security Measures) Regulations 2022](https://www.legislation.gov.uk/uksi/2022/933/contents); [official XML](https://www.legislation.gov.uk/uksi/2022/933/data.xml) | Binding, proportionate duties for in-scope public providers; micro-entity exemption. Consolidated page retrieval limitation is recorded in LAW-1; statutory passage relies on earlier direct official XML review. Applicability remains provider-specific. |
| P7; Table 1 (UK Code row) | T22 / LAW-2 | [Telecommunications Security Code v1.1 page](https://www.gov.uk/government/publications/revised-telecommunications-security-code-of-practice-2026-version-11); [official PDF](https://assets.publishing.service.gov.uk/media/6a4fac891228eb26a4cab6de/Web_Accessible_-_COP.pdf) | Official guidance issued 14 July 2026; detailed measures target Tier 1/2; Tier 3 qualification and legal effect remain as recorded in LAW-2. Not the Regulations or the only compliance route. |
| P8; Table 1 (CIRCIA row) | T6 / LAW-3 | [CISA CIRCIA status page](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia) | Directly read 16 Nov 2026: final rule in progress; mandatory CIRCIA reporting starts only when effective; voluntary reporting encouraged. Not a statement about other duties. |
| Table 2 | Author analysis | No external source claim | Supplier dependency/evidence questions, not claims about specific contracts or supplier capability. |
| P2-P3, P9-P14, P16-P24, P26-P27 | Author analysis/recommendation | No additional source claim | Jurisdiction mapping, supplier dependency, exit, bounded-use, continuity and transition advice. No unverified operator practice, cost, contract or exit result asserted. |

## Chapter 6 — The Next 12 Months: A Defensible Operator Agenda

| Draft anchor | Claim/source IDs | Support and limit |
|---|---|---|
| P1-P32 | Author analysis/synthesis; outline-v3 §6 and Chapters 1-5 | No new empirical or sector-prevalence claim. Visibility/support tension is analytic, not a measured incident cause. Candidate priorities are recommendations, not a universal ranking or observed operator programme. |
| P12-P14 | Chapter 4 NOC-assistant and Chapter 5 supplier-feature situations | The three-of-four capacity decision is explicitly hypothetical. No local costs, budget, staffing, deployment or outcome is asserted; existing situation facts remain bounded as mapped above. |

## Update rule

When a chapter changes, recalculate its paragraph anchors and update this map in the same revision. Keep exact source evidence, source classes and dispositions in the claim ledger. Mark author analysis and educational assumptions so they cannot be mistaken for empirical operator claims.