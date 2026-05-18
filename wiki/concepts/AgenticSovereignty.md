---
title: "Agentic Sovereignty"
type: concept
tags: [multi-agent, alignment, formalism]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Agentic Sovereignty

$\mathcal{S}(p, \vec{a}, \tau) \in [0,1]$: the probability that a propagator model $p$ maintains the integrity of its internal logical derivation on task $\tau$, *independently of the swarm consensus* $\vec{a}$. Formalized in [[2605.10698-bystander-effect-mas]]. $\mathcal{S}=1$ is the *Fortified Mind* ceiling (resilient metacognitive vigilance); $\mathcal{S}=0$ is the [[HollowedMind]].

Governed by the [[SovereigntyDecayLaw]]:

$$\mathcal{S}(p,\vec{a},\tau) = \mathcal{S}_0 \cdot \exp\!\left(-\frac{\mathcal{H}_\tau}{\gamma_p} \cdot \mathcal{L}(\vec{a},p)\right)$$

where $\mathcal{H}_\tau$ is [[TaskEntropy]], $\gamma_p$ is the model's intrinsic *Resilience* (architectural constant — empirically $\gamma_{Claude} \to \infty$ on the benchmarks tested), and $\mathcal{L}$ is the [[CompositeSocialLoad]]. The 0.5-crossing of $\mathcal{S}$ defines the [[InteractionDepthLimit]] $D_L$.
