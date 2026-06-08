---
title: "Thermal Wall"
type: concept
tags: [ml-systems, mobile, hardware, power, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Thermal Wall

The **hard physics ceiling on sustained power consumption** in a passively-cooled device, independent of battery capacity. A central mobile constraint in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Every watt of computation becomes a watt of heat. A data center removes it with massive cooling; a thin, sealed, fanless [[MobileML|mobile]] device can only dump heat through its glass/metal casing — capping sustained power at ~2–5 W. The thermal wall is distinct from (and harder than) the **battery tax**:

- *Battery tax* = a **budget** problem (total operations per charge, $O$ over time) — solvable by duty-cycling or a larger battery.
- *Thermal wall* = a **rate** ceiling ($R_{peak}\cdot\eta$) — no duty cycle, battery, or software optimization can raise the maximum sustained wattage a passive chassis dissipates.

A model exceeding the envelope triggers [[ThermalThrottling|hardware throttling]] within seconds. Worked example: a 12 W LLM rises ~1 °C/s, hits the 80 °C thermal trip in ~60 s, and drops 100→30 FPS — and even FP32→INT8 [[Quantization|quantization]] (~4× power cut) leaves ~3 W, "the absolute limit of the hardware. Physics sets a hard ceiling that no optimization can exceed."

## Connections

- [[MobileML]] — the paradigm bounded by the thermal wall.
- [[ThermalThrottling]] — the hardware response to crossing it.
- [[PowerWall]] / [[DennardScaling]] — the underlying thermodynamic constraint.
- [[Quantization]] — reduces power ~4× but cannot beat the absolute ceiling.
- [[IronLawOfMLSystems]] — the thermal wall caps the instantaneous compute rate term.
- [[mlsysbook-ch02-ml-systems]] — source.
