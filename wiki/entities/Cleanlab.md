---
title: "Cleanlab"
type: entity
tags: [tool, data-centric-ml, evaluation, data-selection]
sources: [madewithml-mlops-evaluation, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Cleanlab

Data-centric ML library implementing confident learning for finding label errors and noisy data. Referenced in [[madewithml-mlops-evaluation]] alongside [[Snorkel]] for improving training-set quality.

## Connections

- [[DataPruning]] / [[DataSelection]] — [[mlsysbook-ch09-data-selection|Reddi Ch 9]] names Cleanlab as the canonical tool for **label-error detection** in quality-based static pruning: samples the model consistently predicts as class A but labeled class B are flagged as likely annotation mistakes and removed/corrected.
- [[StaticDataPruning]] — the optimization stage it serves.
- [[madewithml-mlops-evaluation]] / [[mlsysbook-ch09-data-selection]] — sources.
