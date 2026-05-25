---
title: "Inpainting Feedback"
type: concept
tags: [user-feedback, multimodal, image-generation, human-ai-collaboration]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Inpainting Feedback

**A model of human-AI collaboration where the user selects a region of a generated artifact and describes how to fix just that region — simultaneously delivering a better output and producing **region-level edit feedback** as a byproduct.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"An example of human–AI collaboration is the inpainting functionality for image generation. If a generated image isn't exactly what the user needs, they can select a region of the image and describe with a prompt how to make it better. … This feature allows users to get better results while giving developers high-quality feedback."* — Ch 10

Figure 10-14 in Ch 10 shows inpainting with [[DALLE|DALL-E]] ([[openai|OpenAI]] 2021).

## Why it's the design exemplar

Most feedback mechanisms force a tradeoff: explicit feedback is high-quality but costs the user; implicit feedback is cheap but noisy. **Inpainting collapses the tradeoff** — the user does the action they wanted to do anyway (fix the image), and that action *is* the feedback signal:

- **Which region** the user selected → which part of the model's output failed.
- **What prompt** they used to fix it → the desired behavior on that region.
- **The new generation** → a paired (failed_region, prompt, fixed_region) tuple, comparable to a [[UserEditFeedback|user edit pair]] but spatially localized.

The user gets a better image; the developer gets training-grade data; both sides are unambiguously incentivized.

## Generalization beyond images

Ch 10's footnote names the natural next target:

> *"I wish there were inpainting for text-to-speech. I find text-to-speech works well 95% of the time, but the other 5% can be frustrating. AI might mispronounce a name or fail to pause during dialogues. I wish there were apps that let me edit just the mistakes instead of having to regenerate the whole audio."* — Ch 10, footnote

The general pattern is: **partial-output editing affordances**. Any modality where users would normally re-prompt for the whole output is a candidate — text-to-speech, video, code (already exists in some IDEs), document drafting, etc.

## Design principle the pattern encodes

> Let users **collaborate with the AI** at the granularity where the AI fails, not at the granularity where the AI was invoked.

This is the deeper design insight Huyen draws from inpainting: regenerate-the-whole-thing is a coarse affordance that creates noisy [[RegenerationSignal|regeneration signals]]; edit-just-the-bad-part is fine-grained and creates clean feedback.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[UserEditFeedback]] — the text/code-side sibling pattern.
- [[ConversationalFeedback]] / [[ImplicitConversationalSignal]] — parent categories.
- [[DALLE]] — Ch 10's named example.
- [[Midjourney]] — adjacent feedback-design exemplar (upscale/vary/regen).
- [[RegenerationSignal]] — the *coarse* feedback alternative inpainting outperforms.
- [[humanintheloop]] / [[HumanInTheLoopApproval]] — broader human-AI-collaboration category.
- [[DataFlywheel]] — inpainting is a flywheel-quality feedback source.
