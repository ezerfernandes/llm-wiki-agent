---
title: "Information Entropy (Data Density)"
type: concept
tags: [ml-systems, mlsysbook, data-engineering, information-theory]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Information Entropy (Data Density)

In the data-engineering sense of Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]), **information entropy is the density of signal** — bits of useful information per byte of data. A dataset of 1 million identical images has high [[DataGravity|gravity]] (TB of storage) but near-zero entropy (one image's worth of information); 10,000 diverse edge cases have low gravity but high entropy.

It is the numerator of **Data Selection Gain ∝ Information Entropy / Data Gravity**, the ratio that effective data engineering maximizes. "Data cleaning" is reframed as **signal-to-noise engineering**: [[DataDeduplication|deduplication]] removes mass without reducing entropy (raising the ratio), while [[ActiveLearning|active learning]] adds high-entropy edge cases and ignores low-entropy common cases.

This grounds the "more data isn't always better" fallacy: beyond a threshold, redundant low-entropy examples add mass without information, and test loss follows a power law in dataset size. Smart [[DataSelection|data selection]] beats naive accumulation.

## Connections

- [[DataGravity]] — the denominator of Data Selection Gain.
- [[DataSelection]] / [[ActiveLearning]] / [[DataDeduplication|Deduplication]] — levers that raise entropy per byte.
- [[Entropy]] / [[KullbackLeiblerDivergence]] — the information-theory roots.
- [[mlsysbook-ch04-data-engineering]] — source.
