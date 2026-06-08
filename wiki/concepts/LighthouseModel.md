---
title: "Lighthouse Model"
type: concept
tags: [ml-systems, benchmarking, mlsysbook, workloads]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Lighthouse Model

The **five recurring canonical workloads** that Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) uses as diagnostic probes for the [[IronLawOfMLSystems|iron law]] across chapters. Each isolates a distinct system bottleneck.

| Lighthouse Model | Bottleneck | What it reveals | Key question |
|---|---|---|---|
| [[ResNet50|ResNet-50]] | Compute throughput under weight reuse | GPU utilization, batching | Is my hardware doing math or waiting for data? |
| GPT-2 / [[Llama]] | [[MemoryBandwidth|Memory bandwidth]] | KV caching, weight loading | How fast can I move weights to compute? |
| [[DLRM]] | Memory *capacity* | Embedding tables, scale-out | How do I fit TB-scale models in memory? |
| [[MobileNetV2]] | Latency & power | Efficient operator design | Can I meet real-time on battery? |
| [[KeywordSpotting]] | Power envelope | Extreme quantization | Can I run always-on inference on milliwatts? |

The same equation yields different diagnoses: ResNet-50 reuses small weight filters (compute-bound under batching), while GPT-2 loads billions of unique weights per token (bandwidth-bound) — so doubling $R_{peak}$ helps the former and barely touches the latter. Quantitative specs appear in the Network Architectures chapter.

[[mlsysbook-ch02-ml-systems|Ch 2]] pairs each Lighthouse Model with a [[WorkloadArchetype|workload archetype]] and the [[DeploymentSpectrum|paradigm]] where it predominantly runs: ResNet-50 = Compute Beast (cloud training, edge inference); GPT-2/Llama = Bandwidth Hog (cloud inference); DLRM = Sparse Scatter (cloud-only, distributed); MobileNet = efficient Compute Beast (mobile, edge); KWS = Tiny Constraint (TinyML, always-on).

## Connections

- [[IronLawOfMLSystems]] — the law these workloads probe.
- [[WorkloadArchetype]] — the four archetypes each Lighthouse Model instantiates.
- [[DAMTaxonomy]] — each model stresses a different axis.
- [[RooflineModel]] / [[ArithmeticIntensity]] — where each sits relative to the ridge point.
- [[ResNet50]] / [[MobileNetV2]] / [[DLRM]] / [[KeywordSpotting]] / [[Llama]] — the five workloads.
- [[mlsysbook-ch16-conclusion]] — the conclusion revisits the five as "systems detectives" that probe every term of the [[ThirteenQuantitativeInvariants|thirteen invariants]] across the [[DeploymentSpectrum]]; it traces the full MobileNetV2 journey (Foundations→Architecture→Training→Compression→Acceleration→Serving→Operations) to make [[ConstraintPropagationPrinciple|constraint propagation]] concrete.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] — sources.
