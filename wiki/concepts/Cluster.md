---
title: "Cluster (parallel computing)"
type: concept
tags: [parallel-computing, hardware, message-passing, network]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# Cluster

A set of independent computers networked together for use as a parallel processing system. [[parproc-ch01-intro-parallel-processing]]'s defining example of [[MessagePassingArchitecture]]: "one has a set of commodity PCs and networks them for use as a parallel processing system. The PCs are of course individual machines, capable of the usual uniprocessor (or now multiprocessor) applications, but by networking them together and using parallel-processing software environments, we can form very powerful parallel systems."

Key practical considerations from the chapter:
- **Network speed** matters disproportionately: "ordinary Ethernet and TCP/IP are fine for the applications envisioned by the original designers of the Internet, e.g. e-mail and file transfer, but is slow in the cluster context. A good network for a cluster is, for instance, [[Infiniband]]."
- **Recipe culture**: "clusters have become so popular that there are now 'recipes' on how to build them for the specific purpose of parallel processing." [[Beowulf]] is the canonical recipe name.
- **Setup tooling**: "software packages such as ROCKS (`http://www.rocksclusters.org/wordpress/`) have been developed to make it easy to set up and administer such systems."

Software targeting clusters typically uses [[MPI]] for explicit message passing, or higher-level abstractions like Hadoop/[[MapReduce]] or R's [[Snow]] for [[ScatterGather]] workloads.

Note: the chapter distinguishes its hardware-cluster sense from R `snow`'s software-cluster sense — `makePSOCKcluster(rep("localhost", 2))` constructs a *snow cluster* of R processes (which "may be running on different machines (i.e. a real cluster), or on a multicore machine, or a combination of the two") — the two senses overlap but are not synonyms.

## Connections
- [[parproc-ch01-intro-parallel-processing]] — introduces cluster hardware and the snow/cluster terminology overlap.
- [[Beowulf]] — commodity-PC cluster recipe.
- [[MessagePassingArchitecture]] — the architectural paradigm.
- [[MPI]] — canonical cluster programming layer.
- [[Snow]] — R's "software cluster" abstraction.
- [[Infiniband]] — high-bandwidth cluster interconnect.
- [[ScatterGather]] — dominant cluster programming pattern.
