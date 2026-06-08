---
title: "Compilation Continuum Principle"
type: concept
tags: [frameworks, performance, compilation, iron-law]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Compilation Continuum Principle

The execution models form a continuum from maximum flexibility to maximum optimization:

$$\text{Eager} \xrightarrow{\text{tracing}} \text{JIT} \xrightarrow{\text{AOT}} \text{Static Graph} \xrightarrow{\text{synthesis}} \text{Custom Hardware}$$

The **Compilation Continuum Principle** turns "where on this continuum should I operate?" into a calculation. The optimal strategy depends on the ratio of production executions to development iterations:

$$\text{Compilation Benefit} = \frac{N_{\text{prod}}(T_{\text{eager}}-T_{\text{compiled}})}{T_{\text{compile}}+N_{\text{dev}}\cdot T_{\text{compile}}}$$

Compile when Benefit > 1. Three regimes:

- **Research prototyping** ($N_{\text{dev}} \gg N_{\text{prod}}$) → stay [[EagerExecution|eager]]; recompiling every few minutes wastes more time than it saves.
- **Training** ($N_{\text{prod}} \gg N_{\text{dev}}$) → compile. ResNet-50 breakeven ≈ **134,000 images** at a 30 s compile cost — recouped within the first ImageNet epoch (1.28M images): $N_{\text{breakeven}} = T_{\text{compile}}/(T_{\text{eager}}-T_{\text{compiled}})$.
- **Production inference** ($N_{\text{dev}} \approx 0$, $N_{\text{prod}} \to \infty$) → maximize compilation (`max-autotune` despite hour-long compiles).

The principle pairs with the [[DispatchOverhead|Dispatch Overhead Law]] (per-operation cost). The same logic maps deployment tiers from [[EagerExecution|eager]] cloud frameworks down to [[TinyML]] [[StaticGraph|static]] micro-runtimes.

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — quantitative principles of execution.
- [[DispatchOverhead]] — the complementary per-op law.
- [[EagerExecution]] / [[JITCompilation]] / [[StaticGraph]] — the continuum's points.
- [[TorchCompile]] — the JIT step; [[TinyML]] — the AOT extreme.
