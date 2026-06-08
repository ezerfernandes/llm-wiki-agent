---
title: "Wake-Word Detection"
type: concept
tags: [tinyml, audio, mobile, hybrid, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Wake-Word Detection

Always-on listening for an acoustic trigger phrase ("Hey Siri", "Alexa", "Ding Dong") on dedicated **sub-milliwatt** hardware, which gates the activation of far more power-hungry components. A recurring example across [[TinyML]], [[MobileML|Mobile ML]], and [[HybridML|hybrid]] architectures in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

The wake-word model acts as an **aggressive power gate**: it does nothing but listen, preventing needless activation of the main application processor (which draws 100–1,000× more power). The entire energy-saving architecture fails if this always-on component exceeds its ~1 mW budget. It is the first stage of the canonical layered voice pipeline (TinyML wake-word → on-device/[[MobileML|mobile]] speech recognition → [[CloudML|cloud]] NLP) and the reason cloud-only voice processing is *physically impossible* at billion-device scale (the "voice assistant wall"). A close relative of the [[KeywordSpotting|keyword-spotting]] Lighthouse Model.

## Connections

- [[KeywordSpotting]] — the closely related Lighthouse Model / archetype.
- [[TinyML]] / [[EnergyHarvesting]] — the sub-mW regime it runs in.
- [[HybridML]] — wake-word is the first tier of the Progressive Deployment / Hierarchical Processing voice pipeline.
- [[MobileML]] / [[CloudML]] — the higher tiers the wake word gates.
- [[mlsysbook-ch02-ml-systems]] — source.
