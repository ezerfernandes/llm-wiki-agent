---
title: "Energy Quantization (Planck)"
type: concept
tags: [chemistry, general-chemistry, quantum-chemistry, physics]
sources: [chemistry-2e-ch06-electronic-structure-periodic-properties, college-physics-2e-ch29]
last_updated: 2026-06-07
---

# Energy Quantization (Planck)

**Energy quantization** is the principle that energy can take only discrete (not continuous) values. In atomic and molecular systems, energy is exchanged in fixed-size packets rather than arbitrary amounts.

> Disambiguation: this is the *physics* concept of quantized energy. The ML/model-compression sense of "quantization" lives at [[Quantization]] (precision reduction) and [[WaveQuantization]] (GPU warp tax) — unrelated.

## The Ultraviolet Catastrophe
Classical physics modeled a heated **blackbody** (an ideal emitter) as radiating energy continuously, predicting that intensity should grow without bound at short wavelengths — the "ultraviolet catastrophe," absurdly implying room-temperature objects glow in the UV. Observed blackbody curves instead peak and fall (λmax shifting to shorter wavelengths as temperature rises, Wien's law).

## Planck's Solution (c. 1900)
Max Planck matched the experimental curves exactly by assuming a vibrating atom can have only discrete energies for each frequency:

> **E = nhν**, where n = 1, 2, 3, …

with **Planck's constant h = 6.626 × 10⁻³⁴ J·s** (see [[PlancksConstant]]). The extremely small value of h is why quantization is invisible in everyday macroscopic phenomena. Planck himself could not explain *why* energy is quantized — it was [[AlbertEinstein|Einstein]] who took the idea literally for light (see [[PhotonQuantum]]).

## Physics formulation (College Physics 2e Ch.29)
College Physics 2e frames the oscillating atoms of a [[BlackbodyRadiation|blackbody]] as having quantized energies, with adjacent levels spaced by ΔE = hf:

> **E = (n + ½)hf**, where n = 0, 1, 2, 3, …

Higher temperature shifts the radiated peak to shorter wavelengths and raises total intensity as T⁴ (Stefan-Boltzmann). For example, at f = 10¹⁴ Hz the energy step is ~0.4 eV — significant atomically but negligible macroscopically, which is exactly the [[WaveParticleDuality|correspondence principle]] in action. The same quantization governs [[PhotonQuantum|photon]] energies, the [[PhotoelectricEffect|photoelectric effect]], and discrete [[AtomicSpectra|line spectra]].

## Significance
Quantization is the thread running through the whole chapter: standing waves (integer half-wavelengths), the [[PhotoelectricEffect|photoelectric effect]], discrete [[AtomicSpectra|line spectra]], and the [[BohrModel|Bohr model]]'s quantized orbits all follow from energy coming in discrete amounts.

## Connections
- [[MaxPlanck]] — proposed energy quantization
- [[PhotonQuantum]] — Einstein extended quantization to light
- [[ElectromagneticRadiation]] — blackbody curves are continuous EM spectra
- [[AtomicSpectra]] / [[BohrModel]] — quantized atomic energy levels
- [[BlackbodyRadiation]] — the spectrum quantization explains
- [[PlancksConstant]] — h, the quantum-scale constant
- [[Quantization]] / [[WaveQuantization]] — unrelated ML/GPU senses (disambiguation)
- [[chemistry-2e-ch06-electronic-structure-periodic-properties]] — source chapter (chemistry)
- [[college-physics-2e-ch29]] — source chapter (physics)
