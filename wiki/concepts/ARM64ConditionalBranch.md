---
title: "ARM64 Conditional Branch (b.cond family)"
type: concept
tags: [arm64, armv8, assembly, control-flow, branch, b-cond, conditional-branch]
sources: [dis-9-4-1-arm64-preliminaries, dis-9-4-2-arm64-if-statements, dis-9-4-3-arm64-loops]
last_updated: 2026-05-17
---

# ARM64 Conditional Branch

The **`b.cond` family** is the [[ARM64|AArch64]] **conditional-branch instruction family** — the [[ARM64]] analog of [[X86JumpInstructions|x86 `jXX`]]. Each instruction reads the [[ARM64FlagsRegister|NZCV flags]] and either writes the branch target into `pc` (taken) or lets `pc` advance (not taken). Per [[dis-9-4-1-arm64-preliminaries|Ch 9.4.1 of *[[DiveIntoSystems]]*]] — the control-flow primitive every [[IfStatement|`if`]] / [[WhileLoop|loop]] compiles down to.

## Mnemonic shape

`b.<cond> <label>` — the **condition suffix** is dot-separated from the `b` base mnemonic. **No fall-through suffix forms** (unlike [[X86JumpInstructions|x86]] where `je` / `jz` are aliases) — every conditional branch is one of the canonical suffixes from [[ARM64FlagsRegister|the condition-code table]].

## The full family

| Mnemonic | Meaning | Flag test |
|---|---|---|
| `b.eq` | equal | Z == 1 |
| `b.ne` | not equal | Z == 0 |
| `b.lt` | signed less | N != V |
| `b.le` | signed less-or-equal | Z == 1 OR N != V |
| `b.gt` | signed greater | Z == 0 AND N == V |
| `b.ge` | signed greater-or-equal | N == V |
| `b.lo` / `b.cc` | unsigned lower / carry clear | C == 0 |
| `b.ls` | unsigned lower-or-same | C == 0 OR Z == 1 |
| `b.hi` | unsigned higher | C == 1 AND Z == 0 |
| `b.hs` / `b.cs` | unsigned higher-or-same / carry set | C == 1 |
| `b.mi` | minus / negative | N == 1 |
| `b.pl` | plus / non-negative | N == 0 |
| `b.vs` | overflow set | V == 1 |
| `b.vc` | overflow clear | V == 0 |
| `b.al` | always (semantic alias of `b`) | true |

The **signed/unsigned split** is encoded in the **mnemonic** — `lt`/`le`/`gt`/`ge` consume N + V (signed); `lo`/`ls`/`hi`/`hs` consume C (unsigned). The producing [[ARM64Cmp|`cmp`]] sets all four flags identically; the consumer chooses interpretation. Same convention as [[X86JumpInstructions|x86 `jXX`]]'s `g`/`l` vs `a`/`b` split.

## Range limit

*"Conditional branch instructions have a much more limited range (1 MB) than the `b` instruction."* The 19-bit signed offset encoding caps `b.cond` reach at ±1 MB. For long-distance conditional jumps, the compiler emits a **conditional branch + unconditional `b`** chain:

```
b.eq  1f          // short hop over the long jump
b     far_label   // ±128 MB range via unconditional b
1:
```

The unconditional `b` has a 26-bit signed offset → ±128 MB range. The `cbz` / `cbnz` (compare-and-branch-if-zero / nonzero) and `tbz` / `tbnz` (test-bit-and-branch) instructions have **even tighter ranges** (±32 KB / ±32 KB respectively) but skip the [[ARM64Cmp|`cmp`]] entirely.

## Two compilation contexts

- **Forward branch** ([[dis-9-4-2-arm64-if-statements|Ch 9.4.2]] [[IfStatement|`if`]]-compilation) — `cmp` + `b.cond`-on-negated-condition jumps **over** the `if` body to the `else` arm. The branch is taken when the source condition is **false**.
- **Backward branch** ([[dis-9-4-3-arm64-loops|Ch 9.4.3]] loop-compilation) — `cmp` + `b.cond` jumps **back** to the loop header when the loop condition still holds. Same primitive, opposite control-flow shape.

## Related branch-family instructions

- **`b <label>`** — unconditional branch (no condition suffix), ±128 MB range.
- **`bl <label>`** — branch-and-link (function call), writes return address into `x30` (link register).
- **`br <Xn>`** / **`blr <Xn>`** — indirect (register-target) branch / branch-and-link.
- **`ret`** — return (implicit branch to `x30`).
- **`cbz` / `cbnz <Xn>, <label>`** — compare register against zero and branch, **no [[ARM64Cmp|`cmp`]] needed** and **no [[ARM64FlagsRegister|NZCV]] consumed**.
- **`tbz` / `tbnz <Xn>, #bit, <label>`** — test single bit and branch, also bypasses NZCV.

## Connections

- [[ARM64FlagsRegister]] — supplies the NZCV bits this family consumes.
- [[ARM64Cmp]] — the typical flag-producer paired with `b.cond`.
- [[ARM64ConditionalSelect]] — the branch-free data-flow alternative (`csel`).
- [[X86JumpInstructions]] — the x86 analog (`jXX` family).
- [[BranchInstruction]] — umbrella concept.
- [[ARM64]] / [[InstructionPointer|`pc`]] / [[ControlFlow]] / [[BranchPrediction]] / [[ControlHazard]] — supporting concepts.
- [[dis-9-4-1-arm64-preliminaries]] / [[dis-9-4-2-arm64-if-statements]] / [[dis-9-4-3-arm64-loops]] — sources.
