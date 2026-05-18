---
title: "GlobalAlloc trait"
type: concept
tags: [rust, embedded, memory, no-std, allocator, trait]
sources: [rust-embedded-book-collections-index]
last_updated: 2026-05-16
---

# `GlobalAlloc` (trait)

**`core::alloc::GlobalAlloc`** is the `unsafe trait` a Rust [[GlobalAllocator|global allocator]] must implement so the [[AllocCrate|`alloc`]] crate can route every heap allocation through it. It is the **type-system contract** that the `#[global_allocator]` attribute requires ([[rust-embedded-book-collections-index]]).

## The shape

Two required methods:

```rust
unsafe trait GlobalAlloc {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8;
    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout);
}
```

- **`alloc`** must return a properly-aligned pointer to at least `layout.size()` bytes of usable memory, or **null** to signal [[OutOfMemory|OOM]]. *"a null pointer signal an Out Of Memory condition"* ([[rust-embedded-book-collections-index]]).
- **`dealloc`** receives the same `ptr` and `layout` previously returned by `alloc` and must return the memory to the allocator. The chapter's [[BumpPointerAllocator|bump-pointer allocator]] makes `dealloc` a no-op (*"this allocator never deallocates memory"*).

## Connections

- [[GlobalAllocator]] — the role; `GlobalAlloc` is the trait that role's `static` must implement.
- [[AllocCrate]] — the crate that depends on a `GlobalAlloc` impl being installed via `#[global_allocator]`.
- [[OutOfMemory]] — signaled by a null return from `alloc`.
- [[BumpPointerAllocator]] — the chapter's worked `GlobalAlloc` implementation.
- [[TheEmbeddedRustBook]] — file 29/44 ([[rust-embedded-book-collections-index]]).
