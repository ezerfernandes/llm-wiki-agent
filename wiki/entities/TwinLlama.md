---
title: "TwinLlama"
type: entity
tags: [model, fine-tuned-llm, hugging-face, llama]
sources: [leh-ch02-tooling-and-installation, leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment, leh-ch07-evaluating-llms, leh-ch10-inference-pipeline-deployment]
last_updated: 2026-05-22
---

## What it is
TwinLlama is the family of fine-tuned LLMs produced by the LLM Engineer's Handbook running project. The base is `meta-llama/Meta-Llama-3.1-8B`; the publicly hosted checkpoints (under [[MaximeLabonne|mlabonne]]'s Hugging Face namespace) are `mlabonne/TwinLlama-3.1-8B` (SFT) and `mlabonne/TwinLlama-3.1-8B-DPO` (preference-aligned), with `mlabonne/TwinLlama-3.1-8B-13` deployed in Ch. 10.

## In LLM Engineer's Handbook
TwinLlama is the model the book teaches the reader to build. Ch. 2 ([[leh-ch02-tooling-and-installation]]) introduces it as the artifact hosted on the Hugging Face Hub (the chosen model registry). Ch. 5 ([[leh-ch05-supervised-fine-tuning]]) fine-tunes it from Llama 3.1 8B using [[Unsloth]] + [[TRL]] on `mlabonne/llmtwin` (3,335 pairs) concatenated with `mlabonne/FineTome-Alpaca-100k`, with LoRA `r=32, lora_alpha=32, lora_dropout=0` on all major modules — 50 minutes on an A100. Ch. 6 ([[leh-ch06-preference-alignment]]) DPO-aligns the SFT model on `mlabonne/llmtwin-dpo` (1,467 filtered triples) at `beta=0.5, lr=2e-6` to produce the DPO variant. Ch. 7 ([[leh-ch07-evaluating-llms]]) benchmarks TwinLlama (Accuracy 2.45 / Style 2.04) and TwinLlama-DPO (2.46 / 2.12) against `Meta-Llama-3.1-8B-Instruct` (2.62 / 1.86) using GPT-4o-mini as judge on a 334-prompt test set. Ch. 10 ([[leh-ch10-inference-pipeline-deployment]]) deploys `mlabonne/TwinLlama-3.1-8B-13` to a SageMaker endpoint via the Hugging Face DLC + TGI.

## Connections
- [[MaximeLabonne]] — owns the Hugging Face namespace hosting TwinLlama.
- [[Llama3_8BInstruct]] — adjacent base-family page (TwinLlama derives from Llama 3.1 8B).
- [[meta]] — Llama publisher.
- [[Unsloth]] / [[TRL]] — fine-tuning stack used.
- [[HuggingFace]] — model registry hosting TwinLlama.
- [[lora]] / [[QLoRA]] / [[DPO]] — adapter and alignment techniques applied.
- [[LLMTwin]] — the broader running project TwinLlama instantiates.
- [[CometML]] — experiment tracker recording the training runs.
