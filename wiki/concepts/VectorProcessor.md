---
title: "Vector Processor"
type: concept
tags: [computer-architecture, cpu, parallelism, ilp, simd]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Vector Processor

A **vector processor** is an [[InstructionLevelParallelism|ILP]] architecture that *"executes one operation on an array of data in parallel"* — instead of a scalar instruction acting on one operand pair, a vector instruction acts on many operand pairs simultaneously through replicated execution units. [[dis-5-9-modern|Ch 5.9]] introduces it as the **first of the three ILP families** (alongside [[Superscalar|superscalar]] and [[VLIW|VLIW]]).

## History (per Ch 5.9)

- **1976 — [[Cray1|Cray-1]]** pioneered the commercial vector processor and dominated the high-performance computing market of its era.
- Through the 1980s–1990s, general-purpose CPU markets shifted toward [[Superscalar|superscalar]] designs; standalone vector machines lost share.
- **Today** — vector-processor design *"primarily appears in GPU accelerators"* ([[GPGPU]]). The model has not disappeared; it has migrated.

## Relationship to other ILP families

| Family | Parallelism axis | Dependency analysis |
|---|---|---|
| **Vector** | One op × many operands | Implicit in the instruction's vector semantics |
| **[[Superscalar]]** | Many independent ops, same cycle | **Hardware** (out-of-order) |
| **[[VLIW]]** | Many ops bundled per instruction word | **Compiler** |

## Scope note (Ch 5.9)

Ch 5.9 sketches the vector-processor model at a paragraph level. It does **not** detail vector registers, vector length, masking, gather/scatter, modern [[SIMD|SIMD]] ISAs (x86 SSE/AVX, ARM NEON/SVE, RISC-V V), or the precise architectural lineage from Cray to GPUs. The page captures only what Ch 5.9 says.

## Connections

- [[InstructionLevelParallelism]] — the umbrella category.
- [[Cray1]] — the canonical historical example.
- [[GPGPU]] — the modern continuation of the vector model.
- [[Superscalar]] / [[VLIW]] — the two sibling ILP families.
- [[Vectorization]] — the compiler/programmer side of generating vector instructions.
- [[CPU]] — the device class.
- [[dis-5-9-modern]] — primary source.
