---
title: "Exponent Rules (Properties of Exponents)"
type: concept
tags: [math, prealgebra, algebra, exponents, polynomials]
sources: [prealgebra-2e-ch10-polynomials]
last_updated: 2026-06-07
---

# Exponent Rules (Properties of Exponents)

The **properties of exponents** are the rules for simplifying products, quotients, and powers of exponential expressions. In **exponential notation** `aᵐ`, the number `a` is the **base** and `m` is the **exponent**, and `aᵐ` means *multiply `m` factors of `a`*. OpenStax [[Prealgebra]] 2e (Chapter 10, [[prealgebra-2e-ch10-polynomials]]) develops these rules across §10.2 (multiplication), §10.4 (division), and §10.5 (integer exponents), where the bases are whole-number exponents at first and then extended to all integers.

> **Disambiguation:** the wiki page [[Exponent]] is the IEEE-754 floating-point exponent *field* — a hardware/binary-representation concept, **not** this. Prealgebra exponential notation and the rules below live on *this* page.

## The seven properties
For real numbers `a, b` and integers `m, n` (with the nonzero restrictions noted):

| Property | Formula | In words |
|---|---|---|
| **Product** | `aᵐ · aⁿ = aᵐ⁺ⁿ` | multiply like bases → add exponents |
| **Power** | `(aᵐ)ⁿ = aᵐⁿ` | raise a power to a power → multiply exponents |
| **Product to a Power** | `(ab)ᵐ = aᵐ·bᵐ` | raise a product to a power → raise each factor |
| **Quotient** | `aᵐ ⁄ aⁿ = aᵐ⁻ⁿ` (a≠0) | divide like bases → subtract exponents |
| **Zero Exponent** | `a⁰ = 1` (a≠0) | any nonzero base to the 0 power is 1 |
| **Quotient to a Power** | `(a⁄b)ᵐ = aᵐ ⁄ bᵐ` (b≠0) | raise a fraction to a power → raise top and bottom |
| **Negative Exponent** | `a⁻ⁿ = 1 ⁄ aⁿ` (a≠0) | a negative exponent → reciprocal of the positive power |

When `n > m`, the quotient property can also be written `aᵐ ⁄ aⁿ = 1 ⁄ aⁿ⁻ᵐ`, which is consistent with the negative-exponent property.

## How they combine
- **Multiplying monomials** uses the product, power, and product-to-a-power properties together — e.g. `(2x³)(5x⁴) = 10x⁷`, `(x²y)³ = x⁶y³`.
- **Dividing monomials** uses the quotient, zero-exponent, and quotient-to-a-power properties — e.g. `x¹⁰⁄x⁸ = x²`, `(a⁰)= 1`, with coefficients simplified separately from the variables.
- **Negative exponents** are not "in simplest form" — rewrite them as reciprocals. The negative in the exponent does **not** change the sign of the base. Parentheses matter: `(5y)⁻¹ ≠ 5y⁻¹`, and order of operations means exponents apply before any multiplication.
- Sign/parenthesis subtlety from §10.2/§10.5: `(−3)⁴ = 81` (the base is `−3`) but `−3⁴ = −81` (only the 3 is the base) — see [[OrderOfOperations]].

## Connections
- [[Polynomial]] — the product property drives polynomial multiplication; the quotient property handles monomial division.
- [[ScientificNotation]] — `a × 10ⁿ` is exactly an integer-exponent expression; multiplying/dividing in scientific notation applies the product and quotient properties to the powers of 10.
- [[OrderOfOperations]] — explains `(−3)⁴` vs `−3⁴` and exponents-before-multiplication.
- [[PrimeFactorization]] — repeated prime factors are written compactly with exponents (`2²·3²`).
- [[Exponent]] — *off-domain* IEEE-754 floating-point exponent field; not the same concept (linked only for disambiguation).
- [[prealgebra-2e-ch10-polynomials]] — source (Ch 10.2, 10.4, 10.5).
