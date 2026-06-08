# Chemistry 2e — Chapter 13: Fundamental Equilibrium Concepts

> Source: https://openstax.org/books/chemistry-2e/pages/13-introduction

## Chapter Introduction

Equilibrium is illustrated by an analogy to beachgoers: as those basking in the sun get too hot, they enter the surf to swim and cool off; as the swimmers tire, they return to the beach to rest. When the entry and exit rates equalize, the populations remain steady despite constant movement. Chemical and physical processes are subject to this phenomenon; these processes are at equilibrium when the forward and reverse reaction rates are equal. Equilibrium systems permeate nature — for example, carbon dioxide transport in blood involves reversible reactions. The chapter covers essential equilibrium concepts across four sections.

## 13.1 Chemical Equilibria

### Definition and Nature of Equilibrium Systems
Chemical equilibrium occurs when the rates of the forward and reverse reactions are equal and the concentrations of the reactant and product species remain constant over time. By convention, chemical equations show reactants on the left and products on the right, representing the forward direction; however, reversible reactions proceed in both directions.

### Reversible Reactions and Notation
Reversible reactions are denoted with a double arrow (⇌) to emphasize bidirectional progression. Example:

**N₂O₄(g) ⇌ 2NO₂(g)**

### Dynamic Equilibrium
Chemical equilibria are dynamic; a reaction at equilibrium has not "stopped," but is proceeding in the forward and reverse directions at the same rate. The system maintains constant macroscopic composition while molecular-level reactions continue.

### Reaction Rates and Equilibrium Achievement
For the elementary reaction N₂O₄(g) ⇌ 2NO₂(g), the rate laws are:

- Forward rate: **rate_f = k_f[N₂O₄]**
- Reverse rate: **rate_r = k_r[NO₂]²**

As the reaction begins (t = 0):
- N₂O₄ concentration is finite; NO₂ concentration is zero
- The forward reaction proceeds at a finite rate; the reverse reaction rate is zero
- As time progresses, N₂O₄ decreases (slowing the forward rate) and NO₂ increases (accelerating the reverse rate)
- The process continues until the forward and reverse reaction rates become equal, establishing equilibrium with constant concentrations

### Equilibrium Composition
The relative concentrations of reactants and products in equilibrium systems vary greatly; some systems contain mostly products at equilibrium, some contain mostly reactants, and some contain appreciable amounts of both.

### Physical Equilibria
Reversible phase transitions also establish equilibria. Example:

**Br₂(l) ⇌ Br₂(g)**

Vaporization and condensation rates equalize at equilibrium.

## 13.2 Equilibrium Constants

### Reaction Quotient (Q)
For a reversible reaction: **mA + nB ⇌ xC + yD**

The concentration-based reaction quotient is:

**Qc = [C]^x[D]^y / ([A]^m[B]^n)**

For gaseous reactants and products, a pressure-based quotient can be used:

**Qp = (P_C)^x(P_D)^y / ((P_A)^m(P_B)^n)**

The subscript c denotes use of molar concentrations; p denotes partial pressures. The reaction quotient equations above are a simplification of more rigorous expressions that use relative (dimensionless) values for concentrations and pressures rather than absolute values. Q varies as a reaction proceeds toward equilibrium, serving as an indicator of reaction status.

### Equilibrium Constant (K)
The constant value of Q exhibited by a system at equilibrium is called the equilibrium constant, K: **K ≡ Q at equilibrium**.

### Law of Mass Action
At a given temperature, the reaction quotient for a system at equilibrium is constant. This fundamental principle means all equilibrium systems for a given reaction reach the same K value regardless of initial conditions.

### Interpreting K Magnitude
- **Large K**: a reaction exhibiting a large K will reach equilibrium when most of the reactant has been converted to product.
- **Small K**: a small K indicates the reaction achieves equilibrium after very little reactant has been converted.
- Important caveat: the magnitude of K does not indicate how rapidly or slowly equilibrium will be reached.

### Predicting Reaction Direction
By comparing Q to K:
- If **Q < K**: reaction proceeds in the forward direction (more product forms)
- If **Q > K**: reaction proceeds in the reverse direction (more reactant forms)
- If **Q = K**: the system is at equilibrium

### Homogeneous Equilibria
A homogeneous equilibrium is one in which all reactants and products (and any catalysts, if applicable) are present in the same phase. Homogeneous equilibria occur in solutions — typically liquid or gaseous phases. When water functions as a reactant in aqueous solutions, its concentration is not included in the reaction quotient, because relative concentrations for liquids and solids are equal to 1 and need not be included. Consequently, reaction quotients include concentration or pressure terms only for gaseous and solute species.

### Kc and Kp Relationship
For gas-phase reactions, both Kc (molar concentration) and Kp (partial pressure) expressions are valid. The relationship between them is:

**Kp = Kc(RT)^Δn**

Where:
- R = gas constant (0.0821 L·atm/(mol·K))
- T = absolute temperature (Kelvin)
- Δn = (moles of gaseous products) − (moles of gaseous reactants)

For the reaction aA + bB ⇌ cC + dD: Δn = (c + d) − (a + b). When Δn = 0, Kp = Kc.

### Heterogeneous Equilibria
A heterogeneous equilibrium involves reactants and products in two or more different phases. Examples:
- **PbCl₂(s) ⇌ Pb²⁺(aq) + 2Cl⁻(aq)**
- **CaO(s) + CO₂(g) ⇌ CaCO₃(s)**

Again, concentration terms are only included for gaseous and solute species. Solids and pure liquids are excluded from equilibrium expressions because their activities equal 1.

### Coupled (Related) Equilibria
When two or more equilibrium reactions share common species, the overall equilibrium constant equals the mathematical product of individual K values. Three key manipulations:
1. **Reversing an equation**: K′ = 1/K
2. **Multiplying stoichiometric coefficients by a factor x**: K′ = K^x
3. **Adding two equilibrium equations**: K_overall = K₁ × K₂

## 13.3 Shifting Equilibria: Le Châtelier's Principle

### Core Principle
**Le Châtelier's Principle**: if an equilibrium system is stressed, the system will experience a shift in response to the stress that re-establishes equilibrium. A system at dynamic equilibrium maintains equal forward and reverse reaction rates. When conditions change in ways that affect these rates differently (a "stress"), the rates become unequal and the system shifts to restore equilibrium.

### Effects of Concentration Changes
**Kinetic interpretation** (for H₂(g) + I₂(g) ⇌ 2HI(g)):
- When reactant is added: the forward reaction rate increases more than the reverse rate, so rate_f > rate_r and equilibrium shifts right (toward products).
- When product is removed: the reverse reaction rate decreases, so rate_f > rate_r and equilibrium shifts right.

**Reaction quotient interpretation** (at equilibrium Q_c = [HI]²/([H₂][I₂]) = K_c):
- If reactant is added (increasing denominator) or product is removed (decreasing numerator): Q_c < K_c → equilibrium shifts right.
- If reactant is removed or product is added: Q_c > K_c → equilibrium shifts left.

**Critical point:** the equilibrium constant K remains unchanged regardless of concentration adjustments. Only the composition of the equilibrium mixture changes.

### Pressure and Volume Changes (Gas-Phase Equilibria)
For ideal gases: **M = n/V = P/RT**, so changes in partial pressures are equivalent to concentration changes. The effect of a volume change depends on molar stoichiometry.

**Example 1 — equal moles of gas:** H₂(g) + I₂(g) ⇌ 2HI(g). If volume decreases by a factor of 3, all partial pressures increase by a factor of 3:

Q_P′ = (3P_HI)²/[(3P_H₂)(3P_I₂)] = 9P_HI²/(9P_H₂P_I₂) = Q_P = K_P → **no shift** (2 mol gas on each side).

**Example 2 — unequal moles of gas:** 2NO₂(g) ⇌ 2NO(g) + O₂(g). Decreasing volume by a factor of 3:

Q_P′ = [(3P_NO)²(3P_O₂)]/[(3P_NO₂)²] = 3Q_P > K_P → equilibrium shifts **left** (2 mol reactant ← 3 mol product; volume decrease favors fewer moles).

**General rule:** if total moles of gaseous reactants ≠ total moles of gaseous products, a volume change shifts equilibrium. A volume decrease favors the side with fewer moles of gas; a volume increase favors the side with more moles.

### Temperature Changes
Unlike concentration changes, temperature shifts affect the equilibrium constant itself. For elementary reaction A ⇌ B with rate_f = k_f[A] and rate_r = k_r[B], at equilibrium k_f[A] = k_r[B], so **K_c = [B]/[A] = k_f/k_r**. Since rate constants vary with temperature (Arrhenius equation), K varies with temperature.

**Endothermic reactions** (e.g., N₂O₄(g) ⇌ 2NO₂(g), ΔH = +57.20 kJ): heat may be viewed as a reactant: heat + N₂O₄(g) ⇌ 2NO₂(g).
- Raising temperature (adding "reactant"): equilibrium shifts right.
- Lowering temperature: equilibrium shifts left.

**Exothermic reactions:** heat is treated as a product; temperature effects are opposite to the endothermic case.
- Raising temperature: equilibrium shifts left.
- Lowering temperature: equilibrium shifts right.

### Catalysts
A catalyst enables a reaction via a different mechanism with lower activation energy (E_a). It lowers E_a for both the forward and reverse reactions equally. Consequently:
- Both forward and reverse reactions accelerate.
- Equilibrium is achieved more quickly.
- **The equilibrium constant K remains unchanged.**
- **The equilibrium position does not shift.**

A catalyst only affects the rate at which equilibrium is achieved, not the composition of the equilibrium mixture.

### Case Study: Haber-Bosch Process
Industrial ammonia synthesis: N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = −92.2 kJ.

Challenges: small K_p (~10⁻⁵ at 25 °C) yields little ammonia; slow reaction rate at low temperatures.

Industrial optimization strategies:
1. **High pressure (150–250 atm):** increases reactant concentrations, shifts equilibrium right toward NH₃.
2. **Continuous ammonia removal:** lowers product concentration, shifts equilibrium right.
3. **Catalyst:** accelerates the reaction to reasonable rates at moderate temperatures (400–500 °C).
4. **Temperature compromise:** intermediate temperature where the catalyst provides adequate speed while maintaining acceptable equilibrium yield (low temperature is thermodynamically favorable for this exothermic reaction but kinetically slow).

### Soft Drinks Application
CO₂ dissolution equilibria in carbonated beverages:
- Dissolution: CO₂(g) ⇌ CO₂(aq)
- Hydration: CO₂(aq) + H₂O(l) ⇌ H₂CO₃(aq)
- Ionization: H₂CO₃(aq) ⇌ HCO₃⁻(aq) + H⁺(aq)

Manufacturing applies high CO₂ pressure to shift the first equilibrium right, increasing dissolved CO₂. Upon opening, pressure drops, all three equilibria shift left, and dissolved CO₂ decreases, producing the "flat" taste of a degassed beverage.

## 13.4 Equilibrium Calculations

### Changes in Concentration from Stoichiometry
Changes in reactant and product concentrations are derived from reaction stoichiometry. For the decomposition of ammonia, **2NH₃(g) ⇌ N₂(g) + 3H₂(g)**, if nitrogen concentration increases by amount *x*:
- Δ[N₂] = +*x*
- Δ[H₂] = +3*x* (3 mol H₂ per 1 mol N₂)
- Δ[NH₃] = −2*x* (2 mol NH₃ per 1 mol N₂)

The negative sign indicates a decrease in concentration.

### The ICE Table Method
The ICE (Initial, Change, Equilibrium) table organizes concentration terms systematically:

| | Reactants | Products |
|---|---|---|
| **Initial (I)** | Starting concentrations | Starting concentrations |
| **Change (C)** | −*x* (or stoichiometric multiple) | +*x* (or stoichiometric multiple) |
| **Equilibrium (E)** | Initial + Change | Initial + Change |

**Example: I₂(aq) + I⁻(aq) ⇌ I₃⁻(aq)** with initial [I₂] = 1.000 × 10⁻³ M, [I⁻] = 1.000 × 10⁻³ M, [I₃⁻] = 0. If equilibrium [I₂] = 6.61 × 10⁻⁴ M:
- Change: 1.000 × 10⁻³ − 6.61 × 10⁻⁴ = 3.39 × 10⁻⁴ M = *x*
- [I⁻] at equilibrium: 1.000 × 10⁻³ − 3.39 × 10⁻⁴ = 6.61 × 10⁻⁴ M
- [I₃⁻] at equilibrium: 0 + 3.39 × 10⁻⁴ = 3.39 × 10⁻⁴ M

### Calculation of an Equilibrium Constant
Substitute equilibrium concentrations into the K expression: **Kc = [I₃⁻] / ([I₂][I⁻])**. For the example above:

Kc = (3.39 × 10⁻⁴) / ((6.61 × 10⁻⁴)(6.61 × 10⁻⁴)) = 776

### Calculation of a Missing Equilibrium Concentration
When K and all but one equilibrium concentration are known, solve algebraically.

**Example: N₂(g) + O₂(g) ⇌ 2NO(g)** with Kc = 4.1 × 10⁻⁴, [N₂] = 0.036 M, [O₂] = 0.0089 M:

Kc = [NO]² / ([N₂][O₂]) → [NO]² = Kc[N₂][O₂] = (4.1 × 10⁻⁴)(0.036)(0.0089) = 1.31 × 10⁻⁷

[NO] = √(1.31 × 10⁻⁷) = 3.6 × 10⁻⁴ mol/L

### Calculation of Equilibrium Concentrations from Initial Concentrations
Four-step approach:
1. **Determine reaction direction** — calculate Q and compare to K.
2. **Develop an ICE table** — set up initial, change, and equilibrium rows.
3. **Solve for *x*** — substitute into the K expression; solve quadratically if needed.
4. **Confirm results** — recalculate K from equilibrium concentrations.

**Example: PCl₅(g) ⇌ PCl₃(g) + Cl₂(g)** with Kc = 0.0211, initial [PCl₅] = 1.00 M:

| | PCl₅ | PCl₃ | Cl₂ |
|---|---|---|---|
| Initial | 1.00 | 0 | 0 |
| Change | −*x* | +*x* | +*x* |
| Equilibrium | 1.00 − *x* | *x* | *x* |

Kc = (*x*)(*x*) / (1.00 − *x*) = 0.0211 → *x*² + 0.0211*x* − 0.0211 = 0

Quadratic formula (a*x*² + b*x* + c = 0): *x* = [−b ± √(b² − 4ac)] / (2a)

*x* = [−0.0211 ± √((0.0211)² + 4(0.0211))] / 2 = [−0.0211 ± 0.2912] / 2

Positive root: *x* = 0.135 M. Equilibrium: [PCl₅] = 0.87 M, [PCl₃] = 0.135 M, [Cl₂] = 0.135 M.
Confirmation: Kc = (0.135)(0.135) / 0.87 = 0.021 ✓

### The x-is-Small Approximation
When K is very small and the initial concentration is much larger than the change (*x* ≪ initial concentration), the approximation simplifies calculations.

**Example: HCN(aq) ⇌ H⁺(aq) + CN⁻(aq)** with Kc = 4.9 × 10⁻¹⁰, initial [HCN] = 0.15 M:

| | HCN | H⁺ | CN⁻ |
|---|---|---|---|
| Initial | 0.15 | 0 | 0 |
| Change | −*x* | +*x* | +*x* |
| Equilibrium | 0.15 − *x* | *x* | *x* |

Simplified: if *x* ≪ 0.15 M, then (0.15 − *x*) ≈ 0.15, so Kc ≈ *x*²/0.15 → *x*² = 7.4 × 10⁻¹¹ → *x* = 8.6 × 10⁻⁶ M.

Validity check: 8.6 × 10⁻⁶ ≪ 0.15 ✓. The approximation is valid if *x* is less than 5% of the initial concentration; otherwise the full quadratic method must be used.
