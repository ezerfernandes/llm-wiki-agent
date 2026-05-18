---
title: "Accelerometer"
type: concept
tags: [sensor, mems, embedded, hardware]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# Accelerometer

Sensor that measures **proper acceleration** (the acceleration relative to free-fall, i.e. including gravity), typically as a 3-axis MEMS device on modern embedded boards. Reading the accelerometer at rest yields the local gravity vector — the basis for tilt sensing, screen rotation, drop detection, and (when integrated twice) crude position estimation.

On the [[STM32F3DISCOVERY]], the accelerometer is integrated with a [[Magnetometer]] on the same [[LSM303DLHC]] chip, read over [[I2C]] ([[rust-embedded-book-intro-hardware]]). Combined with the [[Gyroscope]] on the [[L3GD20]] chip this forms a complete 9-axis [[IMU|inertial motion unit]].

## Connections

- [[LSM303DLHC]] — the integrated accel+mag chip on the [[STM32F3DISCOVERY]].
- [[Magnetometer]] — sibling sensor on the LSM303DLHC; together they enable tilt-compensated heading.
- [[Gyroscope]] — completes the 9-axis IMU.
- [[I2C]] — the host bus the LSM303DLHC is read over.
