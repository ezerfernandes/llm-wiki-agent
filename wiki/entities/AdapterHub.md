---
title: "AdapterHub"
type: entity
tags: [tool, peft, adapter, hub, community]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# AdapterHub

An open-source community **registry of pre-trained adapter modules** for transformer models. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], named alongside [[HuggingFace]] as a place where practitioners can find pre-built [[lora|LoRA]] / adapter modules:

> "There are publicly available finetuned LoRA adapters that you can use the way you'd use pre-trained models. You can find them on Hugging Face or initiatives like AdapterHub."

## What it offers

- Pre-trained adapters for many task / language combinations.
- Compatibility with [[HuggingFace]] transformers.
- A research-oriented framework for studying adapter-based transfer learning.
- Web interface for browsing adapters by task / language / base model.

## Position in the ecosystem

Where [[HuggingFace]] is the generalist hub for all model artifacts (full models, adapters, datasets, spaces), AdapterHub is specifically focused on **adapter modules**. The two ecosystems overlap heavily — many AdapterHub adapters are also indexed on HuggingFace.

## Connections

- [[adapterlayers|Adapter Layers]] / [[PEFT]] / [[lora|LoRA]] — the techniques whose outputs AdapterHub catalogs.
- [[HuggingFace]] — the broader artifact-hub neighbor.
- [[MultiLoraServing]] — the serving pattern that pre-built adapters enable.
- [[ai-engineering-ch07-finetuning]] — wiki source.
