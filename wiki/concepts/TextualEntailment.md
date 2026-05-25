---
title: "Textual Entailment"
type: concept
tags: [nlp, classification, factuality, evaluation]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Textual Entailment

A long-standing NLP task — also known as **natural language inference (NLI)** — that classifies the relationship between two statements. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]], textual entailment frames [[FactualConsistency|factual consistency]] as a 3-class classification problem.

## The three classes

Given a **premise** (context) and a **hypothesis** (output or part of output):

- **Entailment** — hypothesis can be inferred from the premise.
- **Contradiction** — hypothesis contradicts the premise.
- **Neutral** — premise neither entails nor contradicts.

## Worked example (Ch 4)

Given context: *"Mary likes all fruits"*

| Hypothesis | Class |
|---|---|
| "Mary likes apples" | Entailment |
| "Mary hates oranges" | Contradiction |
| "Mary likes chickens" | Neutral |

## Mapping to factual consistency

- Entailment → factually consistent
- Contradiction → factually inconsistent
- Neutral → consistency cannot be determined

## Specialized scorers

Instead of using general-purpose [[LLMAsAJudge|AI judges]], you can train classifiers specialized in this 3-class task. Example: [[DeBERTaV3FactConsistency|`DeBERTa-v3-base-mnli-fever-anli`]] — a 184M-parameter model trained on 764K labeled (premise, hypothesis) pairs to predict entailment. Far smaller and cheaper than GPT-4.

## Position

NLI is one of the oldest tasks in NLP (FraCaS 1996, SNLI 2015, MNLI 2018, FEVER 2018, ANLI 2020). Ch 4 repositions it as a **practical factual-consistency evaluator** for LM outputs.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[FactualConsistency]] — what it operationalizes for LM evaluation.
- [[DeBERTaV3FactConsistency]] — canonical small-scorer.
- [[LocalFactualConsistency]] — the setting NLI scorers fit naturally.
- [[LLMAsAJudge]] — the general-purpose alternative.
