---
title: "Generative AI"
type: concept
tags: [generative, ai, foundation-models]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Generative AI

**AI models that produce open-ended outputs** — sequences of tokens, images, audio, or video constructed from a finite vocabulary in a combinatorially-infinite space of possible outputs. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]:

> *"The outputs of language models are open-ended. A language model can use its fixed, finite vocabulary to construct infinite possible outputs. A model that can generate open-ended outputs is called generative, hence the term generative AI."*

## Distinguishing characteristic

The defining trait is **open-endedness**, contrasted with:
- **Discriminative models** — output a class label or score from a fixed set.
- **Embedding models** (e.g., [[CLIP]]) — output a fixed-dimensional vector, not a sample from a distribution.

Note: [[CLIP]] itself is *not* generative — it's an embedding model. The generative multimodal models that build on top of CLIP-style backbones (Flamingo, [[LLaVA15|LLaVA]], [[gemini|Gemini]]) are.

## Why open-endedness matters for engineering

- **Versatility**: any task framed as next-token prediction can be solved — translation, summarization, classification, coding, math.
- **Evaluation difficulty**: open-ended outputs break the classical ground-truth metric paradigm — there are too many valid responses to enumerate. This is the central reason [[Evaluation]] is the hardest part of [[AIEngineering]].
- **Hallucination risk**: open-ended generation is probabilistic and unconstrained by ground truth; the same input can produce a confident-but-wrong output. See [[Hallucination]].

## Connections

- [[FoundationModel]] / [[LargeLanguageModel]] / [[MultimodalLLM]] — the model classes that are generative.
- [[AutoregressiveLanguageModel]] — the most common generative-LM mechanism.
- [[Evaluation]] — open-endedness is what makes evaluation hard.
- [[Hallucination]] — the headline failure mode of generative models.
- [[CLIP]] — non-generative counterexample (embedding model).
- [[ai-engineering-ch01-intro]] — primary source.
