---
title: "Floating-Point Precision (Rounding Error)"
type: concept
tags: [floating-point, numerics, ieee-754, rounding, precision, software-engineering-failures]
sources: [dis-4-8-floating-point]
last_updated: 2026-05-17
---

# Floating-Point Precision (Rounding Error)

**Floating-point precision** describes the **error introduced when a real number is rounded to the nearest representable [[IEEE754|IEEE 754]] value**. Unlike [[FixedPoint|fixed-point]]'s uniform absolute precision, [[FloatingPoint|floating-point]] precision is **relative** — bounded by the **machine epsilon** $\epsilon \approx 2^{-23} \approx 1.19 \times 10^{-7}$ for `binary32`, $\epsilon \approx 2.22 \times 10^{-16}$ for `binary64`.

## The fundamental impossibility

[[dis-4-8-floating-point|Ch 4.8]] opens with: *"for any binary encoding of real numbers, there exist values that cannot be represented exactly."* Integers are countably infinite; reals are uncountable; any finite-bit encoding must approximate **almost all** real numbers — including innocuous-looking decimals like $0.1$ (which has an infinitely repeating binary expansion).

## Non-associativity under rounding

[[dis-4-8-floating-point|Ch 4.8]] directly quote: *"like fixed-point, rounding problems similarly affect floating-point encodings."* The same demonstration the chapter gives for [[FixedPoint|fixed-point]] arithmetic applies to floats: operation order changes the result.

Common failure modes:
- **Catastrophic cancellation** — subtracting two nearly-equal floats wipes out most of the mantissa precision, leaving noise.
- **Accumulated rounding** — summing $N$ floats with naïve accumulation can lose $\sim \log_2 N$ bits; [[KahanSummation|Kahan summation]] recovers them with a compensation term.
- **Cross-precision conversion** — converting `binary64` ↔ `binary32` ↔ integer is a lossy operation that can overflow or truncate silently.

## Two real-world catastrophes [[dis-4-8-floating-point|Ch 4.8]] cites

### 1991 Patriot missile failure (Dhahran, Saudi Arabia)

The Patriot air-defense battery used a 24-bit fixed-point clock counting tenths of seconds. Multiplying by $0.1$ — which is **not exactly representable** in binary (repeating fraction `0.0001100110011…`) — accumulated drift over 100+ hours of continuous operation. The battery's tracking error grew large enough that it *"fail[ed] to intercept an Iraqi Scud missile,"* killing 28 U.S. soldiers. The fix existed — a software patch — but had not yet been installed.

**Lesson**: rounding error is a function of *runtime duration*, not just *expression complexity*. Long-running systems must reset / re-anchor floating-point accumulators.

### 1996 Ariane 5 rocket explosion

The European Space Agency's Ariane 5 maiden launch *"exploded 39 seconds after taking off"* when an inertial-reference subsystem (reused from the slower Ariane 4) tried to convert a 64-bit floating-point velocity to a 16-bit signed integer. The Ariane 5 reached velocities outside the Ariane 4's design envelope; the conversion **overflowed**; an unhandled exception cascaded; the rocket's self-destruct fired.

**Lesson**: float-to-int conversions are unchecked overflow ([[IntegerOverflow|integer overflow]]) waiting to happen. Reused code carries its source platform's assumptions; new platforms invalidate them.

## Defenses (wiki deepening — not in [[dis-4-8-floating-point|Ch 4.8]])

- **Use the right type** — `decimal` (arbitrary-precision base-10) for money, integers for counts, [[FixedPoint|fixed-point]] for bounded-domain DSP, `binary64` for general scientific computing.
- **Compare with tolerance** — `abs(a - b) < eps` instead of `a == b`; relative tolerance for large magnitudes.
- **Numerically stable algorithms** — Kahan summation, Welford's variance, pairwise summation, log-sum-exp trick.
- **Saturating / checked conversion** — wrap float-to-int in `clamp` + explicit-error code paths; never silently truncate at the ISA-defined boundary.
- **Determinism flags** — disable `-ffast-math` for code that must be reproducible across platforms; the compiler will not reorder rounding-sensitive expressions.

## Connections

- [[FloatingPoint]] / [[IEEE754]] — the encoding whose precision this concept characterizes.
- [[FixedPoint]] — shares the rounding-non-associativity property.
- [[Mantissa]] — the field that bounds precision.
- [[IntegerOverflow]] — the failure mode Ariane 5 hit on float-to-int conversion.
- [[UndefinedBehavior]] — float-to-int overflow is UB in C, well-defined-but-platform-specific in other languages.
- [[Patriot]] / [[Ariane5]] — the two cited catastrophes.
- [[dis-4-8-floating-point]] — DIS Ch 4.8 source.
