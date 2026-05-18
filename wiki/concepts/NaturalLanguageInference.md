---
title: "Natural Language Inference"
type: concept
tags: [nlp, text-pair-classification, application]
sources: [d2l-nlp-applications]
last_updated: 2026-05-16
---

# Natural Language Inference

**Natural language inference (NLI)** — also known as *recognizing textual entailment* — determines the logical relationship between a pair of text sequences: a **premise** and a **hypothesis**. Per [[d2l-nlp-applications]] §`natural-language-inference-and-dataset`: "determines the logical relationship between a pair of text sequences."

## Three labels

- **Entailment** — the hypothesis can be inferred from the premise.
  *e.g.* Premise: "Two women are hugging each other." → Hypothesis: "Two women are showing affection."
- **Contradiction** — the negation of the hypothesis can be inferred from the premise.
  *e.g.* Premise: "A man is running the coding example from Dive into Deep Learning." → Hypothesis: "The man is sleeping."
- **Neutral** — neither entailment nor contradiction.
  *e.g.* Premise: "The musicians are performing for us." → Hypothesis: "The musicians are famous."

## Canonical benchmark

The Stanford **[[SNLI|SNLI corpus]]** (Bowman, Angeli, Potts & Manning 2015) — 500k+ labeled English sentence pairs, balanced across the three labels in train and test splits.

## Architectures (per [[d2l-nlp-applications]])

- **[[DecomposableAttention|Decomposable attention]]** (Parikh et al. 2016): attend → compare → aggregate over GloVe embeddings + MLPs. No recurrence, no convolution; achieves the SNLI SOTA of its time with $\mathcal{O}(m+n)$ MLP applications via the decomposition trick.
- **Fine-tuned [[BERT]]**: text-pair input `[CLS] premise [SEP] hypothesis [SEP]` → [[ClsToken|`[CLS]`]] hidden state → MLP head with 3-way output. The modern approach — sequence-level text-pair classification per [[FineTuningBert]].

## Applications

Information retrieval, open-domain question answering, redundancy elimination (identifying semantically-equivalent sentences), automated evaluation of summarization / paraphrase / machine translation.

## Connections

- [[NLP]] / [[TextClassification]] (text-pair variant).
- [[SNLI]] — the dataset.
- [[DecomposableAttention]] / [[BERT]] / [[FineTuningBert]] — the architectures.
- [[Attention]] / [[GloVe]] — feeding the decomposable model.
- [[SemanticTextualSimilarity]] — the closely-related text-pair *regression* task.
- [[d2l-nlp-applications]] §`natural-language-inference-*` — the three worked-example sections.
