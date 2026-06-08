---
title: "Data Pruning"
type: concept
tags: [dataset-engineering, training-efficiency, data-selection, mlsysbook]
sources: [ai-engineering-ch08-dataset-engineering, mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Data Pruning

**Selecting a subset of available training data that gives the best performance per unit of compute.** Per [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]], the canonical reference is Sorscher et al. (2022): *"the discovery of good data-pruning metrics can significantly reduce the resource costs of modern deep learning."*

## Why prune at all

When you have more data than you need (or can afford to train on under your compute budget), you have to drop some examples. The question is **which ones to keep**.

Naive answers: random sampling, keep the most recent. Better answers use **importance metrics**:

- **[[ActiveLearning|Active learning]]** — select examples the model is most uncertain about.
- **[[ImportanceWeighting|Importance sampling]]** — weight examples by their relevance to the task.
- **Difficulty curves** — keep examples that aren't too easy or too hard.
- **Diversity metrics** — keep examples that fill underrepresented coverage gaps.

## Why it's hard

> "Their efficiencies depend on whether you have a good way to evaluate the importance of each training example."

Without a reliable importance metric, all pruning methods devolve into approximate-random.

## Pruning vs deduplication

| Operation | Goal |
|---|---|
| [[DataDeduplication\|Deduplication]] | Remove redundant copies of the same example |
| **Data pruning** | Select the best subset from non-duplicate examples |

## In [[mlsysbook-ch09-data-selection|Machine Learning Systems Ch 9]]

Reddi Ch 9 treats pruning as one of three [[StaticDataPruning|static-pruning]] techniques, distinguishing **quality pruning** (removing samples that actively harm learning) from [[CoresetSelection|coreset selection]] (informativeness) and [[DataDeduplication|deduplication]] (redundancy). Quality pruning = label-error detection ([[Cleanlab]]-style confidence patterns), outlier removal, and [[Perplexity|perplexity]]/low-information filtering. The "Data Quality Multiplier" makes the stakes concrete: clean-data convergence scales $\mathcal{O}(1/N)$ vs noisy $\mathcal{O}(1/\sqrt N)$, so **one clean label is worth ~100 noisy ones** — cleaning is a 100× compute accelerator.

## Connections

- [[DataDeduplication]] — sibling operation (different goal).
- [[StaticDataPruning]] / [[CoresetSelection]] / [[DataSelection]] — the Ch 9 pruning taxonomy.
- [[ActiveLearning]] / [[ImportanceWeighting]] / [[importancesampling|Importance Sampling]] — importance-metric methods.
- [[Cleanlab]] — label-error detection for quality pruning.
- [[DataQuality]] / [[DataCoverage]] — the criteria pruning optimizes for.
- [[ai-engineering-ch08-dataset-engineering]] / [[mlsysbook-ch09-data-selection]] — sources.
