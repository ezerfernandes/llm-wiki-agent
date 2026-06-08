---
title: "Critique Agent"
type: concept
tags: [agentic-design-patterns, agents, reflection, evaluation, cost-optimization, routing]
sources: [agentic-design-patterns-ch16-resource-aware]
last_updated: 2026-06-07
---

# Critique Agent

A **Critique Agent** (Critic Agent) is a dedicated agent that **evaluates the responses produced by other agents/models and provides feedback** — the quality-assurance arm of a multi-agent system. In [[agentic-design-patterns-ch16-resource-aware|Ch 16 of *Agentic Design Patterns*]] it is the component that closes the feedback loop in the [[ResourceAwareOptimization|Resource-Aware Optimization]] pattern, sitting downstream of a [[ModelRouter|Router Agent]] and its answering models.

## Functions

Ch 16 lists several functions of the Critique Agent's feedback:

1. **Self-correction** — identify errors or inconsistencies, prompting the answering agent to refine its output for improved quality.
2. **Performance monitoring** — systematically assess responses, tracking metrics like accuracy and relevance, which are used for optimization.
3. **RL / fine-tuning signal** — consistent identification of inadequate responses (e.g. from a Flash model) can feed [[ReinforcementLearning|reinforcement learning]] or fine-tuning to refine the router agent's logic.
4. **Indirect budget management** — *"While not directly managing the budget, the Critique Agent contributes to indirect budget management by identifying suboptimal routing choices, such as directing simple queries to a Pro model or complex queries to a Flash model, which leads to poor results. This informs adjustments that improve resource allocation and cost savings."*

The agent can be configured to review **only the generated text**, or **both the original query and the generated text**, enabling a comprehensive evaluation of the response's alignment with the initial question. It operates from a predefined system prompt that establishes its evaluator role, its areas of critical focus, and an emphasis on **constructive** feedback (identifying both strengths and weaknesses) rather than mere dismissal — Ch 16's `CRITIC_SYSTEM_PROMPT` frames it as the "quality assurance arm... to meticulously review and challenge information... guaranteeing accuracy, completeness, and unbiased presentation."

## Relation to Reflection

The Critique Agent is the **[[Reflection|reflection]] / [[SelfCritique|critique]] loop applied to routing quality and resource allocation**. As in Ch 4's Generator–Critic model, separating the critic from the producer yields more robust, less self-biased evaluation; here that separation is also what makes the critic able to police the *router's* decisions and improve cost-efficiency over time.

## Connections

- [[ResourceAwareOptimization]] — the pattern this agent closes the feedback loop for.
- [[ModelRouter]] / [[Routing]] — the router whose decisions the critic refines.
- [[DynamicModelSelection]] — the routing decision the critic flags as suboptimal or not.
- [[Reflection]] / [[SelfCritique]] — the general critique loop this specializes (Ch 4).
- [[LLMAsAJudge]] — the related evaluator-model framing.
- [[ActorCriticAgent]] — the RL actor-critic structure (distinct origin, related critic role).
- [[ReinforcementLearning]] — the feedback signal the critic can supply.
- [[agentic-design-patterns-ch16-resource-aware]] — source.
