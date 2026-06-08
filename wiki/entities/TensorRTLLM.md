---
title: "TensorRT-LLM"
type: entity
tags: [tool, inference, nvidia, serving]
sources: [leh-ch08-inference-optimization, ai-engineering-ch09-inference-optimization, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch13-model-serving]
last_updated: 2026-06-05
---

## What it is
NVIDIA's TensorRT-backed inference library for LLMs.

## In LLM Engineer's Handbook
TensorRT-LLM (`NVIDIA/TensorRT-LLM`, 2023) is [[NVIDIA]]'s open-source inference library built on TensorRT for serving LLMs. Per [[leh-ch08-inference-optimization]], it supports continuous batching, [[FlashAttention2]], [[PagedAttention]], [[TensorParallelism]], [[PipelineParallelism]], and [[GPTQ]]/[[AWQ]] quantization. It is the only of the three main engines (alongside [[TGI]] and [[vLLM]]) that supports pipeline parallelism.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 cites TensorRT-LLM in the context of speculative decoding integration:

> *"It's been incorporated into popular inference frameworks such as vLLM, TensorRT-LLM, and llama.cpp."*

Ch 9 also names **the TensorRT compiler** as one of three framework-integrated ML [[Compiler|compilers]]:

> *"Compilers can be ... integrated into ML and inference frameworks, like torch.compile (a feature in PyTorch), XLA, and the compiler built into the TensorRT, which is optimized for NVIDIA GPUs."*

So TensorRT-LLM is the **NVIDIA-only inference stack** — high-performance because it's hardware-specific, less portable than [[XLA]] or `torch.compile` for the same reason.

## In [[mlsysbook-ch13-model-serving|mlsysbook Ch 13]]

Ch 13 names TensorRT-LLM as the engine that calls [[ContinuousBatching|continuous batching]] **"in-flight batching,"** and as a continuous-batching implementation alongside [[vLLM]]. It is the LLM-serving sibling of [[TensorRT]] (the general TensorRT engine, which gives ResNet-50 up to ~9× over PyTorch eager). See also [[mlsysbook-ch13-model-serving]].
