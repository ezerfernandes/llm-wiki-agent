---
title: "Comptime (Zig Compile-Time Execution)"
type: concept
tags: [zig, comptime, metaprogramming, generics, reflection, compile-time]
sources: [zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp, zig-code-examples]
last_updated: 2026-06-07
---

# Comptime

`comptime` is [[Zig]]'s mechanism for compile-time code execution, reflection, and generics. It replaces the preprocessor, macros, and templates found in other languages while preserving the [[NoHiddenControlFlow]] philosophy — metaprogramming happens with the same Zig language, not a separate macro dialect. Per [[zig-in-depth-overview]], it is the feature that lets Zig keep a tiny grammar yet still implement things like formatted printing entirely in user-space Zig.

## Types are values

In Zig, **types are first-class values that must be known at compile time**:

```zig
const std = @import("std");
const assert = std.debug.assert;

test "types are values" {
    const T1 = u8;
    const T2 = bool;
    assert(T1 != T2);

    const x: T2 = true;
    assert(x);
}
```

## Generics = a function that returns a type

Because types are values, generics need no special syntax: a generic data structure is simply a function that takes a `comptime` type parameter and returns a `type`.

```zig
fn List(comptime T: type) type {
    return struct {
        items: []T,
        len: usize,
    };
}
```

`List(i32)` is then used as an ordinary type. This subsumes what other Zig material may call "comptime generics" — there is no separate generics feature, only compile-time evaluation of type-returning functions.

### Worked example: a generic queue

The official [[zig-code-examples|samples page]] makes this concrete with a generic linked-list queue. `Queue` is a function of a `comptime Child: type` that returns an anonymous `struct`; the struct closes over `Child` for its node payload and uses `@This()` to name its own type:

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
        pub fn enqueue(self: *Self, value: Child) !void {
            const node = try self.gpa.create(Node);
            node.* = .{ .data = value, .next = null };
            ...
        }
        pub fn dequeue(self: *Self) ?Child { ... }
    };
}

test "queue" {
    var int_queue = Queue(i32).init(std.testing.allocator);
    try int_queue.enqueue(25);
    try std.testing.expectEqual(int_queue.dequeue(), 25);
}
```

`Queue(i32)` instantiates the type at compile time; the same function would produce `Queue(f64)`, `Queue(MyStruct)`, etc. Note how the generic type still threads an explicit `std.mem.Allocator` (see [[ZigAllocator]]) and uses [[ZigOptional|optional]] `?*Node` / `?Child` and an [[ErrorUnion|`!void`]] `enqueue` — comptime generics compose with the rest of Zig's explicit semantics, not a separate generics dialect.

## Compile-time evaluation

Functions and blocks can be evaluated at compile time. In some contexts (e.g. global variable initializers, array length expressions) this is implicit; otherwise it is requested explicitly with the `comptime` keyword. This composes powerfully with assertions:

```zig
fn fibonacci(x: u32) u32 {
    if (x <= 1) return x;
    return fibonacci(x - 1) + fibonacci(x - 2);
}

test "compile-time evaluation" {
    var array: [fibonacci(6)]i32 = undefined;
    @memset(&array, 42);
    comptime {
        assert(array.len == 12345); // compile error: assertion fails at comptime
    }
}
```

Top-level declarations are order-independent and lazily analyzed; the initialization value of a global is evaluated at compile time.

## Reflection

The `@typeInfo` builtin provides reflection over types, and `@typeName` returns a type's name. Iterating a struct's fields with `inline for` over `@typeInfo(T).@"struct".fields` is how the standard library implements formatted printing in Zig itself:

```zig
fn printInfoAboutStruct(comptime T: type) void {
    const info = @typeInfo(T);
    inline for (info.@"struct".fields) |field| {
        std.debug.print("{s} has a field called {s} with type {s}\n", .{
            @typeName(T), field.name, @typeName(field.type),
        });
    }
}
```

The overview contrasts this with C (compile errors for `printf` hard-coded into the compiler) and [[RustLanguage|Rust]] (format macro hard-coded into the compiler).

## Simplicity through comptime, not macros

The rationale essay [[zig-why-zig-vs-rust-d-cpp]] frames comptime as the answer to a *simplicity* problem: C++, Rust, and D have so many features that one ends up "debugging one's knowledge of the programming language instead of debugging the application itself." Zig instead "has no macros yet is still powerful enough to express complex programs in a clear, non-repetitive way." The cited proof is `format!`: even Rust special-cases it inside the compiler, whereas in Zig "the equivalent function is implemented in the standard library with no special case code in the compiler" — exactly because comptime + reflection are expressive enough to write it in user-space Zig.

## Connections

- [[Zig]] — the language providing `comptime`.
- [[NoHiddenControlFlow]] — comptime replaces macros/preprocessor without hidden control flow.
- [[Metaprogramming]] — comptime is Zig's approach to metaprogramming.
- [[ErrorUnion]] — error sets are also resolved at compile time.
- [[RustLanguage]] — contrasted on hard-coded format macros.
- [[ZigAllocator]] — generic types thread an explicit allocator (the `Queue` keeps `gpa: std.mem.Allocator`).
- [[ZigOptional]] — the queue's `?*Node` / `?Child` show comptime generics composing with optionals.
- [[zig-in-depth-overview]] — source for the comptime/reflection/generics examples.
- [[zig-why-zig-vs-rust-d-cpp]] — source for the simplicity/no-macros argument and the `format!`-in-std-lib contrast.
- [[zig-code-examples]] — source for the runnable generic `Queue(comptime Child: type)` example.
