---
title: "EDVAC"
type: concept
tags: [history, computer-architecture, foundational]
sources: [dis-5-1-history]
last_updated: 2026-05-17
---

# EDVAC (Electronic Discrete Variable Automatic Computer)

The successor design to [[ENIAC]] at the [[UniversityOfPennsylvania|Moore School]], proposed in 1945 by [[JohnMauchly]], [[PresperEckert]], and [[JohnVonNeumann]]. The machine was eventually completed in 1951.

## Significance

The conceptually important artifact is not the physical machine but **[[JohnVonNeumann|von Neumann]]'s 1945 *"First Draft of a Report on the EDVAC"*** — the paper that codified the **[[StoredProgram|stored-program]]** principle and established what is now called the **[[VonNeumannArchitecture|von Neumann architecture]]**:

- **Program instructions and data** both reside in the same internal [[RAM|memory]]
- A [[CPU]] sequentially **fetches** instructions, **decodes** them, and **executes** via an [[ALU]] and [[ControlUnit|control unit]]
- Computation is driven by manipulating a [[ProgramCounter|program counter]] (instruction pointer) rather than by physically rewiring the machine

Per [[dis-5-1-history|*Dive into Systems* Ch 5.1]], the EDVAC paper is the **synthesizing document** of early computing — it distilled the engineering practices emerging in [[ENIAC]] / [[Z3]] / [[Colossus]] / [[HarvardMarkI|Mark I]] into a single architectural template that became the foundation of essentially every modern computer.

Unlike [[ENIAC]]'s decimal representation, EDVAC was a **binary** machine — aligning the hardware representation with [[ClaudeShannon|Shannon]]'s 1937 [[BooleanAlgebra|Boolean circuit]] insight.
