---
title: "The Embedded Rust Book — Interrupts"
type: source
tags: [rust, embedded, book-chapter, interrupts, nvic]
date: 2026-05-16
source_file: raw/book/src/start/interrupts.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Interrupts

## Summary

File 17/44 of *[[TheEmbeddedRustBook]]* — the *Getting Started* chapter's **Interrupts** sub-section and **last entry of the Getting Started chapter**, immediately after [[rust-embedded-book-start-exceptions|Exceptions]]. Deliberately short ("we will not cover those uses in this book") — defers detailed mechanics to the preceding [[rust-embedded-book-start-exceptions|exceptions chapter]] and signals the [[NVIC|interrupt-controller]] details as out-of-scope for the introductory text. Three substantive contributions: (1) draws the **exception-vs-interrupt distinction** — both flow through the same controller and dispatch path, but exceptions are *Cortex-M architectural* (named, fixed-position) while interrupts are *vendor- and chip-specific* (vendor-named, vendor-numbered); (2) introduces the [[InterruptAttribute|`#[interrupt]`]] attribute, which is **not** the [[ExceptionAttribute|`#[exception]`]] sibling re-exported from `cortex-m-rt-macros` directly — instead, users must use the **device-crate re-export** (e.g. `use lm3s6965::interrupt;`) so the compiler can verify the named interrupt exists in the chip's [[SVDFile|SVD]]-generated [[VectorTable|interrupt-vector slot]]; (3) enumerates the three runtime properties advanced users must keep in mind ([[InterruptPriority|programmable priorities]], **nesting / preemption** by higher-priority handlers, and the **clear-reason requirement** to prevent endless re-entry of the same handler). Re-uses the `static mut` safety story verbatim from the exceptions chapter — same soundness invariant, same `*COUNT += 1` example, same hardware-only invocation contract.

## Key Claims

- **Interrupts ≠ Exceptions** (though they share the controller and dispatch path): exceptions are defined by the [[ARMCortexM|Cortex-M architecture]] (fixed names and numbers — `NMI`, `HardFault`, `SysTick`, `PendSV`, …); interrupts are **always vendor- and often chip-specific** in both naming and numbering. Both ultimately populate the same [[VectorTable|vector table]] and dispatch through the same [[NVIC|interrupt controller]].
- **Three advanced-use properties to keep in mind**:
  1. Interrupts have **programmable priorities** that determine handler execution order.
  2. Interrupts can **nest and preempt** — a running handler may be interrupted by another higher-priority interrupt.
  3. The **reason causing the interrupt must be cleared** inside the handler — otherwise the [[NVIC|controller]] immediately re-pends and the handler is re-entered endlessly.
- **Initialization recipe** (always the same three steps at runtime):
  1. Configure the peripheral to *generate* interrupt requests at the desired occasions.
  2. Set the desired *priority* in the [[NVIC|interrupt controller]].
  3. *Enable* the handler in the [[NVIC|interrupt controller]].
- **`#[interrupt]` is `cortex-m-rt`'s declarative surface for device-specific interrupts** — re-exported from `cortex-m-rt-macros`, gated on the **`device` feature**. Calling it directly results in a **compilation error**.
- **Users must use the device-crate re-export, not the macro directly**: `use lm3s6965::interrupt;` (typically the [[Svd2Rust|`svd2rust`]]-generated device crate) — this re-export is wired to the chip's interrupt enum so the compiler can **verify the interrupt actually exists** on the target device. The list of available interrupts (and their vector-table positions) is auto-generated from the chip's [[SVDFile|SVD]].
- **Handler shape mirrors `#[exception]`**: ordinary `fn` (no arguments), `#[interrupt]`-tagged, named after a device interrupt (e.g. `TIMER2A`). **Software-uncallable**: same compile-time guarantee as `#[exception]`. **`static mut` inside is safe**: same soundness rewrite into `&mut T`, same hardware-only invocation invariant.
- **Cross-reference to exceptions**: the chapter explicitly says "for a more detailed description about the mechanisms demonstrated here please refer to the [exceptions section]" — confirming the design intent: `#[interrupt]` and `#[exception]` are siblings sharing the same mental model.
- **Hardware-only invocation, with a software triggering loophole**: like exceptions, interrupt handlers cannot be called directly by firmware due to special calling conventions; **but** the chapter notes interrupt requests **can be generated in software** to deliberately trigger a diversion to the handler (the underlying mechanism is the [[NVIC|NVIC]]'s `STIR` software-trigger register, though the chapter doesn't name it).

## Key Quotes

> "Interrupts differ from exceptions in a variety of ways but their operation and use is largely similar and they are also handled by the same interrupt controller."

> "Whereas exceptions are defined by the Cortex-M architecture, interrupts are always vendor (and often even chip) specific implementations, both in naming and functionality."

> "This attribute is not intended to be used directly—doing so will result in a compilation error. Instead, you should use the re-exported version of the interrupt attribute provided by the device crate (usually generated using svd2rust). This ensures that the compiler can verify that the interrupt actually exists on the target device."

> "In general the reason causing the interrupt to trigger needs to be cleared to prevent re-entering the interrupt handler endlessly."

> "For a more detailed description about the mechanisms demonstrated here please refer to the exceptions section."

## Connections

- [[TheEmbeddedRustBook]] — file 17/44; *Getting Started* chapter's *Interrupts* sub-section; **closes the Getting Started chapter** (the next chapter opens *IO* or *Peripherals* depending on book version).
- [[rust-embedded-book-start-exceptions]] — explicit predecessor and reference target; this chapter intentionally defers all detailed mechanics to that one. Same `static mut` example pattern, same `#[interrupt]`-vs-`#[exception]` design recipe.
- [[Interrupt]] — the underlying concept; this chapter operationalizes its `#[interrupt]`-surface in Rust.
- [[InterruptAttribute]] — the `#[interrupt]` attribute macro the entire chapter is built around.
- [[NVIC]] — the [[ARMCortexM|Cortex-M]] Nested Vectored Interrupt Controller through which both exceptions and device-specific interrupts dispatch; the substrate for the chapter's three "advanced uses" (priority, nesting, clear-reason).
- [[InterruptPriority]] — the programmable per-interrupt priority that determines handler execution order and preemption.
- [[ExceptionAttribute]] — sibling attribute macro the chapter cross-references for detailed mechanics.
- [[CortexMRTCrate]] — supplier of the underlying `interrupt` macro (gated on the `device` feature) that the device crate re-exports.
- [[Svd2Rust]] — generates the device crate's `interrupt` enum and re-exported attribute from the chip's [[SVDFile|SVD]] description.
- [[SVDFile]] — the vendor description that fixes interrupt names and vector-table positions per chip.
- [[VectorTable]] — the data structure `#[interrupt]` ultimately writes into (in the device-specific IRQ slots, `irqn ≥ 0`).
- [[LM3S6965]] — the example device whose `lm3s6965::interrupt` re-export the chapter uses.

## Contradictions

None with existing wiki content. The chapter is **largely additive and aggressively re-uses the exceptions chapter's machinery** — formalizes the `#[interrupt]` attribute that prior chapters referenced only by name (notably [[Interrupt]]'s opening paragraph mentioning `#[interrupt]`-attributed functions, and [[DefaultHandler]]'s `irqn ≥ 0` device-IRQ branch). The only nuance worth flagging: this chapter clarifies that **`#[interrupt]` is not used directly from `cortex-m-rt-macros`** — it must come through the device crate's re-export. Pre-existing [[Interrupt]] page elided that detail; the new [[InterruptAttribute]] concept records it.
