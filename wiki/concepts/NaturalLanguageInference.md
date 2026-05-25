---
title: "Natural Language Inference"
type: concept
tags: [nlp, text-pair-classification, application]
sources: [d2l-nlp-applications, hands-on-llm-ch04-text-classification, hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
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

## From [[hands-on-llm-ch04-text-classification|*Hands-On LLMs* Ch 4]]

Ch 4 names NLI as **the prior dominant approach for [[ZeroShotClassification|zero-shot text classification]]** — and the alternative the chapter explicitly chose *not* to demonstrate:

> "If you are familiar with zero-shot classification with Transformer-based models, you might wonder why we choose to illustrate this with embeddings instead. Although **natural language inference models are amazing for zero-shot classification**, the example here demonstrates the flexibility of embeddings for a variety of tasks." — Ch 4

The trick: cast `(input_text, "This text is a positive review")` as an NLI (premise, hypothesis) pair, then assign the candidate label with the highest entailment probability. This is the recipe behind [[HuggingFace|Hugging Face]]'s `pipeline("zero-shot-classification")` default, which uses an NLI model under the hood. Ch 4 chose embedding-based zero-shot instead specifically to demonstrate **embeddings as a versatile primitive** across Language AI use cases, not because NLI-based zero-shot is inferior on accuracy.

## From [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]

Ch 10 codifies the **wiki's clearest statement of NLI-as-contrastive-data**: NLI's three-way labels map directly to contrastive-learning data — entailment → positive pair, contradiction → negative pair.

> *"When pretraining your embedding model, you will often see data being used from natural language inference (NLI) datasets. ... If you look closely at entailment and contradiction, then they describe the extent to which two inputs are similar to one another. As such, we can use NLI datasets to generate negative examples (contradictions) and positive examples (entailments) for contrastive learning."* — Ch 10

The chapter uses [[GLUE]]'s [[MNLI]] (Multi-Genre NLI) — 392,702 sentence pairs — as its training-data source, with three label-mappings for three losses:

- **[[SoftmaxLoss|Softmax loss]]** — keep all 3 NLI labels, train a 3-way classifier head.
- **[[CosineSimilarityLoss|Cosine loss]]** — relabel: entailment → 1.0; neutral / contradiction → 0.0.
- **[[MultipleNegativesRankingLoss|MNR loss]]** — filter to entailment-only (positives), shuffle the hypothesis column for soft negatives.

NLI is therefore **the canonical pretraining-data source for sentence-embedding contrastive learning** — both [[SNLI]] (single-genre) and [[MNLI]] (multi-genre) are used heavily; the original Sentence-BERT paper trained on the combination.
