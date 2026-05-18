---
title: "typenum (crate)"
type: entity
tags: [rust, crate, type-level-programming]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# `typenum` (crate)

The **`typenum`** crate (crates.io) provides **type-level numerics** for Rust — unsigned integers, signed integers, and constant arithmetic encoded entirely in the type system. Used by [[HeaplessCrate|`heapless`]] (v0.4.x via `heapless::consts::*`) to encode each collection's capacity directly in its type signature: `Vec<_, U8>` is a `heapless::Vec` of capacity **8**, where `U8` is a `typenum` unit type, not a `const` ([[rust-embedded-book-collections-index]]).

## Why it matters here

`typenum` predates Rust's stable `const generics`. Until `const generics` became stable, type-level numeric parameters had to be encoded as distinct *types* (`U0`, `U1`, …, `U8`, …) so the type checker could carry them through generic bounds. [[HeaplessCrate|`heapless`]]'s fixed-capacity API was the canonical embedded use case: capacity is a compile-time parameter the optimizer must propagate end-to-end, and `typenum` is what made that practical.

## Connections

- [[HeaplessCrate]] — primary consumer in the embedded-Rust corpus.
- [[FixedCapacityCollection]] — the design pattern enabled by `typenum`'s capacity-as-type encoding.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
