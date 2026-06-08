---
title: "MLPerf Power"
type: concept
tags: [benchmarking, mlperf, energy, power, efficiency, mlsysbook]
sources: [mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# MLPerf Power

The cross-cutting [[MLPerf]] methodology (Tschand et al. 2025) that turns power measurement from a device-specific reading into a **comparable efficiency claim**: useful inferences per watt under an explicitly defined measurement boundary. Per [[mlsysbook-ch12-benchmarking|mlsysbook Ch 12]], it is the third leg (alongside training and inference benchmarks) that answers "*how much energy* does the system consume to achieve that speed?"

## Measurement boundaries

Where the boundary is drawn determines what counts as "efficient":
- **Tiny SoC** — the entire low-power SoC (compute, memory, basic switch) is inside the boundary.
- **Inference node** — multiple SoCs, accelerators, local RAM, NIC; *remote storage and off-chip components excluded*.
- **Training rack** — only selected compute nodes and network switches measured; *DC cooling and storage nodes excluded*.

## Challenges and findings

Power is *temporal*: a transformer attention layer can spike to **400 W then drop to 40 W within milliseconds**, demanding >1 kHz sampling; sliding-window averages over hundreds of inferences are needed. Cooling = **20–30% of facility power** ([[PowerUsageEffectiveness|PUE]] 1.1–2.0); DVFS-style management produces 30–50% power swings. Across releases, energy efficiency (samples/joule) improved **up to 378× for data-center Llama2** and **1070× for tinyML ResNet**, but traditional workloads (ResNet/BERT/RNN-T) have **plateaued** while generative AI shows large remaining headroom.

## Connections

- [[MLPerf]] / [[MLCommons]] — the benchmark family and consortium.
- [[ThermalThrottling]] — the sustained-vs-burst effect power benchmarks must capture.
- [[MemoryWall]] — data movement (e.g., 57.3% of TF Mobile inference energy) dominates the power profile.
- [[Quantization]] — INT8's ~5.4× MobileNet inference-energy reduction is the algorithmic lever power benchmarks reward.
- [[mlsysbook-ch12-benchmarking]] — source.
