---
title: "Interrupt Priority"
type: concept
tags: [embedded, arm, cortex-m, interrupts, hardware]
sources: [rust-embedded-book-start-interrupts]
last_updated: 2026-05-16
---

# Interrupt Priority

The **per-source programmable priority** the [[NVIC|Nested Vectored Interrupt Controller]] honors when dispatching pending [[Interrupt|interrupts]] and architectural [[ARMCortexM|Cortex-M]] exceptions. Determines two things at runtime:

1. **Dispatch order** when multiple interrupts are pending simultaneously — the highest-priority pending source wins.
2. **Preemption (nesting)** — a running handler can be **interrupted** by another source of *higher* priority; the CPU pushes a second [[ExceptionFrame]] onto the stack and dispatches the new handler. On return, the original resumes from where it was preempted.

[[TheEmbeddedRustBook]]'s [[rust-embedded-book-start-interrupts|Interrupts chapter]] flags this as the **first** of three advanced-use properties to keep in mind: *"Interrupts have programmable priorities which determine their handlers' execution order."*

## Initialization

The chapter's three-step recipe puts priority configuration **second**, between peripheral setup and handler enablement:

1. Setup the peripheral(s) to generate interrupt requests at the desired occasions.
2. **Set the desired priority of the interrupt handler in the [[NVIC|interrupt controller]].**
3. Enable the interrupt handler in the [[NVIC|interrupt controller]].

Order matters: priority must be set **before** enabling, otherwise the (default-priority) handler could fire before its real priority is configured.

## Underlying hardware

On [[ARMCortexM|Cortex-M]] the NVIC's `IPR` (Interrupt Priority Register) array holds an 8-bit priority byte per interrupt source — though most chips implement only the **top few bits** (typically 3–4 of the 8, giving 8–16 distinct priority levels). The book stays agnostic about chip-specific priority-bit counts; concrete numbers come from the chip's reference manual / [[SVDFile|SVD]].

## Connections

- [[NVIC]] — the controller that reads priority registers and uses them for dispatch + preemption decisions.
- [[Interrupt]] — what priority is assigned to.
- [[InterruptAttribute]] — declares the *handler*; priority must be configured separately (PAC/HAL call) before enabling.
- [[ARMCortexM]] — the architecture defining the NVIC priority model (8-bit fields, top-N-bits-implemented).
- [[ExceptionFrame]] — pushed onto the stack at every preemption boundary; nested preemption means stacked frames.
- [[TheEmbeddedRustBook]] — flagged as advanced-use property #1 in [[rust-embedded-book-start-interrupts]].
