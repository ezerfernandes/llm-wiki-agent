---
title: "cortex-m-rt"
type: entity
tags: [rust, embedded, crate, runtime, cortex-m]
sources: [rust-embedded-book-start-qemu, rust-embedded-book-start-exceptions]
last_updated: 2026-05-16
---

# cortex-m-rt

**Minimal startup / runtime crate** for [[ARMCortexM|ARM Cortex-M]] microcontrollers — the structural substitute for the missing [[RustRuntime|`libstd` pre-`main` runtime]] under [[NoStd|`#![no_std]`]] + `#![no_main]`. Published at [crates.io/crates/cortex-m-rt](https://crates.io/crates/cortex-m-rt).

The crate's job: drop in the reset handler, `.bss` zeroing, `.data` copy from [[FlashMemory|Flash]] to [[SRAM]], optional FPU init, the [[VectorTable|vector table]], a `DefaultHandler` for unhandled exceptions, a `HardFault` trampoline, and a `__pre_init` hook — then jump to the user-marked entry point. In *[[TheEmbeddedRustBook]]*'s first code example ([[rust-embedded-book-start-qemu]]) `cargo objdump` exposes exactly this skeleton in the linked binary: symbols `Reset`, `DefaultHandler_`, `HardFaultTrampoline`, `HardFault_`, `DefaultPreInit`, `__pre_init`, `__nop`.

## The `#[entry]` macro

User-facing surface is dominated by the **`#[entry]` attribute** (re-exported from `cortex-m-rt-macros`) that marks a divergent `fn main() -> !` as the post-reset entry point:

```rust
use cortex_m_rt::entry;

#[entry]
fn main() -> ! {
    loop {}
}
```

`#[entry]` exists *because* `#![no_main]` is required to drop the standard `main` interface (which would need nightly under `no_std`) — the macro restores a stable entry-point name once the standard one is gone.

## Linker-script dependency

`cortex-m-rt` requires a project-root `memory.x` ([[LinkerScript]]) declaring the target's Flash + RAM regions. Without it the link step fails. Optional `_stack_start` and `_stext` overrides allow non-default stack placement / pushing `.text` past a vendor config block right after the vector table.

## Connections

- [[CortexMQuickstartTemplate]] — the project template that wires `cortex-m-rt` into a new Cargo project.
- [[PanicHaltCrate]] — pairs with `cortex-m-rt` to supply the `#[panic_handler]` the skeleton needs.
- [[CortexMSemihostingCrate]] — the standard companion for host-IO inside an `#[entry]`-driven program.
- [[RustRuntime]] — the abstract `libstd` layer `cortex-m-rt` operationally replaces on bare metal.
- [[NoStd]] — the regime that makes `cortex-m-rt` necessary.
- [[VectorTable]] — defined by `cortex-m-rt` at the base of [[FlashMemory|Flash]] (`.vector_table` section, 1 KiB).
- [[LinkerScript]] — `cortex-m-rt`'s contract is that the user supplies `memory.x` at the project root.
- [[ARMCortexM]] — the ISA the crate targets.
- [[ExceptionAttribute]] — `cortex-m-rt`'s user-facing surface for installing handlers in the [[VectorTable|vector table]] ([[rust-embedded-book-start-exceptions]]).
- [[DefaultHandler]] / [[HardFault]] / [[ExceptionFrame]] — runtime-supplied exception machinery ([[rust-embedded-book-start-exceptions]]).
- [[TheEmbeddedRustBook]] — `cortex-m-rt` is the runtime substrate for every code example.
