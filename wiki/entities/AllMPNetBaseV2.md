---
title: "all-mpnet-base-v2"
type: entity
tags: [model, embeddings, sentence-transformers]
sources: [hands-on-llm-ch02-tokens-and-embeddings, hands-on-llm-ch04-text-classification, hands-on-llm-ch10-creating-text-embedding-models, hands-on-llm-ch11-fine-tuning-representation-models]
last_updated: 2026-05-23
---

# all-mpnet-base-v2

A [[SentenceTransformers|sentence-transformers]] [[TextEmbedding|text-embedding]] model — `sentence-transformers/all-mpnet-base-v2` on [[HuggingFace|Hugging Face]] — built on Microsoft's MPNet encoder backbone. **Output dimension: 768.** Mid-cost / high-quality default for sentence-embedding tasks.

## From [[hands-on-llm-ch02-tokens-and-embeddings|*Hands-On LLMs* Ch 2]]

Ch 2 uses `all-mpnet-base-v2` as its worked example for [[TextEmbedding|text embeddings]]:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
vector = model.encode("Best movie ever!")
vector.shape  # (768,)
```

> "This sentence is now encoded in this one vector with a dimension of 768 numerical values." — Ch 2

The chapter forward-references **Chapter 4** for guidance on choosing among the many available embedding models for a specific task.

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 makes `all-mpnet-base-v2` the **default embedding model for two of the chapter's four classification regimes**:

1. **Embedding + logistic regression** — `model.encode(...)` produces `(8530, 768)` train features; [[LogisticRegression]] reaches **F1 = 0.85** on Rotten Tomatoes.
2. **[[ZeroShotClassification|Zero-shot classification]]** — `model.encode(["A negative review", "A positive review"])` produces 2 × 768 [[LabelEmbedding|label embeddings]]; cosine similarity assigns labels at **F1 = 0.78** with no labeled training data.

The choice was made via the [[MTEB|MTEB leaderboard]] balancing performance with inference speed: *"a small but performant model."* The chapter forward-references the same `all-mpnet-base-v2` for **Ch 5** (clustering / topic modeling) and **Ch 8** (semantic search / RAG).

## Position vs alternatives

| Model | Dim | Speed | Quality |
|---|---|---|---|
| `all-MiniLM-L6-v2` | 384 | Fast | Good |
| **`all-mpnet-base-v2`** | **768** | **Mid** | **Better** |
| `all-MiniLM-L12-v2` | 384 | Mid | Mid |
| `all-distilroberta-v1` | 768 | Mid | Good |

Choice between MiniLM-L6 (RAG defaults — see [[leh-ch04-rag-feature-pipeline]]) and mpnet-base-v2 (this chapter's choice) is the canonical embedding-quality-vs-throughput tradeoff in sentence-transformers.

## Connections

- [[SentenceTransformers]] — the library that loads this model.
- [[TextEmbedding]] / [[SentenceEmbedding]] / [[Embedding]] — the concept type.
- [[HuggingFace]] — model hub host.
- [[NilsReimers]] / [[IrynaGurevych]] — sentence-transformers maintainers.
- [[HandsOnLLM]] / [[hands-on-llm-ch02-tokens-and-embeddings]] — Ch 2 worked example.
- [[rag]] / semantic search — typical downstream uses.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 mentions `all-mpnet-base-v2` only briefly — as the **possible-but-overkill out-of-domain alternative** to `bert-base-uncased` and `all-MiniLM-L6-v2`: *"instead of using a pretrained BERT model like 'bert-base-uncased' or a possible out-of-domain model like 'all-mpnet-base-v2', you can also perform masked language modeling on the pretrained BERT model to first adapt it to your domain."*

The chapter's fine-tuning worked example chose **`all-MiniLM-L6-v2`** (smaller, faster) rather than `all-mpnet-base-v2` (more accurate). Both are reasonable choices — Ch 10 picks MiniLM-L6 because *"due to its small size [it] is quite fast"* in the chapter's pedagogical context. For production fine-tuning where the target is the highest possible STS-B / MTEB score, `all-mpnet-base-v2` is the stronger base.

The structural role of mpnet-base in Ch 10: it appears as **the alternative the chapter chose NOT to fine-tune from**, naming the same speed-vs-quality tradeoff that previous chapters established for the model. Ch 10's loss-ladder demonstration would have produced higher absolute scores on mpnet-base-v2 but the relative differences across losses (softmax 0.59 → cosine 0.72 → MNR 0.80 → fine-tune 0.85) are what the chapter argues — and those would hold qualitatively on either base model.

## From [[hands-on-llm-ch11-fine-tuning-representation-models|*Hands-On LLMs* Ch 11]]

Ch 11 uses `all-mpnet-base-v2` as the **base [[SentenceTransformers|SentenceTransformer]] for [[SetFit]]** — loaded via `SetFitModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")` and fine-tuned via contrastive learning on in-class / out-class sentence pairs generated from 32 labeled examples (16 per class) on Rotten Tomatoes. Result: **F1 = 0.85** — matching the F1 a logistic regression trained on `all-mpnet-base-v2` embeddings of the full 8,500-example dataset achieves in Ch 2 / Ch 4.

Per Ch 11: *"the official documentation contains an overview of pretrained SentenceTransformer models from which we are going to be using 'sentence-transformers/all-mpnet-base-v2'. It is one of the best-performing models on the MTEB leaderboard."*

Ch 11 also names `all-mpnet-base-v2` as the substrate for the **differentiable-head SetFit variant**:

```python
model = SetFitModel.from_pretrained(
    "sentence-transformers/all-mpnet-base-v2",
    use_differentiable_head=True,
    head_params={"out_features": num_classes},
)
```

This continues the wiki's pattern of `all-mpnet-base-v2` as the **default high-quality 768-dim embedding model** across multiple chapters and tasks.
