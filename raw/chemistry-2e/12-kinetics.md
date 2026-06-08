# Chemistry 2e — Chapter 12: Kinetics

> Source: https://openstax.org/books/chemistry-2e/pages/12-introduction

## Introduction

Chemists ask three fundamental questions about reactions: (1) Will the desired products form in useful quantities? (2) How rapidly will the reaction occur? (3) What molecular-level processes occur during the reaction? The field of **chemical kinetics** addresses the latter two questions, examining "the rate at which a reaction yields products and the molecular-scale means by which a reaction occurs." This chapter explores the factors that affect reaction rates, reaction mechanisms, and quantitative methods for describing reaction rates. (The chapter opens with the example of a cold-blooded lizard relying on the sun's heat, because warmer temperatures accelerate the chemical reactions controlling muscle movement.)

Sections:
- 12.1 Chemical Reaction Rates
- 12.2 Factors Affecting Reaction Rates
- 12.3 Rate Laws
- 12.4 Integrated Rate Laws
- 12.5 Collision Theory
- 12.6 Reaction Mechanisms
- 12.7 Catalysis

## 12.1 Chemical Reaction Rates

A **rate** is a measure of how some property varies with time. The **rate of a chemical reaction** is a measure of how much reactant is consumed, or how much product is produced, by the reaction in a given amount of time. Reaction rates are determined by measuring the time dependence of some property related to reactant or product amounts:
- volume or pressure changes for gaseous substances
- light absorption for colored substances
- conductivity changes for aqueous electrolytes
- concentration changes for solutions

### Rate expressions

For reactants and products in solution, concentration (molar) is used. For the decomposition of hydrogen peroxide:

$$\text{rate of decomposition of } \mathrm{H_2O_2} = -\frac{\Delta[\mathrm{H_2O_2}]}{\Delta t}$$

- Brackets `[ ]` indicate molar concentrations.
- Δ (delta) indicates "change in."
- The negative sign converts the (negative) change in reactant concentration into a positive rate value. Product-formation rates use a positive sign.

### Types of rate

- **Average rate**: the rate over a specific time interval, computed by dividing the change in concentration by the corresponding time increment.
- **Instantaneous rate**: the rate at which a reaction proceeds at a specific moment in time. On a concentration-vs-time plot, the instantaneous rate at time *t* equals the slope of the line tangent to the curve at that time. The curve becomes less steep as the reaction proceeds, showing the reaction slows over time.
- **Initial rate**: the instantaneous rate at time zero, when the reaction commences.

### Relative rates of reaction (stoichiometry)

For the general reaction $aA \rightarrow bB$, the rate expressions for reactants and products relate through the stoichiometric coefficients:

$$\text{rate} = -\frac{1}{a}\frac{\Delta[A]}{\Delta t} = \frac{1}{b}\frac{\Delta[B]}{\Delta t}$$

For a complete reaction $aA + bB \rightarrow cC + dD$ in a single volume:

$$-\frac{1}{a}\frac{\Delta[A]}{\Delta t} = -\frac{1}{b}\frac{\Delta[B]}{\Delta t} = \frac{1}{c}\frac{\Delta[C]}{\Delta t} = \frac{1}{d}\frac{\Delta[D]}{\Delta t}$$

Example — ammonia decomposition $2\mathrm{NH_3}(g) \rightarrow \mathrm{N_2}(g) + 3\mathrm{H_2}(g)$:

$$-\frac{1}{2}\frac{\Delta[\mathrm{NH_3}]}{\Delta t} = \frac{\Delta[\mathrm{N_2}]}{\Delta t} \qquad \frac{1}{3}\frac{\Delta[\mathrm{H_2}]}{\Delta t} = \frac{\Delta[\mathrm{N_2}]}{\Delta t}$$

The rate of formation of H₂ is three times the rate of formation of N₂ because three moles of H₂ are produced per mole of N₂.

**Worked example (H₂O₂ decomposition):** For $2\mathrm{H_2O_2} \rightarrow 2\mathrm{H_2O} + \mathrm{O_2}$, given an instantaneous decomposition rate of $3.20\times10^{-2}$ mol L⁻¹ h⁻¹ at t = 11.1 h:
- $\Delta[\mathrm{O_2}]/\Delta t = \tfrac{1}{2}(3.20\times10^{-2}) = 1.60\times10^{-2}$ mol L⁻¹ h⁻¹
- $\Delta[\mathrm{H_2O}]/\Delta t = 2(1.60\times10^{-2}) = 3.20\times10^{-2}$ mol L⁻¹ h⁻¹

## 12.2 Factors Affecting Reaction Rates

Five factors influence the frequency and effectiveness of collisions, and therefore reaction rates:

1. **Chemical nature of the reacting substances.** The rate depends fundamentally on which substances react. Sodium reacts completely with air overnight while iron is barely affected. Calcium and sodium both react with water to give H₂ and a base, but calcium reacts moderately while sodium reacts explosively.

2. **Physical states of the reactants.** Reactions require intimate contact between reactants. When reactants are in different phases, reaction occurs only at the interface between phases. **Surface area**: smaller particles react faster because increased surface area provides greater contact. Iron powder reacts rapidly with dilute HCl while an iron nail reacts slowly; sawdust burns explosively while large wood pieces only smolder. (Example: Fe(s) + 2HCl(aq) ⟶ FeCl₂(aq) + H₂(g).)

3. **Temperature of the reactants.** Higher temperatures accelerate reactions. "For many chemical processes, reaction rates are approximately doubled when the temperature is raised by 10 °C." (E.g., food spoils quickly at room temperature but lasts days refrigerated.)

4. **Concentrations of the reactants.** Rates typically increase as reactant concentrations rise, because higher concentrations mean more frequent molecular collisions. Example: SO₂(g) + H₂O(g) ⟶ H₂SO₃(aq), then CaCO₃(s) + H₂SO₃(aq) ⟶ CaSO₃(aq) + CO₂(g) + H₂O(l); carbonate stone deteriorates faster in polluted (high-SO₂) air. Phosphorus burns faster in pure O₂ than in air (~20% O₂).

5. **Presence of a catalyst.** "Substances that function to increase the rate of a reaction are called catalysts." Dilute hydrogen peroxide decomposes slowly (2H₂O₂(aq) ⟶ 2H₂O(l) + O₂(g)), but biological catalysts in exposed tissue make it foam vigorously on a wound.

Underlying principle: chemical reactions occur when molecules collide and undergo a chemical transformation; all five factors affect the frequency and effectiveness of those collisions.

## 12.3 Rate Laws

**Rate law (rate equation):** a mathematical expression describing the relationship between the rate of a chemical reaction and the concentrations of its reactants. General form:

$$\text{rate} = k[A]^m[B]^n\ldots$$

- **Rate constant (k):** the proportionality constant specific to a particular reaction at a particular temperature. It is independent of reactant concentrations but varies with temperature.
- **Reaction orders (m, n):** the exponents in the rate law. Usually small positive integers but can be fractional, negative, or zero. They **must be determined experimentally** and are not reliably predicted by stoichiometry.
- **Order with respect to a reactant:** the dependence of rate on that one reactant's concentration (the reaction is "m order in A and n order in B").
- **Overall reaction order:** the sum of all the individual orders (m + n + …).

Examples of rate-law forms:
- `rate = k[H₂O₂]` — first order in H₂O₂, first order overall
- `rate = k[C₄H₆]²` — second order in C₄H₆, second order overall
- `rate = k[H⁺][OH⁻]` — first order in each, second order overall

### Method of initial rates

An experimental procedure to determine orders and k:
1. Measure the initial rate for multiple trials with different initial reactant concentrations.
2. Compare rate ratios for pairs of trials in which only one reactant's concentration changes, holding others constant:

$$\frac{\text{rate}_x}{\text{rate}_y} = \frac{k[A]_x^m[B]_x^n}{k[A]_y^m[B]_y^n}$$

Solving (with logarithms if needed) gives each exponent.
3. Substitute a known rate and concentrations into the rate law to calculate k.

### Units of the rate constant (by overall order)

| Overall order | Units of k |
|---|---|
| 0 (zero) | mol L⁻¹ s⁻¹ |
| 1 (first) | s⁻¹ |
| 2 (second) | L mol⁻¹ s⁻¹ |
| 3 (third) | L² mol⁻² s⁻¹ |

General: units of k are $\mathrm{L}^{(x-1)}\,\mathrm{mol}^{(1-x)}\,\mathrm{s}^{-1}$, where x = overall order.

Key principles: rate laws are determined by experiment only and are not reliably predicted from reaction stoichiometry; reaction orders often differ from stoichiometric coefficients; fractional and negative orders can occur; a concentration term raised to the zero power equals 1 and is omitted.

## 12.4 Integrated Rate Laws

Integrated rate laws relate concentration to time (the differential rate laws above relate rate to concentration).

### First-order reactions

- Differential: rate = k[A]
- Integrated forms:
  $$[A]_t = [A]_0\,e^{-kt} \qquad \ln\frac{[A]_t}{[A]_0} = -kt \qquad \ln[A]_t = -kt + \ln[A]_0$$
- **Linear plot:** ln[A]ₜ vs t → slope = −k, y-intercept = ln[A]₀
- **Half-life:** $t_{1/2} = \dfrac{0.693}{k}$ — independent of initial concentration (constant for a given first-order reaction).

### Second-order reactions

- Differential: rate = k[A]²
- Integrated form:
  $$\frac{1}{[A]_t} = kt + \frac{1}{[A]_0}$$
- **Linear plot:** 1/[A]ₜ vs t → slope = k, y-intercept = 1/[A]₀
- **Half-life:** $t_{1/2} = \dfrac{1}{k[A]_0}$ — inversely proportional to initial concentration; increases as the reaction proceeds.

### Zero-order reactions

- Differential: rate = k (rate is constant, independent of concentration)
- Integrated form:
  $$[A]_t = -kt + [A]_0$$
- **Linear plot:** [A]ₜ vs t → slope = −k, y-intercept = [A]₀
- **Half-life:** $t_{1/2} = \dfrac{[A]_0}{2k}$ — directly proportional to initial concentration.

Which order a reaction follows is identified by which plot is linear (ln[A] vs t → first order; 1/[A] vs t → second order; [A] vs t → zero order); a non-linear plot rules out that order.

Worked-example takeaways:
- First-order decomposition of cyclobutane at 500 °C (k = 9.2×10⁻³ s⁻¹): time for 80% decomposition ≈ 1.7×10² s.
- Graphical determination: a linear plot of ln[H₂O₂] vs time indicates first-order kinetics; from it k = 0.116 h⁻¹.
- Second-order butadiene dimerization (k = 5.76×10⁻² L mol⁻¹ min⁻¹, [A]₀ = 0.200 M): after 10.0 min, [A]ₜ = 0.179 mol/L.

## 12.5 Collision Theory

"Atoms, molecules, or ions must collide before they can react with each other." **Collision theory** explains reaction kinetics and the factors affecting reaction rates. Its three postulates:

1. **Collision frequency:** the rate of reaction is proportional to the rate of reactant collisions (rate ∝ collisions per unit time).
2. **Orientation:** the colliding species must be oriented so that the atoms that will become bonded in the product are in contact.
3. **Energy:** the collision must occur with adequate energy to permit mutual penetration of the reacting species' valence shells, so electrons can rearrange and form new bonds.

**Activation energy (Eₐ):** the minimum energy necessary to form product during a collision between reactants. If Eₐ is much larger than the average molecular kinetic energy, only a small fraction of collisions succeed and the reaction is slow; a low Eₐ allows a fast reaction.

**Activated complex (transition state):** an unstable, very short-lived species (usually undetectable) formed when reactants collide with both proper orientation and adequate energy. It sits at the energy maximum between reactants and products.

**Reaction energy diagrams** (potential energy vs reaction coordinate) show:
- **Activation energy Eₐ:** energy difference between reactants and the transition state (the barrier).
- **Enthalpy change ΔH:** energy difference between reactants and products. Exothermic: ΔH < 0 (products lower than reactants); endothermic: ΔH > 0.

### The Arrhenius equation

$$k = A\,e^{-E_a/RT}$$

- k = rate constant
- A = **frequency factor** (related to the frequency of collisions and the orientation of reacting molecules; higher A = better conditions for properly oriented collisions)
- Eₐ = activation energy (J/mol)
- R = gas constant (8.314 J mol⁻¹ K⁻¹)
- T = temperature (K)
- e ≈ 2.7183

The exponential term $e^{-E_a/RT}$ is the fraction of molecules with enough energy to overcome the activation barrier; raising T increases that fraction. The factor A captures collision frequency and the orientation requirement.

**Linear (logarithmic) form:**

$$\ln k = \left(-\frac{E_a}{R}\right)\frac{1}{T} + \ln A$$

A plot of ln k vs 1/T is a straight line with slope = −Eₐ/R and y-intercept = ln A, so $E_a = -\text{slope}\times R$.

**Two-temperature form:**

$$\ln\frac{k_1}{k_2} = \frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$

which rearranges to let Eₐ be computed from two rate constants at two temperatures:

$$E_a = -R\,\frac{\ln k_2 - \ln k_1}{(1/T_2) - (1/T_1)}$$

## 12.6 Reaction Mechanisms

A **reaction mechanism** (reaction path) is the precise, step-by-step sequence of events by which a reaction occurs. A balanced overall equation shows what reacts and what is produced but reveals nothing about the actual process.

**Elementary reaction:** each step in a mechanism. Elementary reactions occur exactly as written, and they must sum to the balanced overall equation. Example (ozone decomposition):
- Step 1: O₃(g) → O₂(g) + O
- Step 2: O + O₃(g) → 2O₂(g)
- Overall: 2O₃(g) → 3O₂(g)

**Intermediate:** a species produced in one step and consumed in a later step; it does not appear in the overall equation. In the example, the O atom is an intermediate.

**Molecularity:** the number of reactant entities (atoms, molecules, or ions) in an elementary reaction.
- **Unimolecular** (one reactant): A → products; rate = k[A] (first order).
- **Bimolecular** (two reactants): A + B → products gives rate = k[A][B] (second order overall); 2A → products gives rate = k[A]² (second order in A).
- **Termolecular** (three reactants colliding simultaneously): e.g. 2NO + O₂ → 2NO₂, rate = k[NO]²[O₂]; 2NO + Cl₂ → 2NOCl, rate = k[NO]²[Cl₂]. Termolecular steps are uncommon because simultaneous three-body collisions are improbable.

**Key rule:** the rate law for an *elementary* reaction may be derived directly from its balanced equation (the orders equal the molecularities). This contrasts with overall reactions, whose rate laws must be determined experimentally.

**Rate-determining (rate-limiting) step:** when one step is much slower than the others, it limits the overall rate — a reaction can be no faster than its slowest step.

- **Slow first step:** the overall rate law equals the rate law of that slow first step. Example (NO₂ + CO below 225 °C):
  - Step 1 (slow): NO₂ + NO₂ → NO₃ + NO
  - Step 2 (fast): NO₃ + CO → NO₂ + CO₂
  - Overall: 2NO₂ + CO → CO₂ + NO; rate = k[NO₂]²
- **Fast initial equilibrium:** when the slow step is preceded by a fast reversible step, the intermediate's concentration is eliminated by setting forward = reverse rates. For NO + NO ⇌ N₂O₂: k₁[NO]² = k₋₁[N₂O₂], so [N₂O₂] = (k₁/k₋₁)[NO]². Intermediate concentrations cannot appear in the overall rate law, so this is substituted into the slow step.
  - Worked example: NO + Cl₂ ⇌ NOCl₂ (fast); NOCl₂ + NO → 2NOCl (slow); overall 2NO + Cl₂ → 2NOCl. With [NOCl₂] = (k₁/k₋₁)[NO][Cl₂], substituting into the slow step gives rate = (k₂k₁/k₋₁)[NO]²[Cl₂].

## 12.7 Catalysis

A **catalyst** is a substance that increases the reaction rate without being consumed in the reaction. It works by providing an alternative reaction mechanism with a lower activation energy.

- Catalysts are regenerated and not consumed overall.
- A catalyst does **not** change the reaction thermodynamics: it leaves ΔH (the energy difference between reactants and products) unchanged and lowers only the activation barrier. It speeds both the forward and reverse reactions, so it does not shift the position of equilibrium.
- On a reaction energy diagram, the catalyzed path (often a multi-step mechanism) has a lower Eₐ for its rate-determining step than the single-step uncatalyzed path.

### Homogeneous catalysts

Exist in the same phase as the reactants. They form an intermediate with a reactant that later decomposes or reacts, regenerating the catalyst.

- **Ozone decomposition catalyzed by NO** (vs uncatalyzed O₃ → O₂ + O; O + O₃ → 2O₂):
  - NO(g) + O₃(g) → NO₂(g) + O₂(g)
  - O₃(g) → O₂(g) + O(g)
  - NO₂(g) + O(g) → NO(g) + O₂(g)
  - Overall: 2O₃(g) → 3O₂(g)
- **Chlorine-catalyzed ozone destruction** (Cl from photochemical CFC breakdown):
  - Cl + O₃ → ClO + O₂
  - ClO + O → Cl + O₂
  - Overall: O₃ + O → 2O₂
  A single Cl atom can catalyze destruction of thousands of O₃ molecules. This work by Mario Molina and F. Sherwood Rowland earned the 1995 Nobel Prize in Chemistry and led to the Montreal Protocol.

### Heterogeneous catalysts

Exist in a different phase (typically a solid) from the reactants, providing an active surface. Mechanism steps:
1. Adsorption of reactant(s) onto the catalyst surface
2. Activation of the adsorbed reactant(s)
3. Reaction of the adsorbed reactant(s)
4. Desorption of product(s) from the surface

Example — nickel-catalyzed hydrogenation, C₂H₄ + H₂ → C₂H₆: H₂ adsorbs (H–H bond breaks, Ni–H bonds form); ethylene adsorbs (C=C π-bond breaks, Ni–C bonds form); surface diffusion forms new C–H bonds; C₂H₆ desorbs.

Industrial uses: production of ammonia, nitric acid, sulfuric acid, and methanol. **Automobile catalytic converters** use platinum–rhodium catalysts to simultaneously reduce nitrogen oxides (2NO₂ → N₂ + 2O₂), oxidize carbon monoxide (2CO + O₂ → 2CO₂), and oxidize hydrocarbons (2C₈H₁₈ + 25O₂ → 16CO₂ + 18H₂O).

### Enzymes as biological catalysts

Enzymes are typically proteins that catalyze biologically important reactions, especially in cellular metabolism. Enzyme classes: oxidoreductases (redox), transferases (group transfer), hydrolases (hydrolysis), lyases (group elimination forming double bonds), isomerases (isomerization), ligases (bond formation with ATP hydrolysis).

An enzyme has an **active site** whose shape is complementary to a specific **substrate**, forming an enzyme–substrate complex (a reaction intermediate).
- **Lock-and-key hypothesis:** active site and substrate have rigidly complementary shapes.
- **Induced-fit hypothesis:** the flexible enzyme changes shape to accommodate the substrate while retaining specificity.

Example: glucose-6-phosphate dehydrogenase (G6PD) is the rate-limiting enzyme of the pentose phosphate pathway that supplies NADPH and regulates glutathione (an antioxidant) in red blood cells. G6PD deficiency — the most common human enzyme deficiency — reduces protection against oxidative damage and can cause jaundice.
