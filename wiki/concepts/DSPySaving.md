---
title: "DSPy Saving"
type: concept
tags: [dspy, persistence, serialization, deployment, security, backward-compatibility]
sources: [dspy-saving-tutorial, dspy-optimizers, dspy-optimization-overview, dspy-optimizer-tracking-tutorial, dspy-deployment-tutorial]
last_updated: 2026-05-24
---

# DSPy Saving

**DSPy Saving** is the framework's **two-mode program-persistence surface** — the discipline that turns a runnable, optimized [[DSPyModules|`dspy.Module`]] subclass into a durable artifact on disk and back. Introduced canonically by [[dspy-saving-tutorial|the Saving and Loading tutorial]] (`https://dspy.ai/tutorials/saving/`), the surface composes orthogonally over every prior DSPy artifact — [[DSPySignatures|Signatures]], [[DSPyModules|Modules]], [[DSPyAdapters|Adapters]], [[DSPyLM|LM]] bindings, [[DSPyOptimizers|Optimizer]]-refined instructions/demos — without changing the [[DSPyProgrammingModel|four-concerns decomposition]].

The two modes are selected by the `save_program` flag on `Module.save(...)`:

| Mode | Flag | Format | Architecture | Recovery | Min version |
|---|---|---|---|---|---|
| **State-only** | `save_program=False` | `.json` (default) or `.pkl` | **Reconstructed in code** before load | `loaded = MyProgram(); loaded.load(path)` | All |
| **Whole-program** | `save_program=True` | Directory ([[Cloudpickle|cloudpickle]]) | **Embedded in the artifact** | `loaded = dspy.load(path)` | `dspy>=2.6.0` |

## State-only mode

State-only mode persists *only* the program's mutable parameters — *"the signature, demos (few-shot examples), and other information"* plus configurable module attributes. The architecture (the `dspy.Module` subclass, its sub-Modules, its `forward(...)` logic) is **not** saved — it must be reconstructed in code at load time. The result is the lightweight, [[DSPyOptimizers|Optimizer]]-friendly persistence path that every prior wiki receipt of `optimized_program.save(path)` exercises by default.

### JSON sub-format (default)

```python
compiled_dspy_program.save("./dspy_program/program.json", save_program=False)
```

The artifact is **plain-text JSON** the developer can `cat` to see the optimizer-chosen instructions and demonstrations — the **inspectability commitment** the [[DSPyOptimizers|Optimizers page]] anchors. *"A developer can `cat` it and see exactly which instructions and demonstrations the optimizer chose. This is consistent with DSPy's writing code instead of strings discipline."*

JSON is the safer default but **cannot serialize non-JSON-native types** — including:

- [[DSPyImage|`dspy.Image`]] (multi-modal Signature input/output)
- `datetime.datetime` objects
- Any custom Python object without a built-in JSON encoder

If the program's [[DSPyExample|`Example`]]s or attributes carry such types, the JSON path silently fails or drops fields; the pickle sub-format is the documented fallback.

### Pickle sub-format

```python
compiled_dspy_program.save("./dspy_program/program.pkl", save_program=False)
```

Pickle handles arbitrary Python objects (covering [[DSPyImage|`dspy.Image`]], datetimes, custom classes) at the cost of the standard **arbitrary-code-execution security risk** on load:

> *"Loading `.pkl` files can execute arbitrary code and may be dangerous. Only load pickle files from trusted sources in secure environments."*

The framework's response is the explicit-acknowledgement gate `allow_pickle=True` on `.load(...)`:

```python
loaded_program.load("./dspy_program/program.pkl", allow_pickle=True)
```

Without the flag, pickle loads are refused. This is the **save/load-side analog** of the [[DSPyCache|caching layer's]] `restrict_pickle=True` allowlist-deserializer — same threat (tampered pickle file → arbitrary code execution), different mitigation (explicit user flag vs allowlist-based deserialization).

### Load is two-step

State-only mode requires the architecture to be reconstructed *before* loading:

```python
loaded_program = dspy.ChainOfThought("question -> answer")
loaded_program.load("./dspy_program/program.json")
```

The reconstructed instance must match the saved program's structure (Signature, sub-Module composition) for the load to succeed. Mismatches surface as `KeyError`s or silent state-mismatch bugs.

### Demos round-trip as `dict`, not `dspy.Example`

A subtle type asymmetry on the load path: **loaded demos arrive as plain Python `dict`s, not [[DSPyExample|`dspy.Example`]] objects**. Code that consumes the loaded program's demos via `.with_inputs(...)` / `.inputs()` / `.labels()` ([[DSPyExample|the `dspy.Example` API]]) must accommodate the dict form — convert via `[dspy.Example(**d).with_inputs(...) for d in loaded.demos]` if those methods are needed.

This is **not a bug** — it follows from JSON serialization round-tripping the demos through `dict` shape; pickle-mode and whole-program-mode preserve `dspy.Example` identity.

## Whole-program mode

Whole-program mode (added in `dspy>=2.6.0`) serializes **architecture and state together** via [[Cloudpickle|`cloudpickle`]] into a **directory** (not a single file):

```python
compiled_dspy_program.save("./dspy_program/", save_program=True)
```

The directory also carries **dependency-version metadata** — recording the DSPy version the artifact was written against, the load-side BC-check anchor for the future-3.0.0+ BC story.

Recovery is one line, no reconstruction:

```python
loaded_dspy_program = dspy.load("./dspy_program/")
```

The top-level `dspy.load(...)` is **only valid for whole-program-mode artifacts** — the state-only path stays on `Module.load(...)` after reconstructing the architecture.

### Custom-module by-value serialization

For programs built on user-defined module classes (e.g., a `class MyRAG(dspy.Module)` with custom `forward(...)`), whole-program mode by default serializes the class **by reference** — the load-side import path must match the save-side import path, or load fails.

The `modules_to_serialize=[...]` opt-in changes this to **by-value serialization**:

```python
compiled_dspy_program.save(
    "./dspy_program/",
    save_program=True,
    modules_to_serialize=[my_custom_module],
)
```

Under the hood this calls `cloudpickle.register_pickle_by_value(...)` on each entry — the **class definitions travel with the artifact**, independent of the load-side import environment. This is the canonical pattern for shipping a DSPy program to a deployment target that does not have the saving-side code installed.

## Persistence-path decision tree

| Need | Path |
|---|---|
| Standard optimizer save/load; want JSON inspectability | State-only, JSON (default — every prior wiki receipt) |
| Program has [[DSPyImage|`dspy.Image`]] or datetime fields; want JSON otherwise | State-only, pickle (`.pkl` + `allow_pickle=True` on load) |
| Want one-line load with no architecture reconstruction | Whole-program, JSON-free `dspy.load(...)` |
| Shipping a custom-Module program to a fresh deployment | Whole-program + `modules_to_serialize=[...]` |
| Need provenance + experiment-tracking context with the artifact | [[MLflow|`mlflow.dspy.log_model(...)`]] wrapping state-only save — see [[dspy-optimizer-tracking-tutorial]] |
| Production REST serving with versioning | [[MLflow|`mlflow.dspy.log_model(...)`]] + `mlflow models serve` — see [[dspy-deployment-tutorial]] |

## Backward-compatibility posture

The tutorial commits the framework to an explicit pre-3.0.0 **non-guarantee**:

> *"Current versions (pre-3.0.0) offer no guarantee of backward compatibility across DSPy versions. Load saved programs using the same version they were created with for consistent performance."*

The 3.0.0+ commitment is:

> *"Future releases (3.0.0+) will guarantee backward compatibility within major versions."*

This is the **first DSPy receipt** in the wiki corpus that explicitly disavows cross-version artifact loading. Operational implications:

- **Pin the DSPy version** in production deployments — re-loading a saved artifact under a different version is unsupported until 3.0.0.
- **Re-run the [[DSPyOptimizers|Optimizer]]** when upgrading DSPy versions in the pre-3.0.0 line — the alternative (load + accept silent behavior drift) is the framework's explicit warning.
- **Whole-program mode's dependency-version metadata** is the load-side BC-check anchor — the artifact records the version it was written against, so a future BC-check can refuse loads with a mismatched version rather than silently degrade.

## Position in the wiki's DSPy landscape

- **vs [[DSPyOptimizers]] (the catalog that already exercises `save(...)`).** The Optimizers catalog page documents the *inspectability commitment* — `optimized_program.save(YOUR_SAVE_PATH)` → plain-text JSON, *"writing code instead of strings"*. **This page** completes that by adding the pickle and whole-program modes the catalog defers, plus the security and BC fine print. The split mirrors [[DSPyEvaluation]] / [[DSPyMetrics]] — one page anchors the discipline-level commitment, the sibling anchors the per-mechanism machinery.

- **vs [[DSPyCache]] (the sibling-axis production-shape concept).** Caching and saving are both production-shape surfaces orthogonal to the [[DSPyProgrammingModel|four-concerns decomposition]]. Both have to negotiate pickle's arbitrary-code-execution risk — Cache chose an **allowlist-based deserializer** (`restrict_pickle=True` + `safe_types=[...]`); Saving chose an **explicit user flag** (`allow_pickle=True`). Both endorse JSON as the safer default.

- **vs [[MLflow]] (the experiment-tracking persistence carrier).** The [[dspy-optimizer-tracking-tutorial|Optimizer Tracking tutorial]]'s `mlflow.dspy.log_model(...)` and the [[dspy-deployment-tutorial|Deployment tutorial]]'s `mlflow models serve` rest on the primitives documented here — MLflow is the provenance-bearing carrier, the actual round-trip is still `save(...)` / `load(...)`. The two persistence paths coexist as *plain-file* (this page) and *provenance-bearing* (MLflow).

- **vs [[DSPyOptimization]] (the workflow-level anchor).** Optimization's workflow contract — *three inputs (program + metric + training set) → one output (optimized program)* — terminates at an in-memory `optimized_program` object; **this page** is what gives that output a durable life beyond the Python process that produced it.

- **vs [[DSPyAsync]] / [[DSPyStreaming]] / [[DSPyObservability]] / [[DSPyCache]] (the four-axis production-shape sibling cluster).** Five orthogonal production-shape surfaces — async dispatch, token streaming, observability instrumentation, multi-layer caching, on-disk persistence — all sit *outside* the four Programming-Model concerns and compose uniformly across every [[DSPyModules|Module]].

## Operational subtleties

1. **JSON vs pickle is a per-call choice**, not a framework-wide setting. The same program can be saved twice — once to JSON for inspectability + once to pickle for fidelity — without configuration changes.

2. **Whole-program mode pickles the bound LM reference.** If the save-side process was configured with `dspy.configure(lm=dspy.LM('openai/gpt-4o-mini', api_key=...))`, the load-side artifact carries a serialized LM reference. The load-side environment must have the credentials (or reconfigure the LM after load) for invocation to succeed.

3. **`modules_to_serialize` does not chain transitively.** If a custom module imports another custom module, both must be listed explicitly — the tutorial does not call this out but it follows from `cloudpickle.register_pickle_by_value` being per-class.

4. **State-only `.json` is the only inspectable mode.** Pickle (state-only) and cloudpickle (whole-program) artifacts are opaque binaries — the *"cat it to read the prompt"* discipline from the [[DSPyOptimizers]] page only applies to the JSON path. Choose accordingly when the artifact will need human inspection.

5. **Demo type asymmetry is JSON-mode-specific.** Pickle-mode state-only loads preserve [[DSPyExample|`dspy.Example`]] identity (pickle round-trips Python types); whole-program-mode loads preserve everything. Only JSON state-only mode flattens demos to `dict`.

## Tutorials

Tutorials that exercise this concept (roughly increasing depth):

- [[dspy-saving-tutorial]] — canonical receipt of the two-mode persistence surface: state-only (JSON default + pickle fallback with `allow_pickle=True` gate) vs whole-program (`save_program=True`, `dspy>=2.6.0`, [[Cloudpickle|cloudpickle]] directory + dependency-version metadata).
- [[dspy-tool-use-tutorial]] — `compiled_program.save(path)` round-trip of a `dspy.SIMBA`-optimized ToolHop program; demonstrates the JSON state-only path on a tool-using agent.
- [[dspy-multihop-search-tutorial]] — `optimized.save(path)` of a `dspy.MIPROv2`-compiled [[HoVer]] multi-hop program; demonstrates persistence as the natural terminus of the three-stage optimization loop.
- [[dspy-tutorial-gepa-aime]] — `program.save(path)` of a `dspy.GEPA`-compiled AIME math program; the GEPA-output artifact carries reflection-derived instructions inspectable via the JSON path.
- [[dspy-rl-multihop-tutorial]] — persistence of an `ArborGRPO`-optimized program with [[lora|LoRA]] adapter weights; the most advanced save case in the corpus, where the optimizer's output is **not pure JSON** (weight references on the LM side) and the [[BootstrapFinetune]]-style exception applies.

## See also

- [[dspy-saving-tutorial]] — canonical source
- [[DSPyOptimizers]] — the catalog whose every receipt exercises this surface
- [[DSPyOptimization]] — the workflow that produces save-worthy programs
- [[DSPyCache]] — sibling-axis production-shape concept with related pickle-safety pattern
- [[MLflow]] — provenance-bearing persistence carrier
- [[BackwardCompatibility]] — general concept the pre-3.0.0 / 3.0.0+ split operationalizes
- [[Cloudpickle]] — whole-program mode's underlying serializer
- [[Pickle]] — state-only pickle sub-format's underlying serializer
