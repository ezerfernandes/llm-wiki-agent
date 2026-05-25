---
title: "GPTQ"
type: concept
tags: [llm-engineering]
sources: [leh-ch08-inference-optimization]
last_updated: 2026-05-22
---

## Definition
GPU-targeted 4-bit post-training quantization algorithm (Frantar et al. 2023).

## In LLM Engineer's Handbook
GPTQ (Frantar et al. 2023) is a one-shot post-training quantization algorithm that refines Optimal Brain Quantization for LLM-scale matrices via Cholesky-decomposed Hessian inverse and lazy batched column updates. Limited to 4-bit precision. Per [[leh-ch08-inference-optimization]] inference runs through [[ExLlamaV2]]; supported by [[TGI]] and [[TensorRTLLM]] (not [[vLLM]]).
