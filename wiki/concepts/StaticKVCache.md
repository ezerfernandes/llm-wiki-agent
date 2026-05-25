---
title: "Static KV Cache"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
Pre-allocated KV cache enabling torch.compile fusion.

## In LLM Engineer's Handbook
Pre-allocated [[KVCache]] variant that is fixed-size. Because shape is constant during decoding, the forward pass becomes amenable to [[TorchCompile]] graph fusion — reportedly yielding up to 4x forward-pass speedup in Hugging Face `transformers`. Configured with `model.generation_config.cache_implementation = "static"`. Per [[leh-ch08-inference-optimization]] architecture support is partial.
