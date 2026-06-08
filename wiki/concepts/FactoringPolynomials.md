---
title: "Factoring Polynomials (GCF)"
type: concept
tags: [math, prealgebra, algebra, polynomials, factoring]
sources: [prealgebra-2e-ch10-polynomials]
last_updated: 2026-06-07
---

# Factoring Polynomials (GCF)

**Factoring** a polynomial means writing it as a **product** of factors — the inverse of multiplying it out. OpenStax [[Prealgebra]] 2e (Chapter 10, [[prealgebra-2e-ch10-polynomials]], §10.6) introduces the first and most general technique: pulling out the **greatest common factor (GCF)**. This is the [[DistributiveProperty|distributive property]] run in reverse: where multiplication does `a(b + c) = ab + ac`, factoring does `ab + ac = a(b + c)`.

## Greatest common factor of expressions
The **GCF** of two or more expressions is the largest expression that is a factor of all of them — it has both a numeric part (the GCF of the coefficients) and a variable part (each common variable to its **lowest** power).

**Steps to find the GCF:**
1. Factor each coefficient into primes (see [[PrimeFactorization]]) and write each variable's power in expanded form.
2. List the factors, aligning common factors in columns; circle the factors shared by *all* the expressions.
3. Bring down the common factors that every expression has.
4. Multiply those factors together — that product is the GCF.

For example, the GCF of `12x²` and `18x³` is `6x²` (numeric GCF `6` from `12 = 2·2·3`, `18 = 2·3·3`; the shared variable power is `x²`).

## Factor the GCF out of a polynomial
1. Find the GCF of all the polynomial's terms.
2. Rewrite each term as the GCF times the remaining factor.
3. Apply the distributive property **in reverse** to pull the GCF outside parentheses.
4. **Check** by multiplying the factored form back out — it should reproduce the original polynomial.

Example: `12x² + 18x³ = 6x²(2) + 6x²(3x) = 6x²(2 + 3x)`. The examples in §10.6 range over constants only, variable-and-constant mixes, variables with exponents, binomials and trinomials, and cases with a negative leading coefficient (where the GCF carries the negative sign).

## Connections
- [[DistributiveProperty]] — factoring out the GCF is this property applied in reverse.
- [[Polynomial]] — factoring is the inverse of the polynomial multiplication taught in the same chapter.
- [[PrimeFactorization]] — used to find the numeric part of the GCF.
- [[MultiplesAndFactors]] — supplies the factor/common-factor ideas the GCF builds on.
- [[ExponentRules]] — the variable part of the GCF takes each common variable to its lowest power.
- [[prealgebra-2e-ch10-polynomials]] — source (Ch 10.6).
