---
title: "Chapter 19 — Evaluation and Monitoring (Agentic Design Patterns)"
type: source
tags: [agentic-design-patterns, agents, evaluation, monitoring, observability, llm-as-judge, trajectory, ab-testing]
date: 2025-06-01
source_file: raw/books/agentic-design-patterns.pdf
sources: [agentic-design-patterns]
---

## Summary
Chapter 19 of [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (Agentic Design Patterns, PDF pp 306–324) presents the **Evaluation and Monitoring** pattern — the continuous, often external measurement of an agent's effectiveness, efficiency, and compliance in operational environments. It moves from naive accuracy checks to richer metrics (semantic similarity, [[LLMAsAJudge|LLM-as-a-Judge]], [[RAGEvaluation|RAG metrics]]), production telemetry (latency, cost, token usage), and **[[AgentTrajectoryEvaluation|trajectory evaluation]]** of single- and multi-agent systems, closing with the **"[[AIContract|contractor]]"** evolution and [[GoogleADK|Google ADK]]'s evaluation tooling.

## Key Claims
- Agents are probabilistic/non-deterministic, so **traditional software testing is insufficient**; continuous post-deployment assessment is required to catch drift, faulty tool calls, and goal deviation.
- Evaluation must assess **both the final output and the trajectory** (sequence of steps/tool selections), comparing actual actions against an ideal ground-truth path.
- Naive exact-string-match accuracy fails on paraphrase (it scores *"The capital of France is Paris."* vs *"Paris is the capital of France."* as 0.0); real evaluation needs string-similarity, keyword, semantic (cosine/embedding), LLM-as-judge, and RAG-specific metrics.
- Latency and token usage must be logged to persistent stores (time-series DBs, data warehouses, observability platforms), not printed; token tracking is essential for LLM cost management.
- **LLM-as-a-Judge** enables nuanced, scalable scoring of subjective qualities (e.g. "helpfulness") via a rubric; the worked example scores legal survey questions 1–5 across five criteria, returning structured JSON.
- Three evaluation methods trade off: human eval (subtle but unscalable), LLM-as-judge (scalable but may miss intermediate steps), automated metrics (objective but incomplete).
- Multi-agent evaluation = assessing a team: cooperation, plan adherence, right-agent-for-task, and scalability when adding agents.
- The **AI "Contract"/contractor** model (Agent Companion, Gulli et al.) — Formalized Contract, negotiation lifecycle, quality-focused iterative self-validation, hierarchical subcontracts — moves agents from brittle/probabilistic to accountable/verifiable for high-stakes domains.
- [[GoogleADK|Google ADK]] supports evaluation via `adk web` (interactive), `pytest` + `AgentEvaluator.evaluate` (CI/CD), and `adk eval` (CLI), using **test files** (unit) and **evalset files** (integration).

## Key Quotes
> "Evaluating agents' trajectories is essential, as traditional software tests are insufficient. Standard code yields predictable pass/fail results, whereas agents operate probabilistically, necessitating qualitative assessment of both the final output and the agent's trajectory—the sequence of steps taken to reach a solution." — Ch 19, "Agents trajectories"

> "An evolution from simple AI agents to advanced 'contractors', moving from probabilistic, often unreliable systems to more deterministic and accountable ones designed for complex, high-stakes environments." — Ch 19, "From Agents to Advanced Contractors"

> "This contract explicitly defines the required deliverables, their precise specifications, the acceptable data sources, the scope of work, and even the expected computational cost and completion time, making the outcome objectively verifiable." — Ch 19, Formalized Contract pillar

## Connections
- [[EvaluationAndMonitoring]] — the named pattern (PRIMARY concept page created from this source).
- [[AgentTrajectoryEvaluation]] — trajectory/tool-use comparison + multi-agent evaluation (created).
- [[AIContract]] — the contractor evolution / Agent Companion model (created).
- [[AgenticDesignPatterns]] — the book hub; this is the 19th of 21 patterns.
- [[GoalSettingAndMonitoring]] — Ch 11; the internal self-management loop Ch 19 explicitly distinguishes from.
- [[Guardrail]] — Ch 18; compliance/safety audits and anomaly detection.
- [[Reflection]] — Ch 4; the Critic/LLM-judge mechanism reused for helpfulness scoring and contractor self-validation.
- [[ReasoningTechniques]] — Ch 17; reasoning-process quality as a trajectory dimension.
- [[LLMAsAJudge]] — scalable subjective-quality scoring; worked Gemini rubric example.
- [[Monitoring]] / [[observability]] — the production-telemetry discipline applied to agents.
- [[ABTesting]] — comparing agent versions on live traffic.
- [[ConceptDrift]] / [[DriftDetection]] — degradation modes monitored.
- [[CostAndLatency]] / [[Latency]] — efficiency metrics; persistent logging.
- [[RAGEvaluation]] — RAG faithfulness/relevance metrics.
- [[HumanInTheLoop]] — human verification of audits; gold-standard evaluation.
- [[MultiAgentCollaboration]] — multi-agent trajectory evaluation.
- [[GoogleADK]] — `adk web` / `pytest` / `adk eval`, test files, evalsets.
- [[gemini|Gemini]] — judge model (`gemini-1.5-flash-latest`) in the legal-survey example.
- [[Datadog]] / [[Splunk]] / [[Grafana]] / [[Prometheus]] / [[InfluxDB]] / [[Snowflake]] / [[GoogleBigQuery]] — latency/telemetry sinks named in the chapter.
- [[AntonioGulli]] — author.

## References (cited in chapter)
- ADK Web: github.com/google/adk-web
- ADK Evaluate: google.github.io/adk-docs/evaluate/
- Survey on Evaluation of LLM-based Agents — arXiv:2503.16416
- Agent-as-a-Judge: Evaluate Agents with Agents — arXiv:2410.10934
- Agent Companion, Gulli et al. — kaggle.com/whitepaper-agent-companion

## Contradictions
- None found. Reinforces and externalizes [[GoalSettingAndMonitoring|Ch 11]]'s self-evaluation loop (internal goal-progress vs. external production measurement) and extends [[Reflection|Ch 4]]'s Critic into a production/contractor evaluation discipline.
