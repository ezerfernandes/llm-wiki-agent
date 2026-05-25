---
title: "Waveform Data Enhancement (WDE)"
type: concept
tags: [contrastive-learning, ecg, data-augmentation, ecg-chat]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Waveform Data Enhancement (WDE)

A text-side data-augmentation technique from [[2408.08849-ecg-chat|ECG-Chat]] (Zhao et al. 2025) for contrastive ECG-text pretraining. Most open ECG datasets ([[MIMIC-IV-ECG]], [[ChampanShaoxingNingbo|CSN]], [[ShandongProvincialHospital|SPH]], [[PTB-XL]], [[CPSC2018]]) have a **highly templated report space** — the same boilerplate diagnostic sentence (*"sinus rhythm; no abnormality"*) is attached to many physiologically distinct records. This collapses the contrastive signal: a CLIP/[[CoCa]]-style dual encoder cannot separate samples whose text labels are identical even though the underlying ECG signals differ.

**The WDE recipe.** For each ECG record, extract lead-II waveform morphology via [[NeuroKit2]] — **RR interval, PR interval, QRS complex duration, QT/QTc interval, and the P/R/T wave peaks** — and **append these numeric features to the text report** before contrastive training. *"This approach artificially increases the distinction between samples, even when reports are identical, helping prevent contrastive loss from failing to converge during small-batch training."*

## Empirical effect (Table I, [[2408.08849-ecg-chat|ECG-Chat]])

Zero-shot retrieval on [[PTB-XL]] (2K test set), CoCa architecture, **same** ECG encoder + same text encoder, the only delta is WDE on the text side:

| | ECG→Report R@1 | R@5 | R@10 | Report→ECG R@1 | R@5 | R@10 |
|---|---|---|---|---|---|---|
| CoCa (no WDE) | 2.14 | 6.65 | 9.60 | 2.37 | 6.10 | 10.2 |
| **CoCa + WDE** | **64.7** | **84.7** | **89.4** | **71.6** | **89.0** | **93.0** |

A **30× lift on R@1** from a single text-side augmentation. The paper notes this is also what makes downstream classification work — small-batch contrastive training without WDE simply fails to converge.

## Connections
- [[2408.08849-ecg-chat]] — the paper proposing and ablating WDE.
- [[CoCa]] — the architecture WDE rescues from collapse on repetitive medical text corpora.
- [[NeuroKit2]] — the Python toolbox extracting the waveform features.
- [[ECG]] — the modality.
- [[ContrastiveLearning]] — the parent training paradigm.

## What's still owed
- Whether WDE generalizes to other physiological signals (EEG, EMG, PPG) with similarly templated report spaces — paper does not test beyond ECG.
- Whether a sufficiently large dataset (the 805K-record SPH/CSN/MIMIC mix is large by clinical standards but small by general-MLLM standards) would obsolete the trick — Table VI shows the data-scaling curve is steep but does not isolate WDE's contribution at the data ceiling.
