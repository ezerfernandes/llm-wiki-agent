---
title: "LiveBench-Math"
type: concept
tags: [benchmark, math, contamination-free, evaluation]
sources: [2507.19457-gepa]
last_updated: 2026-05-22
---

# LiveBench-Math

The math subset of **LiveBench** (White et al., 2025) — a continuously-updated benchmark designed to be **contamination-free** by sourcing problems from recent competition mathematics and other live sources, releasing only on a rolling basis to minimize training-data leakage.

Used by [[2507.19457-gepa|GEPA]] as one of six core benchmarks, alongside [[AIME2025]] for math reasoning.

## GEPA results on LiveBench-Math

| Optimizer | Qwen3 8B | GPT-4.1 Mini |
|---|---|---|
| Baseline | 48.70 | 60.74 |
| [[grpo|GRPO]] | 51.26 | — |
| [[MIPROv2]] | 46.60 | 61.84 |
| **GEPA** | **51.95** | **64.13** |
| **GEPA+Merge** | **51.95** | **64.13** |

## Connections
- [[2507.19457-gepa]] — uses LiveBench-Math as a core benchmark.
- [[AIME2025]] — sibling math benchmark.
- [[grpo|GRPO]] — competitive with GEPA on Qwen3 LiveBench-Math (51.26 vs 51.95).
