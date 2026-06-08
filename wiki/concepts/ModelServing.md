---
title: "Model Serving"
type: concept
tags: [mlops, deployment, inference, serving, mlsysbook]
sources: [madewithml-serving, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Model Serving

Exposing a trained model behind an API (batch or [[OnlineInference]]) for downstream consumers. Concerns include latency, scaling, [[ModelComposition]], and [[ShadowDeployment]] strategies.

## In mlsysbook (Ch 13)

[[mlsysbook-ch13-model-serving|mlsysbook Ch 13]] (opening the Deploy part) defines serving as "the operational phase that provides model predictions under strict latency constraints" and frames it as **the serving inversion**: training maximizes throughput, serving minimizes latency and pays a tax on every request (the [[IronLawOfMLSystems|iron law]]'s $L_{\text{lat}}$ term becomes dominant). The common pitfall — serving is "just the forward pass" — misses that it is a distributed-systems problem: routing, load balancing, request transformation. The chapter organizes the whole stack around the [[LatencyBudget|latency budget]], [[QueuingTheory|queuing theory]], and [[DynamicBatching|dynamic batching]], extending into [[LLMServing|LLM serving]], [[InferenceRuntime|runtime]]/precision selection, and [[CostPerInference|serving economics]].

## Connections

- [[LatencyBudget]] / [[QueuingTheory]] / [[TailLatency]] — the analyses serving requires.
- [[InferenceServer]] / [[DynamicBatching]] — the software architecture and core throughput lever.
- [[LLMServing]] / [[ContinuousBatching]] / [[PagedAttention]] — the generative-model deepening.
- [[InferenceRuntime]] / [[CostPerInference]] / [[CapacityPlanning]] — runtime choice and economics.
- [[StaticInference]] / [[DynamicInference]] — the precompute-vs-on-demand axis.
- [[mlsysbook-ch13-model-serving]] — source.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 covers the operational side of serving (framework selection, latency budget where inference is only ~45% of end-to-end, autoscaling cold starts).

