---
title: "Computational Photography"
type: concept
tags: [ml-systems, mobile, computer-vision, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Computational Photography

The use of ML algorithms (multi-frame fusion, neural denoising, depth estimation, segmentation) to **overcome the physical limits of small mobile camera sensors**. In [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]) it is the exemplar of the [[MobileML|mobile]] multi-pipeline thermal-budget problem.

Modern flagships run every photo through **10–15 distinct ML models in real time** — portrait mode (depth + segmentation), night mode (9–15-frame capture + alignment + denoising), HDR merge, super-resolution, scene optimization. The engineering challenge is not any single model but the *pipeline*: it must complete within the user's perceived ~200 ms shutter delay while sharing a single 2–5 W thermal budget, forcing careful scheduling across the [[SystemOnChip|SoC]]'s CPU, GPU, and [[NeuralProcessingUnit|NPU]] to avoid [[ThermalThrottling|throttling]].

## Connections

- [[MobileML]] — the paradigm; computational photography is its canonical multi-model workload.
- [[SystemOnChip]] / [[NeuralProcessingUnit]] — the heterogeneous hardware the pipeline schedules across.
- [[ThermalWall]] / [[ThermalThrottling]] — the shared budget the pipeline must respect.
- [[mlsysbook-ch02-ml-systems]] — source.
