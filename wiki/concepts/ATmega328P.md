---
title: "ATmega 328P"
type: concept
tags: [embedded, mcu, avr, atmel, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# ATmega 328P

8-bit [[AVR]] microcontroller from [[Atmel]] (now Microchip); the chip on every [[ArduinoUno|Arduino Uno]]. Architecture details from [[embedded-controllers-fiore]] chapters 16–17 and the appendix register map.

## Core

- **8-bit data bus**, [[HarvardArchitecture|Harvard architecture]] with simple pipelining (next instruction is fetched from program memory while the current one executes).
- **[[RISC]]** instruction set — most instructions execute in **one** 16 MHz clock tick.
- **32 general-purpose 8-bit registers** feed the [[ALU]] (ALU operates on register contents, not main memory directly).
- Special registers:
  - **[[ProgramCounter|PC]]** — address of the currently executing instruction.
  - **[[StackPointer|SP]]** — top of the [[Stack|stack]] (used for `auto` locals and call frames).
  - **[[StatusRegister|SREG]]** — bits `I T H S V N Z C`:
    - **I** Global Interrupt Enable. Manipulated by `sei()` / `cli()`; auto-cleared on ISR entry, set by `RETI`.
    - **T** Bit Copy Storage (BLD / BST).
    - **H** Half Carry (BCD arithmetic).
    - **S** Sign = N ⊕ V.
    - **V** Two's Complement Overflow.
    - **N** Negative.
    - **Z** Zero.
    - **C** Carry.
  - SREG is **not** auto-saved on ISR entry — the application must save/restore it.

## Memory

| Region | Size | Type | Use |
|---|---|---|---|
| [[FlashMemory|Flash]] | 32 k | Non-volatile, block-programmable | Program code |
| [[SRAM]] | 2 k | Volatile, flip-flop-per-bit, fast | Variables + GPRs + memory-mapped peripheral registers |
| [[EEPROM]] | 1 k | Non-volatile, byte-programmable, slow | User settings that must survive power cycle |

All peripheral registers — `PORTB` at `0x25`, `DDRB` at `0x24`, `PINB` at `0x23`, `ADCH/ADCL` at `0x79/0x78`, etc. — are [[MemoryMappedIO|memory-mapped]] into the SRAM address space. See the [[ATmega328PRegisterMap|register-map appendix]] of [[embedded-controllers-fiore]].

## Peripherals

- **GPIO**: three ports — B (8 bits), C (7 bits), D (8 bits). Each port has a triple of registers: [[DataDirectionRegister|DDRx]] (direction), [[PortRegister|PORTx]] (output / pull-up), [[PinRegister|PINx]] (input). See [[GPIO]].
- **[[ADC]]**: single 10-bit successive-approximation, 6 channels on the Uno (8 on Mini/Nano), ~15 kSPS, configurable reference (DEFAULT 5 V / INTERNAL 1.1 V / EXTERNAL).
- **[[TimerCounter|Timer/Counters]]**: TC0 (8-bit), TC1 (16-bit), TC2 (8-bit). TC0/TC1 used internally by the Arduino runtime for `delay()` / `millis()`. Each timer has compare-match registers and a waveform-generation mode capable of [[PulseWidthModulation|PWM]] (Fast PWM, Phase Correct PWM) or [[ClearTimerOnCompare|CTC]] mode.
- **Serial**: USART, SPI, TWI (I²C).
- **Analog comparator**, **watchdog timer**, **brown-out detection**, **on-chip 1.1 V bandgap reference**.

## Interrupt vectors

26 vectors named in `iom328p.h`:
`RESET → INT0_vect → INT1_vect → PCINT0_vect → PCINT1_vect → PCINT2_vect → WDT_vect → TIMER2_COMPA_vect → TIMER2_COMPB_vect → TIMER2_OVF_vect → TIMER1_CAPT_vect → TIMER1_COMPA_vect → TIMER1_COMPB_vect → TIMER1_OVF_vect → TIMER0_COMPA_vect → TIMER0_COMPB_vect → TIMER0_OVF_vect → SPI_STC_vect → USART_RX_vect → USART_UDRE_vect → USART_TX_vect → ADC_vect → EE_READY_vect → ANALOG_COMP_vect → TWI_vect → SPM_READY_vect`.

User code installs handlers via `ISR(VECTOR_vect) { ... }`; the build system emits the matching entry into the [[VectorTable|vector table]] automatically.

## Operating limits

- **Per-pin**: 40 mA source/sink.
- **Whole-chip**: 200 mA total.
- **Clock**: 16 MHz on Uno (8 MHz on 3.3 V variants).

## Connections

- [[ArduinoUno]] — the canonical board.
- [[AVR]] / [[Atmel]] — family and designer.
- [[embedded-controllers-fiore]] — the source.
- [[GPIO]] / [[ADC]] / [[TimerCounter]] / [[InterruptServiceRoutine]] — the peripheral subsystems.
- [[ARMCortexM]] — counter-architecture (32-bit ARM RISC Harvard) reached via the [[Arduino]] Due.
