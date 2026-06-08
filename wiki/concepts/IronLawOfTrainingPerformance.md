---
title: "Iron Law of Training Performance"
type: concept
tags: [training, performance, ml-systems, mlsysbook, roofline]
sources: [mlsysbook-ch08-model-training]
last_updated: 2026-06-05
---

# Iron Law of Training Performance

A specialization of the general [[IronLawOfMLSystems|iron law of ML systems]] that isolates the computational bottleneck of iterative optimization:

$$T_{\text{train}} = \frac{O}{R_{\text{peak}} \times \eta_{\text{hw}}}$$

where **$O$** = total operations (reducible by pruning, distillation, sparsity, fewer training tokens), **$R_{\text{peak}}$** = peak hardware throughput (improved by faster accelerators and lower-precision Tensor Cores), and **$\eta_{\text{hw}}$** = hardware utilization (the primary engineering target).

Introduced in [[mlsysbook-ch08-model-training|*Machine Learning Systems* (mlsysbook Vol 1) Ch 8]] as the chapter's organizing framework: **every training optimization maps to exactly one term**. Mixed precision raises $R_{\text{peak}}$; data prefetching, gradient accumulation, and operator fusion raise $\eta_{\text{hw}}$; gradient checkpointing trades extra $O$ for memory capacity; [[FlashAttention]] cuts memory traffic and raises $\eta_{\text{hw}}$.

## Key Points

- **Validity condition**: the simplified form holds only when the pipeline is correctly staged — data movement ($D_{\text{vol}}/\text{BW}$) overlapped via prefetching and communication ($L_{\text{lat}}$) absorbed by gradient overlap. For small-batch or bandwidth-limited workloads the dropped terms resurface and the simplification breaks.
- **$\eta_{\text{hw}}$ is not fixed by hardware** — memory-bandwidth saturation, kernel-launch overhead, and synchronization barriers each erode it independently; diagnosis requires profiling, not spec sheets. Measured concretely as [[MFU]].
- GPT-3 training achieved $\eta_{\text{hw}}\approx0.45$; modern systems target $>0.55$. The theory-to-practice gap is typically **2–3×**.
- The law captures *execution efficiency* only — it does not model data quality, dataset size, or curriculum, which change $O$ (the number of operations needed to reach a target accuracy) independently of hardware.

## Connections

- [[IronLawOfMLSystems]] — the parent law (models all three of $D_{\text{vol}}/\text{BW}$, $O/(R_{\text{peak}}\cdot\eta_{\text{hw}})$, $L_{\text{lat}}$).
- [[MFU]] — the $\eta_{\text{hw}}$ term made measurable.
- [[RooflineModel]] / [[ArithmeticIntensity]] — the diagnostic for whether a workload is compute- or memory-bound.
- [[MixedPrecisionTraining]] / [[GradientCheckpointing]] / [[GradientAccumulation]] / [[FlashAttention]] / [[DataPrefetching]] — each maps to a specific term.
- [[DAMTaxonomy]] — the bottleneck classification that guides which term to attack.
- [[mlsysbook-ch08-model-training]] — defining source.
