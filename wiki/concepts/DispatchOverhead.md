---
title: "Dispatch Overhead Law"
type: concept
tags: [frameworks, performance, execution-model, iron-law]
sources: [mlsysbook-ch07-ml-frameworks]
last_updated: 2026-06-05
---

# Dispatch Overhead Law

The **Dispatch Overhead Law** quantifies the regime in which framework overhead — rather than compute or memory — dominates execution time:

$$\text{Overhead Ratio} = \frac{N_{\text{ops}} \cdot t_{\text{dispatch}}}{T_{\text{compute}} + T_{\text{memory}}}$$

When the ratio > 1 the workload is **overhead-bound**, and [[JITCompilation|compilation]] provides maximum benefit because it eliminates per-operation dispatch. Per-op cost is ~10 μs of Python dispatch plus 5–20 μs of [[Kernel|kernel]] launch ("[[EagerExecution|the dispatch tax]]").

The regimes split sharply by model size:

- **Small MLP** (6 ops, ~2.6 μs hardware time, ~30 μs software overhead) → **~92% overhead-bound**; a 100-param toy model can see 10× from [[TorchCompile|torch.compile]].
- **GPT-3 layer** (~100 ms hardware, ~50 μs overhead) → **<0.05% overhead**; a 175-billion-param model sees only ~1.3×.

This is why compilation matters most for efficient inference on *smaller*, deployed models — and why large models benefit from compilation mainly via [[KernelFusion|kernel fusion]] (memory bandwidth) rather than dispatch elimination. It is the per-operation counterpart to the [[CompilationContinuum|Compilation Continuum Principle]].

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — quantitative principles of execution.
- [[CompilationContinuum]] — the complementary when-to-compile principle.
- [[EagerExecution]] — where the dispatch tax is paid; [[TorchCompile]] / [[KernelFusion]] — the fixes.
- [[IronLawOfMLSystems]] — overhead is the $L_{\text{lat}}$ term.
