---
title: "Critical or Complementary"
type: concept
tags: [planning, ux, apple, ai-engineering]
sources: [ai-engineering-ch01-intro]
last_updated: 2024-12-04
---

# Critical or Complementary

**One of [[Apple|Apple's]] three axes for classifying the role of AI in a product**, surfaced in [[ai-engineering-ch01-intro|*AI Engineering* Ch 1]]. Asks: *if AI fails, does the app still work?*

## The axis

- **Critical**: the application cannot function without AI. **Example**: Face ID — facial recognition is the whole point.
- **Complementary**: the application works without AI; AI just makes it better. **Example**: Gmail Smart Compose — Gmail still sends mail without it.

## Engineering implication

> *"The more critical AI is to the application, the more accurate and reliable the AI part has to be. People are more accepting of mistakes when AI isn't core to the application."*

Critical AI features need:
- Higher quality bars in the [[UsefulnessThreshold|usefulness threshold]].
- Stronger graceful-degradation paths.
- Tighter monitoring + faster regression-response.

Complementary AI features can tolerate more variance — users will just ignore bad suggestions.

## Where this sits

One of three role axes; the others are:
- **[[ReactiveOrProactive]]** — does AI respond to requests or surface insights opportunistically?
- **[[DynamicOrStatic]]** — does the AI update continually with user feedback or periodically?

Together, the three axes give a planning team a quick triage of the engineering bar required for a proposed AI feature.

## Connections

- [[Apple]] — framework source.
- [[ReactiveOrProactive]] / [[DynamicOrStatic]] — companion axes.
- [[UseCaseEvaluation]] — parent planning framework.
- [[UsefulnessThreshold]] — downstream quality-bar setting.
- [[ai-engineering-ch01-intro]] — primary source.
