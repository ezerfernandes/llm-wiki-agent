---
title: "Model-Based Testing"
type: concept
tags: [testing, fuzzing, model-based-testing, finite-state-machine, grammar, gui]
sources: [fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# Model-Based Testing

**Model-based testing** derives tests from an explicit *model* of the system's expected behavior — typically a [[FiniteStateMachine|finite state machine]], grammar, or other abstract structure — rather than from hand-written test cases. The model captures the legal states the system can be in and the transitions (events/actions) between them; a test generator then traverses the model to produce input/interaction sequences, and coverage of the model (e.g. visiting every state or every transition) becomes the testing adequacy criterion.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] is a worked instance of model-based testing applied to graphical user interfaces ([[GUIFuzzing|GUI fuzzing]]). The model is a [[UINavigationModel|UI navigation model]] — a [[FiniteStateMachine|finite state machine]] whose states are pages (identified by their set of interactive elements) and whose transitions are user actions (`fill`/`check`/`submit`/`click`). The chapter's key trick is to **embed the FSM into a [[Grammar|grammar]]**:

- every FSM *state* `<s>` becomes a grammar *symbol* `<s>`;
- every *transition* from `<s>` to `<t>` with actions `a₁ a₂ …` becomes an *alternative* `a₁ a₂ … <t>` of `<s>`.

This unifies two generation tasks under one structure — producing text for form fields *and* producing navigation sequences — so a single [[GrammarFuzzer|grammar fuzzer]] generates complete test scenarios. Crucially, because each transition is a grammar expansion, ordinary [[GrammarCoverage|grammar coverage]] (via [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]) *is* FSM transition coverage — model coverage falls out of grammar coverage with no special machinery. The model is also *mined while it is traversed* ([[GUIFuzzer|`GUIFuzzer`]] grows the grammar each time it reaches a new state), so model construction and test generation are interleaved rather than sequential.

## Connections
- [[FiniteStateMachine]] — the model structure most commonly used (and the one Ch 28 embeds in a grammar).
- [[UINavigationModel]] — the concrete model Ch 28 builds for a UI.
- [[GUIFuzzing]] / [[GUIFuzzer]] — the GUI application of model-based testing.
- [[Grammar]] — the representation into which the FSM model is embedded.
- [[GrammarCoverage]] / [[GrammarCoverageFuzzer]] — model (transition) coverage realized as grammar coverage.
- [[Testing]] / [[Fuzzing]] — the broader disciplines.
- [[fuzzingbook-28-gui-fuzzer]] — the chapter that applies it to GUIs.

## Sources
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces."
