---
title: "Semantic Similarity"
type: concept
tags: [evaluation, metric, embeddings, nlp]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Semantic Similarity

**Semantic similarity** measures *"how close the generated response is to the reference responses in meaning"* ([[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]) — using [[Embedding|embeddings]] rather than surface tokens. Also called **embedding similarity**.

## The pipeline

1. Convert candidate and reference into embedding vectors.
2. Compute [[CosineSimilarity|cosine similarity]] between embeddings.
3. Score is in [-1, 1] (or [0, 1] for many text-embedding spaces). Higher = more semantically similar.

## Why it beats lexical

Ch 3's canonical examples:
- *"What's up?"* and *"How are you?"* — lexically distant, semantically close. Semantic similarity correctly scores them as similar; lexical similarity does not.
- *"Let's eat, grandma"* vs *"Let's eat grandma"* — lexically close, semantically opposite. Semantic similarity *should* score them as different, although the punctuation-only difference is hard to catch.

## Metrics

- **[[BERTScore]]** — embeddings from [[bert|BERT]]; precision/recall/F1 via greedy matching.
- **[[MoverScore]]** — embeddings from a *mixture* of algorithms.

## Caveat: still depends on embedding quality

Per Ch 3: *"The reliability of semantic similarity depends on the quality of the underlying embedding algorithm. Two texts with the same meaning can still have a low semantic similarity score if their embeddings are bad."* And the underlying embedding model may add nontrivial compute and latency.

## The "exact-but-subjective" twist

Ch 3 places semantic similarity in the [[ExactEvaluation|exact-evaluation]] category but flags a nuance:

> "While I put semantic similarity in the exact evaluation category, it can be considered subjective, as different embedding algorithms can produce different embeddings. However, given two embeddings, the similarity score between them is computed exactly."

So: *the embedding step is subjective; the cosine-similarity step is exact.*

## Modality-agnostic

Although Ch 3 uses text, semantic similarity computes the same way for images, audio, and any data with a learned embedding space — see [[MultimodalEmbeddingSpace]] and [[ImageBind]] for the cross-modality extension.

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[SimilarityMeasurement]] — parent.
- [[Embedding]] — the substrate.
- [[CosineSimilarity]] — the standard score function.
- [[BERTScore]] / [[MoverScore]] — concrete metrics.
- [[bert|BERT]] / [[CLIP]] / [[SentenceTransformers]] — embedding-model lineage.
- [[LexicalSimilarity]] — the surface-form alternative.
- [[SemanticTextualSimilarity]] — the task this metric measures.
- [[MultimodalEmbeddingSpace]] / [[ImageBind]] / [[ULIP]] — cross-modal extension.
- [[SemanticSearch]] — the application that ranks documents by semantic similarity to a query (Ch 8 of *Hands-On LLMs*'s dense-retrieval framing).
