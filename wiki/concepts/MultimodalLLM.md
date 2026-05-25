---
title: "Multimodal LLM"
type: concept
tags: [mllm, multimodal, architecture, llava-style]
sources: [2408.08849-ecg-chat, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Multimodal LLM (MLLM)

A language model whose **input modality is extended beyond text** — typically by attaching a *frozen non-text encoder* (image, audio, video, physiological signal) to the LLM via an **adapter / projection** module, then fine-tuning the LLM under [[lora]] or full FT to interpret the adapter's outputs alongside text.

The canonical 2024-era pattern (formalized by [[LLaVA15|LLaVA-v1.5]]):
1. **Pretrained non-text encoder** ([[CoCa]]-style ViT for images, [[ECGEncoder|1d-ViT]] for ECG signals).
2. **Projector** (2-layer MLP) maps encoder embeddings into LLM token space.
3. **Two-stage training**: (a) freeze LLM and encoder, train projector only on aligned modality-text pairs; (b) fine-tune LLM (often via [[lora]]) on instruction-following data that mixes modality inputs and text inputs.

Native multimodality (e.g. [[gemini|Gemini]]) trains all modalities from scratch under one objective; the **adapter-on-frozen-encoder** pattern is the budget-conscious academic default. [[2408.08849-ecg-chat|ECG-Chat]] is the wiki's first record of this pattern extended to a **physiological-signal modality**.

## Connections
- [[2408.08849-ecg-chat]] — adapter-style MLLM for ECG.
- [[LLaVA15]] — the visual-multimodal precedent.
- [[gemini]] — the native-multimodality alternative.
- [[Vicuna13B]] — the standard open-weight LLM backbone for academic adapter-MLLMs.
- [[CoCa]] — a typical visual encoder for MLLMs.
- [[lora]] — the parameter-efficient FT method most adapter-MLLMs use.
- [[nativemultimodality]] — the alternative training regime.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 supplies **the wiki's first runnable end-to-end vision-language pipeline** anchored on this pattern category — and the canonical worked example of an **adapter-on-frozen-encoder multimodal LLM**: [[BLIP2|BLIP-2]] (`Salesforce/blip2-opt-2.7b`, loaded via `transformers.Blip2ForConditionalGeneration` + `AutoProcessor`).

Ch 9 generalizes the pattern across **three named instances**: *"Since BLIP-2, many other visual LLMs have been released that have similar processes, like LLaVA, a framework for making textual LLMs multimodal or Idefics 2, an efficient visual LLM based on the Mistral 7B LLM."* The chapter's common-pattern statement is the cleanest formulation of the family in the wiki:

> *"Both visual LLMs, although having different architectures, connect pretrained CLIP-like visual encoders with textual LLMs. The goal of these architectures is to project visual features from the input images to language embeddings such that they can be used as the input for an LLM. Similar to the Q-Former, they attempt to bridge the gap between images and text."*

### The three instances and their bridges

| Model | Bridge between frozen ViT and frozen LLM | LLM backbone |
|---|---|---|
| [[BLIP2|BLIP-2]] (Li et al. 2023) | [[QFormer|Q-Former]] (2 sub-modules with shared attention) + linear projection | OPT-2.7b ([[meta|Meta]]) |
| [[LLaVA15|LLaVA-v1.5]] (Liu et al. 2024) | 2-layer MLP projector | [[Vicuna13B|Vicuna-13B]] |
| [[Idefics2|Idefics 2]] (Laurençon et al. 2024) | (chapter does not detail) | Mistral 7B ([[Mistral]]) |

### What Ch 9 contributes the wiki didn't already have

- The **first concrete adapter-style architecture decomposed into stages** — Ch 9 walks BLIP-2's [[QFormer|Q-Former]] training as two stages (representation learning on three joint objectives → soft-prompting the LLM), where prior wiki coverage of the pattern ([[2408.08849-ecg-chat|ECG-Chat]]) only sketched the LLaVA simplification.
- The **[[SoftVisualPrompt|soft-visual-prompt]] equivalence** — *"these embeddings serve as soft visual prompts that condition the LLM on the visual representations that were extracted by the Q-Former"* — Ch 9 is the wiki's first runnable instance of soft-prompting where the soft prompt is **derived from a non-text encoder**.
- The **bridge-architecture diversity** — the same pattern admits a Q-Former bridge ([[BLIP2|BLIP-2]]) or a 2-layer MLP bridge ([[LLaVA15|LLaVA]]) or yet another shape ([[Idefics2|Idefics 2]]); Ch 9 names the **common goal** ("project visual features into language-embedding space") and treats the specific bridge as a design choice rather than a defining feature.

### Position against [[nativemultimodality|native multimodality]]

Ch 9 does **not** claim adapter-style is universally superior; it claims it is **compute-feasible** where native multimodality is not. *"Creating a multimodal language model from scratch requires significant computing power and data. We would have to use billions of images, text, and image-text pairs to create such a model. As you can imagine, this is not easily feasible! Instead of building the architecture from scratch, BLIP-2 bridges the vision-language gap by building a bridge ..."* The adapter pattern is the **budget-conscious choice**; [[nativemultimodality|native multimodality]] remains the higher-ceiling alternative (Gemini's stance).
