---
title: "Anyscale"
type: entity
tags: [company, platform, ray, inference]
sources: [madewithml-mlops-setup, madewithml-mlops-jobs-and-services, madewithml-mlops-training, madewithml-mlops-tuning, madewithml-mlops-serving, ai-engineering-ch09-inference-optimization]
last_updated: 2024-12-04
---

# Anyscale

Managed [[Ray]] platform. Provides the Workspaces, Jobs, and Services primitives that host development, batch training, and online serving throughout the [[MadeWithML]] MLOps track.

## From [[ai-engineering-ch09-inference-optimization|AI Engineering Ch 9]]

Ch 9 cites Anyscale (Kadous et al. 2023) for the **100-input-tokens ≈ 1-output-token latency claim** — one of the chapter's load-bearing facts:

> *"In an experiment, Anyscale found that a single output token can have the same impact on latency as 100 input tokens (Kadous et al., 2023). Improving the autoregressive generation process by a small percentage can significantly improve user experience."*

This number — 100:1 between [[Decode|output]] and [[Prefill|input]] token latency impact — quantifies why Ch 9 spends so much of its budget on attacking the autoregressive decoding bottleneck. It's also why an output token costs 2–4× an input token in API pricing.

## Connections

- [[InferenceOptimization]] — the discipline.
- [[Decode]] / [[Prefill]] — the asymmetry Anyscale quantified.
- [[Ray]] — Anyscale's platform substrate.
