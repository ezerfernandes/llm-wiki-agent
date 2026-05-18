---
title: "Anthropic"
type: entity
tags: [organization, ai-lab, frontier-lab, protocol-author]
sources: [2604.25067-frontier-coding-agents-c4, dspy-mcp, dspy-language-models]
last_updated: 2026-05-17
---

# Anthropic

AI safety company. Develops the [[ClaudeOpus47|Claude family]] (Opus / Sonnet / Haiku tiers; Mythos was reportedly held back over advanced cybersecurity capability — see [[2604.25067-frontier-coding-agents-c4]]). Surfaced in the wiki corpus in three distinct roles:

- **Frontier-model provider.** Developer of [[ClaudeOpus47|Claude Opus 4.7]], the dominant agent in the [[2604.25067-frontier-coding-agents-c4|C4-AlphaZero benchmark]] (7/8 wins as first-mover vs Pons solver). Surfaced as a Conductor worker provider in [[2512.04388-conductor]].
- **Managed-API LM provider via [[DSPy]] / [[LiteLLM]].** [[dspy-language-models|`dspy.LM('anthropic/claude-sonnet-4-5-20250929')`]] is one of the canonical managed-API examples DSPy demonstrates through the [[DSPyLM|`dspy.LM`]] universal client routed through [[LiteLLM]]. Anthropic is one of eight managed-API providers in DSPy's provider matrix.
- **Originator of the [[ModelContextProtocol|Model Context Protocol (MCP)]].** Authored and published the open standard for connecting LLMs to external tools and context via standalone servers ([modelcontextprotocol.io](https://modelcontextprotocol.io/)). MCP is **framework-agnostic** — [[DSPy]] consumes it via [[DSPyMCP|`dspy.Tool.from_mcp_tool(...)`]] ([[dspy-mcp]], page 8 of 13 of the DSPy *Learn* corpus), [[ClaudeCode|Claude Code]] consumes it natively, and a growing ecosystem of independent MCP clients implements the same protocol. This is the wiki's first record of an Anthropic-authored open standard outside of the model-development thread.

## Connections

- [[claudeopus47|ClaudeOpus47]] — Anthropic's flagship frontier model; dominant in the C4-AlphaZero benchmark.
- [[claudeopus46|ClaudeOpus46]] — prior-generation Opus model.
- [[claudecode|ClaudeCode]] — Anthropic's coding agent; native MCP client.
- [[ModelContextProtocol]] — Anthropic-authored open protocol for tool/context plumbing between LMs and external services.
- [[DSPyMCP]] — DSPy's binding to MCP; one consumer among many.
- [[DSPyLM]] — DSPy's universal LM client; lists Anthropic as a managed-API provider via [[LiteLLM]].
- [[LiteLLM]] — provider-abstraction layer that routes Anthropic API calls.
- [[2604.25067-frontier-coding-agents-c4]] — C4 benchmark where Claude Opus 4.7 dominates.
- [[2512.04388-conductor]] — names Anthropic as a worker provider.
- [[dspy-mcp]] — page 8 of 13 of the DSPy *Learn* documentation; records the MCP integration.
- [[dspy-language-models]] — page 3 of 13; records Anthropic as one of eight managed-API LM providers DSPy spans.
