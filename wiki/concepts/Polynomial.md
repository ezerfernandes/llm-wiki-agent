---
title: "Polynomial"
type: concept
tags: [math, prealgebra, algebra, polynomials]
sources: [prealgebra-2e-ch10-polynomials]
last_updated: 2026-06-07
---

# Polynomial

A **polynomial** is a monomial, or two or more monomials combined by addition or subtraction. It is a special kind of [[AlgebraicExpression|algebraic expression]] in which every term is a constant times a product of variables raised to **whole-number** exponents. OpenStax [[Prealgebra]] 2e (Chapter 10, [[prealgebra-2e-ch10-polynomials]]) introduces polynomials and the four operations on them; this page covers classification, degree, and addition/subtraction/multiplication. (Division by a monomial and GCF factoring are covered in [[ExponentRules]] and [[FactoringPolynomials]].)

## Classification by number of terms
- **Monomial** — exactly one term, of the form `a·xᵐ` where `a` is a constant and `m` a whole number (e.g. `7`, `3x`, `−4z²`).
- **Binomial** — exactly two terms (e.g. `x + 3`, `4y − 5`).
- **Trinomial** — exactly three terms (e.g. `x² + 9x + 7`).
- A polynomial with more than three terms is just called a *polynomial* (no special name).

## Degree and standard form
- The **degree of a term** is the exponent on its variable. A constant has degree 0; a variable written with no exponent has an understood exponent of 1.
- The **degree of a polynomial** is the highest degree among its terms.
- **Standard form** writes the terms in **descending order of degree**, e.g. `2x³ + x² − 7x + 24`.

## Add and subtract
Adding and subtracting polynomials is just **combining [[AlgebraicExpression|like terms]]** — terms with identical variables raised to identical exponents. Only the coefficients are combined; the variable parts and exponents are unchanged (`3x + 5x = 8x`, but `3x + 3x²` cannot combine).

- **Add:** identify like terms, group them (commutative property of addition), add their coefficients, write in standard form.
- **Subtract:** first **distribute the leading negative** to *every* term of the second polynomial (this is where [[SignedNumberArithmetic|sign handling]] matters), then combine like terms. e.g. `(4x² + 7) − (x² − 3) = 4x² + 7 − x² + 3 = 3x² + 10`.
- **Evaluate** a polynomial by substituting a value for the variable and simplifying via the [[OrderOfOperations|order of operations]] (exponents before multiplication). Applications include projectile height, stopping distance, and fuel efficiency.

## Multiply
Multiplication of polynomials is driven by the [[DistributiveProperty|distributive property]] and the [[ExponentRules|product property of exponents]] (`xᵐ·xⁿ = xᵐ⁺ⁿ`). Note the sum/product distinction: `x + x = 2x` (combine like terms) but `x · x = x²` (add exponents).

- **Monomial × polynomial:** distribute the monomial over each term — `a(b + c) = ab + ac`. e.g. `−2x(5x² + 7x − 3) = −10x³ − 14x² + 6x`.
- **Binomial × binomial:** three equivalent methods —
  1. **Distribution** — treat one binomial as a unit and distribute it across the other.
  2. **FOIL** — multiply the **F**irst, **O**uter, **I**nner, **L**ast pairs of terms, then combine like terms. e.g. `(x + 6)(x + 9) = x² + 9x + 6x + 54 = x² + 15x + 54`. FOIL applies **only to two binomials**, not to other polynomials.
  3. **Vertical** method — stack the binomials and multiply like numeric long multiplication, aligning like terms before adding.
- **Trinomial × binomial:** distribute each term of the binomial across the trinomial (or use the vertical method) and combine like terms. e.g. `(x + 3)(2x² − 5x + 8) = 2x³ + x² − 7x + 24`.

## Connections
- [[AlgebraicExpression]] — polynomials are a subtype; terms, coefficients, and like terms come from here.
- [[ExponentRules]] — the product property powers polynomial multiplication; the quotient property handles monomial division.
- [[FactoringPolynomials]] — the inverse of multiplying out: pulling a GCF back out.
- [[DistributiveProperty]] — the rule behind every polynomial multiplication (and, reversed, behind factoring).
- [[SignedNumberArithmetic]] — distributing a leading negative when subtracting.
- [[OrderOfOperations]] — used when evaluating a polynomial at a value.
- [[Variable]] — terms are constants times variables raised to whole-number powers.
- [[prealgebra-2e-ch10-polynomials]] — source (Ch 10.1, 10.3).
