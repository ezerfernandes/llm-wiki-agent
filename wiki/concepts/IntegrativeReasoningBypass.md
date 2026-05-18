---
title: "Integrative Reasoning Bypass"
type: concept
tags: [multi-agent, sycophancy, failure-mode]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Integrative Reasoning Bypass

Definition 3 of [[2605.10698-bystander-effect-mas]]. Binary failure state $\mathcal{B}=1$ that triggers when the propagator's integrative effort $E_{int}$ falls below the intrinsic task entropy $\mathcal{H}_\tau$:

$$\mathcal{B} = \begin{cases} 1 & \text{if } E_{int} \ll \mathcal{H}_\tau \\ 0 & \text{if } E_{int} \geq \mathcal{H}_\tau \end{cases}$$

The agent rationally offloads procedural retrieval to the simulated swarm (cheap, useful) and *also* offloads integrative reasoning (expensive, destructive) — the [[CognitiveLoafing]] state. Manifests as the $G_\mathcal{S} \ll 0$ regime of the [[SovereigntyGap]]: low internal validity *plus* residual external accuracy that's just probabilistic guessing.

Contrasts with [[AlignmentHallucination]] where the integrative effort *is* spent but the result is overridden externally.
