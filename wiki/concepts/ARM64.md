---
title: "ARM64 (ARMv8-A AArch64)"
type: concept
tags: [isa, arm64, arm, aarch64, armv8, risc, load-store, 64-bit]
sources: [dis-9-1-arm64-basics]
last_updated: 2026-05-17
---

# ARM64

**ARM64** — also known as **AArch64** (the **64-bit execution state** of the [[ARMv8]] architecture) — is the **64-bit [[RISC]] [[ISA]]** developed by Arm Holdings and used by Apple Silicon, modern Android phones, AWS Graviton, and the [[RaspberryPi|Raspberry Pi]] 3+. It is the third [[ISA]] in [[DiveIntoSystems]]' Part III assembly tour, after [[X86_64|x86-64]] (Ch 7) and [[IA32]] (Ch 8) — and unlike the Ch 7 → Ch 8 transition, the move from x86 to ARM64 is **not** a structural mirror but a jump to a **fundamentally different instruction model**.

## ISA characteristics

Per [[dis-9-1-arm64-basics|Ch 9.1]]:

- **[[RISC]] instruction model** — fixed-width 4-byte instruction encoding, large uniform register file, regular instruction format.
- **[[LoadStoreArchitecture|Load/store architecture]]** — *"Data cannot be read or written to memory directly; instead, ARM follows a load/store model, which requires data to be operated on in registers."* Memory operands appear **only** on the `ldr` (load) and `str` (store) instructions; every other instruction class (arithmetic, logic, shift, comparison, branch) takes **registers or immediates only**.
- **31 general-purpose 64-bit registers** — `x0`–`x30`. See [[AArch64Registers]] for the full register-set page.
- **32-bit component aliases** — `w0`–`w30` are the **low 32 bits** of `x0`–`x30`. *"If 32-bit data is stored in component register `w0`, then the upper 32 bits of the register become inaccessible, and are zeroed out."*
- **Three architectural special-purpose registers** — `sp` ([[StackPointer|stack pointer]]), `pc` (program counter — read-only at user-mode), `zr` (zero register — permanently 0; reads return 0; writes are discarded).
- **Destination-first operand order** — `opcode D, O1, O2`. Mirrors [[IntelSyntax|Intel syntax]] order, not [[AtAndTSyntax|AT&T order]]. But ARM64 syntax is **not** Intel syntax — it uses bare register names (no `%` prefix), `#` for immediates, brackets for memory.
- **No suffix-on-mnemonic sizing** — the register width (`xN` vs `wN`) determines the operand size; the instruction mnemonic is invariant. Contrast [[OperandSize|`b`/`w`/`l`/`q` AT&T suffixes]] on [[X86_64|x86-64]] / [[IA32]].

## Operand types

Per [[dis-9-1-arm64-basics|Ch 9.1]], operands are one of three types — same taxonomy as [[Operand|the x86 operand taxonomy]], with [[ARM64]]-specific decoration:

| Type | Form | Example |
|---|---|---|
| **Register** | bare name | `x0`, `w0`, `sp` |
| **Immediate** | `#` prefix | `#0x2`, `#12` |
| **Memory** | brackets | `[sp, #12]`, `[x0, x1]`, `[x0, x2, LSL, #2]` |

See [[ARM64AddressingMode]] for the four memory-operand forms.

## Worked example — `adder2`

The canonical [[DiveIntoSystems|DiveIntoSystems]] cross-ISA worked example — the same `adder2(int a) { return a + 2; }` that appears in [[dis-7-1-x86-64-basics|Ch 7.1]] and [[dis-8-1-ia32-basics|Ch 8.1]] — compiles to **three instructions** on ARM64 (unoptimized):

```
str w0, [sp, #12]      ; store parameter a to stack slot
ldr w0, [sp, #12]      ; reload from stack slot
add w0, w0, #0x2       ; add immediate 2
```

The visible inefficiency (store-then-immediately-reload) is the **unoptimized compiler's load/store reflex** — without `-O1` the compiler does not keep `a` in `w0` across statement boundaries. Per Ch 9.1: *"three instructions required to perform what is a single C operation"*.

## Headline deltas from x86-family

| Dimension | [[X86_64\|x86-64]] (Ch 7.1) | [[IA32]] (Ch 8.1) | [[ARM64]] (Ch 9.1) |
|---|---|---|---|
| ISA family | [[CISC]] | [[CISC]] | [[RISC]] |
| GPR count | 16 | 8 | **31** |
| GPR width | 64-bit | 32-bit | 64-bit |
| Subregister scheme | `%rax` / `%eax` / `%ax` / `%al`/`%ah` + `%r8d`-style suffix | letter-substitution only | **`xN` / `wN` two-width only** |
| Memory operand on `add` | yes | yes | **no — load/store** |
| Instruction width | variable (1–15 bytes) | variable | **fixed 4 bytes** |
| Operand order | source-first (AT&T) | source-first (AT&T) | **destination-first** |
| Register prefix | `%` | `%` | **none** |
| Immediate prefix | `$` | `$` | **`#`** |
| Size suffix on mnemonic | `b`/`w`/`l`/`q` | `b`/`w`/`l` | **none** (encoded in register width) |
| Scaled-index addressing | `disp(base, index, scale)` with `scale ∈ {1,2,4,8}` | same | **`[xN, xM, LSL, #s]`** — explicit shift mnemonic + bit count |

## Connections

- [[dis-9-1-arm64-basics]] — promoting source; Ch 9.1 of [[DiveIntoSystems]].
- [[ARMv8]] — the architecture revision; ARM64 / AArch64 is its 64-bit execution state.
- [[AArch64Registers]] — the register-set page.
- [[LoadStoreArchitecture]] — the ISA-philosophy page.
- [[ARM64AddressingMode]] — the memory-operand form page.
- [[RISC]] — the [[ISA]] family.
- [[ISA]] — the umbrella concept.
- [[X86_64]] — the contrasting CISC ISA at the same chapter position (Ch 7.1).
- [[IA32]] — the contrasting 32-bit CISC ISA at the same chapter position (Ch 8.1).
- [[AssemblyLanguage]] — the umbrella concept.
- [[GeneralPurposeRegister]] — the umbrella; ARM64 contributes the 31-GPR row.
- [[Operand]] — the operand-type taxonomy reused.
- [[ARMCortexM]] — the **microcontroller-scope** ARM cousin; Cortex-M implements ARMv7-M / ARMv8-M (32-bit), **not** ARM64. Distinct ISA family despite the shared "ARM" name.
- [[ARM]] — the broader umbrella covering both 32-bit ARM (ARMv7-A) and 64-bit ARM (ARMv8-A AArch64).
