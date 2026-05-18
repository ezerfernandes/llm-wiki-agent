---
title: "Transistor"
type: concept
tags: [computer-architecture, digital-circuits, hardware, electronics]
sources: [dis-5-3-gates]
last_updated: 2026-05-17
---

# Transistor

A **transistor** is a semiconductor device that acts as a **voltage-controlled switch** regulating electrical flow — *"a transistor can switch its state between on or off (between a high or low voltage output)"* ([[dis-5-3-gates|DIS Ch 5.3]]). It is the physical primitive beneath every [[LogicGate|logic gate]] and therefore beneath every [[CPU]], [[RAM|memory]] cell, and [[ArithmeticLogicUnit|ALU]] in a modern computer.

## Why it matters

- A handful of transistors arranged in a specific pattern realizes one [[LogicGate|logic gate]] (e.g. a CMOS NAND uses 4 transistors; a CMOS inverter uses 2).
- Modern CPUs pack **billions** of transistors on a die — e.g. Apple's M-series and high-end Intel/AMD parts cross $10^{10}$ transistors as of the mid-2020s.
- **[[MoorseLaw|Moore's Law]]** historically described the roughly-2-year doubling of transistor density that drove the entire compute scaling story from the 1970s through the 2010s.

## In context

[[dis-5-3-gates|DIS Ch 5.3]] introduces the transistor only at the *"switch with on/off states"* level — it does **not** distinguish bipolar vs. MOSFET vs. CMOS, nor cover physical-design topics like threshold voltage, sub-threshold leakage, or process node scaling. Those belong to a VLSI / device-physics course downstream.

## Connections

- [[LogicGate]] — the abstraction one level above transistors; gates are built *from* transistors.
- [[ArithmeticLogicUnit]] — built from gates built from transistors.
- [[CPU]] — billions of transistors arranged into gates arranged into the [[VonNeumannArchitecture|von Neumann]] units.
- [[dis-5-3-gates]] — introducing source.
