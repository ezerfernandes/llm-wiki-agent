---
title: "Dive into Systems — Ch 4.10 Exercises"
type: source
tags: [book, textbook, dive-into-systems, ch-4, binary-representation, exercises]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/exercises.html
---

## Summary

[[SuzanneJMatthews|Matthews]] / [[TiaNewhall|Newhall]] / [[KevinCWebb|Webb]]'s **Ch 4.10** of *[[DiveIntoSystems]]* — the exercise set that closes Ch 4 *Binary and Data Representation*. Four problems drilling [[NumberBase|number-base]] conversion: (1) `0b01001010` → decimal + hex; (2) `389` → binary + hex; (3) base-5 `1423` → decimal (a non-power-of-2 base, exercising [[PositionalNotation|positional notation]] beyond the $2^k$ family); (4) an *Early Access Interactive Number Conversion* problem set linked to the book's external interactive platform. **Structural sibling of [[dis-1-8-exercises|Ch 1.8]] / [[dis-2-11-exercises|Ch 2.11]]** — the redirect-to-interactive-platform pattern that closes each major chapter. Drills [[dis-4-1-bases|Ch 4.1]]'s base-definitions and [[dis-4-2-conversion|Ch 4.2]]'s four conversion routes ([[BaseConversion|place-value sum]], [[RepeatedDivisionMethod|repeated division]], powers-of-target-base subtraction, [[BinaryHexConversion|per-nibble table lookup]]). No new conceptual material. **47th ingested chapter — fully closes Ch 4 *Binary and Data Representation*.**

## Key Claims

- **Four exercises** drill base-conversion mechanics from [[dis-4-2-conversion|Ch 4.2]].
- **Problem 1** — binary `0b01001010` → decimal `74` and hex `0x4A` (per-nibble lookup: `0100 1010` ↔ `4A`).
- **Problem 2** — decimal `389` → binary `0b110000101` and hex `0x185` ([[RepeatedDivisionMethod|repeated division]] or powers-of-target subtraction).
- **Problem 3** — **base-5** `1423` → decimal `238` ($1 \cdot 5^3 + 4 \cdot 5^2 + 2 \cdot 5^1 + 3 \cdot 5^0 = 125 + 100 + 10 + 3$). The first chapter exercise using a **non-power-of-2 base**, exercising [[PositionalNotation]] in the generic $\sum d_i \cdot B^i$ form rather than the binary-friendly $B = 2^k$ shortcut.
- **Problem 4** — interactive *Number Conversion* problem set on the book's external platform.

## Key Quotes

> "What are the decimal and hexadecimal representations for the value 0b01001010?" — exercise 1
> "What are the binary and hexadecimal representations for the value 389?" — exercise 2

## Connections

- [[DiveIntoSystems]] — Ch 4.10 of the book; **47th ingested chapter**; **fully closes Ch 4 *Binary and Data Representation***.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-1-8-exercises]] / [[dis-2-11-exercises]] — structural siblings (exercises-redirect pattern).
- [[dis-4-9-summary]] — the prose summary that precedes this exercise set.
- [[dis-4-1-bases]] — [[NumberBase|number-base]] definitions exercised here.
- [[dis-4-2-conversion]] — the four [[BaseConversion|conversion routes]] drilled by the exercises.
- [[BinaryHexConversion]] / [[RepeatedDivisionMethod]] / [[PositionalNotation]] — concrete techniques applied.

## Contradictions

None — purely operational drill on [[dis-4-1-bases|Ch 4.1]] / [[dis-4-2-conversion|Ch 4.2]] material.
