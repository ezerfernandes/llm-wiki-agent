---
title: "Label Embedding"
type: concept
tags: [llm, embeddings, zero-shot, classification]
sources: [hands-on-llm-ch04-text-classification]
last_updated: 2026-05-23
---

# Label Embedding

A **dense vector representation of a class label** — produced by passing a natural-language *description* of the label (not just its name) through an [[EmbeddingModel|embedding model]] — so that documents and labels live in the **same vector space** and can be compared via [[CosineSimilarity|cosine similarity]].

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

The chapter's core trick for **[[ZeroShotClassification|zero-shot classification]]**:

```python
# Embed natural-language label descriptions, not bare class IDs
label_embeddings = model.encode([
    "A negative review",
    "A positive review",
])
```

By embedding labels in the same space as documents, the chapter eliminates the need for labeled training data — *"by describing and embedding the labels and documents, we have data that we can work with."* Documents are then classified by **nearest-neighbor cosine similarity** to the label embeddings.

> "To embed the labels, we first need to give them a description, such as 'a negative movie review.' This can then be embedded through sentence-transformers." — Ch 4

## Why the description matters

A label embedding is **only as good as its description**. Bare label names (`"positive"`, `"negative"`) carry little semantic content; richer descriptions (`"A very negative movie review"`) anchor the embedding closer to the document distribution. Per Ch 4: *"we can make them a bit more concrete and specific toward our data ... the embedding will capture that it is a movie review and will focus a bit more on the extremes of the two labels."*

This makes label-embedding design a **prompt-engineering activity** — iterative refinement of the label description string, the same way one would iterate on an instruction prompt.

## Connections

- [[ZeroShotClassification]] — the technique that uses label embeddings.
- [[EmbeddingModel]] / [[SentenceTransformers]] / [[AllMPNetBaseV2]] — the embedding backbone.
- [[CosineSimilarity]] — the label-assignment metric.
- [[PromptEngineering]] — the discipline of refining the label description.
- [[Embedding]] / [[TextEmbedding]] — parent concepts.
- [[hands-on-llm-ch04-text-classification]] — primary source.
