---
title: "Return Address Overwrite"
type: concept
tags: [security, buffer-overflow, x86-64, stack, exploit-primitive]
sources: [dis-7-10-x86-64-buffer-overflow]
last_updated: 2026-05-17
---

# Return Address Overwrite

**Return address overwrite** is the [[StackSmashing|stack-smashing]] exploit *primitive*: the moment a [[BufferOverflow|buffer overflow]] writes past adjacent stack data and **replaces the saved return address** in the current [[StackFrame|stack frame]] with attacker-controlled bytes. When the function returns via [[RetInstruction|`retq`]], [[InstructionPointer|`%rip`]] is set to those bytes — the attacker now controls execution.

## Where the return address lives on [[X86_64|x86-64]]

Per [[dis-7-5-x86-64-functions|Ch 7.5]] of [[DiveIntoSystems]], the [[X86_64|x86-64]] [[CallingConvention|System V calling convention]] places the saved return address at **`8(%rbp)`** — one 8-byte slot above the saved [[FramePointer|`%rbp`]]. The standard prologue (`push %rbp; mov %rsp, %rbp`) and epilogue ([[LeaveInstruction|`leaveq`]] + [[RetInstruction|`retq`]]) make this slot the **only stack location whose value [[RetInstruction|`retq`]] reads** — therefore the **only target an attacker needs to corrupt** to redirect `%rip`.

## The corruption order

A buffer overflow on a stack buffer `char buf[N]` corrupts memory in the direction **up the stack** (toward higher addresses, since the stack grows down):

```
high addr  ┌─────────────────────────┐
           │   return address (8B)   │  ← 8(%rbp)   target
           ├─────────────────────────┤
           │   saved %rbp (8B)       │  ← 0(%rbp)   collateral
           ├─────────────────────────┤
           │   adjacent locals       │              collateral
           ├─────────────────────────┤
           │   char buf[N]           │  ← overflow starts here
low addr   └─────────────────────────┘
```

The exact byte offset from `buf` to the return address — call it $k$ — depends on the function's specific frame layout. Per [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]'s `secret` example, $k = 40$ bytes for a 12-byte `buf`. The attacker's payload is therefore: **$k$ bytes of arbitrary padding + 8 bytes of target address**.

## Little-endian payload encoding

[[X86_64|x86-64]] is [[ByteOrder|little-endian]] (per [[dis-4-7-byte-order|Ch 4.7]]) — the target address `0x4006da` appears in the payload as the byte sequence `\xda\x06\x40\x00\x00\x00\x00\x00`. Forgetting this is the most common beginner exploit-construction error.

## Target classes

The attacker chooses what address to write into the return-address slot from a menu:

- **An existing function in the program**. The [[dis-7-10-x86-64-buffer-overflow|Ch 7.10]] `secret` example redirects to a never-normally-called `endGame()` function. Trivial but illustrative.
- **Injected shellcode on the stack**. Pre-[[ExecutableSpaceProtection|NX]] systems allow the attacker to place arbitrary instructions in the overflow buffer itself and point the return address at them. Defeated by [[ExecutableSpaceProtection|NX / DEP]].
- **A libc function** (return-to-libc). Avoids the need for stack-resident shellcode; `system("/bin/sh")` is the classic target. **Defeats early [[ExecutableSpaceProtection|NX]]** without needing full [[ReturnOrientedProgramming|ROP]].
- **A [[ReturnOrientedProgramming|ROP gadget chain]]**. Modern variant; the *return-address slot* becomes the *first* in a sequence of small gadget addresses, each ending in `retq` to advance the chain.

## Detection / prevention

- **[[StackCanary|Stack canaries]]** — a guard value placed *between* the local buffers and the saved return address detects any contiguous overflow before [[RetInstruction|`retq`]] is reached.
- **[[AddressSpaceLayoutRandomization|ASLR]]** — randomizes the locations the attacker would target, forcing them to leak an address before constructing a payload.
- **[[BoundsChecking|Bounded library functions]]** — prevent the overflow that enables the overwrite in the first place ([[dis-7-10-x86-64-buffer-overflow|Ch 7.10]]'s programmer-level defense).
- **Shadow stacks / [[ControlFlowIntegrity|CFI]]** — modern hardware-assisted defenses keep an out-of-band copy of the return address and verify it before `retq` (e.g., Intel CET).

## Sources

- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 names `8(%rbp)` as the target slot and walks the 40-byte-padding + 8-byte-little-endian-address payload construction explicitly.
