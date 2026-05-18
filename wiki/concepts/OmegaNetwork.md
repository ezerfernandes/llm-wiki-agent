---
title: "Omega (Delta) Network"
type: concept
tags: [parallel-computing, hardware, interconnect, shared-memory]
sources: [parproc-ch03-shared-memory-parallelism]
last_updated: 2026-05-17
---

# Omega (Delta) Network

A multistage interconnection topology between $n = 2^k$ processors and $n$ memory modules, organized as $\log_2 n$ rows of $n/2$ 2×2 switches each. Cheaper than a [[Crossbar|crossbar]] but more parallel than a bus — *"Omega-networks amount to a compromise between buses and crossbars, and for this reason have become popular."* ([[parproc-ch03-shared-memory-parallelism|ParProcBook Ch3]] §3.3.3.2 / §3.3.4).

## Routing by destination-bit

Number the rows 0…log₂n−1 from the bottom; number switches and processing elements (PEs) left-to-right starting at 0; number bits in the destination address most-significant-first as 0,1,…,log₂n−1. At stage `i`, the switch routes the packet based on **bit `i` of the destination**: 0 → left output, 1 → right output.

Worked example for an 8×8 system: P2 reads from M5 = 101₂.
- Stage 0 reads bit 0 = 1 → right out → stage-1 node 3
- Stage 1 reads bit 1 = 0 → left out → stage-2 node 2
- Stage 2 reads bit 2 = 1 → right out → PE5
M5 then ships the read response back along the same path.

## General wiring formula

For $N = 2^n$ PEs, let $S_{ij}$ denote the switch at row $i$ (from bottom), column $j$ (from left). Output port $O_{ik}$ connects to input port $I_{jm}$ of the next row up, where $j = i+1$ and:

$$m = (2k + \lfloor 2k/N \rfloor) \mod N$$

The last row wraps back to the PEs: $O_{ik}$ → PE $k$.

## Scaling

- **Latency**: $O(\log_2 n)$
- **Bandwidth**: $O(n)$
- **Cost**: $O(n \log_2 n)$

## Weakness: clash at shared switches

Unlike a crossbar, an omega network does *not* guarantee $n$ simultaneous distinct-destination packets. *"If for example, PE0 wants to send to PE3, and at the same time PE4 wishes to sent to PE2, the two packets will clash at the leftmost node of stage 1, where the packet from PE0 will get priority."* One of the two must wait.

## Connections
- [[parproc-ch03-shared-memory-parallelism]] — §3.3.3.2.
- [[Crossbar]] — the more-expensive alternative.
- [[NUMA]] — typical deployment context.
- [[FetchAndAdd]] — §3.7's packet-combining optimization specifically targets omega-style multistage networks.
- [[SharedMemoryArchitecture]] — context.
- [[Latency]] / [[Bandwidth]] — the scaling axes.
