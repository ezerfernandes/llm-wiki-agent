---
title: "FineRadScore"
type: concept
tags: [evaluation, radiology, line-by-line, prior-art, stub]
sources: [2507.03152-medval]
last_updated: 2026-05-22
---

# FineRadScore

**Line-by-line radiology report evaluation generating corrections with severity scores** — Huang, Banerjee, Wu, Pontes Reis & Rajpurkar, arXiv:2405.20613 (2024). Ref [41] in [[2507.03152-medval]].

Operates at the **line level** within a radiology report: for each line, generates a correction with a severity score. Tightly scoped to one sub-specialty. [[2507.03152-medval]] §4 groups it with [[GREEN]] / [[ReXTrust]] / [[ReXErr]] as radiology-only prior art that MedVAL generalizes beyond.

## Connections
- [[2507.03152-medval]] — the successor.
- [[MedVAL]] — generalizes across non-radiology tasks.
- [[GREEN]] / [[ReXTrust]] / [[ReXErr]] — sibling radiology-specific evaluators.
