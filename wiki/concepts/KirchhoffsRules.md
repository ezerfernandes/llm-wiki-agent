---
title: "Kirchhoff's Rules"
type: concept
tags: [physics, electricity, circuits, dc]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
Two rules, formulated by [[GustavKirchhoff]], for analyzing circuits too complex to reduce by simple series/parallel combination. The **junction (node) rule** applies conservation of charge; the **loop rule** applies conservation of energy. Together they generate enough independent equations to solve for all unknown currents and voltages.

## Key Points
- **Junction rule:** the sum of currents entering a junction equals the sum leaving (charge conservation).
- **Loop rule:** the algebraic sum of potential changes around any closed loop is zero (energy conservation).
- Assign current directions arbitrarily; a wrong guess simply yields a negative value, not a wrong magnitude.
- Sign conventions when traversing a loop:
  - resistor with the current: drop `−IR`; against the current: rise `+IR`
  - emf source from − to +: `+emf`; from + to −: `−emf`
- Use one junction equation per independent node and one loop equation per independent loop.

## Equations
- Junction: `I₁ = I₂ + I₃` (currents in = currents out)
- Loop: `Σ V = 0` around any closed path
- Example loops: `−I₂(R₂ + r₁) + emf₁ − I₁R₁ = 0`; `I₁R₁ + I₃(R₃ + r₂) − emf₂ = 0`

## Related
- [[GustavKirchhoff]] — physicist who formulated the rules
- [[ResistorsInSeriesAndParallel]] — the simpler reduction these generalize
- [[ElectromotiveForce]] / [[InternalResistance]] — appear as emf and r terms in loop equations
- [[ElectricCurrent]], [[Voltage]] — the conserved/summed quantities
- [[WheatstoneBridge]] — analyzed via the balance (null) condition derived from these rules
