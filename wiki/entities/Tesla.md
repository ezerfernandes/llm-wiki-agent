---
title: "Tesla"
type: entity
tags: [company, autonomous-vehicles]
sources: [d2l-introduction, mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch11-hardware-acceleration, mlsysbook-ch14-ml-operations]
last_updated: 2026-06-05
---

# Tesla

US electric-vehicle and partial-autonomy company. [[d2l-introduction]] cites Tesla — alongside NVIDIA and Waymo — as a shipping example of how [[DeepLearning|deep learning]] has reached **partial autonomy** in self-driving despite full autonomy still being out of reach.

The chapter's framing: "What makes full autonomy so challenging is that proper driving requires the ability to perceive, to reason and to incorporate rules into a system. **At present, deep learning is used primarily in the visual aspect of these problems. The rest is heavily tuned by engineers.**"

In other words, Tesla's autopilot is a useful boundary case for the corpus: it demonstrates real-world DL deployment in computer vision (lane detection, obstacle recognition) but exposes the limits of pure end-to-end learning when the downstream task requires planning, rule-following, and high-stakes reasoning under partial observability.

Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|Vol 1, Ch 1]]) notes Tesla as where [[AndrejKarpathy|Andrej Karpathy]] (Director of AI) applied deep learning to autonomous-vehicle fleets — the experience behind his [[Software2|Software 2.0]] thesis. [[mlsysbook-ch02-ml-systems|Ch 2]] cites Tesla Full Self-Driving as the canonical [[EdgeML|Edge ML]] case: multi-camera perception through custom edge hardware with millisecond end-to-end latency, "infeasible with cloud processing due to network delays."

## Connections

- [[AndrejKarpathy]] / [[Software2]] / [[mlsysbook-ch01-introduction]] — Karpathy's AI directorship and the data-as-code reframing.
- [[EdgeML]] / [[mlsysbook-ch02-ml-systems]] — Tesla FSD as the latency-critical edge-inference exemplar.
- [[ComputerVision]] — the deep-learning component of Tesla's autopilot.
- [[reinforcementlearning]] — the framework that would unify perception + planning (still aspirational here).
- [[d2l-introduction]] — corpus anchor.
- [[mlsysbook-ch14-ml-operations]] — Ch 14 cites Autopilot as an undeclared-consumer-debt example: OTA updates silently changed multiple subsystems lacking interface governance.

