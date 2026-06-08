---
title: "Equilibrium Calculations"
type: concept
tags: [chemistry, general-chemistry, equilibrium]
sources: [chemistry-2e-ch13-fundamental-equilibrium-concepts]
last_updated: 2026-06-07
---

# Equilibrium Calculations

**Equilibrium calculations** are the quantitative use of the [[EquilibriumConstant|equilibrium constant]] K to find unknown equilibrium concentrations (or pressures), or to find K from measured concentrations. They rely on the [[ICETable|ICE table]] to track stoichiometric changes.

## Changes follow stoichiometry

All concentration changes are tied to one unknown x through the balanced equation. For $\mathrm{2NH_3(g) \rightleftharpoons N_2(g) + 3H_2(g)}$, if [N₂] rises by x then Δ[H₂] = +3x and Δ[NH₃] = −2x.

## Finding K from equilibrium concentrations

Substitute measured equilibrium values into the K expression. For $\mathrm{I_2(aq) + I^-(aq) \rightleftharpoons I_3^-(aq)}$ with equilibrium [I₃⁻] = 3.39 × 10⁻⁴ M and [I₂] = [I⁻] = 6.61 × 10⁻⁴ M:

$$K_c = \frac{[\mathrm{I_3^-}]}{[\mathrm{I_2}][\mathrm{I^-}]} = \frac{3.39\times10^{-4}}{(6.61\times10^{-4})(6.61\times10^{-4})} = 776$$

## Finding a missing concentration from K

For $\mathrm{N_2(g) + O_2(g) \rightleftharpoons 2NO(g)}$ with Kc = 4.1 × 10⁻⁴, [N₂] = 0.036 M, [O₂] = 0.0089 M:

$$[\mathrm{NO}]^2 = K_c[\mathrm{N_2}][\mathrm{O_2}] = (4.1\times10^{-4})(0.036)(0.0089) = 1.31\times10^{-7}$$
$$[\mathrm{NO}] = \sqrt{1.31\times10^{-7}} = 3.6\times10^{-4}\ \text{mol/L}$$

## Four-step method (concentrations from initial conditions)

1. **Determine direction** — compute the [[ReactionQuotient|reaction quotient]] Q and compare with K.
2. **Build an [[ICETable|ICE table]]** — Initial, Change (±x × coefficient), Equilibrium.
3. **Solve for x** — substitute the Equilibrium row into the K expression; solve (quadratic if necessary).
4. **Confirm** — plug results back into K.

**Quadratic example** — $\mathrm{PCl_5(g) \rightleftharpoons PCl_3(g) + Cl_2(g)}$, Kc = 0.0211, [PCl₅]₀ = 1.00 M:

$$\frac{x^2}{1.00 - x} = 0.0211 \ \Rightarrow\ x^2 + 0.0211x - 0.0211 = 0$$
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{-0.0211 + 0.2912}{2} = 0.135\ \text{M}$$

Equilibrium: [PCl₅] = 0.87 M, [PCl₃] = [Cl₂] = 0.135 M (check: (0.135)²/0.87 ≈ 0.021 ✓).

## The x-is-small approximation

When K is **very small** so that x ≪ the initial concentration, the change term in the denominator can be dropped, avoiding the quadratic. For $\mathrm{HCN(aq) \rightleftharpoons H^+(aq) + CN^-(aq)}$, Kc = 4.9 × 10⁻¹⁰, [HCN]₀ = 0.15 M:

$$K_c \approx \frac{x^2}{0.15} \ \Rightarrow\ x^2 = 7.4\times10^{-11} \ \Rightarrow\ x = 8.6\times10^{-6}\ \text{M}$$

**Validity:** the approximation holds when x is **less than ~5%** of the initial concentration (here 8.6 × 10⁻⁶ ≪ 0.15 ✓). If x exceeds 5%, discard the approximation and solve the full quadratic.

## Connections
- [[ICETable]] — the bookkeeping framework these calculations use
- [[EquilibriumConstant]] — K is computed or applied here (Kc/Kp)
- [[ReactionQuotient]] — Q sets the reaction direction in step 1
- [[ChemicalEquilibrium]] — the state being quantified
- [[chemistry-2e-ch13-fundamental-equilibrium-concepts]] — source chapter (§13.4)
