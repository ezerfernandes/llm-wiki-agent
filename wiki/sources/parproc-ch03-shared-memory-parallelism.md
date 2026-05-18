---
title: "ParProcBook Ch3: Shared Memory Parallelism"
type: source
tags: [textbook, parallel-computing, shared-memory, cache, synchronization, numa]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch3: Shared Memory Parallelism

Chapter 3 (pp. 43–80) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. A thirty-eight-page descent from the high-level vocabulary of [[parproc-ch02-recurring-performance-issues|Ch2]] into the hardware mechanisms that make shared-memory programming possible: memory module structure ([[MemoryInterleaving|interleaving]] and [[BankConflict|bank conflicts]]), interconnection topologies (bus / [[Crossbar|crossbar]] / [[OmegaNetwork|omega-delta]]), synchronization primitives ([[TestAndSet|TAS]], Intel `LOCK` prefix, [[FetchAndAdd|fetch-and-add]]), [[CacheCoherency|cache coherency]] (snoopy invalidate/update, directory-based, and the [[MESI]] state machine), [[FalseSharing|false sharing]], [[MemoryConsistency|memory-access consistency models]] (sequential / release / scope), [[Multicore|multicore]] chips, [[ProcessorAffinity|processor affinity]], [[SoftwareDSM|software DSM]] with [[JIAJIA]] as the worked case study, and three barrier implementations — a use-once mutex barrier, a reusable two-counter barrier, and parallel [[TreeBarrier|tree]] / [[ButterflyBarrier|butterfly]] barriers.

## Summary

The chapter answers a deceptively simple question — *what does it actually mean for memory to be "shared"?* — by laying out the hardware substrate one layer at a time. At the lowest level (§3.1–§3.2), memory is **split into modules / banks**; consecutive accesses to the same bank serialize and so [[BankConflict|conflict]]. The two interleaving disciplines — **high-order** (consecutive words in the same module) and **low-order** (consecutive words in consecutive modules) — trade off block-locality for stride-parallelism, and the chapter shows that a stride-`s` access on `b` low-order-interleaved banks hits all banks iff `gcd(s, b) = 1`. Layer two (§3.3) connects processors to modules via three topologies — bus, [[Crossbar|crossbar]] ($n^2$ pathways, e.g. Sun Enterprise 10000's 16×16), and [[OmegaNetwork|omega/delta]] (multistage, $\log_2 n$ depth) — with an explicit latency/bandwidth/cost scaling table: bus is $O(1)/O(1)/O(1)$; omega is $O(\log n)/O(n)/O(n \log n)$; crossbar is $O(n)/O(n)/O(n^2)$. Omega is presented as the popular compromise. Layer three (§3.4) is **synchronization hardware**: [[TestAndSet]] as the canonical atomic primitive, Intel's `LOCK` prefix (`lock cmpxchg`, `lock inc`, `lock addl` — locks the bus for the whole instruction), and [[FetchAndAdd]] (one round-trip instead of two for `X++`, with optional packet-combining in multistage networks so two `F&A(X,1)` packets meeting at a switch coalesce into one `F&A(X,2)`). Layer four (§3.5) is [[CacheCoherency]]: snoopy bus protocols of **invalidate** vs **update** flavors (the analogy: invalidate ↔ write-back, update ↔ write-through), directory-based protocols for non-bus systems, and the [[MESI]] four-state machine (Modified / Exclusive / Shared / Invalid) used in the Pentium series. The chapter walks every MESI transition table — reads, writes, read snoops, write snoops — and gives a worked example. §3.5.3 names [[FalseSharing]] as the pathological consequence of cache-line granularity: two unrelated variables on the same cache line ping-pong invalidations. §3.6 distinguishes **coherency** (multiple caches, one address) from **consistency** (one variable, *when* its new value becomes visible) — driven by write buffers and register caching — and surveys [[MemoryConsistency|sequential / release / scope]] models, SPARC's `MEMBAR`, and notes the recent Pentium reversion to sequential consistency. §3.8 frames [[Multicore]] as "just SMPs, for the most part." §3.10 introduces [[ProcessorAffinity]]: pinning threads to cores to preserve cache contents (OpenMP 3.1 supports this). §3.11 covers [[SoftwareDSM]] — the page-based illusion of shared memory over [[MPI|message-passing]] hardware via `mprotect` + SIGSEGV handlers — with **[[JIAJIA]]** (Academy of Sciences, China) and Treadmarks (Rice) as the named systems; JIAJIA is *page-based*, uses *scope consistency*, is *home-based*, and **allows multiple writers** per page (reducing false-sharing penalty via diff-and-twin reconciliation). The chapter closes (§3.12) with three barrier implementations of increasing sophistication: a buggy use-once mutex barrier, a buggy reusable variant, a correct two-counter alternating-parity barrier, a `pthread_cond_wait` refinement that swaps spinning for blocking, and finally the parallel [[TreeBarrier|tree]] ($\log_2 n$ levels of sub-barriers) and [[ButterflyBarrier|butterfly]] (each node bit-flip-handshakes with $\log_2 n$ partners) schemes.

## Key Claims

- **Shared memory = shared address space.** *"The term **shared memory** means that the processors all share a common address space."* (§3.1). Global variable `X` mapped by the compiler to address 200 is the same physical cell from every CPU; the stack-pointer (ESP) trick gives each thread its own private `Y` even though all stacks live in the shared address space.
- **Memory is split into modules / banks for parallelism.** *"parallel execution of a program requires, to a large extent, parallel accessing of memory… facilitated by dividing the memory into separate modules or banks."* (§3.2).
- **Two interleaving disciplines.** **High-order interleaving** — top `k` bits of word-address select the module, so consecutive words stay in the same module (good for block partitioning). **Low-order interleaving** — bottom `k` bits select the module, so consecutive words land in consecutive modules (good for stride-1 vector access; used historically on **vector processors** and modernly on **GPUs**).
- **The [[BankConflict|bank conflict]] disaster.** If 16 threads each sum 1 M elements of a 16-million-element array with `x` starting at a multiple of 4 in bank 0 under low-order interleaving and four banks, *"these will all be in memory bank 0! Thus there will be major conflicts, hence major slowdown."* Fix: assign thread `thr` to indices `16*j + thr` so consecutive threads access consecutive banks — *no conflicts, hence speedy performance*.
- **Stride / bank theorem.** Under `b` low-order banks, a stride-`s` access pattern hits all `b` banks iff `gcd(s, b) = 1`. *"This can be proven with group theory."* (§3.2.2).
- **Padding** is a workaround when the algorithm can't be rewritten: lengthen the array (e.g. 16M → 16,000,016) to shift conflicting elements into different banks.
- **Struct-of-arrays beats array-of-structs** for parallel access patterns: contiguous struct fields cause excessive cache misses when only one field is hot; pivoting to a struct-of-arrays restores contiguity (§3.2.2).
- **Three interconnection topologies with explicit scaling.**

  | criterion | bus | omega | crossbar |
  |---|---|---|---|
  | latency | O(1) | O(log₂n) | O(n) |
  | bandwidth | O(1) | O(n) | O(n) |
  | cost | O(1) | O(n log₂n) | O(n²) |

  *"Omega-networks amount to a compromise between buses and crossbars, and for this reason have become popular."* (§3.3.4). Sun Microsystems Enterprise 10000 had a 16×16 crossbar.
- **[[NUMA]] generalizes [[SMP]] for larger systems.** Each processing element (PE) is a P/M/R triple; same-PE access is fast via the local bus, cross-PE access goes through the router and global bus. *"Today almost all high-end MIMD systems are NUMAs."* Good NUMA programming exploits the nonuniformity (matching matrix rows to local modules).
- **Bus saturation forces multipathway topologies.** *"If one has more than, say, two dozen processors are on the bus, the bus becomes saturated, even if traffic-reducing methods such as adding caches are used."* (§3.3.3).
- **[[TestAndSet]] is the canonical synchronization primitive.** Atomic `copy L to R; if R is 0 then write 1 to L`. Bus arbitration plus a dedicated TAS line make the two micro-steps indivisible. *"no bus transactions by other processors may occur between the two steps."* (§3.4.1).
- **Intel `LOCK` prefix gives bus-atomic instructions without software locks.** Applies to ADD/ADC/AND/BTC/BTR/BTS/CMPXCHG/DEC/INC/NEG/NOT/OR/SBB/SUB/XOR/XADD (XCHG asserts `LOCK#` unconditionally). *"we could do `lock inc total` without software locks!"* — replaces a three-line `pthread_mutex_lock` / `total++` / `pthread_mutex_unlock` block. The cost is that the bus is locked for the *entire* duration of the instruction; `lock addl $3, x` requires two bus transactions (read old, write new).
- **You may not need the latest.** A work-queue consumer that misses a producer's just-added task still operates correctly — just slower. Not every shared read demands strict freshness. (§3.4.2).
- **[[FetchAndAdd]] cuts round-trips.** *"There would be hardware adders placed at each memory module. That means that the whole operation could be done in one round trip to memory."* `X++` plus a software `LOCK/UNLOCK` pair otherwise requires multiple round-trips. (§3.4.3). The chapter later extends this to **packet combining** in multistage networks (§3.7): when two F&A packets meet at a switch node, the node coalesces them into one F&A with summed delta — *delicate but valuable for shared counters*.
- **[[CacheCoherency]] is "consistency between caches"** (§3.5.1). Spinning on a TAS lock variable in a bus-only system *"would be unthinkable: as each processor contending for a lock variable spins in the loop shown above, it is adding tremendously to bus traffic."* Solution: per-CPU caches, with coherency protocols to keep them consistent.
- **Snoopy bus protocols of two flavors.** **Invalidate**: when a CPU writes a variable, it first tells other caches to mark their copies invalid; they re-fetch on next access. **Update**: the writing CPU broadcasts the new value to all other caches immediately. *"This relation between these two is somewhat analogous to the relation between **write-back** and **write-through** protocols for caches in uniprocessor systems."* The chapter notes that *which* protocol wins depends on workload — update is bandwidth-wasteful when other CPUs don't actually need the latest, invalidate wastes work when the data is hot at many CPUs.
- **Directory-based protocols for non-bus systems.** *"A solution is to send messages only to 'interested parties.'"* — maintain a directory at the memory listing the *home* of each block and which caches currently have valid copies; send invalidates/updates only to those copies. Needed because broadcast over a multipath network requires extra copies per path.
- **[[MESI]] = Modified / Exclusive / Shared / Invalid** — Pentium's invalidate protocol. The four-state machine governs each (cache, block) pair: M = written-to and unique-valid; E = unique-valid but not yet written; S = at-least-one-other-cache-also-valid; I = invalid or absent. The state changes are tabulated in full for reads, writes, and read/write snoops. Notable transition: a **write miss does NOT bring the block in from memory** — it just publishes the write and leaves the local state I. *"Note that a write miss does NOT result in the associated block being brought in from memory."*
- **[[FalseSharing]] is the price of cache-line granularity.** Adjacent C variables `int W, Z;` typically share a cache line; writing `Z` invalidates `W` at other processors even though they care only about `W`. *"this can lead to a 'ping-pong' effect, in which alternate writing to two variables leads to a cyclic pattern of coherency transactions."* Fix: pad — `int W, U[1000], Z;`.
- **Cache coherency ≠ memory consistency.** *"the issues here are quite different. In this case, it is a timing issue: After one processor changes the value of a shared variable, when will that value be visible to the other processors?"* (§3.6). **Write buffers** and register caching introduce the delay.
- **[[MemoryConsistency|Consistency model]] hierarchy.** **Sequential consistency** (strongest, slowest): memory ops in the executed order are observed in that order by all CPUs. **Release consistency**: ACQUIRE/RELEASE instructions; ACQUIRE waits for all pending RELEASEs, RELEASE flushes write buffers. **Scope consistency**: relaxed release variant tied to specific lock variables — writes within a critical section guarded by lock `L` become visible to the *next* CPU that acquires `L`. SPARC's `MEMBAR` instruction is the concrete hardware barrier (LOAD or STORE operand). *"The recent Pentium models use Sequential Consistency, with any write done by a processor being immediately sent to its cache as well."*
- **Cache coherency operations are *postponed* until the consistency model says they fire.** When a write goes to a write buffer, the cache coherency protocol *does not see it* until the buffer is flushed at the next consistency-prescribed event (MEMBAR / RELEASE / barrier).
- **[[Multicore]] is just SMPs.** *"Multicore is extremely important these days. However, they are just SMPs, for the most part, and thus should not be treated differently."* A typical dual-core has shared L2, private L1, and interfaces the bus via L3.
- **Optimal thread count is application-dependent** (§3.9): I/O-bound apps want more threads than cores; purely-computational apps want at most one thread per core; lock-heavy apps want fewer; GPUs want very many (memory accesses are I/O-like).
- **[[ProcessorAffinity]] preserves caches across timeslices** (§3.10). Designate a preferred core per thread; OpenMP 3.1 supports this. Without it, cache contents get refreshed every time the OS migrates a thread.
- **[[SoftwareDSM]] (SDSM) sells the shared-memory illusion on message-passing hardware.** *"the shared-memory paradigm is believed to be the easier one to program in. Thus SDSM allows us to have 'the best of both worlds'."* Two flavors: **page-based** (clearer to program in; the chapter focuses on this) and **object-based**. Named systems: **Treadmarks** (Rice University, uses UDP), **[[JIAJIA]]** (Academy of Sciences, China). Mechanism: `mprotect` marks pages non-resident; a SIGSEGV signal handler implemented by the SDSM library performs network transactions to fetch the latest value before resuming.
- **SDSM cannot fake shared pointers.** Pointers store addresses; each SDSM node has its own address space, so a variable `Y` lives at a different address on each node and `int *P = &Y;` cannot have consistent semantics across nodes.
- **SDSM coherency transactions are larger than hardware ones.** *"In the hardware case we are dealing with cache blocks, with a typical size being 512 bytes. In the SDSM case, we are dealing with pages, with a typical size being 4096 bytes."* — 8× the granularity, so 8× the false-sharing surface.
- **[[JIAJIA]] case study (§3.11.2).** Four characteristics: **page-based, scope consistency, home-based, multiple writers**. API: `jia_alloc()`, `jia_init()`, `jia_barrier()`, `jia_lock()`, `jia_unlock()`, `jia_exit()`, magic variable `jiapid` for self-rank. Allows multiple writers per page (each node's writes are reconciled at the barrier via a **diff** computed against a saved **twin** copy — the chapter notes Treadmarks measured 167 μs per twin and 686 μs per diff). The worked example is Odd/Even Transposition Sort.
- **Barriers are tricky to implement correctly.** §3.12.1's use-once version (single `Count` variable + mutex + spin) works once but breaks on reset. §3.12.2's attempted reusable version race-conditions: a fast processor can race ahead, increment `Count` for iteration 2 *before* a slow processor resets it from iteration 1. §3.12.3's correct version uses **two `Count[2]` counters with an alternating `EvenOdd` parity bit** — the fast processor increments a *different* counter than the slow processor is resetting.
- **`pthread_cond_wait` replaces spinning with blocking** (§3.12.4.1). The condition variable lets the OS deschedule waiting threads; `pthread_cond_broadcast` wakes them all at the barrier release. Better than busy-spin, and with `cond_wait` a single `Count` suffices again.
- **[[TreeBarrier|Tree barriers]] (§3.12.4.2.1) parallelize the serial reduction.** For `n = 2^k` threads, build a log₂n-level binary tree of sub-barriers; level `i` has `n/2^i` sub-barriers of 2 threads each. Reduces the critical section's serial fan-in from `n` to `log n`.
- **[[ButterflyBarrier|Butterfly barriers]] (§3.12.4.2.2) generalize tree barriers via bit-flipping.** In phase `k`, node `i` shakes hands with node `i ⊕ 2^k` (bit-flip on bit `k`). After `log₂n` phases, every node has effectively exchanged with every other. *"Actually, a butterfly exchange amounts to a number of simultaneously tree operations."* Uses a global `ReachedBarrier[]` array; `pthread_cond_wait` or a busy loop guards each handshake.

## Key Quotes

> *"The term **shared memory** means that the processors all share a common address space."* — §3.1, p. 43. The chapter's foundational definition.

> *"parallel execution of a program requires, to a large extent, parallel accessing of memory. To some degree this is handled by having a cache at each CPU, but it is also facilitated by dividing the memory into separate **modules** or **banks**."* — §3.2, p. 44.

> *"Here, consecutive threads work on consecutive elements in **x**. That puts them in separate banks, thus no conflicts, hence speedy performance."* — §3.2.2, p. 46. The bank-conflict solution in a single sentence.

> *"Omega-networks amount to a compromise between buses and crossbars, and for this reason have become popular."* — §3.3.4, p. 54. The chapter's verdict on interconnection topology.

> *"And most importantly, these operations are done in an **atomic** manner; no bus transactions by other processors may occur between the two steps."* — §3.4.1, p. 55. The semantics of TAS in one line.

> *"we could do `lock inc total` without software locks!"* — §3.4.1.1, p. 56. The LOCK-prefix value proposition.

> *"Relying purely on TAS for interprocessor synchronization would be unthinkable: As each processor contending for a lock variable spins in the loop shown above, it is adding tremendously to bus traffic."* — §3.5.1, p. 58. Why caches must be added — and why coherency becomes necessary.

> *"This relation between these two is somewhat analogous to the relation between **write-back** and **write-through** protocols for caches in uniprocessor systems."* — §3.5.1, p. 59. The invalidate-vs-update analogy.

> *"This is the **false sharing** problem, alluding to the fact that the two variables are sharing a cache line even though they are not related."* — §3.5.3, p. 63. The cleanest single-sentence definition of false sharing.

> *"Though the word **consistency** in the title of this section may seem to simply be a synonym for **coherency** from the last section, and though there actually is some relation, the issues here are quite different. In this case, it is a timing issue."* — §3.6, p. 64. The coherency-vs-consistency distinction.

> *"Multicore is extremely important these days. However, they are just SMPs, for the most part, and thus should not be treated differently."* — §3.8, p. 67. Matloff's flattening of multicore into SMP.

> *"the shared-memory paradigm is believed to be the easier one to program in. Thus SDSM allows us to have 'the best of both worlds' — the convenience of the shared-memory world view with the inexpensive cost of some of the message-passing hardware systems."* — §3.11.1, p. 68. The SDSM thesis.

> *"Implementing a barrier in a fully correct manner is actually a bit tricky."* — §3.12, p. 73. The chapter's understated warning before three buggy attempts.

## Connections

- [[NormMatloff]] — author; this chapter cites his own *Computer Organization* PDF (heather.cs.ucdavis.edu/~matloff/50/PLN/CompOrganization.pdf) as the cache primer, and his JIAJIA tutorial at heather.cs.ucdavis.edu/~matloff/jiajia.html.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — Ch1 introduced [[SMP]] / [[NUMA]] / [[Multicore]] / [[CoherentCaches]] as forward-references; this chapter resolves them.
- [[parproc-ch02-recurring-performance-issues]] — Ch2's closing §2.8 forward-references "memory banks" and "cache-coherency overhead" to this chapter — both delivered here.
- [[SMP]] — §3.3.1 gives the bus + processors + memory-modules picture.
- [[NUMA]] — §3.3.2 — the per-PE local-bus + global-bus + router topology, with explicit *"Today almost all high-end MIMD systems are NUMAs."*
- [[Multicore]] — §3.8, framed as just-an-SMP.
- [[SharedMemoryArchitecture]] — the chapter's organizing paradigm.
- [[MemoryInterleaving]] — §3.2.1, high-order vs low-order disciplines.
- [[BankConflict]] — §3.2.2, the serialization pathology and the stride-1 fix.
- [[Crossbar]] — §3.3.3.1, $n^2$ pathways, Sun Enterprise 10000 16×16 example.
- [[OmegaNetwork]] — §3.3.3.2, the $\log_2 n$-depth multistage compromise.
- [[TestAndSet]] — §3.4.1, atomic primitive with bus arbitration.
- [[FetchAndAdd]] — §3.4.3 + §3.7 packet combining.
- [[CacheCoherency]] — §3.5.1, snoopy invalidate / update / directory.
- [[CoherentCaches]] — Ch1 stub now fleshed out.
- [[MESI]] — §3.5.2, Pentium's four-state machine.
- [[FalseSharing]] — §3.5.3, the cache-line ping-pong.
- [[MemoryConsistency]] — §3.6, sequential / release / scope models.
- [[ProcessorAffinity]] — §3.10, OS thread-to-core pinning.
- [[SoftwareDSM]] — §3.11, page-based vs object-based; Treadmarks + JIAJIA.
- [[JIAJIA]] — §3.11.2, the page-based scope-consistency multi-writer SDSM case study.
- [[Barrier]] — §3.12, finally with concrete implementations (Ch1's stub).
- [[TreeBarrier]] — §3.12.4.2.1.
- [[ButterflyBarrier]] — §3.12.4.2.2.
- [[Pthreads]] — `pthread_mutex_lock`, `pthread_cond_wait`, `pthread_cond_broadcast`, `pthread_barrier_wait` are the named API surfaces.
- [[OpenMP]] — §3.10 notes OpenMP 3.1 supports processor affinity.
- [[MPI]] — §3.11 names message-passing hardware (NOWs) as the SDSM substrate.
- [[Latency]] / [[Bandwidth]] — §3.3.4's scaling table reuses Ch2's vocabulary.
- [[LoadBalancing]] — §3.10's thread-pinning is a load-balancing knob via cache preservation.
- [[CriticalSection]] — repeatedly invoked as the structure guarded by TAS / LOCK / MESI / consistency-model operations.

## Contradictions

- **No contradictions with prior wiki content.** This chapter resolves forward-references rather than contradicting them: [[CoherentCaches]], [[NUMA]], [[SMP]], and [[Barrier]] were all introduced as stubs in Ch1, and Ch2 explicitly deferred bank conflicts and cache-coherency detail here; the substantive content arrives now as advertised.
- **Mild internal-to-the-book tension to flag for downstream chapters.** §3.8 declares multicore is *"just SMPs, for the most part"* — but §3.10 (processor affinity) and §3.5.3 (false sharing) are tools that matter much *more* on multicore than on the discrete-CPU SMPs the chapter describes pictorially in §3.3.1. The "just SMPs" framing is best read as a software-API claim, not a microarchitectural one.
- **Update for §3.6's Pentium aside.** The chapter states *"The recent Pentium models use Sequential Consistency."* — historically inaccurate as of the 2026 reading; x86-TSO (a relaxation of sequential consistency permitting store-buffer reordering) is the model documented by Intel since at least the mid-2000s. Not a wiki-internal contradiction (no current page asserts otherwise) but worth flagging if a future ingest covers x86 memory models more carefully.
