---
title: "Low-Rank Attention Correction"
type: concept
tags: [concept, attention, adapter, memory]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# Low-Rank Attention Correction

Steering interface introduced by [[deltamem|δ-mem]] in [[2605.12357-delta-mem]]: a frozen Transformer's attention computation is adjusted at inference by adding two **history-dependent** low-rank deltas.

## Mechanism
Given the [[onlinestateofassociativememory|OSAM]] readout $\mathbf{r}_t = \mathbf{S}_{t-1}\mathbf{q}_t^m \in \mathbb{R}^r$:

- **Query-side correction:** $\Delta\mathbf{q}_t = \mathbf{W}_q^\Delta \mathbf{r}_t$, added as $\tilde{\mathbf{q}}_t = \mathbf{q}_t^0 + \frac{\alpha}{r}\Delta\mathbf{q}_t$.
- **Output-side correction:** $\Delta\mathbf{o}_t = \mathbf{W}_o^\Delta \mathbf{r}_t$, added post-attention as $\tilde{\mathbf{y}}_t = \mathbf{a}_t + \frac{\alpha}{r}\Delta\mathbf{o}_t$.

Default rank $r=8$ with scaling $\alpha=16$.

## Distinction from static LoRA
[[parammem|LoRA]]-style adapters insert *static* low-rank weight updates after training. δ-mem's projection weights $\mathbf{W}_q^\Delta, \mathbf{W}_o^\Delta$ are also static — but their **input** $\mathbf{r}_t$ is the readout of a *runtime-evolving* state. Consequence: the same parameters generate different steering trajectories under different histories. The correction lives in the same low-rank subspace but its coordinates change online.

## Ablation results
| Branches modified | Avg score |
|---|---|
| q only | 44.51 |
| k only | 42.19 |
| v only | 44.24 |
| o only | 47.05 |
| qo (default) | **48.05** |
| qkvo | 48.05 |

Output branch alone is the strongest single-branch choice; qo captures most of the qkvo benefit at half the parameters. Layer ablation: applying to *all* layers is best (47.97 avg), with middle 12 layers > front > back among partial configurations.
