---
title: "The Embedded Rust Book — QEMU"
type: source
tags: [rust, embedded, book-chapter, qemu, emulation]
date: 2026-05-16
source_file: raw/book/src/start/qemu.md
---

## Summary

File 11/44 of *[[TheEmbeddedRustBook]]* — the **first real code chapter** of the *Getting Started* part, opened at file 10 by [[rust-embedded-book-start-index]]. End-to-end walkthrough of the embedded-Rust development loop on the [[LM3S6965|LM3S6965]] [[ARMCortexM|Cortex-M3]] microcontroller emulated by [[QEMU]]: scaffold a project from the [[CortexMQuickstartTemplate|`cortex-m-quickstart`]] template (via [[CargoGenerate|`cargo-generate`]] / `git` / zip), write the **canonical `no_std` / `no_main` skeleton** (link [[RustCoreLibrary|`libcore`]] only, panic handler via [[PanicHaltCrate|`panic-halt`]], entry point via [[CortexMRTCrate|`cortex-m-rt`]]'s `#[entry]` macro on a divergent `fn main() -> !`), pin the [[ARMCortexM|Cortex-M3]] memory layout in a [[LinkerScript|`memory.x` linker script]], [[CrossCompilation|cross-compile]] to the `thumbv7m-none-eabi` [[RustTarget|target]], inspect the ELF with [[CargoBinutils|`cargo-binutils`]] (`cargo readobj` / `cargo size` / `cargo objdump`), then run on `qemu-system-arm -machine lm3s6965evb` via a Cargo `runner` and [[GDB|remote-debug]] over `-gdb tcp::3333`. The chapter materializes every abstract construct from chapters 3–4 into one continuous shell session.

## Key Claims

- **Pedagogical choice of [[LM3S6965]].** A TI [[ARMCortexM|Cortex-M3]] MCU chosen "because it can be emulated using QEMU so you don't need to fiddle with hardware" — pushes hardware out of the critical path for the first code example. Realized via `qemu-system-arm -machine lm3s6965evb`.
- **Three scaffolding paths from the [[CortexMQuickstartTemplate|`cortex-m-quickstart`]] template.** (1) `cargo install cargo-generate` + `cargo generate --git https://github.com/knurling-rs/app-template` (the modern path, hands off to a [[Knurling]] / [[FerrousSystems|Ferrous Systems]] template); (2) `git clone https://github.com/rust-embedded/cortex-m-quickstart app` + manually fill `Cargo.toml` placeholders; (3) zip download. The template ships an `examples/` directory the chapter draws `hello` from.
- **Canonical bare-metal `main.rs` skeleton (5 essential lines).** `#![no_std]` + `#![no_main]` + `use panic_halt as _;` + `use cortex_m_rt::entry;` + `#[entry] fn main() -> ! { loop {} }`. Each piece justified: `#![no_std]` to link only [[RustCoreLibrary|`core`]] not [[RustStandardLibrary|`std`]] ([[NoStd]]); `#![no_main]` because the standard `main` interface "in `no_std` context requires nightly"; [[PanicHaltCrate|`panic_halt`]] supplies the mandatory `#[panic_handler]`; [[CortexMRTCrate|`cortex-m-rt`]]'s `#[entry]` macro re-establishes a stable entry point (substituting for the absent [[RustRuntime|`libstd` runtime]]); divergent `-> !` guarantees the program never returns — *"our program will be the only process running on the target hardware so we don't want it to end"*.
- **[[LinkerScript|`memory.x`]] declares the target memory map.** Hand-written linker fragment naming `FLASH : ORIGIN = 0x00000000, LENGTH = 256K` and `RAM : ORIGIN = 0x20000000, LENGTH = 64K` for the [[LM3S6965]]. Without it "the build will fail to link the image." Hooks an optional `_stack_start` override (default `ORIGIN(RAM) + LENGTH(RAM)` — full-descending stack), an `_stext` override (push `.text` past `0x400` for MCUs that store config after the [[VectorTable|vector table]]), and a `SECTIONS { .ram2bss }` example for placing non-zero-initialized data in a custom RAM region.
- **[[CrossCompilation|Cross-compilation]] via [[RustTarget|target triple]] `thumbv7m-none-eabi`.** The Cortex-M3 triple. The template's `.cargo/config.toml` enumerates the four common triples — `thumbv6m-none-eabi` (M0 / M0+), `thumbv7m-none-eabi` (M3, the default), `thumbv7em-none-eabi` (M4 / M7 no-FPU), `thumbv7em-none-eabihf` (M4F / M7F with FPU) — and the user uncomments exactly one. Triple isn't installed by default: `rustup target add thumbv7m-none-eabi` is mandatory. Once set as default in `[build] target`, `cargo build` and `cargo build --target thumbv7m-none-eabi` are equivalent.
- **ELF inspection via [[CargoBinutils|`cargo-binutils`]].** `cargo readobj --bin app -- --file-headers` confirms `Machine: ARM`, `Class: ELF32`, `Type: EXEC`, entry point `0x405`. `cargo size --bin app --release -- -A` prints section sizes; for the empty `loop {}` example: `.vector_table 1024 @ 0x0`, `.text 92 @ 0x400`, `.rodata 0`, `.data 0 @ 0x20000000`, `.bss 0 @ 0x20000000` — total **14570 bytes** including debug info. **Critical caveat:** ELF on-disk size ≠ flashed-binary size; "Always use `cargo-size` to check how big a binary really is" because `.ARM.attributes` and `.debug_*` sections never reach the target.
- **The `.vector_table` is non-standard.** Listed alongside `.text` / `.rodata` / `.data` / `.bss` as a fifth section that "we use to store the vector (interrupt) table" — the [[VectorTable|Cortex-M vector table]] sits at `0x00000000` at the very base of Flash.
- **`cargo objdump --bin app --release -- --disassemble --no-show-raw-insn --print-imm-hex`** dumps Thumb-2 instructions, revealing the [[CortexMRTCrate|`cortex-m-rt`]]-supplied skeleton: `main:` at `0x400` branches to user code, then loops; `Reset:` at `0x406` (called from the reset vector); `DefaultHandler_`, `HardFaultTrampoline`, `HardFault_`, `__pre_init`, `__nop`, `DefaultPreInit` — the symbols `cortex-m-rt` injects for ISR handlers, pre-init hook, and panic-by-hardfault path.
- **Running on [[QEMU]] — `hello` example uses [[Defmt|`defmt`]] over [[ARMSemihosting|semihosting]].** The template's `hello` example logs via `defmt` + RTT by default; the chapter swaps `defmt-rtt` for `defmt-semihosting` (`cargo remove defmt-rtt` + `cargo add defmt-semihosting` + edit `src/lib.rs`) because *"when using QEMU [semihosting] Just Works"* whereas RTT requires a real debug session. Manual run: `qemu-system-arm -cpu cortex-m3 -machine lm3s6965evb -nographic -semihosting-config enable=on,target=native -kernel target/thumbv7m-none-eabi/debug/hello`. Decoding `defmt` output requires the Ferrous Systems [[QemuRun|`qemu-run`]] helper.
- **The six QEMU flags explained.** `qemu-system-arm` (full-system ARM emulation, not user-mode); `-cpu cortex-m3` (catches miscompile — running a Cortex-M4F binary errors); `-machine lm3s6965evb` (the actual evaluation board model); `-nographic` (no GUI); `-semihosting-config enable=on,target=native` ([[ARMSemihosting|ARM semihosting]] lets the emulated firmware use the host's stdout / stderr / stdin and create host files — the mechanism behind `hprintln!`); `-kernel $file` (binary to load).
- **Cargo `runner` automation.** `.cargo/config.toml` ships a commented-out `runner = "qemu-system-arm -cpu cortex-m3 -machine lm3s6965evb -nographic -semihosting-config enable=on,target=native -kernel"` line. Uncomment → `cargo run --example hello --release` builds and launches QEMU in one shot, scoped to the `thumbv7m-none-eabi` target.
- **Remote debugging is the only debug model.** "Debugging an embedded device involves *remote* debugging as the program that we want to debug won't be running on the machine that's running the debugger program (GDB or LLDB)." Client = [[GDB]]; server = the QEMU process running the firmware.
- **The two debug flags.** Add `-gdb tcp::3333` (QEMU listens for a GDB connection on TCP 3333) + `-S` (freeze the machine at startup — "Without this the program would have reached the end of main before we had a chance to launch the debugger").
- **[[GDB]] connection sequence.** `gdb-multiarch -q target/thumbv7m-none-eabi/debug/examples/hello` (or `arm-none-eabi-gdb` / plain `gdb` per [[rust-embedded-book-intro-install-linux|the install chapter]]) → `target remote :3333` → process halts at the `Reset` handler from `cortex-m-rt-0.6.1/src/lib.rs:473` — *"That is the reset handler: what Cortex-M cores execute upon booting."* → `list main` → `break 13` → `continue` → execution stops at `hprintln!("Hello, world!").unwrap();` (the [[CortexMSemihostingCrate|`cortex-m-semihosting`]] `hprintln!` macro routes through [[ARMSemihosting|semihosting]] to host stdout) → `next` prints to the QEMU terminal → `next` again hits `debug::exit(debug::EXIT_SUCCESS)` and QEMU exits normally.
- **`-cpu cortex-m3` as a miscompile detector.** Specifying the exact CPU model — not just the ABI — lets QEMU error out at execution time if the binary was built for a richer ISA (e.g. Cortex-M4F with FPU instructions): a cheap consistency check on the [[RustTarget|target triple]] choice.

## Key Quotes

> ```rust
> #![no_std]
> #![no_main]
>
> use panic_halt as _;
>
> use cortex_m_rt::entry;
>
> #[entry]
> fn main() -> ! {
>     loop {
>         // your code goes here
>     }
> }
> ```
> — The canonical bare-metal-Rust skeleton. Every embedded program in [[TheEmbeddedRustBook]] is a specialization of this five-line template.

> "`#![no_std]` indicates that this program will *not* link to the standard crate, `std`. Instead it will link to its subset: the `core` crate. `#![no_main]` indicates that this program won't use the standard `main` interface that most Rust programs use. The main (no pun intended) reason to go with `no_main` is that using the `main` interface in `no_std` context requires nightly."

> "Our program will be the *only* process running on the target hardware so we don't want it to end! We use a divergent function (the `-> !` bit in the function signature) to ensure at compile time that'll be the case." — The compile-time argument for `fn main() -> !`.

> "ELF files contain metadata like debug information so their *size on disk* does *not* accurately reflect the space the program will occupy when flashed on a device. *Always* use `cargo-size` to check how big a binary really is."

> ```text
> section             size        addr
> .vector_table       1024         0x0
> .text                 92       0x400
> .rodata                0       0x45c
> .data                  0  0x20000000
> .bss                   0  0x20000000
> ```
> — `cargo size --release` output: the [[VectorTable|vector table]] occupies the first 1 KiB of [[FlashMemory|Flash]] starting at `0x0`; user code (`.text`) starts at `0x400` (the default position right after the vector table); `.data` / `.bss` live in [[SRAM]] at `0x20000000`.

> ```toml
> runner = "qemu-system-arm -cpu cortex-m3 -machine lm3s6965evb -nographic -semihosting-config enable=on,target=native -kernel"
> ```
> — The Cargo runner line, scoped to `[target.thumbv7m-none-eabi]`. With this uncommented, `cargo run` is the embedded development loop.

> "Debugging an embedded device involves *remote* debugging as the program that we want to debug won't be running on the machine that's running the debugger program (GDB or LLDB)." — The structural reason every later debug chapter assumes a probe-server architecture.

## Connections

- [[TheEmbeddedRustBook]] — the parent corpus; this is file 11/44, the first code-rich chapter.
- [[rust-embedded-book-start-index]] — preceding chapter (file 10/44) opens *Getting Started* and promises this chapter's no-hardware QEMU flow.
- [[rust-embedded-book-intro-tooling]] — chapter 4 cataloged the tools (`cargo-generate`, `cargo-binutils`, `qemu-system-arm`, `gdb`) this chapter now exercises end-to-end.
- [[rust-embedded-book-intro-no-std]] — chapter 3 established the [[NoStd|`no_std`]] / [[RustRuntime|missing-runtime]] story; this chapter shows what the missing runtime gets replaced *by* ([[CortexMRTCrate|`cortex-m-rt`]] + [[PanicHaltCrate|`panic-halt`]] + a hand-written [[LinkerScript|linker script]]).
- [[rust-embedded-book-intro-install]] — `rustup target add thumbv7m-none-eabi` is the chapter's first install-chapter prerequisite invoked.
- [[QEMU]] — the runtime engine of the chapter.
- [[LM3S6965]] — the emulated MCU (new entity).
- [[CortexMQuickstartTemplate]] — the project template (new concept).
- [[CortexMRTCrate]], [[PanicHaltCrate]], [[CortexMSemihostingCrate]] — the three Rust crates that materialize the skeleton (new entities).
- [[ARMSemihosting]] — the host-firmware bridge for `hprintln!` + `debug::exit` (new concept).
- [[VectorTable]] — the `.vector_table` ELF section at `0x0` (new concept).
- [[LinkerScript]] — `memory.x` as the canonical example (new concept).
- [[Defmt]], [[Knurling]], [[FerrousSystems]], [[QemuRun]] — the modern logging / template / runner stack the chapter touches (new entities).
- [[CargoBinutils]] — `cargo readobj` / `cargo size` / `cargo objdump` are the inspection commands.
- [[CrossCompilation]] / [[RustTarget]] — the formal mechanics behind `--target thumbv7m-none-eabi`.
- [[GDB]] — the debugger driving QEMU over `-gdb tcp::3333`.
- [[CargoGenerate]] — the scaffolding tool.
- [[ARMCortexM]] — the ISA family (Cortex-M3 specifically).

## Contradictions

None. The chapter is strictly additive — it operationalizes every abstract construct introduced in chapters 3–4 ([[rust-embedded-book-intro-no-std]] / [[rust-embedded-book-intro-tooling]]) without revising any prior claim.
