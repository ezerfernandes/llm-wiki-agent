---
title: "GDB `load` (Flashing via the Debugger)"
type: concept
tags: [gdb, openocd, embedded, flashing, debugging]
sources: [rust-embedded-book-start-hardware]
last_updated: 2026-05-16
---

# GDB `load` (Flashing via the Debugger)

The [[GDB]] command that **writes the loaded ELF into the target's [[FlashMemory|Flash memory]]** through the connected debug server ([[OpenOCD]] / [[ProbeRs]]). In the embedded-Rust model documented by *[[TheEmbeddedRustBook]]* ([[rust-embedded-book-start-hardware]]), `load` *is* the flashing step — there is no separate `st-flash` or `openocd flash write_image` invocation; the debugger doubles as the programmer.

## Semantics

`load` walks every section of the currently-loaded ELF that has a non-zero LMA (load-memory-address) — typically `.vector_table`, `.text`, `.rodata` — and writes each into target memory at its LMA via the GDB Remote Serial Protocol. Sections destined for [[SRAM]] (`.data` initial image, `.bss`) are typically not loaded; they're initialized by the [[CortexMRTCrate|`cortex-m-rt`]] reset handler from values stored in Flash.

## Example output (F3 board)

```console
(gdb) load
Loading section .vector_table, size 0x400 lma 0x8000000
Loading section .text, size 0x1518 lma 0x8000400
Loading section .rodata, size 0x414 lma 0x8001918
Start address 0x08000400, load size 7468
Transfer rate: 13 KB/sec, 2489 bytes/write.
```

Three sections, all landing in the F3's Flash @ `0x0800_0000` — directly matching the `FLASH : ORIGIN = 0x08000000` declared in `memory.x` ([[LinkerScript]]). The 13 KB/s rate is typical for [[STLink|ST-LINK]] over [[SWD]].

## Position in the debug session

The [[CortexMQuickstartTemplate|`cortex-m-quickstart`]] template's `openocd.gdb` script invokes `load` right after `monitor arm semihosting enable` and right before `stepi`:

```text
target extended-remote :3333
…
monitor arm semihosting enable
load
stepi
```

i.e. flash, then halt at the first instruction so the debugger has control before any user code runs.

## Failure modes

- **Silent post-`continue` hang** — almost always a mis-configured `memory.x` (wrong Flash origin or length). The `load` itself succeeds against a stale `memory.x` because GDB asks OpenOCD to write to whatever LMAs the ELF declares; the boot then fails to find a valid [[VectorTable|vector table]] at `0x0800_0000`.
- **`load` fails outright** if the target isn't halted, or if OpenOCD's session voltage check rejects the probe.

## Connections

- [[GDB]] — the command's host.
- [[OpenOCD]] — the typical server that translates `load` into [[STLink|ST-LINK]] flashing operations.
- [[ProbeRs]] — the Rust-native alternative server, also speaks GDB's flash-loading protocol.
- [[FlashMemory]] — the destination memory.
- [[VectorTable]] — typically the first section `load` writes (`lma 0x8000000` on the F3).
- [[LinkerScript]] — `memory.x` declares the LMAs `load` honors.
- [[CortexMRTCrate]] — supplies the reset handler that runs first after `load` completes.
- [[ARMSemihosting]] — must be enabled via `monitor arm semihosting enable` *before* `load` so `hprintln!` works during the first run.
- [[rust-embedded-book-start-hardware]] — chapter where `load` is introduced as the flashing primitive.
