---
title: "ECG-Instruct"
type: concept
tags: [dataset, instruction-tuning, ecg, gpt4o, ecg-chat]
sources: [2408.08849-ecg-chat]
last_updated: 2026-05-22
---

# ECG-Instruct

The instruction-tuning dataset released by [[2408.08849-ecg-chat|ECG-Chat]] (Zhao et al. 2025). **45,044 ECG samples / 325,730 sentences / 3,294,880-word vocabulary / 6,319 distinct vocabularies** — the first open ECG instruction-tuning corpus.

## Two subsets

| Subset | Size | Format | Caption length | Per-sample sentences |
|---|---|---|---|---|
| **ECG-Instruct-Diagnosis** | 20,258 | single-turn QA | avg 66.77 words | avg 4.10 |
| **ECG-Instruct-Conversations** | 24,786 | multi-turn (4–30 rounds) | avg 78.36 words/conv | avg 9.79 |

## Construction

Built by giving GPT-4o:
- The [[MIMIC-IV-ECG]] free-text report (gold reference).
- [[NeuroKit2]]-extracted lead-II waveform features (RR / PR / QRS / QT / P/R/T peaks).
- A randomly-selected ECG-interpretation question (e.g. *"Is there anything abnormal in this ECG?"*).
- A **negative-example regime**: random diagnostic/waveform features *not present* in the original report are injected, and GPT-4o is told to answer accurately (refuting the false features). Generates *"negative answers"* that teach the model to disagree with wrong premises.

Reports are reformatted as multi-turn dialogues using the template *"Your ECG shows {Report 1}; {Report 2}; .... It's a normal/abnormal/borderline ECG."*

## Connections
- [[2408.08849-ecg-chat]] — paper releasing the dataset.
- [[MIMIC-IV-ECG]] — the source ECG corpus.
- [[NeuroKit2]] — the waveform-feature extractor.
- [[ECGExpertQA]] — the evaluation knowledge-base counterpart (123 expert-curated pairs).
- [[ECG]] — the modality.

## What's still owed
- Real-world clinical validation — paper explicitly flags that *"the dataset for instruction tuning is small and does not come from real world, which leads to bias and hallucinations in LLMs."* The GPT-4o-generated nature of the corpus inherits any biases of the synthetic-data pipeline.
