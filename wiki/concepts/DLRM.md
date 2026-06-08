---
title: "DLRM (Deep Learning Recommendation Model)"
type: concept
tags: [deep-learning, recommendation, architecture, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch06-network-architectures, mlsysbook-ch08-model-training, mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# DLRM (Deep Learning Recommendation Model)

Meta's Deep Learning Recommendation Model, used in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the **memory-capacity [[LighthouseModel|Lighthouse Model]]** — the question it poses is *"how do I fit terabyte-scale models in memory?"*

DLRM's dominant cost is its enormous **embedding tables** (one row per categorical feature value, e.g. per user or item ID), which can reach TB scale and force scale-out across many devices. This makes memory *capacity*, not bandwidth or compute, the binding [[DAMTaxonomy|Machine-axis]] constraint — distinct from the bandwidth bottleneck of GPT-2/Llama or the compute bottleneck of batched [[ResNet50|ResNet-50]].

[[mlsysbook-ch02-ml-systems|Ch 2]] makes DLRM the canonical **[[WorkloadArchetype|Sparse Scatter]]** archetype (irregular memory access, poor cache locality) and a **cloud-only** workload: production embedding tables can exceed 100 TB, requiring distributed memory and high-bandwidth all-to-all interconnects. Netflix processes >100 billion data points daily through such systems.

## Connections

- [[LighthouseModel]] — the memory-capacity probe.
- [[WorkloadArchetype]] — DLRM is the Sparse Scatter archetype.
- [[DAMTaxonomy]] — stresses memory capacity on the Machine axis.
- [[IronLawOfMLSystems]] — capacity sits outside the time decomposition but bounds feasibility.
- [[CloudML]] — the only paradigm that can host TB-scale embedding tables.
- [[meta|Meta]] / [[Netflix]] — its originator and a deployer.
- [[SequenceAwareRecommendation]] — related recommendation modeling in the wiki.
- [[mlsysbook-ch03-ml-workflow]] — [[mlsysbook-ch03-ml-workflow|Ch 3]]'s "workflow variations" table casts DLRM as the memory-bound archetype: feature-store lookups <2 ms, strict <10 ms p99 SLA, embedding tables dominating storage — each lifecycle stage optimizing the $D_{vol}/\text{BW}$ term.
- [[mlsysbook-ch08-model-training]] — Ch 8 uses DLRM as the **training** counter-example to GPT-2: its massive embedding tables make it **memory-bandwidth-bound, not compute-bound**, requiring model parallelism for *capacity* rather than *throughput* — the chapter otherwise focuses on dense, compute-intensive transformer training.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] — sources.
- [[mlsysbook-ch10-model-compression]] — Ch 10's "DLRM and embedding quantization" Lighthouse: DLRM is *memory-capacity*-bound (TB-scale embedding tables), so [[Quantization|quantization]] FP32→INT8/INT4 is a pure *storage-density* win (4–8× more table per GPU), not a math-speed win.
- [[mlsysbook-ch06-network-architectures]] — Ch 6's "Sparse Architectures: RecSys" section: DLRM = bottom MLP (dense, compute-light) + [[EmbeddingTable|embedding tables]] (sparse, memory-heavy) + interaction layer + top MLP. A 1B-user×128-dim FP32 table ≈ 512 GB, forcing [[ModelParallelism|embedding sharding]] and an [[AllToAllCommunication|all-to-all]] gather limited by bisection bandwidth; the lookups are index-based random gathers that defeat caching. Notes RecSys is the *majority of AI inference cycles* at Meta/Google/Amazon despite minimal academic attention.
