---
title: "Electrical Safety"
type: concept
tags: [physics, electromagnetism, safety, biology]
sources: [college-physics-2e-ch20, college-physics-2e-ch23]
last_updated: 2026-06-07
---
## Definition
**Electrical safety** concerns the two hazards posed by [[ElectricCurrent|current]]: the **thermal hazard** (excess [[ElectricPower|power]] producing unwanted heat and fire) and the **shock hazard** (current passing through a person, ranging from painful to lethal). A **short circuit** — a low-resistance path between terminals — is the classic cause of dangerous heating.

## Key Points
- Thermal danger scales with power: wire overheating follows P = I²R_w, and a short dissipates P = V²/r (small r → extreme heat).
- For shock, **current magnitude** dominates severity (with path, duration, and frequency fixed). Voltage matters only through Ohm's law and body resistance.
- Approximate effects: 1 mA barely felt; ~5 mA max safe; 10–20 mA "can't-let-go" muscle contraction; 50 mA pain; 100–300 mA ventricular fibrillation (often fatal); ~6 A sustained heart/breathing arrest (reversible if removed).
- Skin resistance varies hugely (dry ~200 kΩ, wet ~10 kΩ), so wetness sharply raises current for a given voltage; body tissue conducts well via water and electrolytes.
- **Microshock sensitivity**: bypassing skin (catheters, pacemaker leads) makes ~1/1000 of normal currents dangerous.
- Modifying factors: frequency (most dangerous near 50–60 Hz; high frequency stays near the skin), duration (longer = worse), and path through the body.
- Protective devices: **fuses** melt to break a circuit permanently; **circuit breakers** trip via a bimetallic strip and reset.

### Systems and induction-based devices (Ch.23)
- **Three-wire system**: live/hot, neutral, and ground (earth) wires; multiple earth grounds keep appliance cases and the neutral at ~0 V and provide alternate current return paths.
- **Leakage current**: AC in an appliance can induce an emf on its metal case via [[FaradaysLaw|electromagnetic induction]]; the green ground wire bonds the case to 0 V, removing the shock hazard.
- **Ground-fault interrupter (GFI)**: uses induction to compare the live and neutral currents through a sensing coil — equal currents cancel, but a difference (leakage) of more than ~5 mA induces a net voltage that trips the circuit.
- **Isolation transformer**: a 1:1 [[ElectricalTransformer|transformer]] that inserts high-resistance insulation between source and load, preventing a complete circuit through a user.
- **Doubly insulated** tools have non-conductive cases and need no ground wire (asymmetric two-prong plug).

## Equations
- P = I² R_w  (wire heating)
- P = V² / r  (short-circuit heating)
- I = V / R  ([[OhmsLaw|Ohm's law]] governs body current)

## Related
- [[ElectricPower]]
- [[ElectricCurrent]]
- [[OhmsLaw]]
- [[AlternatingCurrent]]
- [[NerveConduction]]
- [[FaradaysLaw]] — induction underlies leakage current and GFI operation
- [[ElectricalTransformer]] — isolation transformers protect users
