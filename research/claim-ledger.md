# High-consequence claim ledger

**Audit cut-off:** 16 November 2026. **Scope:** claims in `research/trend-synthesis.md`, `outline-v2.md`, and `research/research-map.md` that carry the evidence argument, especially deployment stage, operator-reported outcomes, the two ENISA datasets, AI attribution, UK telecom duties, and AI/Zero Trust/IGA convergence. This is a bounded claim audit, not a full audit of every source row or every quotation in the repository.

**Status key:** **Verified** = primary source text directly supports the stated wording and the essential scope is clear; **partially verified** = primary text directly says it, but important method, denominator, stage, or causal limits remain; **unresolved** = the primary text cannot be read or does not settle the claim; **exclude** = do not use as an established fact (it may remain as a clearly labelled proposal or reported statement).

A quote below is copied from a source body or report page opened directly. Where the source body was blocked, no quote is supplied. Search-result snippets and resolved URLs are not treated as source verification. “Verified” never means independently measured where the source is a company or vendor statement.

## 1. Heavy Reading: survey dates and autonomy claims

### HR-1 — Full survey population and field dates
- **Exact proposed wording (current map/trend):** “Heavy Reading surveyed 84 qualified individuals at mobile network businesses”; the synthesis further says the survey was “fielded globally July/August 2025.”
- **Primary source:** [2025 AIOps Network Operator Survey](https://radcom.com/wp-content/uploads/2025/10/HR-AIOps-Network-Operator-Survey.pdf), Heavy Reading/Omdia, report dated October 2025, p. 3.
- **Exact supporting passage:** “This report is based on a survey of 84 qualified individuals working at a verifiable network operator with mobile network businesses. The questionnaire was jointly developed by Heavy Reading (now part of Omdia), Amdocs, and RADCOM and fielded globally by corporate parent Informa TechTarget in July/August 2025.”
- **Source class / incentive:** Analyst survey/white paper hosted by RADCOM; questionnaire jointly developed with project partners Amdocs and RADCOM. The source does not publish names or respondent-level data. Commercial project-partner interest is material.
- **Denominator, geography, period, definition:** 84 people, not 84 distinct operators; global fielding; 43% worked at a mobile operator, 26% at a converged operator with a mobile network, and 14% at a cable operator with a mobile network. Respondent location was concentrated in the U.S. (48%, report demographics). The report calls respondents “qualified individuals” at verifiable network operators; it does not provide a unique-operator count.
- **Support and limits:** Directly verified as an 84-person survey of people at operators with mobile businesses, not an operator census. Percentages should be phrased as respondent self-reports, not “operators” as a population.
- **Status:** **Verified** for the sample description; not representative-population evidence.

### HR-2 — 47% bounded assurance autonomy and >74% intended agent deployment
- **Exact proposed wording:** “47% of n=83 self-reported bounded assurance autonomy and over 74% of n=82–83 planned agent deployments within two years.” The trend also quotes the assurance wording and uses this to distinguish bounded autonomy from closed-loop control.
- **Primary source:** Same Heavy Reading PDF, pp. 15–16 (Figure 11) and p. 25 (Figure 19).
- **Exact supporting passages:** p. 15: “Almost half of the respondents (47%) believe their network assurance operations are ‘operating autonomously for specific proactive use cases and domains, with minimal human oversight.’” Figure 11 gives `n=83`. p. 25: “Over 74% of operators plan to deploy AI agents across all NetOps survey categories within two years”; Figure 19 gives `n=82–83`. The report also says 64% are unlikely to deploy closed-loop automation or plan to do so in two to three years (p. 16; Figure 19).
- **Source class / incentive:** Same partner-supported analyst survey as HR-1; self-assessment and stated intention, not measured deployment telemetry.
- **Denominator, geography, period, definition:** Item denominators differ (n=83; n=82–83); people/respondents, not unique operators. Global survey, with 48% of respondents U.S.-based. Questions ask respondents to characterize maturity and plans; “within two years” is an intention horizon, not an observed rollout.
- **Date contradiction — direct report check:** The demographics paragraph on p. 3 says the survey was fielded globally in **July/August 2025**. Figure 11 (p. 16) and Figure 19 (p. 25) each state “Source: Heavy Reading (now part of Omdia), June 2025.” The PDF does not say whether June denotes a distinct figure-specific collection period, a source/cut date, or something else; it does not reconcile these notes with the stated survey fieldwork. Do not infer a separate June sample, editorial error, or date hierarchy. **The relationship between the figure notes and the survey fieldwork is unresolved.**
- **Support and limits:** The percentages and item n values are printed in the PDF, but the temporal basis of the figures is not settled. “Plan to deploy” is not production; “operating autonomously” is respondent characterization, not independent validation.
- **Local evidence required:** Ask each operator for the underlying workflow, respondents/owners, stage, action authority, sample period, and evidence of actual actions; do not use either percentage as a proxy for the operator’s own maturity.
- **Status:** **Partially verified** for the reported percentages and item denominators; **unresolved** for how the June 2025 figure notes relate to the July/August 2025 fieldwork and for any claim about actual market-wide deployment.

## 2. Check Point Q1 2025: growth versus volume

### CP-1 — 94% increase and 2,664 weekly attacks per protected telecom organization
- **Exact proposed wording in the map:** “Check Point Research’s ThreatCloud AI report says telecommunications had the highest year-over-year percentage increase in Q1 2025 (94%), reaching 2,664 attacks per organization weekly; the weekly-volume measure ranked third across sectors.”
- **Primary source:** Check Point Research, [Q1 2025 Global Cyber Attack Report](https://blog.checkpoint.com/research/q1-2025-global-cyber-attack-report-from-check-point-software-an-almost-50-surge-in-cyber-threats-worldwide-with-a-rise-of-126-in-ransomware-attacks/), published 16 April 2025 (WordPress post ID 247359; last modified 21 May 2025). The article HTML/browser path returned 403, but the official Check Point WordPress REST API returned the complete post body (HTTP 200); the quotes below are from that body, not a search snippet.
- **Exact supporting passages:** In “Sectors Most Affected,” Check Point says the telecommunications sector had “the highest percentage increase, with a 94% jump, reaching 2,664 attacks per organization weekly.” Its summary separately says telecommunications had 2,664 weekly attacks, behind education (4,484) and government (2,678), so it ranked third by weekly volume, not by growth. The source footnote says: “The statistics and data used in this report present data detected by Check Point ThreatCloud AI platform, which analyzes big data telemetry and millions of Indicators of Compromise (IoCs) daily. Our threat intelligence database is sourced from 150,000 connected networks, millions of endpoint devices, Check Point Research (CP), and dozens of external feeds. Over 50 AI-powered engines provide weekly reports on attacks our solutions prevented, and organizational networks Check Point protected, broken down by country and sector.”
- **Source class / incentive:** Check Point Research company report using vendor ThreatCloud AI/product telemetry; commercial interest in reporting threat volume and threat-intelligence capability. It is not a respondent survey, independent census, or count of successful incidents.
- **Denominator, geography, period, definition:** Q1 2025 versus the same quarter of 2024; global report, with sector-level counts. The source says it reports on attacks its solutions prevented and on organizational networks Check Point protected, broken down by country and sector. It does not publish the telecom-only number of protected organizations, selection/inclusion method, deduplication rule, or precise unit/definition of an “attack.”
- **Secondary source cross-check:** The directly opened [Protiviti article, 26 September 2025](https://blog.protiviti.com/2025/09/26/zero-trust-iga-and-ai-in-next-gen-telecom-networks-cisos-convergence-approach/) calls the measure a “survey” and says telecom had the third-highest percentage increase. The primary Check Point article contradicts both labels: it identifies vendor telemetry and says highest percentage increase, while telecom is third by weekly volume.
- **Required treatment:** Keep growth (94%, highest sector YoY increase) and weekly volume (2,664 per protected organization, third by volume) as separate facts. Attribute both to Check Point telemetry, state the protected-network scope and undisclosed telecom denominator/event definition, and never describe them as sector-wide prevalence or successful-incident counts.
- **Status:** **Partially verified.** The primary wording, period, ranking and telemetry source are directly verified via the official REST API; telecom-specific denominator, sampling/inclusion method and attack definition remain unresolved.

## 3. Operator and supplier claims: stage, scale, and outcomes

### OP-1 — Deutsche Telekom RAN Guardian production and first-month results
- **Exact proposed wording:** “Deutsche Telekom says its RAN Guardian Agent is live in production in Germany and reports 100+ autonomous remediation actions in its first month and management of major events falling from hours to about a minute.”
- **Primary source:** [Deutsche Telekom and Google Cloud announcement](https://www.telekom.com/en/newsroom/latest-updates/media-information/2026/2/mindr-ai-agents-in-telekom-network), 25 February 2026.
- **Exact supporting passages:** The announcement says RAN Guardian is “already live in production in Germany”; it reports “over 100 remediation actions autonomously triggered” in the first month after launch and says live operations reduced major-event management time “from hours to around a minute.”
- **Source class / incentive:** Joint operator/hyperscaler announcement; operator-reported deployment and benefits, co-marketed by Google Cloud. Not an independent measurement.
- **Denominator, geography, period, definition:** Germany; first month after launch for the 100+ actions; the announcement says launch was in November 2025 and refers to Christmas-market events. It does not state the number/type of events, action success/failure counts, baseline method, or how “time to manage major events” was measured.
- **Cross-source date qualification:** Deutsche Telekom’s 5 October 2026 Investor Day transcript says RAN Guardian was live in Germany “since January.” The February announcement says it launched in November 2025. These may describe different rollout milestones, but the sources do not reconcile the dates. Report the two source statements with their dates; do not silently choose one.
- **Local evidence required:** Action logs, event sample, exact action authority, acceptance/override/retry/rollback rates, time-measurement start/end, service-impact data, and the baseline/comparator.
- **Status:** **Partially verified** as a company-reported, bounded production deployment and reported result; not independent proof of safer operations or security improvement.

### OP-2 — MINDR MVP and live demo
- **Exact proposed wording:** The map distinguishes MINDR from production RAN Guardian and says the October 2026 transcript called it an MVP “about to go live.”
- **Primary source:** [Deutsche Telekom AI Investor Day transcript](https://corporate-media.telekom.com/adobe/assets/urn:aaid:aem:5f06dc2a-d1c8-491d-a4ad-c2ae675f9310/original/as/DT%20AI%20Investor%20Day%20-%20Transcript.pdf), 5 October 2026, p. 12 and pp. 15–16.
- **Exact supporting passage:** “MINDR is an MVP that is about to go live”; later the transcript says the “first use case as an MVP [will be] live by the end of the year in Germany.” The transcript labels the demo as being “for this demo purposes” and introduces a step-by-step view.
- **Source class / incentive:** Operator management/investor presentation; demonstration and future plan, not independent deployment evidence.
- **Denominator, geography, period, definition:** First MINDR use case in Germany; planned MVP live by end of 2026. No production data, duration, adoption, error/override or service results are provided. The demonstration is not evidence of a live customer incident or production performance.
- **Status:** **Partially verified** for “MVP about to go live” as of 5 October 2026; **unresolved** for actual status after that date. Do not describe MINDR as established production at the 16 November audit cut-off without a later operator source.

### OP-3 — One NZ Network Concierge and generator-placement assistant
- **Exact proposed wording:** “One NZ says it deployed the Network Concierge agent … and reports an 80% reduction in analysis time”; a separate weather-related generator-placement tool was used during severe weather.
- **Primary source:** [One NZ media release](https://media.one.nz/networkconcierge), 2 December 2025.
- **Exact supporting passages:** “One New Zealand today announced it has deployed a ‘Network Concierge’”; “Our Network Concierge agent reduces the time to analyse network-related customer complaints by 80 percent”; body text says, “An 80% drop-in analysis time.” The same release separately says AWS agentic AI was put to work during storms/outages to help engineers decide where to send mobile generators.
- **Source class / incentive:** Operator media statement; AWS platform dependence and partner context are disclosed. No independent measurement.
- **Denominator, geography, period, definition:** Network-related customer complaint analysis; no number of cases, baseline duration, measurement window, comparator, sample selection, quality/error rate, or cost is published. The generator-placement example is a separate workflow, not a network-state-changing agent.
- **Local evidence required:** Case count and period, definition of “analysis time,” before/after sample, complaint complexity mix, accepted answer rate, human rework/override, and service impact; for generator placement, decision outcome and resilience measure.
- **Status:** **Partially verified** as an operator-reported deployment and outcome; no causal, security, or sector-wide productivity conclusion.

### OP-4 — One NZ Core Network VoLTE Agent
- **Exact proposed wording:** “Google Cloud’s separate One NZ VoLTE-agent item is a vendor-reported ‘deploying’ status.”
- **Primary source:** [Google Cloud, “Scaling the autonomous network: Introducing the Data Steward and Core Network Agents”](https://cloud.google.com/blog/topics/telecommunications/new-agents-for-the-autonomous-network-operations-framework), 4 March 2026.
- **Exact supporting passages:** Google says One NZ “has deployed [the agent] into its operations,” then quotes its own executive saying “One NZ is deploying the Core Network VoLTE Agent.”
- **Source class / incentive:** Vendor announcement with a customer name; commercial incentive to demonstrate framework adoption. No operator-authored confirmation or measured result in the cited passage.
- **Denominator, geography, period, definition:** One NZ is named; the deployment scope, dates, production status, operator users, affected network elements, authority and KPI are not stated.
- **Caveat:** The vendor’s own page uses both completed (“has deployed”) and ongoing (“is deploying”) language. The status cannot be resolved from this source.
- **Status:** **Unresolved** as to production stage; accurately label as a vendor-reported deployment claim, not verified production.

### OP-5 — Orange France MAIA and Sharlie
- **Exact proposed wording:** The map says MAIA is deployed to 3,000 sales advisers and supports nearly 1 million conversations/month; the synthesis currently calls Sharlie prospective.
- **Primary source:** [Orange France press release](https://www.orange.com/en/press-release/orange-france-launches-two-new-artificial-intelligence-services-to-enhance-customer-relations-444308), published 17 March 2026.
- **Exact supporting passages:** “Deployed to 3,000 Orange sales advisors”; “Launched in early December 2025, Mon Assistant IA already supports nearly 1 million conversations per month”; “The advisor remains in control of the relationship and validates the proposed responses.” The release describes the launch of two services, Sharlie and MAIA, and says Sharlie is “Available 24/7.” It also says: “Once deployed, the Sharlie voice assistant will have the capacity to handle over 3 million conversations per year.”
- **Source class / incentive:** Operator press release; the release names Verint, Microsoft, ILLUIN Technology, and TP as technology/operating partners. Company-reported rollout and scale.
- **Denominator, geography, period, definition:** Orange France sales advisers; 3,000 accounts are the stated deployment reach. “Nearly 1 million conversations per month” is a volume claim as of the release, not unique users or a measured result. The release gives no adviser activity distribution, quality/error/override rate, cost, or measurement method. The >3 million Sharlie figure is explicitly a prospective capacity (“once deployed”), not realized usage.
- **Correction:** The source does not support “Sharlie remains prospective” as a general status: Orange’s own 17 March release calls the service launched and available, while separately making its 3-million/year capacity prospective. Avoid conflating launch/availability with proven scale or actual volume.
- **Local evidence required:** Number of active advisers, usage per adviser, time period and conversation definition, response acceptance/rework/error/complaint rates, impact on customer resolution, and total cost; for Sharlie, actual traffic, containment/transfer rates, safety and service outcomes.
- **Status:** **Partially verified** for Orange’s reported MAIA deployment and volume; **verified** that the 3-million/year number is prospective capacity, not an observed result. Neither establishes security improvement or ROI.

### OP-6 — Telefónica “500+” AI use cases and 15 Level 4
- **Exact proposed wording:** “Telefónica claims 500+ AI use cases in production and 15 at Level 4, without publishing an inventory or per-case evidence.”
- **Primary source:** [Telefónica, “How Telefónica is reinventing smart telecommunications network management”](https://telefonica.com/en/communication-room/blog/autonomous-networks-ai-advanced-automation-telefonicas-strategy-building-network-future), 31 August 2026.
- **Exact supporting passage:** “Currently, the company has more than 500 AI use cases in production, 15 of which are already at Level 4 of autonomy.”
- **Source class / incentive:** Operator corporate blog by a Telefónica executive; company strategy and progress claim.
- **Denominator, geography, period, definition:** Telefónica group; the source does not enumerate use cases, define which forms of AI count, name the denominator of eligible workflows, break the 500 down by country/domain, or describe how “in production” and Level 4 were audited. No measurement period or independent verification is supplied.
- **Status:** **Partially verified** as the company’s exact public claim, not as an independently verified deployment census or proof of 500 scaled production systems.

### OP-7 — Telefónica Germany Network Operation Agent (NOA)
- **Exact proposed wording:** “Telefónica Germany developed Network Operation Agent (NOA) for NOC incident analysis; production scale and measured results are unstated, and closed-loop actions are future work.”
- **Primary source:** [Telefónica, “Driving network incident resolution with AI agents and LLMs”](https://telefonica.com/en/communication-room/blog/driving-network-incident-resolution-ai-agents-llms), 30 March 2026.
- **Exact supporting passages:** “In Telefonica Germany [they] have developed the Network Operation Agent (NOA)”; the article says it is integrated with ticketing and accesses databases, documentation and prior closed-incident resolutions. It says that with future orchestrator/agent integration it “will be possible to execute intents and closed-loop actions directly over the network.”
- **Source class / incentive:** Operator-authored corporate technology article; no independent evaluation.
- **Denominator, geography, period, definition:** Telefónica Germany; no user count, production start, incident count, accuracy, handling-time result, or service outcome. The described future closed-loop action is not an achieved NOA capability in this article.
- **Status:** **Partially verified** for development and stated integration; **unresolved** for production stage and operational result. Do not present NOA as live closed-loop production.

### OP-8 — SK Telecom/Samsung AI-RAN recommender
- **Exact proposed wording:** “SKT says its recommender was applied and validated on the commercial network while real-time application remained future work.”
- **Primary source:** [SK Telecom Newsroom](https://news.sktelecom.com/208077), 28 October 2024 (Korean operator release; machine translation should be checked by a Korean reader before any quotation in the book).
- **Exact supporting passage (translated page text):** SKT says the AI-based parameter recommender was “applied to the commercial network” and “systematically demonstrated/validated”; it says expanding the parameters and subway application were ongoing, while “developing real-time application” was planned for the future.
- **Source class / incentive:** Joint operator/vendor announcement (SK Telecom and Samsung); no independent validation.
- **Denominator, geography, period, definition:** SKT 5G base-station parameters; cell count, test period, comparison group, KPI lift, approval/rollback and production footprint are not given.
- **Status:** **Partially verified** as commercial-network application and systematic validation, not network-wide autonomous production or measured customer/service improvement.

### OP-9 — Airtel/Ericsson Operations Engine results
- **Exact proposed wording:** “Airtel’s Ericsson Operations Engine case reports 69% of alarms fully automated, MTTR down 29%, network unavailability down 47%, and a 26% customer-experience-related result.”
- **Primary source available:** [TM Forum case study, “Airtel’s data-driven transformation journey”](https://info.tmforum.org/Airtels-data-driven-transformation-journey.html), case page presented as 2022; the Ericsson case page [returned anti-bot blocking](https://www.ericsson.com/en/cases/2022/airtels-data-driven-transformation-journey).
- **Exact supporting passage:** TM Forum case “Outcomes” states: “Doubled the amount of automation in its network; 69% of alarms fully automated; Reduced mean time to repair (MTTR) by 29%; Reduced network unavailability by 47% resulting in a 26% improvement in customer experience.” It gives operator context of a multivendor Indian 2G/4G network, 112 petabytes/day and 220,000 towers.
- **Source class / incentive:** Vendor/industry-association case study for Ericsson Operations Engine, with an Airtel CTO quotation. It is not independent corroboration; the Ericsson primary page body was inaccessible, so the accessible TM Forum case is the only readable case text.
- **Denominator, geography, period, definition:** Airtel India network; no time period, baseline, sample size, denominator for alarm automation, measurement method, confidence interval, or definition of “26% improvement in customer experience.” Do not silently convert that phrase into complaint reduction or an audited KPI.
- **Status:** **Partially verified** that the case report states these results; **unresolved** as measured/causal performance. Not a sector benchmark or security outcome.

### OP-10 — China Mobile/ZTE: event deployments versus pilot metrics
- **Exact proposed wording in the synthesis/map:** “GSMA describes a China Mobile/ZTE large-model network O&M pilot” and reports “83% lower assurance-manpower investment and fivefold efficiency.” The outline calls it an “O&M pilot.”
- **GSMA source sought:** [GSMA Foundry project page](https://www.gsma.com/get-involved/gsma-foundry/gsma_resources/increase-efficiency-operations-and-maintenance-om-china-mobile-zte/). **No source passage was retrieved:** the page was reported blocked by anti-bot controls and no readable primary text was obtained in this audit. The 83% and fivefold figures are not quoted or validated here.
- **Alternate primary supplier source:** [ZTE announcement](https://www.zte.com.cn/global/about/news/china-mobile-and-ztes-multi-agent-collaboration-solution-wins-gsma-foundry-network-efficiency-and-optimization-award.html), 4 March 2025.
- **Exact supporting passage from ZTE:** “The solution has been successfully deployed at various high-profile events, including the World Internet Conference in Wuzhen, concerts at Hangzhou Olympic Sports Center, the Jin'an International Tennis Open, and Xi'an Datang Everbright City.” It reports “monitoring personnel requirements decreased by 30% during the Hangzhou Olympic Sports Center concert, while network traffic increased by 20% at Xi'an Datang Everbright City.”
- **Source class / incentive:** Supplier/partner success announcement by ZTE about its China Mobile joint solution; award and commercial incentive. Not an operator-authored independent evaluation.
- **Denominator, geography, period, definition:** Event-specific deployments in China; the 30% compares staffing requirements at one named concert, but headcount/baseline/time period are absent. The 20% network-traffic increase is a different event and not a security or efficiency KPI. No routine network-wide production footprint is stated.
- **Treatment:** These ZTE event claims do not validate the GSMA 83%/5× figures. Do not merge the distinct numbers or call event deployments evidence of scaled routine production. If citing GSMA’s “pilot” label or 83%/5×, keep it explicitly unresolved until the page or another primary source is opened.
- **Local evidence required:** Named use case/site, event period, staffed baseline and task definition, control authority, network/service KPI, comparison method, error/override/fallback and independent operator confirmation.
- **Status:** **Partially verified** for ZTE’s event-specific supplier-reported deployments and figures; **unresolved** for the GSMA pilot status and 83%/fivefold claims.

### OP-16 — ZTE white-paper claim of deployment across 10+ sites
- **Exact proposed wording in the research map:** “Direct PDF review (p. 43) confirms ZTE claims digital intelligent agents deployed at over 10 sites across China and abroad, naming China Mobile, China Telecom, Bangladesh GP and Thailand AIS. The same supplier white paper reports, for its GP Bangladesh O&M services, MTTR down 12.5%, human-machine collaboration efficiency up 70%, and outstanding fault work orders down 3%.”
- **Primary source:** [ZTE Autonomous Networks White Paper 2026](https://www.zte.com.cn/content/dam/zte-site/res-www-zte-com-cn/mediares/zte/service/ZTE%20Autonomous%20Networks%20White%20Paper%202026%20(EN).pdf), 2026, PDF p. 43 (the “Results” section for digital intelligent agents for fault management).
- **Exact supporting passages:** “The digital intelligent agents for fault management have been deployed across over 10 sites across China and abroad, including China Mobile, China Telecom, Bangladesh GP, and Thailand AIS. These implementations empower 5 high-value professional scenarios for fault monitoring and handling…” The next passage says ZTE provides network O&M services for GP Bangladesh and reports “a 12.5% reduction in fault MTTR (KEI), a 70% improvement in human-machine collaboration efficiency, and a 3% reduction in outstanding fault work orders.”
- **Source class / incentive:** ZTE vendor white paper; commercial incentive to demonstrate product deployment and autonomous-network capability. The stated outcomes are supplier-reported, not operator-confirmed evidence.
- **Denominator, geography, period, definition:** “Over 10 sites” is a site count, not a distinct-operator count. The paper names China Mobile, China Telecom, Bangladesh GP and Thailand AIS but does not allocate sites among them or state rollout/production dates, deployment threshold, per-operator stage or observation period. For GP Bangladesh, the paper gives no MTTR/work-order denominator, baseline, period, comparison method, confidence/quality measure or definition of “human-machine collaboration efficiency.”
- **Support and limits:** The PDF was directly downloaded and searched; its text directly supports that ZTE makes the deployment and outcome claims. It does not independently verify the named operators’ acceptance, production stage, scale per operator, or results.
- **Status:** **Partially verified** as ZTE-reported multi-site deployment and GP Bangladesh case metrics; not an independently verified operator production census or performance result.

### OP-11 — China Mobile figures repeated by TM Forum
- **Exact proposed wording in the research map’s unresolved notes:** A TM Forum article reports China Mobile “30% O&M staffing / 30% MTTR” claims.
- **Primary/secondary source:** [TM Forum, “How telcos worldwide are implementing AN”](https://inform.tmforum.org/features-and-opinion/how-telcos-worldwide-are-implementing-an), 15 April 2026.
- **Exact passage:** “China Mobile, for example, already cites a more than 30% reduction in backend O&M man-power, as well as a 30% reduction in fault and customer complaint mean time to repair (MTTR) on average, by reaching Level 4 in its network operations centers.” The page also says it surveyed 125 people at 80 companies worldwide.
- **Source class / incentive:** TM Forum survey/report excerpt and industry analysis; the China Mobile outcome statement is not linked to a directly accessible China Mobile source in the article. TM Forum promotes its Autonomous Networks benchmark/research.
- **Denominator, geography, period, definition:** China Mobile operations; no staffing baseline, denominator, measurement period, scope of the NOCs, Level 4 criteria, or MTTR calculation is supplied. The survey’s 125 people/80 companies is not the denominator for the China Mobile metric.
- **Treatment:** Keep separate from ZTE/GSMA event results. Do not present as independent operator evidence or merge it with the 83%/5× pilot metrics.
- **Status:** **Unresolved** as a China Mobile result until an operator primary source and method are obtained; the TM Forum page verifies only that TM Forum printed the claim.

### OP-12 — TELUS customer-facing GenAI search metrics
- **Exact proposed wording:** “TELUS reports 50,000+ customer queries and 28% more customers finding information than conventional search.”
- **Primary source:** [TELUS media release](https://www.telus.com/en/about/news-and-events/media-releases/telus-unveils-genaI-customer-support-tool-powered-by-fuel-ix-and-microsoft-azure-openaI-service%20to%20enhance%20customer%20experience), 6 May 2024; [company-distributed Newswire copy](https://www.newswire.ca/news-releases/telus-unveils-genai-customer-support-tool-powered-by-fuel-ix-and-microsoft-azure-openai-service-to-enhance-customer-experience-879815483.html).
- **Retrieved passage:** None. TELUS returned a Cloudflare block in the browser. The company-distributed Newswire copy returned a bot-verification page. Search-result snippets are not accepted as verification; no quote is supplied.
- **Source class / incentive:** Proposed operator press release about a customer-accessible GenAI feature built with Fuel iX and Microsoft Azure OpenAI; commercial product/partner announcement.
- **Denominator, geography, period, definition:** The project’s earlier note says rollout began in 2024 and records 50,000 queries and a 28% comparison; the accessible primary body does not permit verification of timing, sample, unique visitors, comparison design, answer quality, cost, or whether “customers” means sessions or people.
- **Status:** **Unresolved**. Do not use the figures as measured adoption, productivity, quality, or ROI until the release body or an alternate TELUS/Microsoft primary case can be opened.

### OP-13 — BT Call Protect service and blocked-call counts
- **Exact proposed wording:** The map says BT’s service is AI-powered, and that the 2024 release reports 2.43m scam and 17.7m spam calls blocked across 2.5m customers.
- **Primary source for service:** [BT Help: Call Protect for Digital Voice](https://www.bt.com/help/home-phone/digital-voice-calling-features-/bt-call-protect-for-digital-voice), current page accessed 16 November 2026.
- **Exact supporting passage:** “Our partner, Hiya, delivers an AI-powered service which monitors incoming calls in real-time and notifies you of any suspected nuisance calls.” The BT help page says the feature is part of Digital Voice/Home Phone Standard.
- **Primary source sought for counts:** [BT newsroom release, 3 October 2024](https://newsroom.bt.com/bts-new-home-phone-scam-protection-service-stops-201-million-scam-and-spam-attempts-in-first-4-months/). Direct page returned 403; no release body obtained. Its title/search listing is not sufficient evidence.
- **Source class / incentive:** BT product/service page and partner-driven consumer-security feature; release metrics are BT service telemetry if confirmed, not independent efficacy measurement.
- **Denominator, geography, period, definition:** Service page confirms a UK customer product but gives no scale. The alleged release window is first four months from May 2024; unique callers, attempted calls, classification accuracy, false positives, fraud losses, and covered-customer denominator are not verifiable here.
- **Status:** **Verified** that BT describes a customer-facing Hiya AI-powered screening service; **unresolved** for the 2.43m/17.7m/2.5m counts. This is not evidence of BT internal SOC adoption.

### OP-14 — Orange Cyberdefense/Qevlar SOC integration
- **Exact proposed wording:** “Orange Cyberdefense announced a gradual Qevlar AI rollout in SOCs, without scale or outcome data.”
- **Primary source:** [Orange Cyberdefense/Orange newsroom](https://newsroom.orange.com/ocd-qevlar-334578), 6 October 2025.
- **Exact supporting passage:** “Through the gradual integration of Qevlar’s AI platform into its Security Operation Centers (SOCs), Orange Cyberdefense will be able to” improve alert processing, responsiveness and analysis.
- **Source class / incentive:** Provider/vendor partnership announcement by Orange Cyberdefense and Qevlar; commercial announcement.
- **Denominator, geography, period, definition:** No SOC count, rollout date/coverage, production threshold, alert volume, accuracy, false-positive rate, analyst time, containment outcome or customer cohort is stated. The benefits are framed as expected (“will be able to”).
- **Status:** **Partially verified** as an announced gradual integration; **exclude** any claim of scaled production or demonstrated SOC benefit.

### OP-15 — Vodafone/JT/FICO fraud case and the “30%/44%” figures
- **Exact proposed wording:** The map records a 30% detection improvement after a three-month pilot at one UK bank, 30–40% customer savings, up to 55% fewer false positives, and 44% overall fraud-loss decrease.
- **Primary source accessible:** [Vodafone Business case study](https://www.vodafone.com/business/news-and-insights/case-studies/fighting-evolving-app-fraud-threat-jt-fico), 3 April 2025.
- **Exact supporting passage on the live page:** Under “Results”: “Reduced fraud losses between 30-40% with a decrease in false positives by up to 55%.” The “Solution” says “Use algorithms and mobile intelligence to identify irregular behaviours.”
- **Source class / incentive:** Vodafone/JT/FICO commercial case study; the service applies mobile-network data to financial institutions/bank fraud, not an internal telecom security control. The page describes algorithms/mobile intelligence; it does not call the method AI.
- **Denominator, geography, period, definition:** The current page gives no customer sample, bank count, baseline, observation period, denominator, or calculation for the 30–40% and 55% claims. The “30% after a three-month pilot” and “44%” wording in the map was **not found in the accessible case-page text**; a downloadable case study was linked but no readable copy was obtained in this audit.
- **Status:** **Partially verified** for the page’s 30–40%/up-to-55% claims as vendor-reported; **unresolved** for the 30%/three-month and 44% claims. Do not call this AI deployment evidence or a telecom-wide outcome.

## 4. Surveys and adoption/ROI claims

### SV-1 — TM Forum 2026 AN survey (125 people/80 companies)
- **Exact proposed wording:** “TM Forum’s separate 2026 survey covered 125 individuals at 80 companies.”
- **Primary source:** [TM Forum, “How telcos worldwide are implementing AN”](https://inform.tmforum.org/features-and-opinion/how-telcos-worldwide-are-implementing-an), 15 April 2026.
- **Exact supporting passage:** “During research for our latest AN Benchmark report we surveyed 125 individuals at 80 companies worldwide.”
- **Source class / incentive:** TM Forum report excerpt/industry survey, authored by TM Forum staff; an industry association promoting an Autonomous Networks benchmark.
- **Denominator, geography, period, definition:** 125 people across 80 companies; worldwide. Field dates, operator/vendor respondent split, question-specific n values, sampling frame, response rate and weighting are not disclosed on the page. It includes estimates and company examples; it is not a representative operator census.
- **Additional claim requiring caution:** The article says “some CSPs estimate they can resolve 95% of trouble tickets without human intervention” but names no respondent, sample, definition, period or measurement. This is an unattributed estimate, not an established outcome.
- **Status:** **Partially verified** for the published sample description; **exclude** the 95% ticket claim as an outcome unless a named operator source and method are obtained.

### SV-2 — TM Forum China Mobile claims in the same 2026 article
- **Exact proposed wording:** Trend 2 uses O3 as evidence that fully realized zero-touch remains out of reach for most CSPs; the research map also records China Mobile’s >30% backend manpower and 30% MTTR claims.
- **Primary/secondary source:** Same TM Forum article as SV-1, 15 April 2026.
- **Exact passages:** The article says a fully realized zero-touch vision “remains out of reach for most operators” and says China Mobile “already cites a more than 30% reduction in backend O&M man-power” and “a 30% reduction in fault and customer complaint mean time to repair (MTTR) on average.”
- **Source class / incentive:** TM Forum industry report excerpt; not linked to an accessible China Mobile primary statement. No independent corroboration.
- **Denominator/method:** No China Mobile site, sample, baseline, period, calculation, or validation is given. The 125/80 survey sample does not substantiate the separate China Mobile result.
- **Status:** **Partially verified** that the TM Forum page contains these statements; **unresolved** as operator-measured results. Qualify “most operators” as the article’s synthesis, not a measured population prevalence.

### SV-3 — TM Forum interim AN ROI survey
- **Exact proposed wording:** “TM Forum’s 2026 interim survey of 78 validated operator respondents reports that 62% can easily link AN improvements to operational benefits, while 37% can link those benefits to financial outcomes; results may change before final publication.”
- **Primary source:** [TM Forum, “AN has a benchmarking challenge: The road to ROI must be measured”](https://inform.tmforum.org/features-and-opinion/an-has-a-benchmarking-challenge-the-road-to-roi-must-be-measured), 7 October 2026.
- **Exact supporting passages:** “Interim TM Forum survey data from 78 validated operator respondents…”; “These percentages may change by the time the survey closes”; and “62% of telcos can easily link autonomous network improvements to operational benefits / But only 37% can link AN operational benefits to financial outcomes.”
- **Source class / incentive:** TM Forum interim survey/research article; TM Forum states it will publish a final report and asks for survey participation. No external sponsor is identified on the page.
- **Denominator, geography, period, definition:** 78 validated operator respondents overall; no geographic split, precise start date, sampling frame, response rate, question-level n, weighting, or definitions for “easily link” are stated. At the time of the article, the operator and vendor surveys were still open and expected to close in late October. These are respondent perceptions, not audited ROI or causal measurement.
- **Status:** **Partially verified** for the preliminary reported percentages and sample count; not final or audited ROI evidence.

### SV-4 — Heavy Reading percentages as evidence of production
- **Exact proposed wording:** The outline asks “Which operator deployments are live?” and cites Heavy Reading surveys alongside production cases.
- **Primary source:** Heavy Reading survey, same PDF as HR-1/HR-2.
- **Evidence distinction:** HR-2 reports self-assessed maturity and future deployment intentions. It does not verify actual agent installations, production counts, safe authority, outcome, or security efficacy. Its June/July–August date discrepancy remains unresolved.
- **Status:** **Exclude** any conversion of 47%/74% into production prevalence or sector-wide readiness. Use only as respondent self-report/intention with the date contradiction visible.

## 5. ENISA datasets and AI attribution

### EN-1 — 30 telecom cybersecurity incidents in the 2024 OSINT overview
- **Exact proposed wording:** “ENISA separately reported 30 telecom incidents in its 2024 OSINT collection.”
- **Primary source:** [ENISA, 2024 Telecommunications Cyber Threat Overview](https://www.enisa.europa.eu/sites/default/files/2025-03/5-ENISA_2024%20Telco%20threat%20landscape_March%202025.pdf), 20 March 2025, p. 3.
- **Exact supporting passages:** The original overview’s p. 3 infographic says “30 cybersecurity incidents in 2024” and “Source: ENISA OSINT collection.” On p. 4, the “Tempo of Activity” section states: “Late January–February: Several attacks reported in SP, IT, NL, BE, and DK”; “June–July: Uptick in attacks claimed by NoName057, focusing on RO, BE, FR, and PT”; and “November: Another cluster of incidents, mostly data breaches and ransomware, especially affecting FR and IT.”
- **Source class / incentive:** EU agency threat-landscape overview using open-source intelligence; no vendor sponsor indicated.
- **Denominator, geography, period, definition:** Calendar-year 2024 cybersecurity incidents included in ENISA’s OSINT collection. Page 4 gives selected geographic activity using abbreviations as printed; the eight-page overview does not define the complete geographic universe, an all-incident population, a unique-operator denominator, or a standardized inclusion threshold. It is not a census.
- **AI attribution:** The overview text opened in this audit does not attribute AI to the listed incidents. It is not evidence that AI was never used.
- **Status:** **Partially verified** as an OSINT count. Do not compare it as a rate with EN-2.

### EN-2 — 188 authority-submitted telecom security incident reports
- **Exact proposed wording:** “ENISA’s separate annual summary reports 188 authority-submitted incident reports.”
- **Primary source:** [ENISA publication page](https://www.enisa.europa.eu/publications/telecom-security-incidents-2024), publication date 15 July 2025; directly opened [original report PDF](https://www.enisa.europa.eu/sites/default/files/2025-07/ENISA_Telecom_Security_Incidents_2024_en_1.pdf), executive summary pp. 3–4 and reporting/root-cause sections pp. 7, 11–12.
- **Exact supporting passages:** Executive summary, p. 3: “The 2024 annual summary contains reports of 188 incidents submitted by national authorities from 26 EU Member States and 2 European Free Trade Association (EFTA) countries.” Introduction, p. 7: “Electronic communication providers in the EU have to report security incidents that have a significant impact on the continuity” to national telecom regulatory authorities; “Every year the NRAs provide ENISA with a summary of the most significant incidents based on a set of agreed EU-wide thresholds”; the report “aggregates the 188 incident reports received in 2024.” Root-cause analysis, p. 11: “For the year 2024, 25 EU Member States, two European Free Trade Association countries participated in the annual process, reporting 188 significant incidents.” The report lists 178 service outages and root causes including system failures, human errors, natural phenomena, and malicious actions (pp. 3–4, 11–12).
- **Source class / incentive:** ENISA annual regulatory-reporting summary based on national authority submissions under Article 40 of the European Electronic Communications Code; official public-sector data product.
- **Denominator, geography, period, definition:** Incidents occurred during calendar year 2024; the report says the 2024 reporting period ran from 1 January to 24 February 2025. Provider notifications of significant continuity-impact incidents go to national authorities, which submit annual summaries to ENISA under the EECC reporting process. The collection uses agreed EU-wide thresholds and is described as major/significant incidents, not all cyberattacks or all minor events. The current ENISA publication page (15 July 2025) repeats the 26-EU-Member-State figure from the executive summary; the linked official PDF’s p. 11 instead says 25. No correction notice was present on the accessible publication page. The count remains unresolved.
- **Internal geography contradiction:** Executive summary p. 3 and the current ENISA publication page say 26 EU Member States plus 2 EFTA countries; root-cause analysis p. 11 says 25 EU Member States plus 2 EFTA countries reported the 188 incidents. The report does not reconcile the difference. Do not state exact Member-State coverage as settled.
- **AI attribution:** The report’s incident taxonomy and source text do not establish AI use; it does not provide a telecom-AI attribution count.
- **Status:** **Partially verified** for 188 reports and reporting mechanism; **unresolved** for exact Member-State participation count. Do not label 188 as 188 cyberattacks or compare it numerically with EN-1.

### AI-1 — Whether confirmed AI use in telecom attacks is established
- **Exact proposed wording:** “The reports do not establish AI use in those events”; “absence of public AI attribution is not proof AI was never used.”
- **Direct sources examined:** (1) [CSA Singapore disclosure](https://www.csa.gov.sg/news-events/press-releases/largest-multi-agency-cyber-operation-mounted-to-counter-threat-posed-by-advanced-persistent-threat--apt--actor-unc3886-to-singapore-s-telecommunications-sector/), 9 February 2026; (2) [FBI/CISA joint statement](https://www.cisa.gov/news-events/news/joint-statement-fbi-and-cisa-peoples-republic-china-prc-targeting-commercial-telecommunications), 13 November 2024; (3) [Google GTIG/Mandiant GRIDTIDE report](https://cloud.google.com/blog/topics/threat-intelligence/disrupting-gridtide-global-espionage-campaign), 25 February 2026; (4) ENISA sources EN-1 and EN-2.
- **Exact incident passages:** CSA says all four major Singapore telecom operators were targeted and describes a coordinated response spanning more than eleven months with over 100 cyber defenders; it does not attribute AI. FBI/CISA says PRC-affiliated actors compromised multiple telecom companies, enabling call-record theft, some private-communications compromise and copying of court-order information; it does not attribute AI. GTIG reports 53 victims in 42 countries across all sectors, including telecom/government targets; it does not give a telecom-only victim count in the passage reviewed or attribute the campaign to AI.
- **Source class / incentive:** Government incident disclosures (CSA, FBI/CISA), EU agency incident datasets, and vendor threat-intelligence investigation (Google/Mandiant). Google’s case is vendor telemetry/analysis and suspected state-nexus attribution, not a regulator incident census.
- **Denominator, geography, period, definition:** The incident disclosures use different populations and time periods; no shared denominator. The 53-victim Google number includes multiple sectors, not 53 telecom operators.
- **Boundary of finding:** These opened texts establish serious intrusion activity and do not establish AI use in those events. Other sources are blocked or incomplete (notably the IMDA backdoor advisory PDF, some Check Point/TELUS/BT sources), and absence of attribution is not evidence of absence. No confirmed AI-attributed telecom attack was established in this audit, but do not claim that none occurred.
- **Status:** **Partially verified** as a bounded reading of these named sources; a universal “no AI in telecom attacks” claim is **excluded**.

## 6. Legal status and applicability

### LAW-1 — UK Electronic Communications (Security Measures) Regulations 2022
- **Exact proposed wording:** “The UK’s Electronic Communications (Security Measures) Regulations are binding on public telecom providers.”
- **Primary source:** [Official consolidated Regulations](https://www.legislation.gov.uk/uksi/2022/933/contents) and [XML text](https://www.legislation.gov.uk/uksi/2022/933/data.xml), in force from 1 October 2022; official metadata records a 2 April 2024 modification date.
- **Exact passages:** Regulation 3(1): “A network provider must take such measures as are appropriate and proportionate to ensure…” security of the public electronic communications network. Regulation 4 imposes proportionate protections for data and network functions. Regulation 16(1): “Nothing in regulations 3 to 15 applies in relation to a network provider or service provider that is a micro-entity.” The official XML states the instrument’s extent as England, Wales, Scotland and Northern Ireland.
- **Source class / incentive:** Binding UK statutory instrument; official legislation text.
- **Applicability:** Applies to providers within the statutory definitions of public electronic communications networks/services, in the stated UK extent, subject to the statutory micro-entity exemption. It is not a blanket rule for every technology firm or every private network. Entity/service status and micro-entity classification must be assessed for the specific operator.
- **AI scope:** The Regulations impose telecom security duties; the reviewed text is not an AI-agent-specific control mandate. Do not infer that an AI feature automatically triggers a particular requirement without legal analysis.
- **Status:** **Verified** for the regulation’s in-force status, relevant duties, territorial extent and micro-entity exemption; organization-specific applicability requires counsel.

### LAW-2 — UK Telecommunications Security Code of Practice v1.1
- **Exact proposed wording:** “The related Code of Practice is guidance, with version 1.1 published 14 July 2026.”
- **Primary source:** [DSIT/GOV.UK Code v1.1 page](https://www.gov.uk/government/publications/revised-telecommunications-security-code-of-practice-2026-version-11) and [Code v1.1 PDF](https://assets.publishing.service.gov.uk/media/6a4fac891228eb26a4cab6de/Web_Accessible_-_COP.pdf), published/issued 14 July 2026, Version 1.1, §§0.15, 0.19–0.30 (printed pp. 7–10).
- **Exact supporting passages:** §0.19: “The Code of Practice provides detailed technical guidance to public telecoms providers on the measures to be taken under sections 105A to 105D of the Act.” §0.20 says it “is not the only way” to comply. §0.21 allows different technical approaches, but Ofcom may require reasons. §§0.22–0.23 require Ofcom and courts/tribunals to take relevant Code provisions into account. §0.15 says the measures are intended to apply to Tier 1 and Tier 2 providers; Tier 3 providers “are not expected to follow” the Code measures. §0.30 says Tier 3 providers still “must continue to take appropriate and proportionate measures to comply with their new duties under the Act and the regulations”; it also reiterates that the Regulations do not apply to micro-entities.
- **Source class / incentive:** Official government code/guidance issued under the Communications Act; not itself a statutory instrument, but legally relevant in Ofcom and court determinations.
- **Applicability:** The Code’s implementation tiers are based on relevant turnover. Tier 3 is not expected to follow the Code measures, but still has statutory duties unless the provider is a micro-entity exempt from Regulations 3–15. Private-network providers may choose to adopt relevant measures. Do not say simply “the Code is non-binding” without explaining its legal effects or simply “the Code applies to every provider.”
- **Status:** **Verified** for version, stated tiering, guidance status and legal effects. Specific operator tier and compliance posture require local legal review.

### LAW-3 — CIRCIA reporting status in the United States
- **Exact proposed wording:** “CIRCIA’s covered-entity reporting requirements are not a generic current mandate for all telecom companies.”
- **Primary source:** [CISA CIRCIA status page](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia), accessed 16 November 2026; [CIRCIA NPRM, Federal Register](https://www.federalregister.gov/documents/2024/04/04/2024-06526/cyber-incident-reporting-for-critical-infrastructure-act-circia-reporting-requirements), 4 April 2024.
- **Exact current passage:** CISA says it “continues to work on the final rule” and that “covered cyber incident and ransomware payment reporting under CIRCIA will not be required until the CIRCIA final rule goes into effect.”
- **Source class / incentive:** Current federal agency rulemaking page; official proposed rule. CIRCIA is enacted legislation mandating rulemaking, but the proposed reporting rule is not yet in effect.
- **Denominator, geography, definition:** U.S. covered entities as later defined by final regulation; the current page says reporting is voluntary before the final rule’s effective date. Telecom entities must be assessed against statutory and eventual final-rule scope; no blanket current CIRCIA reporting duty for every telecom provider is established here.
- **Status:** **Verified** as of the accessed 16 November 2026 CISA page. Recheck before publication because rulemaking can change.

### LAW-4 — Broad FCC, NIST, GDPR, and CISA statements in the Protiviti article
- **Exact proposed wording in the article:** FCC rules “require telecom companies and internet service providers to monitor their networks continuously, implement encryption protocols”; NIST ZTA guidelines “call for … real-time analytics”; GDPR requires “full visibility” into data flows; “CISA reporting mandates” demand rapid detection/response.
- **Sources:** Protiviti article, 26 September 2025 (directly opened); [FCC 25-81 announcement](https://www.fcc.gov/document/fcc-corrects-course-outlines-improved-cybersecurity-measures-0); [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final); [GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng); current CISA CIRCIA page above.
- **Exact source support:** The Protiviti article supplies no exact statute or section for the broad FCC wording. NIST SP 800-207 is a ZTA architecture publication, not a telecom rule requiring real-time analytics. GDPR Arts. 30 and 32 support records of processing and risk-appropriate security, not an unqualified “full visibility” duty. The CISA page says CIRCIA reporting requirements are not required until the final rule takes effect. The map records FCC 25-81 as rescinding the 2025 declaratory ruling and withdrawing its NPRM; the FCC page itself returned access denied in this audit, so that current-status detail is not re-quoted here.
- **Status:** **Exclude** the article’s blanket legal paraphrases. Use jurisdiction-, entity-, service-, and date-specific legal text; the FCC history needs a directly readable primary order before a new legal summary is published.

## 7. AI, Zero Trust, and IGA convergence

### ZI-1 — Integrated AI + Zero Trust + IGA is a production practice
- **Exact proposed wording:** Protiviti says “Some forward-thinking telecom CISOs are staying ahead of the curve with a combination of artificial intelligence, zero-trust security architecture and identity management tools”; the map notes the diagram as a design hypothesis, not a demonstrated outcome.
- **Source:** [Protiviti View article](https://blog.protiviti.com/2025/09/26/zero-trust-iga-and-ai-in-next-gen-telecom-networks-cisos-convergence-approach/), 26 September 2025, by Jim Kinsman, Managing Director, Security & Privacy.
- **Exact passage:** The article says the combination gives “continuous identity validation, autonomous threat detection and dynamic governance.” It names no operator, implementation, production system, measurement, denominator, or outcome supporting this adoption statement. The article’s commercial context is a consulting firm that sells technology/security advisory services.
- **Source class / incentive:** Consulting opinion/market narrative; commercial service incentive.
- **Denominator/geography/method:** None. “Some” is unquantified; no geography, population, field period, deployment definition or evidence is supplied.
- **Status:** **Exclude** as evidence of telecom production adoption. Retain only as a conceptual recommendation/proposition to test.

### ZI-2 — TM Forum zero-trust agent governance Catalyst
- **Exact proposed wording:** “One [Catalyst] applies Identity, Policy, Observability and Evidence to agent governance.”
- **Primary source:** [TM Forum, “If you cannot trust the agent, you cannot scale autonomy”](https://inform.tmforum.org/research-and-analysis/proofs-of-concept/if-you-cannot-trust-the-agent-you-cannot-scale-autonomy), 10 August 2026.
- **Exact source classification and passage:** The page labels the item “Proof Of Concept” and says the Catalyst “introduces a zero-trust model” and “is tackling” agent governance with a reusable model. It describes an IPOE framework (Identity, Policy, Observability, Evidence) and scenarios including impostor agents, prompt injection, lateral movement and scope creep.
- **Source class / incentive:** TM Forum Catalyst/proof-of-concept article; industry participants/solution providers may benefit from demonstrating the architecture. No operator production metrics are reported.
- **Denominator/geography/measurement:** No deployed-operator count, live production scope, control-efficacy measurement, service outcome, or evaluation sample is provided. The article’s broad “agents are entering live telecom operations” statement is not quantified in the source.
- **Status:** **Verified** as a Catalyst/POC design description; **exclude** as production adoption or measured security outcome.

### ZI-3 — AI compliance agent and identity-management Catalyst
- **Exact proposed wording:** “Another proposes an AI compliance agent that drafts access-policy changes for dry-run and human approval through a digital-identity layer.”
- **Primary source:** [TM Forum, “If you can’t prove it, you can’t sell it”](https://inform.tmforum.org/research-and-analysis/proofs-of-concept/if-you-cant-prove-it-you-cant-sell-it-making-trust-a-competitive-advantage), 10 August 2026.
- **Exact supporting passage:** The page labels the item “Proof Of Concept.” It says the compliance agent “translates [legal/contractual/policy text] into candidate access-policy updates”; “The agent does not directly apply policy changes to production systems”; proposed changes are tested by dry runs, and high-risk changes receive human review/approval.
- **Source class / incentive:** TM Forum Catalyst/POC article; proposed workflow/design demonstration, not independent operator evaluation.
- **Denominator/geography/method:** No production operator, deployment count, policy-change count, false positive/negative rate, audit result, service outcome or independent test is disclosed.
- **Status:** **Verified** as a proof-of-concept design; **exclude** as live AI+Zero Trust+IGA production evidence.

### ZI-4 — Telenor IGA vendor case
- **Exact proposed wording:** “Telenor’s vendor-reported IGA case is a separate component example, not AI+Zero Trust integration.”
- **Primary source:** [Omada case study, Telenor Norway](https://omadaidentity.com/resources/case-studies/telenor-norway-case/), publication date not stated on the page accessed 16 November 2026.
- **Exact supporting passage:** The vendor says “Telenor chose Omada” and “Telenor built over 230 integrations to over 300 applications and various systems” and eliminated “hundreds of previously orphaned accounts.”
- **Source class / incentive:** IGA vendor customer case; Omada sells the product. The case names a Telenor IAM architect, but no independent report or methodology is attached.
- **Denominator/geography/period/method:** Telenor Norway; 230 integrations/300 applications are vendor-reported counts. Date, rollout duration, account denominator, validation method, and measured risk/security impact are absent.
- **Convergence boundary:** Supports a vendor-reported IGA implementation example; it does not establish AI, Zero Trust policy enforcement, or an integrated production control loop.
- **Status:** **Partially verified** as vendor-reported IGA use; **exclude** as evidence of AI+ZTA+IGA convergence or independent effectiveness.

### ZI-5 — NIST/3GPP/GCOT materials as production evidence
- **Exact proposed wording:** The outline uses NIST ZTA publications, 3GPP/GSMA material, GCOT principles, and Ericsson/SKT guidance to frame design roles and telecom context.
- **Primary sources:** [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final), August 2020; [NIST SP 1800-35](https://csrc.nist.gov/pubs/sp/1800/35/final), 10 June 2025; [GCOT 6G Security and Resilience Principles](https://www.gov.uk/government/publications/global-coalition-on-telecoms-security-and-resilience-principles-for-6g/gcot-security-and-resilience-principles-for-6g), 3 March 2026; 3GPP/GSMA documents in the research map.
- **Evidence classes:** NIST architecture and practice guidance (SP 1800-35 has lab/example implementations); GCOT government policy principles; 3GPP/GSMA standards/industry guidance; Ericsson vendor architecture guidance; SKT operator strategy paper. These do not establish an integrated, measured production system at a telecom operator.
- **Status:** **Verified** as design/guidance sources; **exclude** any conversion into operator deployment or security-effectiveness evidence.

## 8. Decisions for current synthesis and outline

1. **Check Point’s 94%/2,664 wording and rank are directly verified via the official WordPress REST API; qualify them as ThreatCloud AI telemetry.** Keep percentage growth (highest sector YoY increase) separate from weekly volume (third by volume); state that the telecom-only protected-organization denominator, attack definition, inclusion and deduplication methods are undisclosed. Do not call the measure a survey, census, or successful-incident count, or generalize it to sector-wide prevalence.
2. **Heavy Reading dates remain unresolved.** Report the explicit full-survey July/August 2025 fielding statement and the June 2025 source notes under Figures 11 and 19 side by side. Do not invent a figure-specific June sample explanation.
3. **Correct Sharlie’s maturity wording.** Orange’s March 2026 release calls the service launched/available; only the >3-million annual capacity remains prospective. Avoid treating capacity as actual volume.
4. **Keep the China Mobile/ZTE sources separate.** ZTE’s 2025 release supports event-specific supplier claims; the GSMA 83%/fivefold pilot page remains unverified; the TM Forum 30%/30% China Mobile statement has no accessible operator method/source.
5. **Do not use TELUS, BT release, GSMA 83%/5×, or extra Vodafone 30%/44% numbers as verified outcomes** until an accessible primary passage and method are obtained.
6. **ENISA’s 30 and 188 are distinct.** The 188 set is significant-in-2024 authority-reported security incidents, many service outages/system failures; its own geography count conflicts (26 vs 25 Member States). It is not a count of 188 cyberattacks.
7. **No opened incident source attributes AI to the named telecom events.** Keep the statement bounded to sources actually inspected; never turn it into “AI was not used.”
8. **UK law and Code are distinct.** The Regulations are in force with a micro-entity exemption; Code v1.1 is relevant guidance, tiered and legally consequential but not the only compliance route. The framework is not an AI-agent-specific rule.
9. **Keep AI+Zero Trust+IGA as a testable design hypothesis.** The current evidence is consulting opinion, government/standards/vendor guidance, TM Forum Catalysts/POCs and a separate vendor IGA case—not a measured integrated production control loop.
10. **Draft readiness:** not ready. The source/access gaps and operator validation requirements in `research/unresolved-evidence.md` affect central claims and should remain visible before any chapter drafting.
