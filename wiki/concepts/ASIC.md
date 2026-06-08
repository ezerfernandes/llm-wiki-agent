---
title: "ASIC (Application-Specific Integrated Circuit)"
type: concept
tags: [hardware, accelerators, asic, domain-specific]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# ASIC (Application-Specific Integrated Circuit)

An **application-specific integrated circuit** implements a single algorithm directly in silicon, achieving extreme efficiency — often $10^3×$ to $10^5×$ better performance-per-watt — at the cost of *total inflexibility*. If the core algorithm changes, an ASIC cannot be reprogrammed and becomes obsolete.

## Examples ([[mlsysbook-ch11-hardware-acceleration]])

- **Cryptographic hashing** for blockchain mining — fixed enough to justify dedicated silicon (Bedford Taylor 2017).
- **Sequence alignment / variant calling** for genomics (Shang 2018).
- Google's first-generation [[GoogleTPU|TPU]] is an ML inference ASIC: a 256×256 INT8 [[SystolicArray|systolic array]] that delivered 15–30× throughput-per-watt over contemporary GPUs by stripping away caches, branch prediction, and out-of-order logic.

## Trade-off vs. [[FPGA]]

The ASIC is the inflexible extreme of the specialization spectrum: maximum efficiency, zero post-fabrication adaptability. [[FPGA|FPGAs]] sacrifice some efficiency for reconfigurability, which suits evolving ML architectures.

## See also
- [[DomainSpecificArchitecture]] — the class an ML ASIC belongs to.
- [[FPGA]] — the reconfigurable counterpart.
- [[GoogleTPU]] — the canonical ML inference ASIC.
- [[HardwareSoftwareCodesign]] — why ASIC efficiency only materializes when algorithms match the silicon.
- [[mlsysbook-ch11-hardware-acceleration]] — ASIC efficiency/inflexibility trade-off.
