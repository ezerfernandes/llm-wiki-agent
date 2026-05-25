---
title: "Error Correction (Natural-Language Feedback)"
type: concept
tags: [user-feedback, natural-language-feedback, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Error Correction (Natural-Language Feedback)

**The strongest, simplest [[NaturalLanguageFeedback|natural-language feedback]] signal: a user follow-up message that starts with an explicit contradiction.** Named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"If a user starts their follow-up with 'No, …' or 'I meant, …', the model's response is likely off the mark."* — Ch 10

## Why it's a clean signal

Unlike [[RephraseAttempt|rephrases]] (which could be ambiguity) or sentiment outbursts (which require classifiers), the *"No, …"* / *"I meant, …"* opener is **surface-detectable** and almost always indicates the prior response failed. Implementation is a regex on the first few tokens of a turn.

## Two flavors of correction content

Ch 10 distinguishes:

- **Generic correction** — just signals failure; no information about *how* to fix.
- **Specific correction** — names the failure. *"Bill is the suspect, not the victim."* — directly editable into the prior model output. The model should be able to take the correction and revise its summary.

Specific corrections can be folded back into the model's context to fix the immediate response and, in aggregate, become training data for error patterns.

## Boundary with [[ActionCorrectingFeedback|action-correcting feedback]]

Error correction targets the **content of the last response**. Action-correcting feedback targets the **agent's plan** ("you should also check XYZ's GitHub"). They overlap when an agent's "response" *is* a plan.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[NaturalLanguageFeedback]] — parent category.
- [[RephraseAttempt]] / [[ActionCorrectingFeedback]] — sibling natural-language signals.
- [[ConversationalFeedback]] — grandparent category.
