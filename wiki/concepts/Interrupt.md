---
title: "Interrupt"
type: concept
tags: [embedded, hardware, async, operating-systems]
sources: [rust-embedded-book-intro-index, rust-embedded-book-start-interrupts, dis-13-1-booting-running]
last_updated: 2026-05-17
---

# Interrupt

Asynchronous control-flow event in which the CPU suspends its current execution, saves context, and jumps to a designated *interrupt service routine* (ISR) in response to a hardware signal (timer expiring, peripheral data ready, GPIO edge, etc.), then resumes the prior execution after the ISR returns. The dominant mechanism for handling external events in [[EmbeddedSystems|embedded systems]] and the reason [[BareMetalProgramming|bare-metal]] firmware can stay responsive without an OS scheduler. Listed by [[TheEmbeddedRustBook]] as a prerequisite concept for embedded-experienced readers ([[rust-embedded-book-intro-index]]).

On [[ARMCortexM|ARM Cortex-M]] the [[NVIC|**Nested Vectored Interrupt Controller (NVIC)**]] prioritizes and dispatches interrupts; Rust embedded HAL crates expose interrupt handlers as [[InterruptAttribute|`#[interrupt]`]]-attributed functions with type-state-checked register access.

## Exceptions vs interrupts

[[rust-embedded-book-start-interrupts|The Interrupts chapter]] formalizes the distinction: **exceptions** are defined by the [[ARMCortexM|Cortex-M]] architecture (fixed names like `NMI`, `HardFault`, `SysTick`) and handled by [[ExceptionAttribute|`#[exception]`]]; **interrupts** are vendor- and chip-specific (the names come from the [[SVDFile|SVD]] description) and handled by [[InterruptAttribute|`#[interrupt]`]]. Both flow through the same [[NVIC]] and populate the same [[VectorTable|vector table]] — the [[DefaultHandler|`DefaultHandler`]]'s `irqn: i16` discriminant splits them at runtime (`< 0` ⇒ architectural exception, `≥ 0` ⇒ device interrupt).

## Three advanced-use properties (NVIC-level)

From [[rust-embedded-book-start-interrupts]]:

1. **[[InterruptPriority|Programmable priorities]]** — handlers dispatch in priority order.
2. **Nesting / preemption** — running handlers can be interrupted by higher-priority sources.
3. **Clear-reason requirement** — handlers must clear the peripheral flag that triggered them, or the [[NVIC]] re-pends endlessly.

## OS-level role ([[dis-13-1-booting-running|DIS 13.1]])

On a general-purpose [[OperatingSystem|OS]], interrupts are the **architectural mechanism** that makes the system reactive — *"Most operating systems are implemented as interrupt-driven systems, meaning that the OS doesn't run until some entity needs it to do something — the OS is woken up (interrupted from its sleep) to handle a request."* Two interrupt sources are distinguished:

- **Hardware interrupts** — devices signal the [[CPU]] via an interrupt bus (NIC data arrival, disk I/O complete, timer tick).
- **Traps / software interrupts** — user programs execute a trap instruction to invoke a [[SystemCall|system call]].

Either path drives the CPU into [[KernelMode|kernel mode]] to run an OS handler; on return the CPU resumes the interrupted user-mode instruction — the [[ContextSwitch|context switch]].

## Connections

- [[EmbeddedSystems]] — interrupts are the canonical event-handling mechanism here.
- [[OperatingSystem]] / [[Kernel]] — at the OS level, interrupts wake the kernel from sleep.
- [[SystemCall]] — the software-interrupt (trap) variant invoked by user code.
- [[KernelMode]] / [[UserMode]] / [[ContextSwitch]] — what a trap or hardware interrupt drives.
- [[DiveIntoSystems]] · [[dis-13-1-booting-running]] — OS-level treatment.
- [[Microcontroller]] — MCUs expose interrupt controllers (NVIC on Cortex-M) for peripheral events.
- [[ARMCortexM]] — Cortex-M's NVIC is the specific interrupt-controller architecture in [[TheEmbeddedRustBook]]'s examples.
- [[NVIC]] — the Cortex-M Nested Vectored Interrupt Controller; dispatches priorities, handles nesting.
- [[InterruptAttribute]] — the Rust `#[interrupt]` attribute that marks an `fn` as a device interrupt handler.
- [[InterruptPriority]] — programmable per-source priority the NVIC honors.
- [[ExceptionAttribute]] — sibling attribute for architectural Cortex-M exceptions.
- [[Svd2Rust]] / [[SVDFile]] — the device crate's interrupt enum and `#[interrupt]` re-export come from the chip's SVD.
