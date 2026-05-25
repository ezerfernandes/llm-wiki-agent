---
title: "Inference Optimization"
type: concept
tags: [inference, optimization, performance, ai-engineering]
sources: [ai-engineering-ch01-intro, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Inference Optimization

**Making models faster and cheaper to run at serving time.** A model-development-layer responsibility in the [[AIEngineeringStack|AI engineering stack]]. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]:

> *"Inference optimization means making models faster and cheaper. Inference optimization has always been important for ML engineering. Users never say no to faster models, and companies can always benefit from cheaper inference. However, as foundation models scale up to incur even higher inference cost and latency, inference optimization has become even more important."*

## The autoregressive amplifier

[[AutoregressiveLanguageModel|Autoregressive]] foundation models generate tokens sequentially:

- ~**10ms per token** × 100 tokens = **1 second** for a typical short response.
- Web applications expect **~100ms** total latency.
- Long outputs explode this further.

This is the single largest source of pressure on inference optimization in [[AIEngineering|AI engineering]].

## Techniques (Chs 7–9 of the book)

- **[[Quantization|Quantization]]** — reduce weight precision (FP16 → INT8 → INT4 → FP8/FP4).
- **[[KnowledgeDistillation|Distillation]]** — train a smaller "student" model from a larger "teacher."
- **Parallelism** — tensor, pipeline, expert, sequence parallelism for distributing inference across GPUs.
- Service-level optimizations — batching, KV-cache management, speculative decoding.

## Why it's more important in AI engineering than in ML engineering

The comparison table from Ch 1's stack discussion:

| Category | Traditional ML | Foundation models |
|---|---|---|
| Inference optimization | Important | **Even more important** |

Reasons:
- Foundation models are **bigger** → more compute per inference.
- Foundation models are **autoregressive** → latency scales with output length.
- Foundation models serve **interactive applications** → user expectations are tight (chat-grade latency).

## Latency metrics

Ch 1 names two foundation-model-specific latency metrics that Chapter 9 develops in depth:

- **[[TTFT]]** — Time To First Token (how fast the model starts responding).
- **[[TPOT]]** — Time Per Output Token (steady-state generation speed).
- **Total latency** — TTFT + (TPOT × output length).

## Connections

- [[AIEngineering]] / [[AIEngineeringStack]] — discipline-level home.
- [[AutoregressiveLanguageModel]] — the model class whose sequential nature creates the pressure.
- [[Quantization]] / [[knowledgedistillation]] — concrete techniques.
- [[TTFT]] / [[TPOT]] — latency metrics.
- [[UsefulnessThreshold]] — latency is one of the four usefulness metric groups.
- [[ai-engineering-ch01-intro]] — primary source (Ch 1).

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 is the book's deep dive on inference optimization, organizing techniques into a **three-level taxonomy** (model-level / hardware-level / service-level) via an archery metaphor:

- **Model-level** = "crafting better arrows" — [[ModelCompression|model compression]] ([[Quantization]], [[knowledgedistillation|distillation]], [[Pruning]], [[LowRankFactorization]]), attention-mechanism optimization ([[multiqueryattention|MQA]] / [[GroupedQueryAttention|GQA]] / [[CrossLayerAttention]] / [[PagedAttention]] / [[FlashAttention]]), and decoding-bottleneck attacks ([[SpeculativeDecoding]] / [[InferenceWithReference]] / [[ParallelDecoding]]).
- **Hardware-level** = "training a stronger archer" — accelerator selection, kernel writing, compilers ([[CUDA]] / [[Triton]] / [[ROCm]] / [[TVM]] / [[MLIR]] / [[XLA]]).
- **Service-level** = "refining the shooting process" — [[Batching]] ([[StaticBatching]] / [[DynamicBatching]] / [[ContinuousBatching]]), [[PrefillDecodeDisaggregation|prefill-decode disaggregation]] ([[DistServe]]), [[PromptCaching|prompt caching]], parallelism ([[TensorParallelism]] / [[PipelineParallelism]] / [[ReplicaParallelism]] / [[ContextParallelism]] / [[SequenceParallelism]]).

### Core diagnostic framework

Ch 9's analytical backbone is the **[[ComputeBound|compute-bound]] vs [[MemoryBandwidthBound|memory-bandwidth-bound]]** distinction (Williams et al. 2009, *Roofline*), measured by **[[ArithmeticIntensity|arithmetic intensity]]** (FLOPs per byte). The single load-bearing claim:

> **Autoregressive LLM decode is memory-bandwidth-bound, not compute-bound.** Each step loads the full model weights from HBM to generate one token — making bandwidth, not FLOPs, the binding constraint. Most of Ch 9's techniques attack this regime.

### Metrics framework

- **Latency**: [[TTFT]] (prefill-dominated), [[TPOT]] (decode-dominated), [[TBT|TBT]] / ITL (streaming cadence), [[TimeToPublish]] (user-visible vs model-internal).
- **Throughput**: TPS, RPS, RPM, **[[Goodput|goodput]]** (the SLO-respecting throughput metric to actually optimize).
- **Utilization**: **[[MFU]]** and **[[MBU]]** (introduced in PaLM paper; the metrics that matter — `nvidia-smi`'s [[GPUUtilization|GPU utilization]] is misleading).

### Huyen's closing prescription

> *"Across various use cases, the most impactful techniques are typically quantization (which generally works well across models), tensor parallelism (which both reduces latency and enables serving larger models), replica parallelism (which is relatively straightforward to implement), and attention mechanism optimization (which can significantly accelerate transformer models)."*

### Cost reality

Inference accounts for **up to 90% of ML costs for deployed AI systems** (Desislavov et al. 2023). An output token costs **2–4× an input token** across providers; one output token has the same latency impact as **100 input tokens** (Anyscale, Kadous et al. 2023). This cost asymmetry is what justifies Ch 9's intensity.
