---
title: "LLaVA-v1.5"
type: concept
tags: [mllm, vision-language, llava, vicuna]
sources: [2408.08849-ecg-chat, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# LLaVA-v1.5

**Liu, Li, Li, Lee (CVPR June 2024) — *"Improved baselines with visual instruction tuning."*** Open-source vision-language model that established the canonical 2024-era **adapter-on-frozen-encoder** pattern for academic multimodal LLMs: pretrained vision encoder → 2-layer MLP projector → [[Vicuna13B|Vicuna-13B]] LLM, trained in two stages (feature alignment → instruction tuning).

In [[2408.08849-ecg-chat|ECG-Chat]]: the **architectural precedent** that ECG-Chat directly mirrors — *"The modality interface in ECG-Chat resembles LLaVA-v1.5. ECG encoding is embedded like text tokens and fed into LLMs."* The only substantive swap is the encoder side (image ViT → [[ECGEncoder|1d-ViT]]); the rest of the recipe (2-layer MLP, Vicuna-13B base, LoRA fine-tune, two-stage training) carries over.

## Connections
- [[2408.08849-ecg-chat]] — ECG-modality extension.
- [[Vicuna13B]] — LLM backbone.
- [[MultimodalLLM]] — the architectural pattern category.
- [[lora]] — the fine-tuning method.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 names LLaVA alongside [[BLIP2|BLIP-2]] and [[Idefics2|Idefics 2]] as a contemporary adapter-style [[MultimodalLLM|multimodal LLM]] — and frames LLaVA as the **simplification of BLIP-2**:

> *"Since BLIP-2, many other visual LLMs have been released that have similar processes, like LLaVA, a framework for making textual LLMs multimodal or Idefics 2, an efficient visual LLM based on the Mistral 7B LLM."* — Ch 9

The pattern relationship: where BLIP-2 uses a multi-module [[QFormer|Q-Former]] (with shared attention layers between an Image Transformer and a Text Transformer) plus a linear projection as the bridge between frozen ViT and frozen LLM, LLaVA collapses the bridge to a **2-layer MLP projector** — same architectural slot, simpler shape. Cited in Ch 9 as **Liu et al. 2024** *"Visual instruction tuning"* (NeurIPS 36, the LLaVA paper that established the canonical visual-instruction-tuning recipe).

Ch 9's punchline generalization across BLIP-2 / LLaVA / Idefics 2: *"Both visual LLMs, although having different architectures, connect pretrained CLIP-like visual encoders with textual LLMs. The goal of these architectures is to project visual features from the input images to language embeddings such that they can be used as the input for an LLM. Similar to the Q-Former, they attempt to bridge the gap between images and text."*
