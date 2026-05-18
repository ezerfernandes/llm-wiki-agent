---
title: "Bandwidth"
type: concept
tags: [parallel-computing, networking, performance]
sources: [parproc-ch02-recurring-performance-issues]
last_updated: 2026-05-17
---

# Bandwidth

**The number of bits per unit time that can be input into a communications channel.** The second of the two independent dimensions of [[CommunicationBottleneck|communication delay]] in parallel systems; the first is [[Latency]].

## The chapter's definition

[[parproc-ch02-recurring-performance-issues]] §2.5:
> *"Bandwidth is the number of bits per unit time that can be input into the communications channel. This can be affected by factors such as bus width in a shared memory system and number of parallel network paths in a message passing system, and also by the speed of the links."*

## Bridge analogy

In [[NormMatloff]]'s recurring bridge analogy, bandwidth is the number of cars that can enter the bridge per unit time. You raise it by *"improving the speed by which toll takers can collect tolls, and increasing the number of toll booths."* You raise [[Latency|latency]] separately, by raising the speed limit on the bridge itself.

## What it depends on

| Platform | Bandwidth determined by |
|---|---|
| [[SharedMemoryArchitecture|Shared-memory]] | Bus width, number of memory channels, link speeds |
| [[MessagePassingArchitecture|Message-passing cluster]] | Number of parallel network paths; link bit-rate |
| [[GPU]] | Memory bus width to HBM/GDDR; PCIe lanes for host transfer |

## Bandwidth vs latency — when each is the bottleneck

- **Latency-bound**: small, frequent messages where the per-message setup cost dominates. Fix by batching, by [[LatencyHiding|hiding the latency]] behind useful work, or by reducing the number of messages.
- **Bandwidth-bound**: large bulk transfers where you saturate the channel. Fix by widening the channel, by adding parallel paths, or by reducing the total bytes moved (compression, locality, smarter algorithms).

## Connections

- [[parproc-ch02-recurring-performance-issues]] — primary source, §2.5.
- [[Latency]] — the orthogonal axis.
- [[CommunicationBottleneck]] — bandwidth is one of the two dimensions of this cost.
- [[LatencyHiding]] — the workaround for latency that doesn't help with bandwidth.
