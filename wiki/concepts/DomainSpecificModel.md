---
title: "Domain-Specific Model"
type: concept
tags: [foundation-models, domain-adaptation, specialization]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Domain-Specific Model

A foundation model trained on **highly specialized data** to perform on tasks unlikely to appear in publicly available internet data. Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], general-purpose models like [[gemini|Gemini]], [[GPT4|GPT-4]], and Llama excel at many domains but typically underperform on domain-specific tasks they never saw during training.

## When you need one

Ch 2's canonical examples of where general-purpose FMs fall short:
- **Drug discovery** — protein, DNA, RNA sequences are expensive to acquire and follow specific formats unlikely to appear on the public internet.
- **Cancer screening** — X-ray and fMRI scans are hard to obtain because of patient privacy.
- **Architectural sketches** — a domain-tuned model could beat [[StableDiffusion|Stable Diffusion]] for architects.
- **Manufacturing factory plans** — a domain-tuned model could outperform [[ChatGPT|ChatGPT]].

## Canonical biomedicine examples

- **[[AlphaFold|AlphaFold]]** ([[googledeepmind|DeepMind]]) — trained on the sequences + 3D structures of ≈100,000 known proteins.
- **[[BioNeMo|BioNeMo]]** ([[NVIDIA]]) — biomolecular data for drug discovery.
- **[[MedPaLM2|Med-PaLM2]]** ([[google|Google]]) — combined LLM + medical data for medical QA.

## How they're built

Two paths per Ch 2:
1. **Train from scratch** on domain-specific data — used for the most specialized cases (AlphaFold).
2. **Finetune on top of a general-purpose model** — more common, cheaper, often sufficient.

The chapter footnotes that as of writing, the bulk of activity is in biomedicine — but other fields (architecture, manufacturing) are open opportunities.

## Trade-off

> "Training on more data often requires more compute resources and doesn't always lead to better performance. For example, a model trained with a smaller amount of high-quality data might outperform a model trained with a large amount of low-quality data." — Ch 2

Gunasekar et al. (2023) trained a **1.3B-param model on 7B tokens of high-quality coding data** that outperformed much larger general-purpose models on coding benchmarks.

## Connections
- [[FoundationModel]] — parent category.
- [[FineTuning]] — the common construction approach.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[AlphaFold]] / [[BioNeMo]] / [[MedPaLM2]] — biomedical exemplars.
- [[DatasetEngineering]] — what produces the domain dataset.
