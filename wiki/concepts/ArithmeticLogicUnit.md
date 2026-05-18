---
title: "Arithmetic / Logic Unit (ALU)"
type: concept
tags: [computer-architecture, cpu, von-neumann, alu]
sources: [dis-5-2-von-neumann, dis-5-1-history]
last_updated: 2026-05-17
---

# Arithmetic / Logic Unit (ALU)

The **arithmetic / logic unit (ALU)** is the part of the [[CPU]]'s [[ProcessingUnit|processing unit]] that **performs the actual computation** — arithmetic operations (addition, subtraction, multiplication, division), [[BooleanAlgebra|boolean]] / logical operations, and comparisons. It is one of the two halves of the [[ProcessingUnit|processing unit]] (the other being the [[CpuRegister|register]] file) in the [[VonNeumannArchitecture|von Neumann architecture]] ([[dis-5-2-von-neumann|*Dive into Systems* Ch 5.2]]).

Where the [[ControlUnit|control unit]] decides *what* to do and *when*, the ALU is *how* — the data-path circuit that consumes operand values (from [[CpuRegister|registers]] or [[RAM|memory]]) and produces a result that the [[ControlUnit|control unit]] then stores back.

## Role in the fetch-decode-execute cycle

The ALU is the active element of the **execute** phase of the [[FetchDecodeExecuteCycle|fetch-decode-execute-store cycle]]:

- **Fetch** ([[ControlUnit|control unit]]) — read next instruction from [[RAM|memory]].
- **Decode** ([[ControlUnit|control unit]]) — identify operation, fetch operand values.
- **Execute** (**ALU**) — perform the arithmetic / logical operation on operands.
- **Store** ([[ControlUnit|control unit]]) — write result back to [[CpuRegister|registers]] or [[RAM|memory]].

## Connections

- [[CPU]] — the ALU lives inside the [[CPU]]'s [[ProcessingUnit|processing unit]].
- [[ProcessingUnit]] — the ALU's enclosing unit; the other half is the [[CpuRegister|register]] file.
- [[ControlUnit]] — drives the ALU; sequences operands in and results out.
- [[CpuRegister]] — the ALU's typical operand source and destination.
- [[FetchDecodeExecuteCycle]] — the ALU is the heart of the *execute* phase.
- [[VonNeumannArchitecture]] — the architecture that places the ALU here.
- [[BooleanAlgebra]] — the algebraic substrate of the ALU's logical-op circuits ([[ClaudeShannon|Shannon]] 1937).
- [[BinaryAddition]] / [[BinarySubtraction]] / [[BinaryMultiplication]] / [[BinaryDivision]] — the algorithms [[dis-4-4-arithmetic|Ch 4.4]] explored at the bit-pattern level that the ALU's circuits implement.
- [[dis-5-2-von-neumann]] — primary source.
- [[dis-5-1-history]] — historical context.
