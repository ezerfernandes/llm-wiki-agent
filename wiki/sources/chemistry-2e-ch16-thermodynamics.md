---
title: "Chemistry 2e — Ch 16: Thermodynamics"
type: source
tags: [chemistry, textbook, openstax, general-chemistry]
date: 2026-06-07
source_file: raw/chemistry-2e/16-thermodynamics.md
---

## Summary
Chapter 16 of OpenStax *Chemistry 2e* develops the thermodynamic machinery for predicting whether a chemical or physical process will occur. It distinguishes spontaneous from nonspontaneous processes via the dispersal of matter and energy (16.1), introduces entropy as a state function with the Boltzmann microstate interpretation S = k ln W (16.2), states the second law (ΔS_univ ≥ 0) and the third law (S = 0 for a perfect crystal at 0 K) and uses standard molar entropies to compute ΔS° (16.3), and defines the Gibbs free energy G = H − TS as the system-only spontaneity criterion, tying ΔG° to the equilibrium constant via ΔG° = −RT ln K (16.4).

## Key Claims
- A spontaneous process occurs without sustained external input; spontaneity is a thermodynamic property uncorrelated with rate (diamond → graphite is spontaneous yet immeasurably slow).
- Spontaneity tracks the increase in dispersal/distribution of matter and energy; gas expanding into a vacuum is spontaneous even though ΔU = 0.
- Entropy is a state function with ΔS = q_rev/T, and statistically S = k ln W (k = 1.38 × 10⁻²³ J/K); more microstates ⇒ higher entropy. S_gas > S_liquid > S_solid; entropy rises with T, particle count, mass, mixing, and dissolution.
- Second law: ΔS_univ = ΔS_sys + ΔS_surr; a process is spontaneous iff ΔS_univ > 0. At constant P, ΔS_surr = −ΔH_sys/T.
- Third law: the entropy of a pure, perfect crystal at 0 K is zero (W = 1), giving an absolute entropy reference; hence elements have nonzero S° (unlike ΔHf°).
- Standard entropy change: ΔS° = Σν S°(products) − Σν S°(reactants).
- Gibbs free energy G = H − TS, ΔG = ΔH − TΔS = −TΔS_univ; ΔG < 0 ⇒ spontaneous, = 0 ⇒ equilibrium, > 0 ⇒ nonspontaneous.
- ΔG° from formation values: ΔG° = Σν ΔGf°(products) − Σν ΔGf°(reactants); ΔGf° = 0 for an element in its standard state.
- Four ΔH/ΔS sign cases set the temperature dependence; when ΔH and ΔS share a sign the crossover temperature is T = ΔH/ΔS.
- ΔG° = −RT ln K (R = 8.314 J mol⁻¹ K⁻¹), and under nonstandard conditions ΔG = ΔG° + RT ln Q.

## Key Quotes
> "The spontaneity of a process is *not* correlated to the speed of the process." — 16.1, distinguishing thermodynamics from kinetics
> "all spontaneous changes cause an increase in the entropy of the universe" — 16.3, the second law
> "the entropy of a pure, perfect crystalline substance at 0 K is zero" — 16.3, the third law

## Connections
- [[SpontaneousProcess]] — the 16.1 spontaneous/nonspontaneous distinction and dispersal principle
- [[EntropyThermodynamics]] — entropy as a state function and dispersal measure (16.2)
- [[BoltzmannEntropyEquation]] — S = k ln W microstate model (16.2)
- [[StandardMolarEntropy]] — S° and ΔS° = Σν S° products − reactants (16.3)
- [[SecondLawOfThermodynamics]] — ΔS_univ ≥ 0 spontaneity criterion (updated with chemistry framing)
- [[ThirdLawOfThermodynamics]] — S = 0 at 0 K, absolute-entropy reference (16.3)
- [[GibbsFreeEnergy]] — G = H − TS spontaneity criterion and the four ΔH/ΔS cases (16.4)
- [[StandardFreeEnergyOfFormation]] — ΔGf° and ΔG° from formation values (16.4)
- [[GibbsFreeEnergyAndEquilibrium]] — ΔG° = −RT ln K and ΔG = ΔG° + RT ln Q (16.4)
- [[EnthalpyChemistry]] — the ΔH in ΔG = ΔH − TΔS (Ch 5 / Ch 16)
- [[FirstLawOfThermodynamics]] — the conservation law these direction/availability laws complement
- [[StandardEnthalpyOfFormation]] — parallel formation-value bookkeeping to ΔGf°
- [[EquilibriumConstant]] / [[ChemicalEquilibrium]] — K connected to ΔG° (Ch 13 / Ch 16)
- [[ReactionQuotient]] — Q in ΔG = ΔG° + RT ln Q
- [[LudwigBoltzmann]] / [[JosiahWillardGibbs]] / [[RudolfClausius]] / [[SadiCarnot]] — namesakes
- [[chemistry-2e-ch05-thermochemistry]] — prerequisite thermochemistry (ΔH, Hess's law)

## Contradictions
None identified. The second law's entropy-form treatment here is fully consistent with the physics treatment in [[college-physics-2e-ch15]] (heat engines / Carnot); the chemistry chapter emphasizes ΔS_univ = ΔS_sys + ΔS_surr and the Gibbs free-energy reformulation, while the physics chapter emphasizes engine efficiency — two complementary expressions of the same law.
