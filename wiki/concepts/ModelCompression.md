---
title: "Model Compression"
type: concept
tags: [inference, optimization, compression, quantization, distillation, pruning]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch10-model-compression, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Model Compression

**Techniques that reduce a model's size** — and, as a consequence, often make it faster to serve. Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Model compression involves techniques that reduce a model's size. Making a model smaller can also make it faster."*

The umbrella for several distinct techniques covered in *AI Engineering*.

## The four families

| Family | What it does | Status in 2024 |
|---|---|---|
| **[[Quantization|Quantization]]** | Reduce precision (FP32 → FP16 → INT8 → INT4 → ...) | **Dominant**, easy to use, works out of the box |
| **[[KnowledgeDistillation|Distillation]]** | Train a smaller model to mimic a larger one | Common; uses AI-generated data |
| **[[Pruning|Pruning]]** | Remove unimportant nodes or zero out parameters | Encouraging but less common (harder, smaller gains, hardware-dependent) |
| **[[LowRankFactorization|Low-rank factorization]]** | Approximate weight matrices as products of smaller matrices | Foundation of LoRA-style PEFT; less common as pure compression |

## Why quantization dominates

> *"Weight-only quantization is by far the most popular approach since it's easy to use, works out of the box for many models, and is extremely effective. Reducing a model's precision from 32 bits to 16 bits reduces its memory footprint by half. However, we're close to the limit of quantization — we can't go lower than 1 bit per value."*

The 1-bit floor is theoretically near at hand — see [[BitNetB158]] (Microsoft 2024) for the 1.58-bit work.

## Why distillation is common

A distilled model can be substantially smaller while matching behavior on a target task. [[DistilBERT]] is the canonical baseline (40% smaller, 60% faster, 97% capability). [[ai-engineering-ch08-dataset-engineering|Ch 8]] discusses distillation as an AI-data-synthesis use case in detail.

## Why pruning is rare

> *"In practice, as of this writing, pruning is less common. It's harder to do, as it requires an understanding of the original model's architecture, and the performance boost it can bring is often much less than that of other approaches. Pruning also results in sparse models, and not all hardware architectures are designed to take advantage of the resulting sparsity."*

Frankle & Carbin (2019, the *lottery-ticket-hypothesis* paper) showed pruning can remove > 90% of non-zero parameters of certain trained networks "without compromising accuracy." But the engineering effort vs. quantization is unfavorable.

## Model compression and the autoregressive bottleneck

Ch 9 frames compression as one of three model-level levers (the other two: overcoming the [[Decode|autoregressive decoding]] bottleneck, and optimizing the [[Attention|attention mechanism]]). Compression alone doesn't solve autoregression — but it **multiplies** the effects of every other optimization by reducing the bytes that must be moved per token.

## As an efficiency dimension (mlsysbook)

Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) positions model compression as the core lever of **algorithmic efficiency** — the Algorithm-axis dimension of the [[EfficiencyFramework|efficiency framework]] (alongside compute efficiency and [[DataSelection|data selection]]). It is the *required consequence* of choosing an [[EdgeML|edge]]/[[TinyML]] deployment target: compression trades predictive accuracy to fit a device's fixed resource budget, often reducing model size by **over 90%** so a data-center model can run within kilobyte-scale memory and milliwatt power.

## The three-dimension stack ([[mlsysbook-ch10-model-compression|mlsysbook Ch 10]])

Ch 10 is the wiki's most systematic treatment. It rejects the "bag of tricks" view and organizes *every* technique along three composable dimensions:

1. **Structural optimization** — *what* to compute: [[Pruning]], [[KnowledgeDistillation]], [[NeuralArchitectureSearch|NAS]], [[LowRankFactorization]] / [[TensorDecomposition]].
2. **Precision optimization** — *how precisely*: [[Quantization]] (FP32→INT8 and below).
3. **Architectural efficiency** — *how efficiently it executes*: [[OperatorFusion]], [[Sparsity]] exploitation, [[AdaptiveInference]] / [[ConditionalComputation]], [[DepthwiseSeparableConvolution|hardware-aware design]].

Two governing lessons: (1) **dimensions compose multiplicatively** — BERT 440 MB → 28 MB (16×) via sequential pruning + distillation + INT8 QAT, ~0.6% loss when sequenced correctly; (2) **theoretical compression ratios lie** — a 50%-pruned + INT8 model has a 6× paper target but often measures ~1.5× on commodity hardware unless aligned with the hardware's execution model. The whole discipline is governed by the [[ConservationOfComplexity|conservation of complexity]] (no free lunch) and grounded in the [[IronLawOfMLSystems|iron law]] / [[RooflineModel|roofline]] physics. [[mlsysbook-ch10-model-compression]]

## Connections

- [[EfficiencyFramework]] / [[DataSelection]] / [[mlsysbook-ch01-introduction]] — compression as the algorithmic-efficiency dimension.
- [[mlsysbook-ch10-model-compression]] — the dedicated chapter: three-dimension stack, energy physics, conservation of complexity, decision framework.
- [[mlsysbook-ch02-ml-systems]] — frames compression as more important, not less, as the hardware budget tightens (cloud→edge→TinyML); buys 2–4× edge speedup and is mandatory below the TinyML memory-fit constraint.
- [[mlsysbook-ch03-ml-workflow]] — situates compression in the model-development stage as an iterative *compress-validate-adjust* loop (typically 3–5 iterations), because each step can silently push accuracy below the deployment threshold until the full validation suite runs.
- [[TinyML]] / [[EdgeML]] / [[MobileML]] — the deployment tiers that mandate it.
- [[Quantization]] — the dominant family.
- [[knowledgedistillation]] — the second most common family.
- [[Pruning]] — the third (less common) family.
- [[LowRankFactorization]] — fourth family; appears prominently in [[lora|LoRA]].
- [[Sparsity]] — the byproduct of pruning that hardware may or may not exploit.
- [[InferenceOptimization]] — broader discipline; model compression is one branch.
- [[ai-engineering-ch07-finetuning]] — depth on quantization.
- [[ai-engineering-ch08-dataset-engineering]] — depth on distillation.
- [[ai-engineering-ch09-inference-optimization]] — the umbrella source.
- [[mlsysbook-ch12-benchmarking]] — Ch 12 is the *validation* layer for compression: it demands **multi-dimensional** [[Benchmarking|benchmarking]] (accuracy + [[ExpectedCalibrationError|calibration/ECE]] + edge-case robustness + speedup + memory + energy), shows INT8 MobileNet holds top-1 (−0.9 pp) while ECE and edge-case accuracy degrade, maps the trade-off with the [[ParetoFrontier|Pareto frontier]], and warns that MLPerf mostly benchmarks dense unoptimized models while production runs compressed ones (a "consequential blind spot").
