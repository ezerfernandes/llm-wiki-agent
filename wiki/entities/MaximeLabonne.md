---
title: "Maxime Labonne"
type: entity
tags: [person, author, llm-engineering, fine-tuning]
sources: [leh-ch01-understanding-llm-twin-concept, leh-ch02-tooling-and-installation, leh-ch03-data-engineering, leh-ch04-rag-feature-pipeline, leh-ch05-supervised-fine-tuning, leh-ch06-preference-alignment, leh-ch07-evaluating-llms, leh-ch08-inference-optimization, leh-ch09-rag-inference-pipeline, leh-ch10-inference-pipeline-deployment, leh-ch11-mlops-and-llmops]
last_updated: 2026-05-22
---

## What it is
Maxime Labonne (Hugging Face handle `mlabonne`) is an LLM researcher/engineer, co-author of "LLM Engineer's Handbook" (Packt, 2024), and the publisher of the book's fine-tuned models and datasets on the Hugging Face Hub.

## In LLM Engineer's Handbook
Labonne is the fine-tuning lead in the book — chapters 5 ([[leh-ch05-supervised-fine-tuning]]) and 6 ([[leh-ch06-preference-alignment]]) center on his recipe for SFT and DPO using [[Unsloth]] and [[TRL]]. The artifacts `mlabonne/llmtwin`, `mlabonne/llmtwin-dpo`, `mlabonne/FineTome-Alpaca-100k`, `mlabonne/TwinLlama-3.1-8B`, and `mlabonne/TwinLlama-3.1-8B-DPO` are all hosted under his Hugging Face namespace; the Comet ML run is `comet.com/mlabonne/llm-twin-training`. He is also one of the two configured LLM Twin "users" whose Medium/Substack/LinkedIn writing seeds the crawl pipeline in Ch. 3 ([[leh-ch03-data-engineering]]).

## Connections
- [[PaulIusztin]] — co-author.
- [[AlexVesa]] — co-author.
- [[Packt]] — publisher.
- [[LLMEngineersHandbook]] — the book he co-authored.
- [[TwinLlama]] — the fine-tuned model artifact he hosts.
- [[HuggingFace]] — hub where his models live.
- [[Unsloth]] / [[TRL]] — fine-tuning stack he uses.
- [[CometML]] — experiment tracker for the TwinLlama runs.
