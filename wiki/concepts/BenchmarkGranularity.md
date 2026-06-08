---
title: "Benchmark Granularity"
type: concept
tags: [benchmarking, ml-systems, profiling, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Benchmark Granularity

The level of detail at which evaluation occurs. Standardization specifies *how* measurement is consistent; granularity specifies *what* is measured ([[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]]). Three levels, each revealing different problems:

- **Micro benchmarks** — isolate individual components (kernel time, memory bandwidth, single-layer accuracy). Diagnose *where* problems occur. Tools: cuDNN, Baidu's DeepBench, framework profilers (PyTorch Profiler — logical step-time breakdown) and kernel profilers (Nsight Systems/Compute — physical roofline analysis). Recommended workflow: framework profiler finds the slow layer, kernel profiler diagnoses the physics.
- **Macro benchmarks** — evaluate complete models (ResNet-50 on ImageNet; EEMBC MLMark; AI-Benchmark). Reveal *what* problems exist (accuracy, memory, throughput, latency interacting at model scale).
- **End-to-end benchmarks** — measure full workflows (ETL → preprocessing → inference → postprocessing → infrastructure). Show *whether the system works*. Largely proprietary; no public benchmark fully accounts for storage + network + compute.

The core tension is **isolation/diagnostic power vs. real-world representativeness**: micro pinpoints the slow kernel but misses system bottlenecks; end-to-end captures production behavior but obscures root causes. A 3× kernel speedup can deliver zero end-to-end gain if the data pipeline cannot keep pace. Effective evaluation combines all three.

## Connections

- [[Benchmarking]] — the discipline this structures.
- [[BenchmarkComponents]] — every granularity level must still specify task/data/model/metrics/harness.
- [[AmdahlsLaw]] — why component (micro) speedups dilute at end-to-end scale.
- [[RooflineModel]] — the kernel-profiler diagnostic at micro granularity.
- [[mlsysbook-ch12-benchmarking]] — source.
