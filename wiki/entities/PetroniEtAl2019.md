---
title: "Petroni et al. 2019 — LAMA"
type: entity
tags: [paper, factual-probing, benchmark, knowledge-extraction]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Petroni et al. 2019 — LAMA

The paper introducing the [[LAMABenchmark|LAMA (Language Model Analysis) benchmark]] — a probe for relational knowledge in pretrained language models. From [[meta|Meta]]'s AI lab. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the founding work of [[FactualProbing|factual probing]].

## The method

Fill-in-the-blank cloze prompts encoding relational facts: *"Winston Churchill is a ___ citizen"* → *"British"*. Measure how often the model correctly fills in the blank.

This methodology — benign in its original research context — is the **primitive operation** of later [[TrainingDataExtraction|training-data extraction]] attacks (e.g., *"[Person X]'s email address is ___"*).

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[LAMABenchmark]] — the benchmark.
- [[FactualProbing]] — the research area.
- [[meta|Meta]] — origin lab.
- [[TrainingDataExtraction]] — the adversarial application.
- [[InformationExtraction]] — broader attack family.
