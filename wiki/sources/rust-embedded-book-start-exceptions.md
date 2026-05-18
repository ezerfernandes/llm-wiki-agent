---
title: "The Embedded Rust Book — Exceptions"
type: source
tags: [rust, embedded, book-chapter, exceptions, cortex-m]
date: 2026-05-16
source_file: raw/book/src/start/exceptions.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Exceptions

## Summary

File 16/44 of *[[TheEmbeddedRustBook]]* — the *Getting Started* chapter's **Exceptions** sub-section, immediately after [[rust-embedded-book-start-panicking|Panicking]]. Introduces the [[CortexMRTCrate|`cortex-m-rt`]] [[ExceptionAttribute|`#[exception]`]] attribute as the declarative surface for [[ARMCortexM|Cortex-M]] exception handlers; explains why such handlers can use `static mut` *safely* (the attribute makes them un-callable from software, so the hardware-only invocation contract precludes reentrancy on a single core). Three worked examples: a [[SysTick]] handler that increments a `COUNT` `static mut` and prints over [[ARMSemihosting|semihosting]] on [[QEMU]]; an override of [[DefaultHandler|`DefaultHandler`]] with the `irqn: i16` discriminant (negative → Cortex-M architectural exception, ≥ 0 → device [[Interrupt|interrupt]]); and a [[HardFault]] handler with the mandatory `fn(&ExceptionFrame) -> !` signature, demonstrating post-mortem of an invalid `ptr::read_volatile(0x3FFF_0000)` via the [[ExceptionFrame|`ExceptionFrame`]] register snapshot + disassembly cross-reference.

## Key Claims

- **Exceptions are the hardware preemption mechanism**: asynchronous events + fatal errors (e.g. invalid instruction) suspend current execution and dispatch to subroutines (handlers).
- **`#[exception]` is `cortex-m-rt`'s declarative surface**: an attribute macro from `cortex-m-rt-macros` that marks a `fn` as the handler for a specific named architectural exception (`SysTick`, `HardFault`, `NMI`, …) or as the catch-all `DefaultHandler`.
- **Software-uncallable handlers**: calling an `#[exception]`-attributed function from regular code is a **compile error** (`SysTick();` won't compile). This is intentional — it is the precondition that makes the next claim sound.
- **`static mut` inside `#[exception]` is safe**: the attribute rewrites `static mut COUNT: u32 = 0;` into `&mut u32` of the same name, ergonomically as if wrapped in `unsafe`. Soundness rests on **non-reentrancy by hardware invariant**: the hardware will not concurrently re-enter the same handler on a single core, so the `&mut` is unique.
- **Multicore caveat**: on multiple cores the same exception handler can run concurrently on different cores; the soundness argument no longer holds and explicit synchronization (locks / atomics) becomes necessary.
- **`DefaultHandler` is the override-able catch-all**: `cortex-m-rt` populates every unfilled slot with `DefaultHandler` (an infinite loop, `#[no_mangle]` so a debugger can breakpoint it). User can override with `#[exception] fn DefaultHandler(irqn: i16) { … }`; `irqn` < 0 ⇒ Cortex-M exception number, `irqn` ≥ 0 ⇒ device-specific [[Interrupt|IRQ]] number.
- **`HardFault` is special**: signature is forced to `fn(&ExceptionFrame) -> !` (must diverge — returning from a hard fault is undefined behavior because the program is already in an invalid state). The `cortex-m-rt` runtime performs a `HardFaultTrampoline` preamble that pushes a register snapshot and passes it as `&ExceptionFrame` so the handler can diagnose.
- **`ExceptionFrame` is the diagnostic primitive**: a snapshot struct with `r0, r1, r2, r3, r12, lr, pc, xpsr` fields — exactly what the Cortex-M architecture pushes onto the stack at exception entry. The chapter's example dumps it over semihosting then cross-references `pc` against the `cargo objdump` disassembly to identify the faulting instruction (`ldr r0, [r0]` at `0x0800094a` reading `0x3fff_fffe`).
- **The `SysTick` worked example pins the dependency set**: `cortex-m = "0.5.7"`, `cortex-m-rt = "0.6.3"`, `panic-halt = "0.2.0"`, `cortex-m-semihosting = "0.3.1"` — and runs on QEMU via `qemu-system-arm -cpu cortex-m3 -machine lm3s6965evb`.
- **Self-terminating QEMU pattern**: `if *COUNT == 9 { debug::exit(debug::EXIT_SUCCESS); }` inside the handler stops the emulator after nine ticks. Same hardware caveat as [[rust-embedded-book-start-semihosting|the Semihosting chapter]]: never `debug::exit` on real hardware (corrupts the [[OpenOCD]] session).

## Key Quotes

> "`exception` handlers can *not* be called by software. Following the previous example, the statement `SysTick();` would result in a compilation error."

> "`static mut` variables declared *inside* `exception` handlers are *safe* to use."

> "These handlers are called by the hardware itself which is assumed to be physically non-concurrent."

> "The `HardFault` exception is a bit special. This exception is fired when the program enters an invalid state so its handler can *not* return as that could result in undefined behavior."

> "If you don't override the handler for a particular exception it will be handled by the `DefaultHandler` function, which defaults to: `fn DefaultHandler() { loop {} }`."

## Connections

- [[TheEmbeddedRustBook]] — file 16/44; *Getting Started* chapter, *Exceptions* sub-section.
- [[rust-embedded-book-start-panicking]] — immediate predecessor; both chapters use attribute macros (`#[panic_handler]`, `#[exception]`) to inject runtime-essential functions into `cortex-m-rt`'s machinery.
- [[CortexMRTCrate]] — supplier of `#[exception]`, `DefaultHandler`, `HardFaultTrampoline`, and `ExceptionFrame`. The chapter exercises the user-facing surface of the runtime that earlier chapters introduced structurally.
- [[VectorTable]] — the underlying mechanism: `#[exception]` populates a specific slot in the `.vector_table` section that the chapter's predecessor ([[rust-embedded-book-start-qemu]]) made visible via `cargo size`.
- [[SysTick]] — the example exception in the long worked example; the chapter operationalizes the SysTick handler slot that [[rust-embedded-book-start-registers|the Registers chapter]] introduced as a peripheral.
- [[Interrupt]] — exceptions are a superset: Cortex-M architectural exceptions (negative `irqn`) plus device-specific interrupts (`irqn` ≥ 0) share the same dispatch path through `cortex-m-rt`.
- [[ARMCortexM]] — defines the exception model the chapter exercises (16 architectural slots + N device IRQs, exception entry pushes the register snapshot that becomes `ExceptionFrame`).
- [[HardFault]] — the special exception with the forced `fn(&ExceptionFrame) -> !` signature.
- [[DefaultHandler]] — the catch-all the chapter walks through overriding.
- [[ExceptionAttribute]] — the `#[exception]` attribute macro the entire chapter is built around.
- [[ExceptionFrame]] — the register-snapshot diagnostic primitive used in the `HardFault` example.
- [[ARMSemihosting]] / [[QEMU]] / [[LM3S6965]] — the host-IO + emulation substrate used by the SysTick example, inherited from earlier chapters.
- [[PanicHaltCrate]] — paired panic handler in the example's `Cargo.toml`.

## Contradictions

None with existing wiki content. The chapter is additive: it introduces handler-surface concepts ([[ExceptionAttribute]], [[DefaultHandler]], [[HardFault]], [[ExceptionFrame]]) that [[VectorTable]] and [[CortexMRTCrate]] previously referenced only by name.
