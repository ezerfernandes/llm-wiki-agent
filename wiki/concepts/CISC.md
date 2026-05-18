---
title: "CISC"
type: concept
tags: [computer-architecture, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# CISC

**Complex Instruction Set Computing**. CPU design philosophy in which the instruction set is large and each instruction may do significant work in one mnemonic (memory-to-memory operations, string copies, complex addressing modes) at the cost of multi-cycle execution and harder pipelining. Historical examples: VAX, original x86, Motorola 68000.

Per [[embedded-controllers-fiore]] ch. 16:

> "A CISC processor contains instructions that might offer several low-level steps rolled into one. While this sounds very convenient, the down side is that these instructions often take several clock cycles to execute. … Early CISC processors had very few registers (indeed, many had a single 'accumulator' for these sorts of operations)."

Modern x86 is internally a [[RISC]] microarchitecture wrapped in a CISC instruction-set front-end; the µops the CPU actually executes are RISC-like even though the externally visible ISA is CISC. The CISC/RISC distinction is therefore largely academic at the high end, but stays sharp at the MCU end where [[AVR]] (RISC) and the legacy 8051 / Z80 / 6809 (CISC) sit on different sides.

## Connections

- [[RISC]] — the opposite philosophy.
- [[embedded-controllers-fiore]] — the source.
