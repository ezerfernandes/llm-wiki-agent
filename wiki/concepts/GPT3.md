---
title: "GPT-3"
type: concept
tags: [llm, foundation-model, scaling, mlsysbook]
sources: [mlsysbook-ch01-introduction]
last_updated: 2026-06-05
---

# GPT-3

OpenAI's 175-billion-parameter language model (Brown et al. 2020), used in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the recurring scale anchor for the **compute bottleneck** of the [[DeepLearning|deep-learning]] era.

Systems facts the chapter pins to GPT-3:

- **175B parameters** ≈ **350 GB** in FP16 (every inference request loads these through the memory hierarchy — weight count is the largest determinant of memory footprint and serving cost).
- Trained on **~300B tokens** (~420 GB of filtered web text, books, Wikipedia), requiring an estimated **~314 zettaFLOPs** (10²¹ FLOPs each).
- **~1,287 MWh** of training energy and **552 tonnes CO₂e** (Patterson et al. 2021) — roughly 120 US-household-years; the energy is dominated by [[MemoryBandwidth|data movement]], not arithmetic.
- Iron-law worked example: ~1,024 A100s at 45% [[GPUUtilization|utilization]] → ~25 days; 60% → ~19 days.

GPT-3 is the [[EfficiencyFramework|efficiency paradox]] exemplar: despite ~44.5× per-FLOP gains since AlexNet, total training compute grew ~10⁷×, because efficiency savings were reinvested into scale.

## Connections

- [[GPT4]] — the successor scale anchor (~2.25M A100 GPU-days public estimate).
- [[BitterLesson]] / [[EfficiencyFramework]] — the scaling story it illustrates.
- [[IronLawOfMLSystems]] / [[MemoryBandwidth]] — its performance/energy analysis.
- [[FoundationModel]] / [[LargeLanguageModel]] — its category.
- [[ModelWeights]] — the 350 GB footprint.
- [[mlsysbook-ch01-introduction]] — source.
