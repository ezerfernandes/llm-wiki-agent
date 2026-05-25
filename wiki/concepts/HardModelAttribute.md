---
title: "Hard Model Attribute"
type: concept
tags: [model-selection, methodology, ai-engineering]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Hard Model Attribute

A model attribute **you cannot change** (or cannot practically change). Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Hard attributes are often the results of decisions made by model providers (licenses, training data, model size) or your own policies (privacy, control). For some use cases, the hard attributes can reduce the pool of potential models significantly."

## Examples

- **Provider-set**: license, training data, model size, model architecture, supported features.
- **Your-policy-set**: privacy requirements (can data leave your network?), regulatory constraints, on-device deployment needs.

## Use in model selection

[[ModelSelectionWorkflow|Step 1]] of the four-step workflow: *"Filter out models whose hard attributes don't work for you."* The hard-attribute filter happens before benchmark comparisons because there's no point benchmarking a model you legally can't use.

## Hard vs soft is context-dependent

> "What you define as hard and soft attributes depends on both the model and your use case. For example, latency is a soft attribute if you have access to the model to optimize it to run faster. It's a hard attribute if you use a model hosted by someone else."

If you self-host, latency is improvable (via [[Quantization|quantization]], batching, etc.) → soft. If you use an API, latency is what it is → hard.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[SoftModelAttribute]] — the complement.
- [[ModelSelectionWorkflow]] — where the filter is applied.
- [[ModelBuildVsBuy]] — the highest-impact hard-attribute decision.
- [[ModelLicense]] / [[LlamaLicense]] — license is the canonical hard attribute.
