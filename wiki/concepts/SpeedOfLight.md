---
title: "Speed of Light (Light Barrier)"
type: concept
tags: [ml-systems, physics, latency, networking, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Speed of Light (The Light Barrier)

The first of three physical constraints (with the [[PowerWall|power wall]] and [[MemoryWall|memory wall]]) that carve the [[DeploymentSpectrum|deployment spectrum]] into four paradigms in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]). The "light barrier" sets the **absolute, irreducible [[Latency|latency]] floor** for any networked computation:

$$L_{lat,min} = \frac{2\times\text{Distance}}{c_{fiber}} \approx \frac{2\times\text{Distance}}{200{,}000\ \text{km/s}}$$

where $c_{fiber}\approx200{,}000$ km/s is light in optical fiber (~two-thirds of vacuum speed, because light is slower in glass).

California→Virginia (~3,600 km) requires ~36 ms round-trip *before any computation begins*; real cloud services add 60–150 ms of software overhead. Applications needing sub-10-ms response *cannot* use distant cloud infrastructure — physics forbids it. A 1,500 km cloud datacenter gives a robotic-arm safety monitor a −5 ms deficit against a 10 ms budget. This constraint is *why* [[EdgeML|Edge ML]] and [[TinyML]] exist; 5G/6G improve bandwidth but cannot lower this floor.

## Connections

- [[MemoryWall]] / [[PowerWall]] — the other two physical constraints in the deployment framework.
- [[Latency]] — the quantity the light barrier floors.
- [[DataLocalityInvariant]] — the feasibility test that follows from the light barrier.
- [[EdgeML]] / [[CloudML]] — the latency floor forces edge deployment for sub-10-ms tasks.
- [[IronLawOfMLSystems]] — the $L_{lat}$ overhead term.
- [[mlsysbook-ch02-ml-systems]] — source.
