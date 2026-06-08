---
title: "Information-Compute Ratio (ICR)"
type: concept
tags: [ml-systems, data-selection, metric, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Information-Compute Ratio (ICR)

The central metric of [[DataSelection|data selection]] in [[mlsysbook-ch09-data-selection|Reddi Ch 9]]: the learning each sample contributes per unit of computation, $\text{ICR} = \Delta I / \Delta \text{FLOPs}$. A higher ICR means each training FLOP buys more learning; raising ICR is the goal of every technique in the chapter. A **2× improvement in ICR is mathematically equivalent to a 2× improvement in hardware peak throughput** $(R_{\text{peak}})$, but usually cheaper to achieve.

**The ICR frontier ("data tax"):** ICR is not constant. In redundant data, information scales logarithmically ($I(D)\sim\log D$) while compute cost is linear ($C(D)=O_{\text{sample}}\cdot D$), so $\text{ICR}(D)\approx 1/(O_{\text{sample}}\cdot D)$ decays toward zero. Past the "knee" of this curve, more data yields near-zero learning at linear cost — data becomes a **data tax** inflating the [[IronLawOfMLSystems|iron law]] $O$ term. Worked example: a 50% EL2N coreset on ImageNet achieves ~1.8× higher ICR than random sampling.

## Connections

- [[DataSelection]] — ICR is its measurable objective.
- [[DataWall]] — the ICR-decay region is the data wall.
- [[IronLawOfMLSystems]] — ICR turns the $O$ term from constant into variable.
- [[CoresetSelection]] / [[EL2N]] — techniques that push ICR up.
- [[DataSelectionCostModel]] — extends ICR reasoning to acquisition/labeling/storage costs.
- [[mlsysbook-ch09-data-selection]] — source.
