# Chemistry 2e — Chapter 16: Thermodynamics

> Source: https://openstax.org/books/chemistry-2e/pages/16-introduction

Thermodynamics, the study of relationships between the energy and work associated with chemical and physical processes, provides the ability to predict whether a process will occur under specified conditions. This chapter builds on prior thermochemistry concepts (Chapter 5) to introduce additional thermodynamic principles — entropy, the second and third laws, and free energy — that enable forecasting of chemical and physical transformations given particular environmental parameters.

Sections:
- 16.1 Spontaneity
- 16.2 Entropy
- 16.3 The Second and Third Laws of Thermodynamics
- 16.4 Free Energy

## 16.1 Spontaneity

### Core Definitions
- **Spontaneous process**: a process that occurs naturally under certain conditions, without requiring external energy input.
- **Nonspontaneous process**: a process that will not take place unless it is "driven" by the continual input of energy from an external source.

Directionality: a process spontaneous in one direction under given conditions is nonspontaneous in the reverse direction under those same conditions. At room temperature and atmospheric pressure, ice melts spontaneously, but liquid water does not spontaneously freeze.

### Spontaneity vs. Speed
"The spontaneity of a process is *not* correlated to the speed of the process." Spontaneous changes may be effectively instantaneous or so slow as to be unobservable on practical timescales. Spontaneity is a thermodynamic concept; rate is a kinetic concept.

Examples of varying rate:
- **Technetium-99m**: relatively rapid radioactive decay, half-life ≈ 6 hours.
- **Uranium-238**: very slow decay, half-life > 4 billion years.
- **Diamond → graphite**: C(s, diamond) ⟶ C(s, graphite) is thermodynamically spontaneous at ambient pressure, yet proceeds immeasurably slowly at low-to-moderate temperatures. Diamond is *thermodynamically unstable* but *kinetically stable* under ambient conditions.

### Dispersal of Matter and Energy

**Gas expansion into vacuum.** An isolated system: ideal gas in one flask connected by a closed valve to an evacuated flask. Opening the valve, the gas spontaneously expands to fill both flasks uniformly.
- Expansion against vacuum: w = −PΔV = 0 (P = 0 in a vacuum)
- Isolated system exchanges no heat: q = 0
- Therefore ΔU = q + w = 0 + 0 = 0

The process is spontaneous despite ΔU = 0; the driving change is the "greater, more uniform dispersal of matter" (gas distributed across twice the volume).

**Heat flow.** Two objects at different temperatures (object X at T_X, object Y at T_Y, with T_X > T_Y). Heat spontaneously flows hot → cold:
- q_X < 0 and q_Y = −q_X > 0
- No net thermal energy change for the system; the available thermal energy is *redistributed*, giving "more uniform dispersal of energy."

### Key Principle
Spontaneity correlates with "the extent to which [a process] changes the dispersal or distribution of matter and/or energy." Spontaneous processes consistently produce a more uniform distribution of matter and/or energy.

### Example 16.1 — Redistribution of Matter
- **(a) Sublimation (solid → gas)**: much greater dispersal of matter (molecules occupy a much greater volume).
- **(b) Condensation (gas → liquid)**: much lesser dispersal of matter.
- **(c) Food coloring diffusing in water**: more uniform dispersal of matter (initial state has two concentration regions; final state has a single uniform concentration).
- **Application — spoon in hot coffee**: heat spontaneously flows from the hotter coffee to the colder spoon, giving a more uniform distribution of thermal energy.

## 16.2 Entropy

### Definition and History
Entropy (S) was introduced by **Rudolf Clausius**, building on **Sadi Carnot's** study of steam-engine efficiency. It is a thermodynamic state property relating the spontaneous heat flow accompanying a process to the temperature at which the process occurs.

Reversible entropy change:

**ΔS = q_rev / T**

where q_rev is reversible heat and T is absolute temperature (K). The entropy change for a real, irreversible process equals that of the theoretical reversible process between the same initial and final states (S is a state function).

### Entropy and Microstates (Boltzmann)
**Ludwig Boltzmann** developed a statistical model relating entropy to the number of microstates (W) available to a system. A **microstate** is a specific configuration of all the locations and energies of the atoms or molecules of a system. A **macrostate** is the observable bulk condition (e.g., P, T, V); many microstates map to one macrostate.

**S = k ln W**

where k is the **Boltzmann constant, k = 1.38 × 10⁻²³ J/K**.

Entropy change between states:

**ΔS = S_f − S_i = k ln(W_f / W_i)**

- W_f > W_i ⇒ ΔS > 0 (entropy increases)
- W_f < W_i ⇒ ΔS < 0 (entropy decreases)

The most probable distribution (most evenly dispersed) corresponds to the greatest number of microstates and thus the greatest entropy. Configurations with all particles in one box are most ordered (least entropy); evenly distributed configurations are most disordered (greatest entropy).

**Worked microstate example.** Four particles distributed between two boxes: initial state (all four in one box) = 1 microstate; final state (even distribution, 2 and 2) = 6 microstates.
- ΔS = (1.38 × 10⁻²³ J/K) × ln(6/1) = 2.47 × 10⁻²³ J/K (positive, reflecting increased microstates).

### Factors Affecting Entropy
**Phase**: S_gas > S_liquid > S_solid. Solids fix atoms near lattice positions; liquids allow movement over and around each other; gases occupy much greater volume.
- Melting, vaporization, sublimation: ΔS > 0.
- Freezing, condensation, deposition: ΔS < 0.

**Temperature**: Higher T ⇒ more extensive vibrations and a broader (more dispersed) distribution of kinetic energies; entropy of any substance increases with temperature.

**Particle characteristics**: At a given temperature, heavier atoms possess greater entropy than lighter atoms; molecules with more atoms have more vibrational modes ⇒ more microstates ⇒ greater entropy.

**Mixtures**: A mixture of two or more particle types has greater entropy than a pure substance, due to additional orientations and interactions among nonidentical components.

**Dissolution**: When a solid dissolves in a liquid, the solid's particles gain freedom of motion and new solvent interactions — more uniform dispersal, more microstates — so dissolution generally involves ΔS > 0.

### Example 16.3 — Predicting the Sign of ΔS
- **(a)** Liquid water (room temp) → liquid water (50 °C): **positive** (temperature increase).
- **(b)** Ag⁺(aq) + Cl⁻(aq) → AgCl(s): **negative** (fewer particles in solution, decreased dispersal of matter).
- **(c)** C₆H₆(l) + 15/2 O₂(g) → 6 CO₂(g) + 3 H₂O(l): **negative** (net decrease in moles of gaseous species).
- **(d)** NH₃(s) → NH₃(l): **positive** (solid → liquid phase transition, net increase in dispersal of matter).

## 16.3 The Second and Third Laws of Thermodynamics

### The Second Law of Thermodynamics
The second law relates entropy change to spontaneity via the total entropy of the universe:

**ΔS_univ = ΔS_sys + ΔS_surr**

Statement: all spontaneous changes cause an increase in the entropy of the universe.

| Condition | Process status |
|---|---|
| ΔS_univ > 0 | Spontaneous |
| ΔS_univ < 0 | Nonspontaneous (spontaneous in reverse) |
| ΔS_univ = 0 | At equilibrium |

When the surroundings are vast relative to the system (constant T), the surroundings' entropy change is:

**ΔS_surr = q_surr / T = −q_sys / T = −ΔH_sys / T** (at constant pressure)

so

**ΔS_univ = ΔS_sys + q_surr / T**

**Worked example — ice melting.** H₂O(s) → H₂O(l) with ΔS_sys = 22.1 J/K and q_surr = −6.00 kJ:
- At −10.00 °C (263.15 K): ΔS_univ ≈ −0.7 J/K → nonspontaneous.
- At +10.00 °C (283.15 K): ΔS_univ ≈ +0.9 J/K → spontaneous.
(For freezing the signs reverse, with opposite results at each temperature.)

### The Third Law of Thermodynamics
Statement: the entropy of a pure, perfect crystalline substance at 0 K is zero. From the Boltzmann equation, a perfect crystal at 0 K has a single accessible microstate (W = 1):

S = k ln(W) = k ln(1) = 0

This zero reference allows determination of absolute (not merely relative) entropies.

### Standard Molar Entropy and ΔS°
**Standard entropy (S°)** (standard molar entropy): the entropy of one mole of a substance under standard conditions (1 bar, conventionally 298.15 K). Units: J mol⁻¹ K⁻¹. Unlike ΔHf°, standard molar entropies are nonzero for elements in their standard states (a consequence of the third-law absolute reference).

**Standard entropy change of reaction:**

**ΔS° = Σ ν S°(products) − Σ ν S°(reactants)**

where ν are stoichiometric coefficients.

- **Example — condensation of water.** H₂O(g) → H₂O(l): ΔS° = (1 mol)(70.0 J mol⁻¹ K⁻¹) − (1 mol)(188.8 J mol⁻¹ K⁻¹) = −118.8 J/K (negative, as expected for a transition to a higher-density phase).
- **Example — methanol combustion.** 2 CH₃OH(l) + 3 O₂(g) → 2 CO₂(g) + 4 H₂O(l): ΔS° = [2(213.8) + 4(70.0)] − [2(126.8) + 3(205.2)] = −161.6 J/K.

## 16.4 Free Energy

### Gibbs Free Energy
**Gibbs free energy (G)** (named for **Josiah Willard Gibbs**):

**G = H − TS**

where H is enthalpy, T is absolute temperature, and S is entropy. The change at constant temperature and pressure:

**ΔG = ΔH − TΔS**

G is a state function, so ΔG is path-independent.

### Derivation from the Second Law
Starting from ΔS_univ = ΔS_sys − ΔH/T (substituting ΔS_surr = −ΔH/T) and multiplying both sides by −T:

**ΔG = −TΔS_univ**

Because ΔS_univ governs spontaneity, ΔG is a reliable, system-only spontaneity indicator.

### Spontaneity Criterion
| Condition | Interpretation |
|---|---|
| ΔG < 0 | Spontaneous |
| ΔG = 0 | At equilibrium |
| ΔG > 0 | Nonspontaneous |

### Standard Free Energy Change and Free Energy of Formation
**ΔG° = ΔH° − TΔS°**

**Standard free energy of formation (ΔGf°)**: the free energy change for forming one mole of a substance from its elements in their standard states. ΔGf° = 0 for an element in its standard state.

For mA + nB → xC + yD:

**ΔG° = Σ ν ΔGf°(products) − Σ ν ΔGf°(reactants)**
**ΔG° = [x ΔGf°(C) + y ΔGf°(D)] − [m ΔGf°(A) + n ΔGf°(B)]**

Both methods (ΔG° = ΔH° − TΔS° using ΔHf° and S° tables, or ΔG° from ΔGf° tables) yield the same result.

### Temperature Dependence of Spontaneity — Four Cases
| Case | ΔH | ΔS | Behavior |
|---|---|---|---|
| 1 | > 0 (endothermic) | > 0 | Spontaneous at high T, nonspontaneous at low T (ΔG < 0 when TΔS > ΔH) |
| 2 | < 0 (exothermic) | < 0 | Spontaneous at low T, nonspontaneous at high T (ΔG < 0 when \|TΔS\| < \|ΔH\|) |
| 3 | > 0 (endothermic) | < 0 | Nonspontaneous at all T (ΔG > 0 always) |
| 4 | < 0 (exothermic) | > 0 | Spontaneous at all T (ΔG < 0 always) |

**Temperature crossover / threshold.** When ΔH and ΔS have the *same* sign, there is a transition temperature where ΔG = 0 (system at equilibrium):

**T = ΔH / ΔS**

Above/below this temperature the sign of ΔG flips, determining the direction of spontaneity. (A phase change's normal transition temperature, e.g. a boiling point, is the T where ΔG = 0; thermodynamic estimates closely match experiment.)

### Relationship to the Equilibrium Constant
**ΔG° = −RT ln K**, equivalently **K = e^(−ΔG°/RT)**, with R = 8.314 J mol⁻¹ K⁻¹.

| K | ΔG° |
|---|---|
| K > 1 | ΔG° < 0 (products favored) |
| K < 1 | ΔG° > 0 (reactants favored) |
| K = 1 | ΔG° = 0 (comparable amounts) |

### Nonstandard Conditions
**ΔG = ΔG° + RT ln Q**

where Q is the reaction quotient. This predicts spontaneity under any conditions: Q < K ⇒ reaction proceeds forward (ΔG < 0); Q > K ⇒ reaction proceeds in reverse (ΔG > 0); Q = K ⇒ equilibrium (ΔG = 0).

### Key Takeaways from Examples
- ΔG° computed two ways (ΔH° − TΔS° vs. ΔGf° sums) gives identical results.
- **Coupled reactions**: a nonspontaneous reaction can be driven by coupling it to a spontaneous one; free energy changes add algebraically.
- **Phase transitions**: the normal boiling point is the T where ΔG = 0; thermodynamic estimates closely match measured values.
- **Solubility products**: Ksp can be derived from ΔG° via K = e^(−ΔG°/RT).
