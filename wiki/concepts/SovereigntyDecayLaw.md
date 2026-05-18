---
title: "Sovereignty Decay Law"
type: concept
tags: [multi-agent, formalism, scaling]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Sovereignty Decay Law

Theorem 1 of [[2605.10698-bystander-effect-mas]]:

$$\mathcal{S}(p,\vec{a},\tau) = \mathcal{S}_0 \cdot \exp\!\left(-\frac{\mathcal{H}_\tau}{\gamma_p} \cdot \mathcal{L}(\vec{a},p)\right)$$

[[AgenticSovereignty]] decays *exponentially* as a function of [[CompositeSocialLoad]] $\mathcal{L}$ and [[TaskEntropy]] $\mathcal{H}_\tau$, inversely modulated by the model's intrinsic resilience $\gamma_p$. Derived from the ODE

$$\frac{d\mathcal{S}}{d\mathcal{L}} = -\frac{\mathcal{H}_\tau}{\gamma_p} \mathcal{S}$$

by integration with boundary $\mathcal{S}(\mathcal{L}=0) = \mathcal{S}_0$. The exponential form (rather than e.g. linear or sigmoid) is asserted from a "diffusion of responsibility" axiom rather than derived from first principles — a modeling choice that fits the empirical curves in Figure 1 but inherits its functional form from the analogy to physical decay laws.

The [[InteractionDepthLimit]] $D_L$ is the smallest $n$ at which $\mathcal{S} < 0.5$; closed-form via Corollary 1.
