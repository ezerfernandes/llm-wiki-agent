---
title: "MFU (Model FLOP/s Utilization)"
type: concept
tags: [inference, training, performance, metrics, gpu]
sources: [ai-engineering-ch09-inference-optimization, mlsysbook-ch08-model-training, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# MFU — Model FLOP/s Utilization

**The ratio of observed throughput (tokens/s) to the theoretical maximum throughput at peak FLOP/s.** Introduced in the [[PaLM]] paper (Chowdhery et al. 2022); the metric AI engineers should care about *instead of* `nvidia-smi`'s misleading "GPU utilization." Per [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"MFU is the ratio of the observed throughput (tokens/s) relative to the theoretical maximum throughput of a system operating at peak FLOP/s. If at the peak FLOP/s advertised by the chip maker, the chip can generate 100 tokens/s, but when used for your inference service, it can generate only 20 tokens/s, your MFU is 20%."*

## Why MFU exists (the nvidia-smi critique)

`nvidia-smi`'s GPU utilization reports the **percentage of time the GPU is actively processing something** — not what fraction of its peak FLOP/s it's achieving. Huyen's example: a chip capable of 100 ops/s doing 1 op/s reports 100% utilization. **You can pay for 100 ops and use 1.** MFU is the metric that catches this gap.

## MFU values from PaLM paper (Table 9-1)

Reproduced in Ch 9:

| Model | Params | Accelerator | MFU |
|---|---|---|---|
| GPT-3 | 175B | V100 | **21.3%** |
| Gopher | 280B | 4096 TPU v3 | **32.5%** |
| Megatron-Turing NLG | 530B | 2240 A100 | **30.2%** |
| PaLM | 540B | 6144 TPU v4 | **46.2%** |

> *"For model training, as of this writing, an MFU above 50% is generally considered good, but it can be hard to achieve on specific hardware."* — Ch 9

## MFU at inference vs training

- **Training MFU > Inference MFU** in general — training has more predictable, batchable workloads.
- Within inference: **MFU during [[Prefill|prefill]] > MFU during [[Decode|decode]]** — prefill is [[ComputeBound|compute-bound]] (matches MFU's measure); decode is [[MemoryBandwidthBound|memory bandwidth-bound]] (limited by bandwidth, not FLOPs).

## MFU vs MBU

- **[[ComputeBound|Compute-bound]]** workloads → **high MFU**, lower [[MBU|MBU]].
- **[[MemoryBandwidthBound|Memory-bandwidth-bound]]** workloads → **low MFU**, higher MBU.

Reading both together diagnoses which optimization lever helps.

## "Peak FLOP/s hacking"

Huyen's term for chip-maker benchmark gaming:

> *"This might run experiments in certain conditions, such as using sparse matrices with specific shapes, to increase their peak FLOP/s. Higher peak FLOP/s numbers make their chips more attractive, but it can be harder for users to achieve high MFU."* — Ch 9 footnote

In other words: a 50% MFU on a high-claimed-peak chip may be lower absolute throughput than a 70% MFU on a lower-claimed-peak chip.

## MFU is not the goal

> *"Higher utilization rates for similar workloads on the same hardware generally mean that your services are becoming more efficient. However, the goal isn't to get the chips with the highest utilization. What you really care about is how to get your jobs done faster and cheaper."* — Ch 9

A higher MFU at the cost of more latency or cost is *not* a win. MFU is diagnostic, not the objective.

## Training-side framing from [[mlsysbook-ch08-model-training|mlsysbook Ch 8]]

Ch 8 (the training capstone) defines MFU for **training** as a *FLOP-ratio* rather than a throughput-ratio: $\text{MFU} = O_{\text{model}} / (R_{\text{peak}} \cdot T_{\text{step}})$, where $O_{\text{model}}$ counts only convergence-advancing forward+backward FLOPs (excluding gradient-checkpointing recomputation and padding). This is **the $\eta_{\text{hw}}$ term of the [[IronLawOfTrainingPerformance|iron law of training]] made concrete**. Same PaLM provenance and intent as the inference framing; treat MFU as one metric with a training/inference split rather than two metrics. Practical training ceiling is **55–65%** (only with [[FlashAttention]] + tuned batch sizes); 100% is impossible because weights must still load from DRAM. The chapter ties MFU directly to the [[DAMTaxonomy]] for bottleneck diagnosis.

## Connections

- [[mlsysbook-ch08-model-training]] — the training-side FLOP-ratio definition; MFU as the iron-law $\eta_{\text{hw}}$ term.
- [[IronLawOfTrainingPerformance]] — MFU *is* the utilization term.
- [[DAMTaxonomy]] — MFU value + symptoms classify the bottleneck axis.
- [[MBU]] — companion utilization metric (bandwidth side).
- [[GPUUtilization]] — the `nvidia-smi` metric MFU corrects for.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the regimes MFU/MBU diagnose.
- [[PaLM]] — the paper that named MFU.
- [[InferenceOptimization]] — discipline that uses MFU.
- [[Prefill]] / [[Decode]] — phases with asymmetric MFU.
- [[mlsysbook-ch12-benchmarking]] — [[Benchmarking|benchmarking]] (Ch 12) is what *measures* MFU empirically: it defines ML system benchmarks as isolating $\eta_{\text{hw}} = R_{\text{sustained}}/R_{\text{peak}}$, reports transformer training sustaining 30–50% MFU (a 2–3.5× peak-vs-sustained gap), and treats the [[BenchmarkEngineering|peak-FLOP/s gaming]] MFU exposes as a disqualifiable practice.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
