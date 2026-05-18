---
title: "heapless (crate)"
type: entity
tags: [rust, embedded, crate, no-std, collections]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# `heapless` (crate)

The **`heapless`** crate (crates.io) provides **fixed-capacity** Rust collections — `Vec`, `String`, `HashMap`, queue / ring-buffer types — that **do not require a global memory allocator** ([[rust-embedded-book-collections-index]]). The canonical alternative to [[AllocCrate|`alloc`]] in [[NoStd|`#![no_std]`]] firmware.

## The shape

```rust
use heapless::Vec;
use heapless::consts::*;       // v0.4.x — typenum re-exports

let mut xs: Vec<_, U8> = Vec::new();
xs.push(42).unwrap();           // returns Result — capacity may be exhausted
```

Two distinguishing features ([[rust-embedded-book-collections-index]]):

- **Capacity is part of the type signature**, expressed as a [[Typenum|`typenum`]] type-level unsigned int (`U8` here). Collections **never reallocate**.
- **Every capacity-changing method returns `Result`** — `push`, `extend_from_slice`, etc. all surface "would overflow" as an explicit, local failure rather than the implicit, non-local [[OutOfMemory|OOM]] of [[AllocCrate|`alloc`]].

As of v0.4.x all `heapless` collections store elements **inline**, so `heapless::Vec::new()` allocates on the stack — though `static` and `Box<Vec<_, _>>` placements are also supported.

## Why embedded developers reach for it

- **No global allocator setup.** Drop in and use.
- **OOM is impossible** if it's the only allocation strategy in the program (no allocator → no OOM site).
- **Constant-time `push`** — never reallocates. Critical for [[WorstCaseExecutionTime|WCET]]-sensitive / hard real-time code.
- **Visible to stack-sizing tools** (`-Z emit-stack-sizes` / the `stack-sizes` crate).
- **Linker-detectable RAM overcommit** when stored in `static` variables alongside a capped stack.

## Trade-offs vs `alloc`

- Capacity must be picked per instance — no `shrink_to_fit`, leading to potentially lower load factor (size / capacity).
- API mimics `alloc`/`std` but is not identical due to the pervasive `Result` returns — *"some developers may feel the explicit error handling is excessive or too cumbersome"* ([[rust-embedded-book-collections-index]]).

## Connections

- [[AllocCrate]] — the heap-backed alternative.
- [[FixedCapacityCollection]] — the design pattern `heapless` realizes.
- [[Typenum]] — the type-level-numerics dependency that encodes capacity.
- [[OutOfMemory]] — the failure mode `heapless` makes impossible / local.
- [[WorstCaseExecutionTime]] — the timing-determinism win.
- [[NoStd]] — the regime where `heapless` is most often chosen.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
