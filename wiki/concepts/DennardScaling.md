---
title: "Dennard Scaling"
type: concept
tags: [computer-architecture, hardware, scaling, power, history, mlsysbook]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# Dennard Scaling

The scaling law (Robert Dennard, IBM, 1974) that as transistors shrink, voltage and current scale proportionally, **keeping power density constant** — delivering "free" per-generation performance gains for three decades. Its breakdown is the root cause of the [[PowerWall|power wall]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Under classical Dennard scaling, dynamic power related to frequency cubically:

$$\text{Power} \propto C\times V^2\times f \quad\text{with } V\propto f \implies \text{Power}\propto f^3$$

So doubling clock frequency required ~8× more power. When leakage current made further voltage reduction impossible around the 90 nm node (~2005–2006), power density began rising each generation — **ending single-core frequency scaling** and forcing the industry toward the *parallelism* (multi-core) and *specialization* (GPUs, [[GoogleTPU|TPUs]], [[NeuralProcessingUnit|NPUs]]) that now defines ML hardware. This is why [[MobileML|mobile ML]] hits a hard thermal ceiling at 2–5 W.

## Connections

- [[PowerWall]] — the constraint Dennard's breakdown created.
- [[MemoryWall]] / [[SpeedOfLight]] — the other two physical constraints in mlsysbook's deployment framework.
- [[ThermalWall]] / [[ThermalThrottling]] — the mobile consequence.
- [[MooresLaw]] — the transistor-count law that continued after Dennard scaling ended.
- [[GoogleTPU]] / [[NeuralProcessingUnit]] — the specialization response.
- [[mlsysbook-ch02-ml-systems]] — source.
