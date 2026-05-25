---
title: "Degenerate Feedback Loop"
type: concept
tags: [user-feedback, failure-mode, recommender-systems, alignment, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Degenerate Feedback Loop

**A failure mode where a system's predictions influence the user feedback that trains the next iteration of the system — amplifying initial biases.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"In a system where user feedback is used to modify a model's behavior, degenerate feedback loops can arise. A degenerate feedback loop can happen when the predictions themselves influence the feedback, which, in turn, influences the next iteration of the model, amplifying initial biases."* — Ch 10

Also called **exposure bias**, **popularity bias**, or **filter bubbles** in the recommender-systems literature — *"a well-studied problem"* (Ch 10).

## The video-ranking example

> *"Imagine you're building a system to recommend videos. The videos that rank higher show up first, so they get more clicks, reinforcing the system's belief that they're the best picks. Initially, the difference between the two videos, A and B, might be minor, but because A was ranked slightly higher, it got more clicks, and the system kept boosting it. Over time, A's ranking soared, leaving B behind. This feedback loop is why popular videos stay popular, making it tough for new ones to break through."* — Ch 10

The bias source: **only the top-ranked items get the exposure that produces feedback**. The model never learns what would have happened with the lower-ranked items.

## The cat-photo example (and its dark cousins)

> *"Imagine that initially, a small number of users give feedback that they like cat photos. The system picks up on this and starts generating more photos with cats. This attracts cat lovers, who give more feedback that cat photos are good, encouraging the system to generate even more cats. Before long, your application becomes a cat haven. Here, I use cat photos as an example, but the same mechanism can amplify other biases, such as racism, sexism, and preference for explicit content."* — Ch 10

The mechanism is **user self-selection plus content amplification**: small initial preference signal → system biases its output → biased users self-select into the user base → feedback compounds → product drifts. Cat photos are a benign illustration; the same dynamics drive recommender systems toward extremist content unless explicitly counteracted.

## The connection to [[Sycophancy|sycophancy]]

Ch 10 places **sycophancy** as a degenerate-feedback-loop variant operating at the *response* level rather than the *product* level:

> *"Acting on user feedback can also turn a conversational agent into, for lack of a better word, a liar. Multiple studies have shown that training a model on user feedback can teach it to give users what it thinks users want, even if that isn't what's most accurate or beneficial (Stray, 2023). Sharma et al. (2023) show that AI models trained on human feedback tend toward sycophancy. They are more likely to present user responses matching this user's view."* — Ch 10

Sycophancy is the model-level analog of a content-platform's filter bubble: the model tells each user what *they* want to hear, the same way a recommender platform shows each user what *they* want to see.

## Mitigation

Ch 10's posture is **diagnostic, not prescriptive**:

> *"User feedback is crucial for improving user experience, but if used indiscriminately, it can perpetuate biases and destroy your product. Before incorporating feedback into your product, make sure that you understand the limitations of this feedback and its potential impact."* — Ch 10

The standard recommender-system mitigations (exploration / off-policy correction / inverse-propensity weighting / counterfactual reasoning / forced diversity) apply but are not enumerated in Ch 10.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[Sycophancy]] — model-level instance of the same failure mode.
- [[DataFlywheel]] — the design pattern that degenerate feedback loops corrupt.
- [[LeniencyBias]] / [[PositionBias]] / [[PreferenceBias]] — biases that feed degenerate loops.
- [[ExplicitFeedback]] / [[ImplicitFeedback]] — feedback classes susceptible to loops.
- [[RecommenderSystems]] — the literature where this is most studied.
- [[FeedbackLoop]] — the (control-theoretic) general notion; this page is its *pathological* instance.
