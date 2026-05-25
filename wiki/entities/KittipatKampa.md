---
title: "Kittipat Kampa"
type: entity
tags: [person, tifin, ai-engineer]
sources: [ai-engineering-ch02-foundation-models]
last_updated: 2024-12-04
---

# Kittipat Kampa

Head of AI at [[TIFIN|TIFIN]] (US-based AI-in-finance company). Cited in [[ai-engineering-ch02-foundation-models|*AI Engineering* Ch 2]] for a clever **latency-hedging pattern** in [[TestTimeCompute|test-time compute]]:

## The pattern (Ch 2)

> "Kittipat Kampa, head of AI at TIFIN, told me that his team asks their model to generate multiple responses in parallel and show the user the first response that is completed and valid."

## Why this matters

The pattern is **test-time compute as a latency hedge**, not as a quality lever. For slow chain-of-thought queries where a single chain can take a long time:

- Generate N candidates in parallel (not sequentially).
- Don't wait for all to finish — return the first one that completes and validates.
- The user sees the fastest valid response; slow candidates are abandoned.

Latency floor becomes the *minimum* over N parallel chains rather than the *mean* of a single chain. Cost goes up proportionally; latency comes down asymmetrically.

## Position in the wiki

A small but pointed Ch 2 anecdote that crystallizes the *latency angle* of [[TestTimeCompute|test-time compute]] — distinct from the more-common *quality angle* embodied by [[bestofn|best-of-N]] and [[selfconsistency|self-consistency]].

## Connections
- [[TIFIN]] — employer.
- [[TestTimeCompute]] — the broader pattern this is an instance of.
- [[bestofn]] — closest cousin (best-by-score instead of first-valid).
- [[ai-engineering-ch02-foundation-models]] — primary source.
