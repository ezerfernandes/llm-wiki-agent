---
title: "Magnetometer"
type: concept
tags: [sensor, mems, embedded, hardware]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# Magnetometer

Sensor that measures the **local magnetic field vector**, typically as a 3-axis MEMS device. On Earth's surface the dominant field is the geomagnetic field, so a magnetometer doubles as a **digital compass** — when combined with an [[Accelerometer]] for tilt compensation it can return a reliable heading.

On the [[STM32F3DISCOVERY]], the magnetometer is integrated on the same [[LSM303DLHC]] chip as the accelerometer, read over [[I2C]] ([[rust-embedded-book-intro-hardware]]). The board's 8 user LEDs arranged in a compass-rose pattern (N / NE / E / SE / S / SW / W / NW) are the visual output for the canonical **digital-compass** worked example in the companion [[DiscoveryBook|Discovery Book]].

## Connections

- [[LSM303DLHC]] — the integrated accel+mag chip on the [[STM32F3DISCOVERY]].
- [[Accelerometer]] — sibling sensor on the LSM303DLHC; provides tilt compensation for heading.
- [[I2C]] — the host bus the LSM303DLHC is read over.
