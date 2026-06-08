# Chemistry 2e — Chapter 15: Equilibria of Other Reaction Classes

> Source: https://openstax.org/books/chemistry-2e/pages/15-introduction

## Chapter Introduction

The mineral fluorite, CaF₂, is commonly used as a semiprecious stone in many types of jewelry because of its striking appearance. Deposits of fluorite are formed through a process called hydrothermal precipitation in which calcium and fluoride ions dissolved in groundwater combine to produce insoluble CaF₂ in response to some change in solution conditions. For example, a decrease in temperature may trigger fluorite precipitation if its solubility is exceeded at the lower temperature.

This chapter extends the equilibrium machinery of Chapters 13–14 to two additional reaction classes: the dissolution/precipitation of slightly soluble ionic compounds (solubility equilibria, governed by Ksp), and Lewis acid–base reactions (electron-pair transfer, including complex-ion formation governed by Kf). It closes with coupled (simultaneous) equilibria, in which two or more equilibria sharing a species combine.

## 15.1 Precipitation and Dissolution

### Solubility Product Constant (Ksp)

For a sparingly soluble ionic compound such as silver chloride, the dissolution equilibrium is:

AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq)

The **solubility product constant** expression is:

**Ksp = [Ag⁺][Cl⁻]**

Only gases and solutes are represented in equilibrium constant expressions, so the Ksp does not include a term for the undissolved AgCl (a pure solid).

For a general slightly soluble compound MₚXq:

MₚXq(s) ⇌ p M^(m+)(aq) + q X^(n−)(aq)   →   Ksp = [M^(m+)]^p [X^(n−)]^q

The Ksp relates directly to the measured **molar solubility** — the moles of solute that dissolve per liter to give a saturated solution.

**Representative Ksp values (25 °C):**

| Compound | Ksp |
|---|---|
| CaF₂ | 3.98 × 10⁻¹¹ |
| AgCl | 1.6 × 10⁻¹⁰ |
| AgBr | 5.0 × 10⁻¹³ |
| AgI | 1.5 × 10⁻¹⁶ |
| Ca(OH)₂ | 1.3 × 10⁻⁶ |
| Mg(OH)₂ | 8.9 × 10⁻¹² |
| Mn(OH)₂ | 2 × 10⁻¹³ |
| CuBr | 6.3 × 10⁻⁹ |
| Hg₂Cl₂ | 1.1 × 10⁻¹⁸ |
| MgF₂ | 6.4 × 10⁻⁹ |
| PbCrO₄ | 2.0 × 10⁻¹⁶ |
| PbI₂ | 1.4 × 10⁻⁸ |
| CaC₂O₄ | 1.96 × 10⁻⁹ |
| CdS | 1.0 × 10⁻²⁸ |
| Al(OH)₃ | 2 × 10⁻³² |

### Ksp FROM Molar Solubility (CaF₂ example)

Given the molar solubility of CaF₂ = 2.15 × 10⁻⁴ M:

[F⁻] = (2 mol F⁻ / 1 mol Ca²⁺)(2.15 × 10⁻⁴ M) = 4.30 × 10⁻⁴ M

Ksp = [Ca²⁺][F⁻]² = (2.15 × 10⁻⁴)(4.30 × 10⁻⁴)² = 3.98 × 10⁻¹¹

### Molar Solubility FROM Ksp (Ca(OH)₂ example)

ICE-table equilibrium concentrations: [Ca²⁺] = x, [OH⁻] = 2x.

1.3 × 10⁻⁶ = (x)(2x)² = (x)(4x²) = 4x³

x = ∛(1.3 × 10⁻⁶ / 4) = 6.9 × 10⁻³ M

### Predicting Precipitation (Q vs Ksp)

The reaction quotient Qsp determines whether precipitation occurs:

- **Qsp < Ksp** — solution is unsaturated; no precipitation; more solid can dissolve.
- **Qsp = Ksp** — system is at equilibrium (saturated solution).
- **Qsp > Ksp** — solution is supersaturated; precipitation occurs until Qsp = Ksp.

Mg(OH)₂ example:

Q = [Mg²⁺][OH⁻]² = (0.0537)(0.0010)² = 5.4 × 10⁻⁸

Because Q (5.4 × 10⁻⁸) is greater than Ksp (8.9 × 10⁻¹²), the reverse reaction proceeds, precipitating magnesium hydroxide.

### Common-Ion Effect

The solubility of an ionic compound **decreases** in aqueous solutions that already contain a **common ion** (an ion also produced by dissolution of the compound). The mathematical product [ion₁][ion₂] = Ksp remains constant; increasing one ion's concentration proportionally decreases the other's. This is an application of Le Châtelier's principle to the dissolution equilibrium.

CdS example — dissolving CdS in 0.010 M CdBr₂ (initial [Cd²⁺] = 0.010 M):

CdS(s) ⇌ Cd²⁺(aq) + S²⁻(aq);   (0.010 + x)(x) = 1.0 × 10⁻²⁸

Assume x ≪ 0.010:  (0.010)(x) = 1.0 × 10⁻²⁸  →  x = 1.0 × 10⁻²⁶ M

The common Cd²⁺ ion sharply suppresses CdS solubility relative to pure water.

### Selective Precipitation

When several ions can each form an insoluble compound with the same added counter-ion, careful control of the counter-ion concentration precipitates the ions one at a time, exploiting their differing Ksp values; the **least soluble compound precipitates first**.

Silver halides example — a solution 0.10 M in Cl⁻ and 0.00010 M in Br⁻; Ag⁺ is added gradually.

- AgBr begins to precipitate when [Ag⁺] = Ksp/[Br⁻] = 5.0 × 10⁻¹³ / 0.00010 = 5.0 × 10⁻⁹ M
- AgCl begins to precipitate when [Ag⁺] = Ksp/[Cl⁻] = 1.6 × 10⁻¹⁰ / 0.10 = 1.6 × 10⁻⁹ M

AgCl begins to precipitate at a lower [Ag⁺] than AgBr, so AgCl precipitates first.

## 15.2 Lewis Acids and Bases

### The Lewis Model

In 1923, G. N. Lewis proposed that acids and bases are identified by their ability to **accept or donate a pair of electrons** and form a **coordinate covalent bond**:

- A **Lewis acid** is an electron-pair **acceptor**.
- A **Lewis base** is an electron-pair **donor**.
- The product of a Lewis acid–base reaction is an **acid–base adduct**.

A **coordinate covalent bond** (or dative bond) is a covalent bond in which **one atom provides both bonding electrons**. Examples:

- H₂O (Lewis base) + H⁺ (Lewis acid) → H₃O⁺ (hydronium)
- NH₃ (Lewis base) + H⁺ (Lewis acid) → NH₄⁺ (ammonium)

Brønsted-Lowry acid–base reactions are a **subcategory** of Lewis acid–base reactions — specifically those in which the Lewis acid is H⁺.

### Examples

- **Boron trifluoride:** BF₃ is a strong Lewis acid (boron has only six valence electrons). A fluoride ion (Lewis base) donates a lone pair: BF₃ + F⁻ → [BF₄]⁻.
- **Silver–ammonia:** 2 NH₃ (Lewis bases) donate electron pairs to Ag⁺ (Lewis acid): Ag⁺ + 2 NH₃ → [Ag(NH₃)₂]⁺.
- **Nonmetal oxides** act as Lewis acids with oxide ions (Lewis bases) to form oxyanions: SO₂ + O²⁻ → [SO₃]²⁻.
- **Displacement:** one Lewis base can displace another from an adduct, and one Lewis acid can displace another.

### Complex Ions and Coordination Chemistry

A **complex ion** (coordination complex) consists of a **central atom** (typically a transition-metal cation) surrounded by **ligands** — neutral molecules (H₂O, NH₃) or ions (CN⁻, OH⁻) that act as Lewis bases by donating electron pairs to the central atom. This subdiscipline is **coordination chemistry**.

### Formation Constant (Kf)

The equilibrium constant for a metal ion combining with ligands to form a coordination complex is the **formation constant** (Kf), also called a **stability constant**.

Cu(CN)₂⁻ example:

Cu⁺(aq) + 2 CN⁻(aq) ⇌ Cu(CN)₂⁻(aq)

Kf = [Cu(CN)₂⁻] / ([Cu⁺][CN⁻]²)

The **dissociation constant** Kd for the reverse reaction is Kd = 1/Kf.

### Application: AgCl Dissolution via Complex Formation

AgCl dissolves slightly: AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq); initial [Ag⁺] ≈ 1.3 × 10⁻⁵ M.

Adding ammonia forms a complex: Ag⁺(aq) + 2 NH₃(aq) ⇌ Ag(NH₃)₂⁺(aq), with

Kf = [Ag(NH₃)₂⁺] / ([Ag⁺][NH₃]²) = 1.7 × 10⁷

The large Kf means most free Ag⁺ is consumed into the complex. As [Ag⁺] falls, Q = [Ag⁺][Cl⁻] < Ksp, so more AgCl dissolves; with enough ammonia, all the AgCl dissolves. (This is a coupled equilibrium — see §15.3.)

### Worked Example — Dissociation of a Complex Ion

Calculate [Ag⁺] in a solution initially 0.10 M in Ag(NH₃)₂⁺.

ICE table:

| | Ag⁺ | 2 NH₃ | Ag(NH₃)₂⁺ |
|---|---|---|---|
| Initial (M) | 0 | 0 | 0.10 |
| Change (M) | +x | +2x | −x |
| Equilibrium (M) | x | 2x | 0.10 − x |

Kf = (0.10 − x) / [(x)(2x)²] = 1.7 × 10⁷

Because Kf is very large, x ≪ 0.10, so:

1.7 × 10⁷ ≈ 0.10 / (x · 4x²)  →  x³ = 0.10 / [4(1.7 × 10⁷)] = 1.5 × 10⁻⁹  →  x = 1.1 × 10⁻³

Results: [Ag⁺] = 0.0011 M; [NH₃] = 2.2 × 10⁻³ M; [Ag(NH₃)₂⁺] = 0.099 M. Only ~1.1% of the complex dissociates, validating the small-x assumption.

**Check your learning:** dissolving 1.00 g AgNO₃ and 10.0 g KCN in 1.00 L of water gives [Ag⁺] = 2.9 × 10⁻²² M (reaction assumed complete due to large Kf, then [Ag⁺] from dissociation).

## 15.3 Coupled Equilibria

**Coupled equilibria** involve two or more separate chemical reactions that share one or more reactants or products. This section couples solubility equilibria with acid–base and complex-formation reactions. When two equilibria are added, their equilibrium constants **multiply**: Koverall = K₁ × K₂.

### Ocean Acidification (solubility coupled to acid–base)

Coral skeletons dissolve via:

CaCO₃(s) ⇌ Ca²⁺(aq) + CO₃²⁻(aq);   Ksp = 8.7 × 10⁻⁹

Rising atmospheric CO₂ acidifies the ocean through sequential equilibria:

CO₂(g) ⇌ CO₂(aq)
CO₂(aq) + H₂O(l) ⇌ H₂CO₃(aq)
H₂CO₃(aq) + H₂O(l) ⇌ HCO₃⁻(aq) + H₃O⁺(aq);   Ka1 = 4.3 × 10⁻⁷
HCO₃⁻(aq) + H₂O(l) ⇌ CO₃²⁻(aq) + H₃O⁺(aq);   Ka2 = 4.7 × 10⁻¹¹

Net coupled reaction (dissolution + reverse of the second ionization):

CaCO₃(s) + H₃O⁺(aq) ⇌ Ca²⁺(aq) + HCO₃⁻(aq) + H₂O(l);   K = Ksp/Ka2 = 180

The equilibrium constant for this net reaction is much greater than the Ksp for calcium carbonate, indicating its solubility is markedly increased in acidic solutions.

### Dental Enamel

Tooth-enamel mineral (hydroxyapatite) dissolves:

Ca₅(PO₄)₃OH(s) ⇌ 5 Ca²⁺(aq) + 3 PO₄³⁻(aq) + OH⁻(aq)

Bacterial acid waste reacts with the basic ions, driving dissolution. Phosphate is a triprotic base:

PO₄³⁻(aq) + H₃O⁺(aq) → HPO₄²⁻(aq) + H₂O(l)
HPO₄²⁻(aq) + H₃O⁺(aq) → H₂PO₄⁻(aq) + H₂O(l)
H₂PO₄⁻(aq) + H₃O⁺(aq) → H₃PO₄(aq) + H₂O(l)

and hydroxide is monoprotic: OH⁻(aq) + H₃O⁺(aq) → 2 H₂O(l). The hydroxide is by far the stronger base (the strongest base that can exist in aqueous solution), so it is the dominant factor giving the compound an acid-dependent solubility.

**Fluoride protection:** NaF + Ca₅(PO₄)₃OH ⇌ Ca₅(PO₄)₃F + Na⁺ + OH⁻. The weak base fluoride ion reacts only partially with bacterial acid waste, producing a less extensive shift in the solubility equilibrium and thus increased resistance to acid dissolution. The EPA caps fluoride at 4 ppm (4 mg/L) in US drinking water; excess fluoride causes skeletal fluorosis (joint stiffening, bone thickening, possible thyroid damage), affecting over 2.7 million people globally.

### Complex-Ion Formation (Al(OH)₃)

Three coupled equilibria:

- Dissolution: Al(OH)₃(s) ⇌ Al³⁺(aq) + 3 OH⁻(aq);   Ksp = 2 × 10⁻³²
- Complex formation: Al³⁺(aq) + 4 OH⁻(aq) ⇌ Al(OH)₄⁻(aq);   Kf = 1.1 × 10³³
- Net: Al(OH)₃(s) + OH⁻(aq) ⇌ Al(OH)₄⁻(aq);   K = Ksp × Kf = 22

Coupling complex formation with dissolution drastically increases the solubility of Al(OH)₃.

### Calculation — Increased Solubility in Acidic Solution (Al(OH)₃)

**(a) Molar solubility in pure water:**

Al(OH)₃(s) ⇌ Al³⁺ + 3 OH⁻;   Ksp = [Al³⁺][OH⁻]³ = (x)(3x)³ = 27x⁴ = 2 × 10⁻³²
molar solubility = [Al³⁺] = (2 × 10⁻³² / 27)^(1/4) = 5 × 10⁻⁹ M

**(b) Solubility in a buffer (0.100 M acetic acid + 0.100 M sodium acetate):**

pH = pKa + log([CH₃COO⁻]/[CH₃COOH]) = 4.74 + log(0.100/0.100) = 4.74
pOH = 14.00 − 4.74 = 9.26  →  [OH⁻] = 10⁻⁹·²⁶ = 5.5 × 10⁻¹⁰ M
molar solubility = [Al³⁺] = Ksp/[OH⁻]³ = (2 × 10⁻³²)/(5.5 × 10⁻¹⁰)³ = 1.2 × 10⁻⁴ M

Solubility increases roughly ten million times in the mildly acidic buffer compared to pure water.

**Check your learning:** for a buffer of 0.100 M formic acid + 0.100 M sodium formate, solubility = 0.1 M.

### Photographic Film (silver halide + thiosulfate complex)

Two coupled equilibria govern silver bromide dissolution in thiosulfate solution:

- Dissolution: AgBr(s) ⇌ Ag⁺(aq) + Br⁻(aq);   Ksp = 5.0 × 10⁻¹³
- Complexation: Ag⁺(aq) + 2 S₂O₃²⁻(aq) ⇌ Ag(S₂O₃)₂³⁻(aq);   Kf = 4.7 × 10¹³
- Net: AgBr(s) + 2 S₂O₃²⁻(aq) ⇌ Ag(S₂O₃)₂³⁻(aq) + Br⁻(aq);   K = Ksp × Kf = 24

K = [Ag(S₂O₃)₂³⁻][Br⁻] / [S₂O₃²⁻]²

**Worked calculation — mass of Na₂S₂O₃ to dissolve 1.00 g AgBr in 1.00 L:**

1. [Br⁻] from 1.00 g AgBr: (1.00 g ÷ 187.77 g·mol⁻¹) / 1.00 L = 0.00532 M.
2. Large Kf → essentially all dissolved silver is complexed: [Ag(S₂O₃)₂³⁻] = 0.00532 M.
3. Free thiosulfate at equilibrium: [S₂O₃²⁻] = [Ag(S₂O₃)₂³⁻][Br⁻]/K = (0.00532)(0.00532)/24 = 0.0011 M.
4. Mass of Na₂S₂O₃ (M = 158.1 g·mol⁻¹):
   - bound in complex: 0.00532 mol Ag(S₂O₃)₂³⁻ × 2 × 158.1 = 1.68 g
   - excess free thiosulfate: 0.0011 mol × 158.1 = 0.17 g
   - **Total = 1.68 g + 0.17 g = 1.85 g**

**Check your learning:** to dissolve 2.00 g AgCl in 1.00 L by forming Ag(NH₃)₂⁺ (AgCl Ksp = 1.6 × 10⁻¹⁰; Ag(NH₃)₂⁺ Kf = 1.7 × 10⁷), 5.0 g NH₃ is required.
