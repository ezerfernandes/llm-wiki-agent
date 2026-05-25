---
title: "sentence-transformers"
type: entity
tags: [library, python, embeddings, nlp]
sources: [hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch04-text-classification, hands-on-llm-ch05-text-clustering-topic-modeling, hands-on-llm-ch08-semantic-search-and-rag, hands-on-llm-ch09-multimodal-llms, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# sentence-transformers

Open-source Python library by [[NilsReimers|Nils Reimers]] and [[IrynaGurevych|Iryna Gurevych]] for **training and using [[TextEmbedding|text-embedding]] models**. Originated as the reference implementation for **Sentence-BERT** (Reimers & Gurevych, *"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"*, EMNLP 2019, arXiv:1908.10084) and grew into the de-facto Python interface for sentence- and document-embedding models.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 5 of *Hands-On LLMs* uses sentence-transformers' `SentenceTransformer("thenlper/gte-small")` as the embed step of the [[BERTopic]] pipeline (384-dim vectors over 44,949 [[ArXivNLP|ArXiv NLP]] abstracts) — see [[GTESmall]] for the model and [[hands-on-llm-ch05-text-clustering-topic-modeling]] for the worked example. The same library API powers both Ch 4 (`all-mpnet-base-v2` for classification embeddings) and Ch 5 (`gte-small` for clustering embeddings); the only knob that changes is the underlying [[MTEB|MTEB]] task-column the practitioner optimizes for.

Ch 2 introduces sentence-transformers as the canonical library for producing [[TextEmbedding|text embeddings]]:

> "We can produce text embeddings with sentence-transformers, a popular package for leveraging pretrained embedding models. The package, like transformers in the previous chapter, can be used to load publicly available models." — Ch 2

The chapter's worked example uses the **`sentence-transformers/all-mpnet-base-v2`** model:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
vector = model.encode("Best movie ever!")
vector.shape  # (768,)
```

— a 768-dim vector per input sentence.

## Why it matters

The library standardized **siamese-BERT contrastive training** for embeddings: instead of pooling a generic encoder's outputs and hoping the geometry is useful, train end-to-end with a contrastive objective (positive sentence pairs pull together, negative pairs push apart). This recipe — and the resulting model zoo on [[HuggingFace|Hugging Face]] — is the foundation of essentially every modern **[[SemanticSearch|semantic-search]]** and **[[rag|RAG]]** retrieval pipeline.

## Common models

- `all-MiniLM-L6-v2` — 384-dim, fast, the de-facto default for RAG. ([[leh-ch04-rag-feature-pipeline]] uses this.)
- `all-mpnet-base-v2` — 768-dim, higher quality at higher cost. (*Hands-On LLMs* Ch 2's worked example.)
- `multi-qa-*` variants — trained on QA pairs specifically.
- The **MTEB leaderboard** ([[HuggingFace]]) compares dozens of these on a standard benchmark suite.

## Connections

- [[NilsReimers]] / [[IrynaGurevych]] — co-authors of Sentence-BERT and core maintainers.
- [[HuggingFace]] — the model-hub home for sentence-transformers checkpoints.
- [[AllMPNetBaseV2]] — Ch 2's specific worked model.
- [[TextEmbedding]] / [[SentenceEmbedding]] / [[Embedding]] — the concept layer the library implements.
- [[rag]] / semantic search — downstream consumers.
- [[bert]] — the underlying encoder Sentence-BERT was first trained on top of.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 worked example.
- [[ColBERTv2]] — alternative late-interaction retrieval architecture; uses different objective.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 promotes sentence-transformers from *embedding-tour candidate* (Ch 2) to **the core embedding substrate for three of the four classification regimes**:

1. **Supervised classification** — `model.encode(...)` produces 768-dim features for [[LogisticRegression]] (F1 = 0.85).
2. **[[ZeroShotClassification|Zero-shot classification]]** — `model.encode(label_descriptions)` produces label embeddings; `sklearn.metrics.pairwise.cosine_similarity` assigns labels (F1 = 0.78).
3. **(Forward-referenced)** semantic search and clustering in Chs 5 and 8 reuse the same `all-mpnet-base-v2` embeddings.

The chapter notes that **the same library can be replaced by API-based embedding providers** (Cohere's and OpenAI's offerings) to remove GPU dependency entirely — *"this would allow the pipeline to run entirely on the CPU."*

## From [[hands-on-llm-ch08-semantic-search-and-rag|*Hands-On LLMs* Ch 8]]

Ch 8 names sentence-transformers as the **open-source path for retrieval and reranking**:

> *"If you want to locally set up retrieval and reranking on your own machine, then you can use the Sentence Transformers library. Refer to the documentation at https://oreil.ly/jJOhV for setup. Check the 'Retrieve & Re-Rank' section for instructions and code examples for how to conduct these steps in the library."* — Ch 8

The library is positioned as **the local alternative to [[Cohere]]'s managed `co.embed` + `co.rerank` endpoints** — same architectural pattern (bi-encoder retrieval + cross-encoder reranking), open-weights models instead of managed API. Common production rerankers from sentence-transformers's catalog:

- `cross-encoder/ms-marco-MiniLM-L-6-v2` — the canonical small cross-encoder reranker.
- `cross-encoder/ms-marco-TinyBERT-L-2-v2` — the smaller / faster variant.
- [[BAAI]]'s `bge-reranker-base` / `bge-reranker-large` — published by Beijing Academy of Artificial Intelligence; available through the same sentence-transformers API.

Ch 8 also names **[[BGESmallEnV15|`BAAI/bge-small-en-v1.5`]]** as the local-RAG embedding model — loaded via `HuggingFaceEmbeddings` (LangChain) rather than the sentence-transformers `SentenceTransformer` class directly, though the underlying weights and serving pattern are the same.

## From [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]]

Ch 9 extends sentence-transformers' role from text-only embedding into **multimodal embedding** — the chapter names `SentenceTransformer("clip-ViT-B-32")` as the **easy-mode wrapper around [[CLIP|CLIP / OpenCLIP]]**: *"sentence-transformers implements a few CLIP-based models that make it much easier to create embeddings. It only takes a few lines of code."*

```python
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("clip-ViT-B-32")
image_embeddings = model.encode(images)
text_embeddings = model.encode(captions)
sim_matrix = util.cos_sim(image_embeddings, text_embeddings)
```

The same `.encode(...)` API surface that produces text embeddings in Chs 2/4/5/8 now **accepts PIL images as well as strings** — making sentence-transformers the single most ergonomic Python entry point to the CLIP family for both text and image work. This is the wiki's first record of sentence-transformers used as a **multimodal** embedding library; prior chapters touched only the text-encoder side.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 is the **first chapter that trains** sentence-transformers models from scratch (and fine-tunes existing ones), where Chs 2/4/5/8/9 used `model.encode(...)` as a frozen black box. Ch 10 introduces the **training-side API surface**:

- **`SentenceTransformer(...)`** — load a model (either a pretrained name like `bert-base-uncased` for from-scratch training, or a sentence-transformers model name like `all-MiniLM-L6-v2` for fine-tuning).
- **`losses.*`** — the loss functions: `SoftmaxLoss`, `CosineSimilarityLoss`, `MultipleNegativesRankingLoss`, `DenoisingAutoEncoderLoss`, `MarginMSE`, ...
- **`SentenceTransformerTrainer`** + **`SentenceTransformerTrainingArguments`** — Hugging Face `Trainer`-pattern training loop.
- **`evaluation.EmbeddingSimilarityEvaluator`** — evaluator for [[STSB|STS-B]]-style sentence-pair similarity tasks.
- **`models.Transformer`** + **`models.Pooling(..., "mean" | "cls")`** — manual construction of the encoder + pooling stack (used in Ch 10's TSDAE example to switch from default mean-pooling to [CLS]-pooling).
- **`datasets.DenoisingAutoEncoderDataset`** — helper to add deletion noise to sentences for TSDAE.
- **`cross_encoder.CrossEncoder`** — the cross-encoder counterpart, used in Augmented SBERT to label silver datasets.
- **`datasets.NoDuplicatesDataLoader`** — used by Augmented SBERT.

**By default, all layers are trainable**: *"By default, all layers of an LLM in sentence-transformers are trainable. Although it is possible to freeze certain layers, it is generally not advised since the performance is often better when unfreezing all layers."*

**The training-data discipline** Ch 10 codifies: NLI datasets ([[GLUE]] [[MNLI]] in the worked example) are the canonical contrastive-learning data source; entailment = positive, contradiction = negative. *"The main difficulty of training or fine-tuning your model is finding the right data. With these models, we not only want to have very large datasets, but the data in itself needs to be of high quality."*

**The loss-function ladder** Ch 10 walks (on the same 50k MNLI subset, evaluated on STS-B Pearson cosine): [[SoftmaxLoss]] 0.59 → [[CosineSimilarityLoss]] 0.72 → [[MultipleNegativesRankingLoss|MNR loss]] 0.80 → fine-tune `all-MiniLM-L6-v2` with MNR 0.85.

**Two production fine-tuning workflows** Ch 10 walks at code level:

- **[[AugmentedSBERT]]** (few-labels regime): `CrossEncoder` labels a silver dataset from a gold dataset; `SentenceTransformer` trains on gold + silver. The wiki's first runnable demonstration.
- **[[TSDAE]]** (no-labels regime): `DenoisingAutoEncoderDataset` + `models.Pooling(..., "cls")` + `losses.DenoisingAutoEncoderLoss(model, tie_encoder_decoder=True)`. The **only place** in the wiki where [CLS]-pooling beats mean-pooling.

**[[DomainAdaptation|Domain adaptation]] via [[AdaptivePretraining|adaptive pretraining]]**: Ch 10's closing recipe combines TSDAE (or MLM) on target-domain text with supervised fine-tuning on whatever labeled pairs are available. *"Using everything you have learned in this chapter, you should be able to reproduce this pipeline!"*

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 uses sentence-transformers as the **embedding-model substrate for [[SetFit]]** — *"It is built on top of the architecture of sentence-transformers to generate high-quality textual representations that are updated during training."* The Ch 11 worked recipe wraps `sentence-transformers/all-mpnet-base-v2` ([[AllMPNetBaseV2]]) inside a `SetFitModel.from_pretrained(...)` and fine-tunes it via contrastive learning on in-class / out-class sentence pairs generated from a small labeled dataset (16 examples per class).

The Ch 11 contribution to the sentence-transformers narrative: SetFit demonstrates that the **same sentence-transformers contrastive-fine-tuning machinery** that Ch 10 walked for from-scratch embedding-model creation also serves as the engine for **few-shot text classification** when paired with a downstream classifier head.
