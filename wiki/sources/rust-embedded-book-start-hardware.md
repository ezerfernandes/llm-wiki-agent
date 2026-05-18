---
title: "The Embedded Rust Book — Hardware"
type: source
tags: [rust, embedded, book-chapter, hardware]
date: 2026-05-16
last_updated: 2026-05-16
source_file: raw/book/src/start/hardware.md
---

# The Embedded Rust Book — Hardware

## Summary

File 12/44 of *[[TheEmbeddedRustBook]]* — the *Getting Started* chapter's **hardware walkthrough**, immediately after the [[QEMU]] walkthrough at file 11 ([[rust-embedded-book-start-qemu]]). Adapts the same write → build → flash → debug loop from the emulated [[LM3S6965]] to a *real* [[STM32F3DISCOVERY]] board. Three operational shifts: (1) the [[RustTarget|target triple]] flips from `thumbv7m-none-eabi` ([[ARMCortexM|Cortex-M3]]) to `thumbv7em-none-eabihf` ([[ARMCortexM|Cortex-M4F]] with FPU); (2) `memory.x` is rewritten with the [[STM32F303VCT6]]'s real memory map (256 KiB [[FlashMemory|Flash]] @ `0x0800_0000`, 40 KiB [[SRAM]] @ `0x2000_0000`); (3) [[QEMU]] is replaced by an [[OpenOCD]] ↔ [[STLink|ST-LINK]] server fed from an `openocd.cfg` config file pairing an interface cfg with a target cfg. [[GDB]]'s `load` command flashes the program; `monitor arm semihosting enable` lights up [[ARMSemihosting|semihosting]] on real hardware (vs free under [[QEMU]]); the template's pre-baked `openocd.gdb` script automates the connect / break / load / start sequence so `cargo run` can drive a full debug session via a custom GDB-as-runner. *Distinct from* the intro hardware tour ([[rust-embedded-book-intro-hardware]]) which catalogs the board itself; this chapter is the **operational onboarding** of that hardware into the toolchain established in [[rust-embedded-book-start-qemu]].

## Key Claims

- **Hardware-spec checklist before configuring.** Before scaffolding a project for a new MCU, identify: (1) [[ARMCortexM|ARM core]] (e.g. Cortex-M3); (2) whether the core has an FPU (Cortex-M4**F** / Cortex-M7**F** do; the `F` is load-bearing); (3) [[FlashMemory|Flash]] + [[SRAM|RAM]] sizes (e.g. 256 KiB Flash + 32 KiB RAM); (4) Flash + RAM base addresses (RAM is "commonly located at address `0x2000_0000`"). All four sit in the device's datasheet / reference manual.
- **Worked target = [[STM32F3DISCOVERY]] with the [[STM32F303VCT6]] MCU.** [[ARMCortexM|Cortex-M4F]] core with single-precision FPU, 256 KiB Flash @ `0x0800_0000`, 40 KiB RAM @ `0x2000_0000`. (There is a second RAM region the chapter skips for simplicity.) Note: the **40 KiB** figure conflicts with the **48 KiB** quoted in [[rust-embedded-book-intro-hardware]]; the book is implicitly excluding the secondary 8 KiB CCM-RAM region here.
- **Two-step project configuration.** (a) In `.cargo/config.toml`, set `target = "thumbv7em-none-eabihf"` — the [[RustTarget|target triple]] for [[ARMCortexM|Cortex-M4F]] / Cortex-M7F with FPU. The template enumerates all four common triples with three commented out. **First-time prerequisite:** `rustup target add thumbv7em-none-eabihf` ([[Rustup]]) — the [[CortexMQuickstartTemplate|`cortex-m-quickstart`]] template installs no triple by default. (b) Rewrite `memory.x` with `FLASH : ORIGIN = 0x08000000, LENGTH = 256K` and `RAM : ORIGIN = 0x20000000, LENGTH = 40K` (the comment notes `1 K = 1 KiBi = 1024 bytes` — binary KiB, not decimal). **Cache pitfall:** `cargo build` does not track `memory.x` updates — after editing it, `cargo clean` before `cargo build` or stale link output silently persists.
- **Pre-flight code edit for real hardware.** In `examples/hello.rs`, comment out / remove the `debug::exit(debug::EXIT_SUCCESS)` call — *"it is used only for running in QEMU"* and *"can corrupt [[OpenOCD]] state"* on real hardware. This is the single delta from the QEMU `hello` example. The semihosting `hprintln!("Hello, world!").unwrap();` line is unchanged.
- **`cargo build --example hello` cross-compiles unchanged.** Once the triple and memory map are right, the [[CrossCompilation|cross-compile]] step is identical to QEMU. *"The `cortex-m-rt` crate handles all the magic required to get your chip running, as helpfully, pretty much all Cortex-M CPUs boot in the same fashion."* — [[CortexMRTCrate|`cortex-m-rt`]]'s [[VectorTable|reset-handler + vector table]] is the portable abstraction across Cortex-M variants.
- **[[OpenOCD]] replaces [[QEMU]] as the debug server.** Connection is "remote debugging" (same architecture as the QEMU chapter) but the server changes: GDB → [[OpenOCD]] → [[STLink|ST-LINK]] probe → [[STM32F303VCT6]] (over [[SWD]]). [[STLink|ST-LINK]] is on-board the F3 via the dedicated [[STM32F103]] sub-MCU; no external probe needed.
- **`openocd.cfg` pairs an interface cfg with a target cfg.** The template ships an `openocd.cfg` at project root that [[OpenOCD]] picks up when run from there. It `source`s **two** files via `find`: an **interface** cfg (`interface/stlink.cfg` for newer Revision C boards, `interface/stlink-v2.cfg` for older Revision A/B) and a **target** cfg (`target/stm32f3x.cfg`). Which interface line is uncommented depends on the hardware revision discovered during the [[rust-embedded-book-intro-verify|verify]] section.
- **[[OpenOCD]] startup output as a pass signal.** A working session prints (selected lines): `auto-selecting first available session transport "hla_swd"` → `STLINK v2 JTAG v27 API v2 SWIM v15 VID 0x0483 PID 0x374B` → `Target voltage: 2.913879` → `stm32f3x.cpu: hardware has 6 breakpoints, 4 watchpoints`. The last line is the same pass signal documented in [[rust-embedded-book-intro-verify]].
- **[[GDB]] connection sequence on real hardware.** From a second terminal: `gdb-multiarch -q target/thumbv7em-none-eabihf/debug/examples/hello` (or `arm-none-eabi-gdb` / plain `gdb` per [[rust-embedded-book-intro-install-linux|the install chapter]]) → `target remote :3333` (OpenOCD listens on TCP 3333, same convention as QEMU's `-gdb tcp::3333`).
- **`load` is the flash command.** Unlike QEMU where the binary is given to `qemu-system-arm -kernel`, on real hardware GDB's **`load`** command flashes the program over OpenOCD. The chapter's example output shows three sections written to Flash starting at `0x0800_0000`: `.vector_table` (1024 B @ `lma 0x8000000`), `.text` (5400 B @ `0x8000400`), `.rodata` (1044 B @ `0x8001918`) — total **7468 bytes** transferred at ~13 KB/s. The `lma` (load-memory-address) values match the `memory.x` Flash origin.
- **[[ARMSemihosting|Semihosting]] must be explicitly enabled.** Under QEMU semihosting is free (`-semihosting-config enable=on`); on real hardware **OpenOCD requires** `monitor arm semihosting enable` — the `monitor` prefix is GDB's escape to send commands to the remote server. *"You can see all the OpenOCD commands by invoking the `monitor help` command."* — the discoverability hatch into OpenOCD's command vocabulary.
- **The breakpoint-debug pattern is identical to QEMU.** `break main` → `continue` → halts at `examples/hello.rs:11` (auto-promoted to a *hardware* breakpoint because `main` lives in read-only Flash) → `step` → `next` → "Hello, world!" appears on **the OpenOCD console** (not the GDB console — semihosting output is captured server-side, an important difference from purely-host-side debugging). After `loop {}` the message prints once and the CPU spins forever on `halted: PC: 0x080004…` cycles.
- **`memory.x` mis-configuration → silent GDB hang.** A boxed NOTE: if `continue` hangs the terminal instead of hitting the `main` breakpoint, double-check the `memory.x` Flash + RAM **origins and lengths** for the device. Bad memory layout produces a no-error, no-progress failure mode — operationally the worst kind.
- **The `openocd.gdb` script automates the connect/load/start sequence.** The [[CortexMQuickstartTemplate|`cortex-m-quickstart`]] template ships an `openocd.gdb` GDB-script with: `target extended-remote :3333` (extended remote allows re-running) → `set print asm-demangle on` (Rust symbol demangling) → `break DefaultHandler` + `break HardFault` + `break rust_begin_unwind` (catch unhandled exceptions, hard faults, panics — the three failure modes you can't miss) → `monitor arm semihosting enable` → `load` (flash) → `stepi` (halt at the first instruction so the debugger has control before any user code runs).
- **`<gdb> -x openocd.gdb` runs the whole script.** Pass the script via `-x`: `gdb-multiarch -x openocd.gdb target/thumbv7em-none-eabihf/debug/examples/hello`. One command = connect + enable semihosting + flash + halt at instruction 1.
- **Cargo runner = `<gdb> -x openocd.gdb`.** The template's `.cargo/config.toml` ships a commented-out runner under `[target.'cfg(all(target_arch = "arm", target_os = "none"))']`: `runner = "arm-none-eabi-gdb -x openocd.gdb"` (or `gdb-multiarch -x openocd.gdb` or just `gdb -x openocd.gdb` — pick the GDB variant the install chapter put on the user's `PATH`). Uncomment → `cargo run --example hello` builds *and* starts a GDB session in one shot. Mirrors the QEMU-runner pattern from [[rust-embedded-book-start-qemu]] but now `cargo run` drives real hardware.
- **The `cfg(all(target_arch = "arm", target_os = "none"))` predicate is broader than `thumbv7em-none-eabihf`.** Earlier in the file the QEMU runner under `[target.thumbv7m-none-eabi]` is scoped to one specific triple; the GDB runner sits under a `cfg`-predicate that matches *any* `arm + os=none` triple — i.e. all four Cortex-M triples the template enumerates. This is the practical reason the GDB-runner block isn't duplicated per-triple.
- **Pointer to [the Debugonomicon](https://github.com/rust-embedded/debugonomicon).** The chapter explicitly defers device-specific debugging tricks (custom config files, exotic chips, JTAG quirks) to the Debugonomicon — a sibling [[RustEmbeddedWorkingGroup]] resource. This chapter is the F3-specific reference walkthrough only.

## Key Quotes

> "Before we begin you need to identify some characteristics of the target device as these will be used to configure the project: The ARM core. e.g. Cortex-M3. Does the ARM core include an FPU? Cortex-M4F and Cortex-M7F cores do. How much Flash memory and RAM does the target device have? […] Where are Flash memory and RAM mapped in the address space? […]" — The four-point hardware-spec checklist; the operational contents of every datasheet read.

> ```toml
> # Pick ONE of these compilation targets
> # target = "thumbv6m-none-eabi"    # Cortex-M0 and Cortex-M0+
> # target = "thumbv7m-none-eabi"    # Cortex-M3
> # target = "thumbv7em-none-eabi"   # Cortex-M4 and Cortex-M7 (no FPU)
> target = "thumbv7em-none-eabihf" # Cortex-M4F and Cortex-M7F (with FPU)
> ```
> — The four Cortex-M [[RustTarget|target triples]] the template catalogues; the user uncomments exactly one. F3 board → `thumbv7em-none-eabihf`.

> ```text
> /* Linker script for the STM32F303VCT6 */
> MEMORY
> {
>   /* NOTE 1 K = 1 KiBi = 1024 bytes */
>   FLASH : ORIGIN = 0x08000000, LENGTH = 256K
>   RAM : ORIGIN = 0x20000000, LENGTH = 40K
> }
> ```
> — The `memory.x` [[LinkerScript|linker script]] for the F3. Flash @ `0x0800_0000` (not `0x0` as on the [[LM3S6965]]) is the headline change.

> "NOTE do not run this on hardware; it can corrupt OpenOCD state" — Source comment in `hello.rs` next to `debug::exit(debug::EXIT_SUCCESS)`. The one code-level delta between the QEMU and hardware flows.

> ```text
> # Sample OpenOCD configuration for the STM32F3DISCOVERY development board
>
> # Depending on the hardware revision you got you'll have to pick ONE of these
> # interfaces. At any time only one interface should be commented out.
>
> # Revision C (newer revision)
> source [find interface/stlink.cfg]
>
> # Revision A and B (older revisions)
> # source [find interface/stlink-v2.cfg]
>
> source [find target/stm32f3x.cfg]
> ```
> — The `openocd.cfg` template; *one* interface cfg + *one* target cfg. The pairing pattern generalizes to every OpenOCD-supported board.

> ```console
> (gdb) load
> Loading section .vector_table, size 0x400 lma 0x8000000
> Loading section .text, size 0x1518 lma 0x8000400
> Loading section .rodata, size 0x414 lma 0x8001918
> Start address 0x08000400, load size 7468
> Transfer rate: 13 KB/sec, 2489 bytes/write.
> ```
> — `load`'s output. The three flashed sections + their `lma` (load-memory-address) values map 1:1 to the `memory.x` Flash origin (`0x0800_0000`) — the operational proof that the linker script controls flashing.

> "Now proceed to *flash* (load) the program onto the microcontroller using the `load` command." — The compact definition: in the GDB+OpenOCD model, **`load` *is* the flashing step**. No separate `st-flash` / `openocd flash` invocation.

> ```console
> (gdb) monitor arm semihosting enable
> semihosting is enabled
> ```
> — Mandatory on real hardware. *"You can see all the OpenOCD commands by invoking the `monitor help` command."* — the discoverability hatch.

> "If GDB blocks the terminal instead of hitting the breakpoint after you issue the `continue` command above, you might want to double check that the memory region information in the `memory.x` file is correctly set up for your device (both the starts *and* lengths)." — The diagnostic for the silent-hang failure mode of bad `memory.x` config.

> ```text
> target extended-remote :3333
>
> # print demangled symbols
> set print asm-demangle on
>
> # detect unhandled exceptions, hard faults and panics
> break DefaultHandler
> break HardFault
> break rust_begin_unwind
>
> monitor arm semihosting enable
>
> load
>
> # start the process but immediately halt the processor
> stepi
> ```
> — `openocd.gdb` in full: 7 commands that compress the entire connect / load / start sequence. Every embedded-Rust debug session under this book starts here.

> ```toml
> [target.'cfg(all(target_arch = "arm", target_os = "none"))']
> # uncomment ONE of these three option to make `cargo run` start a GDB session
> # which option to pick depends on your system
> runner = "arm-none-eabi-gdb -x openocd.gdb"
> # runner = "gdb-multiarch -x openocd.gdb"
> # runner = "gdb -x openocd.gdb"
> ```
> — The Cargo runner block scoped to the `arm + os=none` cfg predicate. Uncomment exactly one variant matching the GDB the user installed.

## Connections

- [[TheEmbeddedRustBook]] — the parent corpus; this is file 12/44 — the *Getting Started* chapter's hardware walkthrough.
- [[rust-embedded-book-start-qemu]] — file 11/44; the QEMU walkthrough this chapter mirrors on real hardware. Same loop, swap [[QEMU]] for [[OpenOCD]] + [[STLink|ST-LINK]], swap `thumbv7m-none-eabi` for `thumbv7em-none-eabihf`, swap `-kernel` invocation for `load`.
- [[rust-embedded-book-start-index]] — chapter opener (file 10/44) that promised this Hardware sub-section as the only part of the chapter requiring physical hardware.
- [[rust-embedded-book-intro-hardware]] — the *intro*-chapter hardware tour (file 2/44). That page catalogs *what is on* the F3 board; this page is the operational onboarding of that hardware. **40 KiB vs 48 KiB SRAM** discrepancy noted in this chapter's `memory.x` (intro-hardware quotes 48 KiB total; this chapter declares 40 KiB usable and skips the secondary CCM-RAM region).
- [[rust-embedded-book-intro-verify]] — the smoke test (file 9/44) where the user discovered their F3 board revision; that determines which interface cfg in `openocd.cfg` to uncomment.
- [[rust-embedded-book-intro-tooling]] — chapter 4 cataloged [[GDB]] / [[OpenOCD]] / [[STLink]] as the three-layer probe stack. This chapter exercises that stack end-to-end.
- [[rust-embedded-book-intro-install-linux]] / [[rust-embedded-book-intro-install-macos]] / [[rust-embedded-book-intro-install-windows]] — the three GDB variants (`gdb-multiarch` / `arm-none-eabi-gdb` / plain `gdb`) the runner block expects on `PATH` come from these install branches.
- [[STM32F3DISCOVERY]] — the reference board.
- [[STM32F303VCT6]] — the application MCU configured by `memory.x` (256 KiB Flash + 40 KiB usable RAM).
- [[STM32F103]] — the second MCU on the F3 board implementing the on-board [[STLink|ST-LINK]] probe.
- [[STLink]] — the in-circuit programmer/debugger protocol; OpenOCD drives it.
- [[OpenOCD]] — the debug server. New role this chapter: how to *configure* it via `openocd.cfg` (interface + target cfg pairing).
- [[GDB]] — the debugger front-end. New commands exercised: `load`, `monitor`, `target extended-remote`.
- [[ARMSemihosting]] — the host-IO mechanism for `hprintln!`; `monitor arm semihosting enable` lights it up on real hardware.
- [[ARMCortexM]] — Cortex-M4F is the worked variant; `thumbv7em-none-eabihf` the triple.
- [[CortexMRTCrate]] — supplies the [[VectorTable|reset handler + vector table]] that makes the binary boot on the F3 from `0x0800_0000`. *"Pretty much all Cortex-M CPUs boot in the same fashion."*
- [[CortexMQuickstartTemplate]] — the template's `openocd.cfg` + `openocd.gdb` + `.cargo/config.toml` with the GDB-runner block are the load-bearing scaffolding for this chapter.
- [[CortexMSemihostingCrate]] — `hprintln!` source in the hardware `hello` example.
- [[VectorTable]] — `.vector_table` is the first section flashed by `load` at `lma 0x8000000`.
- [[LinkerScript]] — `memory.x` is the canonical example; lengths *and* origins both matter.
- [[FlashMemory]] / [[SRAM]] — the two memory regions `memory.x` declares.
- [[CrossCompilation]] / [[RustTarget]] — `thumbv7em-none-eabihf` is the [[ARMCortexM|Cortex-M4F]] target triple; `rustup target add` mandatory.
- [[Cargo]] / [[Rustup]] — drive the build + target install.
- [[QEMU]] / [[LM3S6965]] — replaced in this chapter; the comparison-against substrate.
- [[OpenOCDConfig]] — new concept: the interface-cfg + target-cfg pairing convention.
- [[GDBLoad]] — new concept: GDB's `load` command as the flashing primitive over OpenOCD.

## Contradictions

- **40 KiB vs 48 KiB SRAM on the F3.** This chapter declares `RAM : LENGTH = 40K` in `memory.x` *"(There's another RAM region but for simplicity we'll ignore it)"*. [[rust-embedded-book-intro-hardware]] quotes **48 KiB** of SRAM for the [[STM32F303VCT6]]. Reconciliation: the F3 has 40 KiB main SRAM @ `0x2000_0000` + 8 KiB CCM-RAM @ a separate address; the intro hardware tour quotes the **total**, this chapter declares the **main contiguous region** used by `memory.x`. Both are correct in their context — this chapter's `memory.x` omits CCM. No factual contradiction, but a numerical mismatch worth flagging for any later chapter that wants to use CCM.

Beyond that one: none. The chapter is strictly additive — it operationalizes the QEMU flow onto real hardware via the same template, the same `cortex-m-rt` runtime, the same GDB front-end. Every prior abstraction ([[VectorTable]], [[LinkerScript]], [[ARMSemihosting]], [[CortexMQuickstartTemplate]]) is reused, not revised.
