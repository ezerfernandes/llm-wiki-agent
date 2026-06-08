---
title: "Workload Archetype"
type: concept
tags: [ml-systems, performance, mlsysbook, framework, foundations]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Workload Archetype

A **classification of ML workloads by their dominant [[IronLawOfMLSystems|iron-law]] bottleneck rather than their model family**. Introduced in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]) as the diagnostic that the [[BottleneckPrinciple|bottleneck principle]] reduces optimization to.

| Archetype | Binding constraint | Optimization lever | Example ([[LighthouseModel|Lighthouse Model]]) | [[DeploymentSpectrum|Paradigm]] |
|---|---|---|---|---|
| **Compute Beast** | Raw FLOP/s ($R_{peak}$); high FLOP/byte | Faster arithmetic, batching | [[ResNet50|ResNet-50]] training; [[MobileNetV2|MobileNet]] (efficient) | Cloud training; mobile/edge |
| **Bandwidth Hog** | Memory bandwidth ($\text{BW}$) | KV-caching, quantization | [[GPT2|GPT-2]]/Llama autoregressive decode | Cloud inference |
| **Sparse Scatter** | Memory capacity + access latency | Distributed memory, interconnect | [[DLRM]] embedding tables (>100 TB) | Cloud-only (distributed) |
| **Tiny Constraint** | Energy per inference (<1 mW, <256 KB) | Extreme compression, binary nets | [[KeywordSpotting|KWS]] always-on sensing | [[TinyML]] |

The distinction matters because the optimization strategy differs fundamentally: a compute-bound workload benefits from faster arithmetic, a bandwidth-bound workload only from wider memory buses. *Misidentifying the archetype wastes optimization effort on the wrong term* — "as when teams add accelerator FLOP/s to a memory-bound inference pipeline and observe zero speedup." Archetypes map naturally onto deployment paradigms: Compute Beasts and Sparse Scatter gravitate to cloud; Bandwidth Hogs span cloud/edge by latency; Tiny Constraint is exclusively TinyML.

## Connections

- [[IronLawOfMLSystems]] — the law whose dominant term defines each archetype.
- [[BottleneckPrinciple]] — the principle that reduces optimization to archetype identification.
- [[LighthouseModel]] — the five concrete workloads that instantiate the archetypes.
- [[DAMTaxonomy]] — archetypes are the bottleneck-diagnostic reading of D·A·M.
- [[RooflineModel]] / [[ArithmeticIntensity]] — distinguishes Compute Beast from Bandwidth Hog.
- [[DeploymentSpectrum]] / [[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]] — where each archetype runs.
- [[mlsysbook-ch02-ml-systems]] — source.
