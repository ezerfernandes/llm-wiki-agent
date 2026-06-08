---
title: "Domain Randomization"
type: concept
tags: [ml-systems, synthetic-data, data-selection, mlsysbook]
sources: [mlsysbook-ch09-data-selection]
last_updated: 2026-06-05
---

# Domain Randomization

A strategy for bridging the [[DomainGap|domain gap]] between synthetic and real data ([[mlsysbook-ch09-data-selection|Reddi Ch 9]]). The counterintuitive insight: rather than making synthetic data *more* realistic, **randomize lighting, textures, backgrounds, and camera/physics parameters** so wildly that the real world becomes "just another variation" within the model's learned distribution. This eliminates the need for expensive photorealistic rendering, shifting the cost bottleneck from rendering fidelity to variation coverage. Produces strong results in robotics and autonomous driving where simulators are mature. Contrasted with [[DomainAdaptation|domain adaptation]], which instead explicitly aligns the two distributions.

## Connections

- [[DomainGap]] — the problem it addresses; [[DomainAdaptation]] — the alternative strategy.
- [[SyntheticDataGeneration]] — the generation context.
- [[mlsysbook-ch09-data-selection]] — source.
