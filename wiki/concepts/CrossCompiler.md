---
title: "Cross-Compiler"
type: concept
tags: [embedded, toolchain, compilation]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Cross-Compiler

Compiler that **runs on one architecture (the *host*) and produces machine code for a different architecture (the *target*).** The canonical embedded toolchain shape: you cannot natively build firmware on the chip you're targeting — its memory and compute are too small, and it has no filesystem to host a compiler — so all building happens on a desktop PC, and the resulting binary is downloaded to the MCU over USB or a programmer.

Per [[embedded-controllers-fiore]] ch. 15:

> "The real 'kicker' is that you can't do *native development* with embedded code. … Your PC might use a Pentium processor, but the cross-compiler that runs on it creates machine code for a specific Atmel AVR microcontroller. To test your code, you need to either simulate the target on the host, or you can download the compiled code to the target and test it there. This is an extra, but unavoidable, step."

## Toolchain components

For Arduino-class development:

1. **Cross-compiler** — `avr-gcc` (compiles C / C++ for AVR) or `arm-none-eabi-gcc` (for ARM Cortex-M).
2. **Assembler** — `avr-as`; usually invoked through gcc.
3. **Linker** — `avr-ld`; links the compiled object files with `libc` (AVR-libc) and the Arduino library archives, producing an ELF.
4. **Object-copy** — `avr-objcopy`; strips ELF metadata, emits an Intel HEX file for the programmer.
5. **Programmer / bootloader** — `avrdude` over the USB-to-serial bridge talks to the Arduino bootloader to write the HEX into Flash.

The Arduino IDE hides all this behind "Build / Upload" but the same toolchain is reachable from a Makefile or `arduino-cli`.

## Testing

Two options when the target hardware isn't on your desk:

- **Simulate the target on the host** — `simulavr`, `simavr`, `qemu-system-avr`. Functional but not cycle-accurate for everything.
- **Run on the target via JTAG / debugWIRE** — closer to truth but needs a hardware debugger. The 328P supports debugWIRE on its RESET pin.

## Connections

- [[CLanguage]] / [[CompilationProcess]] — the language and pipeline being cross-compiled.
- [[CrossCompilation]] — the more general concept; this is the embedded-specific instance.
- [[AVR]] / [[ARMCortexM]] — the two target families that dominate the wiki.
- [[embedded-controllers-fiore]] — the source.
