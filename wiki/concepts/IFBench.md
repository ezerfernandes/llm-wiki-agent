---
title: "IFBench"
type: concept
tags: [benchmark, instruction-following, evaluation]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# IFBench

**Instruction-Following Bench** (Pyatkin et al. 2025). Evaluates whether LLMs comply with detailed natural-language instructions — multi-part constraints, formatting demands, conditional rules — without sacrificing answer correctness. Used by [[2507.19457-gepa|GEPA]] as one of six core benchmarks alongside [[hotpotqa|HotpotQA]], [[HoVer]], [[PUPA]], [[AIME2025]], [[LiveBenchMath]].

## GEPA results on IFBench

| Optimizer | Qwen3 8B | GPT-4.1 Mini |
|---|---|---|
| Baseline | 36.90 | 47.79 |
| [[grpo|GRPO]] | 35.88 | — |
| [[MIPROv2]] (full) | 36.22 | 49.15 |
| MIPROv2-No-Demos | — | 52.04 |
| TextGrad | — | 48.64 |
| Trace (OptoPrime) | — | 51.19 |
| **GEPA** | **38.61** | 52.72 |
| **GEPA+Merge** | 28.27 | **55.95** |

Notable: IFBench is the only benchmark where GEPA+Merge **degrades** Qwen3 performance (28.27 vs 36.90 baseline) — flagged in the paper as evidence that Merge's invocation timing matters and should be adaptive.

## Connections
- [[2507.19457-gepa]] — uses IFBench as a core benchmark.
- [[PromptOptimization]] — instruction-following is the natural target of instruction-optimization.
- [[GEPA]] — the optimizer; biggest IFBench gain came from GEPA+Merge on GPT-4.1 Mini (+8 over baseline).
