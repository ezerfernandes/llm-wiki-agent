---
title: "MNLI (Multi-Genre Natural Language Inference)"
type: concept
tags: [dataset, benchmark, nli, glue, training-data, embeddings]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# MNLI (Multi-Genre Natural Language Inference)

**MNLI** — the **Multi-Genre Natural Language Inference** corpus — *"a collection of 392,702 sentence pairs annotated with entailment (contradiction, neutral, entailment)"* per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]. One of nine tasks in the [[GLUE]] benchmark. Introduced by Williams, Nangia & Bowman 2018 (*"A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference,"* NAACL).

## Structure

- **Size**: 392,702 train / ~9,815 dev (matched) / ~9,832 dev (mismatched) / ~9,847 test sentence pairs.
- **Labels**: 3-way — `0=entailment`, `1=neutral`, `2=contradiction`.
- **Genres**: 10 written and spoken domains (fiction, government, slate, telephone, travel + 5 mismatched).
- **The "Multi-Genre" name** distinguishes MNLI from the earlier [[SNLI]] (Stanford NLI), which is single-genre (Flickr30k captions only).

## Sample row (Ch 10)

```python
dataset[2]
# {'premise': 'One of our number will carry out your instructions minutely.',
#  'hypothesis': 'A member of my team will execute your orders with immense precision.',
#  'label': 0}  # entailment
```

## Use in Ch 10

Ch 10 uses a **50,000-pair subset** of MNLI as the training data for every regime in its STS-B loss-function ladder (softmax, cosine, MNR, supervised fine-tune, Augmented SBERT, TSDAE). The chapter notes: *"do note, though, that the smaller the dataset, the more unstable training or fine-tuning an embedding model is. If possible, larger datasets are preferred assuming it is still quality data."*

```python
train_dataset = load_dataset("glue", "mnli", split="train").select(range(50_000))
train_dataset = train_dataset.remove_columns("idx")
```

## NLI as contrastive-data source

Ch 10 codifies the wiki's clearest statement of **why NLI datasets are the standard pretraining-data source for sentence embeddings**: entailment pairs are positives, contradiction pairs are negatives. *"If you look closely at entailment and contradiction, then they describe the extent to which two inputs are similar to one another. As such, we can use NLI datasets to generate negative examples (contradictions) and positive examples (entailments) for contrastive learning."*

For [[MultipleNegativesRankingLoss|MNR loss]], Ch 10 filters MNLI to entailment-only rows (50k → 16,875), uses the premise as anchor, the hypothesis as positive, and a randomly-shuffled hypothesis column as soft negatives.

For [[CosineSimilarityLoss|cosine loss]], Ch 10 maps the labels: entailment → 1.0, neutral/contradiction → 0.0.

For [[SoftmaxLoss]], Ch 10 keeps all 3 labels and trains a 3-way classifier head.

## Relationship to SNLI

| Dataset | Genres | Train pairs | Source |
|---|---|---|---|
| **[[SNLI]]** | 1 (Flickr30k captions) | ~550k | Bowman, Angeli, Potts & Manning 2015 |
| **MNLI** | 10 (multi-domain) | ~393k | Williams, Nangia & Bowman 2018 |
| **MultiNLI = MNLI** | — | — | — |

The Sentence-BERT paper (Reimers & Gurevych 2019) trained on the **combination of SNLI + MNLI** (~900k pairs). Ch 10 simplifies to MNLI-only for pedagogical purposes.

## Connections

- [[GLUE]] — the parent benchmark suite.
- [[SNLI]] — the single-genre Stanford predecessor.
- [[NaturalLanguageInference]] — the task NLI datasets benchmark.
- [[ContrastiveLearning]] — the paradigm NLI data feeds.
- [[MultipleNegativesRankingLoss]] / [[CosineSimilarityLoss]] / [[SoftmaxLoss]] — the Ch 10 losses trained on MNLI.
- [[STSB]] — the evaluation counterpart for the trained models.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
