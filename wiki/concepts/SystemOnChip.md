---
title: "System-on-Chip (SoC)"
type: concept
tags: [hardware, mobile, embedded, mlsysbook, energy]
sources: [mlsysbook-ch02-ml-systems, mlsysbook-ch11-hardware-acceleration]
last_updated: 2026-06-05
---

# System-on-Chip (SoC)

An integrated circuit that combines **CPU, GPU, and [[NeuralProcessingUnit|NPU]] cores with shared memory on a single die**. The hardware substrate of [[MobileML|Mobile ML]] in [[VijayJanapaReddi|Reddi]]'s *Machine Learning Systems* ([[mlsysbook-ch02-ml-systems|Vol 1, Ch 2]]).

Tight integration minimizes the physical energy cost of data movement — accessing off-chip memory consumes **>100× more energy** than on-chip access — which is mandatory for mobile battery life. The trade-off is that this same integration imposes the memory-bandwidth constraint (LPDDR5) that caps mobile models at the 10–100 MB scale. Mobile ML partitions workloads across the SoC's heterogeneous units by power tier: a dedicated low-power core runs always-on [[WakeWordDetection|wake-word detection]] (<1 mW), the NPU handles speech recognition (<10 ms), and the GPU/CPU handle bursty tasks.

## Connections

- [[NeuralProcessingUnit]] — the AI-specialized block on the SoC.
- [[MobileML]] — the paradigm the SoC powers.
- [[MemoryWall]] — the bandwidth constraint SoC integration both mitigates (on-chip) and imposes (off-chip).
- [[ComputationalPhotography]] — a pipeline scheduled across the SoC's CPU/GPU/NPU.
- [[mlsysbook-ch02-ml-systems]] — source.
- [[mlsysbook-ch11-hardware-acceleration]] — Ch 11's heterogeneous-SoC section: coordinating CPU/GPU/DSP/NPU is "a coordination problem, not a hardware inventory" (object-detection split NPU/CPU/GPU shifts with battery and thermal state); coordinated DVFS, thermal-throttling-via-migration, [[Qualcomm]] Snapdragon, and automotive real-time/functional-safety constraints.
