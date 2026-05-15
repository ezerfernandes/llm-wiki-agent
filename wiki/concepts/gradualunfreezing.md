---
title: "Gradual Unfreezing"
type: concept
tags: [concept, fine-tuning, parameter-efficient]
sources: [1910.10683-t5]
last_updated: 2026-05-10
---

# Gradual Unfreezing

A fine-tuning schedule (Howard & Ruder, 2018) in which only the final layer of a pre-trained network is updated initially; then, after a fixed number of steps, the second-to-last layer is added to the update set; then the third-to-last; and so on, until the entire network is being fine-tuned.

For encoder-decoder Transformers, [[1910.10683-t5]] applies the schedule in parallel to both stacks (top-down from layer 12 in each), subdividing the 2¹⁸-step fine-tuning into 12 episodes of 2¹⁸/12 steps each. Shared input/output embedding parameters are updated throughout.

## T5's finding

Gradual unfreezing degraded performance slightly on all tasks vs full fine-tuning — the same direction as [[adapterlayers]]. It does provide a small speedup during fine-tuning because most parameters' gradients aren't computed for most of training.

## See also

- [[1910.10683-t5]] — source paper studying this method.
- [[adapterlayers]] — alternative parameter-efficient method.
- [[transformer]] — architecture the schedule is applied to.
