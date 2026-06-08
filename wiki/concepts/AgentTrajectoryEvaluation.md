---
title: "Agent Trajectory Evaluation"
type: concept
tags: [agents, agentic-design-patterns, evaluation, trajectory, tool-use, multi-agent]
sources: [agentic-design-patterns-ch19-evaluation]
last_updated: 2026-06-07
---

# Agent Trajectory Evaluation

**Agent trajectory evaluation** is the practice of judging not just an agent's *final output* but the **trajectory** — the sequence of steps, tool selections, and intermediate decisions taken to reach a solution. Introduced as a core sub-technique of the [[EvaluationAndMonitoring|Evaluation and Monitoring]] pattern in [[AntonioGulli|Gulli]]'s [[AgenticDesignPatterns|*Agentic Design Patterns*]] ([[agentic-design-patterns-ch19-evaluation|Ch 19]]).

## Why trajectory, not just output
Traditional software tests give predictable pass/fail results; agents operate **probabilistically**, so evaluation must assess *both* the final output and the path taken. *"Analyzing trajectory and tool use includes evaluating the steps an agent employs to achieve a goal, such as tool selection, strategies, and task efficiency."* Example: an agent answering a product query might ideally follow `intent determination → database search tool → result review → report generation`. The agent's **actual** actions are compared to this **expected (ground-truth) trajectory** to find errors and inefficiencies.

## Trajectory comparison methods
- **Exact match** — a perfect match to the ideal sequence (for high-stakes scenarios).
- **In-order match** — correct actions in order, extra steps allowed.
- **Any-order match** — correct actions in any order, extra steps allowed.
- **Precision** — relevance of the predicted actions.
- **Recall** — how many essential actions were captured.
- **Single-tool use** — checking for a specific action.

Metric selection depends on the agent's requirements: high-stakes → exact match; more flexible situations → in-order / any-order.

## Test files vs evalsets ([[GoogleADK|ADK]])
Ch 19 names two evaluation artifact types (concretely realized in [[GoogleADK|Google's ADK]]):
- **Test files** — JSON, one **single session** with multiple turns; each turn captures the user query, **expected tool-use trajectory**, intermediate responses, and final response. Ideal for **unit testing** during active development (rapid, simple sessions). Organizable into folders with an optional `test_config.json` defining evaluation criteria. *(Example: "Turn off device_2 in the Bedroom" → expected `set_device_info(location=Bedroom, device_id=device_2, status=OFF)` → final "I have set the device_2 status to off.")*
- **Evalset files** — use an **"evalset" dataset** for complex, lengthy, multi-turn sessions and integration tests. An evalset comprises multiple **"evals,"** each a distinct session with one or more turns (user queries, expected tool use, intermediate responses, reference final response). *(Example: "Roll a 10-sided dice twice and then check if 9 is a prime" → expected `roll_die` calls + a `check_prime` call + a summarizing final response.)*

## Multi-agent trajectory evaluation
Evaluating a multi-agent system ([[MultiAgentCollaboration]]) is *"like assessing a team project."* The many steps and handoffs are an advantage — quality can be checked at each stage, both per-agent and system-wide. Key questions:
- **Are agents cooperating effectively?** (e.g. does a Flight-Booking Agent pass the correct dates to the Hotel-Booking Agent?)
- **Did they make a good plan and stick to it?** (deviation, or an agent stuck endlessly searching for a "perfect" rental car)
- **Is the right agent chosen for the task?** (a Weather Agent for live weather, not a General Knowledge Agent)
- **Does adding more agents improve performance?** (a new Restaurant-Reservation Agent — net benefit or conflict/slowdown → a scalability problem)

## Connections
- [[EvaluationAndMonitoring]] — the parent Ch 19 pattern.
- [[GoogleADK]] — test files, evalsets, `AgentEvaluator.evaluate`, `adk eval`.
- [[ToolUse]] — tool selection is the primary trajectory dimension.
- [[Planning]] — plan adherence is evaluated in multi-agent trajectories.
- [[MultiAgentCollaboration]] — cooperation, handoffs, right-agent-for-task, scalability.
- [[ReasoningTechniques]] — the reasoning process is part of the trajectory.
- [[LLMAsAJudge]] — can score trajectory quality where exact-match is too rigid.
- [[EvaluationTrace]] / [[RequestTrace]] — the recorded execution path the trajectory is read from.
- [[AgenticDesignPatterns]] — book hub; [[agentic-design-patterns-ch19-evaluation|Ch 19]].
