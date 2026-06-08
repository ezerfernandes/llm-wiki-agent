---
title: "College Physics 2e — Ch.23: Electromagnetic Induction, AC Circuits, and Electrical Technologies"
type: source
tags: [physics, openstax, college-physics-2e]
date: 2026-06-07
source_file: raw/college-physics-2e/ch-23.md
---

## Summary
Chapter 23 of OpenStax *College Physics 2e* develops electromagnetic induction — the generation of an emf by a changing magnetic flux — as the converse of currents producing magnetic fields. It covers [[MagneticFlux]], [[FaradaysLaw]], [[LenzsLaw]], [[MotionalEMF]], [[EddyCurrent|eddy currents and magnetic damping]], [[ElectricGenerator|generators]], [[BackEMF|back emf]], [[ElectricalTransformer|transformers]], [[ElectricalSafety|electrical-safety systems]], [[Inductance]], [[RLCircuit|RL circuits]], [[Reactance|inductive/capacitive reactance]], and [[RLCCircuit|RLC series circuits with resonance]]. It is the AC-circuit and electrical-technology core of the book, linking [[MagneticField|magnetism]] to nearly all modern power and signal technology.

## Key Claims
- Only a *changing* magnetic flux induces an emf; static fields do nothing, and only relative motion between magnet and coil matters ([[MagneticFlux]], [[FaradaysLaw]]).
- Faraday's law gives `emf = −N(ΔΦ/Δt)`; the negative sign is [[LenzsLaw]], which states induced effects oppose the change creating them — a direct expression of energy conservation.
- A conductor of length ℓ moving at speed v perpendicular to field B develops a motional emf `B ℓ v`; the same law scales from microvolts at Earth's surface to kilovolts for an orbiting tethered satellite ([[MotionalEMF]]).
- Eddy currents in a solid conductor moving through a field produce velocity-proportional drag (magnetic damping); slotting the conductor cancels the loops and removes most of the damping ([[EddyCurrent]]).
- A rotating coil produces sinusoidal emf `emf(t) = NABω sin(ωt)` with peak `emf₀ = NABω`; this is the basis of AC generators and explains why grid power is alternating ([[ElectricGenerator]]).
- A spinning motor coil generates a back emf proportional to angular speed, so `I = (V_applied − ε_back)/R`; startup current is dangerously high because ε_back starts at zero ([[BackEMF]]).
- An ideal transformer obeys `Vs/Vp = Ns/Np` and `Is/Ip = Np/Ns` with `Pp = Ps`; it works only on AC because it needs changing flux, which is why AC dominates power distribution ([[ElectricalTransformer]]).
- Three-wire grounding plus induction-based ground-fault interrupters (GFIs, ~5 mA threshold) and isolation transformers protect against shock and thermal hazards ([[ElectricalSafety]]).
- Inductance L (henries) depends only on coil geometry/core (`L = μ₀N²A/ℓ` for a solenoid); a current stores `E = ½LI²` in the magnetic field, so interrupting current abruptly causes voltage spikes ([[Inductance]]).
- An RL circuit's current rises/falls exponentially with time constant `τ = L/R` because the inductor opposes instantaneous current change ([[RLCircuit]]).
- Inductive reactance `X_L = 2πfL` grows with frequency while capacitive reactance `X_C = 1/(2πfC)` falls with it; inductor voltage leads current by 90°, capacitor voltage lags by 90° ([[Reactance]]).
- In an RLC series circuit `Z = √[R² + (X_L − X_C)²]`; at resonance `f₀ = 1/(2π√(LC))` the reactances cancel, impedance equals R, current peaks, and the power factor `cos φ = R/Z` reaches 1 ([[RLCCircuit]]).

## Key Quotes (paraphrased)
> Any change in magnetic flux induces an emf — whether the field changes, the area changes, or the orientation changes. (23.1)
> The induced current and field oppose the flux change that produced them; the minus sign embodies energy conservation, ruling out free perpetual energy. (23.2, Lenz's law)
> Motors and generators are the same machine run in opposite directions — electrical-to-mechanical versus mechanical-to-electrical. (23.5–23.6)
> Transformers cannot change a DC voltage because they require a continuously changing flux. (23.7)
> At resonance the inductive and capacitive reactances cancel, leaving only resistance, so current is maximal and all delivered power is real. (23.12)

## Connections
- [[MagneticField]] — induction is driven by changing magnetic flux through a loop
- [[ElectromotiveForce]] — induced emf is the chapter's central quantity
- [[AlternatingCurrent]] — generators and transformers are why grids run on AC
- [[ElectricGenerator]] / [[ElectricMotor]] — same device, opposite energy flow; back emf links them
- [[Capacitor]] / [[Inductor]] — reactive elements in AC circuits
- [[RCCircuit]] — DC-transient analog of the [[RLCircuit]]
- [[Resonance]] — RLC resonance is the electrical analog of mechanical resonance
- [[MichaelFaraday]] — discovered induction and the law that bears his name

## Contradictions
- None. This chapter extends the magnetism material of College Physics 2e Ch.22 and the AC overview in Ch.20 without conflict.
