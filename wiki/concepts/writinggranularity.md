---
title: "Writing Granularity (TSW / SSW / MSW)"
type: concept
tags: [concept, memory, online-learning]
sources: [2605.12357-delta-mem]
last_updated: 2026-05-15
---

# Writing Granularity

Three strategies for *when* the [[onlinestateofassociativememory|OSAM]] state is updated, introduced in [[2605.12357-delta-mem]]:

## Token-State Write (TSW)
Update per token: $\mathbf{S}_t = \mathrm{Update}(\mathbf{S}_{t-1}, \mathbf{x}_t)$. Finest granularity, captures local changes, but susceptible to format symbols and short-term noise.

## Sequence-State Write (SSW)
Update once per message segment. Hidden states within message $\mathcal{M}^{(j)}$ are averaged: $\bar{\mathbf{x}}^{(j)} = \frac{1}{|\mathcal{M}^{(j)}|}\sum_{t \in \mathcal{M}^{(j)}} \mathbf{x}_t$, then $\mathbf{S}_{(j)} = \mathrm{Update}(\mathbf{S}_{(j-1)}, \bar{\mathbf{x}}^{(j)})$. Smoother but loses sub-message detail.

## Multi-State Write (MSW)
Maintain $N$ parallel sub-states; each updates independently and their readouts are concatenated: $\mathbf{r}_t = \mathrm{Concat}(\mathbf{r}_t^{(1)}, \ldots, \mathbf{r}_t^{(N)})$. Reduces mutual interference within a single state. Default $N=4$.

## Empirical winners by backbone
| Backbone | TSW avg | SSW avg | MSW avg |
|---|---|---|---|
| Qwen3-4B-Instruct | **51.66** | 51.44 | 50.74 |
| Qwen3-8B | 50.68 | **50.86** | 49.49 |
| SmolLM3-3B | 34.74 | 36.67 | **36.96** |

Trend: stronger backbones do well with finer (TSW) or sequence-level (SSW) updates; weaker backbones benefit most from MSW's interference reduction. On LoCoMo specifically, MSW is consistently best across all three backbones.
