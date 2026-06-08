---
title: "Energy Harvesting"
type: concept
tags: [tinyml, embedded, power, mlsysbook]
sources: [mlsysbook-ch02-ml-systems]
last_updated: 2026-06-05
---

# Energy Harvesting

Powering a device from **ambient energy** (solar, thermoelectric, RF) rather than a battery — the capability that defines the [[TinyML]] "deploy and forget" operating model in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

The **1 mW threshold** is not arbitrary: below ~1 mW, a device can be powered indefinitely by thumbnail solar cells (~10 mW outdoors, ~10 µW indoors), thermoelectric generators on warm pipes (~100 µW), or RF energy from nearby transmitters (~10 µW). Crossing this threshold transforms deployment from "battery-limited lifetime" to "deploy and forget," which is *why* 1 mW marks the physical boundary that makes TinyML a distinct paradigm rather than a scaled-down [[EdgeML|edge]] device. A keyword-spotting model at ~10 µJ/inference runs for years on a coin cell (CR2032 ≈ 675 mWh) or indefinitely on harvested energy; the regime drives [[Microcontroller|microcontroller]] sleep/wake (intermittent computing).

## Connections

- [[TinyML]] — the paradigm energy harvesting enables.
- [[Microcontroller]] — the sub-1-mW substrate.
- [[KeywordSpotting]] / [[WakeWordDetection]] — the canonical sub-mW always-on workloads.
- [[PowerWall]] — the broader power-constraint context.
- [[mlsysbook-ch02-ml-systems]] — source.
