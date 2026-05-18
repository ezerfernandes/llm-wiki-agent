---
title: "Embedded Controllers Using C and Arduino (2E)"
type: source
tags: [embedded, microcontroller, arduino, avr, c-language, textbook, oer, hardware]
date: 2024-10-15
source_file: raw/embedded-controllers-fiore.pdf
---

## Summary

166-page open-educational-resource textbook by [[JamesFiore]] (Professor Emeritus, [[MohawkValleyCommunityCollege|MVCC]]), version 2.1.11 / 15 Oct 2024, released under Creative Commons BY-NC-SA (ISBN 978-1-796854879). Designed for a one-semester 3–4 credit AAS Electrical Engineering Technology / Computer Engineering Technology course in embedded controllers; assumes prior exposure to a high-level language (Python / BASIC / Pascal / FORTRAN). Two-part structure: **chapters 1–14** teach the [[CLanguage|C language]] from a desktop perspective (memory model, types, functions, libraries, [[BitwiseOperations|bitwise ops]], `#define`, [[Pointer|pointers]], [[CArray|arrays]], structures, [[LinkedList|linked lists]] — last four chapters marked optional for small embedded work); **chapters 15–29** ("Bits & Pieces") drop down to the [[ATmega328P|Atmel ATmega 328P]] microcontroller on the [[ArduinoUno|Arduino Uno]] board, examining the [[ArduinoLibrary|Arduino library]] source code (`pinMode`, `digitalWrite`, `digitalRead`, `analogRead`, `analogWrite`, `delay`, ISRs) function-by-function and showing the equivalent direct-register manipulation that runs faster and ports to non-Arduino [[AVR|AVR]] platforms. Companion lab manual exists separately.

The pedagogical thesis: *don't just rely on the Arduino libraries — read their source.* Many chapters open with the library function's doc, show the [[wiring_digital_c|`wiring_digital.c`]] / [[wiring_analog_c|`wiring_analog.c`]] implementation, then derive the raw register write that bypasses it. This "what's under the hood" stance is what distinguishes it from the typical Arduino book and is what makes the material reusable on non-Atmel platforms.

## Key Claims

- **Embedded ≠ desktop programming.** No `printf` / `scanf`; I/O is reading bits from sensors and switches, writing bits to LEDs / motors / displays via [[MemoryMappedIO|memory-mapped]] [[Peripheral|peripheral]] registers. Code typically runs an [[EventLoop|event loop]] polling input ports. Math is usually integer or [[FixedPointArithmetic|fixed-point]] (floating-point rare and expensive). Programs own the whole machine — no OS, no resource sharing, predictable execution time, [[TimingLoop|timing-loop]] delays are practical because hardware is fixed.
- **You cannot do native development for embedded.** Code is built on a *host* (your PC) using a [[CrossCompiler|cross-compiler]] targeting the *target* MCU's instruction set, then downloaded over USB / programmer. Test by simulating on host or running on target.
- **Microcontroller = specialized microprocessor with peripherals built in.** Less raw compute than a desktop CPU, but ships with on-chip Flash + SRAM + EEPROM + GPIO ports + [[ADC|ADCs]] + [[TimerCounter|timer/counters]] + serial controllers ([[USART]] / [[SPI]] / [[TWI|TWI/I²C]]) so no external glue chips are needed. Pins are usually **multiplexed** — one physical pin offers digital input, digital output, or [[PulseWidthModulation|PWM]] (one at a time).
- **AVR ATmega 328P specifics.** Used by every Arduino Uno. [[HarvardArchitecture|Harvard architecture]] with simple pipelining; 8-bit data bus; [[RISC|RISC]] instruction set (most instructions run in one 16 MHz clock cycle); 32 general-purpose registers; three special registers — [[ProgramCounter]], [[StackPointer]], [[StatusRegister|status register (SREG)]] with bits `I T H S V N Z C` (Global Interrupt Enable, Bit Copy, Half Carry, Sign, Two's-Complement Overflow, Negative, Zero, Carry). Memory: **32 k Flash** (program, non-volatile, block-programmable), **2 k SRAM** (volatile, fast, holds registers + variables), **1 k EEPROM** (non-volatile, byte-programmable, slow, for user settings that must survive power cycle). All register blocks are memory-mapped — PORTB at `0x25`, DDRB at `0x24`, PINB at `0x23`, ADCH/ADCL at `0x79/0x78`.
- **Three GPIO registers per port.** [[DataDirectionRegister|DDRx]] sets per-bit direction (1 = output, 0 = input). [[PortRegister|PORTx]] is the output-data latch — also doubles as the [[PullUpResistor|internal pull-up]] enable when the bit is in input mode. [[PinRegister|PINx]] reads the actual physical pin level (through a [[SchmittTrigger]]). Mnemonic: **"o" in PORT = output, "in" in PIN = input.** Underlying circuit is two D flip-flops (DDxn / PORTxn) plus tri-state buffers plus a pull-up MOSFET gated by `DDxn=0 AND PORTxn=1`.
- **The Arduino library `pinMode` / `digitalWrite` is convenient, not zero-cost.** `digitalWrite(pin, val)` decodes the Arduino pin number into the right port/bit via a lookup table, turns off any active [[PWM|PWM]] timer associated with the pin, saves SREG, clears interrupts, masks the bit, then restores SREG. Direct `PORTB |= 0x01;` or `bitSet(DDRB, MOTORBIT);` is far faster and the book argues you should fall through to it whenever timing matters or interrupts can't run.
- **The ADC is 10-bit successive-approximation with 4.9 mV resolution at 5 V reference.** Six channels (A0–A5) on the Uno, max ~15 kSPS, optimized for source impedance ≤ 10 kΩ, unipolar (positive voltages only). Result lands in `ADCH:ADCL` — must read `ADCL` first to lock both registers. Configurable via `ADCSRA` (enable / start / prescaler / auto-trigger / interrupt), `ADMUX` (reference REFS, left-justify ADLAR, channel MUX), `ADCSRB` (trigger source). Reference choices: DEFAULT 5 V, INTERNAL 1.1 V, EXTERNAL via AREF pin (warning: must set EXTERNAL **before** `analogRead` or you short the internal reference and may damage the chip).
- **PWM = duty-cycle modulation interpreted as average voltage.** `analogWrite(pin, val)` writes a 0–255 duty cycle at ~490 Hz on one of six pre-configured pins (3, 5, 6, 9, 10, 11) using the three timer/counters; the range 0–255 (not 0–100 %) because the 8-bit timer hardware naturally counts to 255. On Arduino Due / other ARM Cortex-M3-based Arduinos, `analogWrite` drives a real internal DAC instead.
- **Three timer/counter blocks (TC0, TC1, TC2) — two 8-bit, one 16-bit.** Each has count register `TCNTn`, compare-match registers `OCRnA` / `OCRnB`, control registers `TCCRnA` / `TCCRnB` selecting [[WaveformGenerationMode|WGM]] (Normal / [[ClearTimerOnCompare|CTC]] / Fast PWM / Phase Correct PWM) and CS prescaler (1, 8, 32, 64, 128, 256, 1024). Six waveform output pins OC0A/OC0B/OC1A/OC1B/OC2A/OC2B map to Arduino pins 6, 5, 9, 10, 11, 3 respectively. The Arduino runtime uses TC0 and TC1 internally for `delay()` / `millis()` — TC2 is the safe one to reprogram.
- **Interrupts: 26 vectors on the 328P,** named in `iom328p.h` (e.g., `INT0_vect`, `TIMER2_OVF_vect`, `ADC_vect`, `USART_RX_vect`). ISR written as `ISR(VECTOR_vect) { ... }`. Two enable layers: the individual interrupt enable bit in `EIMSK` / `TIMSKn` / etc., **and** the global `I` bit in SREG via `sei()` / `cli()`. ISRs must be short; SREG is **not** automatically saved on interrupt entry — the application must save it. Use cases: external pin-state change ([[ExternalInterrupt|`INT0`/`INT1`]] with edge select via `EICRA`), timer overflow for "hands-off" blinking / hand-wrought PWM at arbitrary pins, [[ClearTimerOnCompare|CTC]] mode for fixed-frequency square waves, ADC conversion complete.
- **Bitwise idioms are pervasive.** Setting a bit: `REG |= (1 << BIT)` or `bitSet(REG, BIT)`. Clearing: `REG &= ~(1 << BIT)` or `bitClear(REG, BIT)`. Testing: `if (REG & (1 << BIT))`. The Arduino headers define these as inline-expanded `#define` macros so there's no function-call overhead. `sbi(REG, BIT)` and `cbi(REG, BIT)` are the AVR-libc equivalents that compile to single assembly instructions.
- **The Arduino Uno is open source — both hardware and software.** Powered from USB (≤ 500 mA enumerated, ≤ 100 mA un-enumerated) or an external wall-wart. Per-pin source/sink limit 40 mA; whole-chip limit 200 mA total — driving anything beyond a small LED needs an external driver transistor. Built-in LED on digital pin 13 (PORTB.5) is hardwired and reduces available source current on that pin. The IDE can be bypassed for command-line builds; you can even insert inline assembly.

## Key Quotes

> "Unlike the myriad Arduino books now available, this text does not simply rely on the Arduino libraries. As convenient as the libraries may be, there are other, sometimes far more efficient, ways of programming the boards. Many of the chapters examine library source code to see 'what's under the hood'. This more generic approach means it will be easier for the student to use other processors and development systems instead of being tightly tied to one platform." — Introduction (p. 5)

> "When things get so big, I don't trust them at all / You want some control-you gotta keep it small" — Peter Gabriel, quoted as the author's epigraph (p. 5)

> "C is terse. It is designed for professional programmers who need to do a lot with a little code quickly." — Ch. 3 (p. 14)

> "The real 'kicker' is that you can't do *native development* with embedded code. In other words, you can't program the microcontroller just using the microcontroller the way you can create desktop applications using a desktop computer. Instead, you need to have a *host* and a *target*. … The compiler that you use is technically referred to as a *cross-compiler*." — Ch. 15 (p. 76)

> "Don't confuse pins and ports. … You must remember this, a port is just a port, a pin is just a pin. The fundamental things apply, as the clock ticks by." — Ch. 17, the *Casablanca* film-noir ATmega 328P overview (p. 88). The setup: writing to a port pin uses `PORTB`; reading from the same physical pin uses `PINB`.

> "These four 'functions' [`portModeRegister` / `portOutputRegister` / `digitalPinToBitMask` / `digitalPinToPort`] are really look-up tables disguised as functions." — Ch. 21, dissecting `pinMode` (p. 109).

## Connections

### To existing wiki

- [[EmbeddedSystems]] — second embedded-systems / [[BareMetalProgramming|bare-metal]] corpus in the wiki, complementing the first ([[TheEmbeddedRustBook]]). The two are deliberately *opposite* points in the embedded-language tradeoff space: Rust-on-[[ARMCortexM|Cortex-M]] argues for [[TypeStateProgramming|type-state]] [[StaticGuarantee|static guarantees]] and [[ZeroCostAbstraction|zero-cost abstractions]] layered over the [[PeripheralAccessCrate|PAC]]; Fiore argues for **read the library, then bypass it when you need speed**, using C and direct register pokes. Neither claim is wrong — they reflect different audiences (production embedded engineers vs first-time embedded-CS undergraduates) and different priorities (correctness-by-construction vs hardware-intuition-first).
- [[Microcontroller]] — extends the wiki's MCU coverage from the 32-bit ARM Cortex-M end (Rust book) down to the 8-bit Atmel AVR end. Same concept, very different scale: ATmega 328P has 32 k of Flash vs the STM32F303VCT6's 256 k.
- [[GPIO]] — the AVR GPIO model (DDR / PORT / PIN three-register tuple per port) is the C-level equivalent of the [[PinTypeState|pin typestate]] API the Rust book wraps over the same kind of hardware.
- [[MemoryMappedIO]] — Fiore makes the same load-bearing point as [[rust-embedded-book-peripherals-index|the Embedded Rust Book's Peripherals chapter]]: "ports … are little more than pins on the microcontroller. … a specific address in the memory map is allocated to a given port. You read and write from/to it just like any other variable." Language-agnostic universal hardware-interface contract.
- [[Interrupt]] / [[InterruptAttribute]] — the AVR ISR macro `ISR(VECTOR_vect)` is the C-language equivalent of Rust's `#[interrupt]` attribute. Same vector-table indirection; same prioritization rules; same admonition to keep ISRs short.
- [[BareMetalProgramming]] — fits squarely in the regime, but the language of choice is C and the abstraction layer is the Arduino library rather than a HAL crate.
- [[ARMCortexM]] — the book's footnote on the Arduino Due (Atmel SAM3X8E, ARM Cortex-M3 with two real 12-bit DACs) is a direct bridge to this entity. The Due is what `analogWrite()` *actually* does the analog thing on.

### To people / institutions

- [[JamesFiore]] — author. Released the text plus a series of companion OER lab manuals (Computer Programming with Python, Science of Sound, Operational Amplifiers, Semiconductor Devices, DC / AC Circuit Analysis).
- [[MohawkValleyCommunityCollege]] — institutional home; the text was written for MVCC's ABET-accredited AAS in Electrical Engineering Technology.
- [[Atmel]] — designer of the AVR core and the ATmega 328P (since 2016 a Microchip subsidiary; the schematics in the book are derived from the 2014 Atmel 328P datasheet).
- [[ArduinoCC]] — the Arduino organization; provides the IDE, libraries, and reference documentation (`arduino.cc/en/Reference`) the book frequently cites.

### To concepts introduced or extensively covered

- [[Arduino]] / [[ArduinoUno]] / [[ATmega328P]] / [[AVR]] — the hardware/software stack.
- [[CLanguage]] / [[BitwiseOperations]] / [[CrossCompiler]] / [[FixedPointArithmetic]] — language-and-toolchain background.
- [[DataDirectionRegister]] / [[PortRegister]] / [[PinRegister]] / [[PullUpResistor]] / [[SchmittTrigger]] — the GPIO substrate.
- [[ADC]] / [[PulseWidthModulation]] / [[TimerCounter]] / [[ClearTimerOnCompare]] — the analog and timing peripherals.
- [[StatusRegister]] / [[ProgramCounter]] / [[StackPointer]] / [[ALU]] — the CPU-internal registers.
- [[HarvardArchitecture]] / [[VonNeumannArchitecture]] / [[RISC]] / [[CISC]] — architecture taxonomy.
- [[FlashMemory]] / [[SRAM]] / [[EEPROM]] — the three memory regions on a typical MCU.
- [[InterruptServiceRoutine]] / [[ExternalInterrupt]] / [[VectorTable]] — interrupt mechanics.
- [[OER]] — the publishing model (free, CC BY-NC-SA, share-alike).

## Contradictions

No factual contradictions with prior wiki content. **One productive philosophical tension** with [[TheEmbeddedRustBook]]:

- The Rust book argues that the right way to expose MCU peripherals is **typestate + zero-cost abstractions** so misuse becomes a compile-time error (e.g. `Pin<Input<Floating>>` ≠ `Pin<Output<PushPull>>`, can't `set_high()` on an input pin). Fiore argues the right way to learn MCU peripherals is **first see the register-level C**, then optionally use the Arduino library, with no static safety machinery in between. Neither is wrong: Rust's design assumes a production codebase where type-system mistakes are common and expensive; Fiore's pedagogy assumes a learner who has never poked an MMIO register and needs to see the bytes move before any abstraction makes sense. The two materials are complementary — a student going from this book to the Rust book gains the type-system payoff; a student going the other direction gains the hardware intuition the typestate API hides.

## Structure

| Range | Chapters | Topic |
|---|---|---|
| 1–14 | C Language | Memory organization · variables / types / functions · libraries / `printf` · bitwise ops · `#define` · storage / scope · arrays / strings · conditionals / loops · pointers · lookup tables · structures · *(optional: linked lists, memory, file I/O, command-line args)* |
| 15 | Embedded Programming | I/O paradigm · fixed-point math · host/target · cross-compiler |
| 16 | Hardware Architecture | History from Intel 4004 · μP vs μC · CISC vs RISC · Von Neumann vs Harvard · AVR block diagram · SREG bits · memory types (ROM / PROM / Flash / EEPROM / SRAM / DRAM) |
| 17 | AVR ATmega 328P | Block diagram + Uno schematic, framed as a film-noir parody starring "Arduino" and "Miss C" |
| 18–29 | Bits & Pieces | `#include` / `#define` · digital output / input circuitry · `pinMode` · `digitalWrite` · `delay` · `digitalRead` · analog input circuitry · `analogRead` · `analogWrite` · timer/counters · interrupts |
| App. A | — | ATmega 328P full register map (PINB at 0x23 through UDR0 at 0xC6) |
| App. B | — | Selected answers to chapter exercises |
