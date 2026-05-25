---
title: "TGI (Text Generation Inference)"
type: entity
tags: [tool]
sources: [leh-ch08-inference-optimization, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
Alias for [[TextGenerationInference]]; Hugging Face's production LLM serving framework.

## In LLM Engineer's Handbook
TGI is the short alias for [[TextGenerationInference]] — Hugging Face's production LLM serving framework (`huggingface/text-generation-inference`). Per [[leh-ch08-inference-optimization]] it is the most feature-complete of the three main inference engines (alongside [[vLLM]] and [[TensorRTLLM]]): [[ContinuousBatching]], [[SpeculativeDecoding]], [[FlashAttention2]], [[PagedAttention]], [[TensorParallelism]], and [[GPTQ]] / [[EXL2]] / [[AWQ]] support. [[leh-ch10-inference-pipeline-deployment]] uses it inside the [[HuggingFaceDLC]] for SageMaker deployment.
