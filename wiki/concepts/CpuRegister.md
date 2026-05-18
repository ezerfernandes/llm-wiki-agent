---
title: "CPU Register"
type: concept
tags: [cpu, computer-architecture, assembly, low-level, hardware, storage-circuit]
sources: [dis-3-5-gdb-assembly, dis-5-2-von-neumann, dis-5-4-3-storage-circuits]
last_updated: 2026-05-17
---

# CPU Register

A **CPU register** is a small, fixed-size storage location **inside the [[CPU]]** that holds an operand, address, or status flag for the currently executing instruction. Registers are the **fastest** tier of the [[MemoryHierarchy|memory hierarchy]] — accessed in a single cycle, with no memory address — and every [[AssemblyLanguage|machine instruction]] reads or writes them.

## Gate-level construction ([[dis-5-4-3-storage-circuits|Ch 5.4.3]])

An N-bit register is **N parallel [[DLatch|gated D latches]] sharing one [[WriteEnable|`WE`]] wire**. The canonical example: a 32-bit register stacks 32 D-latches; bit `i` of the input word drives latch `i`'s `D` input; the single `WE` wire fans out to every latch's write-enable; the latches' `Q` outputs jointly present the stored 32-bit value. Each D latch is itself an [[SRLatch|RS latch]] (two cross-coupled [[NandGate|NAND]] gates with feedback) wrapped in a [[WriteEnable|WE]]-gated front-end that prevents the RS latch's forbidden input combination. The cells are **[[SRAM]]-style** — circuit-based, fast, more expensive than the capacitor-based [[DRAM]] used for main [[RAM|memory]]. The K-register file is built by adding a [[Decoder|decoder]] on register-address bits to gate the right register's `WE` and a [[Multiplexer|MUX]] to select which register's outputs to read — see [[RegisterFile]].

## Architectural role ([[dis-5-2-von-neumann|Ch 5.2]])

In the [[VonNeumannArchitecture|von Neumann architecture]] registers form **half of the [[ProcessingUnit|processing unit]]** (the other half being the [[ArithmeticLogicUnit|ALU]]). Per Ch 5.2: *"each register stores one [[DataWord|data word]]"* and — crucially — *"there is no distinction between instructions and data in the von Neumann architecture"*, so registers can hold either bit pattern. The [[ControlUnit|control unit]] additionally owns two special registers not in the general file: the [[ProgramCounter|program counter (PC)]] (next-instruction address) and the [[InstructionRegister|instruction register (IR)]] (current decoding instruction).

## Scope in [[dis-3-5-gdb-assembly|Ch 3.5]]

The chapter names registers only insofar as they become **visible to the [[Debugger|debugger]]**:

- **`info registers`** — the [[GdbInfo|`info`]] sub-command that prints the entire register file: `%rax` / `%rbx` / `%rcx` / `%rdx` / `%rsi` / `%rdi` / `%rbp` / `%rsp` / `%rip` plus `%eflags` on x86-64; the [[IA32|IA-32]] equivalents (`%eax` / `%ebp` / `%esp` / `%eip`) on 32-bit builds.
- **`print $rax`** — [[GdbPrint|`print`]] with a `$`-prefixed register name reads a single register. Works with any register name in the target [[ISA]].
- **`display $rax`** — [[GdbDisplay|`display`]] auto-prints the register at every halt — the canonical pairing with [[GdbStepi|`stepi`]] for watching a value evolve across instructions.
- **`set $rax = 0`** — [[GdbSet|`set`]] writes through to a register as if it were any other [[LValue|lvalue]] — the runtime override primitive.

## Why the `$` prefix

In [[GDB]] expression syntax, `$name` is a **debugger variable** — either a built-in CPU register (`$rax`, `$rip`) or a user-defined convenience variable (`set $i = 0`, then `print $i`). The prefix disambiguates registers from C-program identifiers: `print rax` looks up a variable named `rax` in the debuggee's scope (usually not found), while `print $rax` reads the CPU register.

## Notable special-purpose registers

- **[[InstructionPointer|`%rip` / `%eip`]]** — instruction pointer; holds the address of the next instruction to execute.
- **`%rsp`** — stack pointer; tip of the [[StackSection|stack]] / current [[StackFrame|frame]].
- **`%rbp`** — base pointer; bottom of the current [[StackFrame|frame]] (when frame pointers are enabled).
- **`%eflags`** — condition-code register; carries the comparison flags that `je` / `jl` / `jg` branch on.

## Pairs with

- [[GdbDisassemble|`disass`]] — the code that *uses* the registers.
- [[GdbStepi|`stepi`]] — single-step to see register changes one instruction at a time.
- [[AssemblyLanguage]] / [[IA32]] — the ISA whose register names you are typing.
- [[CPU]] — the hardware the registers live in.
- [[RegisterSpill]] — what happens when the compiler runs out of registers.
- [[StorageCircuit]] — the gate-level category registers belong to.
- [[DLatch]] / [[SRLatch]] — the 1-bit primitive registers are built from ([[dis-5-4-3-storage-circuits|Ch 5.4.3]]).
- [[WriteEnable]] — the single control input gating the whole register.
- [[RegisterFile]] — the K-register array; registers + [[Decoder|decoder]] + [[Multiplexer|MUX]].
- [[SRAM]] — register cells are SRAM-class storage.
