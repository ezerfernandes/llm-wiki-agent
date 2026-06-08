---
title: "Zig Optional Type (?T)"
type: concept
tags: [zig, optional, null-safety, type-system]
sources: [zig-in-depth-overview]
last_updated: 2026-06-07
---

# Zig Optional Type

Zig replaces null pointers with an **optional type** written `?T`. Per [[zig-in-depth-overview]], null references are "the source of many runtime exceptions" and have been called "the worst mistake of computer science"; Zig's type system removes that failure mode by default. This is a sibling of [[ErrorUnion]]: `?T` models *absence*, while `!T` models *failure*.

## Pointers cannot be null by default

An unadorned [[Zig]] pointer cannot be null. Constructing a `*i32` from address zero is a compile error:

```zig
const foo: *i32 = @ptrFromInt(0x0); // error: pointer type '*i32' does not allow address zero
```

## Making a type optional

Any type becomes optional by prefixing `?`. An optional pointer `?*i32` *can* be null:

```zig
const ptr: ?*i32 = @ptrFromInt(0x0);
assert(ptr == null);
```

## Unwrapping optionals

- **`orelse`** supplies a default (or an early return) when the value is null:
  ```zig
  const ptr = malloc(1234) orelse return null;
  ```
- **`if` capture** runs a block only when the value is present, binding the unwrapped payload:
  ```zig
  if (optional_foo) |foo| {
      doSomethingWithFoo(foo);
  }
  ```
- **`while` capture** loops until an iterator returns null — idiomatic for tokenizers and iterators:
  ```zig
  var it = std.mem.tokenizeAny(u8, msg, " ");
  while (it.next()) |item| {
      std.debug.print("{s}\n", .{item});
  }
  ```

Because the compiler tracks optionality, the unwrapped value inside these captures is a non-optional type — eliminating accidental null dereferences.

## Connections

- [[Zig]] — the language providing optionals.
- [[NullPointer]] — the failure mode optionals are designed to prevent.
- [[ErrorUnion]] — companion construct (`!T` failure vs `?T` absence); shares `if`/`while` capture and `orelse`/`catch` symmetry.
- [[NoHiddenControlFlow]] — null handling is explicit, not hidden.
- [[zig-in-depth-overview]] — source for the optional examples.
