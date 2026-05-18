---
title: "Parallel Computing"
type: concept
tags: [systems, parallelism, performance, multicore, parallel-computing]
sources: [dis-0-introduction, parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Parallel Computing

The paradigm of using multiple processing units simultaneously to solve a computational problem. With [[MulticoreProcessor|multicore processors]] now the default across desktops, laptops, [[SingleBoardComputer|SBCs]], and smartphones, parallel computing has shifted from a specialty to a baseline skill ([[dis-0-introduction]]).

[[parproc-ch01-intro-parallel-processing]] organizes the field around a **three-motivation × three-architecture × three-worldview** taxonomy that complements the *Dive into Systems* baseline:

**Three motivations**: (1) **execution speed** — Matloff's primary focus; (2) **memory capacity** — applications too big for one machine; (3) **distributed processing** — data is physically dispersed and locality matters.

**Three hardware paradigms**: [[SharedMemoryArchitecture]] ([[SMP]] / [[Multicore]] / [[NUMA]] — usually [[MIMD]]), [[MessagePassingArchitecture]] ([[Cluster]] / [[Beowulf]]), and [[SIMD]] (historically ILLIAC and [[ThinkingMachines]]'s CM-1/2; today [[GPU|GPUs]]).

**Three programmer worldviews**: shared-memory threading ([[Pthreads]] / [[OpenMP]] / [[Rdsm]] / C++11 `std::thread`), message passing ([[MPI]] / [[Snow]]), and the [[ScatterGather]] manager-worker pattern that spans both.

Matloff's recurring caveat (Ch1, p. 3): "this is a common scenario — someone acquires a fancy new parallel machine, and excitedly writes a program to run on it, only to find that the parallel code is actually slower than the original serial version! This is due to lack of understanding of how the hardware works, at least at a high level." Parallel speedup is not free with parallel code; it requires algorithm/hardware co-design — which is why both *Dive into Systems* and *Programming on Parallel Machines* lead with hardware before software.

## Why [[DiveIntoSystems]] makes it part of the core curriculum

[[DiveIntoSystems]] Ch 0 lists parallel programming on multicore CPUs among the book's stated learning outcomes. The framing is operational: if the hardware exposes $N$ cores, single-threaded code leaves $(N-1)/N$ of the machine idle. Programmers who do not know how to parallelize cannot use the hardware they have.

## Distinctions to mind (forward references)

- **Parallelism vs. concurrency** — overlapping execution in time (concurrency) vs. simultaneous execution on different cores (parallelism).
- **Shared-memory vs. message-passing** — different cores share RAM (typical CPU) vs. communicating over a network.
- **Synchronization primitives** — mutexes, atomics, condition variables; the cost of coordinating cores.
- **[[DistributedComputing]]** — extending parallelism across machines.

The wiki also covers parallelism from the deep-learning side ([[d2l-computational-performance]] / [[DataParallelism]] / [[ModelParallelism]] / [[AutoParallelism]]); the *Dive into Systems* angle is the **CPU-multicore, C-program** view, which is upstream of all of those.

## Connections

- [[MulticoreProcessor]] — the hardware that motivates parallel computing today.
- [[ComputerSystem]] — context.
- [[DistributedComputing]] — the next scale up.
- [[d2l-computational-performance]] — the deep-learning take on parallel + distributed compute.
- [[dis-0-introduction]] — *Dive into Systems* baseline source.
- [[parproc-ch01-intro-parallel-processing]] — [[NormMatloff|Matloff]]'s textbook opening chapter; the 3×3×3 taxonomy summary above.
- [[SharedMemoryArchitecture]] / [[MessagePassingArchitecture]] / [[SIMD]] — three hardware paradigms.
- [[Pthreads]] / [[OpenMP]] / [[MPI]] / [[Snow]] / [[Rdsm]] / [[CUDA]] — software platforms.
- [[ScatterGather]] — cross-paradigm manager/worker pattern.
