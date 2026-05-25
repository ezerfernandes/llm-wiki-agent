---
title: "Krista Opsahl-Ong"
type: entity
tags: [researcher, dspy, stanford, prompt-optimization]
sources: [2406.11695-mipro, 2507.19457-gepa]
last_updated: 2026-05-22
---

# Krista Opsahl-Ong

[[stanforduniversity|Stanford]] CS researcher; **first author** of the [[2406.11695-mipro|MIPRO paper (Opsahl-Ong et al., EMNLP 2024)]] and a member of the GEPA team ([[2507.19457-gepa|Agrawal et al. 2026]]). Supported by the [[NSFCSGrad4US]] Graduate Fellowship.

## Tracked contributions

- **[[2406.11695-mipro]]** (EMNLP 2024, w/ Michael J Ryan as co-first) — introduces **[[MIPROv2|MIPRO]]**, the joint-instruction-and-demonstrations optimizer for multi-stage [[LMProgram|LM programs]]. Released as `dspy.MIPROv2` in [[DSPy]]; the **reference optimizer** of the DSPy 2.x optimizer catalog.
- **[[2507.19457-gepa]]** (ICLR 2026 Oral) — co-author; GEPA continues the DSPy-adjacent optimizer line that MIPRO opened. (Listed among Stanford-side authors in the GEPA paper.)

## Research arc

The MIPRO → GEPA progression: MIPRO ships **Bayesian-surrogate credit assignment** over a fixed set of bootstrapped (instruction, demo) proposals — Lesson 5 of MIPRO's paper explicitly flags *"surrogate-based optimization only allows for optimization over a fixed set of proposals; learnings from past evaluations cannot be used to improve the proposals themselves"*. GEPA closes exactly this gap with reflective prompt mutation. Opsahl-Ong's authorship spans both ends of this arc.
