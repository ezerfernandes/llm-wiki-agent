---
title: "Multi-Challenge"
type: concept
tags: [benchmark, evaluation, conversation]
sources: [2605.10698-bystander-effect-mas]
last_updated: 2026-05-15
---

# Multi-Challenge

Deshpande et al. 2025, ACL 2025: multi-turn conversation benchmark for frontier LLMs. Test split $N=266$.

In [[2605.10698-bystander-effect-mas]], used as the **low-entropy semantic background** ($\mathcal{H}_\tau$ class) — multi-turn conversational contexts treated as discrete logical primitives. Anchors the *Fortified Mind* baseline: the paper's claim that cognitive immunity is observable when the task is cheap enough that effortful verification beats compliance. The terminal-disengagement observation (GPT-5.4 with one Claude auditor: $\mathcal{A}_{ext}=0.10$ but ADOPTED stance only 7%; IGNORED rate 85%) is a Multi-Challenge artifact — a distinct failure mode from active sycophancy.
