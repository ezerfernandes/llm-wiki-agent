---
title: "College Physics 2e — Ch.15: Thermodynamics"
type: source
tags: [physics, openstax, college-physics-2e]
date: 2026-06-07
source_file: raw/college-physics-2e/ch-15.md
---

## Summary
Chapter 15 of OpenStax College Physics 2e develops classical thermodynamics: the first law as energy conservation for systems exchanging heat and work, the four simple processes (isobaric, isochoric, isothermal, adiabatic) and PV work, heat engines and their efficiency, the Carnot cycle as the efficiency ceiling, the second law in its heat-flow/Kelvin/entropy forms, refrigerators and heat pumps with their coefficients of performance, and the statistical (microstate-counting) interpretation of entropy. The throughline is that physical law — not engineering — caps how much heat can become useful work.

## Key Claims
- The first law of thermodynamics is conservation of energy for thermal systems: ΔE_int = Q − W (heat in minus work done by the system); internal energy is a path-independent state function while Q and W are path-dependent.
- Work in a process equals the area under its PV-diagram curve; for a closed cycle, net work equals the enclosed loop area (clockwise = positive output).
- The four simple processes constrain the first law: isobaric W = PΔV; isochoric W = 0; isothermal ΔE_int = 0 so Q = W; adiabatic Q = 0 so ΔE_int = −W.
- A heat engine over a cycle does net work W = Q_h − Q_c with efficiency Eff = W/Q_h = 1 − Q_c/Q_h; the second law (Kelvin statement) forbids 100% efficiency because Q_c > 0 always.
- The Carnot cycle (reversible isothermal + adiabatic steps) gives the maximum possible efficiency between two reservoirs: Eff_C = 1 − T_c/T_h (absolute temperature); for it, Q_c/Q_h = T_c/T_h.
- 100% efficiency would require a cold reservoir at absolute zero (T_c = 0 K), which is unattainable; real engines fall below Carnot because all real processes are irreversible.
- Refrigerators and heat pumps are reversed heat engines obeying Q_h = Q_c + W; COP_hp = Q_h/W and COP_ref = Q_c/W with COP_ref = COP_hp − 1; COP rises as the hot–cold temperature gap shrinks.
- Entropy measures unavailable energy / disorder; for a reversible step ΔS = Q/T. The second law states total entropy never decreases — constant for reversible, increasing for irreversible processes.
- Unavailable energy W_unavail = ΔS·T_0 ties entropy increase directly to lost work capacity; the cosmic limit is "heat death" at maximum entropy.
- Statistically, S = k ln W (Boltzmann): a macrostate's entropy reflects its microstate count; entropy increases because disordered macrostates have overwhelmingly more microstates, so heat flows hot→cold by probability, not force.
- Local entropy can decrease (e.g., living organisms) only if the environment's entropy increases more, keeping ΔS_total > 0.

## Key Quotes (paraphrased)
> Heat moves spontaneously from hot to cold but never the other way on its own — and no cyclic process can turn heat from one reservoir entirely into work. (paraphrased second-law statements, §15.3)
> A Carnot engine is the most efficient engine possible between two temperatures, and every fully reversible engine between those same temperatures matches it. (paraphrased Carnot principle, §15.4)
> Disorder is vastly more probable than order — entropy rises because disordered configurations have astronomically more microstates. (paraphrased, §15.7)

## Connections
- [[FirstLawOfThermodynamics]] — physics form ΔE_int = Q − W (note sign convention differs from chemistry's ΔU = q + w)
- [[SecondLawOfThermodynamics]] — heat-flow, Kelvin, and entropy statements
- [[ThermodynamicProcess]] — isobaric/isochoric/isothermal/adiabatic and PV work
- [[HeatEngine]] / [[CarnotCycle]] — work extraction and the efficiency ceiling
- [[ThermodynamicEntropy]] — ΔS = Q/T and S = k ln W
- [[HeatPump]] — refrigerators, air conditioners, and COP
- [[InternalEnergyThermodynamics]], [[HeatThermodynamics]], [[ConservationOfEnergy]], [[IdealGasLaw]], [[ThermodynamicTemperature]], [[EnergyEfficiency]] — supporting concepts
- [[SadiCarnot]] — originated the Carnot cycle (1824)
- [[Entropy]] — the information-theoretic counterpart of statistical-mechanical entropy

## Contradictions
- None substantive. Note: this physics chapter writes the first law as **ΔE_int = Q − W** (W = work done *by* the system), whereas the chemistry page [[FirstLawOfThermodynamics]] uses **ΔU = q + w** (w = work done *on* the system). These are the same law under opposite work-sign conventions, not a contradiction; the first-law concept page documents both.
