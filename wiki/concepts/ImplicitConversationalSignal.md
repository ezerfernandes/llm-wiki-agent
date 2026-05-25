---
title: "Implicit Conversational Signal"
type: concept
tags: [user-feedback, conversational-ai, implicit-feedback, evaluation]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Implicit Conversational Signal

**Feedback inferred from user *actions* (rather than message content) within a conversational interface.** Sibling category to [[NaturalLanguageFeedback]] under [[ConversationalFeedback]]; named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]].

> *"Other types of conversational feedback can be derived from user actions instead of messages."* — Ch 10

## The signals

### [[RegenerationSignal|Regeneration]]

*"Many applications let users generate another response, sometimes with a different model. If a user chooses regeneration, it might be because they're not satisfied with the first response. However, it might also be that the first response is adequate, but the user wants options to compare."*

**Billing model affects signal strength**: *"regeneration signals might also be stronger for applications with usage-based billing than those with subscriptions. With usage-based billing, users are less likely to regenerate and spend extra money out of idle curiosity."*

Some products (e.g., ChatGPT — Figure 10-13) explicitly ask the user to compare the new response with the previous one — turning regeneration into [[PreferenceData|preference data]].

### Conversation organization

User actions that organize the conversation history:

- **Delete** — strong negative signal (unless the conversation is embarrassing, in which case ambiguous).
- **Rename** — good content, bad auto-title.
- **Share** — *ambiguous*: some users share when the model errs glaringly, others when it helps. *"It's important to study your users to understand why they do each action."*
- **Bookmark / favorite** — positive.

### Conversation length

*"Whether this is a positive or negative signal depends on the application. For AI companions, a long conversation might indicate that the user enjoys the conversation. However, for chatbots geared toward productivity like customer support, a long conversation might indicate that the bot is inefficient in helping users resolve their issues."*

### Dialogue diversity

Combine length with diversity (distinct token / topic count) for interpretation: *"if the conversation is long but the bot keeps repeating a few lines, the user might be stuck in a loop."*

## Explicit vs implicit conversational signals

> *"Explicit feedback is easier to interpret, but it demands extra effort from users. … Explicit feedback also suffers from response biases. For example, unhappy users might be more likely to complain, causing the feedback to appear more negative than it is."*
>
> *"Implicit feedback is more abundant — what can be considered implicit feedback is limited only by your imagination — but it's noisier."* — Ch 10

## Signal stacking for disambiguation

> *"Adding more signals can help clarify the intent. For example, if the user rephrases their question after sharing a link, it might indicate that the conversation didn't meet their expectations."* — Ch 10

A single signal is often ambiguous; combinations are diagnostic.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ConversationalFeedback]] — parent category.
- [[NaturalLanguageFeedback]] — sibling category (content-based).
- [[ImplicitFeedback]] — broader sibling from the recommender-systems literature.
- [[RegenerationSignal]] / [[UserEditFeedback]] / [[InpaintingFeedback]] — specific signal pages.
- [[PreferenceData]] / [[PreferenceFinetuning]] — what comparative-regeneration signals can train.
