---
title: "Repeated Division Method"
type: concept
tags: [systems, math, number-systems, algorithm, base-conversion]
sources: [dis-4-2-conversion]
last_updated: 2026-05-17
---

# Repeated Division Method

The **repeated division method** is one of two interchangeable algorithms [[dis-4-2-conversion|DIS Ch 4.2]] gives for **decimal → base-$B$** conversion. It trades **memorization of powers of $B$** for **a sequence of divide-by-$B$ operations** — the right choice when the powers are unfamiliar or when implementing the conversion in code.

## Algorithm (general form)

To convert a decimal integer $n$ to base $B$:

1. Compute $n \div B$. Record the **remainder** — this is the next digit (in $\{0, \ldots, B-1\}$).
2. Replace $n$ with the **quotient**.
3. Repeat until $n = 0$.
4. Read the recorded remainders **bottom-up** (last collected to first) — that's the base-$B$ representation.

## Specialization: Decimal → Binary

For $B = 2$, divide-by-2's remainder is just **parity** (even → 0, odd → 1). [[dis-4-2-conversion|Ch 4.2]] formulates the recurrence as:

> *"If the decimal value is even, the next bit should be a zero; if it's odd, the next bit should be a one."*

You don't even need to perform the full division — just check parity, then integer-divide by 2 (right-shift by 1).

## Worked Example: $422_{10} \to ?_2$

| Step | $n$ | $n \bmod 2$ | $n \div 2$ |
|---|---|---|---|
| 1 | 422 | **0** | 211 |
| 2 | 211 | **1** | 105 |
| 3 | 105 | **1** | 52 |
| 4 | 52 | **0** | 26 |
| 5 | 26 | **0** | 13 |
| 6 | 13 | **1** | 6 |
| 7 | 6 | **0** | 3 |
| 8 | 3 | **1** | 1 |
| 9 | 1 | **1** | 0 |

Reading bottom-up: `1 1 0 1 0 0 1 1 0` → $422_{10} = $ `0b110100110`. Verified: $256 + 128 + 32 + 4 + 2 = 422$. ✓

## Why It Works

At each step the remainder $r_k = n_k \bmod B$ is exactly the digit at place value $B^k$ in the base-$B$ expansion — that's the **division algorithm** in elementary number theory: any $n_k$ decomposes uniquely as $n_k = q_k B + r_k$ with $0 \le r_k < B$, and the quotient $q_k$ carries the higher-order digits.

## Comparison: Powers-of-$B$ Method

[[dis-4-2-conversion|Ch 4.2]] presents both methods as **interchangeable** (same answer, different mental ergonomics):

| Method | Strength | Weakness |
|---|---|---|
| Powers-of-$B$ | One pass, large jumps | Requires memorized powers |
| Repeated division | No memorization | Many small steps |

For $B = 16$, the powers-of-$B$ method usually wins because most programmers know $1, 16, 256, 4096, 65536, \ldots$ For arbitrary $B$ or when implementing in code, repeated division is the safer default.

## Connections

- [[BaseConversion]] — the umbrella concept; this is route 3.
- [[NumberBase]] — the framework whose digits this method extracts.
- [[BinaryNumber]] — the most common target (the parity simplification).
- [[OctalNumber]] / [[HexadecimalNumber]] — also work, with $B = 8$ / $B = 16$ divisions.
- [[PositionalNotation]] — the place-value formalism the method inverts.
- [[BinaryHexConversion]] — the alternate shortcut when both ends are powers of 2.
- [[dis-4-2-conversion]] — source.
