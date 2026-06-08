---
title: "Output-Stationary Dataflow"
type: concept
tags: [hardware, accelerators, dataflow, systolic-array]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Output-Stationary Dataflow

**Output-stationary** is one of the three [[SystolicArray|systolic-array]] dataflow strategies. It keeps the **partial sums (accumulators, $C$)** resident in local memory while weights and input activations stream through, then writes each final output exactly once. This maximizes accumulator reuse and minimizes partial-sum memory traffic.

## When it wins ([[mlsysbook-ch11-hardware-acceleration]])

Output-stationary execution suits **large-batch matrix multiplication** — accumulating results for many inputs against a large weight matrix — and fully connected layers where reducing partial-sum write traffic matters most. [[NVIDIA]] tensor cores favor this pattern for fully connected layers. It contrasts with [[WeightStationary|weight-stationary]] (CNN filters) and row/input-stationary ([[Eyeriss]], general matmul) strategies.

## See also
- [[WeightStationary]] — the weight-reuse counterpart.
- [[SystolicArray]] — the architecture this dataflow configures.
- [[HardwareMapping]] — per-layer dataflow selection (hybrid mapping).
- [[mlsysbook-ch11-hardware-acceleration]] — the dataflow-strategy table.
