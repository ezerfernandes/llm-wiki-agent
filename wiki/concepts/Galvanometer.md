---
title: "Galvanometer"
type: concept
tags: [physics, electricity, circuits, dc, instruments]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
A galvanometer is an analog current-sensing instrument whose needle deflects in proportion to the current passing through it, via magnetic force on a current-carrying coil. It is the core element from which analog [[Voltmeter]]s and [[Ammeter]]s are built by adding series or shunt resistors.

## Key Points
- Deflection is proportional to current; reading is set by the magnetic torque on the coil.
- **Current sensitivity** is the current that produces full-scale deflection (e.g. 50 µA); smaller values mean a more sensitive instrument.
- Has a small but non-zero internal resistance r.
- Becomes a voltmeter with a large **series** resistor; becomes an ammeter with a small **shunt** (parallel) resistor.
- Higher sensitivity enables higher-quality meters that disturb the measured circuit less.
- Also acts as the zero-current detector in null measurements ([[WheatstoneBridge]], [[Potentiometer]]).

## Equations
- As voltmeter: `R_series = (V / I_G) − r`
- As ammeter: `R_shunt = r · (I_G / I)`
  - I_G = full-scale (sensitivity) current; r = galvanometer resistance

## Related
- [[Voltmeter]] — galvanometer + large series resistor
- [[Ammeter]] — galvanometer + small shunt
- [[ElectricCurrent]] — the quantity it senses
- [[WheatstoneBridge]] / [[Potentiometer]] — use it as a null detector
