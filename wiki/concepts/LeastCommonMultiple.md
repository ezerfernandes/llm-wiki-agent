---
title: "Least Common Multiple (LCM)"
type: concept
tags: [math, prealgebra, arithmetic, number-theory]
sources: [prealgebra-2e-ch02-language-of-algebra]
last_updated: 2026-06-07
---

# Least Common Multiple (LCM)

The **least common multiple (LCM)** of two (or more) numbers is the **smallest number that is a multiple of all of them**. For example, the multiples of 4 are `4, 8, 12, 16, 20, 24, …` and the multiples of 6 are `6, 12, 18, 24, …`; their common multiples are `12, 24, …`, and the *least* of these is `12`, so `LCM(4, 6) = 12`. OpenStax [[Prealgebra]] 2e (Chapter 2, [[prealgebra-2e-ch02-language-of-algebra]], section 2.5) introduces the LCM mainly because it is the **least common denominator** needed to add and subtract fractions with unlike denominators in a later chapter.

**Listing-multiples method.** Write out the first several [[MultiplesAndFactors|multiples]] of each number, scan for the values that appear in *both* lists, and take the smallest one. This method is concrete and easy to understand, and it works well when the numbers are small. It becomes tedious when the numbers are large or share few small multiples, because the lists must be extended far before a common value appears.

**Prime-factors method.** Find the [[PrimeFactorization|prime factorization]] of each number and line the factorizations up so that equal primes sit in the same column. Then bring down each prime the **greatest number of times it appears in any single factorization**, and multiply those primes together. For instance, `15 = 3 · 5` and `18 = 2 · 3 · 3`; lining them up, the LCM takes one 2 (from 18), two 3's (the most in either, from 18), and one 5 (from 15), giving `2 · 3 · 3 · 5 = 90`. This method scales much better than listing and is the standard approach for larger numbers.

The two methods always agree. Listing builds intuition for what "common multiple" means, while the prime-factors method is the efficient, general tool. Note the symmetry with finding a *common factor*: the LCM takes the **highest** power of each prime across the numbers, whereas the greatest common factor (covered later) takes the **lowest** power of the primes they share.

## Connections
- [[MultiplesAndFactors]] — the multiples whose smallest common value is the LCM.
- [[PrimeFactorization]] — the prime-factors method depends on each number's prime factorization.
- [[Divisibility]] — common multiples are numbers divisible by each of the given numbers.
- [[prealgebra-2e-ch02-language-of-algebra]] — source (Ch 2.5).
