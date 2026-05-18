---
title: "Cognitive Loafing"
type: concept
tags: [multi-agent, sycophancy, failure-mode]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Cognitive Loafing

The state $\mathcal{B}=1$ in which a propagator LLM's integrative effort $E_{int}$ falls below the task entropy $\mathcal{H}_\tau$ — i.e. the model skips effortful derivation and adopts the swarm consensus instead. Coined in [[2605.10698-bystander-effect-mas]] as the LLM analogue of the *social loafing* principle (Ringelmann 1913; Latané, Williams & Harkins 1979): individual effort decreases as group size grows.

Distinguished from [[AlignmentHallucination]]: under cognitive loafing the derivation is *not* computed (internal evidence weighting $\mathcal{E}_{ew}$ collapses); under alignment hallucination it *is* computed (high $\mathcal{E}_{ew}$) and then discarded externally. The two manifest as opposite signs of the [[SovereigntyGap]] $G_\mathcal{S} = \mathcal{V}_{int} - \mathcal{A}_{ext}$.

See also: [[IntegrativeReasoningBypass]] (the formal name of the same failure state in the paper's terminology).
