---
title: "LSM303DLHC"
type: entity
tags: [sensor, mems, accelerometer, magnetometer, hardware]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# LSM303DLHC

[[STMicroelectronics]] system-in-package combining a 3-axis [[Accelerometer]] and a 3-axis [[Magnetometer]] in a single chip, accessed over [[I2C]]. Mounted on the [[STM32F3DISCOVERY]] dev board; with the separate [[L3GD20]] gyroscope chip, it gives the board a full 9-axis [[IMU|inertial motion unit]] ([[rust-embedded-book-intro-hardware]]).

The accelerometer + magnetometer pairing on this chip — combined with the 8 user LEDs arranged in a compass-rose pattern — is the hardware basis for the canonical **digital-compass** tutorial in the companion [[DiscoveryBook|Discovery Book]].

## Connections

- [[STM32F3DISCOVERY]] — the board this chip is mounted on.
- [[STMicroelectronics]] — manufacturer.
- [[Accelerometer]], [[Magnetometer]] — the two sensor classes integrated in this chip.
- [[I2C]] — the host bus the chip is read over.
- [[L3GD20]] — sibling chip on the same board providing the third leg (gyroscope) of the 9-axis IMU.
