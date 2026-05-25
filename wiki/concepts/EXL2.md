---
title: "EXL2"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
Mixed-precision per-layer quantization format that fits 70B models on a single 24 GB GPU.

## In LLM Engineer's Handbook
EXL2 (by [[Turboderp]] for [[ExLlamaV2]]) builds on the [[GPTQ]] algorithm but supports mixed precision per layer (e.g. 2.0, 2.55, 3.5, 4.5, 6.0 bits/weight). The quantizer auto-selects per-matrix precisions by quantizing each multiple times and picking the combination that minimizes calibration error at a target average bitrate. Per [[leh-ch08-inference-optimization]] EXL2 has the highest GPU throughput of the three compared formats (with [[GGUF]] and [[GPTQ]]); supported by [[TGI]] only.
