---
title: "Representation Model"
type: concept
tags: [llm, encoder, embeddings, taxonomy]
sources: [hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling]
last_updated: 2026-05-23
---

# Representation Model

In *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch01-introduction-to-llms|Ch 1]]), [[JayAlammar|Alammar]] and [[MaartenGrootendorst|Grootendorst]] use **representation model** as the umbrella term for **encoder-only** Transformer models that focus on **representing language as embeddings** rather than generating text. The canonical example is [[bert|BERT]] (Devlin et al., 2018); the broader class includes RoBERTa, DistilBERT, DeBERTa, and most sentence-encoder models on Hugging Face.

## Definition (from Ch 1)

> "Representation models mainly focus on representing language, for instance, by creating embeddings, and typically do not generate text." — Ch 1

The chapter explicitly distinguishes this from **[[GenerativeModel|generative models]]** (decoder-only, e.g., [[GPT]] family) — *"the main distinction does not lie between the underlying architecture and the way these models work."* Both are Transformer-based; what differs is **what they're optimized to produce**.

The book uses a visual convention throughout: representation models are drawn in **teal with a small vector icon** (to indicate the focus on vectors and embeddings).

## Why encoder-only

The Transformer's encoder uses **bidirectional [[selfattention|self-attention]]** — every position attends to every other position. This is ideal for *representing* an input sequence as a contextual embedding (every token's vector depends on the whole sentence) but unsuitable for *generating* output one token at a time without leaking future information.

[[bert|BERT]]'s training procedure exploits this bidirectionality via [[maskedlanguagemodel|masked language modeling]] (MLM): mask 15% of tokens and predict them from surrounding context. The pretrained model is then fine-tuned with a task-specific head — *"BERT-like models are commonly used for [[TransferLearning|transfer learning]], which involves first pretraining it for language modeling and then fine-tuning it for a specific task."*

A special `[CLS]` token at position 0 serves as the sequence-level summary vector, commonly used as the input embedding for classification heads.

## Applications surface (per Ch 1)

The chapter forward-references representation-model use across the book:

- **Classification** (Chs 4, 11) — fine-tuning BERT with a classification head.
- **Clustering** (Ch 5) — embedding-based unsupervised grouping.
- **Semantic search** (Ch 8) — embedding similarity as the retrieval mechanism.
- **Feature extraction** — *"BERT models [are] feature extraction machines without the need to fine-tune them on a specific task"* — every layer of a BERT-like model produces usable embeddings.

## Position in the LLM taxonomy

Per Ch 1, the book deliberately calls *both* representation models and generative models "large language models":

> "The term LLM is not only reserved for generative models (decoder-only) but also representation models (encoder-only)." — Ch 1

This is **more permissive** than the common 2024 usage that reserves "LLM" for the GPT family. The book's stance: model size and capability matter more than whether the model generates text — *"this book will also cover models with fewer than 1 billion parameters that do not generate text."*

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]] / [[hands-on-llm-ch05-text-clustering-topic-modeling|Ch 5]]

Ch 4 and Ch 5 operationalize the representation-model thesis: in Ch 4 a [[TaskSpecificModel|task-specific representation model]] ([[TwitterRoBERTa|`cardiffnlp/twitter-roberta-base-sentiment-latest`]]) and an [[EmbeddingModel|embedding model]] ([[AllMPNetBaseV2|`all-mpnet-base-v2`]]) each top a [[LogisticRegression|logistic-regression]] classifier; in Ch 5 a sentence-embedding model ([[GTESmall|`thenlper/gte-small`]]) anchors the unsupervised [[BERTopic]] clustering pipeline. Both chapters thus instantiate the *"representation models produce embeddings; downstream heads consume them"* pattern Ch 1 forward-referenced.

> ⚠️ Disambiguation: in Ch 5, the phrase **"representation model"** also refers to [[BERTopic]]'s **per-topic keyword-reranking blocks** ([[KeyBERTInspired]], [[MaximalMarginalRelevance|MMR]], [[GenerativeTopicLabeling|LLM-based labeling]]) — a different sense from the Ch 1 "encoder-only LLM" sense. These are reranking algorithms operating on c-TF-IDF keyword distributions, not LLM architecture categories. The book uses the same name for both.

## Connections

- [[GenerativeModel]] — the decoder-only sibling category Ch 1 pairs it with.
- [[bert|BERT]] — the canonical representation model.
- [[maskedlanguagemodel]] — the training objective.
- [[Embedding]] / [[WordEmbedding]] / [[ContextualEmbedding]] — what representation models produce.
- [[Tokenization]] / [[Tokenizer]] — the input-unit substrate.
- [[transformer|Transformer]] — the underlying architecture (encoder stack only).
- [[encoderdecoder|Encoder-Decoder]] — the original full Transformer; representation models are the "encoder-only" descendant.
- [[FineTuning]] / [[TransferLearning]] — the standard deployment pattern.
- [[LanguageAI]] — the umbrella.
- [[hands-on-llm-ch01-introduction-to-llms]] — primary source.
- [[hands-on-llm-ch04-text-classification]] — task-specific representation model + embedding model worked examples.
- [[hands-on-llm-ch05-text-clustering-topic-modeling]] — also re-uses "representation model" for BERTopic's keyword-reranking blocks (a different sense).
- [[BERTopic]] / [[KeyBERTInspired]] / [[MaximalMarginalRelevance]] / [[GenerativeTopicLabeling]] — Ch 5's "representation models" (different sense).
