---
title: "Currency (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, numeric-precision, financial-computing]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/Currency
---

## Summary
This task asks the programmer to represent monetary values exactly using a data type suited to dollars-and-cents arithmetic, rather than IEEE 754 binary floating point (which cannot represent values like 2.86 or 0.0765 precisely). The key insight is that money requires exact decimal arithmetic: implementations typically use fixed-point integers (counting cents), arbitrary-precision decimals, or rational numbers. The contrived quantity of four quadrillion hamburgers deliberately overflows 64-bit floats, forcing a non-naive solution.

## Task Requirements
- Represent currency exactly using a data type that captures dollars and cents without floating-point error.
- Model two priced items: 4,000,000,000,000,000 hamburgers at $5.50 each and 2 milkshakes at $2.86 each, with a tax rate of 7.65%.
- Compute and output the total price before tax, the tax, and the total with tax.
- The tax must be computed by rounding to the nearest whole cent, and that rounded value added to the pre-tax total.
- Display dollars and cents with a decimal point; expected results are 22000000000000005.72, 1683000000000000.44, and 23683000000000006.16.
- Dollar signs and thousands separators are optional.

## Language Coverage
65 languages implement this task, spanning systems languages, scripting languages, functional languages, and database/query tools. Representative implementations include C, C++, Rust, Go, Java, C#, Python, Perl, Raku, Haskell, Common Lisp, and even DuckDB and jq.

## Connections
- [[FixedPointArithmetic]] — counting cents as integers to avoid float error
- [[ArbitraryPrecisionArithmetic]] — needed because the totals exceed 64-bit float precision
- [[DecimalArithmetic]] — exact base-10 representation of money values
- [[RoundingModes]] — the tax must be rounded to the nearest whole cent
- [[FloatingPointPrecision]] — the IEEE 754 limitation this task is designed to expose

## Contradictions
- None — reference task page.
