---
title: "Second Law of Thermodynamics"
type: concept
tags: [physics, chemistry, thermodynamics, energy]
sources: [college-physics-2e-ch15, chemistry-2e-ch16-thermodynamics]
last_updated: 2026-06-07
---

## Definition
The **second law of thermodynamics** governs the *direction* of thermal processes and caps how much heat can become work. It has several equivalent statements: (1) heat flows spontaneously from hotter to colder bodies, never the reverse on its own; (2) the **Kelvin statement** — no cyclic process can convert heat from a single reservoir *entirely* into work; (3) the **entropy statement** — the total [[ThermodynamicEntropy|entropy]] of a system never decreases.

## Key Points
- Complements the [[FirstLawOfThermodynamics|first law]]: the first law says energy is conserved; the second law says not all of it is usable for work.
- The Kelvin statement forbids 100%-efficient [[HeatEngine|heat engines]] — some heat (Q_c) must always be dumped to a cold reservoir.
- The [[CarnotCycle|Carnot]] restatement: a reversible engine between two temperatures is the most efficient possible, and all reversible engines between the same temperatures share that maximum.
- Real processes are **irreversible** (braking → heat, gas expanding into vacuum, things breaking) and increase total entropy; only idealized reversible processes hold entropy constant.
- Statistically, the law holds because disordered macrostates have vastly more [[ThermodynamicEntropy|microstates]] — entropy increase is a matter of overwhelming probability, not an imposed force.
- Cosmic endpoint: monotonic entropy increase implies an eventual "heat death" at maximum entropy with no temperature gradients to drive work.

## Chemistry Framing (Chemistry 2e, Ch 16)
General chemistry states the entropy form in terms of system and surroundings:

$$\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}}$$

A process is **spontaneous** when ΔS_univ > 0, **at equilibrium** when ΔS_univ = 0, and **nonspontaneous** (spontaneous in reverse) when ΔS_univ < 0 — "all spontaneous changes cause an increase in the entropy of the universe." For surroundings vast relative to the system, at constant pressure ΔS_surr = −q_sys/T = −ΔH_sys/T, so ΔS_univ = ΔS_sys − ΔH/T. Multiplying by −T gives the [[GibbsFreeEnergy|Gibbs free energy]] criterion ΔG = −TΔS_univ, recasting the law in system-only terms. This is the same physics as the heat-engine statements below, just expressed for chemical reactions.

## Equations
- Entropy form: $\Delta S_{\text{tot}} \geq 0$ (= 0 reversible, > 0 irreversible)
- Chemistry form: $\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}} \geq 0$
- Engine efficiency limit: $\text{Eff} \leq \text{Eff}_C = 1 - \dfrac{T_c}{T_h}$

## Related
- [[FirstLawOfThermodynamics]]
- [[ThirdLawOfThermodynamics]] — the companion law fixing S = 0 at 0 K
- [[ThermodynamicEntropy]]
- [[EntropyThermodynamics]] — chemistry treatment of the entropy in ΔS_univ
- [[GibbsFreeEnergy]] — ΔG = −TΔS_univ, the system-only restatement
- [[SpontaneousProcess]] — spontaneity defined by ΔS_univ > 0
- [[HeatEngine]]
- [[CarnotCycle]]
- [[HeatPump]]
- [[HeatThermodynamics]] — spontaneous hot→cold flow
- [[ThermodynamicTemperature]]
- [[college-physics-2e-ch15]]
- [[chemistry-2e-ch16-thermodynamics]] — chemistry entropy-universe form (§16.3)
