---
title: "Conversational Feedback"
type: concept
tags: [user-feedback, conversational-ai, evaluation, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Conversational Feedback

**Feedback signals extracted from the structure and content of a dialogue between user and AI.** Distinct from classical [[ExplicitFeedback|explicit]] (thumbs / stars) and classical [[ImplicitFeedback|implicit]] (clicks, dwell) feedback — though it is itself an implicit-feedback class. Named in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]] as the **new feedback genre enabled by the conversational interface**.

## Why it's distinctive

> *"The conversational interface that many AI applications use makes it easier for users to give feedback. Users can encourage good behaviors and correct errors the same way they would give feedback in daily dialogues. The language that a user uses to give directions to AI can convey feedback about both the application's performance and the user's preference."* — Ch 10

Classical implicit feedback assumes a small fixed action vocabulary (click, scroll, share). Conversational feedback uses an *open* signal vocabulary — the user's full natural-language repertoire — plus chat-specific actions (regenerate, edit, delete, share, organize).

## Two sub-categories

Ch 10 splits conversational feedback into:

### 1. [[NaturalLanguageFeedback|Natural-language feedback]]

Feedback inferred from the **content** of user messages. Examples:

- [[ErrorCorrection|Error correction]] — *"No, …"* / *"I meant, …"*
- [[RephraseAttempt|Rephrase attempts]] — same question, different words
- [[ActionCorrectingFeedback|Action-correcting feedback]] — *"You should also check XYZ's GitHub"*
- Confirmation requests — *"Are you sure?"* / *"Show me the sources"*
- Complaints — bot is wrong / irrelevant / verbose / lacks detail
- Sentiment — *"Uggh"*; voice loudness in call-center applications
- Model refusal rate as a feedback signal — *"As a language model, I can't do …"*

### 2. [[ImplicitConversationalSignal|Other conversational signals]]

Feedback inferred from user **actions** rather than messages:

- Early termination (stop generation, exit, leave hanging)
- [[RegenerationSignal|Regeneration]] (weaker signal under usage-based billing, stronger under subscription)
- [[UserEditFeedback|User edits]] of model outputs — strongest implicit signal; doubles as preference data
- Conversation organization — delete (strong negative), rename (good content + bad title), share (ambiguous), bookmark
- Conversation length — positive for companions, negative for productivity bots
- Dialogue diversity — long + low-diversity = stuck in a loop

## Three uses

> *"User feedback, extracted from conversations, can be used for evaluation, development, and personalization."*

- **Evaluation** — derive metrics to monitor the application.
- **Development** — train future models or guide their development.
- **Personalization** — adapt the application to each user.

## Why it's hard

> *"Because feedback is blended into daily conversations, it's also challenging to extract. While intuition about conversational cues can help you devise an initial set of signals to look for, rigorous data analysis and user studies are necessary to understand."* — Ch 10

The conversational-feedback extraction problem is itself a research area. Pre-ChatGPT work from the RL community ([[FuEtAl2019|Fu et al. 2019]]; Goyal et al. 2019; Zhou and Small 2020; Sumers et al. 2020) and early conversational AI products ([[Amazon|Amazon Alexa]]: Ponnusamy et al. 2019, Park et al. 2020; [[Spotify]] voice: Xiao et al. 2021; Yahoo! Voice: Hashimoto and Sassano 2018) attacked it.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ExplicitFeedback]] / [[ImplicitFeedback]] — classical sibling categories.
- [[NaturalLanguageFeedback]] / [[ImplicitConversationalSignal]] — sub-categories.
- [[ErrorCorrection]] / [[RephraseAttempt]] / [[ActionCorrectingFeedback]] / [[UserEditFeedback]] / [[RegenerationSignal]] / [[InpaintingFeedback]] — specific signals.
- [[FITSDataset]] — Xu et al. 2022 dataset clustering complaint feedback types.
- [[DataFlywheel]] — feedback feeds the flywheel.
- [[PreferenceFinetuning]] — user-edit and comparative signals can feed preference training.
- [[Sycophancy]] / [[DegenerateFeedbackLoop]] — failure modes if feedback is consumed naively.
