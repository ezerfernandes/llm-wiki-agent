---
title: "Idefics 2"
type: entity
tags: [model, multimodal, vision-language, mllm, mistral, huggingface]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Idefics 2

**Idefics 2** — an efficient visual LLM based on the [[Mistral|Mistral 7B]] LLM. Named in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] alongside [[BLIP2|BLIP-2]] and [[LLaVA15|LLaVA]] as a contemporary adapter-style [[MultimodalLLM|multimodal LLM]]: *"Since BLIP-2, many other visual LLMs have been released that have similar processes, like LLaVA, a framework for making textual LLMs multimodal or Idefics 2, an efficient visual LLM based on the Mistral 7B LLM."*

Cited as **Laurençon et al. 2024** *"What matters when building vision-language models?"* (arXiv:2405.02246).

## Pattern category

Idefics 2 instantiates the same architectural family Ch 9 names: *"Both visual LLMs, although having different architectures, connect pretrained CLIP-like visual encoders with textual LLMs. The goal of these architectures is to project visual features from the input images to language embeddings such that they can be used as the input for an LLM. Similar to the Q-Former, they attempt to bridge the gap between images and text."*

The bridge architecture differs from [[BLIP2|BLIP-2]]'s [[QFormer|Q-Former]] and from [[LLaVA15|LLaVA]]'s 2-layer MLP projector; Ch 9 does not detail the specific Idefics-2 design — the cited paper is the canonical reference for the design-space study.

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source (named-only citation).
- [[Mistral]] — the LLM backbone (Mistral 7B).
- [[MultimodalLLM]] — the architectural family.
- [[BLIP2]] / [[LLaVA15]] — sibling adapter-style multimodal LLMs.
- [[CLIP]] — the family of visual encoders Idefics 2 uses (*"CLIP-like visual encoders"*).
