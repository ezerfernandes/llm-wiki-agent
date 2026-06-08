---
title: "Edge ML"
type: concept
tags: [ml-systems, edge, deployment, mlsysbook]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Edge ML

ML systems that **bring computation closer to data sources** to reduce latency and bandwidth, occupying the middle of the [[DeploymentSpectrum|deployment spectrum]] between cloud and [[TinyML]] in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]).

Representative archetype: a Jetson-class robotics platform. **Mobile ML** is the adjacent variant (smartphones with 4–12 GB RAM, 1.5–3 GHz ARM cores, 2–5 W shared budgets; image classification at 100–500 mW and 10–100 ms vs. cloud servers at 200+ W and <1 ms). The binding constraint is often **latency** ($L_{lat}$): autonomous braking needs <10 ms end-to-end — at highway speed each extra millisecond adds ~3 cm of stopping distance — which is why latency-critical systems *cannot* offload to distant cloud servers regardless of their superior compute.

Edge deployment forces aggressive [[ModelCompression|model compression]], over-the-air (OTA) updates with bandwidth management and rollback, and (often) [[FederatedLearning|federated learning]] to keep data local for privacy. Hybrid designs (edge perception + cloud training, on-device wake-word + cloud NLP) are common.

[[mlsysbook-ch02-ml-systems|Ch 2]] separates Edge from [[MobileML|Mobile ML]]: edge is a *location* paradigm (gateways to on-premise servers, often plugged in with active cooling, ~100 W, 25–100 GB/s bandwidth limiting models to 100 MB–1 GB), whereas mobile adds a battery/thermal constraint. Edge eliminates the iron law's network-I/O term ($D_{vol}/\text{BW}_{IO}$). Two physical tests force edge processing: the **bandwidth bottleneck** (100 1080p cameras ≈ 18.7 GB/s overwhelms a 10 Gbps line ~15×; sending only metadata cuts it ~10,000×) and the **[[DataLocalityInvariant|data locality invariant]]** (data must stay local when transmit time exceeds remote processing time). Case studies: Tesla FSD, Amazon Go (>1 TB/hour/store), Industry 4.0 quality control (25–35% downtime reduction).

## Connections

- [[DeploymentSpectrum]] / [[SystemArchetype]] — edge/mobile tiers.
- [[TinyML]] — the more constrained neighbor.
- [[MobileML]] — the battery-bound sibling paradigm.
- [[DataLocalityInvariant]] — the binary feasibility test for local vs. remote processing.
- [[BottleneckPrinciple]] / [[IronLawOfMLSystems]] — edge inference removes the network-I/O term.
- [[FederatedLearning]] — privacy-preserving edge training.
- [[ModelCompression]] — the enabling discipline.
- [[Waymo]] / [[FarmBeats]] / [[Tesla]] / [[Amazon]] — edge/hybrid deployment case studies.
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] — sources.
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 details edge-AI operations: three-tier hierarchy (sensor mW / gateway W / cloud), OTA updates, designed-in graceful degradation (smoke-detector example).

