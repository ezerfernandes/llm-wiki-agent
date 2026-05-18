---
title: "Data Word"
type: concept
tags: [computer-architecture, von-neumann, memory]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Data Word

A **data word** (or just **word**) is the **natural unit of data** a [[CPU]] manipulates — the size of a single [[CpuRegister|register]], the width of the [[ArithmeticLogicUnit|ALU]] data path, and (typically) the width of the [[DataBus|data bus]]. Per [[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]], *"each register stores one data word."*

Word size is the headline architectural parameter — *"32-bit"* and *"64-bit"* architectures take their names from their word size.

## Common word sizes

- **8-bit** — early micros (Intel 8080, 6502, Z80) and modern microcontrollers (AVR, [[ARMCortexM|some Cortex-M]] variants).
- **16-bit** — 8086, PDP-11.
- **32-bit** — i386 / [[IA32]] / ARMv7 / RISC-V32.
- **64-bit** — [[X86_64|x86-64]] / AArch64 / RISC-V64 — universal on contemporary general-purpose CPUs.

## Connections

- [[CpuRegister]] — each register stores one word.
- [[DataBus]] — typically word-width.
- [[ArithmeticLogicUnit]] — operates on word-sized operands.
- [[ByteAddressable]] — addressing granularity is *byte*, even when the word is wider (multi-byte words occupy contiguous addresses).
- [[ByteOrder]] — how the bytes of a word map to addresses (endianness).
- [[VonNeumannArchitecture]] — the architecture this unit lives in.
- [[dis-5-2-von-neumann]] — source.
