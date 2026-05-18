---
title: "Cray-1"
type: concept
tags: [computer-architecture, history, cpu, vector-processor, supercomputer]
sources: [dis-5-9-modern]
last_updated: 2026-05-17
---

# Cray-1

The **Cray-1** (1976) is the canonical early **[[VectorProcessor|vector processor]]** — the first widely-deployed commercial machine to build [[InstructionLevelParallelism|ILP]] around vector instructions operating on arrays of data in parallel. [[dis-5-9-modern|Ch 5.9]] names it as the founding example of the vector-processor family and uses it to anchor the historical claim that *"vector processors eventually lost market dominance to other designs"* — i.e. [[Superscalar|superscalar]] CPUs displaced them in the general-purpose market, while the vector model survived inside **[[GPGPU|GPU accelerators]]**.

## Scope note

Ch 5.9 mentions the Cray-1 in a single historical paragraph; it does **not** cover its 80 MHz clock, 64-bit architecture, vector registers, freon cooling, or Seymour Cray's biography. This page captures only what Ch 5.9 says.

## Connections

- [[VectorProcessor]] — the architectural family the Cray-1 founded.
- [[InstructionLevelParallelism]] — the broader CPU-design strategy.
- [[GPGPU]] — the modern home of the vector model the Cray-1 pioneered.
- [[Superscalar]] — the rival ILP family that displaced standalone vector machines in the general-purpose CPU market.
- [[dis-5-9-modern]] — primary source.
