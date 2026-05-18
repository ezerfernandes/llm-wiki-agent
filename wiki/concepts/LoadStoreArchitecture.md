---
title: "Load/Store Architecture"
type: concept
tags: [isa, risc, load-store, memory-model, architecture]
sources: [dis-9-1-arm64-basics]
last_updated: 2026-05-17
---

# Load/Store Architecture

A **load/store architecture** is an [[ISA]]-design discipline that **confines memory operands to two dedicated instruction classes** — *load* (memory → register) and *store* (register → memory). Every other instruction class — arithmetic, logic, shift, comparison, branch — operates **exclusively on registers and immediate constants**. Memory is **never** the destination of an arithmetic operation; computation happens in registers.

Per [[dis-9-1-arm64-basics|Ch 9.1]]: *"Data cannot be read or written to memory directly; instead, ARM follows a load/store model, which requires data to be operated on in registers."*

## The two operand-policy regimes

| Regime | Where can memory appear? | Example ISAs | This wiki's page |
|---|---|---|---|
| **Load/store** ([[RISC]]) | Only on `load` / `store` instructions | [[ARM64]], [[RISCV]], MIPS, PowerPC | this page |
| **Register-memory** ([[CISC]]) | On any instruction with a memory operand | [[X86_64]], [[IA32]], x86, VAX | [[Operand]] |

The two regimes are **alternative ISA-design answers** to the question *where can a memory operand appear?* — not bug-vs-feature. Each has structural consequences for instruction count, pipeline depth, encoding density, and compiler complexity.

## Consequences

**More instructions per C operation, smaller per-instruction work.** A C statement like `*p = *p + 2` compiles to:

| ISA | Instruction count | Pattern |
|---|---|---|
| [[X86_64]] | 1 | `addl $0x2, (%rdi)` — single read-modify-write memory operand |
| [[ARM64]] | 3 | `ldr w0, [x0]` → `add w0, w0, #2` → `str w0, [x0]` |

The ARM64 form's three-instruction sequence operationalizes the load/store rule — the read, the add, and the write-back are **three distinct architectural events**, exposed to the compiler / scheduler / pipeline.

**Simpler pipeline + more uniform instruction timing.** Because every instruction is *either* register-only *or* a single memory access (load XOR store), pipeline hazards become simpler to reason about — there is no read-modify-write data hazard internal to a single instruction.

**More registers needed.** Because intermediate values cannot live in memory while computation proceeds, the ISA designer compensates by exposing **more architectural registers** — [[ARM64]]'s **31 GPRs** and [[RISCV]]'s **32** vs [[X86_64]]'s **16** and [[IA32]]'s **8**. See [[AArch64Registers]] for the AArch64 count.

**Fixed-width instruction encoding becomes feasible.** With memory operands and computation never combined, instruction-encoding complexity drops — a single 4-byte fixed-width encoding suffices for [[ARM64]] / [[RISCV]] (vs [[X86_64]]'s 1–15-byte variable encoding).

## Compiler effect — the unoptimized-`adder2` detour

Per [[dis-9-1-arm64-basics|Ch 9.1]]'s `adder2(int a) { return a + 2; }` worked example — the unoptimized compilation emits:

```
str w0, [sp, #12]      ; load/store: store param to stack
ldr w0, [sp, #12]      ; load/store: reload from stack
add w0, w0, #0x2       ; arithmetic: register + immediate, no memory
```

The store-then-reload looks redundant — but it is the **mechanical consequence** of the load/store rule combined with the unoptimized compiler's decision to spill `a` to the stack. The arithmetic operation itself (`add w0, w0, #0x2`) **cannot** read memory directly — so the value must be in a register at the moment of computation. Optimization (`-O1`+) elides the spill.

## What load/store does **not** mean

- It does **not** mean *less expressive*. Every computation expressible on [[X86_64]] is expressible on [[ARM64]] — the difference is **instruction count**, not capability.
- It does **not** mean *slower*. Modern out-of-order ARM cores (Apple Silicon, AWS Graviton, Cortex-A) routinely outperform x86 cores per-watt; the larger register file and uniform timing help.
- It does **not** apply to [[ARMCortexM|Cortex-M]] differently — ARMv7-M and ARMv8-M are also load/store architectures, just at 32-bit instead of 64-bit width.

## Connections

- [[dis-9-1-arm64-basics]] — promoting source.
- [[ARM64]] — the [[ISA]] this discipline defines.
- [[RISC]] — the broader [[ISA]] family that the load/store discipline is a defining feature of.
- [[CISC]] — the contrasting family that permits register-memory and memory-register-memory operands.
- [[X86_64]] — the contrasting [[ISA]] this wiki uses as the CISC reference point.
- [[IA32]] — same.
- [[Operand]] — the operand-type taxonomy; load/store narrows the memory-operand row to two instruction classes.
- [[AArch64Registers]] — the AArch64 register file that absorbs the load/store overhead.
- [[ARM64AddressingMode]] — the memory-operand forms permitted on `ldr` / `str`.
- [[ARMCortexM]] — also a load/store ISA, at 32-bit Cortex-M scope.
- [[ISA]] — the umbrella concept.
