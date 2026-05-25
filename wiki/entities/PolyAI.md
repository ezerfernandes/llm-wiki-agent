---
title: "PolyAI"
type: entity
tags: [company, dataset-publisher, conversational-ai, banking77]
sources: [dspy-optimizers, dspy-tutorial-classification-finetuning]
last_updated: 2026-05-24
---

# PolyAI

**PolyAI** is a UK-based conversational-AI company whose open-data contribution to the wiki's corpus is the **[[Banking77]]** dataset — the canonical 77-way fine-grained intent-classification benchmark used in two independent wiki `dspy.BootstrapFinetune` receipts.

PolyAI's hosted-on-Hugging-Face dataset identifier is `PolyAI/banking77`. The dataset is referenced in [[dspy-optimizers|page 13 of the DSPy *Learn* corpus]] (the page that introduces `BootstrapFinetune` end-to-end) and is the central dataset of the [[dspy-tutorial-classification-finetuning|Classification Fine-tuning tutorial]].

## Wiki Presence

- [[Banking77]] — the 77-way intent-classification dataset; the only PolyAI artifact in active wiki use.
- [[dspy-optimizers]] — uses Banking77 as the worked example for the only weight-tuning optimizer in the DSPy catalog.
- [[dspy-tutorial-classification-finetuning]] — the wiki's first end-to-end runnable `BootstrapFinetune` receipt; uses Banking77 to demonstrate cross-model open-weights distillation.

## Connections

- [[Banking77]] — the dataset.
- [[HuggingFace]] — the hosting platform.
- [[Classification]] / [[IntentClassifier]] — the task family Banking77 belongs to.
- [[BootstrapFinetune]] — the DSPy optimizer with two worked Banking77 receipts in the wiki.
