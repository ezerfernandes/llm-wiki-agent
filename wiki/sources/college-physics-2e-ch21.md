---
title: "College Physics 2e — Ch.21: Circuits and DC Instruments"
type: source
tags: [physics, openstax, college-physics-2e]
date: 2026-06-07
source_file: raw/college-physics-2e/ch-21.md
---

## Summary
Chapter 21 of OpenStax *College Physics 2e* extends circuit analysis past single-resistor cases. It covers combining resistors in series and parallel, the distinction between a source's emf and its terminal voltage (set by internal resistance), Kirchhoff's junction and loop rules for multi-loop networks, the construction and connection of DC voltmeters/ammeters from galvanometers, precision null measurements (potentiometer and Wheatstone bridge), and the transient charging/discharging of resistor–capacitor (RC) circuits under DC.

## Key Claims
- Series resistances add (`Rs = R₁ + R₂ + ...`); parallel resistances combine reciprocally (`1/Rp = Σ 1/Rₙ`), so the parallel total is always less than the smallest branch resistor.
- In series the current is shared and voltages add; in parallel the voltage is shared and currents add; energy/charge conservation guarantees `P_source = Σ Pₙ`.
- A real source equals an ideal emf in series with internal resistance r; terminal voltage `V = emf − I r` drops under heavy load, and r rises as a battery ages.
- Series sources add emf and add internal resistance; parallel identical sources keep emf but lower internal resistance, increasing current capacity.
- Kirchhoff's junction rule expresses charge conservation (currents in = currents out); the loop rule expresses energy conservation (`Σ V = 0` around a loop). Assigned current directions are arbitrary; a wrong guess only flips a sign.
- A voltmeter connects in parallel (same voltage) and a galvanometer plus large series resistor; an ammeter connects in series (same current) and is a galvanometer plus a small shunt `R = r·(I_G/I)`.
- Every connected meter perturbs the circuit; ideal voltmeters have very high resistance and ideal ammeters near-zero resistance.
- Null measurements (potentiometer, Wheatstone bridge) achieve high accuracy by adjusting the circuit until zero detector current flows, so ratios cancel unknowns: `emf_x = emf_s·(R_x/R_s)`, `R_x = R₃R₂/R₁`.
- In an RC circuit the time constant is `τ = RC`; charging follows `V = emf(1 − e^(−t/RC))` reaching 63.2% of final at one τ, and discharging follows `V = V₀ e^(−t/RC)` falling to 36.8% at one τ.

## Key Quotes (paraphrased)
> A power source's emf is the voltage it produces at zero current; its terminal voltage is what you actually measure once current flows and internal resistance takes its toll.
> The junction rule is just charge conservation at a node, and the loop rule is just energy conservation around a closed path.
> A galvanometer becomes a voltmeter by adding a large series resistor and an ammeter by adding a small parallel shunt.
> Null methods are accurate precisely because no current flows through the detector at balance, so the act of measuring does not disturb the circuit.

## Connections
- [[ResistorsInSeriesAndParallel]] — series/parallel combination rules
- [[ElectromotiveForce]] — emf vs. terminal voltage of a real source
- [[InternalResistance]] — source resistance that lowers terminal voltage
- [[KirchhoffsRules]] — junction and loop rules for complex circuits
- [[Voltmeter]] — parallel-connected voltage meter from a galvanometer
- [[Ammeter]] — series-connected current meter from a galvanometer + shunt
- [[Galvanometer]] — the deflection mechanism underlying analog meters
- [[WheatstoneBridge]] / [[Potentiometer]] — null measurement instruments
- [[RCCircuit]] — resistor–capacitor transients
- [[TimeConstant]] — `τ = RC` charge/discharge timescale
- [[OhmsLaw]], [[ElectricalResistance]], [[Voltage]], [[ElectricCurrent]], [[ElectricPower]] — underlying circuit quantities
- [[Capacitor]], [[Capacitance]], [[ElectricPotential]] — basis for RC behavior
- [[GustavKirchhoff]] — namesake of the circuit rules

## Contradictions
- None found. Content is consistent with existing circuit/electricity concept pages and builds on Ch.20 (current, resistance, Ohm's law) and Ch.19 (capacitance).
