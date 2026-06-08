---
title: "UI Navigation Model"
type: concept
tags: [testing, fuzzing, gui, ui, finite-state-machine, model-based-testing, grammar]
sources: [fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# UI Navigation Model

A **UI navigation model** is an abstract model of a user interface as a graph (a [[FiniteStateMachine|finite state machine]]) of *pages/screens* (states) connected by *user actions* (transitions). It captures how a user moves through an application — which interactions are available on each screen and which screen each interaction leads to — so that a tester or fuzzer can systematically explore the whole UI and cover its states and transitions. It is the central artifact of [[ModelBasedTesting|model-based testing]] applied to GUIs.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] mines a UI navigation model of a Web application by exploration with [[Selenium]] ([[GUIFuzzing|GUI fuzzing]]). Two design choices define the model:

- **State identity** — a state is identified by *the set of interactive elements (actions) the page offers*, **not** by its URL. This matters because JavaScript can change a page's contents while leaving its URL unchanged, and non-Web UIs may have no URLs at all; "the way a UI can be interacted with uniquely defines its state."
- **Transitions** — each `click()`/`submit()` action that leaves the current page is a transition to a (possibly new) state. The model starts with reachable states marked `<unexplored>` and is filled in as exploration reaches them; an `<end>` state lets the action stream terminate.

The model is represented as an FSM **embedded in a [[Grammar|grammar]]** (each state → a grammar symbol, each transition → a grammar alternative), letting one structure encode states *and* form values. [[GUIFuzzer|`GUIFuzzer`]] mines this model incrementally — every time it reaches a previously unseen state it mines that state's actions and merges a sub-grammar in, and when it lands in an already-seen state it merges the two via `replace_symbol()`. `fsm_diagram()` visualizes the resulting model; on the chapter's shop server it collapses to `<Order Form>`, `<Terms and Conditions>`, and `<Thank You>` states, and on a large site (fuzzingbook.org) it grows toward roughly one state per page/chapter.

## Connections
- [[FiniteStateMachine]] — the formal structure of the navigation model (states + transitions).
- [[ModelBasedTesting]] — the testing strategy that consumes this model.
- [[GUIFuzzing]] / [[GUIFuzzer]] — the technique/tool that mines and traverses it.
- [[Selenium]] / [[WebDriver]] — the framework used to query elements and follow transitions.
- [[Grammar]] — the representation the model is embedded into.
- [[GrammarMining]] / [[GrammarMiner]] — the model is mined as a grammar from the live UI.
- [[WebCrawling]] — exploring a site by following navigation transitions.
- [[fuzzingbook-28-gui-fuzzer]] — the chapter that builds it.

## Sources
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces."
