---
title: "OpenAI Evals"
type: concept
tags: [evaluation, tooling, openai, benchmark]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# OpenAI Evals

[[openai|OpenAI]]'s **[[EvaluationHarness|evaluation harness]]**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "OpenAI's evals lets you run any of the approximately 500 existing benchmarks and register new benchmarks to evaluate OpenAI models. Their benchmarks evaluate a wide range of capabilities, from doing math and solving puzzles to identifying ASCII art that represents words."

## Position

Sibling to [[lm-evaluation-harness]] (EleutherAI). Both let you run a model against many benchmarks; OpenAI Evals is the OpenAI-centric one — designed for testing OpenAI models, though extensible.

## Distinguishing features

- **User-registered benchmarks** — community-contributed evaluations are first-class.
- **OpenAI integration** — built to make running benchmarks against OpenAI's models easy.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[openai|OpenAI]] — maintainer.
- [[EvaluationHarness]] — parent concept.
- [[lm-evaluation-harness]] — sibling harness.
- [[PublicBenchmark]] — what it runs.
