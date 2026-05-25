---
title: "Stable Diffusion"
type: entity
tags: [model, open-source, image-generation, stability-ai]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Stable Diffusion

Open-source text-to-image diffusion model originally released by Stability AI in 2022. Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as one of the **inflection events triggering the 2023 AI-tooling growth surge** (alongside [[ChatGPT|ChatGPT]]). Per Huyen's March 2024 analysis of 920 AI-related GitHub repositories with 500+ stars:

> *"The data shows a big jump in the number of AI toolings in 2023, after the introduction of Stable Diffusion and ChatGPT."*

The **Stable Diffusion Web UI** (AUTOMATIC1111) is one of four open-source AI-engineering tools (alongside [[AutoGPT]], [[LangChain]], and [[Ollama]]) that within two years of launch had **garnered more GitHub stars than Bitcoin** — on track to surpass React and Vue. This GitHub-star trajectory is Ch 1's anchor data for the *"fastest-growing engineering discipline"* claim.

## Connections

- [[FoundationModel]] — model class (multimodal generative).
- [[AIInvestmentBoom]] — Stable Diffusion is one of the two ignition events for the post-2022 surge.
- [[FoundationModelUseCases]] — image generation category.
- [[Midjourney]] / [[AdobeFirefly]] / [[Sora]] — peer products in the creative-AI cluster.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names Stable Diffusion alongside [[DALLE|DALL·E]] and [[Midjourney]] as a downstream consumer of **[[ContextualEmbedding|contextualized text embeddings]]** — the text-conditioning signal that aligns generated images with input prompts:

> "These contextualized vectors, for example, are what powers AI image generation systems like DALL·E, Midjourney, and Stable Diffusion." — Ch 2

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 cites Stable Diffusion as the **canonical downstream use of multimodal embeddings for *generation***. Among [[CLIP]]'s four named applications (zero-shot classification / clustering / search / generation), generation is operationalized via Stable Diffusion: *"Multimodal embedding models, like CLIP, can be used to drive use cases like image generation (e.g., stable diffusion)."* Cited as **Rombach et al. 2022** *"High-resolution image synthesis with latent diffusion models"* (CVPR 2022). The structural role: Stable Diffusion's text-conditioning head ingests CLIP-family text embeddings — Ch 9 thus closes the loop between the chapter's embedding-model walk and the broader text-to-image generative-AI ecosystem.
