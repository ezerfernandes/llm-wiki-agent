---
title: "Whole Number Arithmetic"
type: concept
tags: [math, prealgebra, arithmetic]
sources: [prealgebra-2e-ch01-whole-numbers]
last_updated: 2026-06-07
---

# Whole Number Arithmetic

**Whole number arithmetic** is the four basic operations — addition, subtraction, multiplication, and division — performed on the [[WholeNumbers|whole numbers]]. Each operation has its own vocabulary, a set of named properties, and a standard pencil-and-paper algorithm that works by lining the numbers up according to [[PlaceValue|place value]] and processing one column at a time, right to left.

## Addition
Adding combines **addends** to produce a **sum** (written a + b). Two named properties:

- **Identity Property of Addition**: a + 0 = a — adding 0 changes nothing, so 0 is the additive identity.
- **Commutative Property of Addition**: a + b = b + a — the order of the addends does not matter.

**Algorithm (carrying / regrouping)**: write the numbers vertically aligned by place, add each column starting from the ones, and when a column total exceeds 9, **carry** the extra ten into the next column to the left. The same procedure adds three or more numbers. A common application is **perimeter**, the distance around a figure, found by adding all of its side lengths.

## Subtraction
Subtracting takes one number from another to find the **difference**. In a − b, a is the **minuend** and b is the **subtrahend**. Subtraction is the **inverse of addition**, which gives the standard check: if a − b = c, then c + b should equal a.

**Algorithm (borrowing / regrouping)**: align by place, subtract each column from the ones place up, and when the top digit is smaller than the one below it, **borrow** one unit from the next-left place (turning it into ten units in the current place). Always check by adding the difference back to the subtrahend.

## Multiplication
Multiplying combines **factors** into a **product**. It can be written with a times sign (a × b), a dot (a · b), or parentheses (a(b)). Three named properties:

- **Multiplication Property of Zero**: a · 0 = 0 — any number times zero is zero.
- **Identity Property of Multiplication**: a · 1 = a — multiplying by 1 changes nothing.
- **Commutative Property of Multiplication**: a · b = b · a — order of the factors does not matter.

**Algorithm (partial products)**: align by place, multiply the top number by each digit of the bottom factor (carrying when a product exceeds 9), shift each successive partial product one place to the left (using a zero placeholder for each higher position), then add all the partial products. A standard application is **area** of a rectangle, length × width.

## Division
Dividing splits a **dividend** by a **divisor** to get a **quotient**, sometimes with a leftover **remainder**. It is written a ÷ b, a/b, or in long-division form b)a, and is conceptually **repeated subtraction**. Division is the **inverse of multiplication**, so the check is (quotient × divisor) + remainder = dividend. Named properties:

- **Properties of One**: a ÷ a = 1 (any nonzero number divided by itself) and a ÷ 1 = a.
- **Properties of Zero**: 0 ÷ a = 0, but **a ÷ 0 is undefined** — you can never divide by zero.

**Algorithm (long division)**: divide the leading digit(s) of the dividend by the divisor, write each quotient digit above the dividend, multiply it by the divisor and subtract, bring down the next digit, and repeat until no digits remain; then check by multiplying the quotient by the divisor (plus any remainder). Whether a division comes out even is governed by [[Divisibility]].

## Translating word problems
Each operation has signal words: *plus / sum of / increased by / more than / total* (add); *minus / difference of / decreased by / less than / subtracted from* (subtract); *product of / times / twice* (multiply); *divided by / quotient of / divided into* (divide). The general strategy is to identify what is asked, write a word phrase, translate it to an expression, simplify, and answer in a complete sentence.

## Connections
- [[WholeNumbers]] — the numbers these operations act on.
- [[PlaceValue]] — every column algorithm aligns numbers by place value.
- [[Rounding]] — used to estimate and sanity-check results.
- [[Divisibility]] — when a division has no remainder.
- [[IntegerDivision]] — the related integer-quotient operation in computing.
- [[prealgebra-2e-ch01-whole-numbers]] — source.
