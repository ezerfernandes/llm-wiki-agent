---
title: "Dive into Systems — Ch 14.4 Measuring Parallel Performance"
type: source
tags: [parallel-computing, performance, multicore, scaling, amdahl, gustafson, dive-into-systems]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C14-SharedMemory/performance.html
---

## Summary

**Hub leaf** of Ch 14.4 *Measuring Parallel Performance* of *[[DiveIntoSystems]]* — the **fourth leaf** of Ch 14 *Leveraging Shared Memory in the Multicore Era*. Pivots from the [[dis-14-3-synchronization|Ch 14.3]] synchronization-primitives arc into the **performance-measurement** arc: now that the reader has correct parallel programs, *how do we evaluate them?* Splits into two sub-leaves: **14.4.1 *Performance Basics*** (foundational metrics — [[ParallelSpeedup|speedup]], [[ParallelEfficiency|efficiency]], [[AmdahlsLaw|Amdahl's Law]]) and **14.4.2 *Advanced Performance Considerations*** ([[GustafsonsLaw|Gustafson-Barsis Law]], [[StrongScaling|strong]] / [[WeakScaling|weak]] scaling, benchmarking discipline). Tiered scope: the basics suffice for an introductory parallel-programming course; the advanced material *"round[s] out a reader's understanding of performance."*

## Key Claims

- **Two-tier organization** — foundational metrics (speedup, efficiency, Amdahl's Law) vs advanced topics (Gustafson-Barsis, scalability classes).
- **Measurement before optimization** — performance evaluation against the serial baseline is the prerequisite for any parallel-program optimization claim.
- **Amdahl's Law** is the **fundamental ceiling** on speedup imposed by serial code fractions.
- **Gustafson-Barsis Law** offers an **alternative scaling framework** addressing the assumptions Amdahl's Law makes.
- **Scalability** — the dimension of *how* parallel performance evolves as resources grow — is the advanced lens both laws articulate.

## Key Quotes

> "Having a good understanding of the following topics will round out a reader's understanding of performance."

(framing the advanced sub-leaf as optional-but-completing material on top of the basics)

## Connections

- [[DiveIntoSystems]] — parent textbook; this is its **133rd ingested chapter — opens Ch 14.4**.
- [[dis-14-4-1-performance-basics]] — first sub-leaf; speedup / efficiency / Amdahl's Law.
- [[dis-14-4-2-performance-advanced]] — second sub-leaf; Gustafson-Barsis / strong / weak scaling / benchmarking.
- [[dis-14-3-3-other-syncs]] — immediately prior leaf; closes the synchronization arc the performance arc builds on.
- [[dis-14-1-multicore]] — opening of Ch 14; supplied the informal **1/c [[Speedup|speedup]]** rule that 14.4.1 now formalizes and 14.4.1 bounds via [[AmdahlsLaw|Amdahl's Law]].
- [[ParallelSpeedup]] / [[ParallelEfficiency]] — the two foundational metrics 14.4.1 codifies.
- [[AmdahlsLaw]] — the serial-fraction speedup ceiling 14.4.1 formalizes.
- [[GustafsonsLaw]] — the problem-scaling alternative 14.4.2 introduces.
- [[StrongScaling]] / [[WeakScaling]] — the two scalability classes 14.4.2 codifies.
- [[Speedup]] — the prior wiki page; this chapter formalizes what 14.1 introduced informally.
- [[ParallelComputing]] / [[SharedMemoryParallelism]] — the paradigm whose performance is being measured.

## Contradictions

- None. Strictly extends [[Speedup]] (informal 1/c rule from [[dis-14-1-multicore|Ch 14.1.2]]) with the formal [[AmdahlsLaw|Amdahl-style]] serial-fraction analysis that [[Speedup]]'s scope note explicitly deferred to other corpus pages.
