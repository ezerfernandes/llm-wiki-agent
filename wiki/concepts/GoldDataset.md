---
title: "Gold Dataset"
type: concept
tags: [data-quality, labeling, training-data, augmented-sbert]
sources: [hands-on-llm-ch10-creating-text-embedding-models]
last_updated: 2026-05-23
---

# Gold Dataset

A **gold dataset** is a **small but fully annotated dataset that holds the ground truth** — every label has been manually verified or comes from a trusted source. The high-quality reference data against which model outputs are compared during training and evaluation.

Per [[hands-on-llm-ch10-creating-text-embedding-models|*Hands-On LLMs* Ch 10]]: *"A gold dataset is a small but fully annotated dataset that holds the ground truth."*

## In [[AugmentedSBERT]]

Ch 10 introduces the gold/silver distinction in the context of [[AugmentedSBERT]] — a procedure for fine-tuning sentence embeddings when only a little labeled data is available:

1. **Gold dataset** = the small set of fully-annotated labeled pairs (Ch 10's worked example uses 10,000 [[MNLI]] entailment pairs with the entailment/neutral/contradiction → 1/0/0 mapping).
2. Train a [[CrossEncoder|cross-encoder]] on the gold dataset.
3. Use the trained cross-encoder to label a much larger pool of unlabeled pairs → **[[SilverDataset|silver dataset]]**.
4. Train the [[BiEncoder|bi-encoder]] on gold + silver.

## The taxonomy as a general data-quality concept

The gold/silver distinction generalizes beyond Augmented SBERT to **any pipeline that combines small high-quality data with larger model-labeled data**:

- **Gold** — manually labeled, expensive, small. The trusted source of truth.
- **Silver** — model-labeled, cheap, large. Not ground truth but typically of acceptable quality if the labeler is well-trained.

This taxonomy lets you talk about hybrid datasets quantitatively — *"the silver:gold ratio,"* *"the silver-labels-quality-against-gold-test-set metric,"* etc.

## Connections

- [[SilverDataset]] — the complement.
- [[AugmentedSBERT]] — the Ch 10 technique that introduces the gold/silver distinction.
- [[DataAnnotation]] / [[DataQuality]] — the broader data-engineering family.
- [[CrossEncoder]] — the model that labels the silver dataset from the gold dataset.
- [[hands-on-llm-ch10-creating-text-embedding-models]] — primary source.
