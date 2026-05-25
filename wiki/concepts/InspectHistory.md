---
title: "InspectHistory"
type: concept
tags: [dspy, observability, debugging, utility]
sources: [dspy-observability-tutorial, dspy-conversation-history]
last_updated: 2026-05-24
---

# `dspy.inspect_history(n=N)`

The **tier-1** [[DSPyObservability|observability]] surface in [[DSPy]] — a zero-dependency print utility that dumps the **last *N* LM calls** the process has made. Defined at the top-level `dspy` namespace; no setup, no install, no configuration.

## Signature

```python
dspy.inspect_history(n=N)
```

- **`n`** — how many recent LM calls to print. The [[dspy-observability-tutorial|tutorial]] uses `n=2`; the [[dspy-conversation-history|conversation-history tutorial]] uses the no-arg form (`dspy.inspect_history()`) to dump everything.
- **No return value** — prints to stdout.

## What it captures

Per the [[dspy-observability-tutorial|tutorial]]: *"all LLM invocations made so far"* — the prompt sent to the LM and the response received, for each of the last *N* calls.

The output is **a flat chronological list of LM calls**. It is the rawest possible window into what the framework actually sent over the wire.

## Three documented limitations

The [[dspy-observability-tutorial|tutorial]] explicitly enumerates three limitations that motivate the upgrade to [[MLflow]] autolog (tier 2):

1. *"It only captures **LM calls**, not other component activity"* — no [[DSPyTools|tool]] invocations, no retriever calls, no [[DSPyAdapters|adapter]] events.
2. *"It does not provide **metadata** like latency, module relationships, etc."* — no timing, no parent/child structure, no module names.
3. *"In **complex applications**, multiple predictions are nested, making it difficult to organize them in the order they were made"* — interleaved nested calls become ambiguous in a flat list.

The same three properties are exactly what tier 2 ([[MLflow]] autolog) and tier 3 ([[DSPyCallback|`BaseCallback`]]) add.

## Why keep it in the framework

Despite the limitations, `inspect_history` survives because it is **zero-friction**:

- **No install** — built into the `dspy` namespace.
- **No server** — prints to stdout in the same process.
- **No code change** — drop it anywhere as a debug print.
- **Faithful to the wire** — shows exactly the prompt-as-rendered, not a structured-output abstraction.

For interactive notebook debugging during the **programming stage** (before any optimization or production deployment), this is often enough. The tutorial corpus uses it that way: end-of-cell sanity check, then move on.

## Relation to other DSPy history surfaces

- **[[DSPyLM|`dspy.LM.history`]]** — per-`dspy.LM`-instance wire-level log. Different layer — `inspect_history` is a **process-wide** global recent-call buffer; `lm.history` is **per-client**. Used by [[DSPyOptimizers|Optimizers]] for replay.
- **[[DSPyHistory|`dspy.History`]]** — [[DSPySignatures|Signature]] field type for *conversation* history. Unrelated despite the shared word — `dspy.History` conditions the model on prior turns; `inspect_history` inspects what the framework sent.
- **[[react|`dspy.ReAct`]] `trajectory`** — intra-call think-act-observe log. Orthogonal — `trajectory` is a **field** on the [[DSPyPrediction|Prediction]], `inspect_history` is a **function** on the framework.

## Canonical usage receipts

```python
# Tutorial-quoted form
dspy.inspect_history(n=2)
```

```python
# Conversation-history tutorial — end-of-loop dump
while True:
    ...
dspy.inspect_history()
```

## Tracked sources

- **[[dspy-observability-tutorial]]** (2026-05-24) — canonical definition and the three documented limitations.
- **[[dspy-conversation-history]]** (2026-05-22) — supplementary usage receipt (no-arg call at end of chatbot loop).
