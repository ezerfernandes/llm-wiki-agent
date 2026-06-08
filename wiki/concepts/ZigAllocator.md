---
title: "Zig Allocator (Explicit Allocation)"
type: concept
tags: [zig, allocator, memory, no-hidden-allocations, freestanding]
sources: [zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp, zig-code-examples]
last_updated: 2026-06-07
---

# Zig Allocator

In [[Zig]] there are **no hidden memory allocations**: any function that needs to allocate takes an explicit `allocator` parameter. This is a direct consequence of the [[NoHiddenControlFlow]] philosophy and the choice of [[ManualMemoryManagement|manual memory management]]. Per [[zig-in-depth-overview]], "any functions that need to allocate memory accept an allocator parameter," and this discipline applies to the standard library itself. The rationale essay [[zig-why-zig-vs-rust-d-cpp]] sharpens the point at the language level: there is **no `new` keyword** and no language feature that uses a heap allocator (even the array/string concatenation operator works only at compile time, doing no runtime heap allocation), so "the entire concept of the heap is managed by library and application code, not by the language" — *"If you never initialize a heap allocator, you can be confident your program will not heap allocate."*

## Reusability is the real motivation

[[zig-why-zig-vs-rust-d-cpp]] argues the main problem with hidden allocations is that they **destroy the reusability** of code: hidden allocation "unnecessarily limit[s] the number of environments that code would be appropriate to be deployed to," because some use cases require a hard guarantee that control flow and function calls have no allocation side-effect. The essay lists how other languages leak allocations:

- **Go** — `defer` allocates to a function-local stack (which can OOM inside a loop), and ordinary function calls can heap-allocate because goroutine stacks are small and get resized as the call stack deepens.
- **C++** — coroutines allocate heap memory just to be called.
- **Rust** — the main standard library APIs panic on out-of-memory, and the alternate allocator-accepting APIs are "an afterthought" (cites rust-lang/rust#29802). See [[RustStandardLibrary]].
- **Garbage-collected languages** — hide allocations throughout, since the GC also hides the cleanup side.

## Why explicit allocators

Because allocation is never implicit, [[Zig]] programmers must manage their own memory and must handle allocation failure. This is precisely what makes Zig libraries usable in environments that other languages struggle with:

- Desktop applications and low-latency servers
- Databases and operating-system kernels
- Embedded devices and real-time software (live performances, airplanes, pacemakers)
- WebAssembly plugins in browsers
- As a C-ABI library callable from other languages

Crucially, because the standard library threads allocators through its APIs rather than calling a global allocator, **the Zig standard library can be used even on the freestanding target** (no OS, no libc).

## Allocation patterns

Allocator methods such as `allocator.create(T)`, `allocator.destroy(ptr)`, `allocator.free(slice)`, and helpers like `std.fmt.allocPrint(allocator, ...)` are used together with [[DeferStatement|defer/errdefer]] to guarantee cleanup. Allocation can fail, so allocating calls return [[ErrorUnion|error unions]] handled with `try`:

```zig
const device = try allocator.create(Device);
errdefer allocator.destroy(device);
```

The standard library's `DebugAllocator` captures stack traces at allocation sites so it can report memory leaks and double frees; [[zig-why-zig-vs-rust-d-cpp]] notes the debug allocator "maintains memory safety in the face of use-after-free and double-free" and automatically prints leak stack traces. An **arena allocator** lets you bundle any number of allocations into one and free them all at once instead of tracking each independently, and special-purpose allocators can be swapped in to tune performance or memory usage per application. Because the std library threads allocators through its APIs rather than calling a global allocator, structures like `std.ArrayList` and `std.AutoHashMap` work even for **bare-metal / freestanding** programming.

### Worked leak-detection example

The official [[zig-code-examples|samples page]] gives a runnable demonstration: instantiate a `std.heap.DebugAllocator`, `defer` an assertion that its `deinit()` returns `.ok` (no leaks), allocate, and then deliberately forget to free:

```zig
const std = @import("std");

pub fn main() !void {
    var debug_allocator = std.heap.DebugAllocator(.{}){};
    defer std.debug.assert(debug_allocator.deinit() == .ok);

    const gpa = debug_allocator.allocator();

    const u32_ptr = try gpa.create(u32);
    _ = u32_ptr; // silences unused variable error

    // oops I forgot to free!
}
```

At runtime the allocator prints the leaked address together with the source line where the allocation happened (`const u32_ptr = try gpa.create(u32);`), and the `deinit() == .ok` assertion then fails, panicking the program — making leaks a loud, traced runtime failure rather than a silent degradation. The same samples page also shows the **arena** path (`init.arena.allocator()`) feeding a `std.ArrayList(u8)` in its cURL example, where one `arena.deinit()` reclaims every allocation at once.

### Allocator-threading in generic data structures

A generic data structure simply stores an `std.mem.Allocator` field and uses it for node allocation. The samples page's generic `Queue` keeps `gpa: std.mem.Allocator`, calls `self.gpa.create(Node)` in `enqueue`, and `defer self.gpa.destroy(start)` in `dequeue` — the same explicit-allocator discipline applied inside a comptime-generic type (see [[Comptime]]).

## Connections

- [[Zig]] — the language enforcing explicit allocation.
- [[NoHiddenControlFlow]] — "no hidden allocations" is part of this philosophy.
- [[ManualMemoryManagement]] — the broader memory model.
- [[DeferStatement]] — defer/errdefer free allocations reliably.
- [[ErrorUnion]] — allocation failure surfaces as an error union.
- [[MemoryAllocation]] — general allocation background.
- [[DynamicMemoryAllocation]] — heap allocation that allocators provide.
- [[RustStandardLibrary]] — contrasted: Rust std APIs panic on OOM; allocator APIs are an afterthought.
- [[Comptime]] — generic data structures thread an `std.mem.Allocator` field through comptime type-returning functions.
- [[zig-in-depth-overview]] — source for the allocator-parameter convention.
- [[zig-why-zig-vs-rust-d-cpp]] — source for the no-`new`-keyword framing, reusability argument, and cross-language counterexamples.
- [[zig-code-examples]] — source for the runnable `DebugAllocator` leak-detection and arena examples.
