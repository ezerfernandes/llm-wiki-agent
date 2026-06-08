---
title: "Square Root"
type: concept
tags: [math, prealgebra, arithmetic, roots, exponents]
sources: [prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# Square Root

To **square** a number is to multiply it by itself: `n²`. If `n² = m`, then `m` is **the square of `n`**, and conversely **a square root of `m`** is any number whose square is `m`. A **perfect square** is the square of a whole number (1, 4, 9, 16, 25, …). OpenStax [[Prealgebra]] 2e (Chapter 5, [[prealgebra-2e-ch05-decimals]], §5.7) introduces squares and square roots; squaring is the [[Exponent|exponent]]-2 case.

## Two roots, one principal root
Because both `n²` and `(−n)²` equal the same positive number, **every positive number has two square roots — one positive, one negative** (both `10` and `−10` square to `100`). The **radical sign** `√` denotes only the **principal (positive) square root**:

> If `m = n²` then `√m = n` for `n ≥ 0`.

The number under the radical is the **radicand**. So `√100 = 10` (not `±10`), while `−√100 = −10` is "the opposite of the square root." There is **no real square root of a negative number** — `√(−25)` has no real value, because no real number squared is negative. This makes `√(−9)` (undefined in reals) sharply different from `−√9 = −3`.

## Radical as a grouping symbol
The radical sign acts like parentheses: **simplify everything under it first**. Hence `√(25 + 144) = √169 = 13`, which is *not* the same as `√25 + √144 = 5 + 12 = 17` (see [[OrderOfOperations]]).

## Simplifying and estimating
- **Perfect squares** simplify exactly (`√36 = 6`, `√121 = 11`). Memorizing squares of 1–15 helps.
- **Variable expressions** (assuming non-negative variables): `√(x²) = x`, `√(16x²) = 4x`, `√(36x²y²) = 6xy`; `−√(81y²) = −9y`.
- **Estimating**: trap a non-perfect-square radicand between consecutive perfect squares to bound its root between consecutive whole numbers — since `49 < 60 < 64`, `7 < √60 < 8`.
- **Calculator approximations** are *approximate*, not exact: `√5 ≈ 2.236… ≈ 2.24` ([[Decimal|decimal]] rounded), and `2.24² = 5.0176 ≠ 5`, so the result is rounded with `≈` (see [[Rounding]]).

## Applications
- **Side of a square** of area `A`: side `= √A` (area `200 ft²` → `≈ 14.1 ft`).
- **Falling-object time**: an object dropped from `h` feet reaches the ground in `√(h/4)` seconds (`h = 400` → `√100 = 5` s).
- **Skid-mark speed**: `speed (mph) = √(24d)` for skid length `d` feet (`d = 190` → `√4560 ≈ 67.5` mph).

## Connections
- [[Exponent]] — squaring is exponent 2; the square root inverts it.
- [[OrderOfOperations]] — the radical is a grouping symbol; simplify the radicand first.
- [[Decimal]] / [[Rounding]] — non-perfect roots are irrational and reported as rounded decimal approximations with `≈`.
- [[Variable]] — square roots of variable expressions (assumed non-negative).
- [[Integer]] / [[SignedNumberArithmetic]] — negatives have no real square root; `−√m` vs `√(−m)`.
- [[prealgebra-2e-ch05-decimals]] — source (Ch 5.7).
