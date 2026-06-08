---
title: "Total Cost of Ownership (TCO)"
type: concept
tags: [ml-systems, deployment, economics, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch15-responsible-engineering]
last_updated: 2026-06-05
---

# Total Cost of Ownership (TCO)

The analysis that quantifies the **gap between sticker price and true system cost** by including all direct and indirect costs (power, cooling, network, labor, development velocity) over a system's lifetime. The economic layer of the [[DeploymentDecisionFramework|deployment decision framework]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

The cloud-vs-edge decision makes TCO explicit, trading high upfront CapEx (hardware) for recurring OpEx (cloud services). For an on-premise GPU, the purchase price is often only 30–40% of the three-year TCO. Worked example (1M inferences/day at ResNet-50 scale): edge reaches cost parity at ~45% utilization and saves ~45% at high steady volume — *but* edge TCO is **dominated by labor** (~60%), not hardware, so organizations without DevOps capacity should not assume edge is cheaper. Below the crossover, cloud elasticity wins. A related pitfall: "minimizing computational resources minimizes total cost" — a $2K/month cloud compute bill can be cheaper than a $6K/month edge total once network engineering, maintenance, and reliability labor are counted (a 3× difference), with development velocity (2 vs. 6 months to production) compounding the gap.

## Connections

- [[DeploymentDecisionFramework]] — TCO is its cost layer.
- [[CloudML]] / [[EdgeML]] — the two paradigms the TCO analysis weighs.
- [[DeploymentSpectrum]] — cost spans ~six orders of magnitude across tiers.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 uses a worked recommender TCO to show **inference dominates training ~40–47:1** ($3.2K/training cycle vs. ~$500K/yr inference; breakdown ≈ 2% training / 73% inference / 25% ops), so efficiency ([[Quantization|quantization]]/[[Pruning|pruning]]) is both a cost and a [[CarbonFootprint|carbon]] lever.
