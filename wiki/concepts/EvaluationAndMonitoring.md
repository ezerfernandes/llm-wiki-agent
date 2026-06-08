---
title: "Evaluation and Monitoring (Agentic Pattern)"
type: concept
tags: [agents, agentic-design-patterns, evaluation, monitoring, observability, llm-as-judge, trajectory, ab-testing, drift]
sources: [agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Evaluation and Monitoring (Agentic Pattern)

**Evaluation and Monitoring** is the 19th of the 21 patterns in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] (see [[agentic-design-patterns-ch19-evaluation|Ch 19]]). It is the discipline of **systematically assessing an agent's effectiveness, efficiency, and compliance** with requirements — defining metrics, establishing feedback loops, and implementing reporting so that agent performance stays aligned with expectations in **operational environments**.

> **Scope vs. neighbouring patterns.** Gulli explicitly distinguishes this pattern from [[GoalSettingAndMonitoring|Goal Setting and Monitoring]] (Ch 11, the agent's *internal* self-management loop) and [[ReasoningTechniques|Reasoning]] (Ch 17). Ch 19 is the **continuous, often external** measurement of the agent — the [[observability|observability]] / [[Monitoring|production-monitoring]] sense applied to agentic systems. Where Ch 11 asks *"am I making progress toward my goal?"*, Ch 19 asks *"is this deployed agent good, fast, cheap, safe, and not degrading?"*

## Why it matters
Agentic systems and LLMs are **probabilistic and non-deterministic**, operating in complex, dynamic environments where performance can degrade after deployment. *"Traditional software testing is insufficient"* — standard code yields predictable pass/fail results, whereas agents need qualitative assessment of both the final output **and the trajectory** (the sequence of steps taken). Problems like [[DataDrift|data drift]], unexpected interactions, faulty [[ToolUse|tool calling]], and deviations from intended goals arise *after* deployment, so continuous assessment is necessary. (Fig. 1 frames best practice as a 5-level pyramid: define measurable objectives → use quantitative + qualitative data → collect data regularly → reward/incentivize agents → provide feedback and coaching.)

## Practical applications (Ch 19)
- **Performance tracking in live systems** — continuously monitor accuracy, [[Latency|latency]], and resource consumption of a deployed agent (e.g. a customer-service chatbot's resolution rate, response time).
- **[[ABTesting|A/B testing]] for agent improvements** — systematically compare versions/strategies in parallel (e.g. two planning algorithms for a logistics agent).
- **Compliance and safety audits** — automated audit reports tracking adherence to ethical guidelines, regulatory requirements, and safety protocols; verifiable by a [[HumanInTheLoop|human-in-the-loop]] or another agent, generating KPIs or triggering alerts. Links to the [[Guardrail|Guardrails]] pattern (Ch 18).
- **Enterprise governance** — a new control instrument, the AI **"[[AIContract|Contract]]"**, codifies objectives, rules, and controls for AI-delegated tasks.
- **[[ConceptDrift|Drift]] detection** — monitor relevance/accuracy over time, detecting degradation from input-distribution change (concept drift) or environmental shifts.
- **Anomaly detection in agent behavior** — identify unusual/unexpected actions signalling an error, malicious attack, or emergent undesired behavior.
- **Learning-progress assessment** — for learning agents ([[LearningAndAdaptation]]), track the learning curve and generalization across tasks/datasets.

## Agent Response Assessment — from naive accuracy to real metrics
The chapter's core building block is **Agent Response Assessment**: judging whether the agent delivers pertinent, correct, logical, unbiased, accurate information. The hands-on example shows a naive `evaluate_response_accuracy` (exact, case-insensitive string match) returning **0.0** for *"The capital of France is Paris."* vs *"Paris is the capital of France."* — illustrating why exact match fails on paraphrase / semantic equivalence. Real-world evaluation needs richer metrics:
- **String-similarity measures** — Levenshtein distance, Jaccard similarity.
- **Keyword analysis** — presence/absence of required keywords.
- **Semantic similarity** — cosine similarity over [[Embedding|embedding]] models.
- **[[LLMAsAJudge|LLM-as-a-Judge]] evaluations** — for nuanced correctness and helpfulness.
- **[[RAGEvaluation|RAG-specific metrics]]** — faithfulness and relevance.

## Production monitoring: latency, cost, token usage
- **Latency monitoring** — measure the duration to process requests and generate outputs; elevated latency hurts UX in real-time/interactive settings. *"Simply printing latency data to the console is insufficient"* — log to persistent storage: structured logs (JSON), time-series DBs ([[InfluxDB]], [[Prometheus]]), data warehouses ([[Snowflake]], [[GoogleBigQuery|BigQuery]], PostgreSQL), or observability platforms ([[Datadog]], [[Splunk]], [[Grafana|Grafana Cloud]]). See [[CostAndLatency]].
- **Token-usage tracking** — for LLM-powered agents, billing depends on input/output token counts, so efficient token use directly reduces operational cost and surfaces prompt-engineering improvement areas. The chapter's `LLMInteractionMonitor` accumulates `total_input_tokens` / `total_output_tokens` per interaction (using the LLM API's real tokenizer in production).
- **Custom "helpfulness" metric via LLM-as-a-Judge** — subjective qualities are evaluated by prompting an LLM evaluator with a rubric. The worked `LLMJudgeForLegalSurvey` ([[gemini|Gemini]] `gemini-1.5-flash-latest` at low temperature, JSON response mode) scores a legal survey question 1–5 across **Clarity & Precision, Neutrality & Bias, Relevance & Focus, Completeness, Appropriateness for Audience**, returning `{overall_score, rationale, detailed_feedback, concerns, recommended_action}`. A good vs. biased vs. vague question demonstrate the rubric in action.

## Three evaluation methods (trade-offs)
| Method | Strengths | Weaknesses |
|---|---|---|
| **Human evaluation** | Captures subtle behavior | Hard to scale, expensive, time-consuming; subjective |
| **[[LLMAsAJudge|LLM-as-a-Judge]]** | Consistent, efficient, scalable | May overlook intermediate steps; limited by LLM capabilities |
| **Automated metrics** | Scalable, efficient, objective | May miss complete capabilities |

## Agent trajectories
See [[AgentTrajectoryEvaluation]]. Beyond the final output, evaluation must assess the **trajectory** — the sequence of tool selections, strategies, and steps. The agent's actual actions are compared against a ground-truth trajectory using **exact match, in-order match, any-order match, precision, recall, single-tool-use** comparison methods. Multi-agent systems amplify the challenge: evaluate both each agent's individual job *and* the system as a whole (cooperation, plan adherence, right-agent-for-the-task, scalability when adding agents).

## From Agents to Advanced Contractors
The chapter closes by introducing the **[[AIContract|"contractor"]]** evolution (Agent Companion, Gulli et al.) — moving from probabilistic, brittle agents to deterministic, accountable systems via a Formalized Contract, a dynamic negotiation/feedback lifecycle, quality-focused iterative self-validation, and hierarchical decomposition via subcontracts.

## Google's ADK evaluation support
[[GoogleADK|Google's ADK]] supports agent evaluation three ways: **web-based UI** (`adk web`) for interactive evaluation and dataset generation; **programmatic** `pytest` integration calling `AgentEvaluator.evaluate(...)` for [[CICD|CI/CD]] test pipelines; and **CLI** (`adk eval`) for automated evaluation in regular build/verification. Two artifact types: single **test files** (one session, multiple turns — unit testing during dev) and **evalset files** (an "evalset" dataset of multiple multi-turn "evals" — integration testing). See [[AgentTrajectoryEvaluation]].

## Connections
- [[AgenticDesignPatterns]] — the book hub; [[agentic-design-patterns-ch19-evaluation|Ch 19]] is the source.
- [[GoalSettingAndMonitoring]] — Ch 11; the *internal* self-management loop, explicitly distinguished from this *external* measurement pattern.
- [[Guardrail]] — Ch 18; compliance/safety audits and anomaly detection feed the safety layer.
- [[Reflection]] — Ch 4; the Critic / [[LLMAsAJudge|LLM-judge]] mechanism reused here for helpfulness scoring.
- [[ReasoningTechniques]] — Ch 17; reasoning-process quality is one trajectory dimension.
- [[LLMAsAJudge]] — the scalable evaluation tier for subjective qualities.
- [[AgentTrajectoryEvaluation]] — trajectory/tool-use comparison and multi-agent evaluation.
- [[AIContract]] — the contractor evolution toward accountable, verifiable agents.
- [[Monitoring]] / [[observability]] — the production-telemetry discipline this pattern instantiates for agents.
- [[ABTesting]] — comparing agent versions on live traffic.
- [[ConceptDrift]] / [[DataDrift]] / [[DriftDetection]] — the degradation modes monitored.
- [[CostAndLatency]] / [[Latency]] — efficiency metrics tracked in production.
- [[RAGEvaluation]] — RAG-specific faithfulness/relevance metrics.
- [[HumanInTheLoop]] — human verification of audits and gold-standard evaluation.
- [[GoogleADK]] — `adk web` / `pytest` / `adk eval`, test files, and evalsets.
- [[gemini|Gemini]] — the judge model in the legal-survey example.
- [[Datadog]] / [[Splunk]] / [[Grafana]] / [[Prometheus]] / [[InfluxDB]] / [[Snowflake]] / [[GoogleBigQuery]] — latency/telemetry sinks named in the chapter.
