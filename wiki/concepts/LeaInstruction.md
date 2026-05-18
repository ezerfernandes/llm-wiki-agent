---
title: "x86-64 `lea` Instruction (Load Effective Address)"
type: concept
tags: [x86-64, assembly, instruction, address-arithmetic, lea]
sources: [dis-7-3-x86-64-arithmetic]
last_updated: 2026-05-17
---

# `lea` — Load Effective Address

The **`lea S, D` instruction** is [[X86_64|x86-64]]'s **address-arithmetic primitive** per [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — computes the effective address that the [[X86AddressingMode|addressing-mode expression]] `S` would resolve to, and writes that **computed address** into `D`, **without** accessing memory:

```
lea S, D    # D ← &S    (compute the address; no memory read)
```

Promoted from forward reference to first-class concept by [[dis-7-3-x86-64-arithmetic|Ch 7.3]] — [[dis-7-2-x86-64-common|Ch 7.2]] flagged `lea` as deferred.

## The headline semantic distinction from `mov`

The [[X86MovInstruction|`mov`]] / `lea` pair share the same source-operand syntax but differ on **whether the address is dereferenced**:

| Instruction | Reads memory? | Result |
|---|---|---|
| `mov 8(%rax), %rdx` | yes — load 8 bytes at `%rax+8` | `%rdx` ← `*(%rax + 8)` |
| `lea 8(%rax), %rdx` | no — compute the address | `%rdx` ← `%rax + 8` |

Per [[dis-7-3-x86-64-arithmetic|Ch 7.3]]: *"the `lea` instruction performs the same (sometimes complicated) operand arithmetic without the memory lookup."* `mov` is *required* to treat a memory-form source as an address to dereference; `lea` evaluates the same expression purely as arithmetic.

## `lea`'s compiler use is general-purpose arithmetic

Because the [[X86AddressingMode|`disp(base, index, scale)`]] expression evaluates `disp + base + index*scale` in **one instruction**, `lea` is functionally a **three-operand arithmetic instruction**: it can encode `D ← B + I*S + C` in a single fast op — replacing what would otherwise be a sequence of [[X86MovInstruction|`mov`]] + [[X86ArithmeticInstructions|`add`]] + [[X86MulInstruction|`imul`]] (or [[X86ShiftInstructions|`shl`]] for power-of-two scale). With `scale` ∈ {1, 2, 4, 8} that means `lea` can compute `x + y`, `x + 2y`, `x + 4y`, `x + 8y`, `x + constant`, `x*2`, `x*4`, `x*8`, and any disp + base + index*scale combination in a single instruction.

The instruction was designed for address computation (its name — *load effective address* — reflects that), but **compilers use it as a general arithmetic shortcut** whenever the expression fits the `disp + base + index*scale` mold. Reading disassembled x86 code, `lea` between non-pointer-typed registers is almost always doing arithmetic, not addressing.

## Worked examples

From [[dis-7-3-x86-64-arithmetic|Ch 7.3]], assuming initial `%rax = 0x5`, `%rdx = 0x4`, `%rcx = 0x808`:

| Instruction | Expression | Result |
|---|---|---|
| `lea 8(%rax), %rax` | `8 + %rax` | `13` |
| `lea (%rax, %rdx), %rax` | `%rax + %rdx` | `9` |
| `lea (, %rax, 4), %rax` | `%rax * 4` | `20` |
| `lea -0x8(%rcx), %rax` | `%rcx - 8` | `0x800` |
| `lea -0x4(%rcx, %rdx, 2), %rax` | `%rcx + %rdx*2 - 4` | `0x80c` |

The last example — the **full form** — uses every slot of the [[X86AddressingMode|`disp(base, index, scale)`]] template and shows `lea` compressing a four-operation arithmetic computation into one instruction.

## Connections

- [[dis-7-3-x86-64-arithmetic]] — **introducing source** (forward-ref delivered).
- [[dis-7-2-x86-64-common]] — flagged `lea` as deferred.
- [[X86_64]] — the ISA.
- [[X86MovInstruction]] — the **no-memory-access contrast**; `lea` is `mov`-shaped without the dereference.
- [[X86AddressingMode]] — the `disp(base, index, scale)` expression that `lea` evaluates without dereferencing.
- [[X86ArithmeticInstructions]] / [[X86MulInstruction]] / [[X86ShiftInstructions]] — the multi-instruction arithmetic sequences `lea` collapses into one op.
- [[CompilerOptimization]] — `lea`-as-arithmetic-shortcut is one of the canonical compiler-emitted x86 patterns.
- [[CISC]] — `lea`'s ability to encode address arithmetic as one instruction is a CISC-style affordance not present in pure RISC ISAs.
