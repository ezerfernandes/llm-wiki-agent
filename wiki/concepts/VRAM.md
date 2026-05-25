---
title: "VRAM"
type: concept
tags: [gpu, hardware, memory, inference]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# VRAM

**Video Random-Access Memory** — the on-board memory of a GPU. Distinct from system RAM (which is on the CPU motherboard). Introduced in *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]) as the **binding constraint for what LLMs you can run locally**:

> "In choosing a GPU, an important component is the amount of VRAM (video random-access memory) you have available. This refers to the amount of memory you have available on your GPU. In practice, the more VRAM you have the better. The reason for this is that some models simply cannot be used at all if you do not have sufficient VRAM." — Ch 1

## Why VRAM matters for LLMs

When running an LLM, the model's weights must fit in VRAM (or be streamed in/out with significant slowdown). A 7B-parameter model in FP16 needs **~14 GB VRAM just for the weights** — plus additional VRAM for activations, KV cache, and inference framework overhead. Hence the wide range of practical considerations:

- **Weight precision matters.** FP32 → 16 GB for a 7B model; FP16 → 8 GB; INT8 → 4 GB; NF4 (4-bit) → 2 GB. See [[Quantization]].
- **Context length matters.** KV cache grows with sequence length × number of attention heads × hidden dimension — long contexts can dominate VRAM.
- **Batch size matters.** Each item in a batch has its own KV cache.

## The "GPU-poor" framing

Ch 1's iconic framing: *"GPU-poor"* describes practitioners without access to high-end accelerators. The chapter's pedagogical commitment:

> "This book is for the GPU-poor! We will use models that users can run without the most expensive GPU(s) available or a big budget. To do so, we will make all the code available in Google Colab instances. At the time of writing, a free instance of Google Colab will net you a T4 GPU with 16 GB VRAM, which is the minimum amount of VRAM that we suggest." — Ch 1

This is the chapter's defining audience choice: **16 GB VRAM (free T4 on Google Colab) is the minimum target**.

The recurring worked model — [[Phi3Mini|Phi-3-mini]] (3.8B parameters) — fits in **under 8 GB VRAM**, and **under 6 GB with quantization** — comfortably inside the T4 target.

## Llama 2 training cost anchor (per Ch 1)

The chapter gives the training side of the GPU-economy story:

> "To create the Llama 2 family of models, for example, Meta used A100-80 GB GPUs. Assuming renting such a GPU would cost $1.50/hr, the total costs of creating these models would exceed $5,000,000! ... The models were trained for 3,311,616 GPU hours."

The asymmetry: training-time compute is out of reach of most practitioners (millions of dollars, weeks-to-months of GPU-time); inference-time compute can be tractable with the right model size + quantization.

## What determines VRAM need (per Ch 1)

> "Unfortunately, there is no single rule to determine exactly how much VRAM you need for a specific model. It depends on the model's architecture and size, compression technique, context size, backend for running the model, etc." — Ch 1

## Connections

- [[GPU]] — the parent hardware concept.
- [[Quantization]] — the technique for fitting more model into less VRAM.
- [[GoogleColab]] — the T4-16GB free reference platform.
- [[NVIDIA]] — the GPU vendor cited (`device_map="cuda"`).
- [[Phi3Mini]] — the book's chosen model that fits the VRAM target.
- [[ContextLength]] — a determinant of VRAM use (KV cache).
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
