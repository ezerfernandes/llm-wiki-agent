---
title: "Thermal Throttling"
type: concept
tags: [ml-systems, mobile, hardware, power, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch12-benchmarking]
last_updated: 2026-06-05
---

# Thermal Throttling

The hardware/OS mechanism that **reduces clock speed (and thus performance) when a device approaches its thermal trip point**, to prevent overheating. The dynamic manifestation of the [[ThermalWall|thermal wall]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Throttling makes mobile ML performance a **time-varying constraint**, not a fixed value: a model running at 60 FPS may drop to 15 FPS within a minute as the [[MobileML|mobile]] SoC heats up, and an unoptimized 12 W workload hits the 80 °C trip in ~60 s and falls from 100 to 30 FPS. It reduces the effective hardware-utilization factor $\eta_{hw}$ in the [[IronLawOfMLSystems|iron law]]. Engineers who benchmark *peak* (burst) NPU throughput systematically overestimate *sustained* performance — one of the chapter's fallacies.

## Connections

- [[ThermalWall]] — the physical ceiling throttling enforces.
- [[MobileML]] — the paradigm where throttling binds.
- [[PowerWall]] / [[DennardScaling]] — the thermodynamic origin.
- [[IronLawOfMLSystems]] — throttling lowers $\eta_{hw}$.
- [[mlsysbook-ch12-benchmarking]] — Ch 12 makes throttling *the* reason edge [[Benchmarking|benchmarking]] is categorically different: Snapdragon 8 Gen 3 drops 45→20 TOPS, doorbell chips 30→15 FPS, datasheet "10 TOPS @ 0.5 W"→3 TOPS @ 2 W (13.3× efficiency gap); benchmarks shorter than 30 s are "functionally meaningless," so sustained (not burst) measurement is mandatory.
- [[mlsysbook-ch02-ml-systems]] — source.
