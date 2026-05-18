---
title: "Instruction Set Architecture (ISA)"
type: concept
tags: [isa, architecture, hardware-software-interface, abstraction]
sources: [dis-2-9-7-c-to-assembly]
last_updated: 2026-05-17
---

# Instruction Set Architecture (ISA)

An **ISA** is the **contract between [[ComputerHardware|hardware]] and software** — the set of instructions a [[CPU]] understands, its register file, memory model, addressing modes, and the binary encoding of each instruction. The ISA is the interface every [[CCompiler|compiler]] must target and every [[AssemblyLanguage|assembly language]] is the text form of.

[[dis-2-9-7-c-to-assembly|DIS Ch 2.9.7]] surfaces the ISA implicitly through the `-m32` flag: *"this functionality is supported by any C compiler, and most compilers support compiling to a number of different assembly languages"* — the `.c → .s → .o → executable` workflow is **ISA-agnostic**, but the `.s` artifact is **ISA-specific**.

## Why the ISA matters

- **Source portability vs. binary portability.** [[CLanguage|C]] source compiles to any ISA. [[BinaryExecutable|Binary executables]] target exactly one. Re-compile to retarget.
- **Why operating systems are written in C.** [[dis-2-9-7-c-to-assembly|Ch 2.9.7]]: *"because C is a portable language and is much higher level than assembly languages, the vast majority of operating system code is written in C"* — one C codebase, recompile per ISA.
- **Abstraction boundary.** Above the ISA: user programs, compilers, OS source. Below: microarchitecture (pipelines, caches, branch predictors — implementation details the ISA doesn't expose).

## Major ISAs

| ISA | Bits | Used in | Assembly dialect |
|---|---|---|---|
| [[IA32]] | 32 | Legacy x86 desktops | [[dis-2-9-7-c-to-assembly\|DIS Ch 2.9.7]] examples (`-m32`) |
| [[X86_64\|x86-64 / AMD64]] | 64 | Modern PCs, servers | `gcc` default on Linux/macOS |
| [[ARM\|ARMv7 / AArch64]] | 32 / 64 | Phones, [[RaspberryPi]], Apple Silicon, embedded ([[TheEmbeddedRustBook]]) | [[ARMCortexM\|Cortex-M]] for microcontrollers |
| [[RISCV\|RISC-V]] | 32 / 64 | Open-standard; emerging | `riscv64-gcc` |

## ISA design axes

- **CISC vs. RISC** — variable-length complex instructions ([[IA32]], [[X86_64]]) vs. fixed-length simple ones ([[ARM]], [[RISCV]]). CISC dominates legacy, RISC dominates new designs.
- **Register count** — 8 ([[IA32]]) vs. 16 ([[X86_64]]) vs. 31 ([[ARM|AArch64]], [[RISCV]]).
- **Memory model** — addressing modes, alignment requirements, endianness.

## Connections

- [[dis-2-9-7-c-to-assembly]] — introducing source.
- [[AssemblyLanguage]] — the text representation of an ISA.
- [[IA32]] / [[X86_64]] / [[ARM]] / [[RISCV]] — major ISA instances.
- [[CompilerVsLinker]] — error-stage taxonomy that is ISA-independent.
- [[CLanguage]] — portable across ISAs by design.
- [[ComputerArchitecture]] — the Ch 3 subject; ISA is its hardware-software interface.
- [[ComputerHardware]] — what the ISA contracts with on the hardware side.
