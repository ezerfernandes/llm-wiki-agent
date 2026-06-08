---
title: "Rounding"
type: concept
tags: [math, prealgebra, arithmetic, estimation]
sources: [prealgebra-2e-ch01-whole-numbers]
last_updated: 2026-06-07
---

# Rounding

**Rounding** replaces a number with a nearby, simpler number that is easier to work with — for example, reporting a crowd of 29,504 as "about 30,000." Rounding always happens **to a chosen place value** (nearest ten, nearest hundred, nearest thousand, and so on), so the first step is always to decide which place you are rounding to.

The core rule looks at the single digit **immediately to the right** of the target place:

- If that digit is **less than 5**, round **down** — leave the target digit unchanged.
- If that digit is **5 or greater**, round **up** — add 1 to the target digit.

Then **replace every digit to the right of the target place with zeros**. The digits to the left normally stay the same; the one exception is when rounding up turns a 9 into a 10, in which case the carry ripples left (rounding 29,504 to the nearest thousand makes the 9 thousands roll over, giving 30,000).

Rounding relies directly on [[PlaceValue]] — you cannot round without first identifying the target place and the digit just to its right. It is the basic tool for **estimation**: rounding the numbers in a problem before computing gives a quick sanity check on an exact answer from [[WholeNumberArithmetic]].

## Connections
- [[PlaceValue]] — rounding is defined relative to a chosen place.
- [[WholeNumbers]] — the numbers being rounded in this chapter.
- [[WholeNumberArithmetic]] — rounding/estimating checks the results of the four operations.
- [[Decimal]] — the same rule rounds decimals to tenths, hundredths, etc. (Ch 5).
- [[prealgebra-2e-ch01-whole-numbers]] — source.
