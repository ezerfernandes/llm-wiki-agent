---
title: "System 1 vs System 2"
type: concept
tags: [cognitive-science, reasoning, framing]
sources: [2402.01817-llm-modulo]
last_updated: 2026-05-10
---

# System 1 vs System 2

Kahneman's dual-process taxonomy (*Thinking, Fast and Slow*, 2011):
- **System 1** — fast, intuitive, associative, parallel, automatic, constant-time response.
- **System 2** — slow, deliberate, sequential, search-based, principled, effortful.

## Use in this wiki
[[2402.01817-llm-modulo]] hangs its central argument on this taxonomy:

> *Even from a pure engineering perspective, a system that takes constant time to produce the next token cannot possibly be doing principled reasoning on its own.*

LLMs are framed as a **giant pseudo-System 1** — an "approximate knowledge source gleaned either from the environment or compiled from System 2" — whose strength is making/finding analogies across vast prior text, not deliberation. Multi-modality (GPT-4V) **extends System 1 imagination** but does not bestow System 2 competence.

The [[LLMModuloFramework]] is, in this framing, an explicit **System 1 (LLM) + System 2 (sound external critic loop)** composition, with soundness inherited from the System 2 side.

## Connections
- [[Planning]], [[SelfVerification]] — examples of System-2 tasks LLMs alone cannot perform
- [[LLMModuloFramework]] — proposed System-1/System-2 composition
- [[ChainOfThought]], [[TreeOfThoughts]], [[Reflexion]] — critiqued as System-1 priming variations, not true System 2
- [[2402.01817-llm-modulo]] — source
