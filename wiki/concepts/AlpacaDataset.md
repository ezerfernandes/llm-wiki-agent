---
title: "Alpaca (Dataset)"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

## Definition
Stanford CRFM's seed-prompt-evolved instruction dataset (Tahori et al. 2023).

## In LLM Engineer's Handbook
Stanford CRFM's 52K-sample instruction dataset (Tahori, Gulrajani, Zhang, Dubois et al., March 2023), built by self-instruct-style synthesis from 175 human-written seed prompts using `text-davinci-003`. Gives its name to both the [[AlpacaFormat|Alpaca data format]] and the Alpaca chat template. [[leh-ch05-supervised-fine-tuning]] Table 5.3 shows five canonical Alpaca seed prompts.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

[[ChipHuyen|Huyen]] frames Alpaca as the **canonical [[knowledgedistillation|distillation]] case study + [[SelfInstruct|Self-Instruct]] descendant**:

### The construction pipeline

1. Start with **175 (instruction, response) seed examples** from the [[SelfInstruct|Self-Instruct seed dataset]] (Wang et al. 2022), originally written to cover diverse uses.
2. Use GPT-3 `text-davinci-003` to generate 52,000 (instruction, response) pairs mirroring the seeds.
3. Finetune Llama-7B on the resulting dataset.

### The distillation framing

> "The resulting model, Alpaca, behaves similarly to text-davinci-003, while being **4% the size of the teacher model**."

Alpaca is one of Ch 8's three canonical examples of [[knowledgedistillation|distillation]] (alongside [[DistilBERT]] and [[BuzzFeed]]'s Flan-T5 + LoRA case).

### Connection to [[InstructionDataSynthesis]]

Alpaca's pipeline is the **archetypal AI-generated instruction-tuning dataset** — every subsequent synthetic instruction dataset ([[UltraChat]], [[EvolInstruct]], [[Cosmopedia]]) builds on the seed-expand-finetune recipe Alpaca made famous.
