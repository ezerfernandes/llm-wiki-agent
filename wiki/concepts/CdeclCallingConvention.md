---
title: "cdecl Calling Convention (IA32)"
type: concept
tags: [calling-convention, abi, ia32, x86, 32-bit, stack]
sources: [dis-8-1-ia32-basics]
last_updated: 2026-05-17
---

# cdecl Calling Convention (IA32)

**cdecl** ("C declaration") is the standard [[CallingConvention|calling convention]] for [[IA32|32-bit x86]] [[CLanguage|C]] code on Linux / macOS / BSD — the IA32 sibling of [[X86_64|x86-64]]'s [[SystemVCallingConvention|System V AMD64 ABI]]. Codified by [[dis-8-1-ia32-basics|Ch 8.1]] of *[[DiveIntoSystems]]* as the **headline delta** from Ch 7's [[X86_64|x86-64]] story.

## Argument passing (the headline difference)

**All function arguments are pushed onto the stack** — IA32 has **no** register-based argument-passing convention analogous to [[SystemVCallingConvention|System V AMD64]]'s six argument registers (`%rdi` / `%rsi` / `%rdx` / `%rcx` / `%r8` / `%r9`). Caller pushes arguments right-to-left so the first argument ends up at the lowest stack address.

Inside the callee (after the standard prologue `push %ebp; mov %esp, %ebp`), parameters are accessed at positive offsets above the saved frame pointer:

| Offset | Slot |
|---|---|
| `0(%ebp)` | saved old `%ebp` (caller's frame pointer) |
| `4(%ebp)` | saved return address (pushed by `call`) |
| `8(%ebp)` | first parameter |
| `12(%ebp)` | second parameter |
| `16(%ebp)` | third parameter |
| ... | ... |

## Return value

Integer / pointer return values are placed in `%eax` — same architectural role as [[X86_64|x86-64]]'s `%rax`. 64-bit return values use the `%edx:%eax` pair (high half in `%edx`, low half in `%eax`).

## Caller cleanup

After the callee's `ret`, the **caller** is responsible for removing the pushed arguments from the stack (typically via `add $N, %esp`). This is what distinguishes cdecl from the Windows API's stdcall convention, where the callee cleans up via `ret $N`. Caller cleanup makes cdecl naturally compatible with **variadic functions** ([[Printf|`printf`]], [[Scanf|`scanf`]]) — the caller knows the actual argument count and can clean up exactly that many bytes.

## Register preservation

- **Caller-saved** (caller must preserve across a call): `%eax`, `%ecx`, `%edx`.
- **Callee-saved** (callee must save+restore): `%ebx`, `%esi`, `%edi`, `%ebp`.

Same caller/callee split philosophy as [[CallerSavedRegister|System V]] — different specific register assignments since IA32 has only 8 GPRs vs x86-64's 16.

## Comparison: cdecl vs System V x86-64

| Dimension | cdecl (IA32) | System V AMD64 (x86-64) |
|---|---|---|
| First 6 args | All on stack | `%rdi`/`%rsi`/`%rdx`/`%rcx`/`%r8`/`%r9` |
| Stack cleanup | Caller | Caller (also) |
| Return value | `%eax` (32-bit) / `%edx:%eax` (64-bit) | `%rax` (64-bit) / `%rdx:%rax` (128-bit) |
| Caller-saved | `%eax`, `%ecx`, `%edx` | `%rax`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%r8`–`%r11` |
| Callee-saved | `%ebx`, `%esi`, `%edi`, `%ebp` | `%rbx`, `%rbp`, `%r12`–`%r15` |

[[dis-7-1-x86-64-basics|Ch 7.1]]'s headline *"first six parameters in registers"* claim does **not** apply at the IA32 surface — the architectural pressure that motivated System V's register-passing (16 GPRs available, fewer arguments need to spill) simply isn't present on IA32's 8-register surface.

## Connections

- [[dis-8-1-ia32-basics]] — introducing source.
- [[CallingConvention]] — the umbrella concept; cdecl is one instance.
- [[SystemVCallingConvention]] — the [[X86_64|x86-64]] sibling — register-based, no IA32 equivalent.
- [[IA32]] — the ISA cdecl serves.
- [[StackFrame]] — `%ebp`-relative addressing of parameters and locals.
- [[FramePointer]] / [[StackPointer]] — `%ebp` / `%esp` are the IA32 names.
- [[CallerSavedRegister]] / [[CalleeSavedRegister]] — the caller-/callee-saved partition concept.
- [[Printf]] / [[Scanf]] — variadic functions whose ABI compatibility motivates caller cleanup.
