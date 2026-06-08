---
title: "Standard Reduction (Electrode) Potential (E°)"
type: concept
tags: [chemistry, general-chemistry, electrochemistry, redox]
sources: [chemistry-2e-ch17-electrochemistry]
last_updated: 2026-06-07
---

# Standard Reduction (Electrode) Potential (E°)

The **standard electrode potential (E°_X)** of a half-cell — by convention always tabulated as a **reduction** — is the [[CellPotential|cell potential]] measured when that half-cell X acts as the **cathode** against a [[StandardHydrogenElectrode|standard hydrogen electrode (SHE)]] acting as the anode, with all species in their standard states:
$$E_\text{cell} = E_X - E_\text{SHE}, \quad E_\text{SHE} \equiv 0\text{ V} \;\Rightarrow\; E_\text{cell} = E_X$$

A single absolute electrode potential is not measurable; assigning **E°(SHE) = 0 V** makes every other half-cell's value definite relative to it.

## Interpreting the Values
Because the potentials describe **reduction**:
- A **more positive E°** = stronger driving force to be reduced = **stronger oxidizing agent** (the species itself is the oxidant).
- A **negative E°** = weaker oxidant than H⁺; such a species is more easily oxidized (a better reducing agent).

Tables list values in descending order — strongest oxidant (most positive, e.g., F₂ at +2.866 V) at top, weakest at bottom (e.g., Zn²⁺/Zn at −0.7618 V).

| Half-Reaction | E° (V) |
|---|---|
| F₂(g) + 2e⁻ → 2F⁻(aq) | +2.866 |
| Cu²⁺(aq) + 2e⁻ → Cu(s) | +0.34 |
| 2H⁺(aq) + 2e⁻ → H₂(g) | 0.00 (SHE) |
| Pb²⁺(aq) + 2e⁻ → Pb(s) | −0.1262 |
| Zn²⁺(aq) + 2e⁻ → Zn(s) | −0.7618 |

## Use: Predicting Spontaneity
Combine two half-cells with E°cell = E°cathode − E°anode. If the oxidant's entry sits **above** the reductant's in the table, E°cell > 0 and the reaction is spontaneous. Values are **intensive** — never scaled by stoichiometric coefficients. For nonstandard states, apply the [[NernstEquation|Nernst equation]].

## Connections
- [[StandardHydrogenElectrode]] — the 0 V reference that anchors the scale
- [[CellPotential]] — E°cell built from two of these values
- [[NernstEquation]] — adjusts E for nonstandard conditions
- [[OxidationReduction]] — oxidant/reductant strength the values rank
- [[GibbsFreeEnergy]] — ΔG° = −nFE°cell links these to free energy
- [[Electrochemistry]] — the broader field
- [[chemistry-2e-ch17-electrochemistry]] — source chapter (§17.3)
