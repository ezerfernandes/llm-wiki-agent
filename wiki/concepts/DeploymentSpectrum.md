---
title: "Deployment Spectrum"
type: concept
tags: [ml-systems, deployment, mlsysbook, foundations, serving]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch13-model-serving, mlsysbook-ch14-ml-operations, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Deployment Spectrum

The continuum of ML-system deployment targets — **from megawatt-scale cloud data centers to milliwatt-scale embedded devices** — each imposing different bottlenecks on data collection, model updates, monitoring, and serving. A framing device in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]).

| Environment | Primary constraint | Efficiency focus |
|---|---|---|
| Cloud training | Cost, throughput | Distributed efficiency, [[GPUUtilization|utilization]] |
| Cloud inference | Latency, cost/query | Batching, serving optimization |
| Edge devices | Memory, power | [[ModelCompression|Compression]], [[Quantization|quantization]] |
| Mobile | Battery, thermal | Energy-efficient inference |
| [[TinyML]] | KB memory, mW power | Extreme compression, specialized architectures |

The cloud↔TinyML gap spans ~10⁷× compute and ~10⁶× memory ([[SystemArchetype|four System Archetypes]]). A single deployment choice cascades through the whole lifecycle: it shapes retraining cadence, data retention, update mechanism (cloud A/B tests vs. edge OTA), and monitoring. Modern systems are often **hybrid** (edge perception + cloud training; on-device wake-word + cloud NLP).

[[mlsysbook-ch02-ml-systems|Ch 2]] grounds the spectrum quantitatively: nine orders of magnitude in power (MW→mW) and memory (TB→KB), with concrete thresholds — [[CloudML|Cloud ML]] (>1000 TFLOP/s, MW, 100–500 ms latency), [[EdgeML|Edge ML]] (~1 PFLOP/s, ~100 W, 10–100 ms), [[MobileML|Mobile ML]] (tens of INT8 TOPS, 2–5 W, 5–50 ms), [[TinyML]] (<1 TOPS, <1 mW, 1–10 ms). It argues the spectrum is dictated by *physics* (light barrier, [[PowerWall|power wall]], [[MemoryWall|memory wall]]), not engineering preference.

## Connections

- [[SystemArchetype]] — the four reference tiers (Cloud / Edge / Mobile / TinyML).
- [[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]] — the four paradigms, each with a distinct binding constraint.
- [[MLSystemLifecycle]] — what deployment reshapes.
- [[ModelCompression]] / [[EfficiencyFramework]] — the toolkit per tier.
- [[HybridML]] — combining paradigms when no single tier suffices.
- [[ConstraintPropagationPrinciple]] — [[mlsysbook-ch03-ml-workflow|Ch 3]] argues paradigm selection is a *day-one* constraint: deferring it ("figure out deployment later") is a named pitfall that triggers a 16× cost multiplier at deployment.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] — sources.
- [[mlsysbook-ch13-model-serving]] — Ch 13 shows the walls *intensify* at serving time (they add SLOs + cost on top of hardware limits): the same ResNet-50 needs FP16 TensorRT on cloud GPU (1.4 ms, batch 1–128), INT8 TF Lite on a mobile NPU (12 ms, batch-1, zero-copy), or a downsized MobileNetV2 in KB of TinyML SRAM (it can't run at all). Maps each paradigm to an [[MLPerfScenarios|MLPerf serving scenario]].
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 references the serving spectrum (online/offline/near-online) and per-archetype utilization targets for the deployment context.
- [[mlsysbook-ch16-conclusion]] — the conclusion argues the same physics (the [[ThirteenQuantitativeInvariants|thirteen invariants]]) governs all of cloud, edge/mobile, and TinyML, each foregrounding a different term — its reference mobile NPU has ~10×+ lower INT8 throughput and >100× smaller power envelope than an H100. **[[GenerativeAI|Generative AI]] is a workload class, not a fourth environment**, stressing all three at token-serving scale; the spectrum's largest end extends to the [[WarehouseScaleComputer|Warehouse-Scale Computer]].

