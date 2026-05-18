---
title: "Return-Oriented Programming (ROP)"
type: concept
tags: [security, buffer-overflow, exploit-technique, post-nx, gadget-chaining]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Return-Oriented Programming (ROP)

**Return-oriented programming (ROP)** is the [[StackSmashing|stack-smashing]] exploitation technique that **chains pre-existing executable instruction sequences** (*gadgets*) — each ending in [[RetInstruction|`retq`]] — to build arbitrary computation **without injecting any new code**. Because no attacker-supplied bytes ever execute, ROP **defeats [[ExecutableSpaceProtection|non-executable-stack / NX / DEP]] mitigations entirely**.

Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] of [[DiveIntoSystems]]: ROP is *"a technique cherry-picking instructions across executable regions."*

## The gadget chain

A **gadget** is a short instruction sequence in already-executable memory (the program's `.text`, libc, or any loaded shared library) ending in [[RetInstruction|`retq`]]. Examples:

```
pop %rdi ; ret           # set %rdi (first argument register)
pop %rsi ; ret           # set %rsi (second argument register)
xor %rax, %rax ; ret     # zero %rax
mov (%rdi), %rax ; ret   # load memory
```

The attacker:

1. **Overflows** a stack buffer until they reach the saved return address.
2. **Writes a list of gadget addresses** starting at the return-address slot (and continuing up the stack — each subsequent `retq` will pop the next).
3. **Triggers the first [[RetInstruction|`retq`]]** by returning from the vulnerable function.

Each gadget executes its 1–3 instructions, then `retq` pops the *next* gadget address from the stack. The stack itself becomes the "program" — a list of *what address to execute next* — and the gadgets form an opcode set built entirely out of bytes that were already executable.

## Why ROP defeats NX

[[ExecutableSpaceProtection|NX]] only prevents execution of *non-executable* pages. Every gadget address lives in `.text` / libc / a shared library — pages the [[OperatingSystem|OS]] has marked **executable** for legitimate reasons. NX has no way to distinguish "the program intended to execute this instruction" from "an attacker chained into this instruction." ROP's payload is a list of *addresses*, not *instructions*; the addresses are stack data, which is allowed to be on a non-executable page.

## Turing-completeness

For any moderately large code base (libc alone is ~2 MB of executable code), an attacker can find enough gadgets to perform arbitrary computation — load constants, do arithmetic, branch, call functions. ROP is **Turing-complete** in practice on any normal Linux binary. The 2007 paper by Shacham (*"The Geometry of Innocent Flesh on the Bone"*) demonstrated this constructively.

## Variants

- **Return-to-libc** (predecessor) — single-target ROP: return into one libc function (e.g., `system("/bin/sh")`). Much simpler; predates the gadget-chain generalization.
- **Jump-Oriented Programming (JOP)** — uses indirect-jump gadgets (`jmp *%rax`) instead of `retq` gadgets. Defeats some ROP-specific defenses.
- **Call-Oriented Programming (COP)** — uses indirect-call gadgets.
- **Sigreturn-Oriented Programming (SROP)** — abuses the `sigreturn` syscall to load arbitrary register state in one step.

## Bypassed by

ROP is defeated (or made much harder) by:

- **[[AddressSpaceLayoutRandomization|ASLR]]** — gadget addresses are randomized; attacker needs an info leak first.
- **[[ControlFlowIntegrity|Control-Flow Integrity (CFI)]]** — runtime checks that every indirect transfer (including `retq`) lands at a valid target. ROP gadgets are typically mid-instruction or non-call-target — CFI catches the mismatch.
- **Shadow stacks** (Intel CET, AArch64 PAC) — hardware-maintained out-of-band copy of return addresses; `retq` cross-checks against the shadow stack. If they disagree, fault.
- **Pointer Authentication** ([[ARM|ARMv8.3-A PAC]]) — return addresses are cryptographically signed before pushing, verified before popping. Forged addresses fail verification.
- **Gadget elimination via compiler** — recent LLVM/GCC passes attempt to remove or relocate `retq` instructions to reduce the gadget surface.

## Historical significance

ROP marks the **collapse of the "make data non-executable" defense strategy**. Pre-ROP, the security community treated NX as a near-complete fix for [[StackSmashing|stack-smashing]] code injection. Shacham's 2007 paper showed the problem can't be solved by data/code separation alone — *what gets executed* matters as much as *whether data can execute*. This pivoted the defense conversation toward [[ControlFlowIntegrity|CFI]], shadow stacks, and pointer authentication — defenses that constrain *which* code can be reached from *where*.

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 introduces ROP as the bypass for [[ExecutableSpaceProtection|NX]] and names it as a *"technique cherry-picking instructions across executable regions."*
