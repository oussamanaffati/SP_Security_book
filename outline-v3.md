# Outline v3 — Working six-chapter architecture

**Status:** Active working outline, created 16 November 2026. It supersedes the ten-chapter concept in `outline-v2.md`, which is retained as historical material. The six-chapter decision sequence follows `research/outline-red-team-review.md`; Chapter 1 uses the title of the completed pilot.

**Working title:** *Service Provider Security in the AI Era*
**Subtitle:** *A Practical Guide to AI, Agents, and Service Continuity for Telecom CISOs and CTOs*

## Reader promise

A telecom CISO or CTO should finish able to choose three or four priorities for the next 12 months and explain them credibly to the CEO and board. The case for each priority should name the service at stake, the accountable owner, the evidence gate, dependencies and costs, fallback, residual risk, and the conditions that would change the decision.

## Central argument

The market uses “AI” to describe very different capabilities and stages. A claim about deployment, productivity, service quality, security effectiveness or return on investment is only useful when its workflow, authority, evidence and measurement are clear. For security, follow the path from identity and data through tools and APIs to the network target and service consequence. Then test whether controls and response preserve the ability to operate and recover. Public evidence supports bounded examples and technical mechanisms, not sector-wide adoption, causal ROI, or an AI-driven telecom attack wave. The book must keep that distinction visible.

## The six decisions

### 1. What Is Actually Deployed?

**Reader question:** When someone says “we use AI,” what is live in this workflow, what can it do, and what does the evidence establish?

**Argument:** Deployment stage, action authority, source type and outcome are separate dimensions. Use a small set of contrasting operator workflows to show how a production action, a recommendation, conversation volume and a commercial-network validation answer different questions. Do not turn one production case into a market-wide maturity claim.

**Evidence boundary:** Use attributed primary operator statements and distinguish them from vendor claims, surveys, telemetry and validation. Keep activity, productivity, service quality, security and ROI separate. The Heavy Reading field-date mismatch and operator metric gaps do not control the chapter’s argument.

**Reader payoff:** A compact claim card for deciding what to inventory, what to believe and what evidence to request.

**Boundary:** Establishes the evidence vocabulary and the local inventory question. It does not map the full attack surface or set sector-wide adoption rates.

### 2. Telecom Threats Without the AI Hype

**Reader question:** What is established about attacks on telecom, and what does the public record actually say about AI’s contribution?

**Argument:** Telecom intrusions deserve serious preparation without an AI label. Attribute a role to AI only when the incident source or a supported investigation establishes it. Explain the difference between an observed intrusion, reported use of an AI tool, evidence that AI contributed to a particular step, and proof of a resulting operational effect. Broader cross-sector threat reporting can inform questions, not supply a telecom incident count or response deadline.

**Evidence boundary:** Begin with readable government disclosures and keep each incident’s scope and attribution intact. Treat the 30-incident ENISA OSINT overview and the separate 188 authority-submitted incident reports as different datasets; omit the disputed Member-State count. Keep vendor threat intelligence and model-provider reports explicitly labelled. Keep this chapter short if the primary evidence remains sparse.

**Reader payoff:** A threat-claim ladder and a decision about which observed techniques merit preparation now, without guessing at AI attribution.

**Boundary:** External adversary activity only. Chapter 3 addresses authority created by the operator’s own tools and identities.

### 3. Follow Authority to the Network Target

**Reader question:** Through which identity, data source, connector and target could an AI-enabled workflow affect a service?

**Argument:** Treat the whole workflow as the unit of review. Follow requester and identity, delegated credentials, retrieved data, connector/API calls, target-side authorization and resulting network state. Distinguish reading, summarizing, recommending, drafting a change, approved execution and autonomous action. Zero Trust, identity governance and AI have different jobs; their appearance together in an architecture proposal is not proof of an integrated control loop.

**Evidence boundary:** Use CISA guidance and AgentDojo/O-RAN research for the mechanisms and test questions they actually support. Label simulation, lab and testbed results. Do not imply that a named operator agent has an unverified path into OSS/BSS, RAN, core, cloud or supplier systems. Use the supplied composites as clearly illustrative exercises, not observed incidents.

**Reader payoff:** An identity-to-target map showing the principal, owner, effective permission, data and connector, write path, target enforcement, service effect and stop path.

**Boundary:** Maps exposure and authority. Chapter 4 tests controls and makes response/recovery decisions; it does not repeat the architecture map.

### 4. Prove Safe Authority and Service-Safe Response

**Reader question:** What evidence shows that a harmful action is blocked at the target, and can the operator contain and restore safely when the boundary is tested?

**Argument:** Architecture review, benchmark, lab test, exercise and production observation are different evidence. Test the actual identity-to-target path, including allowed and prohibited calls, logs, delegated sessions, queued work, stop/revoke behavior, rollback and fallback. Then exercise the SOC/NOC/service-owner decisions and recovery path under stated assumptions. A passed test establishes only what its scope and conditions cover; it does not establish universal safety.

**Evidence boundary:** Use guidance and bounded technical studies to design tests, not to claim operator-wide effectiveness. The supplied edge/core account, supplier diagnostic feature, NOC assistant and deferred patch-window composites may frame questions, clearly labelled as illustrative. Do not present any as a real incident, operator practice or test result.

**Reader payoff:** A test record plus a service-safe response rehearsal that separates expected evidence, observed results, untested paths, decision authority and restoration conditions.

**Boundary:** Chapter 3 maps where authority can reach. Chapter 4 establishes what was tested and who decides to enable, narrow, revoke or defer it.

### 5. Obligations, Suppliers and Exit Conditions

**Reader question:** Which binding duties apply to this operator, and which supplier or platform dependencies could impair service, evidence or exit?

**Argument:** Map obligations by jurisdiction, entity, service and role. Separate law in force from regulatory guidance, standards, proposals and vendor advice. Follow supplier dependencies beyond data location: model and connector changes, cloud availability, support access, updates, evidence rights, subcontractors, portability and recovery. A supplier’s location or “sovereign” label does not by itself establish control or resilience.

**Evidence boundary:** Use dated official legal and regulator sources for named jurisdictions, with counsel review for applicability. Keep CIRCIA and FCC status date-specific; do not generalize one market’s rule to all operators. Supplier cases establish only the reported architecture or dependency, not comparative resilience, cost or exit outcomes.

**Reader payoff:** A dated obligations-and-dependencies map connected to service paths, contract decisions and a tested exit or continuity condition.

**Boundary:** Establishes external constraints and dependencies. Chapter 6 turns local evidence into an investment and oversight agenda rather than repeating compliance controls.

### 6. The Next 12 Months: A Defensible Operator Agenda

**Reader question:** Which three or four priorities should leadership fund, test, defer or stop, and what evidence would change each decision?

**Argument:** Select from local service, threat, authority, test and dependency evidence, not from vendor roadmaps or market percentages. For each priority, put the service outcome, accountable management owner, evidence gate, capacity and full-life cost, supplier dependency, fallback, residual risk and reassessment trigger in the same decision. Management owns execution and accepts residual risk only within delegated authority and approved appetite; the board oversees appetite, resources, escalation and assurance.

**Evidence boundary:** This is a synthesis of preceding chapters, not a new claim that every operator should choose the same priorities. Use local cost, change-window and service evidence; leave unavailable figures unknown rather than inventing values.

**Reader payoff:** A concise CEO/board decision brief with three or four defensible priorities, owners, evidence gates and triggers.

**Boundary:** Converts earlier evidence into decisions. It does not repeat the detailed test procedure, legal map or incident playbook.

## Narrative arc and chapter boundaries

The reader first learns to separate deployment claims from evidence. Then the book refuses to infer AI causation from serious telecom incidents. With that distinction established, the reader follows authority to the network target, tests whether the boundary works, and asks whether the operator can respond and recover without losing service. Jurisdiction and suppliers enter as concrete limits on operation and exit. The ending converts local evidence into a small, defensible agenda.

The former separate workflow heat map, telecom-complexity survey and Zero Trust/IGA chapter are not standalone chapters. Their useful decisions are folded into Chapters 1, 3, 4 and 5. Do not expand Chapter 2 with generic AI-threat material to make it the same length as the others. Chapter lengths follow the evidence and the decision each chapter must support.

## Evidence and editorial guardrails

- Attribute company and supplier claims; never imply independent validation unless the evidence is independent.
- Do not infer AI use or non-use from an incident disclosure that does not mention AI.
- Keep adoption, productivity, service quality, security effectiveness, revenue and ROI distinct.
- Treat unresolved Heavy Reading and ENISA discrepancies as unresolved; omit disputed numbers where they do not help a decision.
- Do not use unsupported operator performance percentages, unitemized adoption totals or inaccessible-source claims as headline evidence.
- Use only the four existing composites when an operational example is useful, label them as illustrative, and do not invent additional incident details, tests, outcomes, quotations, costs or operator practices.
- Keep source IDs, exact support and claim mappings in the research files; keep chapter prose free of reader-facing Sources sections and citation clutter.
- Treat broad identity-to-network paths and cross-operator practices as questions to validate locally unless the sources establish them.
