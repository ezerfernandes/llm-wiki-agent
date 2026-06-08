---
title: "Compound Scaling"
type: concept
tags: [model-compression, efficient-architecture, nas, mlsysbook]
sources: [mlsysbook-ch10-model-compression]
last_updated: 2026-06-05
---

# Compound Scaling

**Scaling a network's depth, width, and input resolution *together* via fixed ratios rather than independently, to stay on the accuracy-efficiency Pareto frontier.** Per [[mlsysbook-ch10-model-compression|mlsysbook Ch 10]], this is the hardware-aware-design principle [[EfficientNet]] empirically validated.

## The formulation

$$ N_L = \alpha^\phi N_{L,0}, \quad w = \beta^\phi w_0, \quad r = \gamma^\phi r_0 $$

where $\phi$ is a scaling coefficient and $\alpha,\beta,\gamma$ are scaling factors fixed by hardware constraints/empirical search. Total conv FLOPs $\propto N_L \cdot w^2 \cdot r^2$, so naively scaling all three explodes cost; compound scaling balances them. EfficientNet traces the frontier: B0 (77.1%, 390M FLOPs) → B7 (84.4%, 37B FLOPs) — a 95× compute increase for 7.3 points.

## Connections

- [[EfficientNet]] — the architecture family built on compound scaling.
- [[NeuralArchitectureSearch]] — NAS discovered the principle.
- [[ModelCompression]] — a hardware-aware scaling-optimization principle.
- [[mlsysbook-ch10-model-compression]] — source.
