---
title: "PlanBench"
type: concept
tags: [benchmark, planning, evaluation]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# PlanBench

An **extensible benchmark for evaluating LLMs on planning and reasoning about change**, introduced by Valmeekam, Marquez, Olmo, Sreedharan & Kambhampati (NeurIPS 2023, Datasets & Benchmarks Track). Built on IPC-style classical planning domains; uses **automated evaluation tools from the planning community** to eliminate subjective rubrics.

## Why it matters
PlanBench is the empirical backbone of the **"LLMs can't plan"** position ([[2402.01817-llm-modulo]]). It provides a domain-rich, formally-checkable, plan-validation-grounded measurement of plan generation that doesn't depend on LLM-judging or human raters.

## Headline results (Table 1, [[2402.01817-llm-modulo]])
On 600 instances of [[Blocksworld]] and the obfuscated **Mystery BW** variant, in zero-shot and one-shot natural-language prompting:

| Domain | Method | GPT-4o | GPT-4-Turbo | Claude-3-Opus | LLaMA-3 70B | Gemini Pro | GPT-4 |
|---|---|---|---|---|---|---|---|
| **Blocksworld** | one-shot | 28.3% | 23% | 48.2% | 12.6% | 11.3% | 34.3% |
| **Blocksworld** | zero-shot | 35.5% | 40.1% | 59.3% | 34.2% | 0.5% | 34.6% |
| **Mystery BW** | one-shot | 0.83% | 0.83% | 1.3% | 2.5% | 0.4% | 4.3% |
| **Mystery BW** | zero-shot | 0% | 0.16% | 0% | 0% | 0% | 0.16% |

## Interpretation
- **Best case ~12% executable plans on average** across the headline set (and only Claude-3-Opus zero-shot crosses 59%).
- **Mystery BW collapse** is the smoking-gun experiment: renaming actions/objects (an identity-preserving change for a true planner) destroys performance → LLMs are doing *approximate plan retrieval*, not planning.
- Fine-tuning and CoT/ReAct prompts don't materially change the qualitative picture.

## Connections
- [[Planning]] — the task class
- [[Blocksworld]] — the canonical domain
- [[LLMModuloFramework]] — the proposed remedy; uses PlanBench domains for case-study evidence
- [[SubbaraoKambhampati]], [[ArizonaStateUniversity]] — authors
- [[2402.01817-llm-modulo]] — source citing PlanBench
