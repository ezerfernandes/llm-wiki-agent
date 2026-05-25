---
title: "Dataset Engineering"
type: concept
tags: [data, dataset, ai-engineering, training-data]
sources: [ai-engineering-ch01-intro, ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Dataset Engineering

**Curating, generating, and annotating the data needed for training and [[ModelAdaptation|adapting]] AI models.** A model-development-layer responsibility in the [[AIEngineeringStack|AI engineering stack]]. Per [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]], dataset engineering replaces classical ML's "feature engineering" as the data-side discipline in the foundation-model era.

## What changes from classical ML

| Aspect | Traditional ML | Foundation models |
|---|---|---|
| Data type | Mostly **tabular** | **Unstructured text + images + audio** |
| Output style | **Close-ended** (predefined labels — e.g., "spam"/"not spam") | **Open-ended** (text generation, image generation) |
| Annotation difficulty | Easy ("spam" or not) | Hard (write a high-quality essay) |
| Main activity | Feature engineering | Deduplication, tokenization, context retrieval, quality control |

## Why annotation is harder for FMs

> *"It's easier to determine whether an email is spam than to write an essay."*

[[GenerativeAI|Open-ended outputs]] make annotation orders of magnitude more expensive — you're producing the target rather than picking it from a fixed set. Data quality has a much bigger leverage on model behavior.

## Dataset engineering activities (Ch 8 of the book)

- **Deduplication** — remove redundant training examples.
- **Tokenization** — convert raw text/code into model-compatible token sequences ([[Tokenization]]).
- **Context retrieval** — select relevant context for [[rag|RAG]] or finetuning.
- **Quality control** — remove low-quality, sensitive, or toxic content; manage [[Hallucination|hallucination]]-inducing patterns.
- **Data synthesis** — use foundation models themselves to generate training data (with humans in the loop to improve labels).

## How much data?

Ch 1's rough scaling guidance:

- **Training from scratch** → most data.
- **[[FineTuning|Finetuning]]** → middle.
- **[[PromptEngineering|Prompt engineering]]** → least.

Even for prompt-engineered systems, data expertise is useful: *"as its training data gives important clues about that model's strengths and weaknesses."*

## "Data as the moat"

Ch 1 notes a common claim Huyen heard during book research: *"because models are now commodities, data will be the main differentiator, making dataset engineering more important than ever."* This connects to the [[AIProductDefensibility|defensibility]] discussion — once model APIs commoditize, data and distribution become the durable moats.

## Connections

- [[AIEngineering]] / [[AIEngineeringStack]] — discipline-level home.
- [[FineTuning]] / [[PromptEngineering]] / [[rag]] — adaptation techniques that consume engineered datasets.
- [[Tokenization]] — one specific dataset-engineering operation.
- [[AIProductDefensibility]] — the moat-formation argument.
- [[ai-engineering-ch01-intro]] — primary source (Ch 1, references Ch 8 deep dive).

## From [[ai-engineering-ch08-dataset-engineering|AI Engineering Ch 8]]

Ch 8 is the book's full treatment of dataset engineering — what Ch 1 forward-referenced. [[ChipHuyen|Huyen]]'s framing rests on three orthogonal axes, analogized to cooking:

- **[[DataQuality]]** — quality of the ingredients.
- **[[DataCoverage]]** / **[[DataDiversity]]** — the right *mix* of ingredients.
- **[[DataQuantity]]** — how many ingredients.

**Six quality characteristics**: relevant, aligned with task requirements, consistent, correctly formatted, sufficiently unique, compliant.

**The chapter's pipeline (paraphrased)**:

1. **[[DataAcquisition|Acquisition]]** — public sources, purchased, annotated, synthesized; the highest-value source is application data ([[DataFlywheel|data flywheel]]).
2. **[[DataAnnotation|Annotation]]** with **[[AnnotationGuidelines|guidelines]]** — manual or AI-assisted; guidelines are harder than the annotation itself.
3. **[[DataAugmentation|Augmentation]]** — derive new from real ([[Perturbation]], gender-token swap, rotation/crop).
4. **[[DataSynthesis|Synthesis]]** — generate mimicking real ([[RuleBasedDataSynthesis|rule-based]], [[Simulation]], [[AIPoweredDataSynthesis|AI-powered]]).
5. **Processing**: inspect → [[DataDeduplication|deduplicate]] → clean/filter → format ([[Tokenization]] + [[ChatTemplate]]).

**Headline empirical claims from Ch 8**:

- Small high-quality data beats large noisy data — [[LIMA]], Yi, Llama 3 all corroborate.
- Coverage saturates around ~282 finetuning tasks (Chung et al. 2022).
- [[Ossification]] flips the finetune-vs-from-scratch decision at millions-of-examples scale.
- [[ModelCollapse]] and [[SuperficialImitation]] are the two main limits on AI-generated data.

This page is the high-level hub; see the individual concept pages for the deep dives.
