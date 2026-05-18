---
title: "Pin Type-State"
type: concept
tags: [rust, embedded, hal, gpio, typestate, design-pattern]
sources: [rust-embedded-book-design-patterns-hal-gpio]
last_updated: 2026-05-16
---

# Pin Type-State

The application of [[TypeStateProgramming|typestate programming]] to [[GPIO]] **pin configuration** in [[HALCrate|HAL]] APIs — pin state (input / output, plus per-direction sub-mode such as push-pull / open-drain / floating / pull-up / pull-down) is encoded as a **type parameter** on the pin handle, so misuse (e.g. calling `set_high` on a pin currently configured as a floating input) is a **compile error**, not a runtime fault. Named **`C-PIN-STATE`** in the Embedded Rust Book's HAL Checklist ([[rust-embedded-book-design-patterns-hal-gpio]]).

## The two-axis state space

```rust,ignore
mod sealed { pub trait Sealed {} }

pub trait PinState:    sealed::Sealed {}
pub trait OutputState: sealed::Sealed {}
pub trait InputState:  sealed::Sealed {}

pub struct Output<S: OutputState> { _p: PhantomData<S> }
pub struct Input<S: InputState>   { _p: PhantomData<S> }

pub struct PushPull;  impl OutputState for PushPull {}
pub struct OpenDrain; impl OutputState for OpenDrain {}

pub struct Floating;  impl InputState for Floating {}
pub struct PullUp;    impl InputState for PullUp {}
pub struct PullDown;  impl InputState for PullDown {}

pub struct PA1<S: PinState> { _p: PhantomData<S> }
```

Two axes: **direction** (`Input<_>` vs `Output<_>`) and **mode** (`PushPull` / `OpenDrain` for output, `Floating` / `PullUp` / `PullDown` for input). Together, a fully-typed pin is `PA1<Output<PushPull>>` or `PA1<Input<PullUp>>`, etc.

## The required-method API

Per [[rust-embedded-book-design-patterns-hal-gpio]]:

```rust,ignore
pub fn into_input<N: InputState>(self, input: N)   -> PA1<Input<N>>;
pub fn into_output<N: OutputState>(self, output: N) -> PA1<Output<N>>;

pub fn with_input_state<N: InputState, R>(
    &mut self, input: N, f: impl FnOnce(&mut PA1<N>) -> R,
) -> R;

pub fn with_output_state<N: OutputState, R>(
    &mut self, output: N, f: impl FnOnce(&mut PA1<N>) -> R,
) -> R;
```

Two flavors of transition:

| Flavor | Receiver | Effect |
|---|---|---|
| `into_*` | `self` (consumed) | Permanent state change; original pin handle no longer usable |
| `with_*_state` | `&mut self` + closure | Scoped reconfiguration; pin is briefly reconfigured for `f`, then restored |

The `with_*_state` form is the addition over a vanilla [[BuilderPattern|builder-style]] typestate — it solves the common embedded use case *"toggle this output pin as an input for one read, then put it back."*

## The sealed-trait closure

*"Pin state should be bounded by sealed traits. Users of the HAL should have no need to add their own state. The traits can provide HAL-specific methods required to implement the pin state API."* ([[rust-embedded-book-design-patterns-hal-gpio]])

The **sealed-trait pattern** (private supertrait `mod sealed { pub trait Sealed {} }`) prevents downstream crates from adding their own pin states. Two consequences:

1. **The HAL author controls the closed set of states** — exhaustive `match`-like reasoning is possible internally.
2. **The trait can expose HAL-private methods** — `OutputState` and `InputState` can carry implementation-required methods (e.g. "write the right register bits") that aren't part of the public Rust API.

## Composes with type erasure

Pin typestate must survive [[ErasedPin|type erasure]]: *"both erased and non-erased pin types should provide the same API."* A `PA1<Output<PushPull>>` erases via `C-ERASED-PIN` to `PA<Output<PushPull>>` and then `Pin<Output<PushPull>>` — all three forms expose `into_input` / `into_output` / `with_*_state`, and all three are constrained by the same `PinState` / `InputState` / `OutputState` traits.

## Connections

- [[TypeStateProgramming]] — the umbrella pattern; pin typestate is its applied form for [[GPIO]] pins.
- [[rust-embedded-book-design-patterns-hal-gpio]] — the source file that names the pattern as `C-PIN-STATE`.
- [[GPIO]] — the peripheral; pin states encode input/output direction and electrical mode.
- [[ErasedPin]] — the sibling pattern (`C-ERASED-PIN`); typestate rides through both erasure stages.
- [[ZeroSizedType]] — `Output<_>`, `Input<_>`, `PushPull`, `OpenDrain`, etc. are [[ZeroSizedType|ZSTs]]; the whole `PA1<Output<PushPull>>` handle is zero bytes (per `C-ZST-PIN`).
- [[ZeroCostAbstraction]] — the resulting compile-time-checked pin API has no runtime cost.
- [[HALCrate]] — the crate layer this pattern lives in.
- [[BuilderPattern]] — distant cousin; pin typestate adds the **scoped-reconfiguration** `with_*_state` variant that the consume-only builder pattern doesn't have.
- [[rust-embedded-book-static-guarantees-design-contracts]] — the earlier file that introduced multi-axis typestate on an imaginary GPIO API; pin typestate is that pattern's canonical HAL form.
- [[rust-embedded-book-design-patterns-hal-checklist]] — `C-PIN-STATE` is one of the three GPIO-group items in the HAL Checklist.
