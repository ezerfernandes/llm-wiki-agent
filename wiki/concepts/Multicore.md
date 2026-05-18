---
title: "Multicore"
type: concept
tags: [parallel-computing, hardware, cpu, shared-memory]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Multicore

Single-chip [[SMP]] — "two or more CPUs share a common memory" on one piece of silicon. [[parproc-ch01-intro-parallel-processing]] frames multicore as the consumerization of shared-memory parallelism: "until recently, shared-memory systems cost hundreds of thousands of dollars and were affordable only by large companies … but now multicore machines … are commonplace in the home and even in cell phones!"

Architecturally identical to off-chip SMP: "the multicore setup is effectively the same as SMP, except that the processors are all on one chip, attached to the bus."

The chapter's terminology footnote on "processor" vs "core" (footnote 1, p. 3): "Although each core is a complete processor, people in the field tend to call the entire chip a 'processor,' referring to the cores, as, well, cores. In this book, the term *processor* will generally include cores, e.g. a dual-core chip will be considered to have two processors." This convention is Matloff's deliberate choice and is worth flagging when reading the book against other sources that reserve "processor" for the chip.

Multicore is the assumed hardware target for the [[Pthreads]] and [[OpenMP]] examples throughout the chapter — and across the book, since this is what the book's audience actually has on their desks.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces the term.
- [[SMP]] — multicore is single-chip SMP.
- [[SharedMemoryArchitecture]] — the broader paradigm.
- [[Pthreads]] / [[OpenMP]] — the typical programming layers used to exploit multicore.
- [[MIMD]] — multicore is MIMD-executing.
- [[GPU]] — alternative on-chip parallelism (SIMD lanes rather than MIMD cores).
