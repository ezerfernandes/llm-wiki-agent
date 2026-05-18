---
title: "panic-semihosting"
type: entity
tags: [rust, embedded, crate, panic-handler, semihosting, debugging, no-std]
sources: [rust-embedded-book-start-semihosting]
last_updated: 2026-05-16
---

# panic-semihosting

**Rust crate providing a `#[panic_handler]` that logs the panic message to the host's stderr via [[ARMSemihosting|ARM semihosting]]** — the richer alternative to [[PanicHaltCrate|`panic-halt`]] for debug builds running under [[GDB]]+[[OpenOCD]] or [[QEMU]]. Used in *[[TheEmbeddedRustBook]]* in chapter 14 ([[rust-embedded-book-start-semihosting]]).

The user imports it the same way as any panic provider:

```rust
use panic_semihosting as _; // features = ["exit"]
```

## The `"exit"` feature

Without features, `panic-semihosting` only **logs** the panic message to host stderr through [[CortexMSemihostingCrate|`cortex-m-semihosting`]] — the firmware then halts in a `loop {}`. The optional `"exit"` Cargo feature additionally invokes `debug::exit(EXIT_FAILURE)` after the log, which under QEMU terminates the emulator with shell exit code 1.

This is the chapter's recipe for **`no_std` run-pass tests on QEMU**: write an `assert_eq!` in firmware, let `cargo run` boot QEMU, let the assertion failure trigger the panic handler, and let `$?` become the test's pass/fail signal. *"This will let you write `no_std` run-pass tests that you can run on QEMU."*

Cargo declaration in `Cargo.toml`:

```toml
panic-semihosting = { version = "VERSION", features = ["exit"] }
```

## Worked example from the chapter

```rust
#![no_main]
#![no_std]

use panic_semihosting as _; // features = ["exit"]

use cortex_m_rt::entry;
use cortex_m_semihosting::debug;

#[entry]
fn main() -> ! {
    let roses = "blue";
    assert_eq!(roses, "red"); // panics here
    loop {}
}
```

```text
$ cargo run
     Running `qemu-system-arm (..)
panicked at 'assertion failed: `(left == right)`
  left: `"blue"`,
 right: `"red"`', examples/hello.rs:15:5

$ echo $?
1
```

## Caveat — hardware safety

Because the `"exit"` feature ultimately invokes `debug::exit`, the same **"do not use on real hardware"** warning from [[rust-embedded-book-start-hardware]] applies: `debug::exit` *"can corrupt your OpenOCD session and you will not be able to debug more programs until you restart it."* `panic-semihosting` without the `"exit"` feature is safe on hardware (just slow); with `"exit"`, it is a QEMU-only tool.

## Connections

- [[ARMSemihosting]] — the host-firmware bridge the crate logs through.
- [[CortexMSemihostingCrate]] — the underlying Rust API for `debug::exit` and stderr writes.
- [[PanicHaltCrate]] — the minimal sibling; `panic-halt` just halts, `panic-semihosting` logs first.
- [[NoStd]] — the regime that mandates an explicit `#[panic_handler]` provider.
- [[CortexMRTCrate]] — provides the `#[entry]` runtime in which panics originate.
- [[QEMU]] — the supported execution environment for the `"exit"` feature; produces a clean shell exit code.
- [[GDB]] / [[OpenOCD]] — the alternate execution environment without the `"exit"` feature (logs through the OpenOCD console).
- [[TheEmbeddedRustBook]] — operationalized in [[rust-embedded-book-start-semihosting]] as the QEMU-CI panic handler.
