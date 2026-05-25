---
title: "all-MiniLM-L6-v2"
type: entity
tags: [model, embeddings, sentence-transformers, minilm, fast]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# all-MiniLM-L6-v2

A [[SentenceTransformers|sentence-transformers]] [[TextEmbedding|text-embedding]] model — `sentence-transformers/all-MiniLM-L6-v2` on [[HuggingFace|Hugging Face]]. **Output dimension: 384.** The de-facto small / fast default for the SBERT family.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 names `all-MiniLM-L6-v2` as **the recommended pretrained base for supervised fine-tuning of [[SBERT|SBERT]]-family embedding models**:

> *"There are many to choose from but generally, all-MiniLM-L6-v2 performs well across many use cases and due to its small size is quite fast."* — Ch 10

The chapter's fine-tuning worked example uses it as the base model with [[MultipleNegativesRankingLoss|MNR loss]] on the same 50,000 MNLI pairs used for the from-scratch runs:

```python
embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
train_loss = losses.MultipleNegativesRankingLoss(model=embedding_model)
# ... train ...
```

Result: STS-B Pearson cosine = **0.85** — the **highest score in Ch 10's loss ladder**, beating all from-scratch training regimes. The chapter notes: *"the pretrained model that we used for fine-tuning was already trained on the full MNLI dataset, whereas we only used 50,000 examples. It might seem redundant but this example demonstrates how to fine-tune a pretrained embedding model on your own data."*

## Position vs alternatives

| Model | Dim | Speed | Quality |
|---|---|---|---|
| **`all-MiniLM-L6-v2`** | **384** | **Fast** | **Good** |
| `all-mpnet-base-v2` | 768 | Mid | Better |
| `all-MiniLM-L12-v2` | 384 | Mid | Mid |
| `all-distilroberta-v1` | 768 | Mid | Good |

The MiniLM family is based on Microsoft's MiniLM distillation work (Wang et al. 2020, *"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers"*). The `L6` indicates 6 transformer layers (vs MPNet's 12), the major source of speedup.

## Training data

`all-MiniLM-L6-v2` was trained on a billion+ sentence pairs combined from many datasets (Reddit comments, S2ORC citation pairs, WikiAnswers, PAQ, S2ORC titles + abstracts, SearchQA, Eli5, Flickr30k, MS MARCO, QQP, MNLI, SNLI, GooAQ, Yahoo Answers, ...) under [[MultipleNegativesRankingLoss|MNR loss]] with in-batch negatives.

## Connections

- [[SentenceTransformers]] — the library that loads this model.
- [[TextEmbedding]] / [[SentenceEmbedding]] / [[SBERT]] — the model family.
- [[AllMPNetBaseV2]] — the higher-quality / slower sibling.
- [[MultipleNegativesRankingLoss]] — the loss used to train it (and to fine-tune it in Ch 10).
- [[HuggingFace]] — model hub host.
- [[microsoft|Microsoft]] — origin of the underlying MiniLM distillation.
- [[NilsReimers]] / [[IrynaGurevych]] — sentence-transformers maintainers.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — Ch 10's fine-tuning base model.
