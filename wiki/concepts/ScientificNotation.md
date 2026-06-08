---
title: "Scientific Notation"
type: concept
tags: [math, prealgebra, algebra, exponents]
sources: [prealgebra-2e-ch10-polynomials]
last_updated: 2026-06-07
---

# Scientific Notation

**Scientific notation** writes a number as a product `a × 10ⁿ`, where the **coefficient** satisfies `1 ≤ a < 10` and the **exponent** `n` is an integer. It is a compact way to express very large or very small numbers, and it is a direct application of the integer-exponent rules in [[ExponentRules]]. OpenStax [[Prealgebra]] 2e (Chapter 10, [[prealgebra-2e-ch10-polynomials]], §10.5) introduces it alongside negative exponents.

The exponent records how far, and in which direction, the decimal point sits relative to the standard form. A **positive** exponent means the number is `≥ 10` (large); a **negative** exponent means the number is between 0 and 1 (small).

## Convert a decimal to scientific notation
1. Move the decimal point so the first factor is `≥ 1` and `< 10`.
2. Count the number of places you moved it; call it `n`.
3. Write the number as the coefficient times a power of 10:
   - if the original number is `> 1`, use `10ⁿ`;
   - if the original number is between 0 and 1, use `10⁻ⁿ`.
4. Check the result.

Examples: `37,000 = 3.7 × 10⁴`; `0.0052 = 5.2 × 10⁻³`.

## Convert scientific notation to a decimal
1. Read the exponent `n` on the factor of 10.
2. Move the decimal point: `n` places to the **right** for a positive exponent, `|n|` places to the **left** for a negative exponent.
3. Add zeros as placeholders as needed.

Examples: `6.2 × 10³ = 6,200`; `8.9 × 10⁻² = 0.089`.

## Operate in scientific notation
- **Multiply:** multiply the coefficients and use the product property of exponents on the powers of 10 — `(4 × 10⁵)(2 × 10⁻⁷) = 8 × 10⁻² = 0.08`.
- **Divide:** divide the coefficients and use the quotient property on the powers of 10 — `(9 × 10³) ⁄ (3 × 10⁻²) = 3 × 10⁵ = 300,000`.

(If the resulting coefficient falls outside `[1, 10)`, renormalize by shifting one place and adjusting the exponent.) Applications include populations, probabilities, and physical measurements.

## Connections
- [[ExponentRules]] — `a × 10ⁿ` is an integer-exponent expression; multiplying/dividing applies the product and quotient properties.
- [[Decimal]] — scientific notation is built on decimal place value; converting back and forth just shifts the decimal point.
- [[Polynomial]] — same Chapter 10 toolkit of exponent properties.
- [[prealgebra-2e-ch10-polynomials]] — source (Ch 10.5).
