---
title: "Chemistry 2e — Ch 17: Electrochemistry"
type: source
tags: [chemistry, textbook, openstax, general-chemistry]
date: 2026-06-07
source_file: raw/chemistry-2e/17-electrochemistry.md
---

## Summary
Chapter 17 of OpenStax *Chemistry 2e* develops electrochemistry — the use of [[OxidationReduction|redox]] reactions to do or consume electrical work. It reviews redox balancing by the half-reaction method (17.1), builds [[GalvanicCell|galvanic cells]] with anode/cathode/salt bridge and cell notation (17.2), defines [[CellPotential|cell]] and [[StandardReductionPotential|standard reduction potentials]] referenced to the [[StandardHydrogenElectrode|standard hydrogen electrode]] (17.3), connects E°cell to free energy and equilibrium via ΔG° = −nFE°cell, E°cell = (RT/nF)ln K, and the [[NernstEquation]] (17.4), surveys [[ElectrochemicalBattery|batteries]] and [[FuelCell|fuel cells]] (17.5), explains [[MetalCorrosion|corrosion]] and [[CathodicProtection|cathodic protection]] (17.6), and treats [[ElectrolysisChemistry|electrolysis]] and the stoichiometry of electrolytic deposition via Q = It = nF (17.7).

## Key Claims
- A redox reaction entails a change in [[OxidationNumber|oxidation number]] for one or more elements; aqueous redox equations are balanced by the eight-step half-reaction method (balance non-H/O atoms, then O with H₂O, H with H⁺, charge with e⁻, scale, add; in base, neutralize H⁺ with OH⁻).
- A [[GalvanicCell|galvanic (voltaic) cell]] houses a spontaneous redox reaction in two half-cells: oxidation at the **anode**, reduction at the **cathode**, with electrons flowing anode→cathode through the external circuit and a **salt bridge** maintaining charge balance.
- [[ElectrochemicalCellNotation|Cell notation]] runs anode (left) → cathode (right); │ marks phase interfaces, comma marks same-phase components, ║ marks the salt bridge; inert (Pt) electrodes are used when no couple member can serve as the electrode.
- Only differences in half-cell potential are measurable: E_cell = E_cathode − E_anode. The [[StandardHydrogenElectrode|SHE]] (2H⁺ + 2e⁻ → H₂) is defined as exactly 0 V; relative to it, each half-cell has a [[StandardReductionPotential|standard reduction potential E°]].
- Larger (more positive) E° = stronger oxidant. E°cell > 0 (cathode E° > anode E°) ⇒ spontaneous; reversing a reaction flips the sign of E°cell. Standard electrode potentials are intensive and are not scaled by stoichiometric coefficients.
- Cell potential ties to thermodynamics: ΔG° = −nF·E°cell with F = 96,485 C/mol; E°cell = (RT/nF)ln K = (0.0592 V/n)log K at 298 K. Positive E°cell ⇔ negative ΔG° ⇔ K > 1 (spontaneous, products favored).
- The [[NernstEquation]] gives the potential at nonstandard conditions: E_cell = E°cell − (RT/nF)ln Q = E°cell − (0.0592 V/n)log Q at 298 K. A [[ConcentrationCell|concentration cell]] (E°cell = 0) is driven purely by the concentration difference of one species.
- Batteries are purpose-built galvanic cells: **primary** (non-rechargeable: zinc-carbon dry cell ~1.5 V, alkaline ~1.43 V) vs **secondary** (rechargeable: NiCd ~1.2 V, [[LithiumIonBattery|lithium-ion]] ~3.7 V, [[LeadAcidBattery|lead-acid]] ~2 V/cell, 12 V from six cells). [[FuelCell|Fuel cells]] (e.g., H₂/O₂, ~1.2 V) feed fuel and oxidant continuously, at 50–75% efficiency.
- [[MetalCorrosion|Corrosion]] is electrochemical metal degradation; iron rusting is a galvanic process (Fe anode E° = −0.44 V; O₂/H₂O cathode E° = +1.23 V; E°cell = +1.67 V). Rust flakes off (no protection); copper patina and stainless-steel chromium oxide passivate. [[CathodicProtection|Cathodic protection]] uses a sacrificial anode (Zn, Mg) to oxidize in place of the protected metal.
- [[ElectrolysisChemistry|Electrolysis]] forces a nonspontaneous redox reaction with an applied voltage exceeding |E°cell| (e.g., molten NaCl in a Downs cell; water needs > +1.229 V; aqueous NaCl yields H₂ + Cl₂ + OH⁻ via the chlor-alkali process).
- Stoichiometry of electrolysis: Q = I·t and Q = n·F, so moles of electrons (and hence mass deposited via the half-reaction's e⁻ count) follow from current and time — [[FaradaysLawsOfElectrolysis|Faraday's laws of electrolysis]].

## Key Quotes
> "Galvanic cells, also known as voltaic cells, are electrochemical cells in which a spontaneous redox reaction takes place." — 17.2
> "Corrosion is usually defined as the degradation of metals by a naturally occurring electrochemical process." — 17.6
> "an external circuit does work on a redox system" vs. "electrical work is done by a redox system on its surroundings" — 17.7, electrolytic vs galvanic cells

## Connections
- [[Electrochemistry]] — the field this chapter develops (overview hub)
- [[OxidationReduction]] / [[OxidationNumber]] — redox foundations extended with the 17.1 half-reaction review
- [[GalvanicCell]] / [[ElectrochemicalCell]] — voltaic cells and the general cell concept (17.2)
- [[ElectrochemicalCellNotation]] — anode║cathode schematic convention (17.2)
- [[CellPotential]] / [[StandardReductionPotential]] / [[StandardHydrogenElectrode]] — measuring redox driving force (17.3)
- [[NernstEquation]] / [[ConcentrationCell]] — nonstandard-condition potentials (17.4)
- [[GibbsFreeEnergy]] / [[GibbsFreeEnergyAndEquilibrium]] / [[StandardFreeEnergyOfFormation]] — ΔG°, K linked to E°cell via ΔG° = −nFE°cell (17.4)
- [[ElectrochemicalBattery]] / [[LeadAcidBattery]] / [[LithiumIonBattery]] / [[FuelCell]] — practical cells (17.5)
- [[MetalCorrosion]] / [[CathodicProtection]] — corrosion and its prevention (17.6)
- [[ElectrolysisChemistry]] / [[FaradaysLawsOfElectrolysis]] — driving and quantifying nonspontaneous redox (17.7)
- [[MichaelFaraday]] — namesake of the Faraday constant and laws of electrolysis
- [[Electrolyte]] — the ion-conducting medium in every electrochemical cell
- [[EquilibriumConstant]] / [[ReactionQuotient]] — K and Q in the E°cell/Nernst relationships
- [[chemistry-2e-ch16-thermodynamics]] — prerequisite thermodynamics (ΔG°, ΔG° = −RT ln K)
- [[chemistry-2e-ch04-stoichiometry-chemical-reactions]] — first introduction of redox and oxidation numbers

## Contradictions
None identified. The chemistry treatment of potential (E in volts = J/C, electrode/cell potentials for redox) is consistent with — and distinct in scope from — the physics treatment of [[Voltage]] / [[ElectricPotential]] in College Physics 2e: chemistry assigns potentials to redox half-cells relative to the SHE, while physics defines electric potential as potential energy per unit charge in a field. [[MichaelFaraday]] is the shared namesake (electrolysis laws here; electromagnetic induction in physics).
