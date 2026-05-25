---
title: "FineWeb-Edu Classifier"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Hugging Face encoder-only quality classifier that scores text for educational value.

## In LLM Engineer's Handbook
Encoder-only quality classifier published by [[HuggingFaceFW]] as `HuggingFaceFW/fineweb-edu-classifier`. Architecture: classification head bolted onto `Snowflake/snowflake-arctic-embed-m`, trained for 20 epochs on 450,000 samples annotated by Llama 3 70B Instruct (knowledge distillation). Per [[leh-ch05-supervised-fine-tuning]] it is the canonical encoder-only quality filter that scales (millions of samples) where heavyweight [[LLMAsAJudge]] does not. [[MaximeLabonne]] uses it to filter `arcee-ai/The-Tome` into [[FineTomeDataset]].
