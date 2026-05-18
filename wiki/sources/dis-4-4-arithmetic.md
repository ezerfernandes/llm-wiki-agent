---
title: "Dive into Systems — Ch 4.4 Binary Integer Arithmetic"
type: source
tags: [systems, binary, arithmetic, hub]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C4-Binary/arithmetic.html
---

## Summary

**Hub page** for Ch 4.4 of *[[DiveIntoSystems]]* — *Binary Integer Arithmetic*. Frames the chapter's central thesis: the same place-value arithmetic algorithms used for decimal numbers transfer directly to [[BinaryNumber|binary]], and — crucially — *"it does not matter to the arithmetic procedures whether we choose to interpret the operands or result as signed or unsigned."* This signed/unsigned **interpretation-invariance** is what lets [[ComputerHardware|hardware]] designers build a single [[ArithmeticLogicUnit|ALU]] adder that serves both [[UnsignedInteger|unsigned]] and [[TwosComplement|two's-complement]] integers — the practical pay-off of [[dis-4-3-signed|Ch 4.3]]'s negative-weight MSB encoding. Body content is delivered by three subsection pages.

## Subsections

- **4.4.1 Addition** — binary column-wise addition with carry.
- **4.4.2 Subtraction** — subtraction reduced to *"flip and add one"* addition via [[TwosComplement|two's complement]].
- **4.4.3 Multiplication & Division** — shift-and-add multiplication; division.

## Key Claims

- Binary arithmetic uses the **same column-by-column algorithms** as decimal arithmetic — only the base changes ($2$ instead of $10$).
- **Signed/unsigned interpretation does not affect the procedure** — the bit-level addition / subtraction / multiplication steps are identical; only the interpretation of the result bits changes.
- This invariance enables **unified hardware** — one [[ArithmeticLogicUnit|ALU]] adder circuit serves both signed and unsigned operands.

## Key Quotes

> "it does not matter to the arithmetic procedures whether we choose to interpret the operands or result as signed or unsigned" — Ch 4.4, the chapter's headline interpretation-invariance principle.

## Connections

- [[DiveIntoSystems]] — host textbook; Ch 4.4 is the **fourth section** of Ch 4 *Binary and Data Representation*.
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — authors.
- [[dis-4-1-bases]] — Ch 4.1, supplies the [[BinaryNumber|binary]] / [[UnsignedInteger|unsigned-integer]] foundation Ch 4.4 operates on.
- [[dis-4-2-conversion]] — Ch 4.2, the conversion-mechanics sibling.
- [[dis-4-3-signed]] — Ch 4.3, supplies the [[TwosComplement|two's-complement]] encoding whose interpretation-invariance Ch 4.4 exploits.
- [[BinaryRepresentation]] — umbrella concept.

## Contradictions

None — Ch 4.4 builds directly on [[dis-4-1-bases|Ch 4.1]] and [[dis-4-3-signed|Ch 4.3]] without conflict.

## What's Deferred

- **Overflow detection** — when the result exceeds the cell width.
- **Worked algorithms** — addition / subtraction / multiplication-and-division details delivered in the 4.4.1 / 4.4.2 / 4.4.3 subsection pages.
