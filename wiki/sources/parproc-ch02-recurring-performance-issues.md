---
title: "ParProcBook Ch2: Recurring Performance Issues"
type: source
tags: [textbook, parallel-computing, performance, load-balancing]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch2: Recurring Performance Issues

Chapter 2 (pp. 31–42) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis]]. A short survey chapter — twelve pages, no platform-specific code beyond one [[OpenMP]] submatrix-extraction snippet — whose purpose is to install the vocabulary that the rest of the book will use to talk about *why parallel code is slow*. Opens with Matloff's signature aphorism — *"Oh no! It's actually slower in parallel!"* — and proceeds to taxonomize the recurring culprits: communication bottlenecks, [[LoadBalancing|load balancing]], static-vs-dynamic task assignment, [[Latency|latency]] / [[Bandwidth|bandwidth]], and the shared-memory-vs-message-passing tradeoff first surveyed in [[parproc-ch01-intro-parallel-processing|Chapter 1]].

## Summary

Matloff frames every parallel-performance pathology as some flavor of communication overhead. On shared-memory machines the cost is contention plus [[CoherentCaches|cache-coherency]] traffic; on a cluster it is network latency; on a [[GPU]] it is both CPU↔GPU transfer and intra-device memory contention. He then connects communication to [[LoadBalancing|load balancing]] via the [[EmbarrassinglyParallel]] discussion: an algorithm is "embarrassingly parallel" in the *modern* sense (his words: the meaning has *drifted*) when it has **low communication needs**, not merely when it's easy to decompose. The chapter's central, slightly counterintuitive thesis — given as the title of §2.4 — is that **static (but possibly randomized) task assignment typically beats dynamic** ([[WorkStealing|work stealing]], [[OpenMP]] `dynamic` / `guided` schedules, task farms). A back-of-envelope calculation with i.i.d. task times $T_i$ shows the coefficient of variation of chunk time falls as $O(1/\sqrt{m})$, so for large chunks the imbalance disappears and the communication cost of dynamic schedulers stops paying for itself. The argument is empirically backed by a Mandelbrot timing table (`static` 47.8s vs `random` 15.7s vs `dynamic` 21.4s vs `guided` 29.6s on an 8000×8000 grid) showing that *randomized static* — Method A' — wins. Side discussions cover [[Latency|latency hiding]] on GPUs, the shared-vs-message-passing scalability question (now scrambled by the GPU's demonstration of "extremely good scalability with shared-memory"), and a brief callout to [[MemoryAllocation|`malloc`/`new`]] overhead.

## Key Claims

- **Communication is always a potential bottleneck** — *"Whether you are on a shared-memory, message-passing or other platform, communication is always a potential bottleneck"*. Shared-memory has bus / cache-coherency contention, clusters have network latency (*"even a very fast network is very slow compared to CPU speeds"*), GPUs have both slow CPU↔GPU transfer and on-device contention.
- **Load balancing is the single most central performance issue** — *"Arguably the most central performance issue is load balancing, i.e. keeping all the processors busy as much as possible."*
- **The Mandelbrot example as a load-balance failure cautionary tale**: Darryl Gove's two-thread Mandelbrot code (left-half / right-half split) was extremely imbalanced because **most Mandelbrot points are in the left half of the picture**, and points in-the-set require many iterations while points out-of-the-set bail out quickly. The right-half thread was therefore *"very often idle"*.
- **Embarrassingly parallel has two meanings**. Old meaning: the problem decomposes so obviously that there is no intellectual challenge ("no shame in having one — except for showoff academics"). New, dominant meaning: **the algorithm has low communication needs**. Under the new meaning, a problem can be *embarrassingly easy to write* but *not embarrassingly parallel* — Matloff cites his own prime-finder from §1.5.1, which is trivially decomposable but has heavy lock + global-array communication and so does *not* qualify. Mandelbrot, by contrast, qualifies under both meanings.
- **Iterative algorithms with a rendezvous per iteration are usually NOT embarrassingly parallel** — unless the per-iteration granularity is so coarse that the rendezvous overhead vanishes. *"But unless the granularity of the problem is coarse, i.e. there is a large amount of work to do in each iteration, the communication overhead will be significant."*
- **Static task assignment typically beats dynamic** (the chapter's headline claim, §2.4). Static = decide at the outset which processor handles which tasks; dynamic = let processors pull tasks from a shared task farm / work queue as they finish.
- The "obvious" intuition that dynamic is better because it's more flexible is wrong because **accessing the task farm itself entails communication costs**, which on shared-memory means lock contention on the shared `nextchunk` counter (Matloff parenthetically reminds the reader this counts as communication: *"in shared-memory programming, the threads communicate through shared variables"*).
- **Mathematical justification**: Treat the per-task times $T_1, ..., T_m$ in a chunk as i.i.d. random variables. Then $E[T_1+...+T_m] = m E[T_1]$, $\text{Var}[T_1+...+T_m] = m \text{Var}[T_1]$, so $\sigma / \mu \sim O(1/\sqrt{m})$. For large chunks the chunk's total runtime is essentially constant, meaning **there's essentially no load imbalance under static assignment** — provided the i.i.d. assumption holds.
- **When the i.i.d. assumption fails — Mandelbrot revisited.** Tasks in a chunk aren't independent: if one point is in the set, its neighbors probably are too. So Method A (chunk-the-rows-contiguously) does *fail* on Mandelbrot. The fix is **Method A'**: randomize. Generate a random permutation $i_0, ..., i_{n-1}$ of row indices and assign thread $k$ rows $i_{1000k}, ..., i_{1000k+999}$. Randomization restores the i.i.d. property *at chunk level*.
- **Mutual web outlinks example**: For computing average mutual outlinks across all $\binom{n}{2}$ pairs of vertices, a naïve split of the outer `i` loop creates a real load-balance problem (the inner `j` loop runs from `i+1` to `n-1`, so thread 0 has way more work than thread 8). The fix is **pairing**: thread 0 handles rows `0..499` and `9500..9999`, thread 1 handles `500..999` and `9000..9499`, etc. Method A still wins — just with a smarter chunking pattern.
- **[[WorkStealing|Work stealing]]** (used by [[Cilk]]): an idle thread "raids" the work queue of another thread. Matloff is mildly skeptical — *"Needless to say, accessing the other work queue is going to be expensive in terms of time and memory contention overhead."*
- **OpenMP scheduling policies operationalize the static/dynamic spectrum**: `static` (pre-assigned chunks, no runtime communication), `dynamic` (shared atomic counter — better balance, more contention), `guided` (chunk size shrinks over time — low communication early, low imbalance late). Plus `random` as Matloff's preferred Method A' variant.
- **Mandelbrot timing table (8000×8000 grid, 4 cores × 2 threads = 8 threads, shared memory)**:
  - `static`: 47.8 s
  - `dynamic`: 21.4 s
  - `guided`: 29.6 s
  - `random`: 15.7 s ← *Method A' wins by 26% over the next-best policy.*
- **[[Latency|Latency]] vs [[Bandwidth|bandwidth]]** are *two* dimensions of communication delay, not one. Latency = time for one bit to travel; bandwidth = bits per unit time the channel can carry. Bridge analogy: latency is the time for one car to cross, bandwidth is the cars-per-unit-time the toll booths process. They are *independently* tunable — speed limit (latency) vs number of toll booths (bandwidth).
- **Latency hiding**: keep many long-latency operations in flight simultaneously so that completed ones become available while later ones are still waiting. GPUs do this aggressively — many pending memory accesses overlap with compute.
- **Shared-memory vs message-passing tradeoff** (§2.6, an updated revisit of [[parproc-ch01-intro-parallel-processing|Ch1]]'s framing): the community consensus is that **shared-memory is easier to write, debug, and maintain** (cites R. Chandra, *Parallel Programming in OpenMP*, MKP 2001). But message-passing can be faster for some algorithms (Odd/Even Transposition Sort is the example — would create a shared-memory bottleneck). The "scalability" claim — that message-passing scales to more nodes — is **now scrambled by the GPU**, which demonstrates *"extremely good scalability with shared-memory."* Most people don't have access to large multicore but do have access to cloud-based message-passing, so message-passing matters even for shared-memory partisans. *"Hybrid systems are common, in which a number of shared-memory systems are tied together by, say, MPI."*
- **[[MemoryAllocation|Memory allocation]] is itself a performance issue**: `malloc()` / C++'s `new` are *"very expensive in time"*. Large allocations trigger cache misses and page faults. Use static arrays where possible; otherwise tune `malloc` call frequency.
- **Shared-memory hazards forward-referenced** (§2.8): memory is divided into **banks** — concurrent access to the same bank is *serialized* by hardware; per-processor caches require coherency overhead. Both topics deferred to Ch3.

## Key Quotes

> *"Oh no! It's actually slower in parallel!—almost everyone's exclamation the first time they try to parallelize code."* — Chapter 2 epigraph, the most-quoted Matloff aphorism.

> *"Arguably the most central performance issue is load balancing, i.e. keeping all the processors busy as much as possible. This issue arises constantly in any discussion of parallel processing."* — p. 32, opening of §2.2.

> *"In recent years, the term **embarrassingly parallel** has drifted to a somewhat different meaning. Algorithms that are embarrassingly parallel in the above sense of simplicity tend to have very low communication between processes, key to good performance. That latter trait is the center of attention nowadays, so the term **embarrassingly parallel** generally refers to an algorithm with low communication needs."* — p. 33, §2.3.1. The terminology-drift remark is the clearest single-sentence statement of the modern meaning.

> *"It would at first seem that dynamic assignment is more efficient, as it is more flexible. However, accessing the task farm, for instance, entails communication costs, which might be very heavy. In this section, we will show that it's typically better to use the static approach, though possibly randomized."* — p. 34, §2.4 thesis statement.

> *"run time for a chunk is essentially constant if m is large, and there is essentially no load imbalance in Method A."* — p. 36, the punchline of the $O(1/\sqrt{m})$ argument.

> *"There is another variation to Method A that is of interest today, called **work stealing**. Here a thread that finishes its assigned work and has thus no work left to do will 'raid' the work queue of some other thread. This is the approach taken, for example, by the elegant [[Cilk]] language. Needless to say, accessing the other work queue is going to be expensive in terms of time and memory contention overhead."* — p. 38, §2.4.4. The chapter's only mention of Cilk.

> *"Latency is the time it takes for one bit to travel for source to destination, e.g. from a CPU to memory in a shared memory system, or from one computer to another in a cluster. Bandwidth is the number of bits per unit time that can be input into the communications channel."* — p. 39–40, §2.5, the canonical definitions.

> *"It's helpful to think of a bridge, with toll booths at its entrance. Latency is the time needed for one car to get from one end of the bridge to the other. Bandwidth is the number of cars that can enter the bridge per unit time."* — p. 40, the bridge analogy that the rest of the book reuses.

> *"There used to be a belief that message-passing was more **scalable**, i.e. amenable to very large systems. However, GPU has demonstrated that one can achieve extremely good scalability with shared-memory."* — p. 40–41, §2.6, scrambling the conventional wisdom.

## Connections

- [[NormMatloff]] — author; this chapter cites his own paper *"Efficient Parallel R Loops on Long-Latency Platforms"* (Rice University, June 2012) as the deeper treatment of the $O(1/\sqrt{m})$ argument.
- [[UCDavis]] — author's institution.
- [[parproc-ch01-intro-parallel-processing]] — preceding chapter; this chapter assumes the three-architectures framing and the prime-finder / matrix-vector-multiply running examples.
- [[LoadBalancing]] — the chapter's central concept; both §2.2 and §2.4.2 are titled around it.
- [[CommunicationBottleneck]] — §2.1's framing.
- [[EmbarrassinglyParallel]] — §2.3, with the old-vs-new meaning distinction.
- [[IterativeAlgorithms]] — §2.3.2.
- [[StaticTaskAssignment]] — §2.4's preferred approach.
- [[DynamicTaskAssignment]] — §2.4's foil; includes task farms, work queues, OpenMP's `dynamic` schedule.
- [[WorkStealing]] — §2.4.4; the [[Cilk]] approach.
- [[Cilk]] — cited by name as the canonical work-stealing language.
- [[MatrixVectorMultiply]] — the chapter's running task-assignment example.
- [[Latency]] — §2.5 definition.
- [[Bandwidth]] — §2.5 definition.
- [[LatencyHiding]] — §2.5 closer; GPU-style technique.
- [[Mandelbrot]] — §2.2's running load-balance example, drawn from Darryl Gove's *Multicore Application Programming: for Windows, Linux and Oracle Solaris* (Addison-Wesley, 2011), Chapter 7.
- [[OpenMP]] — concrete pragma examples: `#pragma omp for schedule(guided)`, the `static` / `dynamic` / `guided` policies, the submatrix-extraction code listing.
- [[CoherentCaches]] — §2.1 names cache-coherency transactions as the shared-memory communication cost; §2.8 forward-references Ch3 for detail.
- [[SharedMemoryArchitecture]] — §2.6 comparison.
- [[MessagePassingArchitecture]] — §2.6 comparison.
- [[GPU]] — §2.1, §2.5, §2.6; recurring example of latency hiding and of shared-memory scalability.
- [[MPI]] — named in §2.6 as the hybrid-system glue tying shared-memory nodes together in clouds.
- [[MemoryAllocation]] — §2.7 brief discussion of `malloc` / `new` overhead and the static-arrays workaround.

## Contradictions

- **Scalability of shared-memory vs message-passing.** §2.6 explicitly retracts what Matloff calls the historical community consensus that message-passing scales better, citing GPUs as a counterexample. This is not a contradiction with [[parproc-ch01-intro-parallel-processing|Ch1]] — Ch1 didn't take a position — but it is a deliberate updating of conventional wisdom worth flagging for downstream chapters that might assume the older framing.
- **Dynamic-is-better-because-flexible intuition.** Matloff explicitly calls this *wrong* on p. 34, then proves the static case mathematically. This contradicts the default cultural assumption in some scheduler / Cilk-adjacent literature where work-stealing is presented as the obvious right answer. The chapter does not name a specific contradicting wiki page — no current wiki page asserts dynamic-is-better — but readers coming from a [[Cilk]]-style background should note the framing inversion.
- **The 1.5.1 prime-finder is "embarrassingly parallel".** Many introductory presentations would call the [[parproc-ch01-intro-parallel-processing|Ch1]] Sieve-of-Eratosthenes example embarrassingly parallel. §2.3.1 explicitly disqualifies it under the *new* meaning, because of lock + global-array communication. Worth being precise about going forward.
