---
title: "Huang et al. 2022 — Training Data Extraction from GPT-3"
type: entity
tags: [paper, privacy, training-data, prompt-attack, llm-security]
sources: [ai-engineering-ch05-prompt-engineering]
last_updated: 2024-12-04
---

# Huang et al. 2022 — Training Data Extraction from GPT-3

The paper that demonstrated **[[TrainingDataExtraction|training-data extraction]] from GPT-3**, extending the [[CarliniEtAl2020|Carlini et al. 2020]] result to larger models. Cited in [[ai-engineering-ch05-prompt-engineering|*AI Engineering* Ch 5]] as part of the early-extraction-attack literature.

## Position

Sits with [[CarliniEtAl2020]] in the **prefix-knowledge-required** generation of training-data extraction work. The attack works but requires the attacker to know how the target data appeared in training context — limiting the practical threat surface.

[[NasrEtAl2023|Nasr et al. 2023]]'s [[DivergenceAttack|divergence attack]] later removed this requirement, increasing the practical severity.

## Connections

- [[ai-engineering-ch05-prompt-engineering]] — primary source.
- [[TrainingDataExtraction]] — the attack.
- [[CarliniEtAl2020]] — prior work on GPT-2.
- [[NasrEtAl2023]] — successor work that defeated the prefix-knowledge defense.
- [[InformationExtraction]] / [[PromptAttack]] — broader families.
