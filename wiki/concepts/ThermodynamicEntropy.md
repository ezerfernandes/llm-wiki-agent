---
title: "Entropy (Thermodynamics)"
type: concept
tags: [physics, thermodynamics, energy]
sources: [college-physics-2e-ch15]
last_updated: 2026-06-07
---

> Disambiguation: this page is *thermodynamic / statistical-mechanical* entropy. For the information-theory measure (Shannon entropy, used in ML), see [[Entropy]] — the two are deeply connected: both are S = −Σ p log p up to constants, and the statistical interpretation below (S = k ln W) is the physical bridge.

## Definition
**Entropy (S)** measures the amount of a system's energy that is *unavailable* to do work — equivalently, its degree of disorder. It is a **state property**, so its change between two states can be computed along any convenient reversible path. The [[SecondLawOfThermodynamics|second law]] states that total entropy never decreases.

## Key Points
- For a reversible heat exchange, ΔS = Q/T; total change sums over reservoirs (ΔS_tot = ΔS_h + ΔS_c).
- Reversible processes (e.g. the ideal [[CarnotCycle|Carnot cycle]]) keep total entropy constant, since Q_c/T_c = Q_h/T_h; irreversible processes (real heat transfer, friction) increase it.
- More entropy means less useful work: the energy made unavailable is W_unavail = ΔS·T_0, where T_0 is the lowest available temperature.
- **Statistical interpretation (Boltzmann):** S = k ln W, where W is the number of **microstates** (detailed configurations) corresponding to a **macrostate** (e.g. P, T, V). Disordered macrostates dominate because they have astronomically more microstates.
- The coin-toss analogy: 50/50 outcomes overwhelmingly outnumber all-heads, just as a gas's random Maxwell–Boltzmann distribution overwhelmingly outnumbers "all atoms in one corner." Hence heat flows hot→cold and disorder grows — by probability, not force.
- Local entropy *can* decrease (living organisms, crystallization) only if the surroundings' entropy increases more: ΔS_system + ΔS_environment > 0.
- Cosmic limit: ever-increasing entropy points toward a maximum-entropy "heat death" with no gradients left to drive work.

## Equations
- Reversible entropy change: $\Delta S = \dfrac{Q}{T}$
- Boltzmann entropy: $S = k \ln W$ (k = 1.38×10⁻²³ J/K)
- Entropy change from microstates: $\Delta S = k \ln W_f - k \ln W_i$
- Unavailable energy: $W_{\text{unavail}} = \Delta S \cdot T_0$

## Related
- [[SecondLawOfThermodynamics]]
- [[CarnotCycle]]
- [[HeatEngine]]
- [[Entropy]] — information-theory counterpart (Shannon)
- [[HeatThermodynamics]]
- [[ThermodynamicTemperature]]
- [[college-physics-2e-ch15]]
