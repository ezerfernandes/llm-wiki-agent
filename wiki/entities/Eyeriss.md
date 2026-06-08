---
title: "Eyeriss"
type: entity
tags: [hardware, accelerator, cnn, dataflow, mit]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Eyeriss

Eyeriss is a pioneering CNN inference accelerator (Chen et al. 2016) that introduced the **row-stationary dataflow** to maximize data reuse for convolutional workloads.

## Significance ([[mlsysbook-ch11-hardware-acceleration]])

Eyeriss is the canonical example of the row/input-stationary strategy in the [[SystolicArray|systolic-array]] dataflow taxonomy — keeping input rows resident to balance input and weight reuse for general matrix multiplication, in contrast to [[WeightStationary|weight-stationary]] (CNN filters, early [[GoogleTPU|TPUs]]) and [[OutputStationary|output-stationary]] (large-batch matmul) designs. It established energy-efficient dataflow as a first-class accelerator design dimension for CNNs.

## See also
- [[WeightStationary]] / [[OutputStationary]] — the alternative dataflow strategies.
- [[SystolicArray]] — the architectural family.
- [[HardwareMapping]] — dataflow as a mapping decision.
- [[mlsysbook-ch11-hardware-acceleration]] — Eyeriss row-stationary dataflow.
