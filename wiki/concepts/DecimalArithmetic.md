---
title: "Decimal Arithmetic"
type: concept
tags: [math, prealgebra, arithmetic, decimals]
sources: [prealgebra-2e-ch05-decimals]
last_updated: 2026-06-07
---

# Decimal Arithmetic

**Decimal arithmetic** is the four operations applied to [[Decimal|decimals]]. Once the position of the decimal point is handled, each operation reduces to the corresponding [[WholeNumberArithmetic|whole-number algorithm]]; the only new work is deciding *where the decimal point goes* in the answer. Signs follow the same [[SignedNumberArithmetic|rules as for integers]]. OpenStax [[Prealgebra]] 2e (Chapter 5, [[prealgebra-2e-ch05-decimals]], §5.2) develops these procedures.

## Addition and subtraction
**Line the decimal points up vertically**, padding with trailing zeros so the columns match, then add or subtract as whole numbers and bring the decimal point straight down into the answer (it stays under the aligned points). Aligning the points is exactly aligning by [[PlaceValue|place value]] — tenths under tenths, hundredths under hundredths.

## Multiplication
You do **not** line up the decimal points. Instead:
1. Determine the sign of the product (same signs → positive, different signs → negative).
2. Multiply the numbers as if they were whole numbers, ignoring the decimal points.
3. **Place the decimal point so that the number of decimal places in the product equals the *sum* of the decimal places in the two factors.** (e.g. `0.03 × 0.045`: 2 + 3 = 5 decimal places → `0.00135`.) Insert leading zeros as placeholders if the product needs more digits than the multiplication produced.

**Multiplying by a power of 10** is a shortcut: move the decimal point to the **right** by the number of zeros in the power of ten (×10 → 1 place, ×100 → 2 places, ×1,000 → 3 places), appending zeros at the end as needed.

## Division
1. Determine the sign of the quotient.
2. **Make the divisor a whole number** by moving its decimal point all the way to the right; move the dividend's decimal point the *same* number of places (this multiplies both by the same power of ten, leaving the quotient unchanged).
3. Divide as in long division, placing the decimal point in the **quotient directly above** the (moved) decimal point in the dividend.

Dividing a decimal by a *whole number* is the same procedure with no shift needed. Money answers are typically **rounded to the nearest cent** (hundredths). The mirror shortcut of the multiplication one — **dividing by a power of 10 moves the decimal point left** — gives the same number of places as zeros.

## Applications
The chapter's general application strategy: identify what to find, write a phrase for it, translate to a numeric expression, simplify, and answer in a complete sentence. Worked types include making change, splitting a bill, hourly wages, fuel purchases, and grocery totals.

## Connections
- [[Decimal]] — the numbers these operations act on; place value underlies decimal-point alignment.
- [[WholeNumberArithmetic]] — each decimal operation reduces to the whole-number algorithm plus decimal-point placement.
- [[PlaceValue]] — aligning decimal points = aligning by place value; powers-of-ten shortcuts are place-value shifts.
- [[SignedNumberArithmetic]] — sign of a product/quotient follows the integer rules.
- [[Rounding]] — division results (especially money) are rounded to a chosen place.
- [[OrderOfOperations]] — multi-operation decimal expressions follow the standard order.
- [[DecimalFractionConversion]] — mixed decimal/fraction expressions convert to one form first.
- [[prealgebra-2e-ch05-decimals]] — source (Ch 5.2).
