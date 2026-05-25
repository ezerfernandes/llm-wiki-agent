---
title: "Evaluation Trace"
type: concept
tags: [llm-supervision, traces, gepa, prompt-optimization]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# Evaluation Trace

[[2507.19457-gepa|GEPA]]'s name for **the natural-language text the environment produces while computing the reward**, distinct from the **execution trace** (the LLM's own output). Examples:

- A compiler's `error: expected ';' before '}' token` while testing generated code.
- A profiler's *"63% of cycles spent in `memcpy`"* while measuring kernel speed.
- A judge LLM's explanation *"the answer 1492 is wrong because Columbus reached Hispaniola, not the mainland"* attached to a 0-rating.
- A unit-test runner's *"3 of 5 cases passed"* output.

Quoting the paper:

> *"The text that LLMs produce is the execution trace of the AI system. The text that the environment produces to compute the reward (e.g., compiler error messages before giving reward 0) is the evaluation trace."*

## Why distinguish

Pre-GEPA prompt optimizers (TextGrad, APO, MIPROv2) primarily consume *execution* traces — the LLM's outputs — plus scalar rewards. Evaluation traces are often discarded by the time the optimizer sees the data point. GEPA's [[FeedbackFunction|feedback function]] $\mu_f$ is built around exactly this slot — capture the evaluator's natural-language byproducts and route them to the [[ReflectivePromptMutation|reflection LM]] alongside the scalar score.

## In the GEPA pipeline

1. Rollout $\Phi(x_i)$ produces execution trace $t^{exec}_i$.
2. Evaluator scores $\Phi(x_i)$ against $m_i$; in producing the score it emits trace $t^{eval}_i$ (compiler stderr, judge rationale, etc.).
3. $\mu_f$ returns $(s_i, t^{eval}_i)$.
4. Reflection LM receives $(\pi_j, t^{exec}_i, s_i, t^{eval}_i)$ for module $j$.
5. Reflection LM proposes new $\pi'_j$ that addresses what $t^{eval}_i$ revealed.

## Domain examples in the paper

- **NPUEval / KernelBench:** compiler errors + profiler output are the dominant feedback; produces 70% vector utilization peaks on AMD XDNA2 by literally feeding the LLM the architecture's compiler errors and letting it learn the kernel coding style from them.
- **HotpotQA / HoVer:** judge / ground-truth-with-explanation as feedback.
- **PUPA:** privacy-leakage explanations from the privacy evaluator.

## Connections
- [[2507.19457-gepa]] — canonical source.
- [[FeedbackFunction]] — the function that surfaces evaluation traces.
- [[ReflectivePromptMutation]] — the consumer.
- [[GEPA]] — the optimizer.
- [[NPUEval]] / [[KernelBench]] — benchmarks where evaluation traces (compiler errors) carry most of the learning signal.
- [[PromptOptimization]] — broader activity.
