---
title: "LIMA"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

## Definition
Zhou et al. 2023 paper showing ~1,000 high-quality samples can fine-tune a 70B-class model effectively.

## In LLM Engineer's Handbook
Chunting Zhou et al. (2023, *LIMA: Less Is More for Alignment*, arXiv:2305.11206) demonstrates that ~1,000 carefully curated instruction-answer pairs can fine-tune a 70B-class base model into a useful assistant — competitive with finetunes trained on hundreds of thousands of samples. Cited in [[leh-ch05-supervised-fine-tuning]] as the canonical evidence that data quality dominates quantity at large model scale.

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

[[ChipHuyen|Huyen]] in Ch 8 adds the **headline experimental result**:

> "LIMA: Less Is More for Alignment (Zhou et al., 2023) shows that a 65B-parameter Llama model, finetuned with 1,000 carefully curated prompts and responses, can produce answers that are either equivalent or strictly preferred to GPT-4 in **43% of cases**, as judged by human annotators."

### The Ch 8 caveat

> "However, the downside of having too few data examples is that LIMA is not as robust as product-grade models."

So LIMA proves the *quality-can-beat-quantity* point — but doesn't undermine the case for larger datasets in production settings where robustness matters.

### Also from Ch 8 — the 7B-parameter diversity experiment

Zhou et al. ran an additional experiment with three 2,000-example datasets:

| Dataset | Result |
|---|---|
| High-quality only | weaker |
| Diverse only | weaker |
| **High-quality + diverse** | **winner** |

This is the chapter's evidence that **quality and [[DataDiversity|diversity]] are independent and both necessary** — neither alone suffices.
