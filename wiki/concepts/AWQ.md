---
title: "AWQ — Activation-aware Weight Quantization"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
Quantization that identifies salient weights by activation magnitude and rescales per channel.

## In LLM Engineer's Handbook
AWQ (Lin et al. 2024) identifies the most important weights by their corresponding activation magnitudes (rather than weight magnitudes) and applies optimal per-channel scaling to those salient weights. Per [[leh-ch08-inference-optimization]] AWQ is close in quality to [[GPTQ]] and [[EXL2]] but slightly slower; widely supported across [[TGI]], [[vLLM]], and [[TensorRTLLM]].
