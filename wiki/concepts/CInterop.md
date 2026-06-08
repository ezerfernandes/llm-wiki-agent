---
title: "C Interop in Zig (@cImport, zig cc)"
type: concept
tags: [zig, c-interop, cimport, translate-c, libc, c-abi, ffi]
sources: [zig-in-depth-overview, zig-why-zig-vs-rust-d-cpp, zig-code-examples]
last_updated: 2026-06-07
---

# C Interop in Zig

A primary use case for [[Zig]] is interoperating with — and replacing — C. Per [[zig-in-depth-overview]], Zig provides bindingless C interop, doubles as a full C compiler, and ships its own libc, leading the docs to claim "Zig is better at using C libraries than C is at using C libraries" and "Zig is a better C compiler than C compilers!"

## Why C interop is strategic: "a portable language for libraries"

The rationale essay [[zig-why-zig-vs-rust-d-cpp]] frames C interop as central to Zig's bid to become the new portable language for reusable libraries. Its reasoning: code reuse is "one of the holy grails of programming," but in practice we keep re-inventing the wheel — real-time requirements disqualify any GC/non-deterministic dependency, and a language that makes it too easy to ignore errors makes it hard to trust a library's error handling (Zig counters by making correct error handling "the laziest thing a programmer can do," see [[ErrorUnion]]). Crucially: *"it is pragmatically true that C is the most versatile and portable language. Any language that does not have the ability to interact with C code risks obscurity."* Zig therefore aims to become the new portable library language by simultaneously making C-ABI conformance for external functions straightforward and adding safety/design that prevents common implementation bugs.

## @cImport — no FFI, no bindings

`@cImport(@cInclude("header.h"))` directly imports C types, variables, functions, and simple macros into Zig — no hand-written bindings. It even translates C inline functions into Zig. The page's example emits a sine wave using the libsoundio C library, calling `c.soundio_create()`, `c.soundio_outstream_create()`, etc. directly:

```zig
const c = @cImport(@cInclude("soundio/soundio.h"));
```

```sh
$ zig build-exe sine.zig -lsoundio -lc
```

### Worked examples: raylib and libcurl

The official [[zig-code-examples|samples page]] gives two more `@cImport` programs. The **raylib** sample imports the C graphics header and calls its functions directly, linking libc and raylib at build time:

```zig
// build with `zig build-exe c-interop.zig -lc -lraylib`
const ray = @cImport({
    @cInclude("raylib.h");
});

pub fn main() void {
    ray.InitWindow(800, 450, "raylib [core] example - basic window");
    defer ray.CloseWindow();
    ray.SetTargetFPS(60);
    while (!ray.WindowShouldClose()) {
        ray.BeginDrawing();
        defer ray.EndDrawing();
        ray.ClearBackground(ray.RAYWHITE);
        ray.DrawText("Hello, World!", 190, 200, 20, ray.LIGHTGRAY);
    }
}
```

The **libcurl** sample shows a fuller real-world workflow — global init/cleanup, a nullable easy-handle (`orelse return error.CURLHandleInitFailed`), an arena allocator for the response buffer, and a `callconv(.C)` write callback that appends bytes into a `std.ArrayList(u8)` using `@ptrCast`/`@alignCast`:

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

These show the recurring interop idioms: C functions are called by their original names, `defer` mirrors each C `*_cleanup`/`*_destroy` next to its acquisition (see [[DeferStatement]]), nullable C returns are unwrapped with `orelse` into [[ErrorUnion|error returns]], and C string parameters are passed as `[*:0]const u8` sentinel-terminated pointers.

### extern — calling a system API with no binding at all

When you don't even need a header, a bare `extern` declaration suffices. The samples page's Windows example declares and calls `user32.dll`'s `MessageBoxA` directly:

```zig
extern "user32" fn MessageBoxA(?win.HWND, [*:0]const u8, [*:0]const u8, u32) callconv(.winapi) i32;
```

"All system API functions can be invoked this way, you do not need library bindings to interface them."

## export — exposing Zig to C

The `export` keyword in front of functions, variables, and types makes them part of a C-ABI library API:

```zig
export fn add(a: i32, b: i32) i32 {
    return a + b;
}
```

`zig build-lib mathtest.zig` produces a static library; adding `-dynamic` produces a shared library. This makes Zig a common choice for shipping a C-ABI library that other languages call into.

## Zig is also a C compiler

`zig build-exe hello.c -lc` compiles C directly. `--verbose-cc` reveals the underlying clang-compatible `zig cc` invocation. Re-running finishes instantly thanks to **Build Artifact Caching**, which parses the generated `.d` file to avoid duplicate work.

## Zig ships with libc

`zig targets` lists ~97 bundled libc targets (glibc, musl, and more); for those targets `-lc` does not depend on any system files. glibc cannot be linked statically, but musl can — `zig build-exe hello.c -lc -target x86_64-linux-musl` builds musl from source (then caches it) and links a fully static binary. Despite supporting libc for ~97 targets plus compiler-rt, libunwind, libcxx, and libtsan, Zig tarballs stay around 50 MiB (versus clang 8.0.0's own ~132 MiB Windows build) thanks to a `process_headers` tool.

## Connections

- [[Zig]] — the language providing C interop.
- [[CLanguage]] — the language Zig imports, compiles, and replaces.
- [[ZigToolchain]] — `zig cc`, `zig build-exe`, `zig build-lib`, `zig targets`.
- [[CrossCompilation]] — bundled libc enables cross-compiling C for any target.
- [[Linker]] — `-lc`, `-lsoundio`, `linkSystemLibrary` drive linking.
- [[DeferStatement]] — `defer` manages C resource cleanup in the examples.
- [[ErrorUnion]] — trustworthy error propagation underpins the library-reuse argument.
- [[ZigBuildSystem]] — depending on and building native C libraries is what makes reuse tractable.
- [[LLVM]] — the clang-compatible C compilation path.
- [[ZigOptional]] — nullable C returns (`curl_easy_init()`) are handled with `orelse`.
- [[zig-in-depth-overview]] — source for the @cImport / zig cc / libc examples.
- [[zig-why-zig-vs-rust-d-cpp]] — source for the "portable language for libraries" argument.
- [[zig-code-examples]] — source for the raylib, libcurl, and `extern "user32"` interop samples.
