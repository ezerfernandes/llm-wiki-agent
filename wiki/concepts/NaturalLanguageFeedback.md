---
title: "Natural Language Feedback"
type: concept
tags: [user-feedback, conversational-ai, nlp, evaluation]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Natural Language Feedback

**Feedback extracted from the *content of user messages* in a conversation — corrections, complaints, rephrases, sentiment, confirmation requests, action nudges.** One of two sub-categories of [[ConversationalFeedback|conversational feedback]] in [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]; the sibling is [[ImplicitConversationalSignal]] (action-based).

> *"Feedback extracted from the content of messages is called natural language feedback. … It's useful to track these signals in production to monitor your application's performance."* — Ch 10

## Signal taxonomy

### Early termination (Ch 10 names this as natural-language even though it's behavioral — Huyen groups it here under "how a conversation is going")

User stops a generation halfway, exits the app, tells the model to stop, or leaves an agent's prompt unanswered. *"It's likely that the conversation isn't going well."*

### [[ErrorCorrection|Error correction]]

*"If a user starts their follow-up with 'No, …' or 'I meant, …', the model's response is likely off the mark."*

### [[RephraseAttempt|Rephrase attempts]]

User rewords the same question. Figure 10-12 in Ch 10 shows an example. Detection: heuristic similarity or a small classifier.

### Specific corrections

*"If a user asks the model to summarize a story and the model confuses a character, this user can give feedback such as: 'Bill is the suspect, not the victim.'"*

### [[ActionCorrectingFeedback|Action-correcting feedback]]

Especially common in agentic settings: *"You should also check XYZ GitHub page"* / *"Check the CEO's X profile."* The user is steering the agent's tool-use plan.

### Confirmation requests

*"Are you sure?"*, *"Check again"*, *"Show me the sources"*. Doesn't necessarily mean the model is wrong — *"it might mean that your model's answers lack the details the user is looking for. It can also indicate general distrust in your model."*

### [[UserEditFeedback|User edits]]

When the application supports direct editing of model output, a user edit is *"a very strong signal that the code [or text] that got edited isn't quite right."* Also produces a preference pair (original = losing, edited = winning).

### Complaints

Often without an attempt to correct: *"wrong, irrelevant, toxic, lengthy, lacking detail, or just bad."* Ch 10 reproduces the [[FITSDataset|FITS dataset]] eight-cluster complaint taxonomy from Xu et al. 2022:

| % | Cluster |
|---|---|
| 26.54% | Clarify demand again |
| 16.20% | Doesn't answer / irrelevant / asks user to find out |
| 16.17% | Point out specific search results that answer the question |
| 15.27% | Suggest the bot should use the search results |
| 11.27% | Factually incorrect / not grounded |
|  9.39% | Not specific / accurate / complete / detailed |
|  4.17% | Bot lacks confidence ("I am not sure …") |
|  0.99% | Repetition / rudeness |

### Sentiment

*"Complaints can also be general expressions of negative sentiments (frustration, disappointment, ridicule, etc.) without explaining the reason why, such as 'Uggh'."* Some call centers track voice loudness through a call as a sentiment proxy.

### Model-side refusal as a signal

*"Natural language feedback can also be inferred from the model's responses. One important signal is the model's refusal rate. If a model says things like 'Sorry, I don't know that one' or 'As a language model, I can't do …', the user is probably unhappy."*

## Extraction

Heuristics work for surface patterns ("No, ", "I meant"); fine-tuned classifiers handle rephrase detection and complaint classification; embedding similarity catches paraphrases. [[SentimentAnalysis|Sentiment-analysis]] models cover the affect axis.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[ConversationalFeedback]] — parent category.
- [[ImplicitConversationalSignal]] — sibling category (action-based).
- [[ErrorCorrection]] / [[RephraseAttempt]] / [[ActionCorrectingFeedback]] / [[UserEditFeedback]] — specific signal pages.
- [[FITSDataset]] — Xu et al. 2022 complaint taxonomy.
- [[SentimentAnalysis]] — extraction technique for the sentiment axis.
- [[FalseRefusalRate]] / [[RefusalRate]] — model-side refusal as a feedback signal.
- [[PreferenceFinetuning]] — user edits feed preference data.
