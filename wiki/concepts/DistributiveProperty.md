---
title: "Distributive Property"
type: concept
tags: [math, prealgebra, algebra, properties-of-real-numbers]
sources: [prealgebra-2e-ch07-properties-of-real-numbers]
last_updated: 2026-06-07
---

# Distributive Property

The **distributive property** connects multiplication and addition: multiplying a number by a sum is the same as multiplying it by each addend and then adding. OpenStax [[Prealgebra]] 2e (Chapter 7, [[prealgebra-2e-ch07-properties-of-real-numbers]], §7.3) states it for [[RealNumbers|real numbers]] `a, b, c`:

> `a(b + c) = ab + ac`   and, for subtraction,   `a(b − c) = ab − ac`

The factor on the outside is **distributed to each term** inside the parentheses. It also works on the right (`(b + c)a = ba + ca`) and over more than two terms.

A concrete motivation from §7.3: three friends each buy a `$9.25` movie ticket. Splitting `9.25` into `9 + 0.25` and distributing, `3(9 + 0.25) = 3·9 + 3·0.25 = 27 + 0.75 = $27.75` — the same as `3 · 9.25`.

## Why it matters
Unlike the [[CommutativeProperty|commutative]] and [[AssociativeProperty|associative]] properties (each about a single operation), the distributive property **links the two operations**, which is what makes it the workhorse of algebra. It is the tool for **removing parentheses** when the terms inside cannot simply be combined, and it is the justification for **combining like terms** (`3x + 5x = (3 + 5)x = 8x`).

## Forms and worked-example types (§7.3)
- **Integer coefficient:** `6(5y + 1) = 30y + 6`.
- **Subtraction:** `2(x − 3) = 2x − 6`.
- **Fraction multiplier:** `¾(n + 12) = ¾n + 9`.
- **Decimal multiplier:** `100(0.3 + 0.25q) = 30 + 25q`.
- **Variable multiplier:** `m(n − 4) = mn − 4m` (then written with the coefficient first per the [[CommutativeProperty]]).
- **Negative multiplier:** `−2(4y + 1) = −8y − 2` (the sign multiplies every term).
- **Distributing a bare negative:** `−(y + 5) = −y − 5` (treat the leading `−` as `−1`).
- **Combining after distributing:** `4(x − 8) − (x + 3) = 4x − 32 − x − 3 = 3x − 35`.

A verification example evaluates the original and the distributed form at a value (e.g. `y = 10` gives `306` for both `6(5y + 1)` and `6·5y + 6·1`) to confirm equivalence.

## Connections
- [[CommutativeProperty]] / [[AssociativeProperty]] — the other two field properties; distribution links the operations they each govern.
- [[IdentityInverseZeroProperties]] — distributing a bare `−` uses `−1` and the inverse idea; simplifications mix all the properties.
- [[RealNumbers]] — the set on which it holds.
- [[Variable]] / [[AlgebraicExpression]] — distribution removes parentheses and underlies combining like terms.
- [[SignedNumberArithmetic]] — sign handling when distributing negatives.
- [[Fraction]] / [[Decimal]] — fraction- and decimal-multiplier examples.
- [[OrderOfOperations]] — distribution is the alternative to "parentheses first" when the inside can't be simplified.
- [[Equation]] — distributing is a standard step when solving equations.
- [[prealgebra-2e-ch07-properties-of-real-numbers]] — source (Ch 7.3).
