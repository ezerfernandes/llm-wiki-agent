---
title: "Carlini et al. 2020 — Training Data Extraction from GPT-2"
type: entity
tags: [paper, privacy, training-data, prompt-attack, llm-security]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Carlini et al. 2020 — Training Data Extraction from GPT-2

The paper that demonstrated **[[TrainingDataExtraction|training-data extraction]] from GPT-2**. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as the first major attack of this kind.

## Setup and result

The attack: given a fragment of context similar to how a piece of memorized data appeared in training, prompt the model to auto-complete it; in some fraction of cases, the model emits the original memorized text verbatim.

Conclusion: training-data extraction is **technically possible** — but the risk was assessed as low because *"the attackers need to know the specific context in which the data to be extracted appears."* If the email lived in training-data context like *"X frequently changes her email address, and the latest one is ___"*, the attacker would need to reconstruct the prefix.

## Position

This is the **prefix-knowledge-required generation** of the training-data extraction attack family. [[HuangEtAl2022|Huang et al. 2022]] extended the technique to GPT-3. [[NasrEtAl2023|Nasr et al. 2023]] then **defeated the prefix-knowledge requirement** with the [[DivergenceAttack|divergence attack]].

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[TrainingDataExtraction]] — the parent attack.
- [[HuangEtAl2022]] / [[NasrEtAl2023]] — successor work.
- [[InformationExtraction]] / [[PromptAttack]] — broader families.
- [[CarliniEtAl2023]] — same first author's later work on diffusion-model extraction.
