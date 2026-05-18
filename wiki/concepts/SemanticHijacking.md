---
title: "Semantic Hijacking"
type: concept
tags: [evaluation, adversarial, prompting]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Semantic Hijacking

3-stage adversarial prompt-construction methodology from Shehata & Li 2026a (arxiv 2604.24512 — *referenced but not yet ingested*), repurposed inside [[2605.10698-bystander-effect-mas]] to artificially elevate the logical search cost of an audit task above the threshold at which the propagator would otherwise pattern-match-and-pass:

1. **Context Hijacking (Primacy Trap):** inject a simulated peer consensus or preliminary guess (the *poisoned ID*) at the primacy boundary of the prompt — frictionless, incorrect, competes directly with the model's mandate to verify ground truth.
2. **Nested 3-Hop Dependency Bridging:** force the model to navigate a chain $F_1 \to F_2 \to F_3$ to derive the correct `true_id` (e.g. authorization session → kernel token → reference signature). No single-needle retrieval shortcut.
3. **Semantic Distraction:** interleave the 3-hop facts with ~500 tokens of realistic randomized system log events. Saturates attention heads, raises [[TaskEntropy]].

Justification: the [[BystanderEffect]] is only visible when verifying truth is *more* expensive than conforming to the peer. Saturating attention with high-entropy distraction is the methodological lever that forces the propagator into a real choice between effortful derivation and frictionless compliance.
