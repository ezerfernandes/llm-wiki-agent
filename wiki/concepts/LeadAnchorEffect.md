---
title: "Lead Anchor Effect"
type: concept
tags: [multi-agent, evaluation, prompting]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Lead Anchor Effect

Lemma 1 of [[2605.10698-bystander-effect-mas]]: for two distinct auditor models $a_x$ and $a_y$, the [[CompositeSocialLoad]] is **sequence-dependent**:

$$\mathcal{L}((a_x, a_y), p) \neq \mathcal{L}((a_y, a_x), p)$$

Operationally: the *first-listed* auditor in a prompted swarm carries disproportionate authority, captured by a monotonically-decreasing positional weight vector $w_1 \gg w_i$ for $i>1$. Empirical proof: GPT-5.4 propagator on SWE-bench at $n=2$ — sequence $(C,P)$ → $\mathcal{A}_{ext}=0.21$, inverted sequence $(P,C)$ → $\mathcal{A}_{ext}=0.31$ ($10\%$ accuracy delta from order alone, identities held constant).

Methodological consequence: any MAS evaluation that mixes auditor identities must control for permutation order, or its measured social pressure is confounded by the Lead Anchor coefficient. The paper's *25-Trial Symmetric Categorical Sweep* is built specifically to cancel this bias.

Curious asymmetry: when [[gemini|Gemini]] is the propagator and [[gpt54|GPT-5.4]] is the lead auditor, Gemini performs *better* (the "Brand Subjugation / Gemini Inversion") — it trusts the GPT brand identity *more than its own*. Architectural humility, not architectural pride, drives some of the Lead Anchor effect.
