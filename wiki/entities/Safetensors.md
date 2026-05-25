---
title: "safetensors"
type: entity
tags: [tool, serialization, huggingface, llm]
sources: [leh-ch08-inference-optimization, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
safetensors is [[HuggingFace|Hugging Face]]'s open tensor-serialization format (`huggingface/safetensors`). It is designed for safety (no arbitrary code execution at load time, unlike pickle / PyTorch `.bin` checkpoints) and speed (zero-copy mmap loading).

## In LLM Engineer's Handbook
[[leh-ch10-inference-pipeline-deployment]] highlights safetensors as one of the headline features of [[TextGenerationInference|TGI]]: fast and safe weight loading is what makes SageMaker endpoint cold-starts tolerable when serving multi-billion-parameter LLMs. [[leh-ch08-inference-optimization]] references the format in the context of [[InferenceOptimization]] more broadly — quantized model files ([[GGUF]], [[GPTQ]], [[AWQ]], [[EXL2]]) and weight-loading speed are the two halves of inference-engine startup.

## Connections
- [[HuggingFace]] — maintainer.
- [[TextGenerationInference]] — primary consumer in the chapter.
- [[HuggingFaceDLC]] — packaging container that bundles TGI + safetensors.
- [[Bitsandbytes]] / [[GGUF]] — adjacent weight formats in the same memory-efficiency family.
