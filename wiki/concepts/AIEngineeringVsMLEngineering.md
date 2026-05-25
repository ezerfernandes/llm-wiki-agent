---
title: "AI Engineering vs. ML Engineering"
type: concept
tags: [ai-engineering, ml-engineering, comparison]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# AI Engineering vs. ML Engineering

The comparison taxonomy defined in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]] for distinguishing **[[AIEngineering|AI engineering]]** (building on foundation models) from **[[MLOps|ML engineering]]** (building models from scratch). Huyen's bottom line:

> *"If traditional ML engineering involves developing ML models, AI engineering leverages existing ones."*

## Three high-level differences

1. **You use someone else's model.** With FMs, you adapt a model someone else has trained. The focus shifts from modeling/training to **[[ModelAdaptation|adaptation]]**.
2. **Models are bigger.** More compute, higher latency, more GPU pressure. *"As the head of AI at a Fortune 500 company told me: his team knows how to work with 10 GPUs, but they don't know how to work with 1,000 GPUs."*
3. **Outputs are open-ended.** Open-endedness makes [[Evaluation|evaluation]] much harder — there's no enumerable list of ground truths.

## Model-development layer comparison

| Category | Traditional ML | Foundation models |
|---|---|---|
| **[[ModelingAndTraining|Modeling and training]]** | ML knowledge required for training a model from scratch | ML knowledge is nice-to-have, not must-have |
| **[[DatasetEngineering|Dataset engineering]]** | More about **feature engineering**, esp. tabular data | Less about feature engineering — more about deduplication, tokenization, context retrieval, quality control |
| **[[InferenceOptimization|Inference optimization]]** | Important | **Even more important** (open-ended autoregressive generation amplifies latency/cost) |

## Application-development layer comparison

| Category | Traditional ML | Foundation models |
|---|---|---|
| **[[AIInterface|AI interface]]** | Less important (apps had AI embedded — recommender systems, fraud detection) | Important (standalone, plug-ins, extensions, chat, voice, embodied) |
| **[[PromptEngineering|Prompt engineering]]** | Not applicable | Important |
| **[[Evaluation|Evaluation]]** | Important | **More important** |

## The workflow inversion

> *"With traditional ML engineering, you usually start with gathering data and training a model. Building the product comes last. However, with AI models readily available today, it's possible to start with building the product first, and only invest in data and models once the product shows promise."*

This is captured by Shawn Wang's "The Rise of the AI Engineer" workflow diagram (Ch 1 reproduces it).

## AI engineering ≈ full-stack engineering

Quoted in Ch 1: *"AI engineering is just software engineering with AI models thrown in the stack."* — Anton Bacaj. Python remains dominant for ML, but JavaScript tooling is growing (LangChain.js, Transformers.js, OpenAI Node library, [Vercel AI SDK](https://sdk.vercel.ai/)). Full-stack engineers' iteration speed is a real advantage over traditional ML engineers in the FM-application era.

## ML knowledge: still useful

Huyen acknowledges that *many people would dispute the "ML knowledge is nice-to-have" claim.* Her position: foundation models have removed the **prerequisite** to building applications, but ML knowledge still expands the tool set and helps with debugging when things break.

## Connections

- [[AIEngineering]] — the discipline.
- [[AIEngineeringStack]] — the architecture.
- [[ModelAdaptation]] — the central activity that distinguishes AI engineering.
- [[MLOps]] — predecessor discipline.
- [[Evaluation]] / [[InferenceOptimization]] / [[DatasetEngineering]] — the layers where the shift is most visible.
- [[ai-engineering-ch01-intro]] — primary source.
