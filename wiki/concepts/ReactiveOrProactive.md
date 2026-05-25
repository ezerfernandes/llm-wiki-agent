---
title: "Reactive or Proactive"
type: concept
tags: [planning, ux, apple, ai-engineering]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
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

## Connections

- [[Apple]] — framework source.
- [[CriticalOrComplementary]] / [[DynamicOrStatic]] — companion axes.
- [[UseCaseEvaluation]] — parent planning framework.
- [[UsefulnessThreshold]] — downstream quality-bar setting.
- [[ai-engineering-ch01-intro]] — primary source.
