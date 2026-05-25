---
title: "Salesforce"
type: entity
tags: [organization, company, research-lab, multimodal]
sources: [hands-on-llm-ch09-multimodal-llms]
last_updated: 2026-05-23
---

# Salesforce

American enterprise-software company; its research arm (Salesforce Research) authored the [[BLIP2|BLIP-2]] vision-language model and published it on Hugging Face under the `Salesforce/` namespace. Cited in [[hands-on-llm-ch09-multimodal-llms|*Hands-On LLMs* Ch 9]] via the worked checkpoint `Salesforce/blip2-opt-2.7b`.

## In Ch 9

The chapter's runnable [[VisualQuestionAnswering|VQA]] / [[ImageCaptioning|captioning]] examples load `Salesforce/blip2-opt-2.7b` via `transformers.Blip2ForConditionalGeneration` + `AutoProcessor` — the canonical pedagogical entry point into adapter-style [[MultimodalLLM|multimodal LLMs]].

## Connections

- [[hands-on-llm-ch09-multimodal-llms]] — primary source.
- [[BLIP2]] — author of this model family.
- [[HuggingFace]] — distribution host for the checkpoint.
- [[MultimodalLLM]] — the architectural family Salesforce Research's BLIP-2 anchors.
