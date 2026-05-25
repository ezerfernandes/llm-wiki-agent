---
title: "SelfCheckGPT"
type: concept
tags: [evaluation, factuality, hallucination, self-verification]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# SelfCheckGPT

**Self-verification by N-variant disagreement** (Manakul et al. 2023). One of the three advanced [[FactualConsistency|factual-consistency]] detection methods discussed in [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]].

## The assumption

> "SelfCheckGPT relies on an assumption that if a model generates multiple outputs that disagree with one another, the original output is likely hallucinated."

## The procedure

1. Given a response **R** to evaluate.
2. Generate **N** new responses to the same query (using sampling).
3. Measure how consistent R is with respect to these N new responses.
4. Disagreement → likely hallucination.

## Trade-offs

- **Reference-free.** No ground truth needed.
- **Expensive.** Requires N+1 model calls per evaluation; *"can be prohibitively expensive."*
- **Sample-method-sensitive.** [[Temperature]] / [[Topk]] / [[Topp]] choices for the N variants matter (lower temperature → less variance → more agreement → fewer hallucinations flagged).

## Position

Sibling to [[SAFEEvaluator|SAFE]] (search-augmented) in Ch 4's "advanced AI-as-judge for factual consistency" trio. Self-verification is the [[SelfEvaluation|self-evaluation]] subtype the wiki anchored from Ch 3.

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[FactualConsistency]] — what it measures.
- [[SAFEEvaluator]] — sibling advanced method (uses search instead of self-disagreement).
- [[SelfEvaluation]] / [[SelfCritique]] — parent paradigm from Ch 3.
- [[LLMAsAJudge]] — the broader method family.
- [[Temperature]] / [[Topk]] / [[Topp]] — sampling controls that affect the N-variant generation.
