# Trend synthesis: AI security in telecommunications

**Cut-off:** 16 November 2026. This synthesis separates observed operator activity from announced plans, vendor telemetry, surveys, technical benchmarks and recommendations. It does not treat an incident as AI-enabled unless the source says so. Source codes below resolve to original links and limits in [`research-map.md`](research-map.md).

## Ten trends

### 1. AI in network operations is real; its maturity is uneven
**What is changing.** Operators used AI/ML and automation in network management before the current agent wave; 3GPP describes this as implementation practice, not one standard model [T1]. Public sources report different stages and tasks: Deutsche Telekom says RAN Guardian is live in production in Germany; One NZ says it deployed Network Concierge for complaint analysis and separately used generator-placement guidance; Telefónica Germany says NOA was developed and connected to operational data/ticketing, without publishing production scale or outcomes; SK Telecom says its recommender was applied and validated on a commercial network while real-time application remained future work [O1, O9, O12, O18]. Orange’s MAIA and Sharlie are customer-service tools, BT/Hiya is consumer call screening, and Orange Cyberdefense/Qevlar is a gradual integration announcement; none is evidence of internal telecom-security efficacy [O13–O15]. MINDR was still an MVP plan in the 5 October 2026 transcript [O10]. The unitemized Telefónica count, supplier-case metrics, event-pilot percentages, call-volume totals and TELUS search figures are not used as cross-operator productivity, service-quality or security outcomes [O11, O16–O19]. Heavy Reading surveyed 84 individuals, not 84 operators; its autonomy and deployment-plan results are respondent self-report/intention. The report says fieldwork was July/August 2025, while Figures 11 and 19 cite June 2025, and does not reconcile the notes [M1]. TM Forum’s separate 2026 survey covered 125 people at 80 companies [O3].

**Evidence and confidence: medium.** There is clear evidence of established use and varied self-reported maturity, but not a robust global census. Survey samples, wording and definitions differ; many figures are intention or self-assessment, not deployment telemetry.

**Counter-evidence / hype.** “AI is already everywhere” collapses rules, analytics, ML, GenAI, agents and closed-loop control into one label. Telefónica’s unitemized company count is not a deployment census; planned integrations are not production. The Orange/Sharlie annual capacity is prospective, not observed usage. Airtel and China Mobile/ZTE case metrics lack the baseline, period or definitions needed for comparison; they are excluded from headline outcome claims. BT’s aggregate blocked/identified call totals are service telemetry, not a false-positive or loss-prevention rate. Vodafone/JT/FICO describes algorithms and mobile intelligence for bank fraud, not an AI method or internal telco security deployment [O11, O13, O16–O19].

**CISO decision.** Require each business owner to name the workflow, deployment stage and authority, rather than count “AI use cases.”

**Collect locally.** System inventory; production/test status; human approval points; target systems; changes actually executed; operator overrides; service impact; evidence period and baseline.

### 2. Agentic network operations have reached bounded production, not universal autonomy
**What is changing.** Deutsche Telekom says RAN Guardian is live in production in Germany and reports 100+ autonomous remediation actions in its first month and event-management time falling from hours to around a minute [O1]. An October 2026 transcript gives a different “live since January” milestone and additional event-scale/avoided-minutes claims without methods; the dates and measures are not reconciled. One NZ says it deployed Network Concierge; its 80% analysis-time figure lacks case count, baseline and quality measure, so it is not used as a comparable productivity result. Its separate generator-placement tool provided decision guidance during storms/outages; the release does not establish network-state control or a resilience outcome [O9]. Google Cloud’s One NZ VoLTE-agent page uses both “has deployed” and “is deploying”; current retrieval timed out and the browser page errored, so stage remains unresolved [O2]. The 5 October DT transcript describes MINDR as an MVP “about to go live,” with a year-end first-use-case plan; its live walkthrough is explicitly a demo and its numbers are targets, not results [O10]. GSMA directly labels China Mobile/ZTE an O&M pilot; its 83%/fivefold values have no baseline or method. ZTE’s separate release reports deployments at named events, but its 30% staffing and 20% traffic figures concern different events and do not establish routine production or security outcomes [O19]. These pilot/supplier numbers are omitted from the headline synthesis.

**Evidence and confidence: medium for named, bounded company-reported deployments; low for prevalence, causal benefit and safety outcomes.** DT is the clearest production control case in this set; One NZ reports a deployed information-aggregation agent and separate generator-placement guidance. The sources do not establish One NZ network-state changes. Neither operator publishes a complete baseline, sample, error/override rates or independent service-quality comparison. No case establishes network-wide autonomy or security-risk reduction.

**Counter-evidence / hype.** TM Forum says fully realized zero-touch operations remain out of reach for most CSPs because they require mature data, cross-domain orchestration and willingness to delegate real-time control [O3]. “Self-healing network” is an aspiration, not a uniform production state.

**CISO decision.** Decide which low-blast-radius actions can be delegated, and what would revoke that authority.

**Collect locally.** Action type, policy/parameter envelope, service domain, approval/override rate, failed actions, rollback, customer/service impact, independent evidence and recovery procedure.

### 3. Adoption and ROI statistics are not interchangeable
**What is changing.** Vendor and analyst research increasingly quantifies AI adoption, investment and expected value. Heavy Reading’s 2025 survey was produced for Amdocs and RADCOM; NVIDIA’s 2026 landing page describes a survey of 1,000+ telecom professionals [M1, M3]. TM Forum’s 2026 interim survey of 78 validated operator respondents reports that 62% can easily link autonomous-network improvements to operational benefits, while 37% can link those benefits to financial outcomes; results may change before final publication [M4].

**Evidence and confidence: medium for what respondents said; low for market-wide deployment or realized ROI.** The survey bases, sponsorships and question denominators differ; none is established here as a representative census of all telecom operators. The 62%/37% figures are survey responses, not audited savings or causally measured performance.

**Counter-evidence / hype.** A percentage saying “adopting,” “assessing” or “planning” does not reveal the number in production, scope, use frequency, quality, net cost or risk reduction. “ROI” may mean expected or reported value, not independently measured causality.

**CISO decision.** Do not make a portfolio decision from industry adoption percentages. Require a local baseline and a benefit measure that includes review, correction, integration, supplier and run costs.

**Collect locally.** Exact denominator; task completion and quality; time-to-accepted result; human review/rework; incident/security outcome; recurring compute and license cost; displaced work; comparison group or credible before/after method.

### 4. The most concrete new security surface is delegated authority
**What is changing.** An agent can combine an identity, retrieved data, connectors, APIs, tools and downstream targets into one workflow. A familiar model may therefore acquire authority through service accounts, inherited permissions or supplier connectors. CISA’s multi-agency 2026 guide identifies expanded attack surface, privilege creep, misalignment and opaque event records as risks and recommends narrow, low-risk starts [O8].

**Evidence and confidence: high for the architectural risk; low for how often it is exploited in telcos.** CISA guidance and the peer-reviewed AgentDojo benchmark support tool-use and indirect prompt-injection failure mechanisms; public telecom incident data do not quantify agent-specific incidents [O8, T19]. A network-operations benchmark reports unsafe tool actions in synthetic scenarios, but that is not a carrier incident rate [T13].

**Counter-evidence / hype.** “Agentic” is not a risk score. Read-only summaries and agents allowed to change network state are different. Model evaluation alone cannot establish target-side permission enforcement.

**CISO decision.** Treat identity-to-target reach and revocation as the unit of review, not the AI product name.

**Collect locally.** Principal/owner, effective permissions, delegated tokens, tool versions, target enforcement, write path, current sessions/queued work, logs linking request to result, supplier access, disablement and fallback.

### 5. Telecoms face serious cyber operations, but AI attribution is sparse
**What is changing.** Official and threat-research sources describe espionage, credential theft and access to telecom infrastructure. Singapore disclosed attacks against four operators; FBI/CISA detailed call-record theft, compromise of a limited number of private communications and copying of court-order law-enforcement data in a U.S. campaign; Google reported a global espionage campaign affecting 53 victims in 42 countries across sectors [O4, O6, O7, O23]. A separate IMDA backdoor advisory could not be read in this audit, so its previously recorded Indonesian-telecom claim is not used here as verified evidence [O5]. ENISA’s 30-incident figure is from its 2024 OSINT collection; the separate 188-report dataset aggregates significant telecom incidents submitted by national authorities under the EU reporting framework and includes service outages/system failures as well as malicious actions. The documents describe different reporting scopes and collection routes; these counts are not comparable incident rates or a sector-wide census [O20, O21]. The named incident sources reviewed here do not establish AI use in those events.

**Evidence and confidence: high that telecoms face sustained intrusion activity; low that AI is a demonstrated cause of telecom incidents.** Official disclosures and technical threat-intelligence investigations are direct evidence of intrusion activity, but differ in public detail and attribution. The lack of AI attribution in these named reports is not proof AI was never used; it is not evidence AI was used either. The blocked IMDA advisory is an additional gap, not a basis for either conclusion.

**Counter-evidence / hype.** Google and Anthropic report threat actors using AI tools across broader campaigns, but those providers’ telemetry is not telecom-specific [T14, T15]. A cross-sector government bulletin reports under-three-hour progress in some cloud intrusions; that is neither a telco incident nor an operator response deadline [T11].

**CISO decision.** Prepare for the observed techniques and operational exposure; do not prioritize a threat scenario solely because an AI label is attached.

**Collect locally.** Identity and privileged-session anomalies; supplier/contractor paths; edge and web-server exposure; credential use; tool execution; incident attribution confidence; evidence that establishes whether AI was used.

### 6. “AI + Zero Trust + IGA” is a design hypothesis, not an evidenced telco outcome
**What is changing.** Consulting and vendor material increasingly presents Zero Trust, identity governance and AI as a converged architecture. NIST’s ZTA publications provide architecture concepts and implementation examples; 3GPP and GSMA address network security, AI/ML management and responsible-AI practice [T2–T5]. GCOT’s seven-government 6G principles recommend function-level Zero Trust; Ericsson publishes MNO-specific ZTA guidance; SK Telecom’s 2026 paper presents a future 6G Zero Trust vision [T16–T18]. TM Forum’s August 2026 Catalysts add proof-of-concept patterns: one applies Identity, Policy, Observability and Evidence to agent governance; another proposes an AI compliance agent that drafts access-policy changes for dry-run and human approval through a digital-identity layer [M9, M10]. These are design, Catalyst and demo claims, not evidence that the combined controls operate as a measured production loop. A vendor case on Telenor documents an IGA selection separately, not AI+Zero Trust+IGA integration [M11].

**Evidence and confidence: high that the reference article is a proposal; low for prevalence or measured benefit of the integrated architecture.** Protiviti names no operator implementation or outcome. The later TM Forum Catalysts are explicitly proof-of-concept work, not measured production outcomes. Omada’s Telenor example is vendor-reported IGA, a separate component, not proof of AI+Zero Trust integration. The Q1 Check Point report body is now directly verified through its official WordPress API: it identifies ThreatCloud telemetry, 94% as the highest YoY percentage increase, and 2,664 as telecom’s third-place weekly volume. The telecom protected-network denominator and attack definition remain undisclosed; Protiviti calls the data a survey and misstates the growth rank (see article audit).

**Counter-evidence / hype.** The three labels do not guarantee clean identity inventory, lifecycle control, policy accuracy, target enforcement, useful telemetry or safe automated response. Dynamic risk scores may create another unvalidated policy dependency.

**CISO decision.** Ask which access decision is improved, at which target, by what evidence, and how the system behaves when identity/data/context is wrong.

**Collect locally.** Joiner/mover/leaver coverage for human and non-human identities; privilege recertification completion; orphaned service accounts; policy decision logs; denied-write tests; downstream revocation; segmentation bypasses; false positives and service impact.

### 7. Telecom architecture makes generic enterprise recipes incomplete
**What is changing.** AI workflows increasingly cross OSS/BSS, cloud and data platforms, network-management systems, RAN/core domains, edge sites, suppliers and multi-market operations. 3GPP’s AI/ML work explicitly emphasizes operator control, model management and data-transfer mechanisms; TM Forum reports cross-domain data and autonomy as a major transformation challenge [T1, O3].

**Evidence and confidence: medium-high for the architecture/operating constraint; less evidence for a uniform industry maturity level.** Standards documents, operator surveys and peer-reviewed O-RAN testbed studies establish complexity and plausible access-control/misconfiguration failure paths, but not the prevalence of those failures in live carrier networks [T20, T21].

**Counter-evidence / hype.** “Autonomous network” is not a single architecture or an upgradeable feature. An enterprise ZTNA product does not by itself secure service-based interfaces, RAN control, roaming, lawful-intercept dependencies or field-engineer access.

**CISO decision.** Decide which network domains and operational functions are in scope, and where the authoritative identity and service state live.

**Collect locally.** OSS/BSS dependency map; service-based API inventory; network-function and supplier identities; roaming/IPX/trust boundaries; cloud/edge data routes; legacy limitations; maintenance windows; fallback services and jurisdictional ownership.

### 8. Supplier, model and platform dependence is an operational risk, not only a data issue
**What is changing.** Operator workflows depend on model providers, cloud platforms, connectors, telemetry and supplier support. GSMA’s responsible-AI and agentic-AI work highlights governance and supply-chain concerns; CISA guidance recommends managing third-party tools and permissions [T4, T5, O8]. Operator reports now include deployments built with Google Cloud and Amazon Bedrock, as well as supplier-developed frameworks described as still deploying [O1, O2, O9].

**Evidence and confidence: medium for the dependency pattern; low for comparative cost, portability and incident rates.** Guidance and announced architectures establish dependence, not the realized exit cost or resilience of each deployment.

**Counter-evidence / hype.** “Sovereign,” “private” or “operator-hosted” does not automatically remove supplier access, update, telemetry, hardware or support dependencies. A model switch may not preserve tool behavior or service performance.

**CISO decision.** Determine which supplier changes require notice and retesting, and what service remains possible if the model, connector or cloud path is unavailable.

**Collect locally.** Provider/subprocessor list; processing location; prompts/output/traces retention; model and connector update path; identity and remote support; outage/fallback; portability; license/token/compute cost; deletion and exit evidence.

### 9. Control effectiveness needs target and operational evidence
**What is changing.** Guidance increasingly calls for tool allowlists, least privilege, logging, human approval, evaluation and prompt-injection testing. NIST’s tool-use workshop emphasizes action, permissions, reversibility, observability and autonomy; CISA warns that agent evaluations remain immature and scenario-dependent [T12, O8].

**Evidence and confidence: high for the need to distinguish evidence types; low for universal control-effectiveness rates.** A policy/configuration review, synthetic benchmark, tabletop and production observation answer different questions. NetInjectBench is a preprint, bounded to its scenarios/models/assumptions [T13].

**Counter-evidence / hype.** “Passed the benchmark,” prompt filtering, a green dashboard or a successful simulation does not prove a connector or target rejects a prohibited action, ends active sessions, stops queued work or preserves the NOC view.

**CISO decision.** Approve the narrowest safe validation that tests the actual identity-to-target path; withhold action authority when the path cannot be verified.

**Collect locally.** Exact principal, connector, policy and target version; allowed/denied calls; active and queued work; attributable logs; stop/revoke behavior; rollback; independent monitoring; staffed fallback; expected vs observed evidence.

### 10. The business case is a service-and-capacity decision
**What is changing.** Operators report bounded operational benefits, but the most visible figures are company-reported: DT’s event-handling claim and One NZ’s complaint-analysis claim lack published baselines and methods. Surveys show investment interest alongside difficulty linking operational change to financial results [O1, O9, M1, M4].

**Evidence and confidence: medium for attributed examples; low for generalized or causal ROI.** DT’s event-time statement and One NZ’s 80% analysis-time statement remain in the ledger as operator-reported claims, not comparable productivity findings: neither publishes the relevant denominator, baseline, measurement period, error/override rates or independent comparison. The One NZ figure is omitted from headline synthesis. Surveys are respondent opinion. None of these claims establishes security-risk reduction or net savings across operators.

**Counter-evidence / hype.** Faster action or more automated tasks may shift rather than remove work: review, exception handling, integration, training, monitoring, supplier support, and fallback all consume capacity. “AI productivity” is not established by tokens processed, tickets touched or an advertised MTTR change.

**CISO decision.** Fund only a use case with an explicit service outcome, local baseline, risk condition, full-life cost and a credible stop/exit path.

**Collect locally.** Task quality, end-to-end time, human corrections, affected service, safety/error rate, run and transition costs, supplier dependence, staff backfill, portability, and before/after method.

## Field-level synthesis

### Three trends with the strongest operator evidence

1. **Telecom intrusion is real and technically consequential.** Readable government disclosures describe Singapore telco targeting and PRC-linked access to U.S. telecom networks; neither attributes AI. The IMDA Indonesian-backdoor advisory could not be read through either official PDF route, so its incident details and AI attribution remain unresolved and should be omitted. Google’s GRIDTIDE report is vendor, cross-sector evidence with no telco-only denominator; broader AI-misuse reports are cross-sector, not telco incident attribution. ENISA’s OSINT and authority-submitted datasets have separate scope [O4–O7, O20, O21, O23].
2. **AI/ML and automation support bounded network workflows, not proven sector-wide autonomy.** 3GPP describes existing use; the strongest direct cases are DT RAN Guardian’s company-reported production remediation, One NZ’s reported deployment of an information tool, and SKT’s commercial-network recommender validation [T1, O1, O9, O18]. Airtel and China Mobile/ZTE performance percentages are excluded from headline evidence because their case-study methods are absent. These examples do not establish security-risk reduction.
3. **Operational autonomy is a stated operator priority, but measurement is immature.** Multi-company surveys show investment interest and priority use cases; interim TM Forum data reports a weaker link from operational to financial outcomes [O3, M1, M4]. This is evidence of strategy and measurement gaps, not realized industry-wide ROI.

### Three trends with the most vendor attention relative to demonstrated operator evidence

1. **Level 4/5 “self-healing” or zero-touch networks across domains.** There is a live bounded RAN example and multiple plans; public evidence of network-wide autonomous production with audited error, rollback and customer-impact measures is sparse [O1–O3, M6].
2. **Multi-agent orchestration as the default telecom operating model.** 3GPP and TM Forum discuss protocols and agentic architectures; operator-ready security, safety and interoperability outcomes remain unsettled [T1, O3, T5].
3. **AI dynamically unifying Zero Trust and IGA into a continuously optimized security architecture.** Consulting/vendor commentary is stronger than named operator outcomes or independent measurements. Protiviti illustrates the proposal; TM Forum’s 2026 Catalysts add proof-of-concept demonstrations, not production evidence; Telenor’s vendor-reported IGA case remains a separate component example [M7, M9–M11, T2–T5].

### Under-discussed risks

- Downstream sessions, delegated credentials and queued actions can outlive an upstream “pause” or token revocation.
- Containment may remove the very alarms, telemetry or supplier support needed to keep the network running.
- A connector’s log can show a request without showing the target’s final state; simulation and tabletop results are not target enforcement.
- Model, tool, connector, prompt, data-retention and supplier-access changes may alter behavior without a new product name.
- Network operations need to distinguish stale/missing data from “no fault”; cross-domain joins can create a confident but wrong service picture.
- Staffing, shift coverage, cost-to-run, token/compute use, energy, exit and portability are less visible than adoption headlines.
- 5G/6G standardization work is often described as an operational deployment; specification work, trials and production use need separate labels.

### Claims too weak for a confident conclusion

- A general proportion of telecom operators using AI in production, given inconsistent populations and “adopting/assessing/deploying” definitions.
- A reliable public estimate of production use by specific function (especially internal SOC/security operations, coding and fraud/risk work); current public cases are sparse, often provider- or vendor-reported, and do not establish sector-wide use.
- A causal estimate of AI’s net ROI, security-risk reduction or change in service quality across carriers.
- The frequency of AI-assisted or AI-autonomous attacks against telecom operators.
- Comparative effectiveness of agent-specific controls, Zero Trust, IGA or model guardrails in live carrier networks.
- Whether a successful benchmark or lab test predicts behavior under carrier-scale dependencies, degraded telemetry, concurrent incidents or supplier outages.
- Whether high-risk AI law classifications and new reporting regimes apply to a specific operator use; legal status and scope are market- and role-specific.

### Regulatory boundary

The UK’s Electronic Communications (Security Measures) Regulations are binding on providers within their public-network/service scope, subject to the statutory micro-entity exemption. The related Code v1.1, issued 14 July 2026, is official guidance with tiering and legal relevance, but is not itself the Regulations or the only compliance route; Tier 3 providers are not expected to follow Code measures but remain subject to statutory duties unless exempt. EU NIS2, GDPR and the AI Act are binding instruments with entity-, role- and scope-specific application; NIST, CISA, GSMA, 3GPP and GCOT materials have distinct voluntary, standards or policy status. None should be paraphrased as a universal AI-agent control mandate [T2, T6, T8, T10, T16, T22].

This synthesis should guide the next research pass, not close it. The highest-value follow-up is operator validation of deployment scope, control behavior and business results, especially for systems said to be in production.
