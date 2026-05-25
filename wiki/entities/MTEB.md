---
title: "MTEB (Massive Text Embedding Benchmark)"
type: entity
tags: [benchmark, embeddings, leaderboard, huggingface]
sources: [hands-on-llm-ch04-text-classification, hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# MTEB (Massive Text Embedding Benchmark)

A multi-task benchmark for evaluating **text-embedding models** across classification, clustering, pair classification, reranking, retrieval, semantic textual similarity, summarization, and bitext mining tasks. Introduced by Muennighoff, Tazi, Magne & Reimers, 2022 (arXiv:2210.07316). Hosted as an interactive leaderboard on the [[HuggingFace|Hugging Face]] Hub at `spaces/mteb/leaderboard`.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 names MTEB as the canonical **starting point for selecting an embedding model**:

> "When selecting models to generate embeddings from, the **MTEB leaderboard** is a great place to start. It contains open and closed source models benchmarked across several tasks. Make sure to not only take performance into account. The importance of inference speed should not be underestimated in real-life solutions. As such, we will use sentence-transformers/all-mpnet-base-v2 as the embedding throughout this section. It is a small but performant model." — Ch 4

The chapter's selection of [[AllMPNetBaseV2|`all-mpnet-base-v2`]] over higher-ranked but slower MTEB leaders explicitly embodies the **performance-vs-throughput tradeoff** the leaderboard surfaces.

## Why it matters

Before MTEB, embedding-model evaluation was fragmented across single-task benchmarks ([[SemanticTextualSimilarity|STS-B]] for STS; BEIR for retrieval; etc.). MTEB unified them into a single multi-task leaderboard, becoming the **de-facto reference** for sentence-embedding model selection in 2023–2024 and the explicit target for new embedding releases (Cohere Embed v3, OpenAI text-embedding-3-*, BGE / GTE / E5 / Nomic series).

## Connections

- [[AllMPNetBaseV2]] — Ch 4's specific worked model, chosen via MTEB.
- [[SentenceTransformers]] — the library underlying many MTEB models.
- [[NilsReimers]] — Sentence-BERT author, co-author of MTEB.
- [[HuggingFace]] — leaderboard host.
- [[EmbeddingModel]] / [[TextEmbedding]] — what MTEB benchmarks.
- [[hands-on-llm-ch04-text-classification]] — primary source.
- [[hands-on-llm-ch08-semantic-search-and-rag]] — Ch 8's embedding-model selection rubric.

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 re-uses MTEB as the **embedding-model selection rubric** for the chapter's local-RAG worked example — *"at the time of writing, it [[BGESmallEnV15|`BAAI/bge-small-en-v1.5`]] is high on the MTEB leaderboard for embedding models and relatively small."* The same selection criterion (high MTEB position + small size) selected `all-mpnet-base-v2` in Ch 4 and `gte-small` in Ch 5; Ch 8's choice of `bge-small-en-v1.5` continues the discipline. This is the **third chapter** in *Hands-On LLMs* using MTEB as the selection rubric for an embedding model.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 names MTEB as **the unifying multi-task benchmark** for embedding models — extending the wiki's MTEB coverage from "what to consult when picking an embedding model" (Chs 4/5/8) to "what to evaluate your trained embedding model on":

> *"A good embedding model is more than just a good score on the STSB benchmark! As we observed earlier, the GLUE benchmark has a number of tasks for which we can evaluate our embedding model. However, there exist many more benchmarks that allow for the evaluation of embedding models. To unify this evaluation procedure, the Massive Text Embedding Benchmark (MTEB) was developed. The MTEB spans 8 embedding tasks that cover 58 datasets and 112 languages."* — Ch 10

The chapter walks **one MTEB task at runnable-code granularity** — `Banking77Classification` — but explicitly defers full MTEB evaluation due to runtime: *"testing your model on the entire MTEB can take a couple of hours depending on your GPU, we will use the STSB benchmark throughout this chapter instead for illustration purposes."*

```python
from mteb import MTEB
evaluation = MTEB(tasks=["Banking77Classification"])
results = evaluation.run(model)
# {'Banking77Classification': {'mteb_version': '1.1.2', ..., 
#                              'test': {'accuracy': 0.4926, 'f1': 0.4908, 
#                                       'evaluation_time': 31.83}}}
```

**Ch 10 codifies the wiki-first observation that evaluation time is itself a MTEB output dimension** alongside accuracy/F1: *"The great thing about this evaluation benchmark is not only the diversity of the tasks and languages but that even the evaluation time is saved. Although many embedding models exist, we typically want those that are both accurate and have low latency. The tasks for which embedding models are used, like semantic search, often benefit from and require fast inference."* This justifies the consistent **performance-vs-throughput tradeoff** discipline Chs 4/5/8/10 share — never pick the highest-scoring MTEB model without checking inference cost.
