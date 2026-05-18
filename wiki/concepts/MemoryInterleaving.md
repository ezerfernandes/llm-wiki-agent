---
title: "Memory Interleaving"
type: concept
tags: [parallel-computing, hardware, memory, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Memory Interleaving

Physical-address-to-memory-module mapping discipline used in [[SharedMemoryArchitecture|shared-memory]] systems whose memory is split into multiple [[BankConflict|banks]] for parallel access. [[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.2.1 names two:

- **High-order interleaving** — the top `k` bits of a word-address select the module. Example: 1024 word-addresses across 4 banks (M0–M3) put 0–255 in M0, 256–511 in M1, etc. Consecutive addresses stay in the *same* module, except at boundaries. Good fit for block-partitioned algorithms (matrix tiles, image regions).
- **Low-order interleaving** — the bottom `k` bits select the module. Addresses 0,1,2,3,4 land in M0,M1,M2,M3,M0,…. Consecutive addresses spread *across* consecutive modules. Good fit for stride-1 vector access — historically used on **vector processors** (regular ADD vs vector VADD reads two vectors from memory, and low-order interleaving spreads their elements across banks for fast simultaneous access). *"A more modern use of low-order interleaving, but with the same motivation as with the vector processors, is in GPUs."*

The chapter's worked example: with 8 banks under high-order interleaving, the top three bits of a word-address are the bank number; under low-order interleaving, the bottom three are.

## Stride / bank theorem

Under `b` low-order-interleaved banks, a stride-`s` access pattern hits all `b` banks if and only if `gcd(s, b) = 1`. *"You should experiment a bit to see that an array access with a stride of s will access s different banks if and only if s and b are relatively prime, i.e. the greatest common divisor of s and b is 1. This can be proven with group theory."*

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.2.1.
- [[BankConflict]] — the pathology this discipline trades off against.
- [[SharedMemoryArchitecture]] — the parent paradigm.
- [[GPU]] — modern user of low-order interleaving.
