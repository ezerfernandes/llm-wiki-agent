---
title: "Voyager Agent"
type: concept
tags: [agents, skills, tools, minecraft]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# Voyager Agent

**Voyager** (Wang et al. 2023) is the Minecraft-playing agent that introduces a **skill manager** — a system component that **stores successful action-sequences as reusable code-tools**, enabling the agent's tool inventory to grow during operation. Cited in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] as the canonical reference for **AI-created tools**.

## The skill manager

> *"Voyager (Wang et al., 2023) proposes a skill manager to keep track of new skills (tools) that an agent acquires for later reuse. Each skill is a coding program. When the skill manager determines a newly created skill is to be useful (e.g., because it's successfully helped an agent accomplish a task), it adds this skill to the skill library (conceptually similar to the tool inventory). This skill can be retrieved later to use for other tasks."*

The structural innovation: **tool inventory is no longer fixed at design time**. The agent extends its own capabilities by promoting successful action sequences to first-class reusable tools.

## Relation to [[Chameleon]]'s tool transition

[[Chameleon]] introduced [[ToolTransition]] analysis (which tools follow which). Voyager goes one step further: instead of just observing that two tools are often used together, **package the pair as a new composite tool**. Voyager's contribution is the engineering pattern for the loop:

1. Detect that an action sequence succeeded.
2. Extract it as a code program.
3. Store it in a vector-database skill library.
4. Retrieve it for future similar tasks.

## Position in the wiki

The wiki already has a [[voyager|Voyager]] stub citing the substrate-mismatch problem from Xu et al. (skills live in C / weights live in θ). This new page is the **agent-engineering** read of the same paper — the contribution as Huyen frames it, not as Xu et al.'s memory-theoretic critique.

## Connections

- [[Agent]] / [[ToolInventory]] — parent abstractions.
- [[CapabilityExtension]] — Voyager's skills extend agent capability.
- [[VectorDatabase]] — Voyager's skill storage substrate.
- [[Chameleon]] / [[ToolTransition]] — the precursor framing.
- [[skillbank]] / [[skilldiscovery]] / [[skillrl]] / [[skillmd]] — the broader skill-library wiki cluster.
- [[voyager]] — the existing wiki stub on Voyager (memory-theoretic angle).
- [[CodeInterpreter]] — the execution surface for Voyager's coding skills.
- [[ai-engineering-ch06-rag-agents]] — primary source.
