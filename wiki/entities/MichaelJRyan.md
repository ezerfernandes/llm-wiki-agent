---
title: "Michael J Ryan"
type: entity
tags: [researcher, dspy, stanford, prompt-optimization]
sources: [2406.11695-mipro, 2507.19457-gepa]
last_updated: 2026-05-22
---

# Michael J Ryan

[[stanforduniversity|Stanford]] CS researcher; **co-first author** of the [[2406.11695-mipro|MIPRO paper (Opsahl-Ong et al., EMNLP 2024)]] and a co-author of [[2507.19457-gepa|GEPA (ICLR 2026 Oral)]] (listed among Stanford-side authors).

## Tracked contributions

- **[[2406.11695-mipro]]** (EMNLP 2024) — co-first author with [[KristaOpsahlOng]] on **[[MIPROv2|MIPRO]]**: the joint instruction + demonstration optimizer for multi-stage [[LMProgram|LM programs]].
- **[[2507.19457-gepa]]** (ICLR 2026 Oral) — co-author; continues the DSPy-adjacent optimizer line.

## Research arc

Two consecutive papers on the optimizer line: **MIPRO** (Bayesian-surrogate joint optimization, ships as `dspy.MIPROv2`) and **GEPA** (reflective-mutation prompt optimization, ships as `dspy.GEPA`). MIPRO's surrogate is over a **fixed** proposal set; GEPA generates *new* proposals reflectively. Ryan's co-authorship across both papers makes him one of the consistent Stanford-side authors on the DSPy-optimizer line ([[KristaOpsahlOng]], [[ChristopherPotts]], [[DilaraSoylu]], Ryan).
