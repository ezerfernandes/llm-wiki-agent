---
title: "Dive into Systems — Ch 15.2 Distributed Memory Systems"
type: source
tags: [dive-into-systems, textbook, parallel-programming, distributed-memory, mpi, cluster]
date: 2026-05-18
source_file: https://diveintosystems.org/book/C15-Parallel/distrmem.html
---

## Summary

**Second leaf of Ch 15** *Looking Ahead: Other Parallel Systems* of *[[DiveIntoSystems]]* — pivots from [[dis-15-1-gpu|Ch 15.1's]] heterogeneous-CPU+GPU framing into the **[[Cluster|cluster]] / distributed-memory** parallelism arc. Codifies *"A collection of computers working together is known as a **distributed memory system**"* — the response to physical CPU-core limits (≈64 cores in commercial servers): scale **out** across multiple autonomous machines connected by a network rather than scale **up** within a single shared-memory box. Each node has its own private [[ProcessAddressSpace|address space]]; coordination requires **explicit [[MessagePassing|message passing]]** instead of shared-memory reads/writes. [[MPI]] (Message Passing Interface) is the standardized C/C++/Fortran library — each process gets a unique **rank** (0 to N−1) within an [[MPICommunicator|communicator]]; point-to-point primitives [[MPISend|`MPI_Send`]] / [[MPIRecv|`MPI_Recv`]] plus collectives [[MPIBcast|`MPI_Bcast`]] / [[MPIScatter|`MPI_Scatter`]] / [[MPIGather|`MPI_Gather`]] / [[MPIReduce|`MPI_Reduce`]] / [[MPIAllreduce|`MPI_Allreduce`]] / [[MPIBarrier|`MPI_Barrier`]] / [[MPIAllgather|`MPI_Allgather`]] handle communication. **142nd ingested DIS chapter.**

## Key Claims

- **Scale-out beyond single-machine limits** — *"A collection of computers working together is known as a **distributed memory system**."* Combines multiple independent computers (each with own CPU + memory) to overcome the ≈64-core ceiling of commercial servers.
- **Message-passing as the communication model** — Processes coordinate **exclusively through explicit message passing**, not shared memory; formal protocols are needed to avoid [[Deadlock|deadlock]] and ensure correctness.
- **MPI process ranking** — *"MPI allows a programmer to divide an application into multiple processes. It assigns each of an application's processes a unique identifier, known as a **rank**, which ranges from 0 to N-1."* Ranks enable selective communication targeting and serve as the **portable abstraction** across heterogeneous hardware.
- **Boss/worker pattern** — Boss distributes divisible work, workers process independently in parallel, then results aggregate — *"Because each worker gets a unique subset of the array, they can execute independently, in parallel, without the need to communicate."* Exemplified by scalar multiplication across array segments.
- **Collective-operation efficiency** — Functions like [[MPIScatter|`MPI_Scatter`]] and [[MPIGather|`MPI_Gather`]] enable single-call distributed operations while signaling intent to MPI implementations for potential hardware-level optimizations (e.g., network-fabric broadcast support).
- **Blocking semantics and implicit synchronization** — [[MPIRecv|`MPI_Recv`]] blocks execution until data arrives, creating implicit synchronization points; workers cannot proceed until the boss sends work assignments. (Compare [[NonblockingComm|non-blocking `Isend`/`Irecv`]] surveyed in [[parproc-ch04-distributed-memory-mpi|ParProc Ch 4]].)
- **Fault independence** — Unlike [[SharedMemoryParallelism|shared-memory]] systems where one component's failure disables the whole machine, distributed nodes fail **independently** — better isolation, but introduces fault-tolerance coordination challenges.
- **Network clock skew** — Autonomous nodes lack synchronized clocks, so message **ordering** determination is difficult due to unpredictable network transmission delays — the structural cause of much distributed-systems theory (Lamport timestamps, vector clocks etc.) the chapter merely names.

## Key Quotes

> *"A collection of computers working together is known as a **distributed memory system**."*

> *"MPI allows a programmer to divide an application into multiple processes. It assigns each of an application's processes a unique identifier, known as a **rank**, which ranges from 0 to N-1."*

> *"Because each worker gets a unique subset of the array, they can execute independently, in parallel, without the need to communicate."*

## Connections

- [[DiveIntoSystems]] — parent textbook; **second leaf of Ch 15** *Looking Ahead: Other Parallel Systems*.
- [[Cluster]] / [[DistributedComputing]] / [[MessagePassingArchitecture]] / [[MessagePassing]] — the substrate this chapter introduces.
- [[MPI]] / [[MPICommunicator]] / [[MPISend]] / [[MPIRecv]] / [[MPIBcast]] / [[MPIScatter]] / [[MPIGather]] / [[MPIReduce]] / [[MPIAllreduce]] / [[MPIBarrier]] / [[MPIAllgather]] / [[BufferingMPI]] / [[NonblockingComm]] — the entire [[ParallelProcessorsAlgorithms|ParProc Ch 4]] MPI corpus this chapter reuses; ParProc gives canonical depth, DIS gives the introductory framing.
- [[SharedMemoryParallelism]] / [[SharedMemoryIPC]] — the **alternative** parallelism substrate the chapter contrasts itself against.
- [[ConcurrencyVsParallelism]] / [[ParallelSpeedup]] / [[AmdahlsLaw]] / [[WeakScaling]] / [[StrongScaling]] — Ch 14's performance lenses now applied to distributed-memory work.
- [[dis-15-1-gpu]] — predecessor leaf; **alternative accelerator substrate** ([[CUDA]] / [[GPU]]).
- [[dis-15-3-exascale]] — successor leaf; the largest-scale distributed-memory systems ([[ExascaleComputing|exascale supercomputers]] + cloud-scale data centers).
- [[DistributedTraining]] / [[NCCL]] — the deep-learning sibling: [[NCCL]] is GPU-fabric-aware MPI for [[DistributedTraining|distributed deep-learning training]].

## Contradictions

None — DIS Ch 15.2 is the **textbook introductory framing** of distributed-memory programming; consistent with the deeper [[parproc-ch04-distributed-memory-mpi|ParProc Ch 4]] treatment.

## Notes

- **142nd ingested DIS chapter.**
- **Reuses extensively** from ParProc Ch 4 MPI corpus: [[MPI]], [[MPISend]], [[MPIRecv]], [[MPIBcast]], [[MPIScatter]], [[MPIGather]], [[MPIReduce]], [[MPIAllreduce]], [[MPIBarrier]], [[MPIAllgather]], [[MPICommunicator]], [[BufferingMPI]], [[NonblockingComm]], [[MessagePassing]], [[MessagePassingArchitecture]], [[Cluster]], [[DistributedComputing]].
- **No new concept pages** — pure reuse of the ParProc + Ch 13.4 IPC corpus.
