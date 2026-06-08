---
title: "Ultrasound"
type: concept
tags: [physics, acoustics, waves, medical-imaging]
sources: [college-physics-2e-ch17]
last_updated: 2026-06-07
---

## Definition
Ultrasound is [[Sound]] at frequencies above 20 kHz, beyond human hearing. Its short wavelengths and partial reflection at tissue boundaries make it valuable for medical imaging and therapy, as well as industrial sensing.

## Key Points
- A **transducer** (piezoelectric crystal) both emits ultrasound pulses and detects their echoes.
- Echoes form at boundaries between media of differing [[AcousticImpedance]]; the **intensity reflection coefficient** quantifies how much reflects. Similar soft-tissue impedances reflect weakly (~1.4% at a fat–muscle boundary), letting the beam penetrate to image deeper structures.
- Resolution cannot exceed the wavelength of the probing wave; effective tissue scanning depth is roughly 500 wavelengths.
- **Doppler-shifted ultrasound** measures velocity of moving reflectors (e.g., blood). A double shift occurs — blood receives a shifted frequency, then re-radiates as a moving source — and the small difference is read as an audible **beat frequency**.
- **Cavitation** (vapor bubbles forming and collapsing) can damage tissue at high intensity and is used therapeutically and for cleaning.

## Equations
- Acoustic impedance: `Z = ρ·v`
- Reflection coefficient: `a = [(Z₂ − Z₁) / (Z₁ + Z₂)]²`
- Doppler shift: `f_obs = f_s · (v_w ± v_obs)/v_w` or `f_s · v_w/(v_w ∓ v_s)`
- Beat frequency: `f_B = |f₁ − f₂|`

## Related
- [[AcousticImpedance]], [[DopplerEffect]], [[Sound]], [[SpeedOfSound]]
- Applications: fetal/cardiac imaging, blood-flow measurement, gallstone/tumor destruction (10³–10⁵ W/m²), diathermy (0.8–1 MHz), sonar, flaw detection.
