---
title: "Root-Mean-Square Speed"
type: concept
tags: [chemistry, general-chemistry, gases, kinetic-theory]
sources: [chemistry-2e-ch09-gases]
last_updated: 2026-06-07
---

# Root-Mean-Square Speed

In a gas, individual molecules have widely varying speeds, but the [[KineticMolecularTheory|kinetic-molecular theory]] gives a representative measure: the **root-mean-square speed (u_rms)**, the square root of the mean of the squared molecular speeds:

$$u_{rms} = \sqrt{\overline{u^2}} = \sqrt{\frac{u_1^2 + u_2^2 + u_3^2 + \ldots}{n}}$$

## Relation to Temperature and Molar Mass

The kinetic energy of one molecule is KE = ½mu². The average kinetic energy per mole is proportional to absolute temperature:

$$KE_{avg} = \frac{1}{2}\mathcal{M}\,u_{rms}^2 = \frac{3}{2}RT$$

Solving for the speed (with R = 8.314 J/(mol·K) and ℳ in kg/mol):

$$u_{rms} = \sqrt{\frac{3RT}{\mathcal{M}}}$$

So u_rms rises with temperature and falls with molar mass. **Example:** N₂ (ℳ = 0.028 kg/mol) at 303 K has u_rms = √[(3 × 8.314 × 303)/0.028] = 519 m/s; O₂ at −23 °C has u_rms = 441 m/s.

## The Maxwell-Boltzmann Distribution

Molecular speeds follow the **Maxwell-Boltzmann distribution**: most molecules have intermediate speeds, few are very slow or very fast. The peak is the **most probable speed (ν_p)**, slightly below u_rms.

- **Higher temperature** → distribution shifts right (higher speeds) and broadens/flattens.
- **Lower temperature** → shifts left.
- **At a fixed temperature**, all gases share the same KE_avg, but **lighter gases have higher u_rms** (distribution peaks at higher speeds) and heavier gases peak lower.

Because effusion rate ∝ u_rms, this directly yields [[GrahamsLaw|Graham's law]].

## Connections
- [[KineticMolecularTheory]] — the model that derives u_rms
- [[GrahamsLaw]] — follows from u_rms ∝ 1/√ℳ
- [[Effusion]] / [[GaseousDiffusion]] — rates set by molecular speeds
- [[TemperatureMeasurement]] — kelvin temperature sets the average KE
- [[MolarMass]] — heavier gases move slower at the same temperature
- [[chemistry-2e-ch09-gases]] — source chapter (§9.5)
