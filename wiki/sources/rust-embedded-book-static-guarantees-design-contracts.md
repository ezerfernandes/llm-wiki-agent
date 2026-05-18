---
title: "The Embedded Rust Book — Design Contracts"
type: source
tags: [rust, embedded, book-chapter, design-by-contract, typestate]
date: 2026-05-16
source_file: raw/book/src/static-guarantees/design-contracts.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Design Contracts

## Summary

File 25/44 of *[[TheEmbeddedRustBook]]* — the **third named sub-section** of the *Static Guarantees* chapter, immediately after [[rust-embedded-book-static-guarantees-state-machines]] (which built the [[GPIO]] state tree + the naive `GpioConfig` API that *"doesn't enforce the design contracts set out by our hardware implementation"*). This file **closes that loop** by presenting two alternative API designs for the same imaginary [[GPIO]] register block and arguing — explicitly through the lens of [[DesignByContract|Design by Contract]] — for the second over the first. Design A is a **runtime-checked** `GpioConfig` whose `set_direction` / `set_input_mode` / `set_output_status` / `get_input_status` methods all return `Result<(), ()>` and each begins with a chain of `if self.periph.read().enable().bit_is_clear() { return Err(()); }` / direction-check guards — design contracts enforced *at runtime, on every call*, *"wast[ing] time and resources"* and producing code that *"will be much less pleasant for the developer to use."* Design B is the same API recast as **[[TypeStateProgramming|typestate]]**: `GpioConfig<ENABLED, DIRECTION, MODE>` parameterized over zero-sized type markers (`Disabled`, `Enabled`, `Input`, `Output`, `HighZ`, `PulledLow`, `PulledHigh`, `DontCare`), with consuming-`self` transition methods (`into_disabled`, `into_enabled_input`, `into_enabled_output`, `into_input_high_z`, `into_input_pull_down`, `into_input_pull_up`) and state-restricted `impl` blocks (`impl GpioConfig<Enabled, Output, DontCare> { fn set_bit(...) }`; `impl<IN_MODE> GpioConfig<Enabled, Input, IN_MODE> { fn bit_is_set(&self) -> bool }`). The chapter's closing section, *Compile Time Functional Safety*, states the payoff: *"this incurs no runtime cost. It is impossible to set an output mode when you have a pin in an input mode."* The illegal-transition example (`output_pin.into_input_pull_down()`) is *"can't do this, output pins don't have this interface!"* — **a compile error, not a runtime `Err(())`**. The chapter is the **promised resolution** of the state-machine motivation from file 24 and the **first fully worked typestate example** in the book (after the abstract `FooBuilder` / `Foo` of file 23).

## Key Claims

- **Design contracts can be enforced two ways.** Runtime (every call checks the current state and returns `Err` on a contract violation) or compile-time (the type system makes the violating call un-typeable). The chapter's framing of the choice is explicitly **[[DesignByContract|Design by Contract]]**.
- **Runtime contract enforcement has measurable cost.** *"Because we need to enforce the restrictions on the hardware, we end up doing a lot of runtime checking which wastes time and resources, and this code will be much less pleasant for the developer to use."* Each `set_*` method on Design A starts with 1-2 register reads + branches before the actual `modify`.
- **Runtime contract enforcement pollutes return types.** `set_direction`, `set_input_mode`, `set_output_status`, `get_input_status` all return `Result<(), ()>` even though the `enable` precondition is a **caller-side** concern, not a hardware failure. `set_enable` is the only contract-free method (no precondition to check).
- **[[TypeStateProgramming|Typestate]] generalizes to three independent state axes.** Design B's `GpioConfig<ENABLED, DIRECTION, MODE>` carries **three type parameters**, one per state-machine axis from the prior file's tree (enabled / direction / input-mode). Unconfigured = `GpioConfig<Disabled, DontCare, DontCare>`. The `DontCare` marker is the **typestate idiom for "this dimension is degenerate in this state"** — input-mode is meaningless when the pin is `Disabled` or `Output`.
- **Transition methods consume `self` and return a *new* type.** `into_disabled(self) -> GpioConfig<Disabled, DontCare, DontCare>`, `into_enabled_input(self) -> GpioConfig<Enabled, Input, HighZ>`, etc. — the **same `FooBuilder.into_foo(self) -> Foo` consuming-`self` recipe** from [[rust-embedded-book-static-guarantees-typestate-programming]], generalized to a full state machine. Sequential transitions chain: `pin.into_enabled_input().into_input_pull_down()`.
- **Generic transitions live on `impl<EN, DIR, IN_MODE>`; state-restricted operations live on monomorphic `impl`s.** The three "anywhere from any state" transitions (`into_disabled`, `into_enabled_input`, `into_enabled_output`) sit on `impl<EN, DIR, IN_MODE> GpioConfig<EN, DIR, IN_MODE>`. The output-only `set_bit` sits on `impl GpioConfig<Enabled, Output, DontCare>`. The input-only `bit_is_set` + input-mode transitions sit on `impl<IN_MODE> GpioConfig<Enabled, Input, IN_MODE>` — partially generic so they accept any input-mode but reject any non-input.
- **Illegal transitions become compile errors, not runtime errors.** The worked example block uses **comment-out lines** to mark the four compile errors: `// pin.into_input_pull_down();` on a `Disabled` pin (not enabled), `// input_pin.set_bit(true);` (no `set_bit` on an input), `// output_pin.into_input_pull_down();` (no input-mode transitions on outputs). Each line is *"Can't do this, [reason]!"* — the type system *refuses to compile*, not *returns `Err`*.
- **Zero runtime cost.** *"Because we are enforcing our design constraints entirely at compile time, this incurs no runtime cost. It is impossible to set an output mode when you have a pin in an input mode. […] there is no runtime penalty due to checking the current state before executing a function."* The type-marker structs (`Disabled`, `Enabled`, `Output`, `Input`, `HighZ`, `PulledLow`, `PulledHigh`, `DontCare`) are **unit structs** — they compile to zero bytes; the entire `GpioConfig<ENABLED, DIRECTION, MODE>` is the same size as the bare `periph: GPIO_CONFIG` handle.
- **No room for consumer error.** *"Because these states are enforced by the type system, there is no longer room for errors by consumers of this interface. If they try to perform an illegal state transition, the code will not compile!"*

## Key Quotes

> "Because we need to enforce the restrictions on the hardware, we end up doing a lot of runtime checking which wastes time and resources, and this code will be much less pleasant for the developer to use." — the verdict on Design A (runtime-checked `Result<(), ()>` API).

> "But what if instead, we used Rust's type system to enforce the state transition rules?" — the chapter's pivot to Design B.

> "Can't do this, pin isn't enabled! […] Can't do this, input pins don't have this interface! […] Can't do this, output pins don't have this interface!" — the three commented-out compile-error sites in the worked example, marking the type-system refusals.

> "Because we are enforcing our design constraints entirely at compile time, this incurs no runtime cost. It is impossible to set an output mode when you have a pin in an input mode. Instead, you must walk through the states by converting it to an output pin, and then setting the output mode. Because of this, there is no runtime penalty due to checking the current state before executing a function." — the *Compile Time Functional Safety* closing.

> "Also, because these states are enforced by the type system, there is no longer room for errors by consumers of this interface. If they try to perform an illegal state transition, the code will not compile!" — the chapter's final sentence; the static-guarantee payoff stated in its strongest form.

## Connections

- [[TheEmbeddedRustBook]] — file 25/44; third named sub-section of the *Static Guarantees* chapter.
- [[rust-embedded-book-static-guarantees-state-machines]] — directly preceding file (24/44); built the [[GPIO]] state tree and showed that the naive `GpioConfig` API *"doesn't enforce the design contracts set out by our hardware implementation."* **This file is the promised resolution** — the same `GpioConfig` recast as `GpioConfig<ENABLED, DIRECTION, MODE>`.
- [[rust-embedded-book-static-guarantees-typestate-programming]] — file 23/44; gave the abstract `FooBuilder.into_foo(self) -> Foo` recipe. This file **scales that recipe** to three type parameters + multiple terminal states + state-restricted `impl` blocks — the first full typestate example in the book.
- [[rust-embedded-book-static-guarantees-index]] — chapter opener (22/44); the *configuration-dependent operations* family it previewed (`set_low` on a floating-input pin is a compile error) is **exactly** what this file mechanizes via `impl GpioConfig<Enabled, Output, DontCare> { fn set_bit(...) }`.
- [[rust-embedded-book-start-registers]] — file 13/44 already showed the *productionized* version of this pattern (`into_af_push_pull::<AF1>()` on a real F3 HAL pin); this file is the **didactic derivation** of why production HAL code looks like that.
- [[DesignByContract]] — the chapter-naming concept; this file is the wiki's primary worked example of contracts enforced at compile time vs at runtime.
- [[TypeStateProgramming]] — the Rust mechanism the chapter applies; this file generalizes the pattern from one type-parameter (file 23's `FooBuilder` → `Foo`) to three (`<ENABLED, DIRECTION, MODE>`) with the `DontCare` degeneracy marker.
- [[FiniteStateMachine]] — the underlying computational model from file 24; this file encodes the GPIO FSM's seven leaf states + transition rules as type-system constraints.
- [[StaticGuarantee]] — the chapter-level framing; this file demonstrates two of the four families (initialization-ordering + configuration-dependent-operations) on the same worked example.
- [[BuilderPattern]] — file 23's named special case of typestate; this file's `into_enabled_input` / `into_enabled_output` / `into_input_pull_down` transitions are **builder-pattern moves applied to a non-builder state machine** — same consuming-`self` mechanism, generalized topology.
- [[GPIO]] — the peripheral; the eight type markers (`Disabled` / `Enabled` / `Input` / `Output` / `HighZ` / `PulledLow` / `PulledHigh` / `DontCare`) encode the GPIO pin-mode taxonomy from file 24's state tree.
- [[Svd2Rust]] — the `periph: GPIO_CONFIG` field in both Design A and Design B is the same [[Svd2Rust|svd2rust]]-generated PAC type from the prior file; the chapter shows that **typestate is a HAL-layer concern layered over an unchanged PAC**.
- [[PeripheralAccessCrate]] — the PAC layer the typestate wrapper sits on top of (`self.periph.modify(|_r, w| w.enable.enabled())` is the same closure idiom from [[rust-embedded-book-start-registers]]).
- [[HALCrate]] — the crate-stack layer where designs like this one *are* the standard idiom (`embedded-hal` GPIO pin mode types follow this exact pattern).

## Contradictions

None with existing wiki content. Strictly additive — supplies the **first fully worked multi-axis typestate example** in the wiki and the **named [[DesignByContract|Design by Contract]] framing** for the compile-time-vs-runtime contract enforcement tradeoff that the prior sub-sections established operationally. The "no runtime cost" claim is consistent with the same claim already on [[StaticGuarantee]] and [[TypeStateProgramming]], elaborated here with a side-by-side runtime-checked / type-checked comparison on the same API surface.
