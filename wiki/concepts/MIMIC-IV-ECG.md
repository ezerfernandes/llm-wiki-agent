---
title: "MIMIC-IV-ECG"
type: concept
tags: [dataset, ecg, mimic, physionet]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# MIMIC-IV-ECG

**Gow, Pollard, Nathanson, Johnson, Moody, Fernandes, Greenbaum, Waks, Eslami, Carbonati, Chaudhari, Erbst, Moukheiber, Berkowitz, Mark, Steven (PhysioNet 2023) — *"Mimic-iv-ecg: Diagnostic electrocardiogram matched subset (version 1.0)."*** A subset of the [[MIMIC]]-IV critical-care database that pairs **800,035 12-lead ECG records across ~160,000 unique patients** with diagnostic free-text reports.

Each recording is sampled at **500 Hz for 10 s**. Reports are machine-generated; one ECG can correspond to multiple text reports.

In [[2408.08849-ecg-chat|ECG-Chat]] the dataset is the primary training source — **788,822 samples after pre-processing** (NaN/inf → 0; remove samples whose final report is empty or whose report content is unrelated to diagnosis). It is also the source corpus for the GPT-4o-generated [[ECGInstruct|ECG-Instruct]] instruction-tuning dataset.

## Connections
- [[MIMIC]] / [[MIMICIV]] — the parent EHR family.
- [[2408.08849-ecg-chat]] — primary user; 788,822 training samples after cleaning.
- [[ECGInstruct]] — derived instruction-tuning dataset.
- [[PTB-XL]], [[CPSC2018]], [[ChampanShaoxingNingbo]], [[ShandongProvincialHospital]] — other open ECG corpora used together in ECG-Chat's training mix.
- [[ECG]] — modality.
