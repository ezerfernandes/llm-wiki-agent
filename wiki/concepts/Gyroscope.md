---
title: "Gyroscope"
type: concept
tags: [sensor, mems, embedded, hardware]
sources: [rust-embedded-book-intro-hardware]
last_updated: 2026-05-16
---

# Gyroscope

Sensor that measures **angular velocity** about its physical axes (degrees-per-second or rad/s), typically as a 3-axis MEMS device. Integrating angular velocity yields orientation change; fusing gyro with [[Accelerometer]] + [[Magnetometer]] (typically via a complementary or Kalman filter) is the standard recipe for stable 3-D orientation estimation in IMUs.

On the [[STM32F3DISCOVERY]] the gyroscope is the [[L3GD20]] chip, read over [[SPI]] ([[rust-embedded-book-intro-hardware]]). Together with the [[LSM303DLHC]] (accel + mag, over [[I2C]]) this gives the board a 9-axis [[IMU|inertial motion unit]].

## Connections

- [[L3GD20]] — the gyroscope chip on the [[STM32F3DISCOVERY]].
- [[Accelerometer]] / [[Magnetometer]] — the other two IMU axes; together they form a 9-axis IMU.
- [[SPI]] — the host bus the L3GD20 is read over.
