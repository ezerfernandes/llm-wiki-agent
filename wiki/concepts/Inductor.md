---
title: "Inductor"
type: concept
tags: [physics, electromagnetism, electronics, component]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
An **inductor** is a circuit component — typically a coil of wire — that exhibits significant [[Inductance|inductance]] L. It resists changes in current by storing energy in its [[MagneticField|magnetic field]] and releasing it via a self-induced [[ElectromotiveForce|emf]]. It is the magnetic-energy counterpart of the [[Capacitor|capacitor]] (which stores electric-field energy).

## Key Points
- Stores energy `E = ½LI²`; current through it cannot change instantaneously.
- In AC circuits an inductor presents **inductive reactance** `X_L = 2πfL`, opposing current more strongly at higher frequencies, with the voltage *leading* the current by 90°.
- Combined with a resistor it forms an [[RLCircuit|RL circuit]] with time constant `τ = L/R`.
- Used as a high-frequency-noise filter, in tuned [[RLCCircuit|RLC]] circuits, and in metal detectors / roadway vehicle-detection loops (nearby metal changes L).

## Equations
- `E = ½ L I²`  (stored energy)
- `emf = −L (ΔI/Δt)`  (self-induced)
- `X_L = 2π f L`  (inductive reactance)
- `τ = L/R`  (RL time constant)

## Related
- [[Inductance]] — the property an inductor embodies
- [[Capacitor]] — the dual energy-storage component
- [[RLCircuit]] — resistor + inductor transient circuit
- [[Reactance]] — inductive reactance in AC
- [[RLCCircuit]] — inductor in a resonant AC circuit
- [[MagneticField]] — where the energy is stored
