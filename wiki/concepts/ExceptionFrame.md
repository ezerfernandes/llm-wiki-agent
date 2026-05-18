---
title: "ExceptionFrame (cortex-m-rt)"
type: concept
tags: [rust, embedded, cortex-m, exceptions, debugging, registers]
sources: [rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# ExceptionFrame

**A register-snapshot struct in [[CortexMRTCrate|`cortex-m-rt`]] mirroring the eight 32-bit words the [[ARMCortexM|Cortex-M]] hardware pushes onto the stack on exception entry.** The single argument of a [[HardFault]] handler, exposing the processor's state at the instant the fault was taken so the handler can perform a post-mortem ([[rust-embedded-book-start-exceptions]]).

## Layout

The struct mirrors the Cortex-M exception-entry stack frame:

```text
r0    — caller-saved general register
r1    — caller-saved general register
r2    — caller-saved general register
r3    — caller-saved general register
r12   — intra-procedure scratch
lr    — link register (return address of the faulting context)
pc    — program counter at the moment of the fault
xpsr  — combined program-status register
```

The `pc` field is the **most useful diagnostic** — it identifies the exact instruction that triggered the exception. The chapter's worked example ([[rust-embedded-book-start-exceptions]]) prints the frame over [[ARMSemihosting|semihosting]], looks up `pc = 0x0800094a` in `cargo objdump -d` output, finds the offending `ldr r0, [r0]`, and then reads `ef.r0 = 0x3fff_fffe` to discover the bad address that the load tried to dereference.

```text
ExceptionFrame {
    r0:   0x3fff0000,
    r1:   0x00000003,
    r2:   0x080032e8,
    r3:   0x00000000,
    r12:  0x00000000,
    lr:   0x080016df,
    pc:   0x080016e2,
    xpsr: 0x61000000,
}
```

## Where it comes from

The `HardFaultTrampoline` preamble that `cortex-m-rt` interposes between the [[VectorTable|vector-table]] entry and the user's [[HardFault]] handler is responsible for materializing the stack-pushed words into the struct and passing it as `&ExceptionFrame` ([[rust-embedded-book-start-exceptions]]). `cargo objdump` of any `cortex-m-rt`-linked binary exposes the `HardFaultTrampoline` symbol — first noted in [[rust-embedded-book-start-qemu]].

## Connections

- [[HardFault]] — the only exception whose handler receives an `&ExceptionFrame`.
- [[ExceptionAttribute]] — the attribute that wires a Rust function to receive this frame.
- [[CortexMRTCrate]] — supplies the struct definition and the `HardFaultTrampoline` that materializes it.
- [[VectorTable]] — the vector table entry the trampoline sits behind.
- [[ARMCortexM]] — defines the hardware push order this struct mirrors.
- [[TheEmbeddedRustBook]] — worked diagnostic example at [[rust-embedded-book-start-exceptions]].
