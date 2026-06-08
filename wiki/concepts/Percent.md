---
title: "Percent (and Percent Conversions & the Percent Equation)"
type: concept
tags: [math, prealgebra, arithmetic, percents]
sources: [prealgebra-2e-ch06-percents]
last_updated: 2026-06-07
---

# Percent (and Percent Conversions & the Percent Equation)

A **percent** is a [[Ratio|ratio]] whose **denominator is 100** — it means "per hundred" (from Latin *per centum*). The symbol is `%`, so `n%` is exactly `n/100`. Because every percent is a hundredths ratio, it is just another notation for the same number that can be written as a [[Fraction|fraction]] or a [[Decimal|decimal]]; the three forms are interchangeable. OpenStax [[Prealgebra]] 2e (Chapter 6, [[prealgebra-2e-ch06-percents]], §6.1–6.2) introduces percent and its arithmetic. (Probability and many [[Ratio|ratios/rates]] are routinely reported as percents — see [[probability]].)

## Conversions among percent, fraction, and decimal

These four procedures all rest on the single fact that `n% = n/100` (see also [[DecimalFractionConversion]] for the fraction↔decimal half of each):

- **Percent → fraction** — write the percent as a ratio over 100, then **simplify** (divide out common factors via [[EquivalentFractions]]). `36% = 36/100 = 9/25`. A decimal or mixed-number percent first clears its own fraction: `24.5% = 24.5/100 = 245/1000 = 49/200`; `33⅓% = (100/3)/100 = 1/3`. Percents over 100% give values greater than 1 (`125% = 5/4`).
- **Percent → decimal** — write over 100, then **divide numerator by denominator** (i.e. divide by 100). The quick pattern: **move the decimal point two places left** and drop the `%`. `6% = 0.06`; `78% = 0.78`; `135% = 1.35`; `12.5% = 0.125`.
- **Decimal → percent** — write the decimal as a hundredths fraction (or just **move the point two places right** and add `%`). `0.05 = 5%`; `1.05 = 105%`; `0.075 = 7.5%`.
- **Fraction → percent** — first convert the fraction to a [[Decimal|decimal]] (divide numerator by denominator), then convert that decimal to a percent. `3/4 = 0.75 = 75%`; `11/8 = 1.375 = 137.5%`; `1/3 = 0.333… ≈ 33.3%` (round as specified).

The two "move the point two places" shortcuts are the same rule of multiplying/dividing a [[Decimal|decimal]] by the power of ten 100 (see [[DecimalArithmetic]]).

## The percent equation

The core relationship for every percent application is:

> **amount = percent × base**

where the **base** is the original whole the percent is taken *of*, the **percent** is written **as a decimal** before multiplying, and the **amount** is the part. The word **"of"** signals the base and **"is"** signals the amount. Translating an English sentence into this equation (or into an [[Equation|algebraic equation]]) and solving gives three problem types:

- **Find the amount** — "What number is 35% of 90?" → `n = 0.35 × 90`.
- **Find the base** — "17 is 25% of what number?" → `17 = 0.25 × n`.
- **Find the percent** — "What percent of 36 is 9?" → `p × 36 = 9`.

The same three quantities can instead be set up as a **[[Proportion|percent proportion]]** `amount/base = percent/100` and solved by cross products — an alternative to the percent equation (§6.5).

## Percent increase and percent decrease

Both are computed as a change measured against the **original** amount:

- **Percent increase** — `increase = new amount − original`, then `increase / original`, expressed as a percent.
- **Percent decrease** — `decrease = original − new amount`, then `decrease / original`, expressed as a percent.

Results are typically rounded to the nearest tenth of a percent.

## Connections
- [[Ratio]] — a percent *is* a ratio with denominator 100; ratios are commonly reported as percents.
- [[Fraction]] / [[EquivalentFractions]] — a percent is a hundredths fraction; percent→fraction ends in simplifying.
- [[Decimal]] / [[DecimalArithmetic]] / [[DecimalFractionConversion]] — percent↔decimal is multiply/divide by 100 (shift the point two places); fraction↔percent routes through a decimal.
- [[Equation]] — percent problems are solved by translating a sentence into an equation and isolating the variable.
- [[Proportion]] — the percent proportion `amount/base = percent/100` is the alternative setup for the same problems.
- [[PercentApplications]] — tax, commission, discount, mark-up, and increase/decrease are all special cases of `amount = percent × base`.
- [[SimpleInterest]] — interest `I = Prt` applies a percent rate; the rate is converted to a decimal first.
- [[probability]] — probabilities (in `[0,1]`) are often expressed as percents.
- [[prealgebra-2e-ch06-percents]] — source (Ch 6.1–6.2).
