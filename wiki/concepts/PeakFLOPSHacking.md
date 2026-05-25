---
title: "Peak FLOP/s Hacking"
type: concept
tags: [hardware, gpu, performance, vendor-claims]
sources: [ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Peak FLOP/s Hacking

**[[ChipHuyen|Chip Huyen]]'s term for chip-maker benchmark gaming** — running peak-throughput experiments under specially-favorable conditions (sparse matrices with specific shapes, etc.) to inflate the headline FLOP/s number. From [[ai-engineering-ch09-inference-optimization|*AI Engineering* Ch 9]]:

> *"Chip makers might also be doing what I call peak FLOP/s hacking. This might run experiments in certain conditions, such as using sparse matrices with specific shapes, to increase their peak FLOP/s. Higher peak FLOP/s numbers make their chips more attractive, but it can be harder for users to achieve high MFU."*

## What gets inflated

The classic vehicle: **"with sparsity"** numbers. NVIDIA's H100 spec table (reproduced as Table 9-2 in Ch 9) reports peak FLOP/s "with sparsity" — assuming the workload matches the 2:4 structured-sparsity pattern. Most real workloads don't.

Example: H100 SXM reports FP8 Tensor Core throughput of **3,958 teraFLOP/s with sparsity**. The dense FP8 number is roughly half.

## Why it matters to AI engineers

The headline number on the chip spec sheet → user expectation → user buys the chip → real workload hits **30% [[MFU|MFU]]** → user is disappointed.

Huyen's implicit recommendation: **read the fine print** on whether peak FLOP/s claims assume sparsity / specific data formats / specific shapes / specific kernels. Compare like-for-like across vendors.

## Sparsity is the most common vehicle

- **NVIDIA Ampere+** — 2:4 structured sparsity gives 2× over dense for tensor-core paths.
- **Other vendors** — similar tricks for their structured-sparsity formats.

If your workload isn't sparse in the structured way the chip supports, the inflated peak number is unreachable.

## Related: the MFU vs claimed-peak gap

[[MFU|Model FLOP/s Utilization]] measures *actual* throughput / *claimed* peak. The gap between MFU and 100% includes:

1. **Real inefficiency** — your kernel isn't optimal.
2. **Peak FLOP/s hacking** — the claimed peak was never achievable without the gaming.

Distinguishing the two requires comparing against **dense, non-gamed** peak numbers — sometimes published as a separate "dense" or "non-sparsity" entry.

## Connections

- [[MFU]] — the metric that catches the gaming.
- [[Sparsity]] — the most common vehicle for peak FLOP/s gaming.
- [[ChipHuyen]] — coined the phrase.
- [[NVIDIA]] / [[GoogleTPU]] / [[AMD]] / etc. — vendors whose claims this critique applies to.
- [[AIAccelerator]] — the chips whose peak claims are at stake.
- [[InferenceOptimization]] — broader discipline.
- [[ai-engineering-ch09-inference-optimization]] — primary source.
