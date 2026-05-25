---
title: "TIES Merging"
type: concept
tags: [model-merging, finetuning, pruning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# TIES Merging

**TrIm, Elect Sign, and merge.** [[Yadav2023TIES|Yadav et al. (2023)]] — "TIES-Merging: Resolving Interference When Merging Models." Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], TIES is one of two pruning-aware [[ModelMerging|model merging]] methods (alongside [[DAREMerging|DARE]]) that **prune redundant [[TaskVector|task-vector]] parameters before merging**.

## The core insight

Most parameters in a finetune's task vector are **redundant** — small adjustments that don't materially contribute to task performance. Reset (i.e., zero out) those parameters, and:

- Single-task performance is essentially unchanged.
- Multi-task merging quality **improves** — because the redundant params would otherwise interfere with other tasks' signal.

Yadav et al. show that **keeping the top 20% of task-vector parameters by magnitude is comparable to keeping 100%**.

## The three steps (the acronym)

1. **TrIm**: keep the top-k% (by magnitude) of each task vector's parameters; zero out the rest.
2. **Elect Sign**: where multiple task vectors disagree on the sign of the *same* parameter, pick the dominant sign (majority vote or magnitude-weighted vote).
3. **Merge**: combine the remaining (sign-aligned) parameters via linear combination.

## Why the sign-election step matters

Multiple finetunes might both want to *increase* a parameter (positive task vector) or both want to *decrease* it (negative). But if one wants +x and another wants −x, naively averaging gives ~0 — losing both signals. Sign election preserves the dominant direction.

## When TIES matters most

> "The more models there are to merge, the more important pruning is because there are more opportunities for redundant parameters in one task to interfere with other tasks." — Ch 7

For merging 2 models, naive linear combination may suffice. For merging 5+ models, TIES/DARE-style pruning becomes important.

## Connections

- [[ModelMerging]] — parent operation.
- [[DAREMerging]] — sibling pruning-aware merge method.
- [[TaskVector]] — the operand TIES operates on.
- [[LinearCombinationMerging]] — the merge step at the end of TIES.
- [[Yadav2023TIES]] — the paper.
- [[ai-engineering-ch07-finetuning]] — primary source.
