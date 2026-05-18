---
title: "RISC"
type: concept
tags: [computer-architecture, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# RISC

**Reduced Instruction Set Computing**. CPU design philosophy in which the instruction set is small, each instruction is fixed length and simple enough to execute in roughly one clock cycle, and the architecture relies on a large register file and pipelining to keep work moving. Examples: [[AVR]], [[ARMCortexM|ARM]], MIPS, RISC-V.

Per [[embedded-controllers-fiore]] ch. 16:

> "RISC architectures do not use these complex instructions, instead focusing on getting each instruction to execute in a single cycle. These are usually *pipelined* as well, meaning that while one instruction is executed, the next instruction is being loaded from program memory."

Contrast: [[CISC|CISC]] — Complex Instruction Set Computing — fewer, more powerful instructions, multi-cycle, fewer registers (x86's historical lineage).

## Tradeoffs

- **+ Predictable cycle counts** make real-time analysis tractable.
- **+ Pipelining is straightforward** when every instruction is the same length and decoding is fast.
- **+ Larger register file** reduces memory traffic.
- **− Each high-level operation may take more individual instructions** than the CISC equivalent.
- **− Code size can be larger** (mitigated on ARM via Thumb mode).

## Where it sits in the wiki

- [[AVR]] / [[ATmega328P]] — 8-bit RISC. Most instructions in 1 of 16 MHz.
- [[ARMCortexM]] — 32-bit RISC, the modern dominant embedded ISA family.

## Connections

- [[CISC]] — the opposite philosophy.
- [[AVR]] / [[ATmega328P]] / [[ARMCortexM]] — RISC MCU instances.
- [[embedded-controllers-fiore]] — the source.
