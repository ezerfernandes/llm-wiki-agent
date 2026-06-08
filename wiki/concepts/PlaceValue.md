---
title: "Place Value"
type: concept
tags: [math, prealgebra, arithmetic, number-systems]
sources: [prealgebra-2e-ch01-whole-numbers]
last_updated: 2026-06-07
---

# Place Value

**Place value** is the rule that the value of a **digit** depends on its **position** within a number. The numbers 537 and 735 use the same three digits, but they mean different amounts because the digits sit in different positions. In our decimal system each position is worth **ten times** the position immediately to its right: reading right to left, the places are ones, tens, hundreds, thousands, ten-thousands, hundred-thousands, millions, and so on. This is exactly the base-10 case of a general positional system — see [[NumberBase]].

Places are grouped into **periods** of three: the ones period, the thousands period, the millions period, the billions period, the trillions period, and onward. In a written number, **commas** separate the periods, which is what makes a long number like 37,519,248 readable. Each period has its own internal hundreds–tens–ones structure, which is why naming and writing big numbers reduces to handling one three-digit period at a time.

**Naming a whole number in words**: start at the leftmost period, name the three-digit number in each period followed by the period's name (million, thousand, …), separate the periods with commas, omit the word "ones" for the last period, and do not use the word "and." For example, 37,519,248 reads "thirty-seven million, five hundred nineteen thousand, two hundred forty-eight."

**Writing a whole number from words**: identify the period words to know how many periods there are, lay out three blanks for each period (the leftmost period may have fewer), place each named digit in its correct slot, and fill any empty interior positions with **zeros** as placeholders. Zero is essential here — it holds an empty place so the other digits keep their correct value.

Place value is the foundation for every standard arithmetic algorithm: [[WholeNumberArithmetic|adding, subtracting, multiplying, and dividing]] whole numbers all work by lining numbers up "by place value" and carrying or borrowing between adjacent places, and [[Rounding]] works by choosing a target place and discarding everything to its right.

## Connections
- [[WholeNumbers]] — the numbers whose values place value defines.
- [[NumberBase]] — the general positional system; decimal place value is its base-10 instance.
- [[Rounding]] — chooses a place and zeroes out everything to the right of it.
- [[Decimal]] — extends place value to the right of the decimal point (tenths, hundredths, …) in Ch 5.
- [[WholeNumberArithmetic]] — column algorithms that align numbers by place value.
- [[prealgebra-2e-ch01-whole-numbers]] — source.
