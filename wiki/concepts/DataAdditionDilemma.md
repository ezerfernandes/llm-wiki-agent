---
title: "Data Addition Dilemma"
type: concept
tags: [dataset-engineering, data-coverage, training]
sources: [ai-engineering-ch08-dataset-engineering]
last_updated: 2024-12-04
---

# Data Addition Dilemma

**The counter-result that adding more heterogeneous data can degrade model performance.** Named in Shen et al. (2024), *"The Data Addition Dilemma"* — cited in [[ai-engineering-ch08-dataset-engineering|*AI Engineering* Ch 8]] as the qualifier on the "more data is always better" default.

## The claim

> "'The Data Addition Dilemma' (Shen et al., 2024) demonstrated that in some cases, adding more heterogeneous data can lead to worse performance."

## What this contradicts

The default heuristic across most chapters of *AI Engineering* — that data quantity helps — is conditional. **More data only helps if the data matches the inference distribution.** Off-distribution data acts as noise; in extreme cases, it pushes the model away from the target distribution faster than the on-distribution data pulls it toward.

## How to use this

When considering a new data source:

1. Sample it and compare its distribution against your inference distribution.
2. Estimate the off-distribution fraction.
3. Run a small-data ablation to see if performance goes up or down.
4. Filter out off-distribution examples before mass training.

This is also the structural reason **application data** (perfectly aligned with the inference distribution) is the highest-leverage source per [[DataFlywheel]].

## Connections

- [[DataCoverage]] / [[DataDiversity]] — the broader concept this counter-result qualifies.
- [[DataQuantity]] — the dimension this counter-result complicates.
- [[DataFlywheel]] — the alignment-by-construction approach.
- [[ai-engineering-ch08-dataset-engineering]] — primary source.
