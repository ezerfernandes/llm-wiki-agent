---
title: "HardFault Exception"
type: concept
tags: [arm, embedded, cortex-m, exceptions, debugging, faults]
sources: [rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# HardFault

The **[[ARMCortexM|Cortex-M]] architectural exception fired when the program enters an invalid state** — an escalation of any other fault (BusFault / UsageFault / MemManage) the system did not, or could not, handle separately. Once `HardFault` is taken, the processor is by definition in an unrecoverable condition for the current execution flow ([[rust-embedded-book-start-exceptions]]).

## The divergent-signature contract

In [[CortexMRTCrate|`cortex-m-rt`]] the `HardFault` slot is unique among [[ExceptionAttribute|`#[exception]`]] handlers: it has a **mandatory** signature

```rust,ignore
#[exception]
fn HardFault(ef: &ExceptionFrame) -> ! {
    // diagnose, log, then halt — never return
}
```

Returning from a hard fault is **undefined behavior**, so the type system forces the handler to diverge (`-> !`). `cortex-m-rt` interposes a `HardFaultTrampoline` preamble that captures the register snapshot at fault-entry and passes it to the user handler as `&ExceptionFrame`.

## The `ExceptionFrame` argument

The single parameter is a pointer to the [[ExceptionFrame|register-snapshot frame]] the hardware pushed on the stack at exception entry: `r0, r1, r2, r3, r12, lr, pc, xpsr`. The chapter's example ([[rust-embedded-book-start-exceptions]]) prints it over [[ARMSemihosting|semihosting]] then cross-references `pc` against the `cargo objdump` disassembly to identify the exact instruction that faulted — for an invalid `ptr::read_volatile(0x3FFF_0000)`, the `ldr r0, [r0]` at `0x0800094a` with `r0 = 0x3fff_fffe`.

## QEMU vs. real hardware caveat

`qemu-system-arm -machine lm3s6965evb` **does not check memory loads** and will silently return `0` on reads to invalid memory — so the chapter's `HardFault` example does **not** trigger a fault under QEMU and only fires on a real [[ARMCortexM|Cortex-M]] target ([[rust-embedded-book-start-exceptions]]). A rare reversal of the "any-example-runs-on-QEMU" pedagogical contract of the broader chapter.

## Connections

- [[ExceptionAttribute]] — the attribute used to install a `HardFault` handler.
- [[ExceptionFrame]] — the diagnostic struct the handler receives.
- [[CortexMRTCrate]] — supplies `HardFaultTrampoline` + `HardFault_` (default) symbols seen by `cargo objdump` in [[rust-embedded-book-start-qemu]].
- [[VectorTable]] — `HardFault` occupies a fixed architectural slot in the table.
- [[ARMCortexM]] — defines the fault hierarchy and the register-push convention.
- [[DefaultHandler]] — fields any *other* exception the user did not override (HardFault is special-cased separately).
- [[TheEmbeddedRustBook]] — chapter dedicated to this exception type at [[rust-embedded-book-start-exceptions]].
