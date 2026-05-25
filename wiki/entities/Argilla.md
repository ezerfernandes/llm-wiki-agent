---
title: "Argilla"
type: entity
tags: [company, open-source, data-curation, distilabel, hugging-face]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# Argilla

**Argilla** is an open-source data-curation and AI-feedback company best known for its NLP data-labeling platform and the **`distilabel`** library — a framework for synthesizing preference data and other LLM-as-judge training signals at scale. Acquired by [[HuggingFace|Hugging Face]] in 2024.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses Argilla's **`argilla/distilabel-intel-orca-dpo-pairs`** dataset as the preference-data source for the worked DPO recipe — see [[DistilabelIntelOrcaDPOPairs]] for the full schema and filtering. The dataset combines Intel's original Orca DPO pairs with Argilla's `distilabel`-generated quality scores, yielding ~13,000 (prompt, chosen, rejected) triples ready for [[DPOTrainer]].

## Connections

- [[HuggingFace|Hugging Face]] — acquired Argilla in 2024 and hosts the datasets.
- [[Distilabel]] — Argilla's AI-feedback library.
- [[Intel]] — partner on the Orca DPO dataset.
- [[DistilabelIntelOrcaDPOPairs]] — Ch 12's worked DPO dataset.
- [[DPO]] / [[PreferenceData]] — the techniques and data category Argilla's tooling supports.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
