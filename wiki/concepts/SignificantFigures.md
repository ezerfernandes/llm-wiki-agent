---
title: "Significant Figures"
type: concept
tags: [chemistry, general-chemistry, measurement, uncertainty, physics]
sources: [chemistry-2e-ch01-essential-ideas, college-physics-2e-ch01]
last_updated: 2026-06-07
---

# Significant Figures

**Significant figures** communicate the uncertainty in a measured quantity. Counting (when the count does not change) and defined relationships (1 in = exactly 2.54 cm; 1 g = exactly 0.001 kg) yield **exact numbers** with no uncertainty; all other measurements are uncertain.

## Counting significant figures
- **Nonzero digits** are always significant.
- **Leading zeros** (before the first nonzero digit) are never significant — 0.00832407 has 6 sig figs.
- **Captive zeros** (between nonzero digits) are always significant — 70.607 has 5 sig figs.
- **Trailing zeros** are significant only if to the right of a decimal point — 55.0 has 3 sig figs. Ambiguous cases are resolved with scientific notation: 1.3 × 10³ (2), 1.30 × 10³ (3), 1.300 × 10³ (4).

## Rules for calculations
1. **Addition/subtraction:** round to the fewest *decimal places* among the inputs (1.0023 g + 4.383 g = 5.385 g; 486 g − 421.23 g = 65 g).
2. **Multiplication/division:** round to the fewest *significant figures* among the inputs (0.6238 cm × 6.6 cm = 4.1 cm²).
3. **Rounding:** dropped digit < 5 round down; > 5 round up; exactly 5 (last, or followed only by zeros) round to make the retained digit *even*; 5 followed by nonzero digits round up.

A calculated result is at least as uncertain as the least-certain measurement it came from. Significant figures are distinct from — but related to — [[AccuracyAndPrecision]].

## In Physics (OpenStax College Physics 2e, Ch. 1)
Physics frames significant figures around instrument precision: the last digit recorded in a measurement is the first digit carrying uncertainty. The same calculation rules apply — multiplication/division keeps the fewest significant figures of the inputs; addition/subtraction keeps the fewest decimal places. Trailing zeros (e.g., 1300) are ambiguous and resolved with scientific notation. Uncertainty can also be reported as **percent uncertainty**, % unc = (δA / A) × 100%, where a measurement is written A ± δA. See [[Uncertainty]].

## Connections
- [[AccuracyAndPrecision]] — closeness to true value vs. repeatability
- [[Uncertainty]] — the δA in A ± δA and percent uncertainty
- [[SIUnits]] — measurements carry units and uncertainty
- [[Density]] / [[DimensionalAnalysis]] — sig-fig rules applied in calculations
- [[chemistry-2e-ch01-essential-ideas]] — source chapter (chemistry)
- [[college-physics-2e-ch01]] — source chapter (physics)
