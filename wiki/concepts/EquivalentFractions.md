---
title: "Equivalent Fractions (and Simplifying)"
type: concept
tags: [math, prealgebra, arithmetic, fractions]
sources: [prealgebra-2e-ch04-fractions]
last_updated: 2026-06-07
---

# Equivalent Fractions (and Simplifying)

**Equivalent fractions** are fractions that name the **same value** even though they have different numerators and denominators — for example `1/2`, `2/4`, and `3/6` all mark the same point on the [[NumberLine|number line]]. OpenStax [[Prealgebra]] 2e (Chapter 4, [[prealgebra-2e-ch04-fractions]], sections 4.1–4.2) develops equivalent fractions because they make two essential operations possible: **simplifying** a [[Fraction|fraction]] to lowest terms, and rewriting unlike fractions over a common denominator so they can be added or subtracted (see [[FractionArithmetic]]).

The engine behind both is the **Equivalent Fractions Property**: if `b ≠ 0` and `c ≠ 0`, then
`a/b = (a·c)/(b·c)`.
Reading it left to right, multiplying numerator and denominator by the same nonzero number `c` produces an equivalent fraction (this is how you "build up" a fraction to a desired denominator, e.g. the LCD). Reading it right to left, dividing out a common factor produces an equivalent fraction in simpler form. The property is itself a consequence of the **Property of One** (`c/c = 1`): multiplying by `c/c` multiplies the value by 1 and so cannot change it.

**Simplifying** (also called *reducing* or writing *in lowest terms*) means producing the equivalent fraction whose numerator and denominator share **no common factor other than 1** — a *simplified fraction*. The procedure: rewrite the numerator and denominator showing their common factors — using [[PrimeFactorization|prime factorization]] when the numbers are large or share no obvious factor — remove the common factors via the Equivalent Fractions Property, and multiply whatever remains. For example `10/15 = (2·5)/(3·5) = 2/3`, and `210/385` simplifies cleanly once both are written as products of primes. The same idea applies to negative fractions (keep the sign), improper fractions, and fractions with variables (e.g. `5xy/15x = y/3`).

Recognizing equivalent fractions is also how the chapter **compares and orders** fractions: rewrite them over a common denominator and compare numerators. The "common denominator" used for this and for addition/subtraction is the [[LeastCommonMultiple|least common denominator]] — the LCM of the denominators.

## Connections
- [[Fraction]] — the object being rewritten; the Property of One underlies equivalence.
- [[FractionArithmetic]] — simplifying finishes most fraction computations; building up to the LCD enables addition/subtraction.
- [[LeastCommonMultiple]] — the least common denominator for comparing and combining unlike fractions.
- [[PrimeFactorization]] — exposes the common factors to cancel (and to build the LCD).
- [[NumberLine]] — equivalent fractions mark the same point.
- [[prealgebra-2e-ch04-fractions]] — source (Ch 4.1–4.2).
