---
title: "Electric Generator"
type: concept
tags: [physics, electromagnetism, induction]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
An **electric generator** produces an [[ElectromotiveForce|emf]] by rotating a conducting coil within a [[MagneticField|magnetic field]]. The rotation continuously changes the [[MagneticFlux|flux]] through the coil, inducing a sinusoidal emf via [[FaradaysLaw|Faraday's law]] — converting mechanical work into electrical energy. A generator is structurally identical to an [[ElectricMotor|electric motor]] run in reverse.

## Key Points
- Steady rotation at angular velocity ω gives a sinusoidal output `emf(t) = NABω sin(ωt)`, which is why grid power is [[AlternatingCurrent|alternating]].
- Output peaks (`emf₀ = NABω`) when the coil's plane is parallel to the field (flux changing fastest) and is zero when perpendicular.
- Peak emf scales with turns N, area A, field B, and rotation speed ω — faster spinning yields higher voltage (e.g., a bicycle dynamo brightens as you pedal harder).
- A **split-ring commutator** reverses the output connections each half-turn to rectify the sinusoid into pulsed DC.
- Driven by water, steam, or wind turbines in practice.

## Equations
- `emf = −N (ΔΦ/Δt)`  (Faraday's law)
- `ΔΦ = A B Δ(cos θ)`
- `emf(t) = N A B ω sin(ωt)`  (instantaneous)
- `emf₀ = N A B ω`  (peak)
- `ω = 2π f`; `T = 1/f = 2π/ω`

## Related
- [[FaradaysLaw]] — the induction law generators apply
- [[MotionalEMF]] — the microscopic source of the induced voltage
- [[ElectricMotor]] — same machine, opposite energy flow
- [[BackEMF]] — links motor and generator behavior
- [[AlternatingCurrent]] — generators are the source of AC
- [[MagneticField]] — the field the coil rotates in
