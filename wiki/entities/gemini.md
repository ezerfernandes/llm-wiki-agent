---
title: "Gemini"
type: entity
tags: [model-family, multimodal, frontier, google, deepmind]
sources: [2312.11805-gemini, 2603.19247-prompt-optimization-jailbreaking, ai-engineering-ch01-intro]
last_updated: 2024-12-04
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

## From [[ai-engineering-ch01-intro|AI Engineering Ch 1]]

[[ChipHuyen|Chip Huyen]] in *AI Engineering* Ch 1 uses Gemini as the **canonical case study for prompt-format-dependence in benchmark scores**. From the December 2023 Gemini technical report:

| Model | Prompt format | MMLU |
|---|---|---|
| Gemini Ultra | CoT@32 | **90.04%** |
| Gemini Pro | CoT@8 | 79.13% |
| GPT-4 | 5-shot | 86.4% |
| Gemini Ultra | 5-shot (matched) | 83.7% |

Huyen's takeaway: *"Different prompts can cause models to perform very differently."* Google's claim that Gemini Ultra beats GPT-4 on MMLU only holds at CoT@32; at matched 5-shot, GPT-4 wins. This becomes Ch 1's anchor anecdote for the importance of **[[PromptEngineering|prompt engineering]] in [[Evaluation|evaluation]]**.

Gemini is also Ch 1's primary example of a **natively multimodal [[FoundationModel|foundation model]]** that justifies the *"foundation model"* umbrella term over the narrower *"LLM"*.

## In [[2603.19247-prompt-optimization-jailbreaking]]

Gemini 2.5 Pro plays **two distinct roles in a single paper**: (i) one of four *target* LMs in the adaptive red-teaming grid — baseline danger **0.645** (the *highest* of the four targets; Gemini is the least safe-by-default at the seed prompts) → SIMBA 0.774; (ii) the [[GEPA]] *reflection model* generating prompt mutations against the other three targets. This dual role gives the paper a within-experiment robustness check: Gemini being both a reflection model and an attack target means any reflection-side bias would have to differentially help GEPA on non-Gemini targets and hurt on Gemini, which the table does not show.
