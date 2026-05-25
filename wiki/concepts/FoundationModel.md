---
title: "Foundation Model"
type: concept
tags: [foundation-models, llm, multimodal, ai-engineering]
sources: [ai-engineering-chip-huyen, ai-engineering-ch01-intro, ai-engineering-ch02-foundation-models, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Foundation Model

**A large generative model — typically [[LargeLanguageModel|LLM]] or large [[MultimodalLLM|multimodal model]] — that serves as a general-purpose base on which applications can be built.** In [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], [[ChipHuyen|Chip Huyen]] explicitly uses "foundation model" to *supersede* "LLM" once the model handles modalities beyond text — both because the word "foundation" signals the **build-upon-able** role these models play and because "LLM" is "hardly a scientific term" (the word "large" being inherently relative).

## Definition (Huyen's working usage)

> *"This book uses the term foundation models to refer to both large language models and large multimodal models."* — Ch 1

## How foundation models broke with prior AI research structure

Before foundation models, AI was organized by **modality** — NLP for text, computer vision for images, speech-processing for audio. Foundation models unify these:

- [[GPT4|GPT-4V]] and [[ClaudeOpus47|Claude 3]] handle text + images.
- [[gemini|Gemini]] is natively multimodal (text + image + audio + video).
- Some FMs handle videos, 3D assets, protein structures.

[[OpenAI|OpenAI's]] [[CLIP]] (2021), trained on 400M co-occurring (image, text) pairs via [[NaturalLanguageSupervision|natural language supervision]], was the first model to zero-shot generalize across image classification tasks — the embedding backbone underlying multimodal generative models like Flamingo, [[LLaVA15|LLaVA]], and [[gemini|Gemini]].

## From task-specific to general-purpose

Foundation models also mark the transition **from task-specific to general-purpose** models. A traditional sentiment-analysis model can't do translation; a foundation model can do both *out of the box* — and can be further [[ModelAdaptation|adapted]] for higher per-task quality via:

1. **[[PromptEngineering|Prompt engineering]]** — provide instructions and examples.
2. **[[rag|RAG]]** — supplement instructions with retrieved data.
3. **[[FineTuning|Finetuning]]** — further-train the model on task-specific data.

## Why FMs make AI development cheaper

> *"Ten examples and one weekend versus 1 million examples and six months."* — Ch 1, on adapting an FM vs. building a task-specific model from scratch.

This cost asymmetry is the **economic precondition for [[AIEngineering|AI engineering]] as a discipline.**

## Who builds them

Because of the resources required (compute, talent, data), foundation-model *development* is restricted to:
- **Big corporations**: [[google|Google]], [[meta|Meta]], [[microsoft|Microsoft]], Baidu, Tencent.
- **Governments**: Japan, the UAE.
- **Well-funded startups**: [[openai|OpenAI]], [[anthropic|Anthropic]], Mistral.

Per [[SamAltman|Sam Altman]] (Sep 2022): *"the biggest opportunity for the vast majority of people will be to adapt these models for specific applications."*

## Connections

- [[LargeLanguageModel]] / [[MultimodalLLM]] — the two FM sub-classes.
- [[CLIP]] — the foundational multimodal embedding model.
- [[SelfSupervision]] / [[NaturalLanguageSupervision]] — the training paradigm.
- [[ModelAdaptation]] / [[PromptEngineering]] / [[rag]] / [[FineTuning]] — the adaptation techniques.
- [[AIEngineering]] — the discipline built atop FMs.
- [[ModelAsAService]] — the API-served deployment pattern.
- [[gemini]] / [[GPT4]] / [[claudeopus47]] / [[LLaVA15]] / [[bert]] — example FMs.
- [[ai-engineering-ch01-intro]] — primary source.

## From [[ai-engineering-ch02-foundation-models|AI Engineering Ch 2]]

Ch 2 is **the deep technical anatomy of a foundation model** — what choices determine what an FM becomes. Per Ch 2:

> "Differences in foundation models can be traced back to decisions about **training data, model architecture and size, and how they are post-trained to align with human preferences**."

Plus a fourth axis the chapter argues is underrated: **sampling**.

### Four design decisions Ch 2 unpacks

1. **[[CommonCrawl|Training data]] / [[MultilingualModel|language coverage]] / [[DomainSpecificModel|domain coverage]]** — what the model learns from.
2. **[[transformer|Architecture]] (dominant) or [[StateSpaceModel|alternatives]] + size** — how the learning is structured.
3. **[[posttraining|Post-training]]** ([[SupervisedFinetuning|SFT]] → [[PreferenceFinetuning|preference finetuning]]) — how the model is aligned for use.
4. **[[Sampling|Sampling]] / inference** ([[Temperature]], [[Topk]], [[Topp]], [[TestTimeCompute]], [[StructuredOutputs]]) — how outputs are drawn from the model.

### Why "skip the nitty-gritty training details"

> "Since most people will be using ready-made foundation models instead of training one from scratch, I skipped the nitty-gritty training details in favor of **modeling factors that help you determine what models to use and how to use them**." — Ch 2 summary

This framing is what makes Ch 2 the right cross-reference for AI-engineering readers who need to *understand* foundation models without *training* them.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 supplies the wiki's **first runnable end-to-end vision-language pipeline** and extends the foundation-model framing into multimodality with two distinct families:

1. **Multimodal embedding foundation models** — [[CLIP]] (Radford et al. 2021). The substrate that enables zero-shot classification / clustering / search / generation across text and image.
2. **Multimodal generative foundation models** — [[BLIP2|BLIP-2]] (Li et al. 2023), [[LLaVA15|LLaVA]] (Liu et al. 2024), [[Idefics2|Idefics 2]] (Laurençon et al. 2024). The [[MultimodalLLM|adapter-on-frozen-encoder]] family that takes images as input and emits text.

Ch 9's central structural observation — *"the moment the embeddings are passed to the encoder, they are treated as if they were textual tokens"* — is what makes the [[transformer|Transformer]] machinery generalize across modalities and underpins the foundation-model thesis itself: **one architecture, many modalities, build-upon-able by downstream applications**.
