---
title: "Divisibility"
type: concept
tags: [math, prealgebra, arithmetic, number-theory]
sources: [prealgebra-2e-ch01-whole-numbers, prealgebra-2e-ch02-language-of-algebra]
last_updated: 2026-06-07
---

# Divisibility

A whole number is **divisible** by another when dividing the first by the second leaves **no remainder** — the division comes out even. Equivalently, in the language of [[WholeNumberArithmetic|division]], the dividend is divisible by the divisor exactly when the remainder is 0. Divisibility lets you tell whether a number splits evenly *without* carrying out the full long division.

Pre-algebra teaches a small set of quick **divisibility tests** that inspect a number's digits:

- **By 2** — the last digit is even (0, 2, 4, 6, or 8).
- **By 3** — the sum of the digits is divisible by 3.
- **By 4** — the number formed by the **last two digits** is divisible by 4.
- **By 5** — the last digit is 0 or 5.
- **By 6** — the number is divisible by **both 2 and 3** (it passes both tests above).
- **By 10** — the last digit is 0.

(Chapter 1, [[prealgebra-2e-ch01-whole-numbers]], gives the tests for 2, 3, 5, 6, and 10; Chapter 2, [[prealgebra-2e-ch02-language-of-algebra]], adds the test for 4.)

These rules follow from [[PlaceValue]]: because each place is a power of ten, looking at the last digit (or the last two digits, or the digit sum) is enough to decide divisibility by 2, 4, 5, 10 (and 3). Divisibility is the gateway to later topics — finding [[MultiplesAndFactors|factors and multiples]], [[PrimeFactorization|primes and prime factorization]], the [[LeastCommonMultiple|least common multiple]], greatest common divisors, and reducing fractions — and is the condition under which a [[WholeNumberArithmetic|division]] of whole numbers produces a remainder of zero.

## Connections
- [[WholeNumberArithmetic]] — divisibility = division with remainder 0.
- [[WholeNumbers]] — the numbers being tested.
- [[PlaceValue]] — why digit-based tests work.
- [[MultiplesAndFactors]] — divisibility identifies a number's multiples and factors.
- [[PrimeFactorization]] / [[LeastCommonMultiple]] — number-theory topics built on divisibility.
- [[prealgebra-2e-ch01-whole-numbers]] — source (tests for 2, 3, 5, 6, 10).
- [[prealgebra-2e-ch02-language-of-algebra]] — source (adds the test for 4; uses divisibility for factors/primes/LCM).
