---
title: "Weight-Stationary Dataflow"
type: concept
tags: [hardware, accelerators, dataflow, systolic-array]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Weight-Stationary Dataflow

**Weight-stationary** is one of three dataflow strategies for [[SystolicArray|systolic arrays]] (alongside [[OutputStationary|output-stationary]] and input/row-stationary). The strategy pins a chosen operand in local registers to minimize its movement; because systolic arrays *physically fix* how data flows, this choice is a permanent architectural commitment made at chip-design time.

## The three strategies ([[mlsysbook-ch11-hardware-acceleration]])

| Strategy | Stationary item | Optimized for | Example workload |
|---|---|---|---|
| **Weight-stationary** | weights ($W$) | high weight reuse | CNNs (Conv2D): small filters reused across the image |
| **Output-stationary** | partial sums ($C$) | accumulator reuse | large-batch matmul |
| **Row/input-stationary** | input rows ($A$) | balanced reuse | general matmul ([[Eyeriss]]) |

## Why it matters

Weight-stationary execution suits CNNs and MLPs, where filters/weights are reused many times. Early [[GoogleTPU|TPUs]] used it. But "there is no perfect accelerator": a weight-stationary chip struggles with small-batch LLM inference, where the weight matrix is read once per token with minimal reuse — pushing designs toward output-stationary or hybrid patterns. This is why [[HardwareMapping|hybrid mapping]] switches strategy at layer boundaries.

## See also
- [[OutputStationary]] — the partial-sum-stationary counterpart.
- [[SystolicArray]] — the architecture whose dataflow this fixes.
- [[Eyeriss]] — the row-stationary CNN accelerator.
- [[HardwareMapping]] — selecting dataflow per layer.
- [[mlsysbook-ch11-hardware-acceleration]] — the stationary-operand dilemma.
