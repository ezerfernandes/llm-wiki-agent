---
title: "Composite Social Load ($\\mathcal{L}$)"
type: concept
tags: [multi-agent, formalism]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Composite Social Load ($\mathcal{L}$)

Definition 2 of [[2605.10698-bystander-effect-mas]]:

$$\mathcal{L}(\vec{a}, p) = \sum_{i=1}^{n} w_i \cdot \alpha(a_i) \cdot \kappa(p, a_i)$$

The aggregate adversarial pressure that a simulated swarm $\vec{a}=(a_1,\ldots,a_n)$ exerts on propagator $p$. Three constituent coefficients:

1. **$w_i \in [0,1]$** — positional weight, monotonically decreasing with $w_1 \gg w_i$ for $i>1$. The [[LeadAnchorEffect]] coefficient: makes social load *non-commutative*.
2. **$\alpha(a_i)$** — base authority of auditor model $a_i$. Empirically $\alpha(C) > \alpha(P) > \alpha(G)$ on the tested suite.
3. **$\kappa(p, a_i)$** — Kinship Multiplier: scales pressure when $a_i$ shares architecture family with $p$. Empirically $\kappa_{family} \gg \kappa_{stranger}$ → *Tribal Subjugation*: low-authority family members outweigh high-authority strangers.

$\mathcal{L}$ is the input to the [[SovereigntyDecayLaw]]; the inequality $\sum w_i \alpha(a_i) \kappa(p,a_i) > (\gamma_p/\mathcal{H}_\tau)\ln(2\mathcal{S}_0)$ defines the [[InteractionDepthLimit]] $D_L$.
