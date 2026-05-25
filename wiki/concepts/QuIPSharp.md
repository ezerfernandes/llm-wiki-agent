---
title: "QuIP#"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
Extreme low-bit quantization using Quantization with Incoherence Processing.

## In LLM Engineer's Handbook
QuIP# is an extreme low-bit (1-2 bit) quantization technique that uses incoherence processing — multiplying weights and Hessians by random orthogonal matrices — to make the distribution easier to quantize. Per [[leh-ch08-inference-optimization]] it inspires the `IQ*` i-quants in [[GGUF]] / [[llamacpp]] and is particularly attractive for very large models (>30B) where post-quantization quality remains competitive with smaller unquantized models.
