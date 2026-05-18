---
title: "ParProcBook Ch1: Introduction to Parallel Processing"
type: source
tags: [textbook, parallel-computing, openmp, mpi, cuda]
date: 2026-05-17
source_file: raw/parproc-matloff.pdf
---

# ParProcBook Ch1: Introduction to Parallel Processing

Opening chapter (pp. 1–30) of *Programming on Parallel Machines: GPU, Multicore, Clusters and More* by [[NormMatloff]] of [[UCDavis|UC Davis]]. The chapter sets up the entire book's hardware/software framing: three motivations for parallelism, the three dominant hardware architectures ([[SharedMemoryArchitecture|shared-memory]] / [[MessagePassingArchitecture|message-passing]] / [[SIMD]]), and three corresponding "programmer world views" walked through with the same running examples (prime sieve, matrix-vector multiply, sampling bucket sort).

## Summary
Matloff motivates parallel processing along three axes — execution speed, memory capacity, and distributed-data locality — then surveys the three canonical hardware platforms (shared-memory multiprocessors / [[SMP|SMP]] with [[Multicore|multicore]] as a degenerate case, message-passing clusters, and [[SIMD]] machines including [[GPU|GPUs]]). The matching software worldviews are introduced via worked examples: [[Pthreads]] (with a Sieve-of-Eratosthenes prime finder demonstrating [[CriticalSection|critical sections]] and [[Barrier|barriers]]), [[OpenMP]] (a [[SamplingBucketSort|sampling bucket sort]] showing `#pragma omp parallel/single/barrier`), [[MPI|MPI]] (a pipelined prime finder across cluster nodes), the [[ScatterGather]] paradigm, the R [[Snow]] package (matrix-vector multiply via `clusterApply`), and [[Rdsm]] (R's quasi-thread shared-memory interface). The chapter closes by foreshadowing [[NUMA]] and coherent caches as Chapter 3 material.

## Key Claims
- Three reasons to do parallel processing: **execution speed**, **memory capacity** (apps too big for one node), and **distributed processing** (data physically dispersed). Matloff's book focuses on speed.
- Parallel hardware partitions into two dominant patterns plus one historical/special-purpose pattern: **shared-memory ([[MIMD]])**, **message-passing** (clusters, [[Beowulf]]-style), and **[[SIMD]]** (lockstep — ILLIAC, [[ThinkingMachines|CM-1/CM-2]], DSPs, and most importantly today, [[GPU|GPUs]]).
- A [[SMP|Symmetric Multiprocessor (SMP)]] has processors P and memory modules M sharing a bus; **multicore is "effectively the same as SMP except processors are on one chip"**.
- Memory modules can be addressed by **high-order interleaving** (consecutive addresses in same module) or **low-order interleaving** (consecutive addresses across modules) — the latter spreads contention.
- Threads programming is the standard shared-memory model: a [[Thread]] is "a special case of an OS [[Process]]" but with shared memory by default. On a single-core machine, threads only simulate parallelism; on multicore they run genuinely concurrently.
- **A [[CriticalSection]] is always a potential bottleneck** because its code is "serial instead of parallel" — performance work often centers on coarsening it (e.g. processing five values of `nextbase` per lock acquisition instead of one).
- A **[[Barrier]]** is "a point in the code that all threads must reach before continuing"; `pthread_join` over all worker threads is a degenerate barrier; OpenMP exposes both implicit and explicit barriers.
- [[OpenMP]] is "a higher-level view of threading" — `#pragma omp parallel`, `#pragma omp single` (implicit barrier at end), `#pragma omp barrier`, `#pragma omp for`, `#pragma omp critical` — abstractions that "alleviate you of work and alleviate your code of clutter".
- Under [[MPI]] (message-passing), even shared logical state must be communicated explicitly via `MPI_Send`/`MPI_Recv` — there is no shared address space. MPI "translates" between heterogeneous (big/little-endian) CPUs automatically.
- **Pipelining** is a software analog of hardware pipelining: in the MPI prime-finder example, "each 'stage' in the pipe is a different computer" — node 0 emits odds, node 1 filters multiples of 3, node 2 filters multiples of 5, etc.
- The [[ScatterGather]] paradigm (a special case of message-passing) is "pervasive": a manager partitions work to workers, workers compute their chunks, results are combined back. Cited instances: MPI's scatter/gather functions, Hadoop/[[MapReduce]], and R's [[Snow]].
- R's `parallel` package (formed by merging the older `snow` and `multicore` libraries) uses scatter/gather; `makePSOCKcluster(rep("localhost", 2))` spawns R processes that "communicate via TCP/IP sockets" — they are independent processes with **no shared memory** (this is "a message-passing system, indeed").
- [[Rdsm]] adds a *quasi*-thread interface on top of `parallel` + `bigmemory` by **redefining R's `[` operator via operator overloading** to address shared memory; achieves genuine shared-memory access on top of independent R processes.
- Practical surprise: many algorithms are "just too complex to understand or express easily in C/C++", so a scripting language (R) with good parallelization is worthwhile alongside the lower-level systems.

## Key Quotes
> "Parallel machines provide a wonderful opportunity for applications with large computational requirements. Effective use of these machines, though, requires a keen understanding of how they work." — opening framing.

> "When he was at Apple in the 1980s, he was always worried that some other company would come out with a faster machine than his. But later at Pixar … he was always hoping someone would produce faster machines, so that he could use them!" — Steve Jobs anecdote on the speed motivation.

> "Until recently, shared-memory systems cost hundreds of thousands of dollars and were affordable only by large companies … but now multicore machines, in which two or more CPUs share a common memory, are commonplace in the home and even in cell phones!"

> "The terminology gets confusing here. Although each core is a complete processor, people in the field tend to call the entire chip a 'processor,' referring to the cores, as, well, cores. In this book, the term processor will generally include cores, e.g. a dual-core chip will be considered to have two processors." — footnote 1, p. 3; the book's convention on processor-vs-core terminology.

> "We are now in the era of Big Data, which requires Big Computation, thus again generating a major need for parallel processing." — p. 2.

> "The OpenMP library gives the programmer a higher-level view of threading. The threads are there, but rather hidden by higher-level abstractions." — p. 15.

> "A critical section is always a potential bottleneck in a parallel program, because its code is serial instead of parallel." — p. 11.

> "Note that R does allow functions defined within functions, which the locals and arguments of the outer function becoming global to the inner function." — p. 25, on R closure semantics in the `snow` `mmul` example.

## Connections
- [[NormMatloff]] — author; UC Davis statistics professor, also author of *The Art of R Programming*; the book reflects his R-and-systems-programming dual focus.
- [[UCDavis]] — author's institution; cited as a real-world shared-memory user (the Registrar's office runs online registration on an SMP).
- [[Pthreads]] — POSIX threads; the chapter's low-level shared-memory exemplar.
- [[OpenMP]] — higher-level pragma-based threading; the chapter's mid-level shared-memory exemplar.
- [[MPI]] — Message Passing Interface; the chapter's message-passing exemplar.
- [[CUDA]] — listed alongside OpenMP and MPI as a software platform the book covers; SIMD/GPU exemplar (full treatment in later chapters).
- [[Rlanguage]] — listed as the fifth software platform; scripting language with good parallelization features. Both [[Snow]] and [[Rdsm]] are R packages.
- [[Snow]] — R scatter/gather package; merged into base R's `parallel` library; used via `makePSOCKcluster`, `clusterApply`, `clusterExport`, `clusterEvalQ`.
- [[Rdsm]] — R "rthreads" library built on `snow` + `bigmemory`; achieves shared-memory via operator-overloading on `[`.
- [[SharedMemoryArchitecture]] — one of three hardware categories.
- [[MessagePassingArchitecture]] — second category.
- [[SIMD]] — third category; GPUs are the prominent modern instance.
- [[MIMD]] — Multiple Instruction Multiple Data; the standard shared-memory CPU model, contrasted with SIMD.
- [[SMP]] — Symmetric Multiprocessor; canonical shared-memory topology.
- [[Multicore]] — "effectively the same as SMP except all processors are on one chip".
- [[Cluster]] — networked commodity PCs as a parallel system; [[Beowulf]] is the canonical recipe.
- [[GPU]] — "today the most prominent example of SIMD"; shared-memory architecture but SIMD execution.
- [[CriticalSection]] — central shared-memory concurrency hazard; the chapter motivates locks via the Sieve-of-Eratosthenes example.
- [[Barrier]] — synchronization primitive; both Pthreads (`pthread_barrier_wait`) and OpenMP (`#pragma omp barrier`) examples are shown.
- [[Mutex]] — Pthreads' `pthread_mutex_lock`/`unlock` is the chapter's first concrete lock.
- [[Thread]] — a "special case of an OS process" with shared memory.
- [[SamplingBucketSort]] — the chapter's OpenMP example algorithm; forward-references the book's chapter 12.5.
- [[ScatterGather]] — pervasive manager-worker paradigm; instances cited include MPI scatter/gather, Hadoop/MapReduce, R snow.
- [[Beowulf]] — cluster-of-commodity-PCs recipe; ROCKS software stack is referenced for cluster setup.
- [[ParallelComputing]] — umbrella concept the chapter introduces.

## Contradictions
- None with existing wiki pages. The chapter introduces foundational parallel-computing terminology that does not directly contradict any of the ML/embedded-systems content already present. One minor terminological wrinkle: Matloff's footnote redefines "processor" to *include* cores, while [[CUDA]] / [[GPU]] wiki pages adopted the more recent convention where "processor" usually means the chip and "core" the execution unit — both conventions coexist in the literature, and Matloff flags the choice explicitly.
