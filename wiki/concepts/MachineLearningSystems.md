---
title: "Machine Learning Systems"
type: concept
tags: [ml-systems, foundations, mlsysbook, definition]
sources: [mlsysbook-ch01-introduction, mlsysbook-ch02-ml-systems, mlsysbook-ch16-conclusion]
last_updated: 2026-06-05
---

# Machine Learning Systems

**Software systems whose core behavior is determined by parameters learned from data rather than explicitly programmed rules, making performance a simultaneous function of data quality, algorithm choice, and hardware capacity.** This is the central definition of Reddi's *Machine Learning Systems* ([[mlsysbook-ch01-introduction|mlsysbook Vol 1, Ch 1]]).

Three interconnected concerns appear in *every* ML system and in *no* traditional software system simultaneously: (1) obtaining and managing training **data** at scale, (2) implementing **algorithms** that learn and generalize, and (3) building **infrastructure** that supports both training and real-time prediction. The canonical illustrative example is email spam filtering against hundreds of billions of daily messages with sub-100 ms latency.

## Defining properties (per [[mlsysbook-ch01-introduction|Ch 1]])

- **Behavior is defined by data, not code** — the [[Software2|"data as code" invariant]].
- **Failure is silent** — [[SilentDegradation|accuracy decays]] under [[DistributionShift|distribution shift]] with no crash or exception; the world changes while frozen weights do not.
- **The model is ~5% of the system** — data pipelines, serving, and monitoring dominate the engineering surface (Sculley et al. 2015 technical-debt schematic).
- **Performance traces to the [[IronLawOfMLSystems|iron law]]** — $T = D_{vol}/\text{BW} + O/(R_{peak}\cdot\eta_{hw}) + L_{lat}$.

## Connections

- [[DAMTaxonomy]] — the Data·Algorithm·Machine diagnostic for any ML-system bottleneck.
- [[AITriad]] — Data (fuel) + Algorithm (blueprint) + Machine (engine).
- [[MLSystemsEngineering]] / [[AIEngineering]] — the discipline of building these systems.
- [[Software2]] — the paradigm reframing.
- [[SilentDegradation]] / [[DistributionShift]] — the distinctive failure mode.
- [[IronLawOfMLSystems]] — the performance decomposition.
- [[DeploymentSpectrum]] / [[SystemArchetype]] — cloud→TinyML span; [[mlsysbook-ch02-ml-systems|Ch 2]] argues *where* a system runs ([[CloudML]] / [[EdgeML]] / [[MobileML]] / [[TinyML]]) is a first-order engineering decision dictated by physics.
- [[SystemEntropy]] — the post-deployment decay that makes ML systems differ from "deploy-once-run-forever" software.
- [[mlsysbook-ch16-conclusion]] — the conclusion sharpens the definition into a thesis — ***the system is the model***: the "true model" is data pipeline + training infrastructure + serving system + monitoring loop, so "systems engineering is not a wrapper around ML; it is the implementation of ML." It names the defining skill of the discipline as *reasoning across boundaries* (the spaces between layers where one team's optimization becomes another's constraint) and consolidates the field's quantitative spine into the [[ThirteenQuantitativeInvariants|thirteen invariants]].
- [[mlsysbook-ch01-introduction]] / [[mlsysbook-ch02-ml-systems]] — sources.
