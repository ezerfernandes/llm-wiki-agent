---
title: "Benchmark Engineering"
type: concept
tags: [benchmarking, gaming, goodharts-law, mlperf, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Benchmark Engineering

The intentional practice of optimizing a model or system specifically to excel on a benchmark's unique characteristics rather than to improve real-world performance — the [[GoodhartsLaw|Goodhart's Law]] dynamic made deliberate ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]]). Distinct from the unintended [[HardwareLottery|hardware lottery]], benchmark engineering (a.k.a. **benchmark gaming**) sits at the blurry threshold where legitimate tuning crosses into overfitting to the test.

Common submission-specific gaming techniques:
- **Precision dropping** — a compiler silently reduces precision (FP32 → BF16) *only during the benchmark run* to inflate throughput.
- **Operator removal** — deleting activation functions or layer-norms the benchmark's top-1 metric doesn't reward, yielding unrealistic speedups.
- **Weight preloading** — hardcoding the model's weights into on-chip SRAM, bypassing the [[MemoryWall|memory-wall]] bottlenecks production models face.

[[MLPerf]] prevents these via **Reference-vs-Submission validation**: every submitter must run the same model structure and hit a verifiable accuracy target (e.g., 75.9% on ImageNet). A submission that drops precision or removes operators fails the accuracy guardrail and is disqualified — turning a speed test into a rigorous engineering benchmark. Mitigations: transparency (document all optimizations), third-party verification, diversified/continuously-updated benchmarks, and multi-hardware testing.

## Connections

- [[GoodhartsLaw]] — the principle benchmark engineering embodies ("when a measure becomes a target...").
- [[HardwareLottery]] — the unintended counterpart bias.
- [[MLPerf]] / [[MLCommons]] — the accuracy guardrail and open-submission rules that deter gaming.
- [[BenchmarkContamination]] — the LLM-specific memorization analogue.
- [[BenchmarkSaturation]] — the related obsolescence failure mode.
- [[mlsysbook-ch12-benchmarking]] — source.
