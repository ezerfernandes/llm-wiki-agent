---
title: "Radioactive Half-Life and Radiometric Dating"
type: concept
tags: [chemistry, general-chemistry, nuclear-chemistry, kinetics, dating, openstax]
sources: [chemistry-2e-ch21-nuclear-chemistry]
last_updated: 2026-06-07
---

# Radioactive Half-Life and Radiometric Dating

> Disambiguation: this is the OpenStax *Chemistry 2e* (Ch 21) treatment of nuclear-decay half-life and dating. For the College Physics 2e treatments see [[HalfLife]] and [[RadiometricDating]]; for the chemical-kinetics (reactant-concentration) half-life see [[ReactionHalfLife]].

[[RadioactiveDecayChemistry|Radioactive decay]] follows **first-order kinetics**, identical in form to a first-order chemical reaction. The **half-life** ($t_{1/2}$) is the time for half the atoms in a sample to decay; for a first-order process it is **constant**, independent of how much sample remains.

### Rate laws
$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda} \qquad \lambda = \frac{0.693}{t_{1/2}}$$

$$\text{decay rate (activity)} = \lambda N \qquad N_t = N_0 e^{-\lambda t} \qquad t = -\frac{1}{\lambda}\ln\!\left(\frac{N_t}{N_0}\right)$$

where λ is the decay constant and N the number of nuclei. After *n* half-lives the fraction remaining is (1/2)ⁿ. **Activity** is the decay rate in disintegrations per second; its units are the **becquerel** (1 Bq = 1 decay/s) and the **curie** (1 Ci = 3.7 × 10¹⁰ Bq) — see [[IonizingRadiationChemistry]].

### Radiometric dating
Because decay rate is proportional to the remaining radioisotope, comparing present and original amounts (or activities) yields an object's age via $t = -\frac{1}{\lambda}\ln(\text{Rate}_t/\text{Rate}_0)$.

**Radiocarbon (carbon-14) dating.** C-14 forms in the upper atmosphere when cosmic-ray neutrons strike nitrogen-14: $^{14}_{7}\text{N} + ^{1}_{0}\text{n} \rightarrow ^{14}_{6}\text{C} + ^{1}_{1}\text{H}$. Living things hold a constant ¹⁴C:¹²C ratio; at death ¹²C is fixed while ¹⁴C decays ($^{14}_{6}\text{C} \rightarrow ^{14}_{7}\text{N} + ^{0}_{-1}\text{e}$).
- Half-life of C-14: **5,730 years**; λ = 0.693/5730 = 1.21 × 10⁻⁴ y⁻¹
- Useful to ~30,000 y (reasonable to ~50,000 y)
- Example (Dead Sea Scrolls): 13.6 → 10.8 disintegrations/min/g C gives an age ~1,910 years
- Corrected against tree-ring (dendrochronology) calibration because fossil-fuel ¹²CO₂ shifted the atmospheric ratio

**Geological clocks** (for much older samples):
- U-238 → Pb-206, t₁/₂ = 4.5 billion y (rocks; oldest Earth material is the Jack Hills zircons, ~4.4 Gy)
- K-40 → Ar-40 (positron emission + electron capture), t₁/₂ = 1.25 billion y
- Rb-87 → Sr-87, t₁/₂ = 48.8 billion y

## Connections
- [[chemistry-2e-ch21-nuclear-chemistry]] — source chapter (§21.3)
- [[HalfLife]] / [[RadiometricDating]] — College Physics 2e counterparts
- [[ReactionHalfLife]] — the chemical-kinetics half-life (Ch 12) this parallels
- [[RadioactiveDecayChemistry]] — the decay processes being timed
- [[IonizingRadiationChemistry]] — activity units (Bq, Ci)
- [[Radioisotope]] — long-lived isotopes used as clocks
