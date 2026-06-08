---
title: "Zig — Getting Started"
type: source
tags: [zig, install, toolchain, tooling, lsp, hello-world]
date: 2026-06-07
source_file: https://ziglang.org/learn/getting-started/
---

## Summary
The official "Getting Started" page from the [[Zig]] Programming Language website, walking a new user from zero to a running program. It explains the difference between tagged releases and development (nightly) builds, then covers every installation path — direct download with manual `PATH` setup, OS package managers (WinGet/Chocolatey/Scoop on Windows, Homebrew/MacPorts on macOS, distro managers on Linux), and building from source. It recommends editor integration via the [[ZigLanguageServer]] (ZLS), then runs a "hello world" through `zig init` + `zig build run`, and points to further learning resources and the [[ZigSoftwareFoundation]].

## Key Claims
- Zig offers two distribution channels: **tagged releases** (recommended for projects with dependencies that benefit from stability) and **development builds** (for people who want to participate in Zig's development).
- Zig installations are **self-contained archives** that can be placed anywhere on the system, and **multiple versions of Zig coexist without issue**.
- **Direct download** is the most straightforward install: grab a bundle for your platform from the Downloads page, extract it to a directory, and add it to `PATH` so `zig` can be invoked from anywhere.
- On **Windows**, `PATH` is set via PowerShell snippets — either system-wide (requires admin PowerShell, modifies the `Machine` environment variable) or per-user (modifies the `User` variable); the snippet must be edited to point at the actual Zig location, and PowerShell must be restarted afterward.
- On **Linux/macOS/BSD**, you add an `export PATH=$PATH:~/path/to/zig` line to a shell startup script (`.profile`, `.zshrc`, …) then `source` it or restart the shell.
- **Windows package managers**: WinGet (`winget install -e --id zig.zig`), Chocolatey (`choco install zig`), Scoop (`scoop install zig`); Scoop also exposes a dev build via the `versions` bucket (`scoop install versions/zig-dev`).
- **macOS package managers**: Homebrew installs the latest tagged release (`brew install zig`); MacPorts (`sudo port install zig`).
- Zig is present in **many Linux package managers**.
- **Building from source** is documented in the project's `README.md` (hosted on Codeberg).
- All major text editors have **Zig syntax highlighting** (some bundle it, some need a plugin); deeper editor integration is provided by `zigtools/zls`, the Zig Language Server.
- The **hello-world workflow** is: `mkdir hello-world`, `cd hello-world`, `zig init` (which scaffolds `build.zig`, `build.zig.zon`, `src/main.zig`, and `src/root.zig`), then `zig build run`, which compiles and runs the executable.
- A correct install prints `All your codebase are belong to us.` followed by `Run \`zig build test\` to run the tests.`
- Users should find documentation matching their Zig version; **nightly builds should use the `master` docs**. The page recommends [zig.guide](https://zig.guide), joining a Zig community, Zig SHOWTIME, and donating to the [[ZigSoftwareFoundation]].
- The page acknowledges Zig is a **young project** without the capacity yet to produce extensive documentation, so community help is encouraged.

## Key Quotes
> "In general, tagged releases are more practical for projects that have dependencies and benefit from stability, while development builds are for people who want to help participate in the development of the Zig project." — on choosing a distribution channel

> "Zig installations are self-contained archives that can be placed anywhere in your system. Multiple versions of Zig coexist without issue." — on the install model

> "If you're interested in a deeper integration between Zig and your editor, checkout zigtools/zls." — on editor tooling (the [[ZigLanguageServer]])

> "All your codebase are belong to us. / Run `zig build test` to run the tests." — output of the generated hello-world program via `zig build run`

> "Zig is a young project and unfortunately we don't have yet the capacity to produce extensive documentation and learning materials for everything…" — on the maturity of the ecosystem

## Connections
- [[Zig]] — this is the canonical onboarding page for the language; defines its install/tooling story.
- [[ZigToolchain]] — the `zig` CLI driver (`zig init`, `zig build`, `zig build run`, `zig build test`) and the self-contained-archive distribution model are described here.
- [[ZigLanguageServer]] — recommended editor integration (`zigtools/zls`) for autocomplete/diagnostics.
- [[LanguageServerProtocol]] — ZLS implements LSP, enabling editor-agnostic integration.
- [[ZigSoftwareFoundation]] — the non-profit stewarding Zig; the page solicits donations to it.
- [[Compiler]] — `zig` is an optimizing compiler; the page describes invoking "the Zig compiler" to build the hello-world binary.
- [[Homebrew]] — listed macOS install path (`brew install zig`).
- [[MacPorts]] — listed macOS install path (`sudo port install zig`).
- [[CrossCompilation]] — not covered on this page, but a hallmark capability of the [[ZigToolchain]] referenced elsewhere.
- [[CLanguage]] — Zig positions itself as a modern alternative to and interoperable with C; relevant context for the toolchain (the `zig cc` C compiler is part of the broader toolchain story).

## Contradictions
- None found. This page introduces a previously-unrepresented topic (the Zig language and its toolchain) and does not conflict with existing wiki content.
