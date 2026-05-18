---
title: "Zero Sized Type"
type: concept
tags: [rust, type-system, compile-time, zero-cost, marker-type]
sources: [rust-embedded-book-static-guarantees-zero-cost-abstractions]
last_updated: 2026-05-16
---

# Zero Sized Type

A Rust type with **`size_of::<T>() == 0`** — *"structures defined like this … contain no actual data. Although these types act 'real' at compile time — you can copy them, move them, take references to them, etc., however the optimizer will completely strip them away."* ([[rust-embedded-book-static-guarantees-zero-cost-abstractions]]). Abbreviated **ZST** in the Rust community.

The mechanism that makes typestate a [[ZeroCostAbstraction|zero-cost abstraction]]: state-marker structs encode information at the type level while taking zero bytes at runtime.

## Canonical form: the unit struct

```rust,ignore
struct Enabled;
struct Input;
struct PulledHigh;
```

Each is a **unit struct** — no fields, no data. `core::mem::size_of` reports `0`:

```rust,ignore
let _ = size_of::<Enabled>();    // == 0
let _ = size_of::<Input>();      // == 0
let _ = size_of::<PulledHigh>(); // == 0
```

## The compile-time / runtime split

ZSTs are real types to the type checker but invisible to the optimizer:

| At compile time | At runtime |
|---|---|
| Distinct types (`Enabled` ≠ `Input`) | Zero bytes |
| Can be copied, moved, referenced | Field initializations compile out |
| Participate in generic monomorphization | No memory traffic |
| Drive `impl` selection / overload resolution | Strip during optimization |

A struct field of ZST type adds nothing to the parent type's size. A `GpioConfig { periph, enabled: Enabled, direction: Input, mode: PulledHigh }` whose every field is a ZST is itself zero bytes.

## Compositional property

> *"In general, these abstractions may be nested as deeply as you would like. As long as all components used are zero sized types, the whole structure will not exist at runtime."* ([[rust-embedded-book-static-guarantees-zero-cost-abstractions]])

**ZST-of-ZST is a ZST.** Arbitrary nesting preserves zero size; this is what lets multi-axis typestate handles like `GpioConfig<ENABLED, DIRECTION, MODE>` carry three independent state parameters with no runtime cost.

## Use cases in the wiki's embedded-Rust corpus

- **State markers** for [[TypeStateProgramming|typestate]] — `Enabled`, `Input`, `Output`, `HighZ`, `PulledLow`, `PulledHigh`, `DontCare` (from [[rust-embedded-book-static-guarantees-design-contracts]]).
- **Builder-pattern terminal markers** — distinguishing `FooBuilder` from `Foo` even when no extra data is needed (see [[BuilderPattern]]).
- **PAC register-block proxies** — [[Svd2Rust|svd2rust]]-generated register-block handles are ZST proxies over raw addresses (which is why `size_of::<GpioConfig<Enabled, Input, PulledHigh>>()` is `0` even though it has a `periph` field).
- **Singleton tokens** — exclusive-ownership tokens that compile to zero bytes (see [[Singleton]]).

## Why ZSTs make zero-cost typestate possible

Without ZSTs, a typestate machine could *still* work (you could pay a byte or two per state marker) — but the abstraction would not be **zero-cost**: each `GpioConfig` would carry a `u8` discriminant per state axis. The ZST property is the mechanical reason the [[TypeStateProgramming|typestate]] *"All with no run-time cost!"* claim holds: monomorphization specializes the type, the optimizer strips the ZST fields, and the resulting machine code is identical to a direct register-bashing implementation. *"Renders to the same machine code as a direct register access."*

## Connections

- [[ZeroCostAbstraction]] — the **umbrella concept**; ZSTs are the mechanism that delivers zero-cost typestate.
- [[TypeStateProgramming]] — the **primary use case** in the embedded-Rust corpus; state markers are ZSTs.
- [[BuilderPattern]] — the simplest typestate, where the terminal marker (`Foo` vs `FooBuilder`) can be a ZST when no extra data is needed.
- [[RustLanguage]] — the language whose **unit structs** and **monomorphization** combine to produce zero-sized types.
- [[Svd2Rust]] / [[PeripheralAccessCrate]] — generated PAC register-block proxies are themselves ZSTs.
- [[Singleton]] — peripheral handles can be ZST tokens whose **exclusive-ownership invariant** is enforced by `take()` at runtime, with no per-token byte cost.
