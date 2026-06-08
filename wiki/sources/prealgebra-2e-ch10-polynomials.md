---
title: "Prealgebra 2e — Ch 10: Polynomials"
type: source
tags: [math, prealgebra, openstax, textbook, polynomials]
date: 2026-06-07
source_file: https://openstax.org/books/prealgebra-2e/pages/10-introduction
---

## Summary
Chapter 10 of OpenStax [[Prealgebra]] 2e introduces **polynomials** — algebraic expressions built from one or more terms — and the four operations on them (add, subtract, multiply, divide), together with the **properties of exponents** that those operations require. It defines monomial/binomial/trinomial, degree, and standard form; develops the product, power, product-to-a-power, quotient, zero-exponent, quotient-to-a-power, and negative-exponent properties; introduces **scientific notation** as an application of integer exponents; and closes with the inverse of multiplication — **factoring out the greatest common factor (GCF)**. It is the algebraic capstone of the book, applying the [[DistributiveProperty|distributive property]] and signed-number arithmetic from earlier chapters.

## Sections
- **10.1 Add and Subtract Polynomials** — vocabulary (monomial, binomial, trinomial, polynomial), degree of a term and of a polynomial, standard form; combining like terms to add/subtract; evaluating a polynomial at a value.
- **10.2 Use Multiplication Properties of Exponents** — exponential notation; Product Property, Power Property, Product-to-a-Power Property; multiplying monomials.
- **10.3 Multiply Polynomials** — monomial × polynomial via distribution; binomial × binomial via distribution, the **FOIL** method, and the **vertical** method; trinomial × binomial.
- **10.4 Divide Monomials** — Quotient Property, Zero-Exponent Property, Quotient-to-a-Power Property; simplifying monomial quotients; dividing a polynomial by a monomial.
- **10.5 Integer Exponents and Scientific Notation** — Negative-Exponent Property; full summary of exponent properties extended to integer exponents; **scientific notation** and conversions; multiplying/dividing in scientific notation.
- **10.6 Introduction to Factoring Polynomials** — greatest common factor (GCF) of expressions; factoring the GCF out of a polynomial (distributive property in reverse); checking by multiplying.

## Key Concepts & Definitions
- **Polynomial** — a monomial, or two or more monomials combined by addition or subtraction. A **monomial** has one term (form `a·xᵐ`, `a` constant, `m` a whole number); a **binomial** has two terms; a **trinomial** has three terms.
- **Degree of a term** — the exponent of its variable (a constant has degree 0; a base with no written exponent has exponent 1). **Degree of a polynomial** — the highest degree among its terms.
- **Standard form** — terms written in descending order of degree.
- **Like terms** — terms with the same variables raised to the same exponents; only their coefficients are combined (exponents are unchanged).
- **Exponential notation** — in `aᵐ`, `a` is the base and `m` the exponent; `aᵐ` means multiply `m` factors of `a`.
- **Greatest common factor (GCF)** — the largest expression that is a factor of all the given expressions.
- **Scientific notation** — a number written as `a × 10ⁿ` with `1 ≤ a < 10` and `n` an integer.

## Key Procedures / Rules
**Exponent properties** (for nonzero bases where division/zero/negative is involved; `m, n` integers in §10.5, whole numbers earlier):

| Property | Formula |
|---|---|
| Product | `aᵐ · aⁿ = aᵐ⁺ⁿ` |
| Power | `(aᵐ)ⁿ = aᵐⁿ` |
| Product to a Power | `(ab)ᵐ = aᵐ·bᵐ` |
| Quotient | `aᵐ ⁄ aⁿ = aᵐ⁻ⁿ` (a≠0); equivalently `1 ⁄ aⁿ⁻ᵐ` when `n>m` |
| Zero Exponent | `a⁰ = 1` (a≠0) |
| Quotient to a Power | `(a⁄b)ᵐ = aᵐ ⁄ bᵐ` (b≠0) |
| Negative Exponent | `a⁻ⁿ = 1 ⁄ aⁿ` (a≠0) |

- **Add/Subtract polynomials** — to subtract, distribute the leading negative across every term of the second polynomial; then identify like terms, group them (commutative property), and combine coefficients; write in standard form.
- **Multiply monomial × polynomial** — distribute the monomial across each term: `a(b+c) = ab+ac`.
- **Multiply binomial × binomial** — three equivalent methods: (1) distribution; (2) **FOIL** = First, Outer, Inner, Last (multiply those four pairs, then combine like terms — applies only to binomials); (3) **vertical** method like numeric long multiplication.
- **Multiply trinomial × binomial** — distribute each term of the binomial across the trinomial (or use the vertical method); combine like terms.
- **Divide monomials** — apply the quotient property per base, simplify coefficients separately; **divide a polynomial by a monomial** by dividing each term of the polynomial by the monomial.
- **Convert to scientific notation** — move the decimal so the first factor is `≥1` and `<10`, count the places `n`; use `10ⁿ` if the original is `>1`, `10⁻ⁿ` if between 0 and 1. **Convert back** by moving the decimal `n` places right (positive `n`) or `|n|` places left (negative `n`). **Operate** by combining the coefficients and applying the product/quotient property to the powers of 10.
- **Factor the GCF from a polynomial** — find the GCF of all terms (prime-factor the coefficients, expand the variables), rewrite each term as GCF × something, then apply the distributive property in reverse: `ab+ac = a(b+c)`; check by multiplying back.

## Connections
- [[Polynomial]] — the central object; classification, degree, add/subtract/multiply.
- [[ExponentRules]] — all seven exponent properties developed across §10.2, §10.4, §10.5.
- [[ScientificNotation]] — §10.5 application of integer exponents.
- [[FactoringPolynomials]] — §10.6 GCF factoring, the inverse of distribution.
- [[DistributiveProperty]] — the engine for multiplying and (in reverse) factoring polynomials.
- [[AlgebraicExpression]] — polynomials are a kind of algebraic expression; terms, coefficients, like terms carry over.
- [[PrimeFactorization]] / [[MultiplesAndFactors]] — used to find the numeric part of a GCF.
- [[SignedNumberArithmetic]] — sign handling when subtracting and distributing negatives.
- [[OrderOfOperations]] — governs how `(−3)⁴` vs `−3⁴` are evaluated.
- [[Decimal]] — scientific notation rests on decimal place value.
- [[Variable]] — terms are built from variables raised to whole-number powers.
- [[Prealgebra]] / [[OpenStax]] — the book and publisher.

## Contradictions
None found. Naming note: the wiki's [[Exponent]] page is the IEEE-754 floating-point exponent *field* (off-domain); prealgebra exponential notation and the exponent rules live in [[ExponentRules]], not there.
