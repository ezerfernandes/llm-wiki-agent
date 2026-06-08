---
title: "Chemistry 2e — Ch 12: Kinetics"
type: source
tags: [chemistry, textbook, openstax, general-chemistry]
date: 2026-06-07
source_file: raw/chemistry-2e/12-kinetics.md
---

## Summary
Chapter 12 of OpenStax *Chemistry 2e* introduces **chemical kinetics**: how fast reactions go and the molecular-scale steps by which they occur. It defines reaction rate (average, instantaneous, and initial) and ties the rates of different species together through stoichiometry; surveys the five factors that affect rate (chemical nature, physical state/surface area, temperature, concentration, catalysts); develops the experimentally determined rate law (rate constant, reaction order, method of initial rates) and the integrated rate laws and half-lives for zero-, first-, and second-order reactions; explains rates microscopically via collision theory (collision frequency, orientation, activation energy, the activated complex/transition state) and quantitatively via the Arrhenius equation; and closes with reaction mechanisms (elementary reactions, molecularity, intermediates, the rate-determining step) and catalysis (homogeneous, heterogeneous, and enzymes).

## Key Claims
- The rate of a reaction measures how much reactant is consumed or product formed per unit time; rates can be average (over an interval), instantaneous (the tangent slope on a concentration-vs-time plot), or initial (instantaneous at t = 0). Reactions slow as they proceed because reactant concentration falls.
- For a reaction aA + bB → cC + dD the species rates are coupled by the stoichiometric coefficients: −(1/a)Δ[A]/Δt = −(1/b)Δ[B]/Δt = (1/c)Δ[C]/Δt = (1/d)Δ[D]/Δt.
- Five factors affect reaction rate: the chemical nature of the reactants, their physical state (and surface area at phase interfaces), temperature (rates roughly double per +10 °C), reactant concentration, and the presence of a catalyst.
- The rate law, rate = k[A]^m[B]^n…, has a temperature-dependent (concentration-independent) rate constant k and reaction orders m, n that must be found experimentally — they are not reliably predicted by stoichiometry and can be fractional, negative, or zero. The overall order is the sum of orders, and it fixes the units of k.
- The method of initial rates finds the orders by comparing initial rates between trials in which one reactant concentration is varied while the others are held constant.
- Integrated rate laws relate concentration to time: first order gives ln[A]ₜ = −kt + ln[A]₀ (linear in ln[A] vs t; constant half-life t½ = 0.693/k); second order gives 1/[A]ₜ = kt + 1/[A]₀ (linear in 1/[A] vs t; t½ = 1/(k[A]₀)); zero order gives [A]ₜ = −kt + [A]₀ (linear in [A] vs t; t½ = [A]₀/2k). The order is identified by which plot is linear.
- Collision theory: reaction requires collisions that are frequent enough, correctly oriented, and energetic enough to exceed the activation energy Eₐ; a successful collision passes through a high-energy, short-lived activated complex (transition state). A catalyst lowers Eₐ but does not change ΔH.
- The Arrhenius equation k = A·e^(−Eₐ/RT) relates the rate constant to activation energy, temperature, and the frequency factor A (collision frequency × orientation). Its linear form ln k = (−Eₐ/R)(1/T) + ln A gives Eₐ from the slope of ln k vs 1/T; a two-temperature form gives Eₐ from two rate constants.
- A reaction mechanism is a sequence of elementary reactions that sum to the overall equation; the rate law of an elementary step can be written directly from its molecularity (unimolecular, bimolecular, termolecular), unlike overall reactions. Intermediates appear and are consumed within the mechanism. The slowest step is the rate-determining step and sets the overall rate; a fast pre-equilibrium lets an intermediate's concentration be substituted out.
- A catalyst speeds a reaction by providing a lower-Eₐ alternative pathway without being consumed and without shifting equilibrium. Homogeneous catalysts share the reactants' phase (e.g., NO- or Cl-catalyzed ozone decomposition); heterogeneous catalysts work on a solid surface via adsorption–reaction–desorption (e.g., catalytic converters, Haber/industrial synthesis); enzymes are protein catalysts acting on substrates at an active site (lock-and-key / induced fit).

## Key Quotes
> "Chemical kinetics is the study of the rate at which a reaction yields products and the molecular-scale means by which a reaction occurs." — chapter introduction
> "For many chemical processes, reaction rates are approximately doubled when the temperature is raised by 10 °C." — 12.2
> "Rate laws are determined by experiment only and are not reliably predicted by reaction stoichiometry." — 12.3
> "The reacting species must collide in an orientation that allows contact between the atoms that will become bonded together in the product." — 12.5 (collision theory)
> "The rate law for an elementary reaction may be derived directly from the balanced chemical equation describing the reaction." — 12.6
> "A catalyst is a substance that can increase the reaction rate without being consumed in the reaction." — 12.7

## Connections
- [[ReactionRate]] — average/instantaneous/initial rate and relative rates via stoichiometry (12.1)
- [[FactorsAffectingReactionRates]] — nature, state/surface area, temperature, concentration, catalyst (12.2)
- [[RateLaw]] — rate = k[A]^m[B]^n; experimentally determined orders (12.3)
- [[RateConstant]] — k, its temperature dependence and order-dependent units (12.3)
- [[ReactionOrder]] — order in a reactant, overall order, method of initial rates (12.3)
- [[IntegratedRateLaw]] — zero/first/second-order concentration-vs-time forms and linear plots (12.4)
- [[ReactionHalfLife]] — t½ for each order; constant for first order (12.4)
- [[CollisionTheory]] — frequency, orientation, energy requirements for reaction (12.5)
- [[ActivationEnergy]] — the energy barrier Eₐ to reaction (12.5)
- [[ArrheniusEquation]] — k = A·e^(−Eₐ/RT); frequency factor; ln k vs 1/T (12.5)
- [[TransitionState]] — activated complex; reaction energy diagrams (12.5)
- [[ReactionMechanism]] — stepwise path summing to the overall reaction (12.6)
- [[ElementaryReaction]] — molecularity and rate laws from the equation (12.6)
- [[RateDeterminingStep]] — slowest step sets the overall rate; pre-equilibrium (12.6)
- [[Catalysis]] — lower-Eₐ pathway; homogeneous/heterogeneous/enzymes (12.7)
- [[KineticMolecularTheory]] — temperature ∝ molecular KE underlies the temperature effect on rate
- [[KineticEnergy]] — distribution of molecular energies relative to Eₐ
- [[Molarity]] — molar concentration used throughout the rate expressions
- [[ChemicalEquation]] — overall vs elementary equations; mechanisms must sum to it
- [[EnthalpyChemistry]] — ΔH on reaction energy diagrams; unchanged by catalysts
- [[OxidationReduction]] — redox enzymes (oxidoreductases) and catalytic-converter reactions
- [[IntermolecularForces]] — physical state/contact between reactant phases

## Contradictions
None identified. Half-life here is a chemical-kinetics concept (decay of reactant concentration), distinct from the radioactivity/ML-decay uses of "half-life" elsewhere in the wiki; a chemistry-explicit [[ReactionHalfLife]] page keeps the domains separate. Activation energy here (a thermochemical reaction barrier) is unrelated to the neural-network [[ActivationFunction]] page.
