# Chemistry 2e — Chapter 9: Gases

> Source: https://openstax.org/books/chemistry-2e/pages/9-introduction

## Introduction

We exist within an ocean of gas—our atmosphere—and many gas properties are familiar from everyday experience. Heated gases expand, which enables hot air balloons to rise or causes bicycle tire blowouts when left in sunshine. Gases shaped chemistry's development significantly: during the seventeenth and eighteenth centuries, scientists studied gas behavior extensively, producing the first mathematical descriptions of the behavior of matter. This chapter examines relationships between gas temperature, pressure, amount, and volume; it covers a simplified theoretical model (the kinetic-molecular theory) to interpret experimental gas behavior, then explores the model's limitations and refinements (non-ideal behavior).

Sections:
- 9.1 Gas Pressure
- 9.2 Relating Pressure, Volume, Amount, and Temperature: The Ideal Gas Law
- 9.3 Stoichiometry of Gaseous Substances, Mixtures, and Reactions
- 9.4 Effusion and Diffusion of Gases
- 9.5 The Kinetic-Molecular Theory
- 9.6 Non-Ideal Gas Behavior

---

## 9.1 Gas Pressure

### Definition of Pressure

Pressure is defined by the relationship:

**P = F / A**

Pressure is directly proportional to force and inversely proportional to area. Pressure increases by increasing force or decreasing area; it decreases by decreasing force or increasing area.

### Pressure Units and Conversions

| Unit | Definition/Relation |
|------|---------------------|
| pascal (Pa) | 1 Pa = 1 N/m²; recommended IUPAC unit |
| kilopascal (kPa) | 1 kPa = 1,000 Pa |
| pounds per square inch (psi) | Air pressure at sea level ≈ 14.7 psi |
| atmosphere (atm) | 1 atm = 101,325 Pa = 760 torr |
| bar | 1 bar = 100,000 Pa |
| millibar (mbar) | 1,000 mbar = 1 bar |
| inches of mercury (in. Hg) | 1 in. Hg = 3,386 Pa |
| torr | 1 torr = 1/760 atm |
| millimeters of mercury (mm Hg) | 1 mm Hg ≈ 1 torr |

Summary of key equalities: **1 atm = 760 mmHg = 760 torr = 101,325 Pa = 101.325 kPa = 1.01325 bar ≈ 14.7 psi.**

### Hydrostatic Pressure

The pressure exerted by a fluid due to gravity:

**p = hρg**

where h = height of the fluid column, ρ (rho) = density of the fluid, g = acceleration due to gravity. Standard atmospheric pressure at sea level (1 atm = 101,325 Pa) corresponds to a mercury column approximately 760 mm (29.92 inches) high.

### Barometer Operation

A barometer measures atmospheric pressure using a glass tube that is closed at one end, filled with a nonvolatile liquid such as mercury, then inverted and immersed in a container of that liquid. The height of the liquid column is proportional to atmospheric pressure. Mercury is preferred because it is approximately 13.6 times denser than water, permitting reasonably sized instruments.

### Manometer Types and Calculations

A manometer measures the pressure of a gas in a container.

**Closed-End Manometer** — one arm is closed (vacuum). The gas pressure equals the hydrostatic pressure of the column height difference:

**P_gas = hρg**

**Open-End Manometer** — one arm is open to the atmosphere; the other connects to the gas container:
- When liquid is higher on the gas side: **P_gas = P_atm − hρg**
- When liquid is higher on the open side: **P_gas = P_atm + hρg**

### Example Conversions

Converting 29.2 in. Hg to other units:
- To torr: 29.2 in. Hg × (25.4 mm / 1 in.) × (1 torr / 1 mm Hg) = 742 torr
- To atm: 742 torr × (1 atm / 760 torr) = 0.976 atm
- To kPa: 742 torr × (101.325 kPa / 760 torr) = 98.9 kPa
- To mbar: 98.9 kPa → 989 mbar

---

## 9.2 Relating Pressure, Volume, Amount, and Temperature: The Ideal Gas Law

### Amontons's Law (Gay-Lussac's Law)

The pressure of a confined amount of gas is directly proportional to its absolute temperature when volume remains constant.

**P ∝ T   or   P = kT   or   P₁/T₁ = P₂/T₂**

T must be on the kelvin scale; k depends on gas identity, amount, and volume. Guillaume Amontons established this relationship (~1700); Joseph Louis Gay-Lussac refined it (~1800).

Example (9.5): Hair spray can of isobutane at 24°C (297 K) and 360 kPa, left in a 50°C (323 K) car → 360/297 = P₂/323 → P₂ = 390 kPa.

### Charles's Law

The volume of a confined amount of gas is directly proportional to its absolute temperature when pressure remains constant.

**V ∝ T   or   V = kT   or   V₁/T₁ = V₂/T₂**

Attributed to Jacques Alexandre César Charles, French scientist and balloon flight pioneer.

Example (9.6): CO₂ occupies 0.300 L at 283 K → at 303 K (same P): 0.300/283 = V₂/303 → V₂ = 0.321 L.
Example (9.7, gas thermometer): H₂ at 273.15 K occupies 150.0 cm³; at boiling liquid ammonia it is 131.7 cm³ → T₂ = 239.8 K = −33.4°C.

### Boyle's Law

The volume of a confined amount of gas held at constant temperature is inversely proportional to the pressure.

**P ∝ 1/V   or   PV = k   or   P₁V₁ = P₂V₂**

A plot of P vs. V is a hyperbola; a plot of P vs. 1/V (or 1/P vs. V) is linear (preferred for data fitting).

Example (9.8): 15.0 mL at 13.0 psi → at 7.5 mL: 13.0 × 15.0 = P₂ × 7.5 → P₂ = 26 psi.

**Breathing application:** On inhalation the diaphragm contracts, the chest cavity and lung volume increase, lung pressure decreases (Boyle's law), and air flows in from high to low pressure. On exhalation the reverse occurs. The lung–surroundings pressure difference is approximately 1–3 torr.

### Avogadro's Law

Equal volumes of all gases measured under identical conditions of temperature and pressure contain the same number of molecules. For a confined gas, volume and moles are directly proportional at constant pressure and temperature.

**V ∝ n   or   V = kn   or   V₁/n₁ = V₂/n₂**

Related: P ∝ n (constant T, V); n ∝ T... etc.

### The Ideal Gas Law

**PV = nRT**

where P = pressure, V = volume, n = moles, T = absolute temperature (K), R = the ideal (universal) gas constant.

Values of R:
- R = 0.08206 L·atm/(mol·K)
- R = 8.314 kPa·L/(mol·K)
- R = 8.314 J/(mol·K)

The form of R used must match the units of P, V, T (dimensional analysis). Gases follow the ideal gas law accurately under relatively low pressure and high temperature. The equation has five terms (R plus P, V, n, T); specifying any four permits calculation of the fifth.

Example (9.9): 655 g CH₄ (40.8 mol) at 298 K and 745 torr (0.980 atm): V = nRT/P = (40.8)(0.08206)(298)/0.980 = 1.02 × 10³ L.

### Combined Gas Law

When moles of an ideal gas remain constant between two states:

**P₁V₁/T₁ = P₂V₂/T₂**

(Each side equals nR.)

Example (9.10, scuba): tank 13.2 L at 153 atm and 300 K → at 3.13 atm and 310 K: (153)(13.2)/300 = (3.13)(V₂)/310 → V₂ = 667 L.

### Standard Conditions of Temperature and Pressure (STP) and Molar Volume

- Temperature: 273.15 K (0°C)
- Pressure: 1 atm (101.325 kPa). IUPAC changed the standard to 1 bar in 1982, but 1 atm remains widely used.

**Standard molar volume:** one mole of ideal gas at STP occupies ≈ 22.4 L (at 1 atm); ≈ 22.71 L at 1 bar. Regardless of chemical identity, one mole of an ideal gas occupies ~22.4 L at STP (illustrated with He, NH₃, O₂, each containing Avogadro's number of molecules).

### Summary: Individual Gas Laws Combined

1. Boyle's Law: PV = constant (T, n constant)
2. Amontons's Law: P/T = constant (V, n constant)
3. Charles's Law: V/T = constant (P, n constant)
4. Avogadro's Law: V/n = constant (P, T constant)

These combine to yield **PV = nRT**.

---

## 9.3 Stoichiometry of Gaseous Substances, Mixtures, and Reactions

### Gas Density and Molar Mass

Density d = m/V. Substituting V from PV = nRT:

**d = (m/V) = (m/n)(P/RT) = ℳP / RT**

where ℳ = m/n is the molar mass. Therefore **d = ℳP/RT**.

Solving for molar mass from measured mass, pressure, volume, temperature:

**ℳ = mRT / PV**

This identifies an unknown gas via its molar mass.

### Dalton's Law of Partial Pressures

The total pressure of a mixture of ideal gases equals the sum of the partial pressures of the component gases:

**P_Total = P_A + P_B + P_C + … = Σᵢ Pᵢ**

The partial pressure of each gas is the pressure it would exert alone in the container (assuming no chemical reaction).

### Mole Fraction and Partial Pressure

The mole fraction of A is X_A = n_A / n_Total, and:

**P_A = X_A × P_Total**

### Collection of Gases over Water

When a gas is collected over water by displacement, the trapped gas becomes saturated with water vapor, so:

**P_Total = P_gas + P_H₂O   →   P_gas = P_Total − P_H₂O**

The vapor pressure of water depends only on temperature and is read from tables; it is the pressure of water vapor in equilibrium with liquid water in a closed container.

### Chemical Stoichiometry and Gases

Because equal volumes of ideal gases at the same T and P contain equal numbers of molecules, the ratios of volumes of gases in a reaction equal the stoichiometric coefficients (provided all volumes are measured at the same T and P). For:

**N₂(g) + 3 H₂(g) → 2 NH₃(g)**

one volume of N₂ reacts with three volumes of H₂ to produce two volumes of NH₃. Gas-stoichiometry workflow: (1) use PV = nRT to convert volume/pressure/temperature to moles; (2) apply mole ratios from the balanced equation; (3) convert back to volume at the specified conditions.

---

## 9.4 Effusion and Diffusion of Gases

### Mean Free Path

The mean free path is the average distance a molecule travels between collisions. It increases as pressure decreases and is typically hundreds of times the molecule's own diameter.

### Diffusion

Diffusion is the process by which molecules disperse in space in response to differences in concentration. Net movement is from high to low concentration; at equilibrium concentrations are equal everywhere and molecules continue moving with no net transfer.

**Rate of diffusion = (amount of gas passing through an area) / (unit of time)**

Diffusion rate depends on temperature, mass of the particles, concentration gradient, available surface area, and distance traveled. Time required is inversely proportional to rate.

### Effusion

Effusion is the escape of gas molecules through a tiny hole (e.g., a pinhole) into a vacuum. Both diffusion and effusion rates depend on molar mass; their absolute rates differ but the ratios of rates are the same.

### Graham's Law of Effusion

The rate of effusion of a gas is inversely proportional to the square root of its molar mass:

**rate of effusion ∝ 1/√ℳ**

For two gases A and B at the same T and P:

**(rate of effusion of A) / (rate of effusion of B) = √(ℳ_B / ℳ_A)**

Lighter gases effuse faster.

Example 9.20: rate(H₂)/rate(O₂) = √(32/2) = √16 = 4 (H₂ effuses 4× as fast). Check: N₂ at 79 mL/s → SO₂ at 52 mL/s.
Example 9.21: equal amounts of Xe and Ne; time(Ne)/time(Xe) = √(ℳ_Ne/ℳ_Xe) = √(20.2/131.3) = 0.392; time(Ne) = 0.392 × 243 s = 95.3 s. Check: He balloon to 2/3 in 8.0 h → air (28.2 g/mol) to 1/2 in 32 h.
Example 9.22: unknown effuses 1.66× faster than CO₂ → 1.66 = √(44.0/ℳ) → ℳ = 44.0/(1.66)² = 16.0 g/mol (likely CH₄). Check: H₂ effuses 8.97× faster than unknown → ℳ ≈ 162 g/mol.

### Application: Uranium Enrichment

Natural uranium is only 0.72% fissile ²³⁵U; reactors need 2–5%, weapons more. Uranium hexafluoride (UF₆) is the only sufficiently volatile uranium compound. UF₆ is pumped through diffusers with porous barriers (holes ~10⁻⁶ cm); lighter ²³⁵UF₆ diffuses faster, so the gas passing through is slightly enriched (~0.4% per diffuser). Many diffusers in sequence form a cascade. First accomplished at Oak Ridge, Tennessee, during WWII (Manhattan Project). Energy-intensive gaseous diffusion is now being replaced by gas centrifuge technology.

---

## 9.5 The Kinetic-Molecular Theory

The kinetic molecular theory (KMT) is a simple microscopic model that explains the gas laws, valid for pressures below ~1–2 atm.

### Five Postulates

1. Gases are composed of molecules in continuous motion, traveling in straight lines and changing direction only on collision with other molecules or container walls.
2. The molecules are negligibly small compared to the distances between them.
3. The pressure exerted by a gas results from collisions between gas molecules and the container walls.
4. Gas molecules exert no attractive or repulsive forces on each other or the walls; collisions are elastic (no energy loss).
5. The average kinetic energy of the molecules is proportional to the kelvin temperature.

### How KMT Explains the Gas Laws

- **Amontons's law:** Higher T raises average speed/KE → more frequent and forceful wall collisions → higher P (constant V).
- **Charles's law:** Higher T at constant P requires expansion; greater travel distances and wall area reduce collision frequency per unit area, balancing the increased force.
- **Boyle's law:** Smaller V crowds molecules → more frequent wall collisions → higher P (constant T).
- **Avogadro's law:** At constant P and T the frequency/force of collisions is constant; more molecules need proportionally more volume.
- **Dalton's law:** Because of large intermolecular distances, each gas bombards the walls independently; total pressure equals the sum of partial pressures.

### Molecular Speeds and Kinetic Energy

Individual speeds vary widely, but the speed distribution and average speed are constant (the **Maxwell-Boltzmann distribution**). Most molecules have intermediate speeds; few are very slow or very fast. The peak is the most probable speed (ν_p); u_rms is slightly higher.

Kinetic energy of one particle: **KE = ½ m u²** (mass in kg, speed in m/s → joules).

Root-mean-square speed: **u_rms = √(ū²) = √[(u₁² + u₂² + … )/n]**.

Average KE per mole: **KE_avg = ½ ℳ u_rms²** (ℳ in kg/mol), and **KE_avg = (3/2) RT** with R = 8.314 J/(mol·K).

Equating the two: ½ ℳ u_rms² = (3/2) RT, so:

**u_rms = √(3RT / ℳ)**

Example: N₂ at 303 K (ℳ = 0.028 kg/mol) → u_rms = √[(3 × 8.314 × 303)/0.028] = 519 m/s. O₂ at −23°C → u_rms = 441 m/s.

### Effect of Temperature and Molar Mass on the Distribution

Higher T → higher KE_avg, distribution shifts to the right (higher speeds) and becomes wider/flatter; lower T shifts it left. At a given temperature all gases have the same KE_avg, but lighter gases have higher u_rms with a distribution peaking at higher speeds; heavier gases peak at lower speeds.

### KMT Explanation of Effusion / Graham's Law

Effusion rate depends directly on average molecular speed: **effusion rate ∝ u_rms**. From u_rms = √(3RT/ℳ):

**(effusion rate A)/(effusion rate B) = u_rms,A / u_rms,B = √(ℳ_B / ℳ_A)**

This derives Graham's law from KMT.

---

## 9.6 Non-Ideal Gas Behavior

Real gas behavior is often non-ideal: the observed P–V–T relationships are not perfectly described by PV = nRT.

### Compressibility Factor (Z)

**Z = (measured molar volume) / (ideal molar volume) = PV_m / RT**

- Z = 1 → ideal behavior
- Z ≠ 1 → non-ideal behavior

### Physical Causes of Non-Ideal Behavior

1. **Finite molecular volume:** At high pressures molecules are crowded; their own volume becomes significant, so the gas is less compressible than Boyle's law predicts.
2. **Intermolecular attractions:** At higher pressures attractive forces pull molecules together, decreasing pressure (constant V) or volume (constant P). The effect is stronger at low temperatures, where molecules have lower KE relative to the attractions.

### Conditions

Ideal behavior is approached at low pressure, high temperature, and low molecular density (few molecules in a large volume). Deviations are greatest at high pressure and low temperature.

### The van der Waals Equation

Johannes van der Waals (1879) added two correction terms:

**(P + a n²/V²)(V − n b) = nRT**

- **Pressure correction a n²/V²** — accounts for intermolecular attraction; a measures attraction strength; more important at low pressures.
- **Volume correction n b** — accounts for the finite, incompressible volume of the molecules; b measures molecular size; more important at high pressures / small volumes.

When V is large and n small, both corrections vanish and the equation reduces to PV = nRT. At low pressure the a correction dominates; at high pressure/small volume the b correction dominates; at some intermediate pressure they offset and the gas appears nearly ideal.

### Van der Waals Constants (selected)

| Gas | a (L²·atm/mol²) | b (L/mol) |
|-----|-----------------|-----------|
| N₂  | 1.39 | 0.0391 |
| O₂  | 1.36 | 0.0318 |
| CO₂ | 3.59 | 0.0427 |
| H₂O | 5.46 | 0.0305 |
| He  | 0.0342 | 0.0237 |
| CCl₄ | 20.4 | 0.1383 |

### Example

3.46 mol CO₂ at 502 K in 4.25 L:
- Ideal: P = nRT/V = (3.46)(0.08206)(502)/4.25 = 33.5 atm.
- van der Waals: P = nRT/(V − nb) − n²a/V² = 32.4 atm.

The 3.3% difference shows deviations are small at moderate pressure and elevated temperature, since CO₂ molecules do have some volume and attractions that the ideal gas law ignores.
