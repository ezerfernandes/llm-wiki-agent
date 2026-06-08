---
title: "Fei-Fei Li"
type: entity
tags: [person, researcher, computer-vision, imagenet, mlsysbook]
sources: [mlsysbook-ch04-data-engineering]
last_updated: 2026-06-05
---

# Fei-Fei Li

Computer-vision researcher who created [[ImageNet]], cited in Reddi's *Machine Learning Systems* ([[mlsysbook-ch04-data-engineering|Vol 1, Ch 4]]) as the canonical example of the value of data-engineering investment.

Li's team spent **two years building the labeling infrastructure** behind ImageNet — 14.2 million images labeled by 49,000 [[AmazonMechanicalTurk|Mechanical Turk]] workers across 21,841 categories (2009). The chapter's point: that one-time data-engineering investment is reused for free by every subsequent team, making ImageNet's value as a benchmark inseparable from its data engineering. The catch is benchmark overfitting — models tuned to ImageNet's distribution underperform on production data with different lighting, occlusion, or demographics, so it is a starting point to augment, never a finishing line.

## Connections

- [[ImageNet]] — the dataset and labeling infrastructure she built.
- [[AmazonMechanicalTurk]] — the crowdsourcing platform used for labeling.
- [[Crowdsourcing]] — the acquisition method ImageNet exemplifies.
- [[mlsysbook-ch04-data-engineering]] — source.
