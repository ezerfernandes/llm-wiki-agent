---
title: "Erased Pin"
type: concept
tags: [rust, embedded, hal, gpio, type-erasure, design-pattern]
sources: [rust-embedded-book-design-patterns-hal-gpio]
last_updated: 2026-05-16
---

# Erased Pin

A [[HALCrate|HAL]]-design pattern for **[[GPIO]] pin types** in which pin identity (and optionally port identity) is **moved from compile time to runtime**, trading compile-time-pin-distinctness for the ability to store heterogeneous pins in a single collection. Named **`C-ERASED-PIN`** in the Embedded Rust Book's HAL Checklist ([[rust-embedded-book-design-patterns-hal-gpio]]).

## The two-stage erasure

```rust,ignore
pub struct PA0;                                  // ZST: one type per physical pin
impl PA0 {
    pub fn erase_pin(self) -> PA { PA { pin: 0 } }
}

pub struct PA { pin: u8 }                        // pin identity now at runtime
impl PA {
    pub fn erase_port(self) -> Pin {
        Pin { port: Port::A, pin: self.pin }
    }
}

pub struct Pin { port: Port, pin: u8 }           // port identity now at runtime
enum Port { A, B, C, D }
```

Three levels of distinctness, three levels of runtime cost:

| Level | Type | Size | Pin distinct at | Port distinct at |
|---|---|---|---|---|
| Statically known | `PA0`, `PA1`, … | 0 bytes (ZST) | compile time | compile time |
| Pin erased | `PA` | 1 byte (`u8`) | runtime | compile time |
| Pin + port erased | `Pin` | ≤2 bytes (port enum + `u8`) | runtime | runtime |

*"These fields can be packed to reduce the memory footprint"* — a port enum (2 bits for 4 ports) and pin index (4 bits for 16 pins) fit comfortably in a single byte.

## Why the trade-off matters

The fully-static form ([[ZeroSizedType|ZST]] per pin, the `C-ZST-PIN` pattern) cannot be stored in a homogeneous collection: `[PA0, PA1, PA2]` is **not a valid Rust array** because the three elements have **different types**. Anywhere a [[GPIO]] application needs a uniform collection — `[Pin; N]`, `Vec<Pin>`, `&dyn` trait objects, runtime-index loops — at least pin erasure is required.

The erasure is **one-way and consuming**: `erase_pin(self)` takes `self` by value, so the original `PA0` cannot be used after erasure. This preserves the [[Singleton|singleton]] discipline — there is still **at most one** Rust value per physical pin, just now in erased form.

## Composes with typestate

Type erasure must **not lose** the [[PinTypeState|pin typestate]]: *"both erased and non-erased pin types should provide the same API"* ([[rust-embedded-book-design-patterns-hal-gpio]]). A `PA1<Output<PushPull>>` erases to `PA<Output<PushPull>>` then to `Pin<Output<PushPull>>` — the typestate parameter rides through both stages. The `into_input` / `into_output` / `with_*_state` methods of `C-PIN-STATE` are required on **all three** pin forms.

## Connections

- [[rust-embedded-book-design-patterns-hal-gpio]] — the source file that introduces the pattern as `C-ERASED-PIN`.
- [[GPIO]] — the peripheral the pattern applies to.
- [[PinTypeState]] — the sibling pattern (`C-PIN-STATE`); typestate must survive erasure.
- [[ZeroSizedType]] — the pre-erasure form is a [[ZeroSizedType|ZST]]; erasure trades zero size for runtime flexibility.
- [[ZeroCostAbstraction]] — fully-static pins are zero-cost; erased pins are *low-cost-runtime* (one or two bytes).
- [[HALCrate]] — the crate layer this pattern lives in.
- [[Singleton]] — preserved through erasure: still one Rust value per physical pin.
- [[rust-embedded-book-design-patterns-hal-checklist]] — `C-ERASED-PIN` is one of the three GPIO-group items in the HAL Checklist.
