---
title: "Thirteen Quantitative Invariants"
type: concept
tags: [ml-systems, principle, mlsysbook, physics, synthesis, foundations]
sources: [mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Thirteen Quantitative Invariants

The **integrated analytical framework** that [[mlsysbook-ch16-conclusion|mlsysbook Vol 1's conclusion]] consolidates from the quantitative principles introduced across all four Parts of the book. They are *invariants* — constraints rooted in **physics, information theory, and statistics** — not best practices that evolve with fashion. "Technologies will change; the physics and the trade-offs will not." Each was introduced in the Part where its governing constraint first becomes visible, and all thirteen are unified by a single meta-principle, the [[ConservationOfComplexity|conservation of complexity]].

## The thirteen, by Part

**Foundations — data physics (where complexity originates):**
1. **Data as Code Invariant** — System Behavior ≈ f(Data); changing the data changes the program.
2. **[[DataGravity|Data Gravity Invariant]]** — moving data costs ≫ moving compute; move compute to the data.

**Build — computation physics (how complexity becomes computation):**
3. **[[IronLawOfMLSystems|Iron Law of ML Systems]]** — $T = D_{vol}/\text{BW} + O/(R_{peak}\eta_{hw}) + L_{lat}$; every optimization pulls one of three levers, and reducing one may inflate another.
4. **Silicon Contract** — $\eta_{hw}\to 1 \iff I_{model}\approx I_{machine}$; matched hardware achieves peak throughput, mismatched wastes money.

**Optimize — efficiency physics (how constraints shape trade-offs):**
5. **[[ParetoFrontier|Pareto Frontier]]** — no universal optimum; every gain trades against another metric.
6. **[[ArithmeticIntensity|Arithmetic Intensity Law]]** — $R_{attainable}=\min(R_{peak}, I\times\text{BW})$; adding compute to a memory-bound model yields zero gain.
7. **Energy-Movement Invariant** — $E_{move}\gg E_{compute}$ (a DRAM access ≈ 100–1,000× an FP32/FP16 FLOP); data locality, not raw FLOP/s, drives efficiency.
8. **[[AmdahlsLaw|Amdahl's Law]]** — the serial fraction caps all parallelism gains.

**Deploy — reliability physics (how reality defeats assumptions):**
9. **Verification Invariant** — ML testing is statistical; it bounds error, never proves correctness.
10. **Statistical Drift Invariant** — Accuracy(t) ≈ Accuracy₀ − λ·D(P_t‖P₀); models decay without code changes as the world drifts from the training distribution.
11. **[[TrainingServingSkew|Training-Serving Skew Law]]** — subtle preprocessing differences between train and serve paths silently degrade accuracy.
12. **[[LatencyBudget|Latency Budget Invariant]]** — P99 is the hard constraint; throughput is optimized within the latency envelope, never at its expense.
13. **Bias Feedback Invariant** — $\Delta_{err,g}(n)\approx\Delta_{err,g}(0)\cdot\alpha_{fb}^n$ with $\alpha_{fb}>1$; errors against subgroups compound across cycles when outputs reshape inputs.

## Properties

- **An integrated web, not a checklist.** A single decision (e.g., FP16→INT8 quantization) ripples through several invariants at once — Pareto frontier, silicon contract, arithmetic intensity, energy-movement, and latency budget simultaneously.
- **The cycle has a feedback arrow.** Invariants 9–13 (verification failures, drift, skew, tail-latency violations, bias amplification) force the system back to its Foundations: new data, retraining, fresh optimization passes.
- **A diagnostic instrument, not a taxonomy.** The conclusion applies them to a worked roofline (70B [[Llama|Llama 2]] decode on an NVIDIA H100 is ≈ 295× memory-bound) and an Amdahl pitfall (10× speedup of a 10% stage → ~1.1× system).
- **Aspires to the Hennessy–Patterson role.** Just as the 1990 quantitative framework turned computer architecture from rhetoric into arithmetic, these invariants aim to give ML systems engineering a shared analytical language ([[JohnHennessy]], [[DavidPatterson]]).

## Connections

- [[ConservationOfComplexity]] — the meta-principle unifying all thirteen; complexity moves between data, algorithm, machine.
- [[DAMTaxonomy]] — the three destinations across which complexity is conserved.
- [[IronLawOfMLSystems]] / [[ParetoFrontier]] / [[ArithmeticIntensity]] / [[AmdahlsLaw]] / [[DataGravity]] / [[TrainingServingSkew]] / [[LatencyBudget]] — named invariants with their own pages.
- [[LighthouseModel]] — the five workloads against which the invariants are tested across the [[DeploymentSpectrum]].
- [[RooflineModel]] — the diagnostic the arithmetic-intensity and energy-movement invariants formalize.
- [[MLSystemLifecycle]] — the Foundations→Build→Optimize→Deploy arc the invariants are organized along.
- [[mlsysbook-ch16-conclusion]] — source; the synthesis chapter that names and consolidates the framework.
