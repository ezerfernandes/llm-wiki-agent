---
title: "Domain-Specific Architecture (DSA)"
type: concept
tags: [hardware, accelerators, dsa, computer-architecture]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Domain-Specific Architecture (DSA)

A **domain-specific architecture** is silicon optimized for a single application domain, sacrificing general-purpose programmability for efficiency. DSAs emerged as the answer to the breakdown of [[MooresLaw|Moore's Law]] and [[DennardScaling|Dennard scaling]] — Hennessy & Patterson named this the new era of computer architecture in their 2017 Turing Lecture.

## Design principles ([[mlsysbook-ch11-hardware-acceleration]])

DSAs achieve superior performance/efficiency through reinforcing choices: customized data paths ([[SystolicArray|systolic arrays]] for matrix multiply), specialized [[MemoryHierarchy|memory hierarchies]] built around the domain's reuse patterns, domain-specific instruction sets, and direct hardware implementation of frequent operations that bypass software interpretation.

## The 10× rule and the TPU shock

Google's [[GoogleTPU|TPU]] achieves 15–30× better performance-per-watt than GPUs on inference by eliminating branch prediction, caches, and out-of-order logic in favor of a systolic array. The trade-off is inflexibility: a DSA that excels at dense matrix multiplication may underperform a CPU on irregular workloads like graph traversal. **Hennessy and Patterson's rule of thumb: a new architecture must deliver ≥10× efficiency over the general-purpose alternative to justify the ecosystem cost of adoption.**

## See also
- [[GoogleTPU]] / [[NeuralProcessingUnit]] / [[ASIC]] — instances of the DSA idea.
- [[HardwareSoftwareCodesign]] — the methodology that makes DSAs pay off.
- [[DennardScaling]] / [[MooresLaw]] — the scaling breakdown that forced the shift.
- [[DAMTaxonomy]] — DSAs are the "Machine" axis.
- [[mlsysbook-ch11-hardware-acceleration]] — DSA efficiency trade-off and the 10× adoption threshold.
