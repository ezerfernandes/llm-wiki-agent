---
title: "Drag Force"
type: concept
tags: [physics, dynamics, friction]
sources: [college-physics-2e-ch04, college-physics-2e-ch05]
last_updated: 2026-06-07
---
## Definition
A drag force is a frictional force exerted by a fluid (such as air or water) on an object moving through it. It always opposes the object's motion relative to the fluid.

## Key Points
- Introduced in Chapter 4 as one of the resistive forces handled with Newton's laws; Chapter 5 gives the quantitative laws.
- For large objects at moderate-to-high speed, drag is proportional to the square of velocity and depends on shape, size, and fluid properties via a dimensionless drag coefficient C (often measured in wind tunnels).
- For small particles at low speed, drag instead follows Stokes' law (linear in velocity and radius).
- When drag grows to balance weight, net force is zero and the object reaches [[TerminalVelocity]] — cross-sectional area strongly affects this value.
- It is electromagnetic in origin (fluid molecules interacting with the object), like other contact forces (see [[FundamentalForces]]).
- In problems it appears as an unknown resistive force solved via [[NewtonsSecondLaw]] once applied force and acceleration are known.

## Equations
- Quadratic drag (large objects): F_D = (1/2) C ρ A v²  (equivalently F_D = b v² with b = 0.5 C ρ A)
- Stokes' law (small particles, low speed): F_s = 6 π r η v
- Terminal velocity: v_t = sqrt( 2 m g / (ρ C A) )
- Solving for drag from an applied force: F_D = F_app − ma

## Related
- [[Force]]
- [[Friction]]
- [[TerminalVelocity]]
- [[NewtonsSecondLaw]]
- [[FreeBodyDiagram]]
