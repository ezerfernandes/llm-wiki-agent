---
title: "Hardware-Software Co-Design"
type: concept
tags: [hardware, accelerators, co-design, computer-architecture]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Hardware-Software Co-Design

**Hardware-software co-design** is a development methodology that intentionally violates the traditional hardware-software abstraction boundary, letting algorithm constraints inform silicon design and hardware capabilities directly shape algorithm formulation.

## Why it matters ([[mlsysbook-ch11-hardware-acceleration]])

Co-design unlocks gains unavailable to either layer alone. INT8 [[Quantization|quantization]] delivers 2–4× throughput **not because 8-bit arithmetic is faster in the abstract**, but because [[NVIDIA]] [[TensorCore|Tensor Cores]] are physically designed to execute four INT8 ops in the die area of one FP32 op. The algorithm change pays off only because the hardware was co-designed to exploit it. Likewise, [[StructuredSparsity|structured pruning]] improves performance while unstructured pruning often does not, because structured patterns preserve the regular memory access the hardware can optimize.

## A continuous feedback loop

Co-design is not a one-time choice but a loop: NVIDIA Tensor Cores were built for FP16 matmul, then extended to TF32 and INT8 after ML workloads demanded them, then to 2:4 structured sparsity after pruning research proved structured sparsity trainable. The chapter frames co-design as *why* the [[Quantization|compression]] techniques of Ch 10 produce real speedups on hardware.

## See also
- [[DomainSpecificArchitecture]] — the architectural output of co-design.
- [[TensorCore]] / [[Quantization]] / [[StructuredSparsity]] — co-design success cases.
- [[ArithmeticIntensity]] / [[RooflineModel]] — the analytical lens for which co-designed changes help.
- [[DAMTaxonomy]] — co-design couples the Algorithm and Machine axes.
- [[mlsysbook-ch11-hardware-acceleration]] — co-design as the chapter's recurring principle.
