---
title: "MetaMath"
type: concept
tags: [dataset-engineering, synthetic-data, math]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# MetaMath

**A synthetic math dataset created by Yu et al. (2023) by rewriting MATH and GSM-8K examples.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], MetaMath is the chapter's canonical example of **paraphrasing as a data-synthesis technique that outperforms the original**.

## The numbers

- **Input**: ~15,000 examples from MATH + [[GSM8K|GSM-8K]].
- **Output**: **~400,000 examples** of MetaMath.
- **Method**: AI-rewriting in different ways (e.g., rephrase questions, restructure solutions, change number formats).

## The headline result

> "They showed that their models, trained on this new dataset, outperformed larger models on related math benchmarks."

So a **smaller** model trained on MetaMath beat **larger** baseline models — synthetic-data leverage at a scale that's hard to replicate with manual annotation.

## What this proves about synthetic data

MetaMath is the **counter-evidence to "synthetic data is lower quality than real data"**: in math specifically, AI-rephrased data isn't just augmentation, it's an **effective data scaling lever**.

Per Ch 8, this connects to a broader claim: AI can generate math problems beyond average human-expert difficulty, so synthesis isn't just expansion but quality improvement.

## Connections

- [[AIPoweredDataSynthesis]] — parent category.
- [[InstructionDataSynthesis]] — parent category.
- [[GSM8K]] — one of the source datasets.
- [[AlphaGeometry]] — sibling synthetic-math-data success (purely procedural).
- [[Cosmopedia]] / [[UltraChat]] / [[AlpacaDataset]] — sibling synthetic datasets.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
