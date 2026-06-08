---
title: "Voltmeter"
type: concept
tags: [physics, electricity, circuits, dc, instruments]
sources: [college-physics-2e-ch21]
last_updated: 2026-06-07
---

## Definition
A voltmeter measures the potential difference (voltage) across a circuit element. It is connected **in parallel** with that element so it experiences the same voltage. An analog voltmeter is a [[Galvanometer]] in series with a large resistor that sets the full-scale voltage range.

## Key Points
- Connected in parallel — parallel elements share the same voltage.
- Built from a galvanometer plus a **large series resistor**, so it draws little current.
- An ideal voltmeter has very high resistance (orders of magnitude above the load) to avoid disturbing the circuit.
- Connecting any voltmeter lowers the effective resistance of the measured element, introducing some error.
- Car dashboard gauges (fuel, temperature) act as voltmeters reading variable-resistance sender units.
- Digital voltmeters draw less current than analog ones and perturb the circuit less.

## Equations
- Total resistance for full-scale: `R_tot = R + r = V / I`
- Required series resistor: `R = R_tot − r`
  - r = galvanometer resistance; I = galvanometer full-scale (sensitivity) current

## Related
- [[Galvanometer]] — the deflection mechanism inside
- [[Ammeter]] — the complementary series-connected current meter
- [[Voltage]] / [[ElectricPotential]] — the quantity measured
- [[ResistorsInSeriesAndParallel]] — parallel connection rationale
- [[WheatstoneBridge]] / [[Potentiometer]] — null methods that avoid voltmeter loading error
