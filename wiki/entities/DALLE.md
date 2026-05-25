---
title: "DALL·E"
type: entity
tags: [model, image-generation, openai, multimodal]
sources: [hands-on-llm-ch02-tokens-and-embeddings]
last_updated: 2026-05-23
---

# DALL·E

[[openai|OpenAI's]] text-to-image generation model family — DALL·E (2021), DALL·E 2 (2022), DALL·E 3 (2023, integrated into [[ChatGPT]]). Generates images conditioned on natural-language prompts.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names DALL·E (alongside [[Midjourney]] and [[StableDiffusion|Stable Diffusion]]) as a downstream consumer of **[[ContextualEmbedding|contextualized text embeddings]]**:

> "These contextualized vectors, for example, are what powers AI image generation systems like DALL·E, Midjourney, and Stable Diffusion." — Ch 2

The chapter uses DALL·E as evidence that **token / text embeddings are foundational to modalities beyond text** — they serve as the conditioning signal that aligns generated images with text prompts. The chapter forward-references **Chapter 9** (multimodal LLMs) for the image-text alignment recipe in more detail.

## Connections

- [[openai|OpenAI]] — developer.
- [[Midjourney]] / [[StableDiffusion]] — peer text-to-image systems Ch 2 names alongside DALL·E.
- [[ContextualEmbedding]] — the embedding type that conditions image generation.
- [[MultimodalLLM]] — the broader class.
- [[ChatGPT]] — DALL·E 3 is integrated into ChatGPT.
- [[hands-on-llm-ch02-tokens-and-embeddings]] — citation.
