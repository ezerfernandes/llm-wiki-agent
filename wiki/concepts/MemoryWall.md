---
title: "Memory Wall"
type: concept
tags: [hardware, performance, mlsysbook, physics, serving]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch05-neural-computation, mlsysbook-ch07-ml-frameworks, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

# Memory Wall

The **binding constraint of the single-node regime**: the rate at which data moves from high-bandwidth memory (HBM) to compute units, which faster arithmetic cannot overcome. Named as one of the book's invariants in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]).

Volume 1 covers the single-node regime (1–8 accelerators connected by shared memory) where the memory wall sets the bandwidth ceiling. Volume 2 extends to the **distributed fleet** regime (thousands of nodes across network fabrics) where the bottleneck shifts to *bisection bandwidth* between nodes. The memory wall is presented as a physical constraint "as permanent as Ohm's law or the speed of light" — no software optimization can repeal it.

[[mlsysbook-ch02-ml-systems|Ch 2]] quantifies the divergence: compute capacity doubles ~every 18 months, but memory bandwidth grows only ~20%/year — a ≈1.33× annual gap (term coined by Wulf & McKee, 1995). This is one of the three physical constraints (with the light barrier and [[PowerWall|power wall]]) that carve the [[DeploymentSpectrum|deployment spectrum]] into four paradigms. It explains why batch-1 inference is memory-bound on *both* a cloud A100 and a mobile NPU, and why [[Quantization|quantization]] (reducing bytes) often beats faster hardware (more FLOP/s).

[[mlsysbook-ch07-ml-frameworks|Ch 7]] makes the memory wall *the* driver of framework optimization: on an A100 (312 TFLOP/s vs 2.04 TB/s → ~153 FLOP/byte ridge point), element-wise ReLU hits <1% of peak compute, so [[KernelFusion|kernel fusion]], [[ActivationCheckpointing|activation checkpointing]], [[MixedPrecisionTraining|mixed precision]], and layout optimization all target the data-movement term $D_{\text{vol}}$, *not* compute. "Compute has grown ~1000× faster than memory bandwidth."

## Connections

- [[mlsysbook-ch07-ml-frameworks]] — the memory wall as the master driver of framework optimization.
- [[MemoryBandwidth]] — the rate the wall caps.
- [[IronLawOfMLSystems]] — the data term the wall bounds.
- [[PowerWall]] / [[SpeedOfLight]] — the other two physical constraints shaping the deployment spectrum.
- [[RooflineModel]] / [[ArithmeticIntensity]] — visualizes memory-bound vs compute-bound regimes.
- [[DAMTaxonomy]] — the Machine-axis constraint.
- [[WeightMatrix]] / [[MemoryBound]] / [[mlsysbook-ch05-neural-computation]] — Ch 5 grounds the wall in neural computation: weights are *distributed* across all parameters (every prediction reads a large fraction), even the MNIST net (~438 KB FP32) overflows L1, and *data movement dominates energy*, driving data-reuse-maximizing accelerators.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] — sources.
- [[mlsysbook-ch11-hardware-acceleration]] — Ch 11 is the definitive treatment: the Horowitz energy ladder (DRAM 640 pJ vs SRAM 5 pJ vs INT8-add 0.03 pJ, ~128× gap; DRAM >20,000× an INT8 op), the [[VonNeumannArchitecture|Von Neumann]] origin, the "distance wall" (speed-of-light limit: 20 mm at ~0.5c can't be fetched in one 2 GHz cycle), the bandwidth taper (HBM ≫ NVLink ≫ PCIe ≫ network), and model-size growth (10,000×) outpacing bandwidth (16×).
- [[mlsysbook-ch12-benchmarking]] — Ch 12 frames the memory wall as the *structural* reason peak ≠ sustained (the 2–3.5× MFU gap is "structurally guaranteed by the memory wall, not an anomaly"), and quantifies its energy dominance in [[Benchmarking|benchmarking]]: register→DRAM costs ~16,000× per byte, data movement = 57.3% of TF Mobile inference energy, so [[Quantization|INT8]] yields ~5.4× MobileNet inference-energy reduction by attacking memory traffic.
- [[mlsysbook-ch13-model-serving]] — Ch 13 makes the memory wall *the* governing constraint of LLM decode ([[LLMServing|LLM serving]]): arithmetic intensity ≈ 1 FLOP/byte (every weight read per token), so $T_{\text{token}} \approx D_{\text{vol}}/\text{BW}$ and "adding compute cores yields zero latency improvement; only faster memory or smaller models help." Bounds [[TPOT]]; the [[KVCache|KV cache]] adds to the per-token bytes moved.
