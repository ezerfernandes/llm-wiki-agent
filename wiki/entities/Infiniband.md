---
title: "InfiniBand"
type: entity
tags: [network, hardware, cluster, interconnect, stub]
sources: [parproc-ch01-intro-parallel-processing]
last_updated: 2026-05-17
---

# InfiniBand

High-bandwidth, low-latency switched-fabric interconnect commonly used in [[Cluster|cluster]] and HPC environments where Ethernet/TCP-IP performance is insufficient.

[[parproc-ch01-intro-parallel-processing]] flags InfiniBand as a representative example of the kind of fast network needed for serious cluster work: "ordinary Ethernet and TCP/IP are fine for the applications envisioned by the original designers of the Internet, e.g. e-mail and file transfer, but is slow in the cluster context. A good network for a cluster is, for instance, Infiniband."

## Connections
- [[parproc-ch01-intro-parallel-processing]] — cites InfiniBand as a fast cluster interconnect.
- [[Cluster]] / [[Beowulf]] — typical deployment context.
- [[MessagePassingArchitecture]] — the architectural setting where network speed is critical.
