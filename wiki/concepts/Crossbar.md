---
title: "Crossbar Interconnect"
type: concept
tags: [parallel-computing, hardware, interconnect, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Crossbar Interconnect

A non-blocking interconnect topology providing $n^2$ dedicated pathways between $n$ processors and $n$ memory modules. Conceptually an $n \times n$ grid of switch nodes; *"E.g. for n = 8"* an 8×8 grid sits between the row of P0…P7 (bottom) and the column of M0…M7 (left). Each diamond-shaped switch has two inputs (bottom and right) and two outputs (left and top), with input-side buffers and a priority rule for output contention. ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.3.3.1).

## Routing

Packets carry source and destination addresses (e.g. 3-bit fields for an 8×8 system), the requested word offset within the module, and an R/W bit plus payload for writes. When a buffer fills, the design either blocks the upstream node or drops-and-retries. A symmetrical return network ships read responses back from memory to processor.

## Scaling

- **Latency**: $O(n)$ — packets traverse up to $n$ switches.
- **Bandwidth**: $O(n)$ — at peak, $n$ simultaneous source-to-distinct-destination packets can flow.
- **Cost**: $O(n^2)$ — the dominant term, set by the switch count.

## Strengths / weaknesses

**Strengths**: *"the crossbar's big advantage is that it is guaranteed that n packets can be sent simultaneously, providing they are to distinct destinations."* No clash if destinations differ.

**Weaknesses**: *"a crossbar is very expensive, and thus is dismissed out of hand in most modern systems."* Also has higher latency than buses under light load — *"an equally troublesome aspect of crossbars is their high latency value; this is a big drawback when the system is not heavily loaded."*

## Real-world example

The 16-CPU **Sun Microsystems Enterprise 10000** used a 16×16 crossbar. Useful in *some* small systems, dismissed for large-scale ones in favor of [[OmegaNetwork|omega-delta]] networks.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.3.3.1.
- [[OmegaNetwork]] — the cheaper $O(n \log n)$ multistage compromise.
- [[NUMA]] — both topologies appear in NUMA systems.
- [[SharedMemoryArchitecture]] — context.
- [[Latency]] / [[Bandwidth]] — the scaling axes.
