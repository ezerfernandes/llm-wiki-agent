---
title: "Factual Probing"
type: concept
tags: [llm, evaluation, knowledge, training-data, privacy]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Factual Probing

**A niche research area focused on figuring out what relational knowledge a language model has memorized from its training data.** Introduced by [[meta|Meta]] AI in 2019 with the [[LAMABenchmark|LAMA (Language Model Analysis)]] benchmark. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the research-side foundation that gets repurposed as a [[InformationExtraction|prompt attack]].

## The technique

Relational knowledge follows the pattern **"X [relation] Y"** — *X was born in Y*, *X is a Y*, *X works for Y*. Factual probing extracts this knowledge via fill-in-the-blank prompts:

```
Winston Churchill is a ___ citizen.
→ British
```

A model that has the (Churchill, citizen-of, British) fact memorized will fill in the blank correctly.

## The benchmark

[[LAMABenchmark|LAMA]] ([[PetroniEtAl2019|Petroni et al. 2019]]) is the canonical factual-probing benchmark — a corpus of cloze-style relational-knowledge prompts used to measure how much relational knowledge an LM has encoded.

## The dual-use problem

The same fill-in-the-blank pattern that probes for benign relational knowledge also probes for **sensitive information**:

```
[Person X]'s email address is ___
```

If the model memorized Person X's email from training data, it may complete the prompt with the email. This is the bridge from factual-probing research to [[TrainingDataExtraction|training-data extraction]] attacks.

Ch 5: *"The same techniques used to probe a model for its knowledge can also be used to extract sensitive information from training data."*

## Defenses

[[anthropic|Anthropic]] and other providers block *"suspicious fill-in-the-blank requests"* — Ch 5's Figure 5-15 shows [[anthropic|Claude]] declining a fill-in-the-blank, mistaking it for a copyrighted-work request. This is a coarse defense (high false-positive rate) but it does cut off the cleanest extraction pattern.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[LAMABenchmark]] — the probe benchmark.
- [[PetroniEtAl2019]] — the LAMA paper authors.
- [[meta|Meta]] — origin lab.
- [[TrainingDataExtraction]] — the attack form factual probing enables.
- [[InformationExtraction]] — parent attack family.
- [[CarliniEtAl2020]] / [[HuangEtAl2022]] — researchers who applied factual-probing-style techniques as extraction attacks.
