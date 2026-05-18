---
title: "#[alloc_error_handler] attribute"
type: concept
tags: [rust, embedded, no-std, attribute, error-handling]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# `#[alloc_error_handler]`

The **`#[alloc_error_handler]`** attribute (unstable; gated by `#![feature(alloc_error_handler)]`) marks a `fn(Layout) -> !` as the program's handler for [[OutOfMemory|OOM]] conditions surfaced by the [[AllocCrate|`alloc`]] crate. Under [[NoStd|`#![no_std]`]] every program using `alloc` must declare one ([[rust-embedded-book-collections-index]]).

## Signature

```rust
#![feature(alloc_error_handler)]

#[alloc_error_handler]
fn on_oom(_layout: Layout) -> ! {
    // the chapter's stub: break + halt
    cortex_m::asm::bkpt();
    loop {}
}
```

- **`Layout`** is the size + alignment description of the request that failed.
- **`-> !`** because the handler cannot recover and return — it must halt, reset, panic, or break into the debugger.

## Composition with `#[global_allocator]`

Both declarations together form the **mandatory two-piece activation contract** for `alloc` under `no_std` ([[rust-embedded-book-collections-index]]):

1. `#[global_allocator]` on a `static`: implements [[GlobalAlloc|`GlobalAlloc`]] and returns null on OOM.
2. `#[alloc_error_handler]` on a `fn(Layout) -> !`: decides *what to do* when `alloc` sees that null return.

Either one missing is a link-time error.

## Connections

- [[OutOfMemory]] — the failure mode this attribute handles.
- [[GlobalAllocator]] / [[GlobalAlloc]] — the other half of the two-piece contract.
- [[AllocCrate]] — the consumer whose collection methods route OOM here.
- [[PanicHandlerAttribute]] — the structurally analogous `no_std`-only handler attribute.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
