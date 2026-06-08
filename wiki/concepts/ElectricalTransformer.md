---
title: "Transformer (Electrical)"
type: concept
tags: [physics, electromagnetism, induction, electronics]
sources: [college-physics-2e-ch23]
last_updated: 2026-06-07
---
> Disambiguation: this page is the electrical-power device. For the neural-network architecture, see [[Transformer]].

## Definition
An **electrical transformer** is a device that changes AC voltage using two coils — a **primary** (input) and **secondary** (output) — magnetically coupled through a shared [[MagneticField|ferromagnetic core]]. AC in the primary creates a changing [[MagneticFlux|flux]] that induces a voltage in the secondary via [[FaradaysLaw|Faraday's law]]. The output-to-input voltage ratio equals the turns ratio.

## Key Points
- **Step-up** transformers (more secondary turns) raise voltage and lower current; **step-down** transformers do the reverse.
- An ideal (lossless) transformer conserves power, so raising voltage necessarily lowers current proportionally.
- Transformers only work on AC — a steady DC current produces no flux change and hence no output. This is a key reason power grids use [[AlternatingCurrent|AC]].
- Used in cascade for power distribution: generation (>10 kV) → high-voltage transmission (200–700 kV, to cut I²R line losses) → step-down to user levels (120–480 V).
- An **isolation transformer** (1:1 ratio) inserts a high-resistance insulating barrier for [[ElectricalSafety|electrical safety]].

## Equations
- `Vs/Vp = Ns/Np`
- `Is/Ip = Np/Ns`
- `Vs = −Ns (ΔΦ/Δt)`,  `Vp = −Np (ΔΦ/Δt)`
- `Pp = Ip Vp = Is Vs = Ps`  (ideal)

## Related
- [[FaradaysLaw]] — the induction law transformers exploit
- [[MagneticFlux]] — the shared flux that couples the coils
- [[AlternatingCurrent]] — transformers require changing flux, hence AC
- [[Inductance]] — mutual inductance describes the coil coupling
- [[ElectricalSafety]] — isolation transformers protect users
- [[Transformer]] — unrelated ML architecture sharing the name
