---
title: "Cerebras"
type: entity
tags: [company, hardware, ai-accelerator, semiconductor]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Cerebras

**Sunnyvale-based AI hardware company; designer of the Wafer-Scale Engine (WSE) — the largest computer chip ever built.** Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"The success of NVIDIA GPUs has inspired many accelerators designed to speed up AI workloads, including ... Cerebras' Wafer-Scale Quant Processing Unit (QPU), and many more being introduced."*

## The Wafer-Scale Engine

Cerebras's distinguishing claim: instead of cutting silicon wafers into many chips and connecting them via PCIe / NVLink, they use **an entire wafer as one chip**. The result is dramatically more on-chip memory and bandwidth than any GPU, eliminating much of the off-chip-communication penalty.

- **WSE-3** (current generation): 4 trillion transistors, 900,000 cores, 44 GB on-chip SRAM.
- For comparison: NVIDIA H100 has 80 billion transistors and ~40 MB on-chip SRAM.

## Where Cerebras appears in Ch 9

Beyond the accelerator-list mention, Cerebras is cited for an experiment about inference-service-provider model-quality variation:

> *"An inference service provider might use optimization techniques that can alter a model's behavior, causing different providers to have slight model quality variations. The experiment was conducted by Cerebras (2024)."* — Figure 9-8 caption

This is Ch 9's evidence that **inference optimizations can change model behavior** — a load-bearing claim for the chapter's "model-level optimization ≠ free" caveats.

## Connections

- [[AIAccelerator]] — umbrella category.
- [[NVIDIA]] / [[AMD]] / [[Groq]] / [[Graphcore]] — competing AI accelerators.
- [[Quantization]] / [[ModelCompression]] — the optimizations Cerebras's experiment showed can shift model behavior.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
