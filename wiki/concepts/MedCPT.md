---
title: "Med-CPT"
type: concept
tags: [text-encoder, biomedical, contrastive, pubmed]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Med-CPT

**Jin, Kim, Chen, Comeau, Yeganova, Wilbur & Lu (Bioinformatics, 2023) — *"Medcpt: Contrastive pre-trained transformers with large-scale pubmed search logs for zero-shot biomedical information retrieval."*** A biomedical text encoder pretrained via contrastive learning on **PubMed search logs**. Embedding dim 512.

In [[2408.08849-ecg-chat|ECG-Chat]]: the **text encoder side of the [[CoCa]]-style dual-loss pretraining**, with only the last 2 layers fine-tuned. The 6-layer transformer decoder for the captioning loss is also at hidden dim 512.

**Encoder ablation** (Table V, ECG-Chat):

| Text encoder | Retrieval R@1 (ECG→Report) | (Report→ECG) | PTB-XL F1 | CPSC2018 F1 |
|---|---|---|---|---|
| [[BioLinkBert]] | **72.7** | **76.6** | 52.7 | 78.3 |
| [[BioClinicalBert]] | 69.9 | 71.2 | 52.4 | 78.8 |
| **Med-CPT** | 64.7 | 71.6 | **52.8** | **80.1** |

BioLinkBert wins retrieval (better reconstruction); **Med-CPT wins classification (better discrimination)** — ECG-Chat ships with Med-CPT given the clinical-deployment focus on classification.

## Connections
- [[2408.08849-ecg-chat]] — primary user; production text encoder choice.
- [[BioLinkBert]], [[BioClinicalBert]] — ablated alternatives.
- [[CoCa]] — the dual-loss architecture Med-CPT slots into as the text side.
- [[ContrastiveLearning]] — Med-CPT's pretraining paradigm and ECG-Chat's downstream paradigm.
