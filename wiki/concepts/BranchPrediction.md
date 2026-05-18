---
title: "Branch Prediction"
type: concept
tags: [computer-architecture, cpu, pipelining, branching, speculation, security]
sources: [dis-5-8-pipelining-advanced]
last_updated: 2026-05-17
---

# Branch Prediction

**Branch prediction** is [[dis-5-8-pipelining-advanced|Ch 5.8]]'s headline mitigation for [[ControlHazard|control hazards]]: rather than [[PipelineStall|stalling]] the pipeline until a [[BranchInstruction|branch instruction]] resolves, the CPU **guesses** which direction the branch will take and **speculatively fetches** from the predicted path. If the guess turns out correct, the pipeline ran at full throughput; if wrong, the speculative instructions are flushed and execution resumes from the actual target.

## What Ch 5.8 says

> *"The most common solution is to use a [[BranchPredictor|branch predictor]], which will predict which way a branch will go, based on previous executions."*

The prediction is **history-driven** — based on the branch's prior behavior. Modern predictors achieve high accuracy. Ch 5.8 does *not* detail specific predictor algorithms (static vs dynamic, two-bit saturating counters, two-level adaptive, perceptron, TAGE) — those are beyond its scope. The page records the mechanism as Ch 5.8 introduces it.

## The security cost

Ch 5.8 flags that branch prediction has *also* created security vulnerabilities — the speculative execution following a predicted-but-wrong branch leaves measurable micro-architectural side effects (cache state, predictor state) that adversaries can probe. The named example is **[[Spectre]]** (no dedicated wiki page yet).

## Connections

- [[ControlHazard]] — the hazard category branch prediction mitigates.
- [[BranchPredictor]] — the named hardware structure implementing prediction.
- [[BranchInstruction]] — the instruction class predicted.
- [[PipelineStall]] — the alternative (worse-performance) mitigation.
- [[InstructionPipelining]] — the optimization branch prediction protects.
- [[Spectre]] — security side effect (named-reference only).
- [[dis-5-8-pipelining-advanced]] — primary source.
