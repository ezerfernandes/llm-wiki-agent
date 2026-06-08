---
title: "Back EMF"
type: concept
tags: [physics, electromagnetism, induction]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
**Back emf** is the [[ElectromotiveForce|emf]] a motor's own rotating coil generates as it turns through a [[MagneticField|magnetic field]] — the motor acts as an [[ElectricGenerator|generator]] at the same time. By [[LenzsLaw|Lenz's law]] this induced emf opposes the applied driving voltage, limiting the current the motor draws.

## Key Points
- Back emf is proportional to angular speed ω, so it is zero at startup and rises as the motor speeds up.
- The net voltage across the coil's resistance is `V_applied − ε_back`, which sets the current `I = (V_applied − ε_back)/R`.
- At startup ε_back = 0, so current (and I²R heating) is at its maximum — this inrush dims household lights when large motors start.
- Under mechanical load the motor slows, back emf falls, and current/torque rise to meet the load; sustained low-speed running can overheat the coil.
- An unloaded motor speeds up until back emf nearly equals the supply, minimizing current draw.

## Equations
- `ε_back ∝ ω`
- `V_coil = V_applied − ε_back`
- `I = (V_applied − ε_back)/R`
- `P = I² R`  (coil heating)

## Related
- [[LenzsLaw]] — back emf opposes the applied voltage
- [[ElectricMotor]] — the device in which back emf arises
- [[ElectricGenerator]] — a motor is a generator run in reverse
- [[FaradaysLaw]] — the induction law producing the back emf
- [[ElectromotiveForce]] — the induced quantity
