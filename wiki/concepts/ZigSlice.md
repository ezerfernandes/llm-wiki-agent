---
title: "Zig Slice ([]T)"
type: concept
tags: [zig, slice, pointer, type-system, memory-safety]
sources: [zig-in-depth-overview]
last_updated: 2026-06-07
---

# Zig Slice

A *slice* in [[Zig]] is a pointer-plus-length view into a contiguous sequence of elements, written `[]T` (mutable) or `[]const T` (immutable). Slices appear throughout [[zig-in-depth-overview]] as the idiomatic way to pass arrays, buffers, and strings without losing length information — a string literal, for example, has type `[]const u8`.

## Usage in the overview

- A generic list stores its backing storage as a slice field, taken from a fixed array with `&buffer`:
  ```zig
  fn List(comptime T: type) type {
      return struct {
          items: []T,
          len: usize,
      };
  }
  // ...
  var buffer: [10]i32 = undefined;
  var list: List(i32) = .{ .items = &buffer, .len = 0 };
  ```
- Function parameters take slices of bytes for strings/buffers:
  ```zig
  fn parseInt(buf: []const u8, radix: u8) !u64 { ... }
  ```
- A struct field can hold borrowed or allocated bytes as a slice: `name: []const u8` / `name: []u8`.

Because a slice carries its `len`, indexing it is subject to Zig's runtime bounds-safety checks in safety-enabled build modes (crashing rather than invoking [[UndefinedBehavior]] / [[BufferOverflow]]). Slicing syntax (`buffer[0..4]`, `buffer[4..]`) produces sub-slices, as seen in the stack-trace example.

## Connections

- [[Zig]] — the language providing slices.
- [[ZigAllocator]] — allocated buffers are handed back and freed as slices.
- [[BufferOverflow]] — slice length tracking + bounds checks guard against this.
- [[UndefinedBehavior]] — out-of-bounds access is checked, not silent, in safe builds.
- [[Comptime]] — slice element types can be comptime-generic (`[]T`).
- [[zig-in-depth-overview]] — source for the slice examples.
