---
title: "Network of Workstations (NOW)"
type: concept
tags: [parallel-computing, hardware, message-passing, cluster, commodity-hardware]
sources: [parproc-ch07-message-passing-systems]
last_updated: 2026-05-17
---

# Network of Workstations (NOW)

The **commodity-PC** answer to the message-passing-hardware problem: take ordinary uniprocessor (or multiprocessor) PCs and network them together for use as a parallel processing system. [[parproc-ch07-message-passing-systems]] §7.3: *"The idea here is simple: Take a bunch of commodity PCs and network them for use as parallel processing systems. They are of course individual machines, capable of the usual uniprocessor, nonparallel applications, but by networking them together and using message-passing software environments such as MPI, we can form very powerful parallel systems."*

The NOW emerged as the economic answer to two problems: (a) [[Hypercube|hypercubes]] were *"too expensive for the type of performance they could achieve, and the market was small anyway"*, and (b) shared-memory hardware was *"extremely expensive, with a typical system costing hundreds of thousands of dollars"*. *"The networking does result in a significant loss of performance, but the price/performance ratio in NOW can be much superior in many applications to that of shared-memory or hypercube hardware of comparable number of CPUs."*

## Terminology hierarchy: NOW → Beowulf → Cluster

[[parproc-ch07-message-passing-systems]] §7.3.2 retires NOW as a term:

> *"NOWs have become so popular that there are now 'recipes' on how to build them for the specific purpose of parallel processing. The term **Beowulf** come to mean a NOW, usually with a fast network connecting them, used for parallel processing. The term NOW itself is no longer in use, replaced by **cluster**."*

So the three names refer to the same hardware today; **cluster** is the contemporary umbrella, **Beowulf** the recipe name (a NOW + a fast network + a build recipe), **NOW** the older academic phrase that the field has migrated away from. For wiki cross-link purposes:

- [[Cluster]] — contemporary umbrella term.
- [[Beowulf]] — the recipe / packaged variant.
- **NOW** — this page; the historical / academic term.

## "The network is literally the weakest link"

[[parproc-ch07-message-passing-systems]] §7.3.1's titular slogan. Without a fast interconnect, the NOW's price/performance ratio collapses:

> *"Still, one factor which can be key to the success of a NOW is to use a fast network, both in terms of hardware and network protocol. Ordinary Ethernet and TCP/IP are fine for the applications envisioned by the original designers of the Internet, e.g. e-mail and file transfer, but they are slow in the NOW context."*

The chapter's prescribed answer is **[[Infiniband]]** — switch-based fabric, RDMA-enabled, with 1–3 μs latency and 1–2 GB/s bandwidth (circa 2010 numbers; contemporary IB is much faster). Other high-performance interconnects designed for the NOW context include Myrinet, Quadrics, and contemporary Cray-Aries / Slingshot fabrics — all of which use the same RDMA + switch-fabric design template Ch7 ascribes to IB.

## Modern hybrid NOWs

[[parproc-ch07-message-passing-systems]] §7.3.2: *"Increasingly today, the workstations themselves are multiprocessor machines, so a NOW really is a hybrid arrangement."* Two programming styles:

- **Pure message-passing** — e.g. *"running eight MPI processes on four dual-core machines"*. Every process talks via `MPI_Send`/`MPI_Recv` regardless of physical co-location. Simpler model.
- **Hybrid MPI + shared-memory** — *"a shared-memory approach being used within a workstation but message-passing used between them."* Canonical realization is **MPI + [[OpenMP]]**: one MPI process per node, each spawning an OpenMP thread team that uses the node's shared memory. Higher complexity but can yield better performance when intra-node memory traffic dominates inter-node bandwidth.

## Cluster software ecosystem

Software for NOW administration / job management:

- **ROCKS** — `http://www.rocksclusters.org/wordpress/` — *"have been developed to make it easy to set up and administer such systems."* The named example in [[parproc-ch07-message-passing-systems]].
- **MPI implementations** — Open MPI, MPICH, MVAPICH (the IB-tuned variant referenced in Ch7's `nowlab.cse.ohio-state.edu/publications/journal-papers/2004/liuj-ijpp04.pdf` paper).
- **Schedulers** — Slurm, PBS, SGE — not in Ch7 but the obvious next layer.

## Communication-cost characterization vs hypercube

[[parproc-ch07-message-passing-systems]] §7.2.1 contrasts the two substrates explicitly:

| Property | [[Hypercube]] | NOW |
|---|---|---|
| Topology | Structured d-cube ($D = 2^d$ PEs, d neighbors each) | Whatever the network gives you (typically a switched fabric) |
| Per-link nature | Dedicated point-to-point | Shared medium (Ethernet) or switch-mediated (IB) |
| Max hops | d = $\log_2 P$ | Topology-dependent (often O(1) for switched, O(P) for shared Ethernet broadcast collisions) |
| Programmability | Bit-flip neighbor structure exploitable in algorithms | Flat — algorithms assume any-to-any costs the same |
| Status | Commercially extinct | Dominant |

## Connections

- [[parproc-ch07-message-passing-systems]] — primary source (§7.3).
- [[NormMatloff]] — author.
- [[MessagePassingArchitecture]] — the paradigm NOWs realize.
- [[Cluster]] — the contemporary name for the same hardware.
- [[Beowulf]] — the recipe-style NOW.
- [[Hypercube]] — the older (extinct) alternative substrate; Ch7 contrasts the two.
- [[Infiniband]] — the prescribed NOW interconnect.
- [[MPI]] — the canonical NOW programming layer.
- [[OpenMP]] — the intra-node companion in the hybrid programming model.
- [[ScatterGather]] — the dominant higher-level paradigm running on top of MPI / NOWs.
- [[Snow]] — R's NOW-style message-passing package.
- [[MapReduce]] — also runs on NOW substrates.
- [[parproc-ch01-intro-parallel-processing]] — Ch1's [[Cluster]] introduction; this page is the deeper Ch7 reframe.
