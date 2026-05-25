---
title: "Native Multimodality"
type: concept
tags: [multimodal, architecture, pretraining]
sources: [2312.11805-gemini, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Native Multimodality

A design discipline in which a foundation model is **pre-trained jointly across all modalities from the start** — text, image, audio, video — rather than assembled after-the-fact by bolting modality encoders onto a frozen text LLM. Coined operationally by the [[Gemini]] team in [[2312.11805-gemini]].

## Contrast with adapter-based multimodality

| | Native multimodal (Gemini, GPT-4o) | Adapter-style (Flamingo, LLaVA) |
|---|---|---|
| Pre-training data | Mixed-modality from epoch 1 | Text-only base + later visual SFT |
| Visual encoder | Trained jointly with the LM | Frozen ViT + projector |
| Output | Can natively emit non-text tokens (e.g. discrete image tokens) | Text-only |
| Cross-modal reasoning | Single forward pass over interleaved tokens | Mediated by the projector bottleneck |

## Mechanisms in Gemini 1.0

- **Tokenization across modalities.** Text via SentencePiece; images via discrete image tokens (Ramesh et al., Yu et al.); audio at 16 kHz from Universal Speech Model (USM) features; video as sampled frames inside the long-context window.
- **Variable image resolution.** More compute is spent on tasks that need fine-grained detail.
- **Image generation.** Output stream can interleave discrete image tokens with text tokens — the model produces images directly without a separate text-to-image pipeline.
- **Inspiration.** The visual encoder borrows from Google's Flamingo, CoCa, and PaLI work; the audio encoder builds on USM; the discrete-image-token output borrows from DALL·E / Parti tokenizer designs.

## Why it matters

The Gemini paper reports a uniform performance lift across modality benchmarks — image (9/9), video (6/6), speech (5/5) — at the same time as setting text SOTA (10/12). The claim is that this kind of broad lift is *only* available when modalities co-train; adapter-style stacks tend to specialize text or vision and trade the other off.

## See also

- [[Transformer]] — the backbone Gemini extends to multimodal tokens.
- [[MultiQueryAttention]] — inference-efficiency primitive for the long multimodal context window.
- [[2604.22748-agentic-world-modeling]] — cross-domain world-modeling taxonomy that sits naturally above a native-multimodal substrate.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 walks the **architectural alternative** to native multimodality — the **adapter-on-frozen-encoder pattern** ([[BLIP2|BLIP-2]] / [[LLaVA15|LLaVA]] / [[Idefics2|Idefics 2]]) — and frames the choice between them as a **compute-feasibility** trade-off rather than a quality one:

> *"Creating a multimodal language model from scratch requires significant computing power and data. We would have to use billions of images, text, and image-text pairs to create such a model. As you can imagine, this is not easily feasible! Instead of building the architecture from scratch, BLIP-2 bridges the vision-language gap by building a bridge ..."*

The Ch 9 stance: **native multimodality is the higher-ceiling alternative for labs that can afford it; the adapter-on-frozen-encoder pattern is the budget-conscious default everywhere else.** Ch 9 does not claim adapter-style is universally superior — it claims it is *feasible* where the native approach is not.

This is **the cleanest two-way framing** in the wiki of the architectural choice: native multimodality (Gemini / GPT-4o) vs adapter-style ([[BLIP2|BLIP-2]] / [[LLaVA15|LLaVA]] / [[Idefics2|Idefics 2]]). The [[MultimodalLLM]] page now anchors the adapter side as a family; this page anchors the native side as an alternative.
