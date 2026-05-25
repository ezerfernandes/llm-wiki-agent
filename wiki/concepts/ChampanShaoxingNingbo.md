---
title: "Champan-Shaoxing-Ningbo (CSN)"
type: concept
tags: [dataset, ecg, china, physionet]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# Champan-Shaoxing-Ningbo (CSN)

**Zheng, Greenbaum, Yacoub, El-Askary, Chang, Ehwerhemuepha, Abudayyeh, Barrett et al. (2020 / PhysioNet 2022).** A 12-lead ECG database from three Chinese hospitals (Champan, Shaoxing, Ningbo); **45,152 records sampled at 500 Hz for 10 s**, each annotated with **SNOMED CT codes**.

In [[2408.08849-ecg-chat|ECG-Chat]]:
- Each SNOMED CT code is converted into a corresponding textual description and merged into a report for the record.
- **40,637 training samples** contributed to the 805K-record contrastive-pretraining mix.

## Connections
- [[2408.08849-ecg-chat]] — primary user.
- [[ECG]] — modality.
- [[MIMIC-IV-ECG]], [[ShandongProvincialHospital]] — the other two corpora composing the ECG-Chat training mix.
