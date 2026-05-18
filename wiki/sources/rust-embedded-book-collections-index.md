---
title: "The Embedded Rust Book — Collections"
type: source
tags: [rust, embedded, book-chapter, collections]
date: 2026-05-16
source_file: raw/book/src/collections/index.md
last_updated: 2026-05-16
---

# The Embedded Rust Book — Collections

## Summary

File 29/44 of *[[TheEmbeddedRustBook]]* — **single-file chapter** (the *Collections* chapter has no sub-files). Operationalizes the opt-in [[HeapAllocation|heap]] recipe sketched in [[rust-embedded-book-intro-no-std]] and contrasts it head-to-head with [[HeaplessCrate|`heapless`]]'s **fixed-capacity, stack-allocated** alternative. The chapter has three parts. **Part 1 — Using [[AllocCrate|`alloc`]]**: under [[NoStd|`#![no_std]`]] the `std` collections (`Vec`, `String`, `HashMap`) are unavailable, but their *implementations* live in the [[AllocCrate|`alloc`]] crate that ships with the compiler (`#![feature(alloc)]; extern crate alloc; use alloc::vec::Vec;` — no `Cargo.toml` entry required). Wiring `alloc` requires two declarations: (a) a [[GlobalAllocator|`#[global_allocator]`]] `static` implementing the [[GlobalAlloc|`GlobalAlloc`]] trait — the chapter implements a minimal **bump-pointer allocator** over a fixed RAM window `[0x2000_0100, 0x2000_0200]`, wrapping `head` in `UnsafeCell` for interior mutability, declaring `unsafe impl Sync`, and using `cortex_m::interrupt::free` ([[CriticalSection|critical section]] from [[CortexMCrate|`cortex-m`]]) to make `alloc` interrupt-safe on single-core; on OOM it returns a null `*mut u8`, and `dealloc` is a no-op (*"this allocator never deallocates memory"*) — explicitly *"single core systems"* only, with a strong recommendation to use a battle-tested allocator from crates.io in real code. (b) An [[AllocErrorHandlerAttribute|`#[alloc_error_handler]`]] `fn(Layout) -> !` (unstable feature `alloc_error_handler`) — the chapter's stub calls `cortex_m::asm::bkpt()` then `loop {}`. Once both are in place, `Vec::new() + push + pop` work *exactly* as in `std`. **Part 2 — Using [[HeaplessCrate|`heapless`]]**: no setup at all — just `use heapless::Vec; use heapless::consts::*;` and `Vec<_, U8>::new()` allocates **on the stack** with a capacity baked into the type signature via [[Typenum|`typenum`]] type-level unsigned ints (v0.4.x). All capacity-changing methods return `Result` (e.g. `xs.push(42).unwrap()`); collections **never reallocate**; can also live in `static` variables or on the heap (`Box<Vec<_, _>>`). **Part 3 — Trade-offs** across four axes: (1) **[[OutOfMemory|OOM]] & error handling** — `alloc::Vec::push` can implicitly OOM at any growth site (the *location of failure* may not match the *cause* because of [[MemoryFragmentation|fragmentation]] / leaks elsewhere; *"memory leaks are possible in safe Rust"*); `try_reserve` exists but is opt-in. `heapless` makes every failure local and explicit via `Result`; with exclusive `heapless` use, OOM becomes *impossible*. (2) **Memory usage** — `alloc` capacities change at runtime (`shrink_to_fit` is allocator-discretionary), and [[MemoryFragmentation|fragmentation]] can inflate apparent usage; `heapless` stored in `static`s + a capped stack lets the **linker statically detect** RAM overcommit, and stack-allocated fixed-capacity collections are visible to `-Z emit-stack-sizes` / `stack-sizes` tooling. Downside: fixed-capacity collections can't be shrunk, so **load factor** (size / capacity) is lower. (3) **[[WorstCaseExecutionTime|WCET]]** — `alloc::Vec::push` WCET depends on allocator + runtime capacity (the realloc tail); `heapless::Vec::push` is **constant time**. (4) **Ease of use** — `alloc` needs global allocator setup but offers the familiar `std` API; `heapless` needs no setup but forces per-instance capacity choice and adds *explicit error handling* that *"some developers may feel … is excessive or too cumbersome."*

## Key Claims

- **`std` collections live in `alloc` under `no_std`.** *"As `core` is, by definition, free of memory allocations these implementations are not available there, but they can be found in the `alloc` crate that's shipped with the compiler."* The [[AllocCrate|`alloc`]] crate is part of the standard Rust distribution — `use` it without declaring it in `Cargo.toml`.
- **Two declarations needed to use `alloc`.** A `#[global_allocator]` static that implements [[GlobalAlloc|`GlobalAlloc`]], **plus** an `#[alloc_error_handler]` `fn(Layout) -> !` to handle [[OutOfMemory|OOM]] (unstable `alloc_error_handler` feature).
- **The chapter's bump-pointer allocator is illustrative, not production-grade.** *"For completeness and to keep this section as self-contained as possible we'll implement a simple bump pointer allocator … However, we *strongly* suggest you use a battle tested allocator from crates.io in your program instead of this allocator."* The example: `head: UnsafeCell<usize>` + `end: usize` over `[0x2000_0100, 0x2000_0200]`, `unsafe impl Sync`, alignment-rounded `start = (*head + align - 1) & !(align - 1)`, returns `ptr::null_mut()` on OOM, `dealloc` is a no-op.
- **`cortex_m::interrupt::free` is what makes `alloc` interrupt-safe** on the chapter's single-core target — *"a critical section that makes our allocator safe to use from within interrupts."* The same primitive used in [[rust-embedded-book-concurrency-index]] for [[CriticalSection|critical sections]].
- **OOM is signaled by a null pointer.** *"a null pointer signal an Out Of Memory condition."*
- **`heapless` is a fixed-capacity, no-allocator alternative.** *"`heapless` requires no setup as its collections don't depend on a global memory allocator."* Capacity is baked into the type signature via [[Typenum|`typenum`]] (`Vec<_, U8>`); all insertion methods return `Result`; collections **never reallocate**.
- **`heapless` v0.4.x stores elements inline.** *"`let x = heapless::Vec::new();` will allocate the collection on the stack, but it's also possible to allocate the collection on a `static` variable, or even on the heap (`Box<Vec<_, _>>`)."*
- **OOM with heap allocators is implicit and non-local.** *"all `alloc::Vec.push` invocations can potentially generate an OOM condition. Thus some operations can *implicitly* fail. … the observed location of failure may *not* match with the location of the cause of the problem. For example, even `vec.reserve(1)` can trigger an OOM if the allocator is nearly exhausted because some other collection was leaking memory (memory leaks are possible in safe Rust)."* `try_reserve` exists as a proactive check.
- **Heap memory accounting is hard to reason about.** Runtime capacity changes implicitly, `shrink_to_fit` is allocator-discretionary, and [[MemoryFragmentation|fragmentation]] can increase *apparent* memory usage. Fixed-capacity collections in `static`s + a capped stack let the **linker** detect overcommit at link time.
- **Stack-allocated `heapless` collections are visible to stack-sizing tools.** *"fixed capacity collections allocated on the stack will be reported by `-Z emit-stack-sizes` flag which means that tools that analyze stack usage (like `stack-sizes`) will include them in their analysis."*
- **Fixed capacity ⇒ lower load factor.** *"fixed capacity collections can *not* be shrunk which can result in lower load factors (the ratio between the size of the collection and its capacity) than what relocatable collections can achieve."*
- **WCET split is sharp.** `alloc::Vec::push` worst case includes the realloc tail and depends on allocator + runtime capacity. `heapless::Vec::push` *"executes in constant time"* — making `heapless` the right choice for hard real-time / [[WorstCaseExecutionTime|WCET]]-sensitive code.
- **Ease-of-use trade is mirrored**: `alloc` = setup cost + familiar API; `heapless` = no setup + per-instance capacity choice + explicit `Result` everywhere.

## Key Quotes

> "Eventually you'll want to use dynamic data structures (AKA collections) in your program. `std` provides a set of common collections: `Vec`, `String`, `HashMap`, etc. All the collections implemented in `std` use a global dynamic memory allocator (AKA the heap)." — the chapter's framing.

> "As `core` is, by definition, free of memory allocations these implementations are not available there, but they can be found in the `alloc` crate that's shipped with the compiler." — the load-bearing fact that resolves the [[HeapAllocation]] forward reference from [[rust-embedded-book-intro-no-std]].

> "To be able to use any collection you'll first need use the `global_allocator` attribute to declare the global allocator your program will use. It's required that the allocator you select implements the `GlobalAlloc` trait." — the [[GlobalAllocator]] entry contract.

> "For completeness and to keep this section as self-contained as possible we'll implement a simple bump pointer allocator and use that as the global allocator. However, we *strongly* suggest you use a battle tested allocator from crates.io in your program instead of this allocator." — the educational-vs-production caveat.

> "Apart from selecting a global allocator the user will also have to define how Out Of Memory (OOM) errors are handled using the *unstable* `alloc_error_handler` attribute." — the second mandatory declaration.

> "`heapless` requires no setup as its collections don't depend on a global memory allocator. Just `use` its collections and proceed to instantiate them." — the elevator pitch.

> "You have to declare upfront the capacity of the collection. `heapless` collections never reallocate and have fixed capacities; this capacity is part of the type signature of the collection." — the fundamental type-level capacity property.

> "With heap allocations Out Of Memory is always a possibility and can occur in any place where a collection may need to grow … some operations can *implicitly* fail. … If you exclusively use `heapless` collections and you don't use a memory allocator for anything else then an OOM condition is impossible." — the OOM-as-implicit-vs-impossible dichotomy.

> "`heapless::Vec.push` executes in constant time." — the WCET clincher.

## Connections

- [[TheEmbeddedRustBook]] — file 29/44.
- [[rust-embedded-book-intro-no-std]] — the chapter that *forecast* this one ("opt-in heap recipe: `alloc` crate + global allocator e.g. `alloc-cortex-m`"); this chapter delivers the recipe.
- [[NoStd]] — the regime that removes the default heap and makes this chapter necessary.
- [[HeapAllocation]] — the underlying memory-allocation concept; this chapter is its embedded operationalization.
- [[RustCoreLibrary]] / [[RustStandardLibrary]] — `core` lacks allocator → no collections; `std` has both → `Vec`/`String`/`HashMap` available.
- [[AllocCrate]] — **introduced** as the heap-collections crate.
- [[HeaplessCrate]] — **introduced** as the fixed-capacity, no-allocator alternative.
- [[GlobalAllocator]] — **introduced** concept of the `#[global_allocator]` attribute + [[GlobalAlloc|`GlobalAlloc`]] trait contract.
- [[OutOfMemory]] — **introduced** as both the runtime condition (null pointer from `alloc`) and the user-defined `#[alloc_error_handler]`.
- [[FixedCapacityCollection]] — **introduced** as the design pattern `heapless` realizes.
- [[BumpPointerAllocator]] — **introduced** as the chapter's illustrative single-core allocator implementation.
- [[Typenum]] — **introduced** entity: the crates.io crate `heapless` uses for type-level unsigned ints (`U8`).
- [[WorstCaseExecutionTime]] — **introduced** as the timing axis where `heapless` dominates.
- [[MemoryFragmentation]] — **introduced** as the cause of *implicit, non-local* OOM in `alloc`.
- [[CriticalSection]] / [[CortexMCrate]] — the `cortex_m::interrupt::free` primitive that makes the chapter's bump allocator interrupt-safe; same primitive load-bearing in [[rust-embedded-book-concurrency-index]].
- [[UnsafeCell]] / [[InteriorMutability]] — used in the bump allocator (`head: UnsafeCell<usize>` + `unsafe impl Sync`); the [[rust-embedded-book-concurrency-index]] interior-mutability stack reused here for a non-concurrency reason.
- [[Atomic]] / [[Mutex]] — the [[rust-embedded-book-concurrency-index]] alternatives to `interrupt::free` that a multi-core allocator would have to use instead.

## Contradictions

- None with existing wiki content. This chapter **completes** the opt-in heap recipe forward-referenced by [[rust-embedded-book-intro-no-std]] (which named `alloc-cortex-m` as the typical allocator) and reuses the [[CriticalSection]] / [[UnsafeCell]] / `unsafe impl Sync` primitives just introduced in [[rust-embedded-book-concurrency-index]] in a non-concurrency context (allocator-as-shared-mutable-state).
