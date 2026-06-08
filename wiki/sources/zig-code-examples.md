---
title: "Zig Code Samples (ziglang.org/learn/samples)"
type: source
tags: [zig, examples, code-samples, c-interop, comptime, allocator]
date: 2026-06-07
source_file: https://ziglang.org/learn/samples/
---

## Summary
The official Zig "Samples" page is a curated set of seven small, annotated programs that show off Zig's headline features in working code rather than prose. The samples span a hello-world, calling external system APIs without bindings, runtime memory-leak detection via `std.heap.DebugAllocator`, C interoperability through `@cImport` (raylib and libcurl), a generic queue implemented with comptime type-returning functions, and a FizzBuzz-style ("Zigg Zagg") loop. Each sample doubles as evidence for a concrete language claim — bindingless FFI, no hidden allocations, comptime generics, and "Zig is also a C compiler."

## Key Claims
- **Hello world** demonstrates a minimal program: `main` takes a `std.process.Init`, writes to stdout via the explicit IO interface (`Io.File.stdout().writeStreamingAll(init.io, "hello world!\n")`), and is built with `zig build-exe hello-world.zig`. Illustrates [[Zig]]'s explicit IO and the `!void` [[ErrorUnion|error-union]] return on `main`.
- **Calling external library functions** demonstrates that any system API can be invoked via an `extern` declaration alone — "you do not need library bindings to interface them." The Windows example declares `extern "user32" fn MessageBoxA(...) callconv(.winapi) i32;` and calls it directly. Illustrates [[CInterop|C-ABI interop]] without hand-written bindings.
- **Memory leak detection** demonstrates that `std.heap.DebugAllocator` tracks double-frees and leaks at runtime: the program `gpa.create(u32)`s but never frees, and `defer std.debug.assert(debug_allocator.deinit() == .ok)` then reports the leak (with the allocation-site stack trace) and panics on the failed assertion. Illustrates [[ZigAllocator|explicit allocators]], [[DeferStatement|defer]], and runtime [[MemoryLeak|leak detection]].
- **C interoperability** demonstrates importing a C header with `@cImport(@cInclude("raylib.h"))` and calling C functions (`ray.InitWindow`, `ray.DrawText`) directly, linking libc and raylib via `zig build-exe c-interop.zig -lc -lraylib`. Illustrates [[CInterop]] and `defer`-based C resource cleanup (`defer ray.CloseWindow()`, `defer ray.EndDrawing()`).
- **Zigg Zagg** demonstrates basic control flow — a `while (i <= 16) : (i += 1)` loop with `if`/`else if` chains and `std.log.info` (a FizzBuzz on multiples of 3 → "Zigg", 5 → "Zagg", 15 → "ZiggZagg"). Tongue-in-cheek: "Zig is optimized for coding interviews (not really)."
- **Generic Types** demonstrates that "in Zig types are comptime values and we use functions that return a type to implement generic algorithms and data structures." A `pub fn Queue(comptime Child: type) type` returns a `struct` with a linked-list `Node`, an `std.mem.Allocator` field, and `init`/`enqueue`/`dequeue` methods; the test instantiates `Queue(i32).init(std.testing.allocator)`. Illustrates [[Comptime|comptime generics]] and the allocator-threading convention.
- **Using cURL from Zig** demonstrates a real C-library workflow: `@cImport(@cInclude("curl/curl.h"))`, an arena allocator from `init.arena.allocator()`, `defer cURL.curl_global_cleanup()` / `defer cURL.curl_easy_cleanup(handle)`, `orelse return error.CURLHandleInitFailed` on a nullable handle, and a `callconv(.C)` write callback that appends into a `std.ArrayList(u8)` via `@ptrCast`/`@alignCast`. Illustrates [[CInterop]], [[ErrorUnion]], [[DeferStatement]], and [[ZigAllocator]] together.

## Key Quotes
> "All system API functions can be invoked this way, you do not need library bindings to interface them." — intro to the external-functions sample (`extern "user32" fn MessageBoxA(...)`)

> "Using `std.heap.DebugAllocator` you can track double frees and memory leaks." — intro to the memory-leak sample

> "In Zig types are comptime values and we use functions that return a type to implement generic algorithms and data structures." — intro to the Generic Types sample

> "Zig is *optimized* for coding interviews (not really)." — intro to Zigg Zagg

Representative leak-detection sample:

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

```
error(DebugAllocator): memory address 0x7fc2e3e60000 leaked:
    const u32_ptr = try gpa.create(u32);
thread ... panic: reached unreachable code
```

Representative comptime-generic sample:

```zig
pub fn Queue(comptime Child: type) type {
    return struct {
        const Self = @This();
        const Node = struct {
            data: Child,
            next: ?*Node,
        };
        gpa: std.mem.Allocator,
        start: ?*Node,
        end: ?*Node,

        pub fn init(gpa: std.mem.Allocator) Self { ... }
        pub fn enqueue(self: *Self, value: Child) !void { ... }
        pub fn dequeue(self: *Self) ?Child { ... }
    };
}

test "queue" {
    var int_queue = Queue(i32).init(std.testing.allocator);
    try int_queue.enqueue(25);
    try std.testing.expectEqual(int_queue.dequeue(), 25);
}
```

Representative cURL `@cImport` sample (excerpt):

```zig
const cURL = @cImport({
    @cInclude("curl/curl.h");
});

pub fn main(init: std.process.Init) !void {
    const arena = init.arena.allocator();
    if (cURL.curl_global_init(cURL.CURL_GLOBAL_ALL) != cURL.CURLE_OK)
        return error.CURLGlobalInitFailed;
    defer cURL.curl_global_cleanup();

    const handle = cURL.curl_easy_init() orelse return error.CURLHandleInitFailed;
    defer cURL.curl_easy_cleanup(handle);
    ...
}
```

## Connections
- [[Zig]] — the language all seven samples exercise.
- [[ZigAllocator]] — `DebugAllocator`, arena allocator, and `std.mem.Allocator` threading appear across the leak, generic, and cURL samples.
- [[MemoryLeak]] — the `DebugAllocator` sample is a runtime leak detector for Zig (parallel to Valgrind/ASan in C).
- [[Comptime]] — the `Queue(comptime Child: type) type` sample is the canonical comptime-generic pattern.
- [[CInterop]] — `@cImport`/`@cInclude` (raylib, libcurl), `extern` declarations, `callconv(.C)`/`callconv(.winapi)`, and `-lc -lraylib` linking.
- [[ErrorUnion]] — `!void` mains, `try`, and `orelse return error.X` throughout.
- [[ZigOptional]] — `?*Node` next-pointers and `?Child` dequeue return; `orelse` on the nullable curl handle.
- [[DeferStatement]] — `defer` cleanup in the leak, raylib, and cURL samples; the leak sample defers the leak-check assertion.
- [[ZigSlice]] — `[*:0]const u8` sentinel-terminated pointers and `std.ArrayList(u8)` slices in the FFI samples.
- [[ZigToolchain]] — every sample's shell block uses `zig build-exe` / `zig test`.
- [[CLanguage]] — raylib and libcurl are C libraries imported directly.

## Contradictions
- None. This page is illustrative; its samples corroborate (and concretize) claims already recorded for [[Zig]], [[CInterop]], [[Comptime]], and [[ZigAllocator]] from the prior Zig ingests. One naming note: the page describes the leak detector as `std.heap.DebugAllocator`, while the [[zig-why-zig-vs-rust-d-cpp]] essay and the [[ZigAllocator]] page refer to the same facility as the "debug allocator" / `GeneralPurposeAllocator` lineage — these are the same standard-library leak-detecting allocator, not a contradiction.
