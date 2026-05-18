---
title: "Instruction Pointer (`%rip` / `%eip`)"
type: concept
tags: [cpu, computer-architecture, assembly, low-level, hardware, registers]
sources: [dis-3-5-gdb-assembly]
last_updated: 2026-05-17
---

# Instruction Pointer (`%rip` / `%eip`)

The **instruction pointer** is the [[CpuRegister|CPU register]] that **holds the address of the next instruction to execute**. On x86-64 it is named **`%rip`** (64-bit); on [[IA32|IA-32]] it is **`%eip`** (32-bit). The same role appears under different names in other ISAs (`pc` on ARM / RISC-V) — sometimes called the **program counter** generically.

## Role in [[dis-3-5-gdb-assembly|Ch 3.5]]

Ch 3.5 names `%rip` / `%eip` as the *"you are here"* register at the assembly level — the source-of-truth for *where execution is paused* once you leave [[GDB]]'s source view. Three workflows hinge on it:

- **`x/i $pc`** — [[GdbExamineMemory|examine memory]] in instruction format at the program counter; prints the single next instruction. (Note: [[GDB]] aliases `$pc` to whichever register plays the IP role on the current [[ISA]], so the same `$pc` form works on x86-64, [[IA32|IA-32]], ARM, and RISC-V.)
- **`display/i $pc`** — [[GdbDisplay|register]] the auto-print of the next instruction at every halt — paired with [[GdbStepi|`stepi`]] this gives a live single-step trace.
- **`info registers`** — `%rip` / `%eip` is in the printout; observing it advance by the instruction's byte width across [[GdbStepi|`stepi`]] confirms the step took effect.

## Why it can't be assigned arbitrarily

Unlike most [[CpuRegister|registers]], the IP is not a normal data register — its value **is** the control-flow state of the program. The CPU updates it implicitly after every instruction (by adding the instruction's byte width) and explicitly on `jmp` / `call` / `ret` / `je` / etc. From [[GDB]], you *can* write to it via [[GdbSet|`set $rip = 0x...`]] to jump execution to an arbitrary address — used for advanced debugging (skip a faulting instruction, replay a basic block) but it is a surgical tool that can leave the [[StackFrame|stack]] in a corrupted state.

## Pairs with

- [[CpuRegister]] — the parent category; `%rip` is the special-purpose one.
- [[GdbDisassemble|`disass`]] — the disassembly listing marks `%rip` with `=>`.
- [[GdbStepi|`stepi`]] — advances `%rip` by one instruction.
- [[AssemblyLanguage]] / [[IA32]] — the ISAs whose register naming this page uses.
