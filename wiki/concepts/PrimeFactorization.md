---
title: "Prime Factorization"
type: concept
tags: [math, prealgebra, arithmetic, number-theory]
sources: [prealgebra-2e-ch02-language-of-algebra]
last_updated: 2026-06-07
---

# Prime Factorization

The **prime factorization** of a composite number is that number written as a **product of prime numbers**. For example, the prime factorization of 36 is `2 · 2 · 3 · 3` (often written `2² · 3²`). Every composite number has exactly one prime factorization apart from the order of the factors — a fact that makes the prime factorization a kind of "fingerprint" of a number. OpenStax [[Prealgebra]] 2e (Chapter 2, [[prealgebra-2e-ch02-language-of-algebra]], section 2.5) teaches two ways to find it, building directly on [[MultiplesAndFactors|factors and primes]] from section 2.4.

**Factor-tree method.** Write the number, then split it into *any* factor pair and draw two branches. Circle any factor that is prime (its branch is finished); for any composite factor, split it again into a factor pair and continue. Keep going until every branch ends in a circled prime. The prime factorization is the product of all the circled primes, written from least to greatest. A useful reassurance: it does not matter which factor pair you start with — `36 = 4 · 9` and `36 = 6 · 6` both lead to the same `2 · 2 · 3 · 3`.

**Ladder (stacked-division) method.** Divide the number by the **smallest prime that divides it**, writing the quotient below. Keep dividing by that same prime as long as it divides evenly, then move up to the next prime and repeat. Stop when the final quotient is itself prime. The prime factorization is the product of all the primes you divided by (down the side of the "ladder") together with that last prime quotient on top.

The two methods always give the same answer; the choice is a matter of preference. The factor tree is more visual and flexible about where you start, while the ladder is more systematic and tends to be tidier for larger numbers. Either way, the [[Divisibility|divisibility tests]] from section 2.4 are what tell you quickly which small primes to try first.

Prime factorization is not an end in itself in pre-algebra — its payoff comes immediately in the **prime-factors method** for the [[LeastCommonMultiple|least common multiple]] (and, later, the greatest common factor and reducing fractions). Because each number's prime factorization is unique, comparing two numbers' factorizations column by column is a reliable, mechanical way to combine them.

## Connections
- [[MultiplesAndFactors]] — supplies the factor and prime/composite ideas this builds on.
- [[Divisibility]] — the tests that reveal which small primes divide a number.
- [[LeastCommonMultiple]] — the prime-factors method for the LCM uses prime factorizations.
- [[Exponent]] — repeated prime factors are written compactly with exponents (e.g. `2² · 3²`).
- [[prealgebra-2e-ch02-language-of-algebra]] — source (Ch 2.5).
