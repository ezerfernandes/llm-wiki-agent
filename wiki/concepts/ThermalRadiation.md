---
title: "Thermal Radiation"
type: concept
tags: [physics, thermodynamics, heat-transfer, electromagnetism]
sources: [college-physics-2e-ch14]
last_updated: 2026-06-07
---

## Definition
**Thermal radiation** is [[HeatTransfer|heat transfer]] by [[ElectromagneticRadiation|electromagnetic
waves]] (radio, microwave, infrared, visible, etc.). It is the only heat-transfer mechanism that needs no
medium and can therefore cross empty space (e.g. sunlight reaching Earth).

## Key Points
- The power a surface radiates follows the **Stefan–Boltzmann law**: it scales with emissivity, surface
  area, and the **fourth power of absolute temperature** ([[ThermodynamicTemperature]], in kelvin) — an
  exceptionally strong temperature dependence.
- **Emissivity (e)** is a dimensionless 0–1 measure of how effectively a surface emits radiation: an
  ideal **black body** has e = 1; a perfect reflector has e = 0; real surfaces lie between. A good
  emitter is also a good absorber.
- **Net** transfer accounts for simultaneous emission and absorption between an object and its
  surroundings; the body cools if it is hotter than its surroundings and warms if cooler.
- Human skin has e ≈ 0.97 in the infrared regardless of visible color, so an unclothed person in a cool
  room radiates ~99 W net; clothing cuts this loss via lower emissivity/reflectivity.
- The **greenhouse effect**: atmospheric gases (CO₂, H₂O) absorb and re-radiate infrared back toward
  Earth's surface, keeping the planet habitable.
- Applications: building thermography (finding heat leaks), urban albedo (dark pavements absorb more
  solar radiation), medical thermography, and solar collectors/cookers.

## Equations
- Q/t = σ e A T⁴   (radiated power)
- Q_net/t = σ e A (T2⁴ − T1⁴)   (net transfer; T2 = surroundings, T1 = object)
- σ = 5.67 × 10⁻⁸ W/(m²·K⁴)   (Stefan–Boltzmann constant)

## Related
- [[HeatTransfer]]
- [[HeatConduction]]
- [[Convection]]
- [[ElectromagneticRadiation]]
- [[ThermodynamicTemperature]]
- [[HeatThermodynamics]]
- [[college-physics-2e-ch14]]
