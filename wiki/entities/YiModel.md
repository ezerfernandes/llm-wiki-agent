---
title: "Yi"
type: entity
tags: [model, llm, 01ai]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Yi

**LLM family from 01.AI (Young et al. 2024).** Cited in [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]] for the team's finding that **10K carefully crafted instructions outperform hundreds of thousands of noisy ones** — a foundational evidence point for [[DataQuality|quality > quantity]] in finetuning.

## Why it matters in Ch 8

The Yi result anchors the chapter's opening claim:

> "A small amount of high-quality data can outperform a large amount of noisy data, e.g., data that is irrelevant or inconsistent. The creators of the Yi model family found that 10K carefully crafted instructions are superior to hundreds of thousands of noisy instructions (Young et al., 2024)."

Paired with [[LIMA]]'s 1,000-example result, this is one of the two empirical anchors for the chapter's quality-over-quantity argument.

## Connections

- [[DataQuality]] — the dimension Yi anchors.
- [[LIMA]] — sibling small-data finding.
- [[Llama|Llama 3]] — also corroborates the small-curated-data finding (with AI-assisted annotation).
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
