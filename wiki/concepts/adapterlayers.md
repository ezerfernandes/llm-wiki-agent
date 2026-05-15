---
title: "Adapter Layers"
type: concept
tags: [concept, fine-tuning, parameter-efficient]
sources: [1910.10683-t5]
last_updated: 2026-05-10
---

# Adapter Layers

A parameter-efficient fine-tuning technique (Houlsby et al., 2019; Bapna et al., 2019) in which small dense-ReLU-dense bottleneck blocks are inserted after each pre-existing feed-forward sub-layer of a [[transformer]], and only those adapter parameters plus layer-norm parameters are updated during fine-tuning. The pre-trained backbone is frozen.

The bottleneck dimension `d` is the main hyperparameter — it trades parameter efficiency for capacity.

## T5's finding ([[1910.10683-t5]] Table 10)

- Low-resource tasks (SQuAD): small `d` (32) is competitive with full fine-tuning.
- High-resource tasks (concatenated GLUE/SuperGLUE): large `d` (2048) needed to approach full fine-tuning, but never quite matches it.
- Full fine-tuning beat adapters on every task in T5's setup, *but* adapters are attractive when many tasks must share one frozen backbone (no separate copy per task).

## See also

- [[1910.10683-t5]] — source paper studying this method.
- [[transformer]] — where adapters are inserted.
- [[gradualunfreezing]] — alternative parameter-efficient method T5 also evaluates.
