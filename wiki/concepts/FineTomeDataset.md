---
title: "FineTome Dataset"
type: concept
tags: [llm-engineering]
sources: [leh-ch05-supervised-fine-tuning]
last_updated: 2026-05-22
---

## Definition
Quality-filtered version of arcee-ai/The-Tome curated with the fineweb-edu-classifier.

## In LLM Engineer's Handbook
`mlabonne/FineTome-Alpaca-100k` is a 100K-sample instruction dataset created by [[MaximeLabonne]] by filtering `arcee-ai/The-Tome` through the [[FinewebEduClassifier]]. Used in [[leh-ch05-supervised-fine-tuning]] as the upsampling source that gives the small `mlabonne/llmtwin` dataset (3,335 pairs) enough volume (10K rows added) to teach the Llama-3.1-8B base model the Alpaca chat template.
