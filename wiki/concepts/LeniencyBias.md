---
title: "Leniency Bias"
type: concept
tags: [user-feedback, bias, evaluation, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Leniency Bias

**The tendency for users to rate items more positively than warranted — to avoid conflict, feel polite, or simply minimize friction.** Named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as one of four feedback biases to design around.

> *"Leniency bias is the tendency for people to rate items more positively than warranted, often to avoid conflict because they feel compelled to be nice or because it's the easiest option. Imagine you're in a hurry, and an app asks you to rate a transaction. You aren't happy with the transaction, but you know that if you rate it negatively, you'll be asked to provide reasons, so you just choose positive to be done with it."* — Ch 10

## The Uber illustration

> *"On a five-star rating scale, four and five stars are typically meant to indicate a good experience. However, in many cases, users may feel pressured to give five-star ratings, reserving four stars for when something goes wrong. According to Uber, in 2015, the average driver's rating was 4.8, with scores below 4.6 putting drivers at risk of being deactivated."* — Ch 10

The Uber rating scale operates effectively in the **4.6–5.0 band** — the bottom 92% of the nominal scale is dead.

## When the bias is fine

> *"This bias isn't necessarily a dealbreaker. Uber's goal is to differentiate good drivers from bad drivers. Even with this bias, their rating system seems to help them achieve this goal."* — Ch 10

Leniency-biased ratings can still **rank** items consistently if the bias is uniform across raters. The bias is a problem when:

- You want **absolute** quality estimates (not ranks).
- The bias is **non-uniform** across rater segments.
- The dynamic range of the active scale shrinks below the threshold where you can distinguish good from great.

## Mitigation

> *"If you want more granular feedback, removing the strong negative connotation associated with low ratings can help people break out of this bias. For example, instead of showing users numbers one to five, show users options such as the following: 'Great ride. Great driver.' / 'Pretty good.' / 'Nothing to complain about but nothing stellar either.' / 'Could've been better.' / 'Don't match me with this driver again.'"* — Ch 10

Reframing each rating level as a **neutral verbal label** removes the implicit "1 star = punishment" association. Other mitigations: anonymization, removing follow-up "why?" friction on negative ratings, comparative formats instead of absolute.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ExplicitFeedback]] — the feedback class leniency bias hits hardest.
- [[PositionBias]] / [[PreferenceBias]] — sibling Ch 10 biases.
- [[DegenerateFeedbackLoop]] — biases can compound through training loops.
- [[Sycophancy]] — model-side mirror of user-side leniency: training on lenient feedback amplifies sycophancy.
