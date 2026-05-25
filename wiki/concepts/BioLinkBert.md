---
title: "BioLinkBert"
type: concept
tags: [text-encoder, biomedical, pretraining]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# BioLinkBert

**Yasunaga, Leskovec & Liang (ACL 2022) — *"Linkbert: Pretraining language models with document links."*** A BERT variant pretrained to leverage **document-link structure** (citations and hyperlinks treated as document-pair supervision). The biomedical variant is pretrained on PubMed with article-citation links.

In [[2408.08849-ecg-chat|ECG-Chat]]: ablated as a text-encoder alternative. **Best retrieval R@1** (ECG→Report 72.7, Report→ECG 76.6) of the three encoders tested, but slightly weaker classification F1 than [[MedCPT|Med-CPT]] on both PTB-XL (52.7 vs 52.8) and CPSC2018 (78.3 vs 80.1). ECG-Chat ships with Med-CPT for classification; BioLinkBert would be the choice for retrieval-first deployments.

## Connections
- [[2408.08849-ecg-chat]] — ablation study.
- [[MedCPT]] — the production encoder choice (wins on classification).
- [[BioClinicalBert]] — sibling ablation alternative.
