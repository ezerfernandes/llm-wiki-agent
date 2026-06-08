---
title: "Reactive or Proactive"
type: concept
tags: [planning, ux, apple, ai-engineering]
sources: [ai-engineering-ch01-intro, agentic-design-patterns-00-frontmatter]
last_updated: 2026-06-07
---

# Reactive or Proactive

**One of [[Apple|Apple's]] three axes for classifying the role of AI in a product**, surfaced in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]. Asks: *does AI respond to user requests, or surface insights on its own?*

## The axis

- **Reactive**: AI responds in reaction to a user request or action. **Example**: a chatbot — the user types, the bot responds.
- **Proactive**: AI surfaces a response when *it* detects an opportunity. **Example**: Google Maps traffic alerts — Maps notices the user is about to drive into traffic and warns them.

## Engineering implications

Two opposite pressures:

| Dimension | Reactive | Proactive |
|---|---|---|
| **Latency** | High pressure — user is waiting | Lower pressure — can be pre-computed |
| **Quality bar** | Lower — user opted in | **Higher** — intrusive if low-quality |
| **Failure cost** | Frustration | Annoyance, distrust, app uninstall |

> *"Because users don't ask for proactive features, they can view them as intrusive or annoying if the quality is low. Therefore, proactive predictions and generations typically have a higher quality bar."*

## Where this sits

One of three role axes; the others are:
- **[[CriticalOrComplementary]]** — does the app work without the AI?
- **[[DynamicOrStatic]]** — does the AI update continually or periodically?

## Parallel framing: Gulli's agent characteristics

[[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[AntonioGulli|Gulli]]) treats **[[Proactiveness|proactiveness]]** and **[[Reactiveness|reactiveness]]** not as a product-design axis but as two of the defining *characteristics* of an [[AgenticAI|agentic system]] — proactiveness = initiating actions toward goals, reactiveness = responding to environmental change. Apple's product axis here (reactive vs. proactive role of AI in a feature) is the UX-level reflection of those two agent capabilities, and shares the same quality-bar tension: unprompted proactive behavior carries a higher bar because users did not ask for it.

## Connections

- [[Proactiveness]] / [[Reactiveness]] — Gulli's agent-characteristic framing.
- [[Apple]] — framework source.
- [[CriticalOrComplementary]] / [[DynamicOrStatic]] — companion axes.
- [[UseCaseEvaluation]] — parent planning framework.
- [[UsefulnessThreshold]] — downstream quality-bar setting.
- [[ai-engineering-ch01-intro]] — primary source.
