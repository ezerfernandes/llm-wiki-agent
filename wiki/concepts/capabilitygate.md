---
title: "Capability Gate"
type: concept
tags: [concept]
sources: [2605.00424-skills-as-verifiable-artifacts]
last_updated: 2026-05-10
---

# Capability Gate

Runtime layer between the LLM-driven agent and the external world. Receives tool-call envelopes, looks up the corresponding capability, applies a verification-level-dependent policy. HITL fires for unverified skills on every irreversible call; for verified skills, only outside the declared capability set.
