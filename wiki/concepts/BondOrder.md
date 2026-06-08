---
title: "Bond Order"
type: concept
tags: [chemistry, general-chemistry, bonding, quantum-chemistry]
sources: [chemistry-2e-ch08-advanced-theories-covalent-bonding]
last_updated: 2026-06-07
---

# Bond Order

**Bond order** is a [[MolecularOrbitalTheory|molecular orbital theory]] metric for the number of chemical bonds between two atoms, computed from the occupancy of [[BondingAndAntibondingOrbitals|bonding and antibonding orbitals]]. It guides bond strength: a bond between two given atoms grows stronger as its bond order increases, and a bond order of **zero** means no stable molecule forms. (Named *BondOrder* to keep the chemistry sense distinct.)

## Formula

$$\text{bond order} = \frac{(\text{bonding electrons}) - (\text{antibonding electrons})}{2}$$

Antibonding (destabilizing) electrons are subtracted from bonding (stabilizing) electrons, and the difference is divided by two because each bond is two electrons.

## Worked Cases (Homonuclear Diatomics)

Reading occupancy off a [[MODiagram|MO diagram]]:

| Molecule | Configuration (summary) | Bond order | Stable? |
|---|---|---|---|
| H₂ | (σ₁ₛ)² | 1 | yes |
| He₂ | (σ₁ₛ)²(σ₁ₛ*)² | 0 | no |
| Li₂ | (σ₂ₛ)² | 1 | yes |
| Be₂ | (σ₂ₛ)²(σ₂ₛ*)² | 0 | no |
| B₂ | …(π₂ₚ)² | 1 | yes |
| C₂ | …(π₂ₚ)⁴ | 2 | yes |
| N₂ | …(π₂ₚ)⁴(σ₂ₚ)² | 3 | yes |
| O₂ | …(σ₂ₚ)²(π₂ₚ)⁴(π₂ₚ*)² | 2 | yes |
| F₂ | …(π₂ₚ*)⁴ | 1 | yes |
| Ne₂ | …(σ₂ₚ*)² | 0 | no |

He₂, Be₂, and Ne₂ have equal bonding and antibonding electrons → bond order 0 → they exist only as separate atoms. O₂'s bond order of 2 (a double bond) coexists with two unpaired electrons, making it [[Paramagnetism|paramagnetic]].

## Connections
- [[MolecularOrbitalTheory]] — the framework bond order comes from
- [[BondingAndAntibondingOrbitals]] — the electrons counted in the formula
- [[MODiagram]] — the occupancy diagram bond order is read from
- [[Paramagnetism]] — O₂ has bond order 2 yet unpaired electrons
- [[BondEnergy]] — bond order tracks bond strength and (inversely) length
- [[chemistry-2e-ch08-advanced-theories-covalent-bonding]] — source chapter
