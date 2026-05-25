---
title: "Reference Data"
type: concept
tags: [evaluation, data, ground-truth]
sources: [ai-engineering-ch03-evaluation-methodology]
last_updated: 2024-12-04
---

# Reference Data

The **ground-truth data** that [[ReferenceBasedMetric|reference-based metrics]] compare generated outputs against. Per [[ai-engineering-ch03-evaluation-methodology|*AI Engineering* Ch 3]]:

> "Each example in the reference data follows the format (input, reference responses). An input can have multiple reference responses, such as multiple possible English translations of a French sentence. Reference responses are also called **ground truths** or **canonical responses**."

## Generation

Two sources:
- **Human-generated** — the gold standard. *"Using human-generated data as the reference means that we treat human performance as the gold standard, and AI's performance is measured against human performance."* Expensive and slow.
- **AI-generated** — increasingly common. *"AI-generated data might still need human reviews, but the labor needed to review it is much less than the labor needed to generate reference data from scratch."*

## Limitations Ch 3 flags

- **Coverage gaps** — Adept's [[Fuyu]] was unfairly penalized on image captioning because reference captions didn't include all correct possibilities.
- **Reference errors** — [[WMT2023]] organizers found *"many bad reference translations in their data."* Bad references mean reference-based metrics can be *worse* than reference-free metrics at correlating with human judgment (Freitag et al. 2023).
- **Bottleneck on iteration speed** — *"this evaluation approach requires reference data, it's bottlenecked by how much and how fast reference data can be generated."*

## Connections

- [[ai-engineering-ch03-evaluation-methodology]] — primary source.
- [[ReferenceBasedMetric]] / [[ReferenceFreeMetric]] — the taxonomy reference data sits within.
- [[SimilarityMeasurement]] — the evaluation family that depends on reference data.
- [[bleu|BLEU]] / [[ROUGE]] / [[BERTScore]] — reference-based metrics that consume it.
- [[ExactMatch]] / [[LexicalSimilarity]] / [[SemanticSimilarity]] — what's done with it.
- [[ComparisonData]] — analogous data structure for preference finetuning.
