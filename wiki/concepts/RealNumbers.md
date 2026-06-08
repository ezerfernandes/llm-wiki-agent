---
title: "Real Numbers"
type: concept
tags: [math, prealgebra, number-systems, real-numbers]
sources: [prealgebra-2e-ch07-properties-of-real-numbers]
last_updated: 2026-06-07
---

# Real Numbers

The **real numbers** are all the numbers that can be placed on a [[NumberLine|number line]] — the union of the **rational** numbers and the **irrational** numbers. OpenStax [[Prealgebra]] 2e (Chapter 7, [[prealgebra-2e-ch07-properties-of-real-numbers]], §7.1) names this set, which the earlier chapters had been building one piece at a time, and uses it as the domain on which the [[CommutativeProperty|commutative]], [[AssociativeProperty|associative]], [[DistributiveProperty|distributive]], and [[IdentityInverseZeroProperties|identity/inverse/zero]] properties are stated.

## Rational numbers
A **rational number** is any number that can be written as a **ratio** `p/q` where `p` and `q` are integers and `q ≠ 0`. This makes a rational number nothing more than a [[Fraction|fraction]] of integers — and it captures a lot:

- Every [[Integer|integer]] is rational, because `n = n/1` (e.g. `−7 = −7/1`).
- Every [[Fraction|fraction]] and [[MixedNumber|mixed number]] is rational.
- Every **terminating** [[Decimal|decimal]] is rational (`7.3 = 73/10`, `−1.2684 = −12684/10000`).
- Every **repeating** decimal is rational (`0.3̄ = 1/3`; the bar marks the repeating block).

The decimal test is the quick one: **a decimal that stops or repeats is rational.**

## Irrational numbers
An **irrational number** is a real number that **cannot** be written as a ratio of two integers. Equivalently, its decimal form **never terminates and never repeats** — the digits run on forever with no repeating block:

- `π = 3.141592653…`
- `√5 = 2.2360679…`

The classic source of irrationals at this level is the [[SquareRoot|square root]] of a number that is **not a perfect square**. So `√36 = 6` is rational (perfect square), but `√44` is irrational; `√100 = 10` is rational, `√5` is not.

## The number-set hierarchy
The sets nest, each one extending the last:

```
counting (natural):  1, 2, 3, 4, …
whole:               0, 1, 2, 3, …          (adds 0)
integers:        …, −2, −1, 0, 1, 2, …      (adds the negatives / opposites)
rational:        all of the above, plus every p/q and terminating/repeating decimal
irrational:      the non-terminating, non-repeating decimals (π, √2, …)  — a separate set
real:            rational  ∪  irrational
```

So counting ⊂ [[WholeNumbers|whole]] ⊂ [[Integer|integer]] ⊂ rational ⊂ real, while the irrationals sit *alongside* the rationals; together they make up the reals. A single number can belong to several sets at once (e.g. `5` is counting, whole, integer, rational, and real).

## Classifying a number
1. Can you write it as `p/q` with integers and `q ≠ 0`? → rational.
2. Is it a decimal? Stops or repeats → rational; runs on without repeating → irrational.
3. Is it a square root? Perfect-square radicand → rational; otherwise → irrational.
4. Worked-example types in §7.1: write numbers as ratios of integers; decide rational vs irrational for a list of decimals; classify [[SquareRoot|square roots]] (`√36` vs `√44`); and categorize a mixed list across all the sets at once.

## Connections
- [[WholeNumbers]] / [[Integer]] — the counting, whole, and integer subsets nested inside the rationals.
- [[Fraction]] / [[MixedNumber]] / [[EquivalentFractions]] — a rational number is exactly a fraction `p/q` of integers.
- [[Decimal]] / [[DecimalFractionConversion]] — terminating and repeating decimals are precisely the rationals.
- [[SquareRoot]] — roots of non-perfect squares are the chapter's irrational numbers.
- [[NumberLine]] — every real number is a point on the line.
- [[CommutativeProperty]] / [[AssociativeProperty]] / [[DistributiveProperty]] / [[IdentityInverseZeroProperties]] — the properties that hold for all real numbers.
- [[TypesOfNumber]] — the broader catalog of number kinds.
- [[prealgebra-2e-ch07-properties-of-real-numbers]] — source (Ch 7.1).
