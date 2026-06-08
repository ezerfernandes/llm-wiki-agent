---
title: "Boltzmann Entropy Equation (S = k ln W)"
type: concept
tags: [chemistry, thermodynamics, statistical-mechanics, general-chemistry]
sources: [chemistry-2e-ch16-thermodynamics]
last_updated: 2026-06-07
---

# Boltzmann Entropy Equation: S = k ln W

> Disambiguation: this is the *statistical-mechanics / chemistry* microstate definition of entropy. For the macroscopic chemical treatment see [[EntropyThermodynamics]]; for the physics/heat-engine view see [[ThermodynamicEntropy]]; for Shannon entropy in ML see [[Entropy]].

[[LudwigBoltzmann]]'s statistical model relates the entropy of a system to the number of **microstates (W)** accessible to it:

$$S = k \ln W$$

where **k is the Boltzmann constant, k = 1.38 × 10⁻²³ J/K**.

- A **microstate** is a specific configuration of all the positions and energies of the atoms or molecules of a system.
- A **macrostate** is the bulk observable condition (e.g., specified P, T, V). Many microstates correspond to one macrostate; the macrostate with the most microstates is the most probable and has the highest entropy.

## Entropy Change
$$\Delta S = S_f - S_i = k \ln\frac{W_f}{W_i}$$

- W_f > W_i ⇒ ΔS > 0 (more accessible microstates, more dispersed).
- W_f < W_i ⇒ ΔS < 0.

**Worked example.** Four particles distributed between two boxes: all-in-one-box = 1 microstate; even (2 + 2) distribution = 6 microstates. ΔS = (1.38 × 10⁻²³ J/K) · ln(6/1) = 2.47 × 10⁻²³ J/K.

## Link to the Third Law
A pure, perfect crystal at 0 K has exactly one accessible microstate (W = 1), so S = k ln(1) = 0 — this is the basis of the [[ThirdLawOfThermodynamics|third law]] and the absolute entropy scale.

## Connections
- [[EntropyThermodynamics]] — macroscopic entropy this equation explains microscopically
- [[ThirdLawOfThermodynamics]] — W = 1 ⇒ S = 0 at 0 K
- [[SecondLawOfThermodynamics]] — disordered (high-W) macrostates dominate, so entropy tends to increase
- [[LudwigBoltzmann]] — originator
- [[StandardMolarEntropy]] — absolute S° values resting on this microstate foundation
- [[chemistry-2e-ch16-thermodynamics]] — source chapter (§16.2)
