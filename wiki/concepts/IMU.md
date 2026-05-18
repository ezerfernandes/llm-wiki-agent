---
title: "IMU"
type: concept
tags: [sensor, mems, embedded, hardware, sensor-fusion]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# IMU

**Inertial Measurement Unit** — a sensor bundle combining a multi-axis [[Accelerometer]] and [[Gyroscope]], usually a [[Magnetometer]] as well. A "9-axis IMU" (or "9-DoF" — 9 degrees of freedom) provides 3 axes of acceleration + 3 of angular velocity + 3 of magnetic field, enough to estimate full 3-D orientation when fused (typically via a complementary or Kalman / Madgwick / Mahony filter).

The [[STM32F3DISCOVERY]] ships a 9-axis IMU as two chips: the [[LSM303DLHC]] (accel + mag over [[I2C]]) and the [[L3GD20]] (gyro over [[SPI]]) ([[rust-embedded-book-intro-hardware]]). With the on-board 8-LED compass-rose pattern, this is the hardware basis for the canonical *digital-compass* and *attitude-estimation* tutorials in the companion [[DiscoveryBook|Discovery Book]].

## Connections

- [[Accelerometer]], [[Gyroscope]], [[Magnetometer]] — the three sensor classes that compose an IMU.
- [[LSM303DLHC]], [[L3GD20]] — the two chips that together form the F3's 9-axis IMU.
- [[STM32F3DISCOVERY]] — the board the F3 IMU lives on.
- [[I2C]], [[SPI]] — the host buses used to read each chip.
