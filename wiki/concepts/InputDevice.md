---
title: "Input Device"
type: concept
tags: [computer-architecture, von-neumann, io, peripherals]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# Input Device

An **input device** is a peripheral that **brings external data and instructions into the computer** — the third of the [[VonNeumannArchitecture|von Neumann architecture]]'s five functional units (counted alongside the [[ControlUnit|control unit]], [[ProcessingUnit|processing unit]], [[RAM|memory unit]], and [[OutputDevice|output unit]]). Per [[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]: keyboard, mouse, camera, microphone, scanner.

Some devices (touchscreens, storage drives, network interfaces) function as **both** input and output — see [[IODevice]] for the umbrella treatment.

## Connections

- [[IODevice]] — umbrella concept; the bidirectional case.
- [[OutputDevice]] — sibling.
- [[Bus]] — how input devices reach [[CPU]] / [[RAM|memory]].
- [[VonNeumannArchitecture]] — the architecture that names it.
- [[dis-5-2-von-neumann]] — source.
