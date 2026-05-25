---
title: "Language AI"
type: concept
tags: [nlp, llm, umbrella-term, language-understanding]
sources: [hands-on-llm-ch01-introduction-to-llms]
last_updated: 2026-05-23
---

# Language AI

**Language AI** is the term used by [[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]] in *[[HandsOnLLM|Hands-On Large Language Models]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]) for *"a subfield of AI that focuses on developing technologies capable of understanding, processing, and generating human language."* The authors position it as the discipline within which large language models sit — broader than "LLM" and approximately interchangeable with **[[NLP|natural language processing]]**, but chosen deliberately because it admits LLM-adjacent technologies that aren't themselves LLMs.

## Why a new umbrella term

> "The term Language AI can often be used interchangeably with natural language processing (NLP) with the continued success of machine learning methods in tackling language processing problems. ... We use the term Language AI to encompass technologies that technically might not be LLMs but still have a significant impact on the field, like how retrieval systems can give LLMs superpowers." — Ch 1

The two practical consequences:

1. **[[rag|Retrieval-augmented generation]] is Language AI but not (strictly) an LLM.** Retrieval is a separate technology component that augments LLM capabilities; the book covers retrieval (Ch 8) as a core Language-AI topic even though the retriever itself is not generative.

2. **Pre-neural techniques like [[BagOfWords|bag-of-words]] are still in scope.** The book opens with bag-of-words as the historical starting point for representing language as numbers — admitting techniques that pre-date neural networks under the Language AI umbrella.

## In the book's chapter structure

Per Ch 1, every chapter explores some facet of Language AI:

- Pre-neural representations: [[BagOfWords|bag-of-words]] (Ch 1, Ch 5).
- Dense embeddings: [[Word2Vec|word2vec]] (Ch 1, Ch 2).
- Sequence models with attention: RNN encoder-decoder + attention (Ch 1, Ch 3).
- The Transformer + its descendants: [[bert|BERT]], [[GPT]], etc. (Ch 1, Ch 3).
- Applications: classification (Chs 4, 11), clustering (Ch 5), prompting (Ch 6), advanced generation (Ch 7), semantic search + [[rag|RAG]] (Ch 8), multimodal (Ch 9), embedding training (Ch 10), fine-tuning generative models (Ch 12).

## Connections

- [[NLP]] — the near-synonym from classical academic vocabulary.
- [[LargeLanguageModel]] — the dominant subset of Language AI by 2024.
- [[FoundationModel]] — the multimodal generalization.
- [[BagOfWords]] / [[Word2Vec]] / [[Embedding]] / [[transformer|Transformer]] / [[bert|BERT]] / [[GPT]] — the chronological sequence of Language AI building blocks Ch 1 narrates.
- [[rag|RAG]] — the explicit example of "Language AI but not LLM" the chapter gives.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
