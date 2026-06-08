---
title: "Wheatstone Bridge"
type: concept
tags: [physics, electricity, circuits, dc, instruments]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
A Wheatstone bridge is a null-measurement circuit that determines an unknown resistance by balancing the potential differences across four resistive arms. A variable resistor is adjusted until a [[Galvanometer]] detector reads zero current; at that balance point the unknown resistance follows from the three known resistances.

## Key Points
- A **null measurement**: at balance no current flows through the detector, so the act of measuring does not disturb the circuit — far more accurate than an ordinary [[Voltmeter]]/[[Ammeter]].
- Balance creates an equipotential condition between the two midpoints of the bridge.
- Resolves unknown resistance to roughly four significant figures.
- Limited by inability to reach exactly zero detector current, uncertainty in standard resistances, wire/contact resistance, and temperature drift.

## Equations
- Balance conditions: `I₁R₁ = I₂R₃` and `I₁R₂ = I₂R_x`
- Unknown resistance: `R_x = R₃ R₂ / R₁`

## Related
- [[Potentiometer]] — sibling null instrument for measuring emf
- [[Galvanometer]] — the zero-current detector
- [[KirchhoffsRules]] — provide the loop/junction basis for the balance condition
- [[ElectricalResistance]] — the quantity measured
- [[OhmsLaw]] — relates the arm currents, voltages, and resistances
