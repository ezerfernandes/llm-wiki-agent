---
title: "User Edit Feedback"
type: concept
tags: [user-feedback, preference-data, llm-app, alignment]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# User Edit Feedback

**When a user directly edits the model's output, the original-vs-edited pair is one of the strongest [[ConversationalFeedback|conversational feedback]] signals and a ready-made [[PreferenceData|preference data]] point.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"Some applications let users edit the model's responses directly. For example, if a user asks the model to generate code, and the user corrects the generated code, it's a very strong signal that the code that got edited isn't quite right."* — Ch 10

## The preference-data property

> *"User edits also serve as a valuable source of preference data. Recall that preference data, typically in the format of (query, winning response, losing response), can be used to align a model to human preference. Each user edit makes up a preference example, with the original generated response being the losing response and the edited response being the winning response."* — Ch 10

This is **automatic preference-pair generation by the user's normal workflow** — no separate explicit rating step needed. Feeds [[PreferenceFinetuning|preference finetuning]] (RLHF, DPO, RLAIF) directly.

## Where it's strongest

Applications where editing the output is natural to the workflow:

- **Code assistants** ([[GitHubCopilot|GitHub Copilot]], Cursor) — the user keeps typing; the diff between accepted suggestion and final code is the edit.
- **Email drafting** (Gmail with Smart Compose) — if Gmail suggests a draft, *"Gmail can track how this draft is used or edited."*
- **Image editing** — [[InpaintingFeedback|inpainting]] is the visual analog: a user-edited region is an edit-pair.

## Why standalone chat assistants miss out

Ch 10's structural observation:

> *"One of the biggest challenges of standalone AI applications like ChatGPT and Claude is that they aren't integrated into the user's daily workflow, making it hard to collect high-quality feedback the way integrated products like GitHub Copilot can. For example, if Gmail suggests an email draft, Gmail can track how this draft is used or edited. However, if you use ChatGPT to write an email, ChatGPT doesn't know whether the generated email is actually sent."* — Ch 10

**Integration into the user's primary workflow is the precondition for collecting edit-pair feedback.** This is one of the structural reasons co-pilot products dominate flywheel-quality feedback over chat products.

## Quality considerations

- **Edit granularity** — a one-character typo fix is a much weaker signal than a paragraph rewrite. Weight or filter pairs by edit-distance / diff size.
- **Edit type** — formatting changes, style changes, and factual corrections all reveal different model deficiencies. Classify edits to feed back to targeted improvements.
- **Sample bias** — users who edit aggressively are systematically different from users who accept-as-is. The flywheel risks over-fitting to the editing minority.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ConversationalFeedback]] / [[NaturalLanguageFeedback]] — parent categories.
- [[PreferenceData]] / [[PreferenceFinetuning]] / [[DPO]] / [[rlhf|RLHF]] — what edit-pairs train.
- [[InpaintingFeedback]] — the image/region-level sibling.
- [[GitHubCopilot]] — Ch 10's named exemplar of edit-feedback-friendly product design.
- [[DataFlywheel]] — edit-feedback is one of the highest-quality flywheel inputs.
