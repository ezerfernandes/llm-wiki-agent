---
title: "Feedback-Bench"
type: concept
tags: [benchmark, evaluation, feedback, prometheus, free-form]
sources: [2604.14585-prompt-optimization-coin-flip]
last_updated: 2026-05-22
---

# Feedback-Bench

**Feedback-Bench** (Kim, Suk, Longpre, Lin, Shin, Welleck, Neubig, Lee, Lee & Seo, arXiv:2405.01535, 2024) is the evaluation benchmark released alongside **[[Prometheus2|Prometheus 2]]** — an open-source LM specialized in evaluating other LMs. Free-form fine-grained feedback over rubric dimensions; LM-judge scoring.

## In Zhang et al. 2026

[[2604.14585-prompt-optimization-coin-flip|Zhang et al. (2026)]] include Feedback-Bench as one of four Study 2 single-agent prompt-optimization tasks.

**Results on Claude Haiku (Table 2):**

| Method | Feedback-Bench |
|---|---|
| Zero-Shot | 82.4 |
| [[APE]] | 82.3 |
| [[OPRO]] | 81.4 |
| [[EvoPrompt]] | 82.0 |
| [[PromptBreeder]] | **83.5** |
| DSPy-style | 81.9 |
| [[PROSEOptimizer\|PROSE]] | 82.1 |

Best gain: **+1.1 pts** ([[PromptBreeder]]) — below the 2-pt [[HeadroomTest|headroom threshold]]. Average across methods: **−0.20 pts**.

**Results on Nova Lite (Table 4):**

| Method | Feedback-Bench |
|---|---|
| Zero-Shot | 80.4 |
| [[OPRO]] | **81.9** |
| Most others | ~80–81 |

Feedback-Bench is the canonical example of a Haiku/Nova **model-specific reversal**: only 1/6 methods beat zero-shot on Haiku, but 4/6 do on Nova — see [[ModelSpecificityShelfLife]].

## Position

Feedback-Bench is one of three **free-form** Study 2 tasks (alongside [[WildBench]] and [[XSum]]) lacking the [[CanButDoesntPattern|"can but doesn't" structural unlock]]. [[HelpSteer2]] is the structured-output counterexample in the same study.

## Connections

- [[2604.14585-prompt-optimization-coin-flip]] — canonical source.
- [[Prometheus2]] — sibling evaluator from the same research group.
- [[WildBench]] / [[XSum]] — sibling free-form failure tasks.
- [[HelpSteer2]] — structured-output counterexample.
- [[ModelSpecificityShelfLife]] — Feedback-Bench's Haiku↔Nova reversal is the cleanest example.
- [[CanButDoesntPattern]] — property Feedback-Bench lacks.
- [[HeadroomTest]] / [[CompoundAIDiagnostic]] — diagnostic context.
