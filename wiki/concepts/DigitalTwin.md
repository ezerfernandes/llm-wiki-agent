---
title: "Digital Twin"
type: concept
tags: [architecture, system-design, simulation]
sources: [leh-ch01-understanding-llm-twin-concept]
last_updated: 2026-05-22
---

## Definition
A **digital twin** is a 1:1 digital representation of a physical entity — a person, machine, building, or system — built and continuously updated so that the digital model mirrors the state and behavior of its physical counterpart.

## In LLM Engineer's Handbook
[[leh-ch01-understanding-llm-twin-concept]] invokes the digital-twin concept as the generalization that motivates the book's central project: an [[LLMTwin]] is the LLM-specific instance of a digital twin where the "entity" is a person and the mirrored properties are their writing style, voice, and personality. The chapter frames the twin as a "projection" rather than a perfect copy — "as with any other projection, you lose a lot of information along the way" — making clear that a digital twin is bounded by the data observable about the source entity.

## Key details
- A digital twin is more than a model: it is a representation kept in (semi-)continuous sync with the real-world counterpart, which in the LLM Twin case means ongoing data collection plus periodic [[ContinuousTraining|CT]].
- The chapter contrasts a *twin* (1:1) with a *[[CoPilot|co-pilot]]* (generic augmentation), arguing the twin abstraction is the right mental model for personalized AI assistants.
- Cross-domain applications cited or alluded to: manufacturing (machine twins), urban planning (city twins), healthcare (patient twins).

## Connections
- [[LLMTwin]] — the book's LLM-specific instantiation of a digital twin.
- [[CoPilot]] — generic-augmentation alternative the book explicitly distinguishes from a twin.
- [[StyleTransfer]] — the image-domain analogue the book invokes for "Van Gogh style applied to your own persona."
- [[FineTuning]] — the primary mechanism by which the digital model is shaped to its source.
