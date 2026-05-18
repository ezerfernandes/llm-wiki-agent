---
title: "Beowulf cluster"
type: entity
tags: [cluster, parallel-computing, linux, commodity-hardware]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Beowulf

Term for "a cluster of PCs, usually with a fast network connecting them, used for parallel processing." The canonical recipe for building a [[Cluster]] from commodity hardware — originally a NASA-driven 1990s project that demonstrated that ordinary off-the-shelf machines plus Linux plus a fast interconnect could replace dedicated supercomputers for many scientific workloads.

[[parproc-ch01-intro-parallel-processing]] notes the term has become so well-established that "there are now 'recipes' on how to build them for the specific purpose of parallel processing." Mentioned software packages: **ROCKS** (`http://www.rocksclusters.org/wordpress/`), which "have been developed to make it easy to set up and administer such systems." A "good network for a cluster is, for instance, [[Infiniband]]" — ordinary Ethernet/TCP-IP is fine for email and file transfer but slow in the cluster context.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces Beowulf in the context of cluster hardware.
- [[Cluster]] — the general architectural category; Beowulf is its commodity-PC instantiation.
- [[MPI]] — the canonical message-passing layer on top of a Beowulf cluster.
- [[Infiniband]] — high-speed interconnect frequently used.
- [[MessagePassingArchitecture]] — the broader hardware paradigm.
