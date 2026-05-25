---
title: "SWE-agent"
type: concept
tags: [agents, coding, tools]
sources: [ai-engineering-ch06-rag-agents]
last_updated: 2024-12-04
---

# SWE-agent

**SWE-agent** (Yang et al. 2024) is the [[GPT|GPT-4]]-powered **coding agent** Huyen uses in [[ai-engineering-ch06-rag-agents|*AI Engineering* Ch 6]] to illustrate **agent environment + tool inventory** decomposition. Its environment is the computer (terminal + file system); its actions are `navigate repo`, `search files`, `view files`, `edit lines`.

## Why it's the chapter's running coding example

Coding agents anchor the chapter because the environment and tool surface are concrete and visible:

- **Environment**: computer with terminal and filesystem.
- **Actions**: discrete read-action (`navigate`, `search`, `view`) + write-action (`edit lines`).
- **Task**: a GitHub issue → a patch.
- **Reward signal**: tests pass.

The structural elements all map to Huyen's agent framework cleanly.

## Position in the wiki

The wiki's other coding-agent anchor is [[codingagents]]; SWE-agent is the first paper-level instance referenced by an AI-engineering source. Adjacent in coverage: the [[CustomerServiceAgent]] tutorial under [[react|ReAct]].

## Connections

- [[Agent]] — parent abstraction.
- [[ToolInventory]] — SWE-agent's actions form its inventory.
- [[codingagents]] — the broader family.
- [[swebench]] — the benchmark family SWE-agent targets.
- [[CodeInterpreter]] — adjacent capability-extension tool.
- [[ai-engineering-ch06-rag-agents]] — primary source.
