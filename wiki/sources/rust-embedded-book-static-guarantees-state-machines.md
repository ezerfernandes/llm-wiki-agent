---
title: "The Embedded Rust Book — Peripherals as State Machines"
type: source
tags: [rust, embedded, book-chapter, state-machines, typestate]
date: 2026-05-16
source_file: raw/book/src/static-guarantees/state-machines.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Peripherals as State Machines

## Summary

File 24/44 of *[[TheEmbeddedRustBook]]* — the **second named sub-section** of the *Static Guarantees* chapter, immediately after [[rust-embedded-book-static-guarantees-typestate-programming]] (which gave the abstract `FooBuilder` → `Foo` recipe). This file **grounds typestate in real hardware** by recasting an [[GPIO|MCU GPIO pin]] as a [[FiniteStateMachine|finite state machine]]: a hierarchical tree of states (*Disabled* → *Enabled* → *Configured as Output / Input* → leaf modes like *Output: High*, *Input: Pulled Low*, *Input: High Resistance*) plus explicit walked-out transition paths between them. Then it **sets up the negative example** the next sub-section will resolve: a naive `GpioConfig` struct with bare `set_enable` / `set_direction` / `set_input_mode` / `set_output_mode` / `get_input_status` methods that wrap an [[Svd2Rust|svd2rust]]-generated `GPIO_CONFIG` peripheral — convenient to write, but *not* state-machine-safe: nothing stops the program from setting `output_mode` while the pin is configured as an input, or from reaching unreachable register states like `input_mode = 11` (marked **"n/a — Invalid state. Do not set"** in the imaginary register-bit table). *"Although this interface is convenient to write, it doesn't enforce the design contracts set out by our hardware implementation."* The chapter's role: bridge the abstract typestate definition of file 23 into the concrete GPIO worked example the rest of the chapter will mechanize.

## Key Claims

- **Peripherals are state machines.** *"The peripherals of a microcontroller can be thought of as set of state machines."* Each peripheral has a finite set of valid configurations and a finite set of valid transitions between them.
- **GPIO has a hierarchical state tree.** A simplified [[GPIO]] pin has the states: *Disabled*, *Enabled → Configured as Output → (Output: High | Output: Low)*, *Enabled → Configured as Input → (Input: High Resistance | Input: Pulled Low | Input: Pulled High)*. Seven leaf states under three intermediate states under the root.
- **Transitions are explicit walks through the tree.** *Disabled → Input: High Resistance* requires four steps: Disabled → Enabled → Configured as Input → Input: High Resistance. *Input: Pulled Low → Output: High* requires four steps walking back up to *Configured as Input*, sideways to *Configured as Output*, then down to *Output: High*. Diagonal jumps are not allowed.
- **Hardware backs the state machine with register bits.** An imaginary `GPIO Configuration Register` packs `enable` (bit 0), `direction` (bit 1), `input_mode` (bits 2..3, with `11` flagged "n/a — Invalid state. Do not set"), `output_mode` (bit 4), and read-only `input_status` (bit 5). The state tree is a **projection** of this bit-pattern space onto its valid subspace.
- **Some register bit-patterns are invalid.** `input_mode = 11` is **not a valid state** — *"Invalid state. Do not set"*. The state machine's valid-state set is a strict subset of the register's representable bit-patterns.
- **The naive Rust API does not enforce the state machine.** A `GpioConfig` struct wrapping the svd2rust-generated `GPIO_CONFIG` peripheral with methods `set_enable(bool)` / `set_direction(bool)` / `set_input_mode(InputMode)` / `set_output_mode(bool)` / `get_input_status()` lets callers reach combinations the state tree disallows.
- **Specific incoherent combinations the naive API allows.** *"What happens if we set the `output_mode` field when our GPIO is configured as an input?"* Also: *"an output that is pulled low, or an input that is set high."* The bit fields are independently writable, so the bit-pattern space is the Cartesian product of bit ranges, **not** the state tree.
- **The cost depends on the hardware.** *"For some hardware, this may not matter. On other hardware, it could cause unexpected or undefined behavior!"* The static guarantee is most valuable precisely where the hardware **silently misbehaves** on illegal state combinations.
- **The verdict.** *"Although this interface is convenient to write, it doesn't enforce the design contracts set out by our hardware implementation."* This is the **gap** that the rest of the chapter's typestate refactor will close.

## Key Quotes

> "The peripherals of a microcontroller can be thought of as set of state machines." — the chapter's headline framing.

> "We could expose the following structure in Rust to control this GPIO […]. However, this would allow us to modify certain registers that do not make sense. For example, what happens if we set the `output_mode` field when our GPIO is configured as an input? In general, use of this structure would allow us to reach states not defined by our state machine above: e.g. an output that is pulled low, or an input that is set high." — the naive-API critique.

> "For some hardware, this may not matter. On other hardware, it could cause unexpected or undefined behavior!" — why the state machine's invalid-state set is a real-hardware concern, not a software-aesthetic one.

> "Although this interface is convenient to write, it doesn't enforce the design contracts set out by our hardware implementation." — the chapter's closing statement, motivating the next sub-section's typestate refactor.

## Connections

- [[TheEmbeddedRustBook]] — file 24/44; second named sub-section of the *Static Guarantees* chapter.
- [[rust-embedded-book-static-guarantees-typestate-programming]] — directly preceding file (23/44); gave the abstract `FooBuilder` → `Foo` typestate recipe. This file applies that recipe's *motivation* to a concrete embedded peripheral.
- [[rust-embedded-book-static-guarantees-index]] — chapter opener (22/44); previewed *configuration-dependent operations* (set_low on a floating-input pin) as one of the four [[StaticGuarantee|static-guarantee]] families. This sub-section unpacks the **state machine** underlying that family.
- [[rust-embedded-book-start-registers]] — file 13/44 already showed the *productionized* [[TypeStateProgramming|typestate]] solution for GPIO pin modes (`into_af_push_pull::<AF1>()`). This sub-section is the **conceptual setup** that explains *why* that solution exists.
- [[FiniteStateMachine]] — the underlying computational model the chapter applies to peripherals; the GPIO state tree is a hierarchical FSM.
- [[TypeStateProgramming]] — the design pattern the rest of the chapter will use to **encode** the GPIO state machine in Rust types so illegal transitions become compile errors.
- [[StaticGuarantee]] — the chapter-level framing concept; this sub-section motivates the *configuration-dependent-operations* family with a concrete state-machine example.
- [[GPIO]] — the peripheral the chapter uses as its worked example; pin modes (Input vs Output, push-pull vs open-drain, pull-up vs pull-down vs floating) are the canonical embedded state-machine.
- [[Svd2Rust]] — the chapter's naive `GpioConfig` wraps an svd2rust-generated `GPIO_CONFIG` peripheral, using the same `periph.modify(|_r, w| w.field().set_bit(...))` closure idiom introduced by [[rust-embedded-book-start-registers]].
- [[PeripheralAccessCrate]] — the PAC layer that supplies the `GPIO_CONFIG` register-block type the naive `GpioConfig` wraps.
- [[HALCrate]] — the crate-stack layer that, *in production*, replaces this naive `GpioConfig` with a typestate-encoded pin-mode API; the chapter's setup is the "before" picture of HAL-style design.

## Contradictions

None with existing wiki content. Strictly additive — supplies the **concrete embedded motivation** (the GPIO state tree + register bit-table + naive-API critique) for the typestate pattern abstractly defined in [[rust-embedded-book-static-guarantees-typestate-programming]] and operationally introduced in [[rust-embedded-book-start-registers]]. The "naive `GpioConfig` doesn't enforce the state machine" framing is consistent with — and elaborates — the *configuration-dependent-operations* family already recorded on [[StaticGuarantee]] and [[TypeStateProgramming]].
