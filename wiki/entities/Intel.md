---
title: "Intel"
type: entity
tags: [company, semiconductor, hardware, open-source-data]
sources: [hands-on-llm-ch12-fine-tuning-generation-models]
last_updated: 2026-05-23
---

# Intel

**Intel Corporation** — the American semiconductor company best known for its x86 CPUs. In the wiki's LLM context, Intel also publishes open-source LLM datasets and tooling: notably the **Orca DPO pairs** dataset used in [[DistilabelIntelOrcaDPOPairs|argilla/distilabel-intel-orca-dpo-pairs]] and the **Intel Neural Compressor** / **Intel Extension for Transformers** quantization libraries.

## In Hands-On LLMs Ch 12

[[hands-on-llm-ch12-fine-tuning-generation-models|Ch 12]] uses Intel-authored preference data via the **`argilla/distilabel-intel-orca-dpo-pairs`** dataset — see [[DistilabelIntelOrcaDPOPairs]]. The dataset is Intel's Orca DPO pairs reprocessed by [[Argilla]] with `distilabel` quality scores.

## Connections

- [[Argilla]] — partner on the DPO pairs dataset.
- [[DistilabelIntelOrcaDPOPairs]] — the dataset used in Ch 12.
- [[hands-on-llm-ch12-fine-tuning-generation-models]] — primary source.
