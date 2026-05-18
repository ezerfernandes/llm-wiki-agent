---
title: "panic-abort"
type: entity
tags: [rust, embedded, crate, panic-handler, no-std]
sources: [rust-embedded-book-start-panicking]
last_updated: 2026-05-16
---

# panic-abort

**Minimal Rust crate providing a [[PanicHandlerAttribute|`#[panic_handler]`]] that executes the target's abort instruction** (on [[ARMCortexM|Cortex-M]] this is the undefined-instruction trap `UDF`). One of the four pre-packaged panic-handler crates surveyed by [[rust-embedded-book-start-panicking|chapter 15 of *The Embedded Rust Book*]].

```toml
panic-abort = "..."
```

```rust
use panic_abort as _;
```

## Why pick it

The chapter's canonical use case is the **release profile** in a profile-conditional panic-handler swap:

```rust
#[cfg(debug_assertions)]
use panic_halt as _;          // dev: keep rust_begin_unwind breakpointable
#[cfg(not(debug_assertions))]
use panic_abort as _;         // release: minimize binary size
```

`panic-abort` elides the formatting / looping / logging code paths that the other panic-handler crates pull in, producing the **smallest final ELF**. The cost is post-mortem opacity: there is no panic message anywhere, and the abort trap may or may not produce a clean fault frame depending on how the system handles `UDF`.

## Connections

- [[PanicHandlerAttribute]] — the attribute the crate implements.
- [[PanicInfo]] — the argument the crate's handler ignores before aborting.
- [[NoStd]] — the regime that requires an explicit panic handler.
- [[PanicHaltCrate]] — the dev-profile sibling; halts instead of aborting.
- [[PanicItmCrate]] / [[PanicSemihostingCrate]] / [[PanicProbeCrate]] — the verbose siblings that log before halting.
- [[ARMCortexM]] — the canonical target; the abort instruction maps to a `UDF` fault.
- [[TheEmbeddedRustBook]] — surveyed in [[rust-embedded-book-start-panicking]].
