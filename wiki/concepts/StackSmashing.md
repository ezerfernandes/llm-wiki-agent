---
title: "Stack Smashing"
type: concept
tags: [security, buffer-overflow, x86-64, stack, exploit-technique]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Stack Smashing

**Stack smashing** is the [[BufferOverflow|buffer-overflow]] exploit technique that corrupts a function's [[StackFrame|stack frame]] — overwriting [[ReturnAddressOverwrite|the saved return address]] — to redirect [[InstructionPointer|`%rip`]] when the function returns via [[RetInstruction|`retq`]]. Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] of [[DiveIntoSystems]], stack smashing is the **canonical exploitation pattern** that takes a [[CLanguage|C]] [[BoundsChecking|bounds-checking]] failure (e.g. `scanf("%s", buf)` writing past a 12-byte buffer) and turns it into attacker-controlled program execution.

## Mechanism

1. **Vulnerable write**. An unbounded write (`gets`, `scanf("%s", ...)`, [[Strcpy|`strcpy`]], `strcat`, [[Sprintf|`sprintf`]]) writes a caller-controlled number of bytes into a fixed-size [[CArray|stack buffer]].
2. **Adjacent memory corruption**. Bytes past the buffer overwrite — in this order, walking up the stack — adjacent local variables, the saved [[FramePointer|`%rbp`]] at `0(%rbp)`, and the **saved return address** at `8(%rbp)`.
3. **Return-address overwrite**. The attacker constructs an input whose tail places a chosen 8-byte address at the saved-return-address slot (little-endian on [[X86_64|x86-64]]).
4. **`retq` redirection**. When the function returns, [[RetInstruction|`retq`]] pops the corrupted address into [[InstructionPointer|`%rip`]] — execution jumps to attacker-chosen code.

## The `secret` worked example (Ch 7.10)

Program with a 12-byte `buf` and an `endGame()` function never called by normal control flow:

- **Normal input** (`1234567890`): ASCII fills `buf` with null termination; program prints "you lose" and exits.
- **Oversized junk input** (43+ chars): program segfaults — return address corrupted to non-code.
- **Crafted exploit input** (48 bytes): 40 bytes of junk padding + 8-byte little-endian address `\xda\x06\x40\x00\x00\x00\x00\x00` (the address of `endGame`, `0x4006da`). After `main`'s `retq`, `%rip` lands on `endGame` and prints *"You win!"*.

The 40-byte padding is **frame-layout-specific**: it equals `buf_size + adjacent_locals + saved_%rbp_slot = 12 + 20 + 8`. Reverse-engineering the exact padding for a real-world target is the bulk of an attacker's work.

## Distinction from related concepts

- **[[BufferOverflow]]** — the broader vulnerability class (any out-of-bounds write past a buffer's capacity, on stack or heap). Stack smashing is the **stack-targeted, return-address-targeted** subspecies.
- **[[HeapOverflow|Heap overflow]]** — the sibling on the [[HeapSection|heap]], typically corrupting [[HeapMetadata|allocator metadata]] rather than a return address.
- **[[ReturnAddressOverwrite]]** — the specific corruption stack smashing performs; stack smashing = (overflow ⇒ return-address-overwrite ⇒ `retq` hijack).
- **[[ReturnOrientedProgramming|ROP]]** — a payload-construction technique often combined with stack smashing when [[ExecutableSpaceProtection|NX]] prevents the simpler shellcode-injection variant. Stack smashing **places the address**; ROP determines **what address(es) to place**.

## Why it works on [[CLanguage|C]] specifically

[[CLanguage|C]] performs **no [[BoundsChecking|array bounds check]]** at write time (per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]]) and the [[X86_64|x86-64]] [[CallingConvention|calling convention]] stores the return address **on the stack, adjacent to local buffers** (per [[dis-7-5-x86-64-functions|Ch 7.5]]). Stack smashing is the structural collision of those two design choices.

## Defenses

The [[BufferOverflow]] page lists the full defense stack. Stack smashing specifically is mitigated by:

- **[[StackCanary|Stack canaries]]** — a guard value between locals and the saved return address detects the contiguous overwrite before `retq`.
- **[[ExecutableSpaceProtection|NX / DEP]]** — prevents the *injected-shellcode* variant; defeated by [[ReturnOrientedProgramming|ROP]].
- **[[AddressSpaceLayoutRandomization|ASLR]]** — randomizes target addresses; defeated by info leaks or brute force.
- **[[BoundsChecking|Bounded library functions]]** — `fgets` / `scanf("%12s")` / [[Strncpy|`strncpy`]] / `strncat` / `snprintf` prevent the overflow in the first place. *"The best line of defense is always the programmer."* ([[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]).
- **[[MemorySafeLanguage|Memory-safe languages]]** ([[Rust]] / [[Go]] / [[Java]] / [[Python]]) make the entire vulnerability class unexpressible.

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 walks the `secret` exploit in detail at the [[X86_64|x86-64]] [[StackFrame|stack-frame]] surface.
