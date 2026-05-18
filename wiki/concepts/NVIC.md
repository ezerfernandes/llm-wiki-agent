---
title: "NVIC (Nested Vectored Interrupt Controller)"
type: concept
tags: [embedded, arm, cortex-m, hardware, interrupts]
sources: [rust-embedded-book-start-interrupts]
last_updated: 2026-05-16
---

# NVIC (Nested Vectored Interrupt Controller)

The **[[ARMCortexM|Cortex-M]] core's built-in interrupt controller** — a memory-mapped peripheral, **architecturally standardized** across every Cortex-M chip, that prioritizes, dispatches, and (optionally) preempts both architectural [[ARMCortexM|Cortex-M]] exceptions and device-specific [[Interrupt|interrupts]] through the same [[VectorTable|vector table]]. The "**N**ested" refers to its ability to interrupt a running handler with a *higher-priority* one (preemption); the "**V**ectored" refers to direct dispatch to a per-source handler pointer (no software dispatch table walk).

## Three properties [[TheEmbeddedRustBook]] flags for advanced use

From [[rust-embedded-book-start-interrupts|the Interrupts chapter]]:

1. **Programmable priorities** ([[InterruptPriority]]) — every interrupt has a per-source priority register; the NVIC dispatches handlers in priority order when multiple are pending simultaneously.
2. **Nesting / preemption** — execution of an interrupt handler **can be interrupted** by another higher-priority interrupt. The CPU pushes a second [[ExceptionFrame]] onto the stack and dispatches the new handler; on return, the original resumes.
3. **Clear-reason requirement** — the cause that triggered the interrupt request **must be cleared inside the handler** (typically by writing to a peripheral status register). Otherwise the NVIC immediately re-pends the source and the handler re-enters endlessly.

## Initialization recipe

Always the same three steps at runtime ([[rust-embedded-book-start-interrupts]]):

1. Configure the **peripheral** to generate interrupt requests at the desired occasions.
2. Set the desired **priority** in the NVIC.
3. **Enable** the handler in the NVIC.

## Relationship to the vector table

The NVIC's interrupt sources occupy slots **16 onward** in the [[VectorTable|vector table]] — the first 16 slots are reserved for [[ARMCortexM|Cortex-M]] architectural exceptions (NMI, HardFault, MemManage, BusFault, UsageFault, SVCall, PendSV, SysTick, …). Device-specific interrupts (`irqn ≥ 0` in `DefaultHandler(irqn: i16)` — see [[DefaultHandler]]) are numbered by the chip vendor and described in the chip's [[SVDFile|SVD]]; [[Svd2Rust|`svd2rust`]] generates the device crate's interrupt enum + `#[interrupt]` re-export from this description.

## Software triggering

Although interrupt handlers cannot be called directly from firmware (special calling convention), the NVIC exposes a software-trigger register (`STIR`) so firmware **can deliberately raise an interrupt request in software** — useful for testing handlers and for inter-task signaling on Cortex-M.

## Connections

- [[ARMCortexM]] — the NVIC is architecturally part of the Cortex-M core; every Cortex-M chip ships with one.
- [[Interrupt]] — the NVIC is the controller that dispatches them.
- [[InterruptPriority]] — the per-source programmable priority the NVIC honors.
- [[VectorTable]] — slots 16+ are the NVIC's device-specific interrupt-handler pointers.
- [[ExceptionAttribute]] / [[InterruptAttribute]] — the Rust attributes that populate (architectural and device-specific) slots the NVIC reads.
- [[DefaultHandler]] — the catch-all whose `irqn: i16` discriminant matches the NVIC's interrupt numbering (`irqn ≥ 0`).
- [[SVDFile]] / [[Svd2Rust]] — the description-and-generator pair that gives Rust code typed access to the NVIC's per-chip interrupt enumeration.
- [[TheEmbeddedRustBook]] — names the NVIC in [[Interrupt]]'s introductory paragraph and operationalizes its three advanced-use properties in [[rust-embedded-book-start-interrupts]].
