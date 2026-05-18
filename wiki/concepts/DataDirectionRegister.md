---
title: "Data Direction Register (DDR)"
type: concept
tags: [embedded, gpio, peripheral, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Data Direction Register

The [[Microcontroller|MCU]] register that selects, **per bit**, whether each pin of a [[GPIO]] port is configured for output (1) or input (0). One of the three core registers in the AVR GPIO triple, alongside [[PortRegister|PORTx]] and [[PinRegister|PINx]].

On the [[ATmega328P]] (per [[embedded-controllers-fiore]] ch. 18–21):

| Port | DDR | PORT | PIN |
|---|---|---|---|
| B (8 bits) | `DDRB` @ 0x24 | `PORTB` @ 0x25 | `PINB` @ 0x23 |
| C (7 bits) | `DDRC` @ 0x27 | `PORTC` @ 0x28 | `PINC` @ 0x26 |
| D (8 bits) | `DDRD` @ 0x2A | `PORTD` @ 0x2B | `PIND` @ 0x29 |

The Atmel datasheet also calls this the "port mode register" — `portModeRegister(port)` in the Arduino runtime is a [[LookupTable|lookup table]] that resolves the Arduino port number to the right `DDRx` address.

## Underlying circuit

Per [[embedded-controllers-fiore]] ch. 19: each DDR bit is a D flip-flop. Its Q output drives the enable on a tri-state buffer between the corresponding PORT bit and the physical pin — Q=1 connects the PORT bit to the pin (output mode); Q=0 disconnects PORT and engages the input path (PIN register + [[SchmittTrigger]]). A separate AND gate uses Q (inverted) AND the PORT bit to enable the optional internal [[PullUpResistor|pull-up MOSFET]] when in input mode with PORT=1.

## Idiomatic uses

```c
// Set bit 0 of port B as output (Arduino digital pin 8):
DDRB |= 0x01;          // or:
DDRB |= (1 << 0);      // or:
bitSet(DDRB, 0);

// Set entire bottom-six of port B as outputs:
DDRB |= 0x3F;          // single-cycle alternative to 6× pinMode() calls

// Set pin to input with pull-up enabled (Arduino pin 2 / PORTD.2):
DDRD &= ~(1 << 2);     // direction = input
PORTD |= (1 << 2);     // PORT bit = 1 → engages pull-up

// Equivalent via Arduino library:
pinMode(2, INPUT_PULLUP);
```

The first idiom — `DDRB |= 0x3F` — is what makes direct DDR manipulation faster than six sequential `pinMode()` calls: one bus write instead of six function calls each doing pin→port→bit lookup and an `cli`/`sei` bracket.

## Why three registers (not one)

Symmetry of the underlying hardware: output requires a latched value (PORT flip-flop) that can be set then forgotten; input requires sampling the live pin state through a [[SchmittTrigger]] (PIN). DDR selects which path the pin takes. Some MCUs collapse this into a single bidirectional register and infer direction from access semantics; AVR exposes it explicitly. The Arduino-pin-13 caveat (built-in LED reduces source current) is a consequence of PORTB.5 being committed to an output role at the hardware level.

## Connections

- [[GPIO]] — the parent peripheral.
- [[PortRegister]] / [[PinRegister]] — the other two registers in the AVR triple.
- [[PullUpResistor]] — engaged by writing 1 to PORT while DDR=0 (input mode).
- [[SchmittTrigger]] — the input-side noise-cleaning element.
- [[ATmega328P]] — the host MCU.
- [[embedded-controllers-fiore]] — the source.
