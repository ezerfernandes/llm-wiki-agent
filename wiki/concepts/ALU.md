---
title: "ALU"
type: concept
tags: [cpu, hardware, computer-architecture]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Arithmetic Logic Unit

CPU sub-unit that performs the actual computation — integer addition / subtraction, bitwise AND/OR/XOR/NOT, shifts, comparisons. The data-path workhorse; the rest of the CPU exists to feed the ALU operands and route its results.

Per [[embedded-controllers-fiore]] ch. 16, on the [[AVR]] core:

> "The ALU performs operations on the values in the registers, not directly on values in general memory. … The ALU has to transfer values from memory to the registers where the computation is performed and then transfer the result back to the final location. A large number of registers is a common feature of [[RISC]] processors. Early [[CISC]] processors had very few registers (indeed, many had a single 'accumulator' for these sorts of operations)."

The ALU's outputs feed the [[StatusRegister|status register]] flag bits (carry, zero, negative, overflow, sign, half-carry) which downstream conditional branch instructions read.

## On the AVR

- 8-bit operations are single-cycle.
- 16-bit operations on `int` / pointer arithmetic happen as two-cycle sequences using carry between ALU passes.
- 32-bit `long` operations chain four passes; doubles are software-emulated with measurable cost.
- No hardware multiply / divide instructions on every variant — 328P has `MUL` (8×8 → 16); divide is always software.

## Connections

- [[StatusRegister]] — the flag-bit output of every ALU operation.
- [[CpuRegister]] — the inputs / outputs of the ALU on a [[RISC]] machine.
- [[AVR]] / [[ATmega328P]] — the host architecture.
- [[embedded-controllers-fiore]] — the source.
