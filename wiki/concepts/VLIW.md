---
title: "VLIW (Very Long Instruction Word)"
type: concept
tags: [computer-architecture, cpu, parallelism, ilp, compilers]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# VLIW (Very Long Instruction Word)

**VLIW** is an [[InstructionLevelParallelism|ILP]] architecture family in which the processor executes wide instruction words encoding **multiple parallel operations**, and the **compiler** — not the hardware — is responsible for scheduling those operations and ensuring they don't conflict. [[dis-5-9-modern|Ch 5.9]] presents VLIW as the third of the three ILP families, alongside [[VectorProcessor|vector processors]] and [[Superscalar|superscalar]] designs.

## The defining trade-off

| Concern | [[Superscalar]] | **VLIW** |
|---|---|---|
| **Dependency analysis** | Hardware ([[OutOfOrderExecution|out-of-order]] logic) | **Compiler** |
| **Hardware complexity** | High | Lower |
| **Compiler complexity** | Moderate | **High — specialized backend required** |
| **Performance ceiling** | Limited by HW issue width and dynamic dependency analysis | Limited by static schedule quality |

Ch 5.9's framing: VLIW *"simplifies processor design but requires specialized compilers for good performance."*

## Scope note (Ch 5.9)

Ch 5.9 sketches VLIW at one paragraph; it does **not** name specific VLIW ISAs (Intel/HP Itanium / IA-64, TI C6x DSPs, Transmeta Crusoe), discuss instruction-bundle formats, or explore why VLIW underperformed dynamic [[Superscalar|superscalar]] schedulers on irregular code. This page captures only what Ch 5.9 says.

## Connections

- [[InstructionLevelParallelism]] — the umbrella category.
- [[Superscalar]] — the rival ILP family that does dependency analysis in **hardware**.
- [[VectorProcessor]] — the third ILP family.
- [[Compiler]] — the side of the system VLIW puts the scheduling burden on.
- [[CPU]] — the device class.
- [[dis-5-9-modern]] — primary source.
