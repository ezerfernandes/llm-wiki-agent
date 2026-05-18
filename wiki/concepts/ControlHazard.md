---
title: "Control Hazard"
type: concept
tags: [computer-architecture, cpu, pipelining, hazards, branching]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Control Hazard

A **control hazard** is a [[PipelineHazard|pipeline hazard]] that arises when *"the pipeline encounters a branch (conditional) instruction"* ([[dis-5-8-pipelining-advanced|Ch 5.8]]) — the processor cannot determine which instruction executes next until the branch resolves, yet [[InstructionPipelining|pipelining]] has already begun fetching speculative successors that may be wrong.

## The problem

Under [[dis-5-7-pipelining|Ch 5.7]]'s pipelining model, every cycle the Fetch stage pulls the *next* instruction from memory. A [[BranchInstruction|branch (conditional) instruction]] makes "next" undefined until the condition is evaluated — typically in the Execute stage, several cycles after Fetch. Instructions speculatively fetched in those intervening cycles may turn out to be from the wrong path and must be **flushed** from the pipeline.

## Mitigations Ch 5.8 covers

- **Pipeline stalling** — inject [[NoOperation|NOP]] bubbles until the branch resolves. Simple but pays a per-branch penalty proportional to the resolution distance.
- **[[BranchPrediction|Branch prediction]]** — guess which way the branch will go and fetch speculatively from the predicted target; on misprediction, flush. *"The most common solution is to use a [[BranchPredictor|branch predictor]], which will predict which way a branch will go, based on previous executions."* Modern predictors achieve high accuracy but have created security vulnerabilities like **[[Spectre]]**.
- **Eager execution** — execute *both* branch paths and conditionally transfer **results** at the join rather than transferring **control** at the branch — avoids the pipeline disruption entirely for compatible code.

## Connections

- [[PipelineHazard]] — parent category.
- [[DataHazard]] — sibling hazard category (register-related).
- [[BranchInstruction]] — the instruction class that triggers control hazards.
- [[BranchPrediction]] — primary mitigation.
- [[BranchPredictor]] — the hardware structure that implements prediction.
- [[PipelineStall]] — fallback mitigation.
- [[InstructionPipelining]] — the optimization control hazards threaten.
- [[Spectre]] — security side effect of speculative branch prediction (named-reference only — no dedicated page yet).
- [[dis-5-8-pipelining-advanced]] — primary source.
