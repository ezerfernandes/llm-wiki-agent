---
title: "lm-evaluation-harness"
type: concept
tags: [evaluation, tooling, eleutherai, benchmark]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# lm-evaluation-harness

[[EleutherAI]]'s **[[EvaluationHarness|evaluation harness]]** for language models. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "EleutherAI's lm-evaluation-harness supports over 400 benchmarks."

## What it includes

A wide range of benchmarks including [[mmlu|MMLU]], [[AGIEval]], [[ARCC]], [[HellaSwag]], [[WinoGrande]], [[GSM8K]], [[bigbench|BIG-bench]] tasks, and many more — *"75% of the tasks … are multiple-choice"* as of April 2024.

## Position

The de facto standard harness for the open-source community. Powers HuggingFace's [[OpenLLMLeaderboard]] under the hood for many of its benchmarks. Sibling to [[OpenAIEvals]] (OpenAI's harness, focused on OpenAI models).

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[EleutherAI]] — maintainer.
- [[EvaluationHarness]] — parent concept.
- [[OpenAIEvals]] — sibling harness.
- [[OpenLLMLeaderboard]] — leaderboard that uses it.
- [[CloseEndedTask]] / [[MultipleChoiceQuestion]] — the dominant task format in its benchmark set.
