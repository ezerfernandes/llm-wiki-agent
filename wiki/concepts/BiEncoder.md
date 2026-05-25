---
title: "Bi-Encoder"
type: concept
tags: [retrieval, embeddings, cross-encoder, ir]
sources: [hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Bi-Encoder

**Bi-encoder** is the embedding architecture where **query and document are encoded independently** by the same (or a sibling) model, then compared via [[CosineSimilarity|cosine similarity]] / dot product / L2 distance. The structural complement of the [[CrossEncoder|cross-encoder]] — which encodes them **jointly**.

## The bi-encoder vs cross-encoder tradeoff

| Property | Bi-encoder | Cross-encoder |
|---|---|---|
| Document encoding | **Once at index time** | Per query |
| Per-query cost | 1 query embed + N cosine sims | **N joint forward passes** |
| Accuracy | Lower (no cross-attention between query and doc) | **Higher** |
| Use case | First-stage retrieval | Second-stage reranking |

The **production-default two-stage pattern** that exploits both:

1. **Bi-encoder first-stage** — retrieve top-100 or top-1000 candidates fast.
2. **[[CrossEncoder|Cross-encoder]] second-stage reranking** — re-score the candidate set with the more expensive but more accurate model; return top-3 or top-5.

This is the [[ReRanking|reranking]] pipeline pattern [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]] codifies — *"this shortlisting step is called the first stage of the search pipeline."*

## Position in the embedding-model lineage

All standard [[SentenceTransformers|sentence-transformers]] embedding models are bi-encoders — `all-mpnet-base-v2`, `gte-small`, `bge-small-en-v1.5`, OpenAI `text-embedding-3-*`, Cohere `embed-*`. The query and the document are passed through the **same** encoder (siamese architecture); their output embeddings live in the same vector space; similarity = cosine.

The **Sentence-BERT paper** (Reimers & Gurevych 2019, EMNLP) was the first widely-adopted formulation of the bi-encoder approach to sentence embeddings — *"a modification of the BERT network using siamese and triplet networks that produces semantically meaningful sentence embeddings."*

## Connections

- [[CrossEncoder]] — the complementary architecture.
- [[ReRanking]] — the production pattern that uses both.
- [[DenseRetrieval]] / [[EmbeddingBasedRetrieval]] — the family bi-encoders power.
- [[SentenceTransformers]] / [[CohereEmbed]] / [[BGESmallEnV15]] / [[GTESmall]] — bi-encoder model examples.
- [[CosineSimilarity]] — the standard scoring function.
- [[FAISS]] / [[VectorDatabase]] — storage of the bi-encoder's document embeddings.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — primary source.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10's runnable training pipeline for bi-encoders (see section below).

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 is the **first chapter that trains** a bi-encoder from scratch, rather than just using a pretrained one. The chapter codifies the structural problem the bi-encoder solves vs the [[CrossEncoder|cross-encoder]]:

> *"Before sentence-transformers, sentence embeddings often used an architectural structure called cross-encoders with BERT. ... finding the highest pair in a collection of 10,000 sentences ... would require $n \cdot (n-1)/2 = 49{,}995{,}000$ inference computations and therefore generates significant overhead. Moreover, a cross-encoder generally does not generate embeddings."* — Ch 10

The bi-encoder is the **structural workaround**: encode each sentence ONCE into a fixed-size vector (via [[MeanPooling|mean-pooling]] of the final layer), then any-pair similarity is a cheap cosine-similarity computation. For 10,000 sentences: 10,000 encoder forward passes + $n(n-1)/2$ cosine sims (free) — vs the cross-encoder's 49,995,000 encoder forward passes.

**The [[SiameseNetwork|siamese-network]] training topology**: per Ch 10, *"we have two identical BERT models that share the same weights and neural architecture. ... Since the weights are identical for both BERT models, we can use a single model and feed it the sentences one after the other."*

**Ch 10's loss-function ladder** for bi-encoder training (50k MNLI subset, STS-B Pearson cosine):

- [[SoftmaxLoss|Softmax loss]] (original SBERT training) → 0.59
- [[CosineSimilarityLoss|Cosine similarity loss]] → 0.72
- [[MultipleNegativesRankingLoss|MNR loss]] → 0.80
- Fine-tune `all-MiniLM-L6-v2` with MNR loss → **0.85**

**The cross-encoder is used at training time in [[AugmentedSBERT]]**, even though only the bi-encoder is used at inference: a fine-tuned cross-encoder labels a silver dataset from a small gold dataset; the bi-encoder is then trained on gold + silver. Augmented SBERT is the canonical *"train with the cross-encoder, deploy the bi-encoder"* pattern in the wiki.
