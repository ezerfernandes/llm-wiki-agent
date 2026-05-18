---
title: "Von Neumann Architecture"
type: concept
tags: [computer-architecture, foundational, stored-program]
sources: [dis-5-1-history, dis-5-2-von-neumann, embedded-controllers-fiore]
last_updated: 2026-05-17
---

# Von Neumann Architecture

The **structural template of essentially every modern computer**, codified in [[JohnVonNeumann|John von Neumann]]'s 1945 [[EDVAC|*First Draft of a Report on the EDVAC*]]. Synthesized prior engineering work on [[ENIAC]], [[Z3]], [[Colossus]], and [[HarvardMarkI|Mark I]] into a clean abstract model.

## The core idea: stored-program

**Program instructions and data both reside in the same internal [[RAM|memory]]**, addressed uniformly. This is the [[StoredProgram|stored-program]] principle — the architectural break that distinguished modern computers from their plugboard-programmed predecessors ([[ENIAC]] in its original 1945 form). Per [[dis-5-2-von-neumann|Ch 5.2]] the operational form of this principle is *"there is no distinction between instructions and data in the von Neumann architecture"* — both share [[RAM|memory]] **and** share [[CpuRegister|register]] storage.

## The five functional units

[[dis-5-2-von-neumann|Ch 5.2]] decomposes the architecture into **five units** organized around the [[Bus|system buses]]:

- **[[CPU]]** = **[[ControlUnit|control unit]]** + **[[ProcessingUnit|processing unit]]**
  - **[[ControlUnit|Control unit]]** — drives the [[FetchDecodeExecuteCycle|fetch-decode-execute cycle]]; owns the [[ProgramCounter|program counter (PC)]] and [[InstructionRegister|instruction register (IR)]]
  - **[[ProcessingUnit|Processing unit]]** = **[[ArithmeticLogicUnit|ALU]]** + **[[CpuRegister|registers]]** — performs arithmetic / [[BooleanAlgebra|Boolean]] operations; each [[CpuRegister|register]] holds one [[DataWord|word]]
- **[[RAM|Memory unit]]** — [[ByteAddressable|byte-addressable]] storage for both instructions and data; a 32-bit [[AddressBus|address bus]] caps it at $2^{32}$ bytes (4 GiB)
- **[[InputDevice|Input unit]]** — keyboard, mouse, camera, microphone — brings external data in
- **[[OutputDevice|Output unit]]** — monitor, speakers, haptics — relays results out (touchscreens / storage drives / NICs are bidirectional [[IODevice|I/O devices]])

The five units are connected by three [[Bus|system buses]] — the [[ControlBus|control bus]] (commands), [[AddressBus|address bus]] (memory addresses), and [[DataBus|data bus]] (the actual bytes).

## The fetch-decode-execute cycle

The architecture's *operational heart* (see [[FetchDecodeExecuteCycle]] for the full treatment):

1. **Fetch** the instruction at the address in the [[ProgramCounter|program counter (PC)]] from [[RAM|memory]] into the [[InstructionRegister|instruction register (IR)]]; increment PC
2. **Decode** the [[InstructionRegister|IR]]'s opcode and operand locations; fetch operand values from [[CpuRegister|registers]] or [[RAM|memory]]
3. **Execute** the operation via the [[ArithmeticLogicUnit|ALU]]
4. **Store** the result back to [[CpuRegister|register]] / [[RAM|memory]] via the [[DataBus|data]] / [[AddressBus|address]] / [[ControlBus|control]] buses
5. Repeat (the new [[ProgramCounter|PC]] now points at the next instruction — or at a branch target)

## The von Neumann bottleneck

Because instructions and data share a single memory and a single bus, sustained throughput is limited by **memory bandwidth** — the *von Neumann bottleneck*. Modern [[CPU]]s mitigate this with the [[MemoryHierarchy]] ([[CPUCache|caches]]), pipelining, and out-of-order execution.

## Relation to alternatives

The **[[HarvardArchitecture|Harvard architecture]]** (separate instruction and data memories) is the principal alternative, used in many [[Microcontroller|microcontrollers]] and DSPs. Modern general-purpose [[CPU]]s present a unified-memory von Neumann model to software but internally use Harvard-style **split L1 caches** (separate I-cache and D-cache).

Per [[dis-5-1-history|*Dive into Systems* Ch 5.1]], the *von Neumann architecture* label is a partial misnomer — the synthesis was a collaborative achievement, but only von Neumann's name attached to the published paper, which is why the architecture bears his name alone.
