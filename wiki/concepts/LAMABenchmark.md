---
title: "LAMA Benchmark"
type: concept
tags: [benchmark, factual-probing, knowledge, llm]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# LAMA Benchmark

**LAMA (Language Model Analysis)** — the relational-knowledge probing benchmark introduced by [[PetroniEtAl2019|Petroni et al. 2019]] at [[meta|Meta]]'s AI lab. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the founding work of [[FactualProbing|factual probing]].

## What it tests

Cloze-style fill-in-the-blank prompts encoding relational facts: *"Winston Churchill is a ___ citizen"* → *British*. The full benchmark covers a wide range of relations sourced from knowledge bases (Wikipedia, ConceptNet).

## Why it matters in the prompt-attack context

The same template ("X [relation] ___") used in LAMA is the basic primitive of [[TrainingDataExtraction|training-data extraction]] attacks. LAMA itself is benign — it's a research probe — but it provided the methodology that later attack papers ([[CarliniEtAl2020|Carlini et al. 2020]], [[HuangEtAl2022|Huang et al. 2022]]) adapted for extracting **sensitive** memorized data.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[FactualProbing]] — the research area LAMA founded.
- [[PetroniEtAl2019]] — paper authors.
- [[meta|Meta]] — origin lab.
- [[TrainingDataExtraction]] — the adversarial application of the same template.
- [[InformationExtraction]] — parent attack family.
