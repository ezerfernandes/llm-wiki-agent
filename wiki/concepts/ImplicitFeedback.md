---
title: "Implicit Feedback"
type: concept
tags: [recommender-systems, data, user-feedback, llm-app]
sources: [d2l-recommender-systems, d2l-introduction, ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Implicit Feedback

User preference signals **inferred from observable behavior** rather than proactively stated — clicks, purchases, watches, dwell time, plays, mouse movements. Canonicalized as a feedback-type distinct from [[ExplicitFeedback|explicit feedback]] by [[YifanHu|Hu]], [[YehudaKoren|Koren]] & Volinsky 2008.

## Defining traits

- **Abundant** — implicit signals are emitted continuously by every user action; explicit ratings require active user effort and are scarce.
- **Noisy** — *"we can only guess their preferences and true motives"*: a user watching a movie does not imply they liked it. ([[d2l-recommender-systems]])
- **Positive-only by default** — observation = positive signal; absence = ambiguous (real negative OR untracked OR future interaction). The defining modeling challenge.
- **Heteroscedastic confidence** — repeated interaction implies stronger preference than a single click; Hu-Koren-Volinsky introduce confidence weights for this.

## Modeling consequences

- **Pure rating-prediction methods break** — MF and AutoRec ignore unobserved entries; on implicit-only data this means *every prediction is positive*. [[d2l-recommender-systems]] §ranking opens with this critique.
- **Negative sampling becomes mandatory** — unobserved pairs must be sampled as candidate negatives during training ([[NegativeSampling]]). Random per-step sampling is the chapter's default in `PRDataset`.
- **Evaluation switches** from RMSE to ranking metrics — [[HitRate|Hit@k]], [[AUC]], [[NDCG]], MRR.
- **Pairwise / listwise losses replace pointwise MSE** — [[BPR]], [[HingeLossRanking|Hinge]] target relative order across `(positive, negative)` pairs rather than absolute scores.

## Connections
- [[ExplicitFeedback]] — sibling category.
- [[YehudaKoren]] — co-author of the canonical 2008 paper.
- [[NeuMF]], [[CaserModel]], [[BPR]], [[NegativeSampling]] — modeling consequences.
- [[CTRPrediction]] — implicit-feedback's most monetized incarnation.
- [[InteractionMatrix]] — typical data structure.
- [[d2l-recommender-systems]], [[d2l-introduction]] — sources.

## From [[ai-engineering-ch10-architecture-feedback|AI Engineering Ch 10]]

Ch 10 extends the recommender-systems framing into the **LLM application** setting. Two extensions matter:

### LLM-app forms of implicit feedback

The action vocabulary is much richer than clicks / dwell. Per Ch 10, foundation models *"enable a new world of applications and, with them, many genres of implicit feedback."*

- **Conversational actions** — regenerate, edit, delete, share, rename, bookmark.
- **Conversational shape** — turns per conversation, dialogue diversity, early-termination rate.
- **[[NaturalLanguageFeedback|Natural-language feedback]]** — error corrections, rephrases, complaints, sentiment, confirmation requests embedded in the user's normal dialogue.

See [[ConversationalFeedback]] for the LLM-app-specific taxonomy.

### Why interpretation is harder than in classical recsys

> *"Interpreting implicit signals can be challenging. For example, sharing a conversation can either be a negative or a positive signal. For example, one friend of mine mostly shares conversations when the model has made some glaring mistakes, and another friend mostly shares useful conversations with their coworkers."* — Ch 10

The same action means different things to different users. Mitigation: **stack multiple signals**. *"If the user rephrases their question after sharing a link, it might indicate that the conversation didn't meet their expectations."*

### The integration constraint

Implicit feedback is *abundant* only when the AI application is **integrated into the user's primary workflow**. Standalone chat applications miss the rich implicit feedback that copilot-style products collect for free (whether a draft is sent, whether a suggestion is accepted, what edits are made). See [[UserEditFeedback]] / [[GitHubCopilot]] for the design exemplar.
