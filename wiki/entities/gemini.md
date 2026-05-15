---
title: "Gemini"
type: entity
tags: [model-family, multimodal, frontier, google, deepmind]
sources: [2312.11805-gemini]
last_updated: 2026-05-10
---

# Gemini

Family of natively multimodal foundation models from [[GoogleDeepMind]], introduced in [[2312.11805-gemini]] (December 2023). Built on [[Transformer]] decoders with [[MultiQueryAttention]]; trained jointly across text, image, audio, and video; deployed in three sizes:

| Variant | Role | Notes |
|---|---|---|
| **Ultra** | Frontier reasoning | First model to exceed human-expert [[MMLU]] (90.04%); SOTA on 30/32 benchmarks reported in 1.0. |
| **Pro** | Cost/latency-optimized | Powers default Gemini consumer chat and base of [[AlphaCode2]]. |
| **Nano-1 / Nano-2** | On-device | 1.8B / 3.25B params; 4-bit quantized; [[KnowledgeDistillation|distilled]] from larger Geminis. |

## Product variants

- **Gemini Apps** — consumer chat. Originally branded as **[[Bard]]** (powered by [[PaLM2]]); rebranded to *Gemini* (with Pro) and *Gemini Advanced* (with Ultra).
- **Gemini APIs** — developer-facing via Google AI Studio and Cloud Vertex AI.

Both variants share pre-training but diverge in post-training: instruction following, tool-use control loop (tools rendered as code blocks), multilinguality (40+ languages), multimodal vision SFT, and safety SFT/RLHF.

## Place in the wiki

Gemini is the second **substrate-defining** entry in the LLM corpus alongside [[1706.03762-attention-is-all-you-need]]. The 2017 paper defines the *architecture*; Gemini 1.0 defines the *frontier-multimodal-deployment template* — three-size family, native multimodality, [[RLHF]] flywheel, structured responsible-deployment review, [[DangerousCapabilities]] evaluation. Most 2026 agent papers in this wiki implicitly assume a Gemini-class base model when they discuss harnesses, memory, or skill verification.
