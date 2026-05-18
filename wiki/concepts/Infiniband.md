---
title: "Infiniband"
type: concept
tags: [parallel-computing, networking, interconnect, message-passing, cluster, rdma]
sources: [parproc-ch01-intro-parallel-processing, parproc-ch07-message-passing-systems]
last_updated: 2026-05-17
---

# Infiniband

A high-performance switch-based interconnect designed for [[NetworkOfWorkstations|NOWs]] / [[Cluster|clusters]] — the standard answer to *"ordinary Ethernet and TCP/IP are too slow in the NOW context."* First mentioned in [[parproc-ch01-intro-parallel-processing|Ch1]] as *"a good network for a cluster is, for instance, Infiniband"*; full treatment in [[parproc-ch07-message-passing-systems|Ch7]] §7.3.1.

## Specs (per Ch7, circa 2010)

[[parproc-ch07-message-passing-systems]] §7.3.1: *"A popular network for a NOW today is Infiniband (IB) (www.infinibandta.org). It features low latency, about 1.0-3.0 microseconds, high bandwidth, about 1.0-2.0 gigaBytes per second, and uses a low amount of the CPU's cycles, around 5-10%."*

| Metric | Value (Ch7 era) |
|---|---|
| [[Latency]] | 1.0–3.0 μs |
| [[Bandwidth]] | 1.0–2.0 GB/s |
| CPU usage | 5–10% |
| Atomic-op latency | 3–5 μs |

(Contemporary IB — HDR / NDR variants — is many times faster on bandwidth; the Ch7 numbers are textbook-period baseline.)

## Architecture

Three load-bearing structural properties from [[parproc-ch07-message-passing-systems]] §7.3.1:

### 1. Switch-based fabric

*"The basic building block of IB is a switch, with many inputs and outputs, similar in concept to Ω-net. You can build arbitrarily large and complex topologies from these switches."* — the same multistage-switch idea Ch3 §3.3.3.1 introduced for shared-memory backplanes ([[OmegaNetwork]]) is reused here at NIC scale. Common topologies: fat-tree (most data centers), dragonfly (HPC), hypercube-of-switches (some Top500 systems).

### 2. RDMA — Remote Direct Memory Access

*"A central point is that IB, as with other high-performance networks designed for NOWs, uses **RDMA** (Remote Direct Memory Access) read/write, which eliminates the extra copying of data between the application program's address space to that of the operating system."*

RDMA's essence: the NIC reads/writes application memory directly, bypassing the OS-kernel copy. Two copies are eliminated:
- send-side: app buffer → kernel send buffer
- receive-side: kernel receive buffer → app buffer

This is the modern equivalent of the [[Hypercube|hypercube's dedicated link]] in one important sense — both bypass intermediate-buffer overhead — but realized via firmware on commodity NICs rather than custom interconnect hardware. The RDMA Consortium spec is at www.rdmaconsortium.org. Related tuned-MPI-on-IB research: `nowlab.cse.ohio-state.edu/publications/journal-papers/2004/liuj-ijpp04.pdf` (the MVAPICH origin paper).

### 3. Hardware-supported collectives + multicast

*"IB has high performance and scalable implementations of distributed locks, semaphores, collective communication operations. An atomic operation takes about 3-5 microseconds. IB implements true **multicast**, i.e. the simultaneous sending of messages to many nodes."*

Multicast is the load-bearing capability for collective operations. The chapter immediately warns about an MPI-portability gotcha:

> *"Note carefully that even though MPI has its **MPI_Bcast()** function, it will send things out one at a time unless your network hardware is capable of multicast, and the MPI implementation you use is configured specifically for that hardware."*

So **MPI_Bcast is not magic** — without IB-style hardware multicast and a matching MPI build, the operation is O(P) sequential point-to-point sends. This is the canonical example of the *"collectives have abstraction-level semantics but implementation-level cost"* warning that applies to all MPI collective operations.

## Why IB matters for clusters

[[parproc-ch07-message-passing-systems]] §7.3.1's framing: *"the network is literally the weakest link"* in a NOW. Ordinary Ethernet's per-message overhead (TCP/IP stack traversal, kernel-bypass copies, ~100 μs latency historically) dominates the actual compute work on per-message scales typical of MPI workloads. IB's 1–3 μs latency + RDMA + hardware collectives narrow the cluster-vs-supercomputer performance gap.

## Connections

- [[parproc-ch07-message-passing-systems]] — primary source (§7.3.1).
- [[parproc-ch01-intro-parallel-processing]] — first mention.
- [[NormMatloff]] — author.
- [[NetworkOfWorkstations]] — IB is the prescribed NOW interconnect.
- [[Cluster]] — same.
- [[Beowulf]] — same.
- [[MessagePassingArchitecture]] — the paradigm IB serves.
- [[MPI]] — the canonical user of IB; the MPI_Bcast-vs-hardware-multicast story lives at this boundary.
- [[OmegaNetwork]] — the conceptual template for IB's switch fabric (per Ch7 §7.3.1).
- [[Latency]] — IB's 1–3 μs is the textbook benchmark.
- [[Bandwidth]] — IB's 1–2 GB/s is the textbook benchmark.
- [[Hypercube]] — historical alternative; IB+RDMA achieves a similar copy-bypass property via commodity hardware.
