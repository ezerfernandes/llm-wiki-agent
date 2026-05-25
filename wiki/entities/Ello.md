---
title: "Ello"
type: entity
tags: [startup, education, reading, instruction-following, case-study]
sources: [ai-engineering-ch04-evaluate-ai-systems]
last_updated: 2024-12-04
---

# Ello

Startup that helps kids read better through AI-generated personalized stories. Per [[ai-engineering-ch04-evaluate-ai-systems|*AI Engineering* Ch 4]]:

> "Ello, a startup that helps kids read better, wants to build a system that automatically generates stories for a kid using only the words that they can understand. The model they use needs the ability to follow the instruction to work with a limited pool of words."

## Significance

Ello is Ch 4's canonical example of a **non-format [[InstructionFollowingCapability|instruction-following]] requirement** — the constraint is *vocabulary*, not *output structure*. The model's outputs don't have to be in JSON or follow a regex; they just have to use only words from a specific allowed list.

This case shows why instruction-following capability is bigger than "JSON mode":

> "Instruction-following capability goes beyond generating structured outputs."

## Connections

- [[ai-engineering-ch04-evaluate-ai-systems]] — primary source.
- [[InstructionFollowingCapability]] — what their use case exercises.
- [[StructuredOutputs]] — the more common (but narrower) case Ello is a counterpoint to.
