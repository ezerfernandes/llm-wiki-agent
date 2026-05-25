---
title: "Regeneration Signal"
type: concept
tags: [user-feedback, implicit-feedback, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Regeneration Signal

**When a user requests a fresh generation of the same prompt, that action is a feedback signal — but a noisy one whose strength depends on the billing model.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"If a user chooses regeneration, it might be because they're not satisfied with the first response. However, it might also be that the first response is adequate, but the user wants options to compare. This is especially common with creative requests like image or story generation."* — Ch 10

## Signal strength varies with billing

> *"Regeneration signals might also be stronger for applications with usage-based billing than those with subscriptions. With usage-based billing, users are less likely to regenerate and spend extra money out of idle curiosity."* — Ch 10

Under a flat subscription, regeneration is cheap for the user — many regenerations are exploratory rather than corrective. Under usage-based billing, each regeneration costs the user, so the bar for clicking is higher and the negative signal is cleaner.

## Regeneration as comparative feedback

After a regeneration, some products ask the user to compare the new response with the old one (Figure 10-13 in Ch 10 shows ChatGPT doing this). Converting regeneration into an explicit better/worse vote turns a noisy implicit signal into [[PreferenceData|preference data]] suitable for [[PreferenceFinetuning|preference finetuning]].

## Use cases

- **Creative generation** — image, story, music: regeneration is *expected* exploration, not negative feedback. Don't weight as negative.
- **Information retrieval / Q&A** — regeneration here is more strongly negative.
- **Code generation** — middle ground; regeneration may indicate the first attempt didn't compile or didn't fit context.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ImplicitConversationalSignal]] — parent category.
- [[ConversationalFeedback]] — grandparent category.
- [[PreferenceData]] / [[PreferenceFinetuning]] — what comparative regeneration can train.
- [[Midjourney]] — Ch 10's design exemplar uses regeneration alongside upscale + vary.
