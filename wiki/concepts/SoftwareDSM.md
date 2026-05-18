---
title: "Software Distributed Shared Memory (SDSM)"
type: concept
tags: [parallel-computing, shared-memory, message-passing, distributed-systems]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Software Distributed Shared Memory (SDSM)

A class of **software packages that simulate shared memory on message-passing hardware** such as Networks of Workstations (NOWs). *"Since the platforms do not have any physically shared memory, the shared-memory view which the programmer has is just an illusion. But that illusion is very useful, since the shared-memory paradigm is believed to be the easier one to program in. Thus SDSM allows us to have 'the best of both worlds'."* ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.11.1).

## Two flavors

- **Page-based SDSM** — generally considered clearer and easier to program in; provides a *"look and feel"* closest to true shared-memory. The chapter focuses here.
- **Object-based SDSM** — every shared variable is a discrete object. Not related to OOP. Not discussed at length.

## Page-based mechanism

Page-based SDSMs co-opt the host OS's virtual memory:

1. The library marks a page **non-resident** via `mprotect()` whenever it knows the local copy of a shared variable on that page is stale — even if the page *is* physically resident.
2. The next access to that page raises a page fault, which on Unix is delivered to user space as a **SIGSEGV signal**.
3. The SDSM library installs its own SIGSEGV handler that performs network transactions to obtain the latest valid page contents.
4. Control returns to the user code, which then re-reads the page.

## Named systems

- **Treadmarks** (Rice University) — the most popular page-based SDSM at time of writing. Uses **UDP** rather than TCP (TCP is *"simply not designed for this kind of work"*).
- **[[JIAJIA]]** (Academy of Sciences, China) — the chapter's worked case study. Page-based, *scope-consistent*, *home-based*, *multiple-writer*.

## Cost relative to hardware shared memory

Two compounding overheads:

1. **Network slowness** — TCP/IP-class round-trips vs nanosecond bus access. Even UDP and the **Virtual Interface Architecture (VIA)** can't close the gap.
2. **Granularity** — SDSMs ship 4 KB **pages**; hardware [[CacheCoherency|coherency]] ships ~512 B cache **blocks**. *"The overhead for a cache coherency transaction can thus be large."*

The granularity mismatch also magnifies [[FalseSharing|false sharing]]; JIAJIA's multi-writer feature is specifically designed to mitigate page-level false sharing.

## What SDSM cannot fake: shared pointers

```c
int Y, *P;
P = &Y;
```

Each SDSM node has its own address space, so the address `&Y` is different on each node. The page system keeps `Y`'s value consistent across nodes, but `P` would store an address that's only meaningful at one node. *"There is no simple way to have a variable like P in an SDSM."*

## Software coherency

Just as hardware shared-memory needs a [[CacheCoherency|cache coherency]] protocol, SDSM needs a **software analog**: when one node writes to a shared variable, every interested node must eventually be notified. Designers pick **update** vs **invalidate**, *just as in the hardware case*. Non-bus-style systems also need directory-style structures listing which node holds the valid copy.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.11.1.
- [[JIAJIA]] — the chapter's case study.
- [[MPI]] — the message-passing substrate SDSMs run on top of.
- [[MessagePassingArchitecture]] — the hardware paradigm.
- [[SharedMemoryArchitecture]] — the paradigm SDSMs *simulate*.
- [[CacheCoherency]] — the hardware analog of SDSM's software-coherency layer.
- [[MemoryConsistency]] — SDSMs pick a consistency model (sequential / release / scope).
- [[FalseSharing]] — magnified at page granularity.
- [[Barrier]] — `jia_barrier()` is the SDSM API surface for the consistency event.
