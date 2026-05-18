---
title: "GAIA"
type: concept
tags: [benchmark, evaluation, agents]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# GAIA

Mialon et al. 2024, ICLR 2024: a *General AI Assistant* benchmark incorporating reasoning + multi-step fact verification + tool use. Test split $N=301$.

In [[2605.10698-bystander-effect-mas]], GAIA serves as the **high-entropy semantic background** ($\mathcal{H}_\tau$ class) for an injected 3-hop verification task — the paper does *not* evaluate on GAIA's own labels; it uses GAIA's text as a noisy context against which to measure the [[SovereigntyGap]]. The terminal-load empirical findings (GPT-5.4 collapses to $\mathcal{A}_{ext}=0.53$ at $n=5$ with $\mathcal{V}_{int}\approx 0.21$ — the [[IntegrativeReasoningBypass]] regime) all come from the GAIA arm.
