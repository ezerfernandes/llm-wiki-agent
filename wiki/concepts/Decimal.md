---
title: "Decimal"
type: concept
tags: [math, prealgebra, arithmetic, decimals, number-systems]
sources: [prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# Decimal

A **decimal** is a way of writing parts of a whole when the whole is divided into a **power of ten** — it extends [[PlaceValue|place value]] to the right of the **decimal point**. Where the whole-number places (ones, tens, hundreds, …) each grow ten-fold to the *left*, the decimal places each *shrink* ten-fold to the **right**: tenths (`1/10`), hundredths (`1/100`), thousandths (`1/1,000`), ten-thousandths (`1/10,000`), hundred-thousandths (`1/100,000`), and so on. The "**th**" suffix is what marks a fractional place — "one thousand" is far larger than one, while "one thousandth" is far smaller. So a decimal is just a [[Fraction|fraction]] whose denominator is a power of ten, written in positional notation. OpenStax [[Prealgebra]] 2e (Chapter 5, [[prealgebra-2e-ch05-decimals]], §5.1) introduces decimals this way.

The **decimal point** separates the whole-number part (left) from the fractional part (right); the number of digits to the right is the count of **decimal places**. **Equivalent decimals** are decimals that name the same value: writing zeros at the *end* of a decimal does not change its value, because `0.31 = 0.310 = 31/100 = 310/1000`. (Zeros *before* significant digits, like the leading `0.` in `0.024`, are placeholders that *do* matter.)

**Naming a decimal**: name the whole-number part, say "**and**" for the decimal point, name the digits to the right as a whole number, then name the place value of the rightmost digit — so `15.68` is "fifteen **and** sixty-eight **hundredths**." **Writing a decimal from words** reverses this: the word "and" locates the decimal point, the final place-value word tells you how many decimal places to mark, and you fill empty interior positions with **zeros** as placeholders ("twenty-four thousandths" → `0.024`).

To **order** two decimals, give them the same number of decimal places by appending trailing zeros, then compare the digits as whole numbers; for **negative** decimals remember that the value farther to the right on the [[NumberLine|number line]] is greater. Decimals are **rounded** exactly as whole numbers are (see [[Rounding]]): pick a target place, look at the single digit immediately to its right, round up if it is `5` or more, then drop every digit to the right of the target place.

A decimal converts to a [[Fraction|fraction]] by writing the fractional digits as the numerator over the matching power-of-ten denominator (the number of zeros equals the number of decimal places), then simplifying — `0.68 = 68/100 = 17/25`. The reverse direction, and the appearance of **repeating decimals**, are covered in [[DecimalFractionConversion]]. The four operations on decimals are in [[DecimalArithmetic]].

## Connections
- [[PlaceValue]] — decimals extend the base-10 place-value system to the right of the decimal point.
- [[Rounding]] — rounding a decimal uses the same "look one place right" rule, to tenths/hundredths/etc.
- [[Fraction]] — a decimal is a fraction with a power-of-ten denominator; [[DecimalFractionConversion]] moves between the two forms.
- [[DecimalArithmetic]] — adding, subtracting, multiplying, dividing decimals.
- [[DecimalFractionConversion]] — converting decimals ↔ fractions, including repeating decimals.
- [[NumberLine]] — decimals are located and ordered on the number line; negatives follow Ch 3 sign rules.
- [[Integer]] / [[SignedNumberArithmetic]] — decimals can be negative and obey the same sign rules.
- [[prealgebra-2e-ch05-decimals]] — source (Ch 5.1).
