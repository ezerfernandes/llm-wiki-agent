---
title: "D·A·M Taxonomy"
type: concept
tags: [ml-systems, diagnostic, mlsysbook, framework, foundations]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch03-ml-workflow, mlsysbook-ch05-neural-computation, mlsysbook-ch08-model-training, mlsysbook-ch10-model-compression, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch12-benchmarking, mlsysbook-ch14-ml-operations, mlsysbook-ch15-responsible-engineering, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# D·A·M Taxonomy (Data · Algorithm · Machine)

A **diagnostic framework that classifies any ML-system performance bottleneck along three interdependent axes** and asks the recurring question: *"Which axis is the binding constraint?"* Introduced in Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) as the operational counterpart to the [[AITriad|AI Triad]].

| Axis | Variables | Role | Metaphor |
|---|---|---|---|
| **Data** | $D_{vol}$, bandwidth $\text{BW}$ | what the system learns | the Fuel |
| **Algorithm** | operation count $O$, model architecture | how patterns are captured | the Blueprint |
| **Machine** | peak throughput $R_{peak}$, memory capacity | computation speed & location | the Engine |

## Key ideas

- **The axes are not independent.** Changing the algorithm (e.g. CNN → transformer) typically mandates a different machine (more memory for $\mathcal{O}(S^2)$ attention) *and* a different data distribution.
- **The moving bottleneck.** Relieving one axis shifts the limit to another — faster GPUs (Machine) can expose storage that can't feed data fast enough (Data); a bigger model (Algorithm) can exceed memory (Machine).
- **Worked example.** Batch-size-1 [[ResNet50|ResNet-50]] on an A100 is *memory-bound*: arithmetic intensity sits below the A100 FP16 ridge point, so buying peak FLOP/s alone won't help — the binding axis is the Machine (data reuse, bandwidth, utilization). See [[RooflineModel]].
- **Maps to the [[IronLawOfMLSystems|iron law]]** term-by-term and to the three [[EfficiencyFramework|efficiency dimensions]].
- **D·A·M × Phase.** [[mlsysbook-ch02-ml-systems|Ch 2]] shows each axis behaves differently in training vs. inference: Data (massive throughput / shuffling vs. low-latency single samples), Algorithm (bidirectional forward+backward vs. unidirectional forward-only with frozen weights), Machine (throughput-optimized clusters vs. latency-optimized edge accelerators). "When bottlenecks shift unexpectedly, check which phase is being optimized." Different [[DeploymentSpectrum|paradigms]] also bind on different axes — cloud on Algorithm, microcontroller on Machine.

- **D·A·M applied to training bottlenecks.** [[mlsysbook-ch08-model-training|Ch 8]] maps each axis to a training bottleneck with a profiler signature and a fix: **Algorithm** → compute-bound (util >90%, arithmetic units saturated) → [[FlashAttention]], [[MixedPrecisionTraining|mixed precision]], faster hardware; **Machine** → memory-bound (util 50–80%, high bandwidth use) → operator fusion, memory-efficient attention, reduced precision; **Data** → data-bound (periodic util→0, CPU busy in the gaps) → [[DataPrefetching|prefetching]], pipeline overlap, faster storage, DataLoader parallelism. Diagnosis runs off [[MFU]] + the profiler trace; the data-bound case (the "GIL-locked GPU") is the most commonly misdiagnosed.

## Connections

- [[mlsysbook-ch08-model-training]] — the D·A·M-to-training-bottleneck mapping and the profile→diagnose→fix→reprofile methodology.
- [[AITriad]] — the conceptual form of the same three elements.
- [[IronLawOfMLSystems]] — the quantitative decomposition; D·A·M maps onto its three terms.
- [[MachineLearningSystems]] — the systems this taxonomy diagnoses.
- [[RooflineModel]] / [[ArithmeticIntensity]] / [[MemoryWall]] — the Machine-axis physics.
- [[EfficiencyFramework]] — algorithmic / compute / data-selection efficiency, one per axis.
- [[LighthouseModel]] — five workloads that each stress a different axis.
- [[WorkloadArchetype]] — classifies workloads by the binding D·A·M/iron-law constraint.
- [[SystemsThinking]] — [[mlsysbook-ch03-ml-workflow|Ch 3]] draws the Triad's deepest lesson: D, A, M *interact* (data constrains feasible algorithms; the algorithm dictates feasible hardware; hardware reshapes processable data), so they must be co-designed, not optimized in isolation.
- [[USPSDigitRecognition]] — [[mlsysbook-ch05-neural-computation|Ch 5]]'s closing case study showing the D·A·M alignment in action: [[LeNet]] matched the task (Algorithm), diverse handwriting captured variation (Data), specialized hardware met latency (Machine). "When performance stalls, the diagnostic question is *where* the flow is blocked — check the D·A·M."
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] / [[mlsysbook-ch03-ml-workflow]] / [[mlsysbook-ch05-neural-computation]] — sources.
- [[mlsysbook-ch10-model-compression]] — [[ModelCompression|model compression]] is the **A (Algorithm)** axis seen from the model side; [[Quantization|quantization]] specifically activates the **M (Machine)** axis (it pays off only when the hardware has INT8/INT4 units), and the [[ConservationOfComplexity|conservation of complexity]] frames compression as *relocating* work among D, A, and M.
- [[mlsysbook-ch11-hardware-acceleration]] — the full **M (Machine)** axis: [[DomainSpecificArchitecture|hardware specialization]], [[ComputePrimitives|compute primitives]], the [[MemoryWall|memory wall]], the [[RooflineModel|Roofline]] diagnostic, and [[HardwareMapping|mapping]]/dataflow — the longest chapter in the book, completing the D·A·M optimization stack before benchmarking.
- [[mlsysbook-ch12-benchmarking]] — [[Benchmarking|benchmarking]] (Ch 12) maps its **three evaluation dimensions directly onto D·A·M**: system benchmarks = Machine, model benchmarks = Algorithm, data benchmarks = Data. The chapter's D·A·M bottleneck diagnostic matrix (each axis × compute/memory/I/O-bound) is the first step when a benchmark reveals underutilization — "where is the flow blocked? Check the D·A·M."
- [[mlsysbook-ch14-ml-operations]] — mlsysbook Vol 1 Ch 14 applies the D·A·M taxonomy as a production diagnostic for latency-budget bottlenecks and the data-first debugging decision tree.
- [[mlsysbook-ch15-responsible-engineering]] — mlsysbook Vol 1 Ch 15 extends D·A·M into the diagnostic spine for *responsibility* failures: biased **Data** ([[Amazon]] recruiting), a proxy **Algorithm** objective ([[COMPAS]], [[Optum]]), and energy-hungry **Machine** infrastructure ([[CarbonFootprint|carbon]]); Zillow is read as all three.
- [[mlsysbook-ch16-conclusion]] — the conclusion names D/A/M as the **three destinations across which the [[ConservationOfComplexity|conservation of complexity]] moves work** — every one of the [[ThirteenQuantitativeInvariants|thirteen invariants]] quantifies a consequence of where complexity currently resides among Data, Algorithm, and Machine. At [[WarehouseScaleComputer|fleet scale]] "the AI Triad still applies, but the 'Machine' is now a global infrastructure."

