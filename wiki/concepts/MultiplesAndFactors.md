---
title: "Multiples and Factors"
type: concept
tags: [math, prealgebra, arithmetic, number-theory]
sources: [prealgebra-2e-ch02-language-of-algebra]
last_updated: 2026-06-07
---

# Multiples and Factors

**Multiples** and **factors** are two sides of the same multiplication fact, and together they are the gateway from arithmetic into number theory. OpenStax [[Prealgebra]] 2e (Chapter 2, [[prealgebra-2e-ch02-language-of-algebra]], section 2.4) introduces them as the groundwork needed to do [[PrimeFactorization|prime factorization]] and to find the [[LeastCommonMultiple|least common multiple]] when working with fractions.

A **multiple** of a number `n` is the product of `n` and a counting number: the multiples of 2 are `2, 4, 6, 8, …` and the multiples of 5 are `5, 10, 15, 20, …`. When a number `m` is a multiple of `n`, we say `m` is **divisible by** `n` — the division `m ÷ n` comes out evenly with no remainder. Multiples and [[Divisibility|divisibility]] are thus the same relationship viewed forward (multiplying up) or backward (dividing evenly).

Rather than divide every time, pre-algebra uses quick **divisibility tests** that inspect a number's digits. A number is divisible by:
- **2** if its last digit is 0, 2, 4, 6, or 8;
- **3** if the sum of its digits is divisible by 3;
- **4** if the number formed by its last two digits is divisible by 4;
- **5** if its last digit is 0 or 5;
- **6** if it is divisible by **both 2 and 3**;
- **10** if its last digit is 0.

(Chapter 2 adds the test for 4 to the tests for 2, 3, 5, 6, and 10 carried over from [[prealgebra-2e-ch01-whole-numbers|Chapter 1]]; see [[Divisibility]] for the full collection.)

A **factor** is the flip side of a multiple. In `a · b = m`, both `a` and `b` are **factors** of `m`, and `m` is their **product**. So 8 is a factor of 24 because `8 · 3 = 24`. To **find all the factors** of a number, divide it by each counting number in turn (1, 2, 3, …); whenever the quotient is a whole number, the divisor and quotient form a **factor pair**; stop once the quotient drops below the divisor (the pairs start repeating), then list every factor from smallest to largest. For 72 the factor pairs are `1·72, 2·36, 3·24, 4·18, 6·12, 8·9`, giving factors `1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72`.

Counting the factors classifies a number. A **prime number** is a counting number greater than 1 whose only factors are 1 and itself (2, 3, 5, 7, 11, …). A **composite number** is a counting number greater than 1 that is not prime — it has at least one factor besides 1 and itself. The number **1 is neither prime nor composite**. To decide which a number is, test each prime (2, 3, 5, 7, …) as a divisor: if any prime divides it evenly the number is composite; if none do (before the quotient falls below the divisor) it is prime. This prime-vs-composite distinction is precisely what [[PrimeFactorization|prime factorization]] in section 2.5 builds on.

## Connections
- [[Divisibility]] — the divisibility tests used to find multiples; 2.4 adds the test for 4.
- [[PrimeFactorization]] — uses factors and primes to break a composite number into primes.
- [[LeastCommonMultiple]] — uses common multiples; the reason multiples are taught here.
- [[WholeNumberArithmetic]] — multiples/factors are forward/backward views of multiplication and division.
- [[prealgebra-2e-ch01-whole-numbers]] — prior chapter with the original divisibility tests.
- [[prealgebra-2e-ch02-language-of-algebra]] — source (Ch 2.4).
