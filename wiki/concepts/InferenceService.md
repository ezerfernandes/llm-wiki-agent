---
title: "Inference Service"
type: concept
tags: [infrastructure, ai-engineering, serving]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Inference Service

The **system that hosts a model and answers user queries**. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "For a model to be accessible to users, a machine needs to host and run it. The service that hosts the model and receives user queries, runs the model to generate responses for queries, and returns these responses to the users is called an inference service. The interface users interact with is called the model API."

## The vocabulary distinction

- **Inference service** = the system (model + serving infrastructure + scaling + auth + monitoring).
- **[[ModelAPI|Model API]]** = the user-facing interface to that service.
- **[[ModelAPIProvider|Model API Provider]]** = the organization running both.

Ch 4 notes that *"the term model API is typically used to refer to the API of the inference service, but there are also APIs for other model services, such as [[FineTuning|finetuning]] APIs and evaluation APIs."*

## Inference-optimization context

Ch 9 (referenced from Ch 4) covers how to optimize inference services. Key levers: [[Quantization|quantization]], batching, kv-caching, speculative decoding, model parallelism, etc.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[ModelAPI]] / [[ModelAPIProvider]] — sibling concepts in the same triad.
- [[ModelBuildVsBuy]] — the decision of whether to use someone else's inference service vs build your own.
- [[Quantization]] / [[CostAndLatency]] — what inference-service optimization targets.
