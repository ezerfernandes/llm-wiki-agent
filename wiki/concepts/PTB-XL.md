---
title: "PTB-XL"
type: concept
tags: [dataset, ecg, benchmark, physionet]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# PTB-XL

**Wagner, Strodthoff, Bousseljot, Kreiseler, Lunze, Samek & Schaeffter (Scientific Data, 2020) — *"Ptb-xl, a large publicly available electrocardiography dataset."*** **21,837 10s ECG signals from 18,885 patients**, each annotated with a free-text report and **SCP-Codes** (Standardized Communication Protocol) at three label tiers (Diagnostic / Form / Rhythm).

PTB-XL is the canonical zero-shot / retrieval evaluation set for ECG-language models because its English-translated reports differ in style from MIMIC training reports — the test of **generalization across report style**, not just record overlap.

In [[2408.08849-ecg-chat|ECG-Chat]]:
- Evaluation set for **zero-shot ECG-report retrieval** (Table I; 2K test split). Headline: CoCa+WDE achieves R@1 64.7 / 71.6 vs prior best 2.14.
- Evaluation set for **ECG classification** under three SCP-Code groupings (Disease 40 categories / Form / Rhythm).
- Reports translated to English-style via GPT-4o; ground-truth comparisons in Table II BLEU-1 row use those translations.

## Connections
- [[2408.08849-ecg-chat]] — primary evaluation set.
- [[ECG]] — modality.
- [[MIMIC-IV-ECG]] — paired training set in the same paper.
- [[CPSC2018]] — sibling evaluation set.
- [[F1Score]], [[bleu]] — primary evaluation metrics.
