---
title: "llms.txt"
type: concept
tags: [documentation, standards, llm-context, retrieval]
sources: [dspy-llms-txt-generation-tutorial]
last_updated: 2026-05-24
---

## What it is

**`llms.txt`** is a **proposed standard for project-level documentation written for LLM consumption** — a single markdown file at the root of a project that gives an LLM a structured map of what the project is, what its key concepts are, how it is organized, where the important entry points live, and how it is used.

Analogous in placement and intent to `robots.txt` (machine-readable file at the root of a project that instructs a class of automated agents how to interact with the project), but oriented toward LLMs ingesting the project as context rather than crawlers indexing it.

## Why it matters

A typical README is written for human readers — narrative, marketing-flavored, often missing the structural map of a codebase that an LLM needs in order to be useful when asked questions about it. `llms.txt` is the conjecture that a **purpose-built, LLM-targeted documentation artifact** does better than a README + raw tree dump as a context-window input to downstream LLM-over-this-repo tasks (Q&A, code generation, retrieval).

The wiki has no measurement of whether this conjecture holds — the [[dspy-llms-txt-generation-tutorial|source tutorial]] generates `llms.txt` files but does not score them against the alternative.

## Canonical sections (per the DSPy tutorial-generated artifact)

| Section | Content |
|---|---|
| Project overview | One-paragraph purpose statement. |
| Key concepts | List of terms and abstractions the project relies on. |
| Architecture organization | High-level structural description. |
| Important files and directories | Entry points + key paths. |
| Usage examples | Multiple illustrative examples — the DSPy-generated artifact emits 5 (classifier building, [[rag|RAG]] pipelines, prompt optimization, agent loops, compositional code). |

This is *one* realization of the format — the DSPy tutorial does not claim it is *the* normative section ordering, only that the generated file follows "the standard format."

## How DSPy generates it

[[dspy-llms-txt-generation-tutorial|The DSPy `llms.txt` generation tutorial]] composes a **four-stage [[DSPyModules|`dspy.Module`]]** (`RepositoryAnalyzer`) over GitHub repository metadata:

1. `AnalyzeRepository` — semantic analysis of repo URL + README + file tree → *purpose*, *key concepts*, *architecture*.
2. `AnalyzeCodeStructure` — structural analysis of file tree + package configs → *important directories*, *entry points*, *dev info*.
3. `dspy.ChainOfThought("repo_info -> usage_examples")` — synthesized purpose + concepts → prose usage examples.
4. `GenerateLLMsTxt` — 7-input synthesis Signature → final `llms.txt` markdown.

The first two stages are LM analyses of repo metadata; the third generates illustrative examples; the fourth synthesizes the whole into the canonical file format. All four sub-Modules are wrapped in [[chainofthought|`dspy.ChainOfThought`]].

## Relation to other documentation artifacts

| Artifact | Audience | Format | Generated how? |
|---|---|---|---|
| `README.md` | Humans | Markdown (narrative) | Hand-authored. |
| `llms.txt` | LLMs | Markdown (structured sections) | Hand-authored *or* LLM-generated from repo metadata (the DSPy tutorial pattern). |
| API reference | Both | Often auto-generated | From docstrings (Sphinx, MkDocs, etc.). |
| `CLAUDE.md` / agent instructions | A specific agent | Markdown | Hand-authored; project-specific operating instructions for an agent. |

`llms.txt` differs from `CLAUDE.md` in audience generality: `CLAUDE.md` is *prescriptive* (how *you*, the agent, should behave in this project), while `llms.txt` is *descriptive* (what this project *is*).

## Open questions

- **Does it actually help?** No published measurement in the wiki — neither the source tutorial nor adjacent DSPy tutorials test downstream LM performance with `llms.txt` vs raw README as context.
- **Does it generalize across LMs?** The DSPy-generated artifact is produced by `gpt-4o-mini` and consumed by an unspecified downstream LLM. Cross-LM transfer is untested.
- **What is the normative section ordering?** The tutorial follows "the standard format" without citing the standard's authoring body.
- **Should it cover the whole repo or be path-scoped?** Mono-repos with multiple distinct sub-projects raise this question; the tutorial generates one `llms.txt` per repo and does not address scoping.

## Connections

- [[dspy-llms-txt-generation-tutorial]] — the canonical wiki source for this concept; treats `llms.txt` as the generation target.
- [[Markdown]] — the output format.
- [[Documentation]] — the broader category `llms.txt` is a member of.
- [[DSPyModules]] — `RepositoryAnalyzer` is the `dspy.Module` that generates it.
- [[DSPySignatures]] — `GenerateLLMsTxt` is the 7-input synthesis Signature that produces the final string.
- [[GitHubAPI]] — the data source for repo metadata fed into the generator.
- [[rag|RAG]] — adjacent: `llms.txt` is one candidate document type to index over a repository, vs raw source files.
