---
title: "AI Engineering Stack"
type: concept
tags: [ai-engineering, architecture, stack]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# AI Engineering Stack

**The three-layer model of an AI application as defined in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]].** The stack is the chapter's organizing diagram for the entire book — each subsequent chapter targets one of these layers.

## The three layers

### 1. Application development (top)

What an [[AIEngineering|AI engineer]] interacts with most. Responsibilities:

- **[[PromptEngineering|Prompt engineering]]** — instructions, examples, formats.
- **Context construction** — [[rag|RAG]], memory, tool integration ([[Agent|agents]]).
- **[[Evaluation|Evaluation]]** — selecting models, benchmarking, detecting regressions, production monitoring.
- **[[AIInterface|AI interface]]** — standalone apps, plug-ins, browser extensions, chat integrations, voice, embodied 3D.

This layer has seen the most action since 2023 and is still rapidly evolving.

### 2. Model development (middle)

The classical [[MLOps|ML engineering]] domain, restructured for foundation models. Responsibilities:

- **[[ModelingAndTraining|Modeling and training]]** — architectures, pretraining, post-training, finetuning.
- **[[DatasetEngineering|Dataset engineering]]** — curating, generating, annotating training data; deduplication, tokenization, context retrieval, quality control, sensitive-data removal.
- **[[InferenceOptimization|Inference optimization]]** — quantization, distillation, parallelism for serving foundation models within latency/cost budgets.
- **Evaluation** (shared with the application layer).

### 3. Infrastructure (bottom)

The least-changed layer with foundation models — *"the core infrastructural needs—resource management, serving, monitoring, etc.—remain the same."* Responsibilities:

- Model serving.
- Data and compute management.
- Monitoring.

## Stack growth (Ch 1 data)

[[ChipHuyen|Huyen's]] March 2024 GitHub analysis of 920 AI-related repos with 500+ stars:

- **2023** saw the biggest jump in tooling after [[StableDiffusion|Stable Diffusion]] and [[ChatGPT|ChatGPT]] launches.
- **Application + application-development** layers grew fastest.
- **Infrastructure** grew more slowly — because resource-management, serving, and monitoring needs are stable.

This supports Huyen's broader claim: **many ML-engineering principles transfer directly** to AI engineering. *"Built on top of these enduring principles are many innovations unique to AI engineering, which we'll explore in this book."*

## Recommended top-down development order

> *"When developing an AI application, you'll likely start from the top layer and move down as needed."*

In practice: build the application with API-served models first (top layer), only descend into model development if prompting + RAG can't reach the [[UsefulnessThreshold|usefulness threshold]]. This is the inverse of traditional ML, where teams would start with data and a model and only later build the product.

## Connections

- [[AIEngineering]] — the discipline organized around this stack.
- [[AIEngineeringVsMLEngineering]] — comparison taxonomy across stack layers.
- [[PromptEngineering]] / [[rag]] / [[Evaluation]] / [[AIInterface]] — application-layer responsibilities.
- [[ModelingAndTraining]] / [[DatasetEngineering]] / [[InferenceOptimization]] / [[FineTuning]] — model-development responsibilities.
- [[MLOps]] — the operations-flavored predecessor.
- [[ai-engineering-ch01-intro]] — primary source.
