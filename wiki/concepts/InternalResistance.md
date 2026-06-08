---
title: "Internal Resistance"
type: concept
tags: [physics, electricity, circuits, dc]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
Internal resistance (r) is the opposition to current flow **inside** a voltage source itself, arising from the source's physical construction and chemistry. It acts in series with the source's ideal [[ElectromotiveForce]], so the measured terminal voltage drops below the emf whenever current flows.

## Key Points
- Terminal voltage `V = emf − I r`; the larger the current or r, the bigger the drop.
- A nearly fresh battery has small r (terminal voltage stays near emf); an aging or depleted battery has large r (output sags under load).
- When the load resistance equals r, the source delivers maximum power to the load but wastes half the power internally.
- Battery testers apply a known load and watch terminal voltage decline to estimate r.
- Series connections add internal resistances; parallel identical sources reduce the combined internal resistance, allowing more current.

## Equations
- `V = emf − I r`
- `I = emf / (R_load + r)`
- Internal power dissipated: `P_r = I² r`

## Related
- [[ElectromotiveForce]] — the ideal source voltage r reduces
- [[ElectricalResistance]] — same quantity, located inside the source
- [[Voltmeter]] / [[Ammeter]] — meters likewise have non-ideal internal resistance
- [[RCCircuit]] — rising battery r slows capacitor charging (camera-flash delay)
