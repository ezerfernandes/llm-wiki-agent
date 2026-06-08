---
title: "Inductance"
type: concept
tags: [physics, electromagnetism, induction, electronics]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
**Inductance (L)** measures how strongly a device opposes changes in the current through it, by generating a self-induced [[ElectromotiveForce|emf]] (via [[FaradaysLaw|Faraday's]] and [[LenzsLaw|Lenz's]] laws). It is measured in **henries (H)**. **Self-inductance** refers to a coil's opposition to its own changing current; **mutual inductance (M)** is one coil inducing a voltage in another (as in a [[ElectricalTransformer|transformer]]).

## Key Points
- A changing current `ΔI/Δt` produces a back-voltage `emf = −L(ΔI/Δt)`; the larger L, the harder it is to change the current quickly.
- Inductance depends only on geometry and core material — turns, area, length, permeability — not on the current itself.
- An [[Inductor|inductor]] (a coil with significant L) stores energy `E = ½LI²` in its [[MagneticField|magnetic field]]; abruptly interrupting that current causes a dangerous voltage spike.
- Mutual inductance can be deliberately minimized (counterwound coils) to keep induced voltages off equipment cases.

## Equations
- `emf = −L (ΔI/Δt)`  (self-inductance)
- `emf₂ = −M (ΔI₁/Δt)`  (mutual inductance)
- `L = N (ΔΦ/ΔI)`  (definition)
- `L = μ₀ N² A / ℓ`  (long solenoid)
- `E = ½ L I²`  (stored energy)

## Related
- [[Inductor]] — the physical device exhibiting inductance
- [[FaradaysLaw]] — the induction law behind self/mutual inductance
- [[LenzsLaw]] — explains the opposing sign
- [[RLCircuit]] — inductance sets the L/R time constant
- [[Reactance]] — inductive reactance X_L = 2πfL in AC circuits
- [[ElectricalTransformer]] — operates by mutual inductance
- [[MagneticField]] — where the inductor stores energy
