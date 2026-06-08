---
title: "FPGA (Field-Programmable Gate Array)"
type: concept
tags: [hardware, accelerators, fpga, reconfigurable]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# FPGA (Field-Programmable Gate Array)

A **field-programmable gate array** is a chip whose logic fabric is *configurable after manufacturing*, in contrast to the fixed-function silicon of an [[ASIC]]. Engineers describe custom hardware pipelines in a hardware description language (Verilog/VHDL) and "program" the gate array to match a specific workload.

## Why it matters for ML ([[mlsysbook-ch11-hardware-acceleration]])

Reconfigurability makes FPGAs attractive for **rapidly evolving ML architectures**, where committing to an [[ASIC]] risks obsolescence if the core algorithm changes. They can improve performance for latency-sensitive data-center services by implementing custom pipelines (Putnam et al. 2014).

## Trade-off

The barrier is productivity: programming requires hardware description languages and compilation times measured in **hours**, limiting adoption to deployments where the efficiency benefit justifies the engineering cost. ML compilers can emit optimized bytecode or execution graphs for FPGA targets that the hardware's runtime then interprets.

## See also
- [[ASIC]] — the fixed-function extreme; FPGAs trade some efficiency for reconfigurability.
- [[DomainSpecificArchitecture]] — the broader class of specialized silicon.
- [[GPU]] / [[GoogleTPU]] / [[NeuralProcessingUnit]] — alternative accelerator classes.
- [[mlsysbook-ch11-hardware-acceleration]] — FPGA reconfigurability vs. ASIC obsolescence trade-off.
