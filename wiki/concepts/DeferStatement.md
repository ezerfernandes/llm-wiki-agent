---
title: "defer / errdefer (Zig Resource Management)"
type: concept
tags: [zig, defer, errdefer, resource-management, cleanup]
sources: [zig-in-depth-overview, zig-code-examples]
last_updated: 2026-06-07
---

# defer / errdefer

`defer` and `errdefer` are [[Zig]]'s constructs for scope-based resource cleanup. Per [[zig-in-depth-overview]], they make "all resource management — not only memory — simple and easily verifiable," and they pair naturally with Zig's [[ManualMemoryManagement|manual memory management]] and explicit [[ZigAllocator|allocators]].

## defer

`defer <statement>` schedules a statement to run when the enclosing scope is exited, regardless of how it is exited. This keeps cleanup next to the acquisition that needs it. It is used throughout the C-interop examples, e.g.:

```zig
const soundio = c.soundio_create();
defer c.soundio_destroy(soundio);
```

```zig
const file = try Io.Dir.cwd().openFile(io, "foo.txt", .{});
defer file.close(io);
```

The official [[zig-code-examples|samples page]] shows the same pattern across C resources — each acquisition is immediately followed by its cleanup: `defer ray.CloseWindow();`, `defer ray.EndDrawing();` (raylib), and `defer cURL.curl_global_cleanup();` / `defer cURL.curl_easy_cleanup(handle);` (libcurl). Its leak-detection sample even defers the *verification* itself — `defer std.debug.assert(debug_allocator.deinit() == .ok);` — so the no-leak check runs at scope exit (see [[ZigAllocator]], [[MemoryLeak]]).

## errdefer

`errdefer <statement>` runs only when the scope is exited *because of an error* — making it the natural complement to [[ErrorUnion|error unions]] and `try`. This lets a function allocate several resources and unwind exactly the ones acquired so far if a later step fails:

```zig
const Device = struct {
    name: []u8,

    fn create(allocator: *Allocator, id: u32) !Device {
        const device = try allocator.create(Device);
        errdefer allocator.destroy(device);

        device.name = try std.fmt.allocPrint(allocator, "Device(id={d})", id);
        errdefer allocator.free(device.name);

        if (id == 0) return error.ReservedDeviceId;

        return device;
    }
};
```

If `allocPrint` succeeds but the `id == 0` check then returns an error, both `errdefer`s fire (freeing the name and destroying the device); if everything succeeds, neither fires.

## Connections

- [[Zig]] — the language providing defer/errdefer.
- [[ErrorUnion]] — `errdefer` runs specifically on the error-return path.
- [[ZigAllocator]] — defer/errdefer are how allocations are reliably freed.
- [[ManualMemoryManagement]] — the model these constructs support.
- [[CInterop]] — `defer` is used for C resource cleanup in the libsoundio, raylib, and libcurl examples.
- [[MemoryLeak]] — the leak sample defers the `deinit() == .ok` no-leak assertion.
- [[zig-in-depth-overview]] — source for the defer/errdefer examples.
- [[zig-code-examples]] — source for the raylib/libcurl/`DebugAllocator` defer examples.
