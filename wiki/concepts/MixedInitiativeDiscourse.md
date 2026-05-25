---
title: "Mixed-Initiative Discourse"
type: concept
tags: [dialogue, multi-agent, framing]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Mixed-Initiative Discourse

**Mixed-initiative dialogue** — a multi-party conversation framing where **either side can take initiative** (ask a question, change topic, take the floor) at any time. Formalized by [[Traum2003|Traum 2003]] *Issues in Multiparty Dialogues* (Workshop on Agent Communication Languages).

## The three modes

| Mode | Initiative | Examples in this wiki |
|---|---|---|
| **User-initiative only** | User asks, system answers | [[QASystem]] · [[rag\|RAG]] chatbot · [[GoogleSearch]] |
| **System-initiative only** | System decides everything | [[STORM]] (one-shot report from a topic) |
| **Mixed-initiative** | Either side, anytime | [[CoSTORM]] · most human-human dialogue |

## Why Co-STORM picks mixed-initiative

Per [[2408.15232-co-storm|Co-STORM §3.1]]:

> *"Co-STORM adopts a mixed-initiative approach. When the user actively engages, the system continues the discourse based on the user's question or argument, allowing for a more targeted discussion. Otherwise, the system automatically generates the next turn. The user controls who takes the initiative."*

This solves a tension that single-initiative systems run into:

- **User-initiative-only** systems require the user to know what to ask — which fails for [[UnknownUnknowns|unknown unknowns]].
- **System-initiative-only** systems (like [[STORM]]) cannot adapt to user-specific goals once the report is generated.

Mixed-initiative lets the user observe and engage *when they have something to ask*, and lets the system progress otherwise.

## Implementation

In Co-STORM, mixed-initiative is implemented by the [[TurnManagement|turn-management protocol]]: a round-robin schedule among experts + moderator override, all preempted by user injection.

## See also
- [[CoSTORM]] · [[TurnManagement]] · [[CollaborativeDiscourse]]
