---
title: "Task-Specific Model"
type: concept
tags: [llm, classification, fine-tuning, representation-model]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Task-Specific Model

In *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch04-text-classification|Ch 4]]), a **task-specific model** is a [[RepresentationModel|representation model]] — typically a [[bert|BERT]]-family encoder — that has been **fine-tuned for one specific downstream task** (sentiment analysis, NER, intent classification, language detection) and is then used as-is, frozen, at inference time.

## Definition (from Ch 4)

> "A task-specific model is a representation model, such as BERT, trained for a specific task, like sentiment analysis." — Ch 4

The chapter distinguishes this from **[[EmbeddingModel|embedding models]]** — representation models that produce *general-purpose embeddings* usable across many downstream tasks. Both are *flavors* of representation-model classification; the distinction is whether the model's last layer is **task-specific** (head + class logits) or **task-agnostic** (an embedding vector).

## Worked example (Ch 4)

[[TwitterRoBERTa|`cardiffnlp/twitter-roberta-base-sentiment-latest`]] — a [[RoBERTa]] checkpoint fine-tuned on tweets for 3-class sentiment (negative / neutral / positive). Loaded via `transformers.pipeline(model=path, tokenizer=path, return_all_scores=True)`. On [[RottenTomatoes|Rotten Tomatoes]]: **F1 = 0.80** weighted average.

## Trade-offs

| Pro | Con |
|---|---|
| **Highest performance** when task + domain match the model's training data | **Inflexible** — useless if no matching pretrained model exists |
| **Zero training compute** at deployment time | **Domain-shift sensitive** (Twitter → movie reviews costs Ch 4 ~5 F1 points) |
| **Lightweight inference** (one model, fixed output schema) | **No reusability** of the model across tasks |

## When to use a task-specific model

Per Ch 4's pedagogical arc: **try this first if a matching pretrained model exists on the [[HuggingFace|Hugging Face]] Hub** (60,000+ text classification models at time of writing). If not, fall back to:
1. **[[EmbeddingModel|Embedding model]] + [[LogisticRegression|logistic regression]]** classifier (supervised; requires labeled data).
2. **[[ZeroShotClassification|Zero-shot classification]]** via [[LabelEmbedding|label embeddings]] + [[CosineSimilarity|cosine similarity]] (no labels needed).
3. **[[GenerativeClassification|Generative classification]]** via prompt + decoder/encoder-decoder LM ([[FLANT5|Flan-T5]], [[ChatGPT|ChatGPT]]).
4. **Fine-tune your own** representation model (Ch 11).

## Connections

- [[RepresentationModel]] — the parent category.
- [[EmbeddingModel]] — the sibling flavor (Ch 4 contrasts them).
- [[bert]] / [[RoBERTa]] / [[DistilBERT]] / [[ALBERT]] / [[DeBERTa]] — BERT-family architectures task-specific models are built from.
- [[TwitterRoBERTa]] — Ch 4's worked example.
- [[FineTuning]] / [[FineTuningBert]] — the training procedure that produces these.
- [[ClassificationHead]] — the trainable output layer atop the encoder.
- [[HuggingFace]] — distribution channel.
- [[hands-on-llm-ch04-text-classification]] — primary source.
