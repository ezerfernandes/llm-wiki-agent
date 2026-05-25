---
title: "Action-Correcting Feedback"
type: concept
tags: [user-feedback, natural-language-feedback, agents, llm-app]
sources: [ai-engineering-ch10-architecture-feedback]
last_updated: 2024-12-04
---

# Action-Correcting Feedback

**A [[NaturalLanguageFeedback|natural-language feedback]] signal where the user nudges an agent toward additional or different actions, rather than correcting the content of a prior response.** Per [[ai-engineering-ch10-architecture-feedback|*AI Engineering* Ch 10]]:

> *"This kind of action-correcting feedback is especially common for agentic use cases where users might nudge the agent toward more optional actions. For example, if a user assigns the agent the task of doing market analysis about company XYZ, this user might give feedback such as 'You should also check XYZ GitHub page' or 'Check the CEO's X profile'."* — Ch 10

## How it differs from [[ErrorCorrection|error correction]]

| Error correction | Action-correcting feedback |
|---|---|
| Targets the **content** of the last response | Targets the **plan / tool-use** of the agent |
| *"Bill is the suspect, not the victim."* | *"You should also check XYZ's GitHub page."* |
| Strongest when the response is text | Strongest in agentic / tool-using applications |

## Why it matters for agents

[[AgenticAI|Agentic systems]] choose **which tools to call and in what order**. Action-correcting feedback is the user's way of editing that plan in flight. Captured systematically, it becomes a corpus of *what the agent should have thought to do* — directly mineable to improve [[Planning|planning]] prompts, expand [[ToolInventory|tool inventories]], or train next-action predictors.

## Detection

Action-correcting feedback often begins with imperatives or "you should" patterns and references specific tools or resources. Combined with an agent's plan log, it can be detected by checking whether the user's follow-up names a tool / resource not in the agent's most recent action sequence.

## Connections

- [[ai-engineering-ch10-architecture-feedback]] — primary source.
- [[NaturalLanguageFeedback]] — parent category.
- [[ErrorCorrection]] / [[RephraseAttempt]] — sibling natural-language signals.
- [[Agent]] / [[AgenticAI]] / [[Planning]] — application context.
- [[ToolInventory]] — what action-correcting feedback often refers to.
- [[ConversationalFeedback]] — grandparent category.
