---
title: "Branch Predictor"
type: concept
tags: [computer-architecture, cpu, pipelining, branching, hardware-structure]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Branch Predictor

The **branch predictor** is the dedicated hardware structure inside a pipelined [[CPU]] that implements [[BranchPrediction|branch prediction]]. [[dis-5-8-pipelining-advanced|Ch 5.8]] names it as the mechanism behind *"the most common solution"* to [[ControlHazard|control hazards]]:

> *"The most common solution is to use a branch predictor, which will predict which way a branch will go, based on previous executions."*

## What Ch 5.8 specifies

- **Inputs**: history of previous executions of branches.
- **Output**: a directional prediction (taken / not-taken) used to drive speculative [[PipelineStages|Fetch]] of the next instructions.
- **Side-effect**: speculative execution of the predicted path; on misprediction those instructions are flushed.

Ch 5.8 does **not** prescribe a specific predictor design (bimodal, two-bit saturating counter, gshare, TAGE, perceptron, neural). The chapter introduces the *role* of the predictor, not its internal microarchitecture.

## Security exposure

Ch 5.8 notes that modern branch predictors — and the speculative execution they enable — created the side-channel attack class exemplified by **[[Spectre]]**. The speculative-execution-without-architectural-commit footprint leaks through cache timing and other micro-architectural state.

## Connections

- [[BranchPrediction]] — the mechanism the predictor implements.
- [[ControlHazard]] — the hazard category the predictor mitigates.
- [[BranchInstruction]] — the instruction class the predictor is consulted for.
- [[CPU]] / [[InstructionPipelining]] — the host machine and optimization context.
- [[Spectre]] — security side effect (named-reference only).
- [[dis-5-8-pipelining-advanced]] — primary source.
