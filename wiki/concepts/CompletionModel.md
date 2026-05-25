---
title: "Completion Model"
type: concept
tags: [llm, generation, framing, decoder]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Completion Model

In *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]), **completion model** is the framing the authors use for generative LLMs viewed as text-completion machines:

> "Generative LLMs, as sequence-to-sequence machines, take in some text and attempt to autocomplete it. ... You will often hear that generative models are completion models." — Ch 1

The framing matches [[ChipHuyen|Chip Huyen's]] [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] *"completion machine"* framing for the [[AutoregressiveLanguageModel|autoregressive LM]] — both books converge on the same metaphor for decoder-only [[GenerativeModel|generative models]].

## Why the framing matters

Many higher-level tasks can be **expressed as completion tasks**, so a single completion model — given the right prompt — can perform tasks that traditionally needed task-specific models:

- *"How are you in French is …"* → *"Comment ça va"* (translation as completion)
- *"Question: Is this email spam? <email> Answer:"* → *"Likely spam"* (classification as completion)
- *"Summary of the following article: <article>"* → *"<summary>"* (summarization as completion)

This is the framing that makes prompt engineering — and instruction tuning ([[InstructModel|instruct models]]) — useful: the base model is a completion engine; the prompt is the input prefix; the user's intent is encoded in the prefix structure.

## From completion to instruction following

> "Although a handy feature, their true power shone from being trained as a chatbot. Instead of completing a text, what if they could be trained to answer questions? By fine-tuning these models, we can create instruct or chat models that can follow directions." — Ch 1

So completion models are the substrate; [[InstructModel|instruct models]] are the fine-tuned variants that follow directions rather than blindly autocomplete.

## Connections

- [[GenerativeModel]] — the broader category; completion-model is a framing of generative models.
- [[InstructModel]] — the instruction-tuned variant of completion models.
- [[AutoregressiveLanguageModel]] — the technical name for the next-token-prediction mechanism that makes completion possible.
- [[GPT]] / [[Phi3Mini]] / [[Llama]] / [[Mistral]] — example completion models.
- [[FoundationModel]] / [[pretraining]] — the base-model framing.
- [[PromptEngineering]] — the practice of crafting prefixes that elicit task behavior from completion models.
- [[ContextLength]] — the maximum prefix + completion length.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
