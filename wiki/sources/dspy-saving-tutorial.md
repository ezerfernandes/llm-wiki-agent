---
title: "DSPy Tutorial — Saving and Loading Programs"
type: source
tags: [dspy, tutorial, persistence, serialization, deployment, security]
date: 2026-05-24
source_file: raw/dspy-saving-tutorial.md
---

## Summary

Official [[DSPy]] tutorial at `https://dspy.ai/tutorials/saving/` documenting the framework's two-mode program-persistence surface — **state-only saving** (lightweight; reconstruct architecture in code, then `program.load(path)`) and **whole-program saving** (DSPy 2.6.0+; `cloudpickle` writes architecture + state into a directory, recovered by the top-level `dspy.load(path)`). State-only mode offers JSON (safe + human-readable; default) and pickle (covers non-serializable objects like [[DSPyImage|`dspy.Image`]] and datetimes) sub-formats; whole-program mode is directory-shaped (not single-file) and persists dependency-version metadata. `modules_to_serialize=[...]` opt-in registers user-defined custom modules via `cloudpickle.register_pickle_by_value` for **by-value serialization** (dependencies travel with the artifact instead of being import-resolved at load time). Backward compatibility is **not guaranteed** in the pre-3.0.0 line; 3.0.0+ commits to backward compatibility within major versions. Pickle loading carries the standard arbitrary-code-execution security warning — `allow_pickle=True` is the explicit acknowledgement gate on state-only `.pkl` loads.

## Key Claims

- **Two persistence modes**, selected by the `save_program` flag on [[DSPyModules|`Module`]]`.save(...)`:
  - **State-only** (`save_program=False`): writes signature, [[FewShotLearning|demos]], and configurable module attributes; architecture must be reconstructed in code before `.load(...)`.
  - **Whole-program** (`save_program=True`): writes architecture + state via `cloudpickle`; recovered by `dspy.load(path)` with no reconstruction step.
- **State-only sub-formats** are chosen by file extension: `.json` (default; safer + human-readable; **cannot serialize** [[DSPyImage|`dspy.Image`]] or datetimes) and `.pkl` (pickle; covers non-serializable objects).
- **State-only load is two steps**: recreate the architecture (`dspy.ChainOfThought("question -> answer")` etc.) → `loaded_program.load(path)`.
- **Loaded demos arrive as plain `dict`s** under state-only mode, **not** [[DSPyExample|`dspy.Example`]] objects — type asymmetry the user must accommodate.
- **`.pkl` loads require explicit `allow_pickle=True`** — the framework's acknowledge-the-risk gate against arbitrary-code-execution attacks via tampered pickle files. *"Loading `.pkl` files can execute arbitrary code and may be dangerous. Only load pickle files from trusted sources in secure environments."*
- **Whole-program mode requires DSPy ≥ 2.6.0**; serialization uses `cloudpickle`; the save target is a **directory** (not a single file).
- **Whole-program save persists dependency-version metadata** alongside the program — supports the [[BackwardCompatibility|backward-compatibility]] story below by recording the version the artifact was written against.
- **Custom-module support**: `save(..., save_program=True, modules_to_serialize=[my_custom_module])` invokes `cloudpickle.register_pickle_by_value(...)` so user-defined modules are pickled **by value** rather than by reference; without this opt-in, the load-side import path must match the save-side import path.
- **Backward compatibility is not guaranteed in pre-3.0.0**: *"Current versions (pre-3.0.0) offer no guarantee of backward compatibility across DSPy versions. Load saved programs using the same version they were created with for consistent performance."* 3.0.0+ will guarantee BC within major versions.

## Key Quotes

> "State represents the DSPy program's internal state, including the signature, demos (few-shot examples), and other information." — state-only section

> "Starting from `dspy>=2.6.0`, DSPy supports saving the whole program, including the architecture and the state." — whole-program section

> "Loading `.pkl` files can execute arbitrary code and may be dangerous. Only load pickle files from trusted sources in secure environments." — security warning

> "Current versions (pre-3.0.0) offer no guarantee of backward compatibility across DSPy versions. Load saved programs using the same version they were created with for consistent performance." — backward-compatibility note

## Connections

- [[DSPySaving]] — primary concept page distilled from this tutorial (state-only vs whole-program decision tree, security posture, BC contract).
- [[DSPyModules]] — `Module.save(...)` / `Module.load(...)` are the per-instance entry points; `dspy.load(...)` is the top-level whole-program recovery entry point.
- [[DSPyOptimizers]] — the canonical save/load consumer: every prior wiki receipt of `optimized_program.save(YOUR_SAVE_PATH)` (math 74→88.57, NER 86→93, RAG-QA 55.5→61.1, HoVer 8→41.67, Banking77 66→87) is operationalized by this tutorial; this tutorial supplies the *whole-program* alternative and the security/BC fine print the catalog page deferred.
- [[DSPyOptimization]] — produces optimized programs whose persistence policy is the subject of this tutorial; closes the loop on the *"optimized program is a refined version of the same program"* commitment (the optimized artifact is JSON-inspectable by default).
- [[DSPyExample]] — state-only loads materialize demos as `dict`s rather than `dspy.Example` objects (type asymmetry on the load path).
- [[DSPyImage]] — explicitly named as a non-JSON-serializable type that forces the pickle fallback or the whole-program path.
- [[DSPyPredict]] / [[ChainOfThought|`dspy.ChainOfThought`]] — the canonical reconstruction targets in the state-only load example.
- [[Pickle]] / [[Cloudpickle]] — the underlying serialization libraries; `cloudpickle.register_pickle_by_value` is the by-value-serialization primitive that `modules_to_serialize` exposes.
- [[MLflow]] — the [[dspy-optimizer-tracking-tutorial|Optimizer Tracking tutorial]]'s `mlflow.dspy.log_model(...)` + `program.load(model_path)` round-trip is a **tracking-server-backed alternative** to the plain `.save(...)` / `.load(...)` recipe documented here; the two coexist as *plain-file* vs *provenance-bearing* persistence paths.
- [[dspy-deployment-tutorial]] — the Deployment tutorial's MLflow-serving path also rests on this save/load primitive (`mlflow.dspy.log_model(...)` wraps it).
- [[dspy-cache-tutorial]] — sibling-axis tutorial; both canonicalize production-shape surfaces (caching / persistence) orthogonal to the [[DSPyProgrammingModel|four-concerns decomposition]]. Cache's `restrict_pickle=True` is the cache-side analog of this tutorial's `allow_pickle=True` — both gate untrusted-pickle ingestion, with cache opting for an allowlist-deserializer and save/load opting for an explicit-flag-on-load.
- [[dspy-async-tutorial]] / [[dspy-streaming-tutorial]] / [[dspy-observability-tutorial]] — the four-axis production-shape sibling tutorial cluster (async / streaming / observability / persistence).
- [[Pydantic]] — relevant to whole-program mode where Pydantic-typed Signature I/O survives the cloudpickle round-trip; the state-only JSON path serializes Pydantic-typed demos as `dict`s.
- [[BackwardCompatibility]] — the pre-3.0.0 *"no guarantee"* posture is the wiki's first DSPy receipt that explicitly disavows cross-version artifact loading.

## Contradictions

- **None identified** against existing wiki content. The tutorial extends every prior DSPy ingest along an orthogonal *persistence* axis.
- **Reconciliations**:
  - The [[DSPyOptimizers|Optimizers catalog page]] documents the JSON-default plain-text persistence surface (`optimized_program.save(path)` → JSON the developer can `cat`); this tutorial **completes** that by adding the pickle and whole-program modes and the security/BC fine print, without contradicting the *"plain-text JSON inspectability"* claim — JSON remains the default, the other modes are opt-ins.
  - The [[dspy-cache-tutorial|Caching tutorial's]] `restrict_pickle=True` allowlist-deserializer (defense-in-depth against arbitrary-code-execution from tampered cache files) and this tutorial's `allow_pickle=True` (acknowledge-the-risk gate on state-only `.pkl` loads) are **complementary** pickle-safety patterns — the cache layer opts for an allowlist, the save/load layer opts for an explicit user flag. Both endorse JSON as the default for the same reason.
  - The [[dspy-optimizer-tracking-tutorial|Optimizer Tracking tutorial's]] [[MLflow]] artifact path (`mlflow.dspy.log_model(...)` → `mlflow.artifacts.download_artifacts(...)` → `program.load(model_path)`) **wraps** this tutorial's primitives — MLflow is the provenance-bearing carrier, the actual round-trip is still `save/load`.

## Scope-limit gaps

- No **on-disk artifact size** comparison between JSON / pickle / whole-program modes.
- No **performance** comparison (save/load latency for the three modes).
- No **threat model** for the security warning beyond "tampered files" — no guidance on safe deserialization (e.g., the cache layer's `restrict_pickle` allowlist pattern is **not** mentioned here even though it could apply by analogy).
- No **migration recipe** for the 2.x → 3.x BC boundary — the page commits to *"no guarantee"* but does not specify how to re-export a 2.x artifact for 3.x consumption.
- No **`modules_to_serialize=` transitive-dependency** guidance — if a custom module imports another custom module, must both be registered? The example shows one entry only.
- No **diff between JSON state-only and whole-program** for the *demos-as-dict-vs-Example* asymmetry — does whole-program preserve `dspy.Example` identity? Implied yes (cloudpickle preserves class identity) but not stated.
- No **versioning policy for `modules_to_serialize` entries** — if a custom module's class definition changes between save and load, what happens? `cloudpickle.register_pickle_by_value` serializes the class definition by value, so the load-side imported class is ignored; this matters for production deployments but is not called out.
- No **size limit** on the whole-program directory; no **multi-LM** save/load example (the whole-program mode pickles the bound LM reference — what if the LM is configured via `dspy.configure(lm=...)` at load time on a different machine?).
- No **streaming-friendly persistence path** (`dspy.streamify(...)`-wrapped programs — does whole-program mode round-trip the streamify wrapper? Unclear).
- No **JSON schema** for the state-only format — the *"cat it to inspect"* discipline from the [[DSPyOptimizers]] page is preserved but undocumented field-by-field.
