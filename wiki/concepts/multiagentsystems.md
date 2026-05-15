---
title: "Multi-Agent Systems"
type: concept
tags: [ml-method, system-architecture]
sources: [2512.04388-conductor, 2605.03310-coordination-architectural-layer, 2605.02396-heavyskill]
last_updated: 2026-05-10
---

# Multi-Agent Systems

Systems where multiple LLM agents collaborate or compete. Two competing positions in the corpus: (1) the Conductor learns coordination end-to-end via RL ([[2512.04388-conductor]]); (2) Nechepurenko & Shuvalov argue coordination should be a separately-specified architectural layer enabling pre-deployment failure-mode prediction ([[2605.03310-coordination-architectural-layer]]). HEAVYSKILL is a third axis: collapse multi-agent orchestration into one model's inner skill.

## Connections
- [[coordinationlayer|CoordinationLayer]]
- [[agenticharness|AgenticHarness]]
- [[mast|MAST]]
