---
title: "Instruction-Level Parallelism (ILP)"
type: concept
tags: [computer-architecture, cpu, parallelism, ilp]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Instruction-Level Parallelism (ILP)

[[dis-5-9-modern|Ch 5.9]] defines **ILP** as *"a set of design techniques used to support parallel execution of a single program's instructions on a single processor."* The key property: ILP is **transparent to the programmer** — sequential code is written as if instructions run one at a time, while the hardware (or, in [[VLIW]], the compiler) extracts parallelism behind the scenes.

## The three ILP families (Ch 5.9 taxonomy)

1. **[[VectorProcessor|Vector processors]]** — execute one operation on an *array* of operands in parallel. Pioneered by the **[[Cray1|Cray-1]]** (1976); now most visible inside [[GPGPU|GPU accelerators]].
2. **[[Superscalar|Superscalar]]** — multiple pipelines + execution units run independent instruction streams in parallel; out-of-order dependency analysis is done **in hardware**. Theoretical IPC ceiling equals the issue width (5-pipeline superscalar → IPC 5), reduced by real-program instruction dependencies.
3. **[[VLIW|VLIW (Very Long Instruction Word)]]** — moves dependency analysis to the **compiler**; the hardware just executes the long instruction words it's handed.

## Why ILP eventually plateaued

[[MooresLaw|Moore's Law]] kept supplying transistors, and architects spent the budget on deeper, wider, smarter single cores — until the early-2000s [[PowerWall|power wall]] made further single-core scaling uneconomical. Post-power-wall, architects pivoted to **multiple execution streams** ([[HardwareMultithreading|hardware multithreading]], [[SimultaneousMultithreading|SMT]], [[MulticoreProcessor|multicore]]) — which require **explicit parallel programming** to exploit, breaking ILP's "free lunch" property.

## Connections

- [[VectorProcessor]] / [[Superscalar]] / [[VLIW]] — the three concrete ILP families.
- [[MooresLaw]] — the historical driver of ILP investment.
- [[PowerWall]] — the constraint that ended ILP's monopoly as the scaling path.
- [[SimultaneousMultithreading]] / [[MulticoreProcessor]] — the post-ILP scaling levers.
- [[InstructionPipelining]] — the simpler time-axis parallelism ILP layers on top of.
- [[CyclesPerInstruction]] / [[InstructionThroughput]] — metrics ILP improves.
- [[dis-5-9-modern]] — primary source.
