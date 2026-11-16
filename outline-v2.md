# Proposed concept v2

> **Historical working outline — superseded 16 November 2026.** This ten-chapter concept is retained for reference only. The active architecture is `outline-v3.md`; do not use this file as authoritative for current drafting.

## Working title

**AI Security for Telecom CISOs: Separating Reality from Hype**

**Subtitle:** *Evidence, operational risk and decisions for networks that must keep running*

## Thesis and reader promise

Telecom’s AI story is not one technology arriving at once. Operators already use analytics, machine learning and automation in selected network and business workflows; generative AI and agents are being tested or introduced at uneven rates; fully autonomous, cross-domain networks remain a different claim. Security leaders need to separate what is in production from what is planned, what is measured from what is surveyed, and what an AI system can actually do from what a product description says. The decisive risk is often the operational connection among identities, data, tools, suppliers and network targets—not the model in isolation. Evidence that AI has been used against telecom operators is much thinner than evidence of serious telecom intrusions generally, so the book will not sell an AI-threat story the sources do not support. The reader will leave able to challenge market claims, map the consequential paths in their own estate, test controls against service conditions, and choose three or four defensible priorities for the next 12 months. Each priority will have a service outcome, owner, evidence gate, cost/dependency and a clear reason to change course.

## The reader's central questions

- What does “AI” mean in this particular product, workflow or network function?
- Which operator deployments are live, and what do the public results actually prove?
- How much of the current telecom threat picture is AI-enabled, and what is only conjecture?
- Where can an AI workflow obtain identity, data, tools or authority to affect a network service?
- Which telecom constraints change a standard enterprise security recommendation?
- When do Zero Trust, identity governance, segmentation and AI security fit together—and when is that only an architecture slide?
- What local evidence proves that a restriction, revocation, detector or fallback works at the target?
- Which legal obligations are binding in the operator's markets, and which are standards, proposals or guidance?
- What has improved: security, service quality, productivity, revenue, or only activity and adoption?
- What should the CISO fund, test, defer or stop, and what must be explained to the CEO and board?

## Proposed table of contents

### 1. The First Question Is: What Is Actually Deployed?
**Reader question:** When someone says “we use AI,” what does that mean in this workflow?

**Key argument:** Separate rule-based automation, predictive ML, generative assistants, tool-using agents and closed-loop control. Distinguish announcement, pilot, limited production and scaled production. A maturity label is not proof of value or safety.

**Evidence and telecom examples:** 3GPP’s account of AI/ML as an implementation choice and its continuing model-management work; the TM Forum and Heavy Reading surveys; Deutsche Telekom’s bounded production RAN Guardian example and One NZ’s operator-reported Network Concierge deployment and analysis-time claim; distinguish each company’s claim from independent validation. Use other customer-care, assurance and fraud examples only where operator-source evidence establishes deployment status.

**Practical payoff:** A one-page **AI claim card**: what system, what task, deployment stage, identity/action rights, source and date, metric/denominator, sponsor, and what is still unknown.

**Boundary:** Establishes evidence language and maturity distinctions. Chapter 2 maps use cases; this chapter does not rank them.

### 2. Where AI Is Changing Telecom Work
**Reader question:** Which operator workflows are changing first, and which reported benefits are credible?

**Key argument:** AI adoption differs by function. Customer service and analytics may scale differently from network-control actions. A survey saying “adopting” is not the same as a production system, and a faster task is not automatically a safer service or a lower total cost.

**Evidence and telecom examples:** Orange France’s deployed MAIA advisor tool and prospective Sharlie voice assistant; One NZ’s Network Concierge; Deutsche Telekom’s RAN Guardian; Airtel’s Ericsson Operations Engine case; SK Telecom’s AI-RAN commercial-network validation; TELUS’s customer-facing GenAI support; China Mobile/ZTE’s O&M pilot; Telefónica’s broad AI-use claims and NOA incident-analysis agent; BT’s Hiya-powered consumer call screening. Treat Orange Cyberdefense’s Qevlar SOC integration as a rollout claim, and keep public evidence gaps in internal fraud, coding and operator security operations explicit. Label supplier/vendor results, operator self-reports, pilots and validation stages; compare workflow-specific measures rather than forcing one adoption figure onto the sector [O1, O9, O11–O19, O22].

**Practical payoff:** A **use-case heat map** by production status, service impact, authority, benefit evidence and dependency.

**Boundary:** Answers where use is appearing and what is measured. Chapter 3 addresses adversaries; Chapter 4 addresses the internal security path.

### 3. AI in the Threat Picture: What We Know and What We Do Not
**Reader question:** Are attackers using AI against telecom operators, or is “AI threat” being added after the fact?

**Key argument:** Telecom espionage, credential theft and supply-chain compromise are serious without an AI label. Attribute AI use only when a primary source or well-supported investigation does so. Broader reports of AI-assisted phishing, coding or reconnaissance are relevant but not telecom incident evidence.

**Evidence and telecom examples:** Official telecom disclosures and advisories (including Singapore, the FBI/CISA PRC-linked U.S. telecom campaign and the Indonesian telecom backdoor advisory); ENISA’s separate 30-incident OSINT overview and 188 authority-submitted incident reports, which must not be treated as comparable counts; independently described campaigns such as Google’s GRIDTIDE investigation; separate model-provider and government reports on AI misuse, with explicit sector limits [O4–O7, O20, O21, O23].

**Practical payoff:** A **threat-claim ladder**: observed action, verified tool use, AI contribution, causal effect, telecom victim and operational impact—each requiring separate evidence.

**Boundary:** External adversary use only. Chapter 4 covers risk created by the operator's own AI-enabled workflows.

### 4. The New Internal Path: Identity, Data, Tools and Targets
**Reader question:** How can an AI feature move from information access to an operational action?

**Key argument:** The control problem follows the full chain: requester, agent identity, data source, connector/API, target system and downstream effect. A model's intended role or a “read-only” setting does not prove target enforcement.

**Evidence and telecom examples:** OSS/BSS, service inventory, alarms, network-management systems, RAN/core cloud APIs, contractor/vendor access and agent tool use; 3GPP/GSMA control work; peer-reviewed AgentDojo prompt-injection evaluation; O-RAN xApp access-control and misconfiguration research. Keep synthetic environments and testbeds distinct from carrier incidents or deployments [T19–T21].

**Practical payoff:** An **identity-to-target path map** with task, owner, read/write authority, connector, target-side denial, delegated credentials, sessions, logs, supplier access and stop path.

**Boundary:** Maps exposure and the architecture of authority. Chapter 5 explains why telecom operational conditions change the safe option; Chapter 7 verifies controls.

### 5. Why Telecom Changes the Security Answer
**Reader question:** Why can't a CISO simply apply a generic enterprise AI-control pattern to a carrier network?

**Key argument:** Telecom operations are multi-domain and service-coupled. OSS/BSS records, RAN and core functions, cloud-native network functions, edge, roaming, contractors, legacy platforms and supplier maintenance windows do not share one identity plane or one failure mode. Availability and recoverability are part of the security design.

**Evidence and telecom examples:** 3GPP architecture/security specifications, GSMA security material, operator disclosures, ENISA and national guidance; use concrete network-management and service-continuity dependencies, not generic “critical infrastructure” rhetoric.

**Practical payoff:** A **service dependency sketch** showing what can be changed, what view disappears if a control is stopped, what supplier must act, and which maintenance/change constraints are real.

**Boundary:** Explains telecom architecture and operating constraints, not the enterprise identity framework itself (Chapter 6) or incident command (Chapter 8).

### 6. Zero Trust, IGA and AI: Useful Pieces, Not a Magic Stack
**Reader question:** What does the advertised convergence of Zero Trust, identity governance and AI actually add?

**Key argument:** Zero Trust is an architectural approach to resource access; IGA governs identity lifecycle and entitlement decisions; AI may support analysis or orchestration. Combining the labels does not demonstrate that the target enforces policy, that non-human identities are governed, or that dynamic decisions are safe. Apply each control at the point where it changes a real risk.

**Evidence and telecom examples:** NIST SP 800-207 and SP 1800-35; 3GPP security and AI/ML management; GSMA guidance; the Protiviti article’s proposed architecture contrasted with TM Forum’s later agent-governance and access-management Catalysts (proofs of concept, not production outcomes) and Telenor’s vendor-reported standalone IGA case [M7, M9–M11, T2–T5]. Distinguish 5G standards-based authentication/control from enterprise-wide ZTA adoption.

**Practical payoff:** A **convergence test**: which identity is governed, which policy decision changes, where enforcement occurs, what evidence links request to target result, and what happens during revocation or control-plane failure.

**Boundary:** Explains design roles and limits. Chapter 7 tests whether a deployed control works; this is not a product-selection chapter.

### 7. Prove the Boundary Before You Trust It
**Reader question:** What evidence shows that a control denies a harmful action in the real workflow?

**Key argument:** Configuration, architecture diagrams, model evaluations, synthetic benchmarks, tabletop exercises and target observations are different evidence classes. A control is only proven for the identity, connector, target, version, path and conditions actually tested. Revoking a token may leave active sessions or queued actions; fallback must be independent and staffed.

**Evidence and telecom examples:** CISA agentic-AI guidance; NIST tool-use taxonomy; AgentDojo and O-RAN xApp studies as bounded benchmarks/testbeds; operator test or incident reports when publicly available; network-management and supplier paths with controlled test environments. A lab pass is not production proof.

**Practical payoff:** A **test-evidence record** with expected vs observed allowed/denied calls, target principal, logs, existing sessions, queued work, fallback and untested paths.

**Boundary:** Technical and operational assurance, not a general incident playbook. Chapter 8 applies verified controls in response and recovery.

### 8. When the Alarm Is Real: SOC/NOC Decisions and Service Continuity
**Reader question:** Can teams detect, decide and contain quickly without making service impact worse?

**Key argument:** Detection speed is not safe containment. A SOC or AI assistant may see a threat while the NOC sees an active change, and IAM or a supplier may hold a separate part of the response. Isolation may remove visibility or support needed to restore service. Response objectives must be service-specific and exercise-backed.

**Evidence and telecom examples:** Official incident timelines, national cyber guidance, operator continuity plans and carefully scoped cross-sector AI-threat-speed evidence. Do not turn a cross-sector attack time into a universal telecom response deadline.

**Practical payoff:** A **service-safe response rehearsal** covering decision authority, time to detect/decide/act/restore, NOC view, supplier support, alternate channels, fallback and recovery.

**Boundary:** Owns response and continuity under pressure. Chapter 7 owns proof of the underlying boundary, not the command model.

### 9. Rules, Suppliers and Sovereignty: What Is Binding, What Is a Choice?
**Reader question:** Which obligations apply to this operator and which requirements are guidance or market claims?

**Key argument:** Separate law in force, regulator rules, draft consultations, voluntary standards, industry guidance and vendor recommendations. Map requirements by service, data, entity, market and operator role. Supplier location, retention, support access, model change and exit terms create operational—not only privacy—dependencies.

**Evidence and telecom examples:** NIS2 national implementation, GDPR, EU AI Act role/classification rules, CIRCIA rulemaking status, FCC provider obligations and rescinded actions, UK Electronic Communications (Security Measures) Regulations and the distinct Code of Practice (updated to version 1.1 in July 2026), national telecom guidance, GSMA/3GPP standards, and TRAI proposals where applicable. Use a dated jurisdiction matrix; do not generalize one market’s law to all carriers [T6–T10, T22].

**Practical payoff:** A **binding-versus-voluntary obligations map** plus a supplier-change checklist tied to actual service paths.

**Boundary:** Identifies obligations and external dependencies. Chapter 10 makes the investment/board decision; this chapter does not prescribe a universal compliance program.

### 10. The CISO's Reality-Based Agenda
**Reader question:** What should leadership fund over the next 12 months, and what evidence will reopen the decision?

**Key argument:** Select a small portfolio from local evidence, not vendor roadmaps. Put security improvement, operational benefit, run cost, displaced work, supplier dependence and fallback into the same decision. Keep “delivered,” “tested,” “effective for this scope” and “risk accepted” distinct.

**Evidence and telecom examples:** Verified operator deployments and incidents from earlier chapters; survey and vendor claims only with their limits; operator-specific cost and change-window evidence gathered locally.

**Practical payoff:** A **three-or-four-priority board brief** with service, owner, decision requested, local evidence, cost/capacity, dependency, fallback, success measure and change trigger.

**Boundary:** Synthesis and prioritization only. It does not repeat the technical procedures from Chapters 4, 7 or 8.

## Narrative arc

Start by giving the executive a way to test claims, then show where AI is entering day-to-day telecom work. Raise the external-threat question without making AI the cause of every intrusion. Turn inward to identities and tools, then explain why carrier architecture and service continuity change the answer. Only after that does the book examine Zero Trust/IGA convergence and the evidence needed to trust a control. The response chapter turns those limits into operational choices; the law/supplier chapter explains which obligations and dependencies apply; the final chapter converts the evidence into a small, defensible investment agenda. The reader moves from “Is this real?” to “What can it affect?” to “What can I prove?” and finally “What should we decide?”

## Distinctive arguments

1. **Measure authority, not AI labels.** The security boundary is the identity-to-target path and the service action it can perform.
2. **Treat evidence type as part of the claim.** A survey, operator announcement, vendor telemetry, technical benchmark and incident disclosure answer different questions.
3. **Do not attribute a telecom incident to AI without evidence.** The absence of an AI label does not reduce the seriousness of the intrusion.
4. **A carrier's fallback is a security control.** If revocation removes the NOC's view or the supplier's repair path, a technically successful block may still fail the service.
5. **Zero Trust + IGA + AI is a hypothesis to validate.** It is neither a standard stack nor a demonstrated outcome by virtue of appearing together in a diagram.
6. **A productivity result is not a security result.** Reported speed, ticket volume or adoption does not prove less risk, lower net cost or better service quality.
7. **Network resilience is not a generic AI-governance add-on.** Change windows, domain dependencies, roaming, supplier support and legacy influence what safe authority looks like.

## Risks, open questions and reader objections

- **Evidence gap:** public operator disclosures often omit error, override, rollback, control-effectiveness and full-life cost measures. The book must not imply that what is not public is not deployed.
- **Operator validation needed:** interview telecom CISOs, NOC leaders, network engineers, identity teams, procurement/legal specialists and operators from different regions before final recommendations. Public case reports cannot validate local processes.
- **Fast-aging material:** model/agent capabilities, 3GPP/6G work, rules, CIRCIA/FCC developments and vendor releases need a dated evidence refresh before publication.
- **Attribution risk:** provider threat reports observe their own ecosystem and investigations; state confidence and alternative explanations.
- **Survey risk:** ask for field dates, population, respondent role, country, question wording, item denominator, sponsorship and whether “deployed” means any or scaled use.
- **Potential objection — “We have used AI in networks for years.”** Agree, then distinguish classical optimization from new tool access, broad language-model interfaces and delegated actions.
- **Potential objection — “Zero Trust is already our strategy.”** Ask which target enforces each policy, how service identities are governed, and what happens to active or queued work after revocation.
- **Potential objection — “Our vendor already tested it.”** Ask what identity, connector, target version, action path and operating condition the test covered.
- **Potential objection — “We need ROI before security work.”** Include actual operating benefit, displaced work, risk reduction and service consequences together; do not invent a monetary figure to make the case.

**Confidence assessment:** medium that this concept can be evidence-led and materially different from generic AI-security books; low-to-medium on the breadth of publicly provable AI-enabled threat activity against telecom operators and on sector-wide ROI. The architecture is ready for research iteration, not for final claims. Operator interviews and source-level denominator checks remain essential.
