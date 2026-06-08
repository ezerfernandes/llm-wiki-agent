---
title: "Error Union (Zig Error Handling)"
type: concept
tags: [zig, error-handling, error-union, try, catch, error-sets]
sources: [zig-in-depth-overview]
last_updated: 2026-06-07
---

# Error Union

Zig's error handling treats **errors as values that may not be ignored**, expressed through *error union* types written `!T` (an error set unioned with a payload type `T`). Per [[zig-in-depth-overview]], this is "a fresh take on error handling" that avoids exceptions and the hidden control flow they imply (see [[NoHiddenControlFlow]]).

## Errors are values and cannot be ignored

Calling a fallible function and discarding the result is a compile error — the [[Zig]] compiler forces you to acknowledge the error union.

## try and catch

- **`catch`** handles an error, optionally binding it: `expr catch |err| { ... }`, or supplying a fallback value/branch.
- **`try expr`** is shorthand for `expr catch |err| return err` — propagate the error up to the caller.

```zig
const file = try Io.Dir.cwd().openFile(io, "does_not_exist/foo.txt", .{});
defer file.close(io);
```

```zig
const file = Io.Dir.cwd().openFile(io, "does_not_exist/foo.txt", .{}) catch |err| label: {
    std.debug.print("unable to open file: {}\n", .{err});
    break :label .stderr();
};
```

## switch forces exhaustive handling

Using `switch` on an error value makes the compiler require that all possible error cases are handled; a missing case is a compile error that lists the unhandled error values (e.g. `error.Overflow`, `error.InvalidCharacter`, `error.DigitExceedsRadix`). Error sets are inferred from the `error.X` values a function can `return`.

```zig
fn charToDigit(c: u8) !u8 {
    const value = switch (c) {
        '0'...'9' => c - '0',
        'A'...'Z' => c - 'A' + 10,
        'a'...'z' => c - 'a' + 10,
        else => return error.InvalidCharacter,
    };
    return value;
}
```

## unreachable as an assertion

`expr catch unreachable` asserts that the error can never occur. In safety-checked build modes a violated assertion panics ("attempt to unwrap error"); in unsafe builds it is [[UndefinedBehavior]], so it must only be used when success is guaranteed.

## Error Return Traces

When an error propagates, Zig produces an **Error Return Trace** — distinct from a stack trace. It shows the path the error took without the program paying the cost of unwinding the stack. (Full stack traces are also available, and work on all Tier 1 and some Tier 2 targets, even freestanding.)

## Connections

- [[Zig]] — the language whose error model this is.
- [[NoHiddenControlFlow]] — errors-as-values replace exceptions, keeping control flow visible.
- [[DeferStatement]] — `errdefer` runs cleanup specifically on the error path.
- [[ZigOptional]] — sibling feature; `?T` for absence vs `!T` for failure.
- [[Comptime]] — error sets are resolved at compile time.
- [[UndefinedBehavior]] — `catch unreachable` is UB if the error actually occurs in unsafe builds.
- [[zig-in-depth-overview]] — source for the try/catch/switch/unreachable examples.
