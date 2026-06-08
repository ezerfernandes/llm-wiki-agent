---
title: "UPC (Rosetta Code)"
type: source
tags: [rosetta-code, programming-task, string-processing, encoding, checksum]
date: 2026-05-30
source_file: https://rosettacode.org/wiki/UPC
---

## Summary
The task asks the programmer to decode UPC-A bar codes that an imaginary reader has rendered as ASCII rows of spaces and `#` characters (ink absence/presence). Each of the ten sample rows must be parsed into its 12 decimal digits and validated; rows that fail must be rejected, and the key insight is that some rows are scanned upside down (and must be reversed) while one row has a timing error that the checksum should catch.

## Task Requirements
- Parse each ASCII row into bit groups: a leading run of spaces, a `# #` start guard, six left-hand digits, a `# #` middle guard, six right-hand digits, and a `# #` end guard.
- Decode digits using the fixed 7-bit-per-digit table, where the right-hand side encoding is the logical negation of the left-hand side.
- Verify each result with the checksum: multiply the 12 digits by weights (3,1,3,1,3,1,3,1,3,1,3,1), sum the products, and require the sum mod 10 to be 0.
- Reject the row that has a timing error.
- Extra credit: detect and correctly decode rows entered upside down (by reversing them) rather than rejecting them.

## Language Coverage
38 languages implement this task, spanning systems, scripting, and functional styles. Representative implementations include C, C++, Rust, Go, Java, Python, Perl, Raku, Julia, Factor, and REXX.

## Connections
- [[BarcodeEncoding]] — UPC-A is the encoding scheme being decoded
- [[ChecksumValidation]] — weighted mod-10 digit check rejects errors
- [[StringParsing]] — fixed-width bit-group segmentation of each row
- [[ModularArithmetic]] — the mod-10 verification rule

## Contradictions
- None — reference task page.
