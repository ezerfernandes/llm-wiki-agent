---
title: "Systems of Measurement"
type: concept
tags: [math, prealgebra, measurement, units]
sources: [prealgebra-2e-ch07-properties-of-real-numbers]
last_updated: 2026-06-07
---

# Systems of Measurement

OpenStax [[Prealgebra]] 2e (Chapter 7, [[prealgebra-2e-ch07-properties-of-real-numbers]], §7.5) covers the two everyday systems of units — the **US customary system** and the **metric system** — the procedure for **converting** units, and **temperature** conversion. The unit-conversion method is an application of the **multiplicative identity** ([[IdentityInverseZeroProperties]]): you multiply a measurement by a fraction that equals `1`.

## US customary system
| Quantity | Equivalences |
|---|---|
| Length | 1 ft = 12 in · 1 yd = 3 ft · 1 mi = 5,280 ft |
| Weight | 1 lb = 16 oz · 1 ton = 2,000 lb |
| Volume | 3 tsp = 1 tbsp · 16 tbsp = 1 cup · 1 cup = 8 fl oz · 1 pt = 2 cups · 1 qt = 2 pt · 1 gal = 4 qt |
| Time | 1 min = 60 s · 1 hr = 60 min · 1 day = 24 hr · 1 wk = 7 days · 1 yr = 365 days |

The relationships are **non-decimal** (12, 16, 5,280, …), which is what makes this system harder to convert in than the metric system.

## Unit conversion by conversion factors
To convert a measurement, **multiply by a conversion factor** — a fraction equal to `1` because its numerator and denominator name the same quantity (e.g. `1 ft / 12 in`). Arrange the factor so the **old unit cancels** ("divides out") and the **new unit remains**:

> `60 in × (1 ft / 12 in) = 60/12 ft = 5 ft`

Because the factor equals `1`, multiplying by it changes the units but not the amount — the **identity property of multiplication** at work. For **multi-step** conversions, chain several factors (e.g. weeks → days → hours → minutes), each canceling the previous unit.

## Metric system
The metric system is **base-10**: every unit relates to the base unit by a power of ten, named with standard **prefixes**.

| Prefix | Meaning |
|---|---|
| kilo- | 1,000 |
| centi- | 1/100 |
| milli- | 1/1,000 |

- **Length:** millimeter (mm), centimeter (cm), meter (m), kilometer (km).
- **Mass:** milligram (mg), gram (g), kilogram (kg).
- **Volume/capacity:** milliliter (mL), liter (L), kiloliter (kL).

The same conversion-factor method applies, but because the system is base-10 you can also just **shift the decimal point**: to multiply by 1,000 move the point 3 places right; to multiply by 0.001 move it 3 places left.

## Converting between US and metric
Approximate equivalences let you cross between systems with the same conversion-factor method:

- 1 in = 2.54 cm
- 1 ft = 0.305 m
- 1 lb = 0.45 kg
- 1 qt = 0.95 L
- 1 fl oz = 30 mL

## Temperature conversion
Fahrenheit (°F) and Celsius (°C) are related by a linear pair of formulas:

> `C = (5/9)(F − 32)`   (Fahrenheit → Celsius)
> `F = (9/5)C + 32`     (Celsius → Fahrenheit)

## Worked-example types (§7.5)
Single-unit conversions; multi-step conversions (weeks → minutes); mixed-unit arithmetic (adding or multiplying measurements expressed in several units); real-world applications (an athlete's distances, package weights, recipe scaling); and temperature conversions both directions.

## Connections
- [[IdentityInverseZeroProperties]] — a conversion factor equals `1`, so converting is the multiplicative-identity property in action.
- [[UnitConversion]] — the wiki's physics treatment of the same conversion-factor / dimensional-analysis method.
- [[SIUnits]] — the formal International System; the metric units here are its everyday subset.
- [[TemperatureMeasurement]] — the chemistry treatment of the F/C (and Kelvin) scales and the same conversion formulas.
- [[Fraction]] / [[Decimal]] / [[DecimalArithmetic]] — conversion factors are fractions; metric conversion shifts the decimal point.
- [[Ratio]] — a conversion factor is a unit ratio equal to 1.
- [[RealNumbers]] — measurements are real-number quantities.
- [[prealgebra-2e-ch07-properties-of-real-numbers]] — source (Ch 7.5).
