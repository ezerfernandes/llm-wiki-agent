---
title: "Sebastian Raschka"
type: entity
tags: [person, educator, practitioner, llm, finetuning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Sebastian Raschka

ML educator, practitioner, and author best known for his books (*Python Machine Learning*, *Machine Learning with PyTorch and Scikit-Learn*, *Build a Large Language Model (From Scratch)*) and his prolific writing on LLM finetuning practice via his *Ahead of AI* newsletter.

Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], cited as the **practitioner data point that contradicts the "small rank is enough" consensus on [[lora|LoRA]]**:

> "Raschka (2023) found that r = 256 achieved the best performance on his tasks."

This is in contrast to the LoRA paper authors and [[Databricks]] (Sooriyarachchi 2023), who report rank ∈ [4, 64] is typically sufficient and higher r doesn't help. The Raschka data point is Ch 7's signal that **LoRA hyperparameter tuning is empirical, not theory-determined**.

## Why his voice is weighted in the chapter

Raschka writes detailed empirical posts on LoRA hyperparameter ablations, finetuning recipes, and practitioner-level diagnostics — material that's harder to find in formal papers. [[ChipHuyen|Huyen]] cites him as a representative practitioner-blogger whose experiments inform community defaults.

## Affiliation

Has been associated with [[Lightning|Lightning AI]] (the company behind PyTorch Lightning / [[LitGPT]]). Previously academic at the University of Wisconsin-Madison.

## Connections

- [[lora|LoRA]] — his empirical contributions to community practice.
- [[LitGPT]] — affiliated framework.
- [[FineTuning]] — his primary writing area.
- [[ai-engineering-ch07-finetuning]] — wiki source.
