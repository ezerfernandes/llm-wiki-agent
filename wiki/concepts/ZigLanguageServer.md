---
title: "Zig Language Server"
type: concept
tags: [zig, lsp, tooling, editor, developer-experience]
sources: [zig-getting-started, zig-tools]
last_updated: 2026-06-07
---

# Zig Language Server (ZLS)

The Zig Language Server, distributed as `zigtools/zls`, is the recommended way to get deep editor integration for the [[Zig]] language — autocompletion, go-to-definition, diagnostics, and other IDE features. It implements the [[LanguageServerProtocol]], so a single server works across any LSP-capable editor.

Per [[zig-getting-started]], all major text editors already provide Zig **syntax highlighting** (bundled or via a plugin), but ZLS is what users should install "if you're interested in a deeper integration between Zig and your editor." The page also points to the website's broader Tools section for the full ecosystem of editor and tooling integrations.

## Editor coverage

The official [[zig-tools]] Tools page splits Zig editor support into two layers and explicitly recommends **preferring a language server (ZLS) over a plain syntax-highlighting extension** "for a richer development experience":

1. **Language Servers** — `zigtools/zls` is the single entry, supplying autocompletion and many other features to any LSP-capable editor.
2. **Text Editors** — per-editor plugins that are "mostly syntax highlighters." Several are maintained under the official `ziglang` org (now on Codeberg):
   - **VS Code** — `ziglang/vscode-zig` (official extension).
   - **Visual Studio** — `ZigVS` (Marketplace).
   - **Sublime Text** — `ziglang/sublime-zig-language`.
   - **Vim** — `ziglang/zig.vim`; see [[VimEditor]].
   - **Emacs** — `ziglang/zig-mode`; see [[EmacsEditor]].
   - **Kate** — `ziglang/kde-syntax-highlighting`.
   - **JetBrains family (IntelliJ IDEA, Fleet)** — `ZigBrains` plugin and a separate Zig Fleet plugin.

The division reinforces ZLS's role: the per-editor plugins mainly handle highlighting, while the intelligent IDE features (completion, diagnostics, navigation) come from pairing the editor with ZLS over LSP.

## Connections

- [[Zig]] — the language ZLS provides editor intelligence for.
- [[LanguageServerProtocol]] — the editor-agnostic protocol ZLS implements.
- [[ZigToolchain]] — the underlying `zig` compiler/build system ZLS complements.
- [[VimEditor]] — Vim integration via the official `ziglang/zig.vim` plugin.
- [[EmacsEditor]] — Emacs integration via the official `ziglang/zig-mode` plugin.
- [[zig-getting-started]] — source recommending `zigtools/zls`.
- [[zig-tools]] — official Tools catalog enumerating ZLS plus per-editor plugins.
