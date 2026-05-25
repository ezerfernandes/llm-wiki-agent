---
title: "MFU (Model FLOP/s Utilization)"
type: concept
tags: [inference, training, performance, metrics, gpu]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
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

## Connections

- [[MBU]] — companion utilization metric (bandwidth side).
- [[GPUUtilization]] — the `nvidia-smi` metric MFU corrects for.
- [[ComputeBound]] / [[MemoryBandwidthBound]] — the regimes MFU/MBU diagnose.
- [[PaLM]] — the paper that named MFU.
- [[InferenceOptimization]] — discipline that uses MFU.
- [[Prefill]] / [[Decode]] — phases with asymmetric MFU.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
