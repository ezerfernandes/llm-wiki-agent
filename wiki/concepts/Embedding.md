---
title: "Embedding"
type: concept
tags: [rag, retrieval, representations, nlp, llm-engineering]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch04-rag-feature-pipeline, leh-ch05-supervised-fine-tuning, leh-ch09-rag-inference-pipeline, hands-on-llm-ch01-introduction-to-llms, hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, mlsysbook-ch06-network-architectures]
last_updated: 2026-06-05
---

## Definition
An **embedding** is a dense, low-dimensional vector representation of a piece of data (text token, sentence, document, image, audio spectrogram) produced by a learned model, such that geometrically close vectors correspond to semantically similar inputs. Embeddings are the substrate of [[rag|RAG]] retrieval and of every modern vector-search system.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] names embedding as the third feature-pipeline operation (clean → chunk → embed) that populates the [[VectorDatabase]]. [[leh-ch04-rag-feature-pipeline]] is the depth treatment: embeddings are typically 64–2048 dimensional, outperform [[OneHotEncoding]] (curse of dimensionality) and feature hashing (collisions, lost semantics), and can be produced by [[Word2Vec]]/[[GloVe]] (classical), encoder-only transformers like [[bert|BERT]] and RoBERTa (modern), [[CNN]]s (images via ResNet-style backbones), or cross-modal models like CLIP (text + image in a shared space; audio via spectrogram-then-image-model). The chapter introduces **Sentence Transformers** (HuggingFace's MTEB leaderboard) as the practical entry point, with `all-MiniLM-L6-v2` and `all-mpnet-base-v2` as defaults, plus **instructor-style** embedding models that accept a natural-language instruction prefix. [[leh-ch09-rag-inference-pipeline]] reuses the same `EmbeddingDispatcher` from the feature pipeline at inference time — a critical invariant to avoid [[TrainingServingSkew|training-serving skew]] in retrieval.

## Key details
- Two-stage embedding flow: (1) tokenize the input, (2) run the embedding model and pool to a fixed-dim vector.
- Same model + same preprocessing must be used at ingest and at query time; otherwise retrieval is corrupted.
- Distance metrics: cosine (most popular), Euclidean, Manhattan, dot product — choice depends on data and embedding model.
- Defaults in the LLM Twin: `sentence-transformers/all-MiniLM-L6-v2` (384 dim).
- An `EmbeddingModelSingleton` ensures the SentenceTransformer model is loaded once into memory.
- Embedding batches benefit from GPU throughput (10x+ speedup via parallel inference).

## Connections
- [[VectorDatabase]] — stores embeddings.
- [[rag]] — retrieves by embedding similarity.
- [[CosineSimilarity]] — primary distance metric.
- [[Tokenization]] / [[Tokenizer]] — the step that precedes embedding.
- [[Word2Vec]] / [[GloVe]] / [[FastText]] / [[bert]] — classical and modern embedding lineage.
- [[CNN]] / [[ResNet]] — image embedders.
- [[OneHotEncoding]] — explicit foil; embeddings condense info into a dense vector while preserving semantic similarity.
- [[CurseOfDimensionality]] — invoked to motivate dense embeddings over one-hot.
- [[ContextualEmbedding]] — the modern (transformer-produced) class of embeddings.
- [[TrainingServingSkew]] — failure mode when ingest-time and query-time embedding models drift apart.
- [[Chunking]] — produces the units that get embedded.
- [[mlsysbook-ch06-network-architectures]] — systems view: in [[DLRM]]/RecSys, embeddings live in massive [[EmbeddingTable|embedding tables]] (each lookup a random gather into a TB-scale table), making recommendation the *memory-capacity-bound* workload distinct from compute-bound vision/language.

## From [[hands-on-llm-ch01-introduction-to-llms|*Hands-On LLMs* Ch 1]]

Ch 1 supplies the **pedagogical intuition** for embeddings as "compressed meaning" — *"vector representations of data that attempt to capture its meaning"* — and the **granularity taxonomy** (word vs sentence vs document embeddings; see [[WordEmbedding]]). Ch 1 also names the static-vs-contextual distinction:

> "The training process of word2vec creates static, downloadable representations of words. ... 'bank' can refer to both a financial bank as well as the bank of a river. Its meaning, and therefore its embeddings, should change depending on the context." — Ch 1

This motivates the move from [[Word2Vec|word2vec]]-style static embeddings to **[[ContextualEmbedding|contextual embeddings]]** produced by [[RNN]]+attention encoders and ultimately [[transformer|Transformer]]-based encoders like [[bert|BERT]]. The chapter forward-references Ch 2 for the deep-dive into token embeddings and Ch 10 for training custom embedding models.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 is the **wiki's canonical deep-dive on the embedding layer of an LLM**. Key contributions:

**Embedding taxonomy** Ch 2 codifies:
- **[[TokenEmbedding|Token embeddings]]** — the per-token rows of the model's embedding matrix; [[StaticEmbedding|static]] (looked up by ID, same vector regardless of context).
- **[[ContextualEmbedding|Contextualized token embeddings]]** — what the model produces after attention layers process the static inputs (per-position, context-dependent).
- **[[TextEmbedding|Text embeddings]]** — single vectors per sentence / paragraph / document.
- **[[SentenceEmbedding|Sentence embeddings]]** — the sentence-level special case.

**The LLM-as-embedding-matrix view**: *"The language model holds an embedding vector for each token in the tokenizer's vocabulary. ... a portion of the model is this embeddings matrix holding all of these vectors."* The matrix is randomly initialized and trained jointly with the rest of the model.

**Tokenizer-model binding**: *"a pretrained language model is linked with its tokenizer and can't use a different tokenizer without training"* — because the token-ID-to-embedding mapping is learned jointly.

**Production text-embedding recipe** (Ch 2 worked example):
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
vector = model.encode("Best movie ever!")  # (768,)
```
Two production approaches the chapter names: (1) mean-pool token embeddings from a generic encoder, or (2) use a model trained specifically on a text-embedding objective (the [[SentenceTransformers|sentence-transformers]] / Sentence-BERT recipe).

**Embeddings work beyond text** — the chapter's headline non-NLP demonstration is the [[Word2VecRecommender|song-embedding recommender]] built by training [[Word2Vec|word2vec]] on playlist sequences. The same pattern works for products in baskets, pages in sessions, anywhere objects appear in user-generated sequences.
