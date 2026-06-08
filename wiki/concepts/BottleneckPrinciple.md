---
title: "Bottleneck Principle"
type: concept
tags: [ml-systems, performance, mlsysbook, physics, foundations]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Bottleneck Principle

The companion to the [[IronLawOfMLSystems|iron law]]: where the iron law gives the *cost* of each term, the bottleneck principle identifies *which term matters*. Introduced in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

> ML systems are dominated by their slowest component: optimizing fast operations yields zero benefit while the slowest stage remains unchanged.

Modern accelerators **pipeline** execution — while computing on batch $n$, the memory system prefetches batch $n+1$ — so whichever operation is slower hides the faster one. This turns the iron law's *sum* into a *max*:

$$T_{bottleneck} = \max\left(\frac{D_{vol}}{\text{BW}},\ \frac{O}{R_{peak}\cdot\eta_{hw}},\ T_{network}\right) + L_{lat}$$

The decisive consequence: if a system is **memory-bound** ($D_{vol}/\text{BW} > O/(R_{peak}\cdot\eta_{hw})$), buying faster processors yields *exactly 0% speedup* — "like widening a six-lane highway when all traffic must funnel through a two-lane bridge." Engineers must identify the dominant term *before* optimizing. The dominant term varies by [[DeploymentSpectrum|paradigm]]: cloud training is compute-bound, cloud LLM inference and edge inference are memory-bandwidth-bound, mobile is energy-bound, TinyML is memory-capacity-bound.

The bottleneck principle is the operational form of [[AmdahlsLaw|Amdahl's Law]] for ML pipelines: a 10× faster model in a 200 ms pipeline (ML = 30%) yields only 1.37× end-to-end. Use the **additive** iron law for single-task latency; the **max** form for continuous-stream throughput.

## Connections

- [[IronLawOfMLSystems]] — the cost decomposition this principle prioritizes.
- [[AmdahlsLaw]] — the theoretical ceiling the bottleneck principle operationalizes.
- [[RooflineModel]] / [[ArithmeticIntensity]] — the diagnostic for compute-bound vs. memory-bound.
- [[WorkloadArchetype]] — archetypes are defined by which iron-law term binds.
- [[DeploymentSpectrum]] / [[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]] — each paradigm has a different dominant term.
- [[MemoryWall]] — why ML systems are more often memory-bound than compute-bound.
- [[mlsysbook-ch02-ml-systems]] — source.
