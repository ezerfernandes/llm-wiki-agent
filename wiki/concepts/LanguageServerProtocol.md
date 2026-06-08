---
title: "Language Server Protocol"
type: concept
tags: [lsp, tooling, editor, developer-experience, protocol]
sources: [zig-getting-started]
last_updated: 2026-06-07
---

# Language Server Protocol (LSP)

The Language Server Protocol (LSP) is an open, editor-agnostic protocol that standardizes communication between a code editor (the *client*) and a *language server* that provides language-aware features: autocompletion, go-to-definition, hover documentation, diagnostics, rename/refactor, and more. Because the protocol decouples editors from languages, a single language server implementation can serve any LSP-capable editor, eliminating the N-editors × M-languages integration explosion.

In the context of [[zig-getting-started]], LSP is the foundation that lets the [[ZigLanguageServer]] (`zigtools/zls`) deliver deep [[Zig]] integration across all major editors, beyond the basic syntax highlighting that editors bundle natively.

## Connections

- [[ZigLanguageServer]] — a concrete LSP implementation for [[Zig]].
- [[Zig]] — one of many languages exposed to editors via an LSP server.
- [[zig-getting-started]] — source where ZLS/LSP editor integration is recommended.
