---
title: "Embedding Model"
type: concept
tags: [llm, embeddings, representation-model, retrieval, classification]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Embedding Model

In *[[HandsOnLLM|Hands-On LLMs]]* ([[hands-on-llm-ch04-text-classification|Ch 4]]), an **embedding model** is a [[RepresentationModel|representation model]] that produces **general-purpose embeddings** — fixed-dimensional dense vectors representing text — that can be fed into many downstream task pipelines (classification, semantic search, clustering, [[rag|RAG]], reranking).

## Definition (from Ch 4)

> "An embedding model generates general-purpose embeddings that can be used for a variety of tasks not limited to classification, like semantic search. ... In this chapter, we keep both models frozen (nontrainable) and only use their output." — Ch 4

The chapter distinguishes this from **[[TaskSpecificModel|task-specific models]]** — representation models with a task-specific head producing class logits or other task-specific output. Both are flavors of representation-model classification; embedding models swap **flexibility** (one model, many tasks) for **per-task tuning** (need a classifier on top).

## Two-step recipe (Ch 4)

1. **Encode**: convert text to embeddings with a frozen embedding model.
   ```python
   from sentence_transformers import SentenceTransformer
   model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
   train_embeddings = model.encode(data["train"]["text"])
   # shape: (8530, 768)
   ```
2. **Classify**: train a lightweight classifier on the embeddings.
   ```python
   from sklearn.linear_model import LogisticRegression
   clf = LogisticRegression(random_state=42).fit(train_embeddings, labels)
   ```

> "A major benefit of this separation is that we do not need to fine-tune our embedding model, which can be costly. In contrast, we can train a classifier, like a logistic regression, on the CPU instead." — Ch 4

On [[RottenTomatoes|Rotten Tomatoes]] with `all-mpnet-base-v2` + `LogisticRegression`: **F1 = 0.85** — the best of the four representation-model regimes Ch 4 tests.

## Model selection (Ch 4)

The [[MTEB|MTEB leaderboard]] is *"a great place to start. It contains open and closed source models benchmarked across several tasks."* Ch 4 picks `sentence-transformers/all-mpnet-base-v2` for the **speed-vs-quality balance** — *"a small but performant model"* — over higher-MTEB models that are slower at inference. **8,000+ embedding models** were on the Hugging Face Hub at time of writing.

## API alternatives

Per Ch 4: embeddings can also be served via API instead of locally. *"Popular choices for generating embeddings are Cohere's and OpenAI's offerings. As a result, this would allow the pipeline to run entirely on the CPU."* The chapter does not switch to APIs but flags this for GPU-poor users.

## Reuse across applications

The same `all-mpnet-base-v2` embeddings Ch 4 trains a logistic regression on are also used for:
- **Ch 4 [[ZeroShotClassification|zero-shot classification]]** (label embeddings + cosine similarity).
- **Ch 5** (text clustering).
- **Ch 8** (semantic search + RAG).

This **embedding-as-feature** discipline is the chapter's central pedagogical move — *"As you will see throughout the book, embeddings can be found in most Language AI use cases and are often an underestimated but incredibly vital component."*

## Connections

- [[RepresentationModel]] — the parent category.
- [[TaskSpecificModel]] — the sibling flavor.
- [[Embedding]] / [[TextEmbedding]] / [[SentenceEmbedding]] — what these models produce.
- [[SentenceTransformers]] — the canonical Python library.
- [[AllMPNetBaseV2]] — Ch 4's worked model.
- [[MTEB]] — model selection rubric.
- [[LogisticRegression]] / [[sklearn]] — the classifier head Ch 4 uses.
- [[CosineSimilarity]] — used downstream for zero-shot label assignment and semantic search.
- [[ZeroShotClassification]] / [[LabelEmbedding]] — the label-less downstream use of these embeddings.
- [[rag]] / semantic search — other downstream uses.
- [[hands-on-llm-ch04-text-classification]] — primary source.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10 walks **how to train** an embedding model from scratch and fine-tune one (see section below).

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 is **the chapter that walks how to create an embedding model**, complementing Ch 4's *"how to use one for classification."* The chapter codifies:

- **What makes embeddings "accurate"**: the geometry preserves semantic similarity. *"We want vectors of documents that are similar to one another to be similar, whereas the embeddings of documents that each discuss something entirely different should be dissimilar."*
- **Steering embeddings**: training data choice steers the geometry. *"By presenting the model with enough examples of semantically similar documents, we can steer toward semantics whereas using examples of sentiment would steer it in that direction."* You can train an embedding model whose geometry clusters by sentiment, by topic, by author, etc. — whatever notion of similarity your training pairs express.
- **The dominant training technique**: [[ContrastiveLearning|contrastive learning]] on paired data ([[MNLI|NLI]] entailments / contradictions; question/answer pairs; image/caption pairs; paper title/abstract pairs).
- **The architectural commitment**: [[SBERTArchitecture|SBERT]] — siamese [[bert|BERT]] with [[MeanPooling|mean-pooling]] and a contrastive loss. *"The resulting architecture is also referred to as a bi-encoder or SBERT for sentence-BERT."*
- **The loss-function effect size**: 20+ STS-B points between softmax (0.59) and [[MultipleNegativesRankingLoss|MNR loss]] (0.80) on the same data — **loss choice matters more than data quantity or base-model choice**.
- **The data-availability regimes**: full labels → supervised MNR-loss fine-tuning (0.85); few labels → [[AugmentedSBERT]] (0.71 with 20% of data); no labels → [[TSDAE]] (0.70 unsupervised).
- **The domain-adaptation recipe**: unsupervised pretraining ([[TSDAE]] or [[MaskedLanguageModel|MLM]]) on target-domain text → supervised contrastive fine-tuning on whatever labeled pairs are available.

The two pages thus form a complementary pair: **Ch 4** (`EmbeddingModel` = a frozen `model.encode(...)` you build downstream tasks on top of) and **Ch 10** (`EmbeddingModel` = a `SentenceTransformer` you train end-to-end with a contrastive objective).
