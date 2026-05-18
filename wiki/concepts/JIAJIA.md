---
title: "JIAJIA (Software DSM System)"
type: concept
tags: [parallel-computing, shared-memory, distributed-systems, sdsm, case-study]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# JIAJIA

A page-based [[SoftwareDSM|software distributed shared memory]] system developed at the **Academy of Sciences, China**, and the worked case study of [[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.11.2. The implementation library is `libjia.a`, linked with applications via `-ljia`; the C/C++/FORTRAN API surface is `jia_init()`, `jia_alloc()`, `jia_barrier()`, `jia_lock()`, `jia_unlock()`, `jia_exit()`, plus the magic variable **`jiapid`** holding the calling node's rank.

[[NormMatloff]] maintains a tutorial at http://heather.cs.ucdavis.edu/~matloff/jiajia.html.

## Defining characteristics

The chapter's §3.11.2 lists four:

- **Page-based** — pages, not objects, are the unit of shared state.
- **Scope-consistent** — see [[MemoryConsistency]]; a write within a critical section guarded by lock L becomes visible to the next acquirer of L. Barriers also force flush.
- **Home-based** — every page has a designated **home processor**; writers must ship their changes to the home on unlock. `jia_alloc()` has variants letting the programmer designate the home, so for matrix problems one can place rows on the same node that writes them.
- **Multiple-writers** — two or more nodes may write to the *same* page simultaneously between barriers. At the barrier, JIAJIA reconciles the writes by computing a **diff** between each writer's local copy and a saved **twin** snapshot taken at the start of the writable interval. *"Allowing multiple writers helps to reduce the performance penalty due to false sharing"* — the dominant pathology at 4 KB page granularity.

## Worked example: Odd/Even Transposition Sort

A bubble-sort variant where every processor `jiapid` alternately trades values with its left (`jiapid-1`) and right (`jiapid+1`) neighbors across `n` phases. JIAJIA's API surfaces in this code as:

```c
jia_init(argc, argv);          // required init
jia_barrier();                  // sync after init
x = (float*) jia_alloc(n * sizeof(float));  // allocate shared array
jia_barrier();                  // sync after allocation
...
jia_barrier();                  // sync after writes
jia_exit();                     // shutdown
```

Each node calls `jia_alloc()` and (visible to the library, not to the programmer) holds its own physical copy of `Prime`. A subsequent write `Prime[I] = 1;` at one node *eventually* triggers a network transaction propagating the update to other nodes' copies.

## Mechanism: page tables + scope events

Each node maintains a page table tracking, for every shared page, one of three states: **Invalid**, **Read-Only**, **Read-Write**. State changes happen when **lock/unlock operations occur** — not eagerly on each write.

When `jia_unlock()` runs, the lock-holder ships the diff to the **home** of the page. When another node next calls `jia_lock()` on that same lock and accesses the variable, a **page fault** at that node triggers JIAJIA's SIGSEGV-style handler, which fetches the updated page from the lock-holder (or the home).

Cost numbers from the related Treadmarks system: *"167 microseconds to make a twin, and as much as 686 microseconds to make a diff."*

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.11.2.
- [[SoftwareDSM]] — the parent category.
- [[MemoryConsistency]] — JIAJIA picks scope consistency.
- [[FalseSharing]] — what JIAJIA's multi-writer feature mitigates.
- [[Barrier]] — `jia_barrier()` is the unify-and-propagate event.
- [[MessagePassingArchitecture]] — the substrate hardware.
- [[MPI]] / [[Pthreads]] — sibling shared-state APIs JIAJIA's interface mimics.
- [[NormMatloff]] — wrote the tutorial at UC Davis.
