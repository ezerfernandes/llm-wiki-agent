---
title: "Zig — Tools"
type: source
tags: [zig, tooling, editor, lsp, developer-experience]
date: 2026-06-07
source_file: https://ziglang.org/learn/tools/
---

## Summary
The official "Tools" page under Zig's Learn section is a curated catalog of editor-integration tooling for the [[Zig]] language. It is organized into two categories: **Language Servers** (editor-agnostic tools delivering syntax highlighting, autocompletion, and richer features) and **Text Editors** (per-editor plugins, mostly syntax highlighters). It recommends preferring a language server over a plain syntax-highlighting extension for a richer development experience. Notably, the page does *not* cover the formatter (`zig fmt`), build/CI tooling, package/registry tooling, or debuggers — it is scoped entirely to editor/IDE integration.

## Key Claims

### Language Servers (editor-agnostic)
- Language servers are described as "editor-agnostic tools for obtaining syntax highlighting, autocompletion, and many other features." This is the [[LanguageServerProtocol]] model — one server serves any LSP-capable editor.
- Users are explicitly advised to **prefer a language server over a syntax-highlighting extension** "for a richer development experience."
- The single language server listed is **`zigtools/zls`** (the [[ZigLanguageServer]]), hosted at `github.com/zigtools/zls`.

### Text Editors (per-editor plugins, mostly syntax highlighters)
The page describes these as "Editor-specific tools, mostly syntax highlighters." Many of the editor plugins are maintained under the official `ziglang` organization (now on Codeberg):
- **VS Code** — `ziglang/vscode-zig` (`codeberg.org/ziglang/vscode-zig`), the official VS Code extension.
- **Visual Studio** — `ZigVS` (LuckystarStudio, on the Visual Studio Marketplace).
- **Sublime Text** — `ziglang/sublime-zig-language` (`codeberg.org/ziglang/sublime-zig-language`).
- **Vim** — `ziglang/zig.vim` (`codeberg.org/ziglang/zig.vim`); see [[VimEditor]].
- **Emacs** — `ziglang/zig-mode` (`codeberg.org/ziglang/zig-mode`); see [[EmacsEditor]].
- **Kate** — `ziglang/kde-syntax-highlighting` (`codeberg.org/ziglang/kde-syntax-highlighting`), the KDE syntax-highlighting integration.
- **JetBrains family (IntelliJ IDEA, Fleet)** — `ZigBrains` (JetBrains plugin #22456) and a separate **Zig Fleet Plugin** (JetBrains plugin #26070).

### Scope notes
- The plugins themselves are "mostly syntax highlighters"; the deeper IDE features (completion, go-to-definition, diagnostics) come from pairing an editor with ZLS over LSP rather than from the per-editor plugins alone.
- Several editor integrations live in the official `ziglang` org and have migrated to Codeberg, mirroring the main `ziglang/zig` repository's move there.

## Key Quotes
> "Language servers are editor-agnostic tools for obtaining syntax highlighting, autocompletion, and many other features. Consider using a Language server over a syntax-highlighting extension for a richer development experience." — Language Servers section

> "Editor-specific tools, mostly syntax highlighters." — Text Editors section intro

## Connections
- [[Zig]] — the language all of these tools integrate with.
- [[ZigLanguageServer]] — `zigtools/zls`, the one language server the page recommends; the hub of the editor-integration story.
- [[LanguageServerProtocol]] — the editor-agnostic protocol that lets a single ZLS instance serve every listed editor.
- [[ZigToolchain]] — the underlying `zig` CLI that ZLS and the editor plugins complement (this page does not itself cover the toolchain/`zig fmt`).
- [[VimEditor]] — target of the official `ziglang/zig.vim` plugin.
- [[EmacsEditor]] — target of the official `ziglang/zig-mode` plugin.

## Contradictions
- None. This page is consistent with [[zig-getting-started]], which already states all major editors ship/offer Zig syntax highlighting and recommends installing ZLS for deeper integration. This page simply enumerates the per-editor plugins behind that statement.
