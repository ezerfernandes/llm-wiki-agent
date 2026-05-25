---
title: "Scaling Bottlenecks"
type: concept
tags: [scaling, training-data, infrastructure]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Scaling Bottlenecks

Per [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]], two visible bottlenecks **threaten further scaling of foundation models**: training data and electricity.

## Bottleneck 1: Training data

Foundation models consume so much data that there's a realistic concern of running out of **internet text** within years. Villalobos et al. (2022) project that **the rate of training-dataset-size growth is much faster than the rate of new data being generated**.

Three sub-pressures:

1. **Data terms of service tightening.** Longpre et al. (2024): between 2023–2024, **the rapid crescendo of data restrictions rendered 28% of the most critical sources in C4 fully restricted; 45% of C4 became restricted overall**. Reddit and Stack Overflow famously changed their data terms post-ChatGPT to block competitor scraping.
2. **Web is filling with AI-generated content.** [[meta|Igor Babuschkin]] (Grok core developer): *"the web is full of [[ChatGPT|ChatGPT]] outputs."* Recursive training on AI-generated data may cause models to *gradually forget the original data patterns* (Shumailov et al. 2023) — though Ch 8 of the book argues the picture is more nuanced.
3. **The "right to forget" problem.** No good technique exists today to make a model forget specific information learned during training. Deleting a blog post doesn't remove its content from already-trained models.

## Bottleneck 2: Electricity

Less obvious but more pressing per Ch 2:

- Data centers consume **1–2% of global electricity** as of writing.
- Projected to reach **4–20% by 2030** (Patel, Nishball, Ontiveros 2024).
- Until energy production scales, **data centers can grow at most ≈50× — less than two orders of magnitude**.
- The consequence: power shortage in the near future, driving up the cost of electricity.

## What's the workaround for the data bottleneck?

Per Ch 2, once publicly available data is exhausted, the most feasible paths for more human-generated training data are:

- **Proprietary data deals.** OpenAI negotiated with Axel Springer, the Associated Press, and others.
- **Unique proprietary corpora** become a competitive advantage: copyrighted books, translations, contracts, medical records, genome sequences, etc.

## What's the workaround for the electricity bottleneck?

Ch 2 doesn't give one — the chapter flags this as **the more pressing bottleneck**.

## Connections
- [[CommonCrawl]] / [[c4]] — the dataset side.
- [[ChinchillaScalingLaw]] / [[scalinglaws]] — the scaling-law framework whose extrapolation collides with these bottlenecks.
- [[ModelCollapse]] (if/when ingested) — the recursive-AI-training-data degradation question.
- [[ai-engineering-ch02-foundation-models]] — primary source.
- [[NVIDIA]] — the GPU vendor whose hardware drives the energy demand.
