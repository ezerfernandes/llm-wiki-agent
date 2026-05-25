---
title: "Evaluation-Driven Development"
type: concept
tags: [evaluation, methodology, ai-engineering, planning]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Evaluation-Driven Development

**Define evaluation criteria before building the application.** Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], evaluation-driven development is the AI-engineering analog of test-driven development:

> "I call this approach evaluation-driven development. The name is inspired by test-driven development in software engineering, which refers to the method of writing tests before writing code. In AI engineering, evaluation-driven development means defining evaluation criteria before building."

## The argument

Most production AI applications succeed because their evaluation criteria are well-defined ahead of time:

- **Recommender systems** — engagement / purchase-through rates.
- **Fraud detection** — money saved from prevented frauds.
- **Coding agents** — [[FunctionalCorrectness|functional correctness]] of generated code.
- **[[CloseEndedTask|Close-ended]] FM use cases** — intent classification, sentiment analysis, next-action prediction — all easier to evaluate than open-ended generation.

Conversely, the riskiest AI applications are those *"deployed but no one knows whether it's working."* Huyen recounts an ML engineer at a used-car dealership who deployed a value-prediction model and *"a year after the model was deployed, their users seemed to like the feature, but he had no idea if the model's predictions were accurate."*

## The lamppost limitation

Huyen flags a counter-argument: focusing only on applications with measurable outcomes is *"similar to looking for the lost key under the lamppost (at night)."* Game-changing applications might be excluded if no one can figure out how to evaluate them. The discipline-level position:

> "I believe that evaluation is the biggest bottleneck to AI adoption. Being able to build reliable evaluation pipelines will unlock many new applications."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[Evaluation]] / [[EvaluationPipeline]] — discipline and execution.
- [[UsefulnessThreshold]] — what specific evaluation values mean "ready to ship."
- [[BusinessMetric]] — the dollars/engagement metric evaluation criteria should map to.
- [[DomainSpecificCapability]] / [[GenerationCapability]] / [[InstructionFollowingCapability]] / [[CostAndLatency]] — the four buckets evaluation criteria live in.
