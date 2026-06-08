---
title: "Potentiometer (Null Measurement)"
type: concept
tags: [physics, electricity, circuits, dc, instruments]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
In the null-measurement sense, a potentiometer is an instrument that measures an unknown electromotive force ([[ElectromotiveForce]]) by comparing it against a precisely calibrated standard voltage. The contact along a resistance wire is adjusted until a [[Galvanometer]] detector reads zero; the ratio of wire resistances then gives the unknown emf without needing to know the circuit current.

## Key Points
- A **null method**: at balance no current is drawn from the source under test, so its [[InternalResistance]] causes no error — the true emf is obtained, not the loaded terminal voltage.
- Ratio comparison cancels the unknown circuit current.
- Used to measure battery emf accurately without knowing internal resistance.
- Shares limitations of all null methods: cannot reach exactly zero, plus standard-voltage and wire/contact uncertainties.
- Distinct from the three-terminal variable-resistor "pot" component (same word, different device).

## Equations
- Comparison ratio: `emf_x / emf_s = R_x / R_s`
- Unknown emf: `emf_x = emf_s · (R_x / R_s)`

## Related
- [[WheatstoneBridge]] — sibling null instrument for measuring resistance
- [[ElectromotiveForce]] — the quantity measured
- [[InternalResistance]] — what the null method sidesteps
- [[Galvanometer]] — the zero-current detector
- [[Voltmeter]] — the loading-prone meter this replaces for precision emf work
