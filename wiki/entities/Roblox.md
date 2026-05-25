---
name: Roblox
title: "Roblox"
type: entity
tags: [company, gaming, ml-deployment]
sources: [dmls-ch07-model-deployment]
last_updated: 2026-05-23
---

# Roblox

US online-gaming platform. Cited in [[ChipHuyen|Huyen]]'s [[dmls-ch07-model-deployment|DMLS Ch 7]] as the canonical case study for **[[Quantization|FP32 → INT8 quantization]] of large transformer models for CPU inference**.

## DMLS Ch 7 case study — BERT-on-CPU at 1B+ daily inferences
Roblox needed to deploy [[bert|BERT]]-based moderation / chat-filtering models at platform scale. Result of quantization:
- **7× latency reduction** (FP32 → INT8).
- **8× throughput increase** on CPU.
- **1B+ daily inferences at <20 ms** end-to-end.

Cited as the proof point that large transformer models can be made cost-effective on CPU via aggressive [[ModelCompression|model compression]] — even before edge-LLM optimization became mainstream in 2023–2024.

## Connections
- [[ChipHuyen]] — DMLS author who anchored this case study.
- [[Quantization]] — the technique whose impact Roblox demonstrated.
- [[ModelCompression]] — the broader family.
- [[bert]] — the model architecture Roblox quantized.
- [[InferenceOptimization]] — the broader discipline.
- [[EdgeComputing]] — adjacent regime (though Roblox uses datacenter CPU, the techniques transfer).
