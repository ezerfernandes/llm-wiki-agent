---
title: "DARE Merging"
type: concept
tags: [model-merging, finetuning, pruning]
sources: [ai-engineering-ch07-finetuning]
last_updated: 2024-12-04
---

# DARE Merging

**Drop And REscale.** Yu et al. (2023) — sibling of [[TIESMerging|TIES]] in the pruning-aware [[ModelMerging|model merging]] family. Per [[ai-engineering-ch07-finetuning|*AI Engineering* Ch 7]], DARE shares TIES's core observation — most parameters in a [[TaskVector|task vector]] are redundant and harmful when merging multiple models — but takes a different pruning strategy.

## The two steps (the acronym)

1. **Drop**: randomly zero out a large fraction (e.g., 90%) of task-vector parameters. Stochastic, not magnitude-based.
2. **REscale**: scale the surviving parameters up by `1/(1−p)` (where `p` is the drop rate) to preserve the expected magnitude.

Then merge the rescaled task vectors with [[LinearCombinationMerging|linear combination]] (or another base merge method).

## DARE vs. TIES

| Property | [[TIESMerging\|TIES]] | DARE |
|---|---|---|
| Pruning criterion | Magnitude-based (top-k) | Random (dropout-style) |
| Rescaling | No | Yes (multiplicative) |
| Sign election | Yes | No (not applicable to random subsets) |

Ch 7 notes that both methods "significantly improve the quality of the final merged models" — the choice between them is empirical.

## Why "random pruning" works

DARE's connection to dropout: at training time, dropout zeros out random activations and rescales the survivors, and the resulting model learns a redundancy-robust representation. DARE applies the same observation to weight-space: finetuning produces redundancy-robust deltas, so we can drop most of them without losing the signal — *as long as we rescale*.

## Connections

- [[ModelMerging]] — parent operation.
- [[TIESMerging]] — sibling magnitude-based variant.
- [[TaskVector]] — the operand DARE prunes.
- [[LinearCombinationMerging]] — the typical merge step after DARE pruning.
- [[Dropout]] — the conceptual ancestor.
- [[ai-engineering-ch07-finetuning]] — primary source.
