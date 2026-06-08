---
title: "Hardware Mapping (AI Acceleration)"
type: concept
tags: [hardware, accelerators, mapping, dataflow, compilers]
sources: [mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Hardware Mapping (AI Acceleration)

**Mapping** is the process of binding a logical computation graph to the physical hardware topology — deciding *which* operations run on *which* processing elements, *where* data resides in the [[MemoryHierarchy|memory hierarchy]], and *in what order*. Where the [[RooflineModel|Roofline Model]] *diagnoses* whether an operation is compute- or memory-bound, mapping *prescribes* how to execute it efficiently.

## The three coupled decisions ([[mlsysbook-ch11-hardware-acceleration]])

1. **Computation placement** — assigning ops to processing elements (an H100 has >16,000 streaming processors, [[Cerebras]] CS-2 has ~850,000 cores; small inefficiencies compound).
2. **Memory allocation** — keeping frequently used data close to compute; accelerators require *explicit* placement (no transparent caches), or pay latency/energy/stall penalties.
3. **Dataflow & scheduling** — the [[WeightStationary|stationary-operand]] strategies plus [[KernelFusion|kernel fusion]] and [[Tiling|tiling]].

## Why it is hard and automated

Mapping targets a **dataflow architecture** where moving data costs ~200× a MAC, so a poor tiling choice can cut effective [[ArithmeticIntensity|arithmetic intensity]] 10–50× and collapse a compute-bound op into a bandwidth-bound one. The search space is too large to hand-tune at scale, so [[XLA]], [[TVM]], and [[MLIR]] automate it (though compiler mappings for specialized accelerators can still be 20–50% off hand-tuned schedules). Real models use **hybrid mapping**, switching strategy per layer (weight-stationary for CNNs, activation-stationary for attention, output-stationary where write traffic dominates).

## See also
- [[WeightStationary]] / [[OutputStationary]] — the dataflow choices mapping selects among.
- [[KernelFusion]] / [[Tiling]] / [[FlashAttention]] — the data-movement techniques mapping applies.
- [[RooflineModel]] / [[ArithmeticIntensity]] — the diagnosis mapping responds to.
- [[XLA]] / [[TVM]] / [[MLIR]] — the compilers that automate mapping.
- [[DAMTaxonomy]] — mapping is the Machine-axis decision.
- [[mlsysbook-ch11-hardware-acceleration]] — mapping definition, the three decisions, and per-architecture strategies.
