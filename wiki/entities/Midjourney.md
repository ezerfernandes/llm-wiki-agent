---
title: "Midjourney"
type: entity
tags: [product, image-generation, startup, generative-ai]
sources: [ai-engineering-ch01-intro, hands-on-llm-ch02-tokens-and-embeddings, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Midjourney

Independent AI image-generation startup; one of the most commercially successful generative-image products. Cited in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] as having reached **$200M annual recurring revenue at age 1.5 years** (late 2023), making it one of the fastest-growing creative-AI businesses.

## In Ch 1

- **Commercial benchmark for image AI**: alongside [[AdobeFirefly|Adobe Firefly]] (photo editing) and [[Runway]] / [[PikaLabs]] / [[Sora]] (video generation) in the [[FoundationModelUseCases|image and video production]] use case category.
- **Interface dual-mode**: Midjourney is used both via its standalone web app and via integration in the Discord chat platform — an example Huyen uses to illustrate the diversity of [[AIInterface|AI interfaces]].
- **App Store dominance**: in December 2023, half of the top-10 free Graphics & Design apps on the Apple App Store had "AI" in the name; Midjourney is the canonical reference.

## Connections

- [[FoundationModel]] — underlying model class.
- [[FoundationModelUseCases]] — image/video category.
- [[AIInterface]] — standalone-web + chat-integrated dual interface.
- [[ai-engineering-ch01-intro]] — Ch 1 source.
- [[Sora]] / [[Runway]] / [[PikaLabs]] / [[AdobeFirefly]] — peer products.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 names Midjourney alongside [[DALLE|DALL·E]] and [[StableDiffusion|Stable Diffusion]] as a consumer of **[[ContextualEmbedding|contextualized text embeddings]]** — the text-conditioning signal that aligns generated images with input prompts.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 holds up Midjourney as **the exemplar of well-designed implicit-feedback collection**:

> *"One example often cited as good feedback design is from the image generator app Midjourney. For each prompt, Midjourney generates a set of (four) images and gives the user the following options: 1. Generate an unscaled version of any of these images. 2. Generate variations for any of these images. 3. Regenerate."* — Ch 10 (Figure 10-18)

### Signal mapping

Each user action maps cleanly to a feedback signal:

| User action | Signal |
|---|---|
| Upscale image *i* | Strong positive on *i* (it's the user's pick of the four) |
| Generate variations of image *i* | Weaker positive on *i* (promising but not perfect) |
| Regenerate the whole batch | None of the four is good enough |

The design's payoff: **the user gets what they want (a better image), and the developer gets graded preference data — every prompt and every click**. No separate rating UI; no friction.

### Public-vs-private signal visibility

Ch 10 also notes that *"in its early days, Midjourney's feedback — someone choosing to upscale an image, generate variations, or regenerate another batch of images — was public."* The chapter uses this as part of a broader discussion of how signal visibility (public vs private) affects candor in feedback. The Midjourney case is a worked example of a product collecting feedback in public-by-default — with the upside of social-proof and discoverability, and the downside of self-censorship effects.
