---
title: "ARM Cortex-M"
type: concept
tags: [arm, isa, microcontroller, embedded]
sources: [rust-embedded-book-intro-index]
last_updated: 2026-05-16
---

# ARM Cortex-M

Family of 32-bit RISC processor cores from Arm Ltd. designed for [[Microcontroller|microcontroller]] use — low power, deterministic interrupt handling, small silicon area. Variants (M0 / M0+ / M3 / M4 / M7 / M23 / M33 / M55) trade off feature set (FPU, DSP, security extensions) and performance. The standardized ISA / core profile family used in **all examples** of [[TheEmbeddedRustBook]]; the [[STM32F3DISCOVERY]] uses a Cortex-M4 ([[rust-embedded-book-intro-index]]).

The book chooses Cortex-M for pedagogical tractability ("to make things easier for both the readers and the writers") but takes care to explain Cortex-M specifics rather than assume reader familiarity. The choice constrains *examples*, not Rust's actual embedded reach — embedded Rust runs on many other ISAs (RISC-V, AVR, MSP430, Xtensa, etc.).

## Connections

- [[Microcontroller]] — Cortex-M is the dominant 32-bit MCU core family.
- [[STM32F3DISCOVERY]] — Cortex-M4 reference board used by [[TheEmbeddedRustBook]].
- [[EmbeddedSystems]] — Cortex-M is the canonical embedded ISA in the book's scope.
