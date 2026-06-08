---
title: "Data Locality Invariant"
type: concept
tags: [ml-systems, deployment, edge, mlsysbook, physics]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Data Locality Invariant

A **binary feasibility test** that determines whether remote (cloud) offloading is architecturally viable: a workload must be processed locally whenever the time to transmit its data exceeds the time to process it remotely. From [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]):

$$\frac{D_{vol}}{\text{BW}_{network}} > L_{lat,network} + \frac{O}{R_{peak,remote}\cdot\eta_{hw,remote}}$$

When the left side dominates, the network pipe cannot deliver the data fast enough, so adding remote compute ($R_{peak}$) yields *zero* benefit — the only way to reduce latency is to move compute to the data. Unlike the [[IronLawOfMLSystems|iron law]] (which decomposes time additively for any workload), this is a *go/no-go* test applied *before* optimizing individual terms.

**Worked example:** a drone's 4K/60-FPS object-avoidance frame at 100 Mbps takes far longer to transmit than the ~110 ms cloud round-trip + compute budget. "The cloud could have an infinite processor and the drone would still crash because it cannot move the bits fast enough." Common pitfall: assuming 5G/6G "solves" locality — they raise bandwidth but cannot beat the [[SpeedOfLight|speed-of-light]] latency floor, so latency-critical tasks remain inherently local. This is the formal justification for [[EdgeML|Edge ML]] in bandwidth- or latency-bound deployments.

## Connections

- [[EdgeML]] — the paradigm this invariant mandates.
- [[IronLawOfMLSystems]] / [[BottleneckPrinciple]] — the additive cost model this binary test precedes.
- [[SpeedOfLight]] — the network-latency floor 5G/6G cannot lower.
- [[CloudML]] — the option the invariant rules out when transmit time dominates.
- [[mlsysbook-ch02-ml-systems]] — source.
