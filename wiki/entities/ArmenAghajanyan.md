---
title: "Armen Aghajanyan"
type: entity
tags: [person, researcher, peft, fine-tuning, theory]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# Armen Aghajanyan

ML researcher cited in [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]] as first author of the **[[Aghajanyan2020IntrinsicDimension|"Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning"]]** paper (2020) — the theoretical underpinning of why [[PEFT|PEFT]] works at all.

## The contribution Ch 7 highlights

The paper showed empirically that:
- **LLMs have very low [[IntrinsicDimension|intrinsic dimensions]]** despite their large parameter counts.
- **Pre-training implicitly compresses intrinsic dimension** — the better-trained the LLM, the lower its intrinsic dimension.
- **Larger models tend to have *lower* intrinsic dimensions** after pre-training — counterintuitive but empirically robust.

These results jointly explain why a 175B-parameter model's behavior can be meaningfully modified by ~4.7M [[lora|LoRA]] parameters (~0.0027% of full): the effective parameter space the model lives on is much smaller than its raw parameter count.

## Affiliation

Has worked at [[meta|Meta AI]] (formerly FAIR). The intrinsic-dimension paper was at Facebook AI.

## Other notable work

- Co-author on [[lora|LoRA]] (Hu et al. 2021) — though not first author.
- Work on multitask learning, prompt-based methods, and model merging.

## Connections

- [[IntrinsicDimension]] — the concept his paper established.
- [[PEFT]] / [[lora|LoRA]] — the techniques his theory justifies.
- [[Aghajanyan2020IntrinsicDimension]] — the paper.
- [[ai-engineering-ch07-finetuning]] — wiki source.
