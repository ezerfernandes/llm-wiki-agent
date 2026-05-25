---
title: "BioClinicalBert"
type: concept
tags: [text-encoder, biomedical, clinical]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# BioClinicalBert

**Alsentzer, Murphy, Boag, Weng, Jin, Naumann & McDermott (2019) — *"Publicly available clinical BERT embeddings."*** A BERT variant pretrained on MIMIC-III clinical notes on top of BioBERT, designed specifically for **clinical-note text**.

In [[2408.08849-ecg-chat|ECG-Chat]]: ablated as a text-encoder alternative. Sits between [[BioLinkBert]] (retrieval-leading) and [[MedCPT|Med-CPT]] (classification-leading) — R@1 69.9 / 71.2, F1 52.4 / 78.8.

## Connections
- [[2408.08849-ecg-chat]] — ablation study.
- [[MedCPT]] — production encoder choice.
- [[BioLinkBert]] — sibling ablation alternative.
- [[MIMIC]] — original pretraining corpus.
