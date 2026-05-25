---
title: "GGUF"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, leh-ch08-inference-optimization, hands-on-llm-ch06-prompt-engineering, hands-on-llm-ch07-advanced-text-generation]
last_updated: 2026-05-23
---

## Definition
llama.cpp's quantization file format (1-8 bit grid).

## In LLM Engineer's Handbook
GGUF (GPT-Generated Unified Format) is the single-file quantized model container used by [[llamacpp]]. Supports bitrates from 1-bit (`IQ1_S/M`) to 8-bit (`Q8_0`), with intermediate options (`Q2_K`, `Q3_K_S/M/L`, `Q4_K_M`, `Q5_K_M`, `Q6_K`). Weights are organized into 32-value blocks and 8-block super-blocks with per-block scales. The `IQ*` i-quants use an E8 lattice inspired by [[QuIPSharp]].

## In *Hands-On LLMs* Chs 6–7

[[hands-on-llm-ch06-prompt-engineering|Ch 6]] uses GGUF [[Phi3Mini|Phi-3-mini]] loaded via `llama-cpp-python` for **grammar-constrained JSON decoding** with `response_format={"type": "json_object"}`. [[hands-on-llm-ch07-advanced-text-generation|Ch 7]] uses an **8-bit GGUF Phi-3** variant (vs Ch 6's fp16) via [[LangChain]]'s `LlamaCpp` wrapper for chains and memory — *"a GGUF model represents a compressed version of its original counterpart through a method called quantization, which reduces the number of bits needed to represent the parameters of an LLM."* Ch 7 frames the **rule of thumb**: *"look for at least 4-bit quantized models. These models have a good balance between compression and accuracy. Although it is possible to use 3-bit or even 2-bit quantized models, the performance degradation becomes noticeable and it would instead be preferable to choose a smaller model with a higher precision."* Per [[leh-ch05-supervised-fine-tuning]], [[Unsloth]] auto-converts fine-tuned models to GGUF. Per [[leh-ch05-supervised-fine-tuning]], [[Unsloth]] auto-converts fine-tuned models to GGUF.
