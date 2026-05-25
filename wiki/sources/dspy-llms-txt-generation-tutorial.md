---
title: "DSPy Tutorial — llms.txt Generation from GitHub Repositories"
type: source
tags: [dspy, tutorial, chain-of-thought, signatures, code-generation, documentation, llms-txt, github-api]
date: 2026-05-24
source_file: https://dspy.ai/tutorials/llms_txt_generation/
---

## Summary

Official [[DSPy]] tutorial demonstrating an **automated [[LLMsTxt|`llms.txt`]] generation system** — a [[DSPyModules|`dspy.Module`]] subclass (`RepositoryAnalyzer`) that composes **three custom class-form [[DSPySignatures|Signatures]] plus one inline Signature**, all wrapped under [[chainofthought|`dspy.ChainOfThought`]], to analyze a GitHub repository (file tree, README, package configs) and emit a complete `llms.txt` document. **Inverts the documentation-to-code direction of [[dspy-sample-code-generation-tutorial|the sample code-generation tutorial]]**: there, library docs were the *input* and runnable code was the *output*; here, a code repository is the *input* and structured LLM-friendly documentation is the *output*. **Establishes the *meta-documentation* application rung** in the DSPy tutorial corpus — generating documentation about repositories *for consumption by other LLMs*. Worked example targets `stanfordnlp/dspy` itself.

## Key Claims

- **Four-stage `dspy.ChainOfThought` composition under one `dspy.Module`** is the structural core: `analyze_repo` → `analyze_structure` → `generate_examples` → `generate_llms_txt`. The first two are class-form Signatures; the third uses the **inline string-form** `"repo_info -> usage_examples"`; the fourth is class-form. **First wiki receipt mixing class-form and inline Signatures in the same `dspy.Module`** — a pattern [[DSPySignatures|the Signatures page]] permits but no prior tutorial had demonstrated.
- **DSPy is *not* the data-gathering layer.** Three helper functions (`get_github_file_tree`, `get_github_file_content`, `gather_repository_info`) call the GitHub REST API directly — recursive tree request, base64-decoded file content fetches — *before* any LM call. The Module receives clean strings (`file_tree`, `readme_content`, `package_files`) as input fields. Echoes the [[dspy-sample-code-generation-tutorial|sample-code-generation tutorial's]] *retrieval-then-generation* split with arbitrary GitHub repos in place of arbitrary documentation URLs.
- **`llms.txt` is described as a "proposed standard for providing structured, LLM-friendly documentation about a project."** The tutorial does not cite the originating proposal but treats the format as load-bearing: project overview, key concepts, architecture details, important files/directories, usage examples. Becomes the **first wiki receipt of the [[LLMsTxt]] proposal** as a concrete artifact.
- **`AnalyzeRepository` Signature**: 3 inputs (`repo_url: str`, `file_tree: str`, `readme_content: str`) → 3 outputs (`project_purpose: str`, `key_concepts: list[str]`, `architecture_overview: str`). Class form is **mandatory** because `key_concepts` is a `list[str]` container ([[DSPySignatures|per the type-system tiers]]).
- **`AnalyzeCodeStructure` Signature**: 2 inputs (`file_tree: str`, `package_files: str`) → 3 outputs (`important_directories: list[str]`, `entry_points: list[str]`, `development_info: str`). Same `list[str]` justification for class form.
- **`GenerateLLMsTxt` Signature**: 7 inputs (the union of upstream outputs plus a `usage_examples: str` from stage 3) → 1 output (`llms_txt_content: str`). **The widest input fan-in of any Signature in the DSPy tutorial corpus** — 7 fields, two of which are `list[str]` containers and the rest `str`.
- **The third stage uses inline string-form Signatures**: `dspy.ChainOfThought("repo_info -> usage_examples")`. Both fields default to `str` per the inline-form convention. The *only* place in the tutorial where the lightweight inline form is used; the three load-bearing Signatures all use the class form because of container-typed I/O.
- **LM configuration is `gpt-4o-mini` via `dspy.LM(model="gpt-4o-mini")` + `dspy.configure(lm=lm)`** — the default LM choice across the DSPy tutorial corpus. Consistent with [[dspy-sample-code-generation-tutorial]], [[dspy-rag-tutorial]], [[dspy-entity-extraction-tutorial]], and the canonical `dspy.LM("openai/gpt-4o-mini")` opener from [[dspy-programming-overview]].
- **No [[DSPyOptimizers|Optimizer]], no [[DSPyMetrics|metric]], no eval set, no benchmark dataset.** Pure Programming-stage receipt — exits at rung 1 of [[DSPyProgrammingModel|the three-stage workflow]]. The tutorial does not measure `llms.txt` quality numerically; output is qualitative.
- **Output is written to a plain `llms.txt` file via a context-managed file write** — no JSON, no schema. The Module returns `dspy.Prediction(llms_txt_content=..., analysis=..., structure=...)` and `.llms_txt_content` is the only field consumed downstream.

## Key Quotes

> "llms.txt as a proposed standard for providing structured, LLM-friendly documentation about a project."

## Code Receipt — structural

```python
import os
import dspy

class AnalyzeRepository(dspy.Signature):
    """Analyze a repository structure and identify key components."""
    repo_url: str = dspy.InputField(desc="GitHub repository URL")
    file_tree: str = dspy.InputField(desc="Repository file structure")
    readme_content: str = dspy.InputField(desc="README.md content")

    project_purpose: str = dspy.OutputField(desc="Main purpose and goals of the project")
    key_concepts: list[str] = dspy.OutputField(desc="List of important concepts and terminology")
    architecture_overview: str = dspy.OutputField(desc="High-level architecture description")

class AnalyzeCodeStructure(dspy.Signature):
    """Analyze code structure to identify important directories and files."""
    file_tree: str = dspy.InputField(desc="Repository file structure")
    package_files: str = dspy.InputField(desc="Key package and configuration files")

    important_directories: list[str] = dspy.OutputField(desc="Key directories and their purposes")
    entry_points: list[str] = dspy.OutputField(desc="Main entry points and important files")
    development_info: str = dspy.OutputField(desc="Development setup and workflow information")

class GenerateLLMsTxt(dspy.Signature):
    """Generate a comprehensive llms.txt file from analyzed repository information."""
    project_purpose: str = dspy.InputField()
    key_concepts: list[str] = dspy.InputField()
    architecture_overview: str = dspy.InputField()
    important_directories: list[str] = dspy.InputField()
    entry_points: list[str] = dspy.InputField()
    development_info: str = dspy.InputField()
    usage_examples: str = dspy.InputField(desc="Common usage patterns and examples")

    llms_txt_content: str = dspy.OutputField(desc="Complete llms.txt file content following the standard format")

class RepositoryAnalyzer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.analyze_repo = dspy.ChainOfThought(AnalyzeRepository)
        self.analyze_structure = dspy.ChainOfThought(AnalyzeCodeStructure)
        self.generate_examples = dspy.ChainOfThought("repo_info -> usage_examples")
        self.generate_llms_txt = dspy.ChainOfThought(GenerateLLMsTxt)

    def forward(self, repo_url, file_tree, readme_content, package_files):
        repo_analysis = self.analyze_repo(
            repo_url=repo_url,
            file_tree=file_tree,
            readme_content=readme_content,
        )
        structure_analysis = self.analyze_structure(
            file_tree=file_tree,
            package_files=package_files,
        )
        usage_examples = self.generate_examples(
            repo_info=f"Purpose: {repo_analysis.project_purpose}\nConcepts: {repo_analysis.key_concepts}"
        )
        llms_txt = self.generate_llms_txt(
            project_purpose=repo_analysis.project_purpose,
            key_concepts=repo_analysis.key_concepts,
            architecture_overview=repo_analysis.architecture_overview,
            important_directories=structure_analysis.important_directories,
            entry_points=structure_analysis.entry_points,
            development_info=structure_analysis.development_info,
            usage_examples=usage_examples.usage_examples,
        )
        return dspy.Prediction(
            llms_txt_content=llms_txt.llms_txt_content,
            analysis=repo_analysis,
            structure=structure_analysis,
        )

# Invocation
lm = dspy.LM(model="gpt-4o-mini")
dspy.configure(lm=lm)

analyzer = RepositoryAnalyzer()
repo_url = "https://github.com/stanfordnlp/dspy"
file_tree, readme_content, package_files = gather_repository_info(repo_url)

result = analyzer(
    repo_url=repo_url,
    file_tree=file_tree,
    readme_content=readme_content,
    package_files=package_files,
)

with open("llms.txt", "w") as f:
    f.write(result.llms_txt_content)
```

## Data-Gathering Helpers (non-DSPy)

| Helper | Purpose |
|---|---|
| `get_github_file_tree(repo_url)` | Recursive GitHub REST tree request → returns serialized file tree string. |
| `get_github_file_content(repo_url, path)` | Per-file fetch → base64-decoded content for README + package configs. |
| `gather_repository_info(repo_url)` | Orchestrator — returns `(file_tree, readme_content, package_files)` tuple consumed by the Module. `package_files` aggregates `pyproject.toml`, `setup.py`, and similar configuration files. |

All three are plain Python over the GitHub REST API. **DSPy receives only strings** — there is no DSPy-aware retrieval layer, no [[react|ReAct]] tool invocation, no vector index. The split mirrors the pre-call HTTP fetching pattern established in [[dspy-sample-code-generation-tutorial]].

## Position in the DSPy Tutorial Corpus

Coverage map after this ingest:

| Tutorial | Task shape | Optimizer? | Distinctive structural property |
|---|---|---|---|
| [[dspy-conversation-history]] | Multi-turn chatbot | — | `dspy.History` field type |
| [[dspy-customer-service-agent]] | 7-tool [[react\|ReAct]] agent | — | Pydantic domain model |
| [[dspy-custom-module]] | 3-stage [[rag\|RAG]] template | — | `dspy.Module` subclass with `forward()` |
| [[dspy-tutorial-rag-as-agent]] | Multi-hop ReAct agent | MIPROv2 | Teacher/student decoupling |
| [[dspy-rag-tutorial]] | Single-hop RAG | MIPROv2 | `SemanticF1` LLM-as-judge metric |
| [[dspy-entity-extraction-tutorial]] | Decoder-LM NER | MIPROv2 | CoNLL-2003 with `list[str]` outputs |
| [[dspy-tutorial-math]] | Single-step CoT | MIPROv2 | `dspy.datasets.MATH` + 4+4 demos |
| [[dspy-ai-text-game-tutorial]] | Interactive fiction | — | 3 Signatures, deterministic state |
| [[dspy-sample-code-generation-tutorial]] | Doc-driven code gen | — | 2 Signatures + HTTP-fetching pre-layer |
| **dspy-llms-txt-generation-tutorial** *(this page)* | **Repo → `llms.txt` doc gen** | **—** | **3 class-form + 1 inline Signature; 4-stage Module; GitHub API pre-layer** |

## Structural Firsts in the Wiki

1. **First DSPy tutorial mixing class-form and inline string-form Signatures inside the same `dspy.Module`.** `analyze_repo`, `analyze_structure`, and `generate_llms_txt` are class-form (containers in I/O force this); `generate_examples` is `dspy.ChainOfThought("repo_info -> usage_examples")` — pure string form, both fields default to `str`. Confirms [[DSPySignatures|the inline-form-when-everything-is-str discipline]] as practiced, not just permitted.
2. **First DSPy tutorial whose explicit motivating use case is *generating documentation for LLM consumption***. Distinct from RAG (Q&A over a corpus), agents (tool use), and code generation (executable artifacts). The output is a markdown file *whose intended reader is another LLM*.
3. **First wiki receipt of the [[LLMsTxt|`llms.txt`]] proposal** as a concrete artifact target.
4. **First DSPy tutorial using the GitHub REST API as the canonical pre-LLM data source.** Establishes the *GitHub-tree-and-README → DSPy* pre-processing pattern complementary to the [[dspy-sample-code-generation-tutorial|HTML-to-markdown-via-html2text]] pattern.
5. **Widest input fan-in in any DSPy tutorial Signature on record — 7 fields on `GenerateLLMsTxt`.** Two `list[str]`, five `str`. Operates as a structured-aggregation Signature whose role is *synthesis*, not analysis.
6. **First DSPy tutorial whose worked example is the DSPy repository itself** (`stanfordnlp/dspy`). The tutorial is *self-referential* — DSPy generating `llms.txt` *about* DSPy.

## Three-Plus-One Signature Decomposition

The tutorial's generalizable design move is splitting repo-to-`llms.txt` into **three narrower analysis Signatures plus one synthesis Signature** rather than a single `repo -> llms.txt` Signature:

| Signature | Stage role | Form | Why narrower works |
|---|---|---|---|
| `AnalyzeRepository` | Semantic | Class (container output) | Sees repo URL + README + tree; emits *purpose* + *concepts* + *architecture* — high-level conceptual map. |
| `AnalyzeCodeStructure` | Structural | Class (container outputs) | Sees tree + package files; emits *directories* + *entry points* + *dev info* — file-system map. The semantic stage does not see package configs; the structural stage does not see README prose. |
| `dspy.ChainOfThought("repo_info -> usage_examples")` | Illustrative | Inline string | Sees a compact synthesis of upstream purpose + concepts; emits prose usage examples. Smallest envelope — no raw tree, no package files, no README. |
| `GenerateLLMsTxt` | Synthesis | Class (mixed I/O) | Sees the unioned outputs of all three upstream stages + the usage examples; emits the final document. The only stage that touches everything. |

This is the [[DSPyProgrammingModel|*separation-of-concerns* discipline]] applied across **four** Signatures rather than two ([[dspy-sample-code-generation-tutorial]]) or three ([[dspy-custom-module]]). Each upstream Signature has a narrower typed contract; the downstream synthesis Signature sees structured intermediates rather than raw HTML or raw tree dumps.

## llms.txt Output Structure

The tutorial states the generated `llms.txt` includes:

- Project overview
- Key concepts
- Architecture organization
- Important files and directories
- **Five illustrative usage examples**: classifier building, RAG pipelines, prompt optimization, agent loops, and compositional code.

The five named usage example categories are themselves a small ontology of DSPy application shapes — they map closely to the application clusters covered across the DSPy tutorial corpus: classifier ≈ [[dspy-entity-extraction-tutorial|entity extraction]], RAG ≈ [[dspy-rag-tutorial]], optimization ≈ [[DSPyOptimizers]], agent loops ≈ [[dspy-tutorial-rag-as-agent|RAG-as-agent]] / [[react|ReAct]], compositional code ≈ [[dspy-custom-module|custom modules]].

## Suggested Extensions (from the tutorial)

| Extension | Significance |
|---|---|
| Multi-repository analysis | Batch the `RepositoryAnalyzer` over many repos — cross-repo concept overlap discovery. |
| Alternative documentation format support | README, API reference, getting-started — same Module, different output Signature. |
| Quality assessment metrics | The missing rung — would convert this from Programming-stage-only to a full [[DSPyProgrammingModel|three-stage workflow]] receipt. Would require an authored eval set of *good* `llms.txt` files. |
| Interactive web interface | Frontend over the analyzer; orthogonal to the DSPy core. |

## Connections

- [[DSPy]] — the framework being demonstrated.
- [[LLMsTxt]] — the proposed standard the tutorial targets; first wiki receipt.
- [[chainofthought|`dspy.ChainOfThought`]] — wraps all four sub-Modules; the unexamined *start simple* default from [[dspy-programming-overview]].
- [[DSPySignatures]] — three class-form Signatures (`AnalyzeRepository`, `AnalyzeCodeStructure`, `GenerateLLMsTxt`) + one inline Signature (`"repo_info -> usage_examples"`); class form **required** wherever `list[str]` appears in I/O.
- [[DSPyModules]] — `RepositoryAnalyzer` is the `dspy.Module` subclass that composes the four sub-Modules through an explicit `forward()`.
- [[DSPyPrediction]] — `dspy.Prediction(llms_txt_content=..., analysis=..., structure=...)` is the return-value shape; the caller reads `.llms_txt_content`.
- [[DSPyLM]] — `dspy.LM(model="gpt-4o-mini")` + `dspy.configure(lm=lm)` is the LM-configuration idiom; consistent across the tutorial corpus.
- [[DSPyProgrammingModel]] — Programming-stage-only receipt; exits at rung 1.
- [[dspy-sample-code-generation-tutorial]] — closest sibling: same pre-call external-data-fetching pattern, inverted task direction (docs→code vs repo→docs).
- [[dspy-custom-module]] — the canonical multi-Signature `dspy.Module` template; this tutorial extends the pattern from 3 stages to 4 and from all-class-form to mixed class/inline.
- [[dspy-rag-tutorial]] — referenced as one of the five usage-example categories the generated `llms.txt` covers.
- [[dspy-entity-extraction-tutorial]] — adjacent for the "classifier building" usage-example category.
- [[dspy-tutorial-rag-as-agent]] — adjacent for the "agent loops" usage-example category.
- [[Markdown]] — output format of `llms.txt`.
- [[GitHubAPI]] — the data-gathering layer; first wiki concept receipt.

## Contradictions

None with the existing wiki. The tutorial reinforces:

- The [[chainofthought|`dspy.ChainOfThought`]] *start simple* default — all four sub-Modules are wrapped in `ChainOfThought` with no justification given.
- The [[DSPySignatures|class-form mandatory for container-typed I/O]] discipline ([[dspy-ai-text-game-tutorial|cross-confirmed]], [[dspy-sample-code-generation-tutorial|cross-confirmed]]).
- The pattern that **Programming-stage-only DSPy tutorials skip both metric and Optimizer** ([[dspy-ai-text-game-tutorial|sibling]], [[dspy-sample-code-generation-tutorial|sibling]]) — the absence is deliberate when output quality is qualitative.
- The pre-call external-data-fetching pattern is **not** a [[react|ReAct]] tool call — it is plain Python over a REST API that produces strings consumed as input fields ([[dspy-sample-code-generation-tutorial|cross-confirmed]] with `requests` + `BeautifulSoup` + `html2text`).

## Scope-Limit Gaps

- **`llms.txt` proposal not cited.** The tutorial calls it "a proposed standard" without naming Jeremy Howard's `llmstxt.org` proposal or any specific authoring body. The wiki [[LLMsTxt]] page must source-attribute independently.
- **No measured quality of generated `llms.txt`.** No metric, no eval set, no comparison to a hand-authored `llms.txt`, no comparison across LM choices. The output is shown but never scored.
- **No [[DSPyOptimizers|Optimizer]] applied.** The tutorial explicitly notes "quality assessment metrics" as an *extension* — the unexplored rung that would close the [[DSPyProgrammingModel|three-stage workflow]].
- **No rate-limiting / authentication discussion** for the GitHub API helpers. Unauthenticated GitHub REST hits 60 req/h; repos with large trees may exceed this in a single `gather_repository_info` call. The helpers' code is not shown verbatim — only their roles.
- **No prompt-injection hardening.** The system feeds arbitrary repo READMEs into LM context. A README containing instructions targeted at the analyzer Module would be passed straight through.
- **`generate_examples` Signature is inline** — `"repo_info -> usage_examples"` — and its input is a manually formatted f-string concatenation (`f"Purpose: {repo_analysis.project_purpose}\nConcepts: {repo_analysis.key_concepts}"`). The choice to inline-format the *purpose + concepts* into a single string rather than passing two separate fields is a structural decision worth noting; it loses the benefit of typed I/O for that stage.
- **No caching layer for the analysis stages.** `AnalyzeRepository` and `AnalyzeCodeStructure` outputs are deterministic functions of the repo at a commit — both could be cached on the commit SHA. The tutorial does not propose this.
- **No discussion of how `llms.txt` interacts with [[rag|RAG]] over a codebase.** The generated file is presumably ingestible by other LLMs as context — but the tutorial does not measure whether it actually improves downstream LM-over-this-repo performance vs raw README.
