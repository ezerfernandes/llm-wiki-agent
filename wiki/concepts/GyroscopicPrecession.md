---
title: "Gyroscopic Precession"
type: concept
tags: [physics, rotation, dynamics, vectors]
sources: [college-physics-2e-ch10]
last_updated: 2026-06-07
---
## Definition
Gyroscopic precession is the slow change in the orientation of a spinning object's axis caused by a [[Torque]] applied perpendicular to its [[AngularMomentum]]. It exposes the *vector* nature of angular momentum: L = Iω points along the rotation axis, and net τ = ΔL/Δt means the axis shifts in the direction of the torque rather than the object simply falling.

> Note: this is the physics/mechanics gyroscope concept. For the MEMS angular-velocity sensor used in embedded IMUs, see [[Gyroscope]].

## Key Points
- [[AngularMomentum]] L and [[AngularVelocity]] ω are vectors parallel to the rotation axis; torque τ is perpendicular to the plane formed by r and F.
- Right-hand rule for ω/L: curl the fingers in the rotation direction, the thumb gives the axis. For τ: curl from r toward F, the thumb gives the torque direction.
- When τ ⊥ L, the change ΔL points along τ; adding ΔL to L reorients the axis while its magnitude stays fixed — the object precesses instead of toppling.
- A spinning bicycle wheel, when twisted, tilts toward the person (perpendicular to the applied force) — the hallmark counterintuitive gyroscopic response.
- Earth acts like a giant gyroscope: gravitational torque from the Sun and Moon precesses its axis with a period of about 26,000 years, slowly shifting the pole star (currently near Polaris).
- Angular momentum is a vector; [[RotationalKineticEnergy]] is a scalar.

## Equations
- net τ = ΔL / Δt   (ΔL points along τ)
- L = I ω   (L, ω along the axis)
- τ ⊥ plane(r, F)

## Related
- [[AngularMomentum]]
- [[Torque]]
- [[AngularVelocity]]
- [[ConservationOfAngularMomentum]]
- [[Gyroscope]]
