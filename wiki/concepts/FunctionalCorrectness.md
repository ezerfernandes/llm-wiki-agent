---
title: "Functional Correctness"
type: concept
tags: [evaluation, methodology, code-generation]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Functional Correctness

**Functional correctness** evaluates a system based on *"whether it performs the intended functionality"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]). It is **the ultimate metric**: it measures the thing you actually care about, not a proxy.

> "Functional correctness is the ultimate metric for evaluating the performance of any application, as it measures whether your application does what it's intended to do. However, functional correctness isn't always straightforward to measure, and its measurement can't be easily automated."

## Where it's automatable

- **Code generation** — execute the generated code in a sandbox and check outputs. Sometimes called [[ExecutionAccuracy|execution accuracy]]. Powers [[HumanEval]] (OpenAI), [[MBPP]] (Google), and text-to-SQL benchmarks [[Spider]] / [[BIRDSQL]] / [[WikiSQL]]. Measured via [[PassAtK|`pass@k`]].
- **Game bots** — the in-game score is the functional metric (e.g., Tetris score).
- **Tasks with measurable objectives** — Ch 3's example: *"if you ask AI to schedule your workloads to optimize energy consumption, the AI's performance can be measured by how much energy it saves."*

## Where it's not

Ch 3 flags the hard cases: *"while many complex tasks have measurable objectives, AI isn't quite good enough to perform complex tasks end-to-end, so AI might be used to do part of the solution. Sometimes, evaluating a part of a solution is harder than evaluating the end outcome. Imagine you want to evaluate someone's ability to play chess. It's easier to evaluate the end game outcome (win/lose/draw) than to evaluate just one move."*

## Functional correctness contradicts surface metrics

OpenAI found on [[HumanEval]] that *"BLEU scores for incorrect and correct solutions were similar"* (Chen et al. 2021). **Optimizing for [[bleu|BLEU]] is not the same as optimizing for functional correctness.** This contradicts the implicit assumption behind many MT and code-eval training pipelines.

## Prior art

Long before AI, automatic functional-correctness validation has been standard practice in software engineering via **unit tests**. Functional correctness is how LeetCode and HackerRank grade submitted solutions.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ExactEvaluation]] — parent concept.
- [[ExecutionAccuracy]] — the code-specific flavor.
- [[PassAtK]] — the canonical code-eval metric.
- [[HumanEval]] / [[MBPP]] / [[Spider]] / [[BIRDSQL]] / [[WikiSQL]] — benchmarks built on functional correctness.
- [[bleu|BLEU]] — the surface-metric counterpoint; BLEU and functional correctness are decoupled on HumanEval.
- [[Verifier]] — adjacent concept; verifiers learn to predict functional correctness on tasks with verifiable answers.
