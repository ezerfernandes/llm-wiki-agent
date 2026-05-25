---
title: "Model License"
type: concept
tags: [license, open-source, model-selection]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Model License

The **legal terms** attached to a model release. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Open source models made the licensing situation worse. Many models are released under their own unique licenses."

## The license landscape

| License | Notable models |
|---|---|
| **MIT** | classic permissive |
| **Apache 2.0** | Gemma, Mistral-7B |
| **GPL** | classic copyleft |
| **BSD** | classic permissive |
| **Creative Commons** | datasets often |
| **Llama 2 Community License** | Llama 2 |
| **Llama 3 Community License** | Llama 3 |
| **BigCode Open RAIL-M v1** | StarCoder family |

## Three questions to ask any model license (Ch 4)

1. **Does the license allow commercial use?** The first Llama model was originally non-commercial.
2. **Any commercial-use restrictions?** Llama 2/3 require *"a special license from Meta"* for applications with **>700M monthly active users**.
3. **Can you use the model's outputs to train other models?** This affects [[knowledgedistillation|distillation]] and [[DataSynthesis|synthetic-data]] use cases. *"Mistral didn't allow this originally but later changed its license. As of this writing, the Llama licenses still don't allow it."*

## Indirect contamination via outputs

A model X trained on outputs from a model Y can inherit Y's license restrictions even if X's own license seems permissive. Ch 4 footnote:

> "Consider model X that is trained on ChatGPT's outputs. X might have a license that allows this, but if ChatGPT doesn't, then X violated ChatGPT's terms of use, and therefore, X can't be used. This is why knowing a model's data lineage is so important."

## "Restricted weight"

Some people call models with restrictive licenses *"restricted weight."* Huyen finds this ambiguous since *"all sensible licenses have restrictions (e.g., you shouldn't be able to use the model to commit genocide)."*

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[LlamaLicense]] — the most-discussed specific license.
- [[OpenWeight]] / [[OpenSourceModel]] / [[OpenModel]] — the category structure licenses constrain.
- [[ModelBuildVsBuy]] — the decision framing where licenses act as filters.
- [[knowledgedistillation|Knowledge Distillation]] — the use case licenses sometimes block.
