---
title: "I/O Device (Input/Output Device)"
type: concept
tags: [computer-architecture, von-neumann, peripherals, io]
sources: [dis-5-2-von-neumann]
last_updated: 2026-05-17
---

# I/O Device (Input/Output Device)

An **I/O device** is a peripheral that crosses the boundary between the computer and the outside world — bringing external data **in** ([[InputDevice|input]]) or relaying computational results **out** ([[OutputDevice|output]]). The two I/O units are the **fourth and fifth** of the [[VonNeumannArchitecture|von Neumann architecture]]'s five functional units ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]), alongside the [[ControlUnit|control unit]], [[ProcessingUnit|processing unit]], and [[RAM|memory unit]].

## Input vs output

- **[[InputDevice|Input devices]]** load external program data and instructions into the computer and signal execution start — *keyboard, mouse, camera, microphone, scanner*.
- **[[OutputDevice|Output devices]]** store or display the program's results — *monitor, speakers, printer, haptic actuators*.
- **Bidirectional devices** function as **both** input and output — *touchscreens* (display + input), *storage drives* (read + write), *network interfaces*.

## Role in the architecture

I/O devices interface with the [[CPU]] over the [[Bus|system buses]] — the [[ControlBus|control bus]] carries device commands and interrupts, the [[AddressBus|address bus]] carries memory-mapped I/O addresses, and the [[DataBus|data bus]] carries the actual bytes moving between device and [[RAM|memory]] / [[CpuRegister|register]].

The I/O units make the [[StoredProgram|stored-program]] principle *useful* in practice: programs can be **loaded** from external storage (rather than rewired in plugboards) and results can be **delivered** to humans — the operational closure of the architecture.

## Connections

- [[VonNeumannArchitecture]] — the architecture that names I/O devices as two of its five units.
- [[InputDevice]] / [[OutputDevice]] — the directional children.
- [[Bus]] — how I/O devices communicate with [[CPU]] and [[RAM|memory]].
- [[CPU]] — coordinates I/O traffic.
- [[RAM]] — the destination/source of most I/O transfers.
- [[StoredProgram]] — I/O is how programs *enter* the addressable memory in the first place.
- [[dis-5-2-von-neumann]] — source.
