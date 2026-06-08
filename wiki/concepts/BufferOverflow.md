---
title: "Buffer Overflow"
type: concept
tags: [security, c-language, memory-safety, undefined-behavior]
sources: [dis-1-5-arrays-strings, dis-7-10-x86-64-buffer-overflow, fuzzingbook-03-fuzzer]
last_updated: 2026-06-06
---

# Buffer Overflow

A **buffer overflow** is the security failure mode where a program writes past the end of a fixed-capacity [[CArray|buffer]] into adjacent memory. The write *succeeds* (no [[BoundsChecking|bounds check]] stops it in [[CLanguage|C]]); the data corrupted is *some other program state* — another local variable, a saved frame pointer, a function return address, a heap chunk's metadata. In the worst case, an attacker who controls the input that drives the overflow can place an arbitrary return address on the stack and **redirect execution into code of their choosing** — the *stack-smashing* exploit.

## Why C is the canonical setting

[[CLanguage|C]] performs **no [[BoundsChecking|bounds check]]** on [[ArrayIndexing|array indexing]] or on the unbounded string functions in [[StringLibrary|`<string.h>`]]. Per [[dis-1-5-arrays-strings|Ch 1.5]] of [[DiveIntoSystems]], [[Strcpy|`strcpy()`]] *"poses a security risk because it assumes that its destination is large enough to store the entire string, which may not always be the case (for example, if the string comes from user input)."*

## The canonical recipe

```c
void greet(void) {
    char name[16];                  // 16-byte stack buffer
    printf("Enter your name: ");
    gets(name);                     // reads until newline, no length limit
    printf("Hello, %s!\n", name);
}
```

If the user types a 100-byte name, [[CLanguage|C]] writes 100 bytes into the 16-byte buffer. The extra 84 bytes overwrite *whatever's after `name` on the stack* — typically the saved frame pointer and the return address that `greet`'s `return` will jump to. (`gets` has been removed from the C standard for exactly this reason.)

The same trick works through [[Strcpy|`strcpy`]] (per [[dis-1-5-arrays-strings|Ch 1.5]]'s explicit warning), [[Sprintf|`sprintf`]], `strcat`, and any function that writes a caller-controlled number of bytes into a fixed-size buffer.

## What's at stake

- **Crashes** (the overflow corrupts a pointer that's later dereferenced).
- **Information disclosure** (an overflow on a *read* — a buffer over-read — exposes adjacent memory; CVE-2014-0160 *Heartbleed* is the famous example).
- **Arbitrary code execution** (the attacker controls the return address and jumps into shellcode they injected into the buffer, or into existing code reused as gadgets — *return-oriented programming*).

A substantial fraction of historical remote-code-execution vulnerabilities in widely-deployed C/C++ software originate in buffer overflows.

## Defenses (in order of when they were deployed)

1. **Don't use the unbounded functions** — prefer `strncpy`/`snprintf` over [[Strcpy|`strcpy`]]/[[Sprintf|`sprintf`]] ([[DiveIntoSystems]] Ch 2.6).
2. **Stack canaries** — compiler inserts a guard value between locals and the saved frame pointer; checked before return. GCC's `-fstack-protector`.
3. **Non-executable stack** (W^X / NX bit) — defeats naïve shellcode injection. Sidestepped by ROP.
4. **ASLR** — randomize address layout so the attacker doesn't know where to jump.
5. **Memory-safe languages** — Rust, Go, Java, [[Python]] simply do not exhibit this class of bug. The most thorough fix.

## Where this lands in [[DiveIntoSystems]]

[[dis-1-5-arrays-strings|Ch 1.5]] *introduces* the hazard in passing (the [[Strcpy|`strcpy`]] warning); Ch 2.6 develops it in detail with the safer-functions catalog; the assembly and architecture chapters return to it when explaining stack layout and calling conventions.

## From The Fuzzing Book — Fuzzing: Breaking Things with Random Inputs
[[fuzzingbook-03-fuzzer|Ch 3]] casts buffer overflows as the **canonical bug class that [[Fuzzing|fuzzing]] finds**, because random inputs trivially produce arbitrarily long strings and input elements. Its minimal C example — `char weekday[9]; strcpy(weekday, input);` — already overflows on `"Wednesday"` (9 chars), corrupting adjacent memory; the book simulates the behavior with a Python `crash_if_too_long(s)`. It then introduces the runtime defense pairing: compile with [[AddressSanitizer]] (`clang -fsanitize=address`, ~2× slowdown) so out-of-bounds reads/writes abort with a diagnostic — the same method that surfaced the [[Heartbleed]] over-read in [[OpenSSL]]. It distinguishes overflows from in-bounds [[InformationLeak|information leaks]], which ASan cannot catch.

## Sources

- [[dis-1-5-arrays-strings]] — Ch 1.5 §1.5.4 flags [[Strcpy|`strcpy`]]'s buffer-overflow risk and forwards the reader to Ch 2.6 for safer alternatives.
- [[fuzzingbook-03-fuzzer]] — *The Fuzzing Book* Ch 3 treats buffer overflows as a primary fuzzing-found bug class and pairs fuzzing with [[AddressSanitizer]].
- [[dis-7-10-x86-64-buffer-overflow]] — Ch 7.10 *operationalizes* the hazard at the [[X86_64|x86-64]] [[StackFrame|stack-frame]] surface with the `secret` worked exploit (40-byte padding + 8-byte little-endian return address); develops [[StackSmashing|stack smashing]], [[ReturnAddressOverwrite]], the [[StackCanary|canary]] / [[AddressSpaceLayoutRandomization|ASLR]] / [[ExecutableSpaceProtection|NX]] defenses, the [[ReturnOrientedProgramming|ROP]] bypass, and the Morris Worm / AOL Chat Wars historical case studies.
