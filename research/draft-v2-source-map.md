# Draft v2 source map

**Purpose:** Internal claim-to-source map for the six manuscript files in `draft-v2/`. Paragraph numbers count prose paragraphs after headings and exclude HTML audit comments. Sentence numbering follows punctuation in the current draft. Exact source passages, evidence classes and limitations are maintained in `research/claim-ledger.md`; this map preserves the manuscript anchors and direct primary links. The prose does not carry inline citations or a reader-facing Sources section.

## Chapter 1 — What Is Actually Deployed?

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S1–S3; P2.S4–S7 | O1 / OP-1 | [Deutsche Telekom RAN Guardian/MINDR announcement](https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/2/mindr-ai-agents-in-telekom-network) | Bounded company-reported production use, first-month action count and event-management-time claim. Missing event denominator, error/override/rollback and service-quality method. |
| P4.S2 | O1 / OP-1; O9 / OP-3 | Same DT source; [One NZ Network Concierge](https://media.one.nz/networkconcierge) | Contrasts remediation with data gathering, summary and recommendation; no comparative performance inference. |
| P7.S2–S3 | O9 / OP-3; O18 / OP-8 | One NZ source; [SK Telecom AI-RAN recommender](https://news.sktelecom.com/208077) | One NZ recommendation workflow is distinct from network-state control; SKT source reports commercial-network validation while real-time application remained future work. |
| P9.S1–S3; P10.S3; P11.S1–S3 | O9 / OP-3 | One NZ source | Operator-reported analysis-time result and separate generator-placement workflow; baseline, sample, quality, error/override and service outcome are not reported. |
| P12.S2–S6 | O13 / OP-5 | [Orange France MAIA/Sharlie release](https://www.orange.com/en/press-release/orange-france-launches-two-new-artificial-intelligence-services-to-enhance-customer-relations-444308) | MAIA reach and conversation volume are operator-reported adoption/volume, not measured quality, productivity, security or ROI; Sharlie capacity is prospective. |
| P13.S2–S3 | O18 / OP-8 | SK Telecom source | Operator/vendor-reported validation on a commercial network; no cell denominator, KPI lift or scale claim. |
| P14.S1–S3 | O1 / OP-1; O9 / OP-3; O13 / OP-5; O18 / OP-8 | Links above | Synthesis of stage and evidence distinctions, not comparative operator performance. |

## Chapter 2 — Telecom Threats Without the AI Hype

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S1–S3; P2.S1–S5 | O4 / AI-1 | [Singapore CSA Operation CYBER GUARDIAN disclosure](https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector/) | Four major operators targeted; operation over eleven months; more than 100 defenders. The source does not attribute the activity to AI. Duration/defender count are response scale, not effectiveness. The source was directly reviewed in the earlier audit; browser recheck returned CloudFront 403. |
| P4.S2–S3; P5.S1–S4 | O23 / AI-1 | [FBI/CISA original CISA statement URL](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-peoples-republic-china-prc-targeting-commercial-telecommunications); [official FBI counterpart](https://www.fbi.gov/news/press-releases/joint-statement-from-fbi-and-cisa-on-the-peoples-republic-of-china-targeting-of-commercial-telecommunications-infrastructure) | Compromised telecom networks and disclosed data access; no AI attribution. CISA URL now returns Page Not Found; FBI page was Cloudflare-blocked in browser. Exact passage remains from prior direct review and is recorded in the claim ledger. |
| P4.S4–S5 | O6 / AI-1 | [FBI/CISA October 2024 statement](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-prc-activity-targeting-telecommunications) | U.S. government investigation into unauthorized access and response support; no public AI attribution. Full page body was directly read in this pass. |
| P7.S1–S4; P8.S1–S6 | O20 / EN-1 / AI-EN20; O21 / EN-2 / AI-EN21 | [ENISA 2024 OSINT overview PDF](https://www.enisa.europa.eu/sites/default/files/2025-03/5-ENISA_2024%20Telco%20threat%20landscape_March%202025.pdf); [ENISA 2024 authority-report summary](https://www.enisa.europa.eu/sites/default/files/2025-07/ENISA_Telecom_Security_Incidents_2024_en_1.pdf) | Distinct 30-incident OSINT collection and 188 authority-submitted significant-incident reports, with different scopes; 188 includes non-malicious causes. Geography discrepancy is unresolved and omitted. Do not compare as a rate or add as a cyberattack total. |
| P3; P6; P9–P15 | Author analysis/recommendation | No additional source claim | Definitions, evidentiary ladder, local questions and decision rule. They do not assert AI use in a named telecom incident or add incident measurements. |

## Chapter 3 — Follow Authority to the Network Target

| Draft anchor | Claim/source IDs | Primary source links | Support and limit |
|---|---|---|---|
| P1.S2–S4; P2.S1, S5 | T20 | [IEEE paper DOI](https://doi.org/10.1109/OJCOMS.2024.3364840); [author PDF](https://faculty.csie.ntust.edu.tw/~smcheng/papers/J39_2402_Security%20Threats%20to%20xApps%20Access%20Control%20and%20E2%20Interface%20in%20O-RAN.pdf) | Peer-reviewed experimental O-RAN H-Release study; missing xApp access permissions and three lab attacks through APIs/E2, with service disruption in the testbed. Not a carrier production deployment or an LLM-agent test. Authors disclose Trend Micro and Taiwan NSTC support. |
| P6.S1–S4 | T19 | [AgentDojo, NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/97091a5177d8dc64b1da8bf3e1f6fb54-Paper-Datasets_and_Benchmarks_Track.pdf) | Peer-reviewed benchmark demonstrating indirect prompt-injection mechanisms in simulated tool environments. No telecom systems, operator incident or network-control frequency/effectiveness estimate. Tool-count figures conflict in the paper and are not quoted. |
| P9.S1–S3 | T2 | [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) | Voluntary architecture publication; the source frames Zero Trust around users, assets and resources rather than static network perimeters. Not a telecom rule. Identity-governance distinction and application to target mapping are author analysis. |
| P14.S1–S2 | O8 | [CISA and international partners, Careful Adoption of Agentic AI Services](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai) | Cross-sector multi-agency guidance recommends low-risk/non-sensitive starts and avoiding broad or unrestricted access to sensitive data and critical systems. Not a telco-specific control standard. |
| P3–P5, P7–P8, P9.S4–S7, P10–P13, P15; authority-map table | Author analysis/recommendation | No additional source claim | Workflow definitions, distinction among identity/data/tool/target/service, local mapping aid and action-level categories. No operator-wide path, deployment, incident or test result is asserted. |

## Update rule

Add each chapter after drafting and ledger review. Where a sentence is author analysis rather than sourced fact, mark it as such; where a claim is omitted or qualified, keep the exact reason visible. When whole-book edits alter paragraph anchors, update this map in the same commit as the manuscript change.
