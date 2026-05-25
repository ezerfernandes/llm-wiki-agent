---
title: "MTTR (Mean Time To Response)"
type: concept
tags: [observability, monitoring, devops, metric]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# MTTR

**Mean Time To Response.** The average elapsed time between *detection* of a problem and its *resolution*. One of three DevOps observability metrics [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] adopts for AI-application observability, alongside [[MTTD|MTTD]] and [[ChangeFailureRate|CFR]].

> *"MTTR (mean time to response): After detection, how long does it take to be resolved?"* — Ch 10

In broader DevOps literature "MTTR" sometimes expands to *Mean Time To Recovery* or *Mean Time To Repair*; Ch 10 uses the *response* expansion to emphasize that the clock starts at detection, not at the original failure.

## Why it matters for AI applications

AI-app fixes often require **diagnostic depth that simple logs can't provide**: was the failure in retrieval, in prompt assembly, in the model, or in post-processing? Ch 10's *log everything* rule and its emphasis on [[RequestTrace|request traces]] are MTTR-lowering tools: they shorten the gap between "metric fires" and "engineer knows what to change."

## The fast-logs requirement

> *"For fast detection, metrics need to be computed quickly. For fast response, logs need to be readily available and accessible. If your logs are 15 minutes delayed, you will have to wait for the logs to arrive to track down an issue that happened 5 minutes ago."* — Ch 10

A 15-minute log lag puts a 15-minute floor on MTTR for any issue diagnosis requires logs to identify — independent of how fast the engineers can think.

## Pairing with MTTD

See [[MTTD]] — MTTD + MTTR together measure the total time a user-facing problem is in the wild. Either one alone is insufficient.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[MTTD]] — paired metric.
- [[ChangeFailureRate]] — third DevOps observability metric.
- [[observability]] / [[Monitoring]] — parent disciplines.
- [[RequestTrace]] / [[Logging]] — the diagnostic tooling that lowers MTTR.
