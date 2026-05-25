---
title: "Utterance Intent (Co-STORM)"
type: concept
tags: [discourse, multi-agent]
sources: [2408.15232-co-storm]
last_updated: 2026-05-22
---

# Utterance Intent

In [[CoSTORM|Co-STORM]], each agent utterance $u_i$ is tagged with an **intent** $a_i$, used to (a) decide whether the agent should search before responding and (b) trigger moderator intervention. Taxonomy borrowed from [[QuEtAl2019|Qu et al. 2019]] *User Intent Prediction in Information-seeking Conversations* (CHIIR 2019).

## The four intents

| Intent | Meaning |
|---|---|
| **Original Question** | Initiates a new question. |
| **Information Request** | Seeks additional information from the prior utterance. |
| **Potential Answer** | Offers a possible answer to a previously posed question. |
| **Further Details** | Provides supplementary information to a previous answer. |

## Two groups

Co-STORM groups the four intents into:

- **Question-asking** — {Original Question, Information Request}. No retrieval; LM generates question from discourse history directly.
- **Question-answering** — {Potential Answer, Further Details}. LM generates a search query, retrieves, and produces a cited response.

## Role in turn management

The [[TurnManagement|turn-management protocol]] uses intents to detect when the discourse is stuck: after **$L = 2$ consecutive turns** with intent in the *question-answering* group (Potential Answer / Further Details), Co-STORM invokes the [[ModeratorAgent|moderator]] to redirect.

The intuition: if multiple experts in a row are only elaborating on prior answers, the discourse is converging on a niche. Pulling the moderator in injects a new question grounded in *unused* sources.

## See also
- [[CoSTORM]] · [[TurnManagement]] · [[PerspectiveGuidedExpert]] · [[ModeratorAgent]] · [[ConversationalQA]]
