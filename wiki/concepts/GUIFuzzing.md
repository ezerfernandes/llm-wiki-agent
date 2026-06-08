---
title: "GUI Fuzzing"
type: concept
tags: [fuzzing, testing, security, gui, ui, selenium, model-based-testing, web, python]
sources: [fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# GUI Fuzzing

**GUI fuzzing** (a.k.a. **GUI testing** / automated UI testing) is the testing of a program *through its graphical user interface* by automatically discovering its interactive elements (text fields, checkboxes, buttons, links) and generating sequences of user actions (fill, check, submit, click) that drive the application through its states. Unlike [[WebApplicationFuzzing|Web-application fuzzing]], which speaks HTTP and parses served HTML, GUI fuzzing drives a *real* UI runtime — in practice a real browser — so it works even when JavaScript generates and mutates the interface client-side, and the same approach generalizes to mobile and desktop apps.

## From The Fuzzing Book — Testing Graphical User Interfaces
[[fuzzingbook-28-gui-fuzzer|Ch 28]] generalizes the HTML form-fuzzing of [[fuzzingbook-27-web-fuzzer|Ch 27]] into a generic UI technique built on the [[Selenium]] [[WebDriver|WebDriver]] framework. Instead of accessing HTML source, it assumes only that there is a set of *user interface elements* it can query and activate. The approach has three moving parts:

1. **Discover** — a [[GrammarMiner|`GUIGrammarMiner`]] queries the live page for its interactive elements and the actions they support (`fill`/`check`/`submit`/`click`), staying on the current host.
2. **Model** — the UI is modeled as a [[FiniteStateMachine|finite state machine]] of pages (a [[UINavigationModel|UI navigation model]]), where each *state is identified by its set of interactive elements* (not its URL — JavaScript can keep the URL fixed while changing the page). That FSM is **embedded into a [[Grammar|grammar]]** so one structure produces both form values and navigation sequences ([[ModelBasedTesting|model-based testing]]).
3. **Explore & cover** — [[GUIFuzzer|`GUIFuzzer`]] grows the grammar at runtime as it reaches new states (generation and exploration happen together), and `GUICoverageFuzzer` (a [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] subclass) covers every state transition because each transition is a grammar expansion.

The chapter demonstrates "deep" exploration (filling forms to reach the states behind them) on the [[fuzzingbook-27-web-fuzzer|Ch 27]] vulnerable shop server and even on the live fuzzingbook.org site. It is explicitly experimental — supporting only a subset of HTML form/link features and not handling JavaScript itself. The Background traces the field to GUI coverage criteria and *GUI Ripping* (Memon 2001/2003), CrawlJax (Mesbah 2012), and the Alex automata-learning framework.

## Connections
- [[GUIFuzzer]] — the concrete `GUIFuzzer`/`GUICoverageFuzzer`/`GUIRunner`/`GUIGrammarMiner` toolkit that realizes this technique.
- [[UINavigationModel]] — the FSM-of-pages model mined during exploration.
- [[ModelBasedTesting]] — the FSM-in-a-grammar generation strategy.
- [[Selenium]] / [[WebDriver]] — the browser-automation layer that activates UI elements.
- [[FiniteStateMachine]] — the underlying model of states and transitions.
- [[WebApplicationFuzzing]] / [[WebFormFuzzer]] — the HTTP/HTML predecessor this generalizes past JavaScript.
- [[WebCrawling]] — exploring a whole site by following links, here through a browser.
- [[GrammarMining]] / [[GrammarMiner]] — mining a grammar from a *live UI*.
- [[GrammarCoverageFuzzer]] / [[GrammarCoverage]] — transition coverage achieved via grammar coverage.
- [[Fuzzing]] — the parent discipline.
- [[fuzzingbook-28-gui-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces."
