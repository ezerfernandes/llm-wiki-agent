---
title: "EEPROM"
type: concept
tags: [memory, embedded, non-volatile, hardware]
sources: [embedded-controllers-fiore]
last_updated: 2026-05-17
---

# EEPROM

**Electrically Erasable Programmable Read-Only Memory.** Non-volatile MCU storage that's **byte-programmable** — unlike [[FlashMemory|Flash]] you can erase and rewrite a single byte without touching its neighbors — at the cost of being slower and more expensive per bit than Flash. Used for "remembers across power cycle" data: device serial number, calibration constants, the last-set channel on a stereo receiver, user-preference flags on a digital camera.

Per [[embedded-controllers-fiore]] ch. 16:

> "A possible example use of EEPROM would involve saving user preference settings for a digital camera. When power is turned off and back on, the user expects the device to be 'as they left it', not reverting back to a default state. Typically, special instructions or procedures are needed to write to or read from EEPROM."

On the [[ATmega328P]]: 1 k of EEPROM, addressed via `EEARH:EEARL` (address) + `EEDR` (data) + `EECR` (control). The AVR-libc API (`<avr/eeprom.h>`) wraps the read / write sequence behind `eeprom_read_byte()` / `eeprom_write_byte()` / `eeprom_update_byte()` (the *update* variant skips the write if the value hasn't changed — important because EEPROM has a finite endurance, typically 100 k write cycles per byte).

## Constraints

- **Endurance**: ~100 k erase-write cycles per cell. Counters that update every loop iteration will wear out the cell — write only on state change.
- **Write latency**: ~3.3 ms per byte on a 328P. Polling the `EEPE` bit (or hooking the `EE_READY_vect` interrupt) is required before issuing the next write.
- **Atomicity**: an interrupted EEPROM write can leave a byte in an indeterminate state. Critical data should be stored with redundancy (two copies + a flag, or CRC).

## Connections

- [[FlashMemory]] — the program-memory counterpart; block-programmable, no endurance worry for normal program use.
- [[SRAM]] — the volatile fast counterpart.
- [[ATmega328P]] / [[AVR]] — typical MCU instance.
- [[embedded-controllers-fiore]] — the source.
