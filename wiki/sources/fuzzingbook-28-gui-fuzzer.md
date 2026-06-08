---
title: "The Fuzzing Book Ch 28 — Testing Graphical User Interfaces"
type: source
tags: [book, fuzzingbook, fuzzing, testing, security, gui, web, selenium, model-based-testing, finite-state-machine, grammar-mining]
date: 2026-06-06
source_file: raw/books/fuzzingbook/fuzzingbook-28-gui-fuzzer.md
book: "The Fuzzing Book"
book_authors: ["Andreas Zeller", "Rahul Gopinath", "Marcel Böhme", "Gordon Fraser", "Christian Holler"]
book_publisher: "CISPA Helmholtz Center for Information Security"
book_year: 2024
book_url: "https://www.fuzzingbook.org/"
---

# Testing Graphical User Interfaces

## Summary
Chapter 28 generalizes the HTTP/HTML approach of [[fuzzingbook-27-web-fuzzer|Ch 27]] from raw Web requests to *arbitrary graphical user interfaces* ([[GUIFuzzing|GUI fuzzing]]), driven through a **real browser** with the [[Selenium]] [[WebDriver|WebDriver]] framework. Rather than parsing served HTML, it *queries the running UI* for its interactive elements (text fields, checkboxes, buttons, links) and the actions they support — so the technique survives JavaScript and even generalizes to mobile apps. Its central idea is to **model the UI as a [[FiniteStateMachine|finite state machine]] of pages** ([[UINavigationModel|UI navigation model]]) where each *state* is identified by its set of interactive elements, then **embed that FSM inside a [[Grammar|grammar]]** so that one structure simultaneously generates form values *and* navigation action sequences ([[ModelBasedTesting|model-based testing]]). The chapter builds this incrementally — `GUIGrammarMiner` (discover actions/states), `GUIRunner` (execute action strings via Selenium), [[GUIFuzzer|`GUIFuzzer`]] (explore states and grow the grammar on the fly), and finally `GUICoverageFuzzer` — which, by inheriting from [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]), covers every state transition because each transition is a grammar expansion. It reuses the [[fuzzingbook-27-web-fuzzer|Ch 27]] vulnerable shop server as its running example and is the last chapter of Part V (Domain-Specific Fuzzing), leading into [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]].

## Key Concepts
- **Driving a real browser with [[Selenium]]** — `start_webdriver(browser, headless, zoom)` launches a *headless* Firefox (`geckodriver`) or Chrome ([[ChromeDriver|`chromedriver`]]) and returns a *GUI driver* (a Selenium `webdriver`). The driver navigates (`get(url)`, `back()`), takes screenshots (`get_screenshot_as_png()`), queries elements (`find_element(By.NAME, ...)`, `find_elements(By.TAG_NAME, "a")`), reads attributes (`get_attribute('href')`), and interacts (`send_keys()`, `click()`). This is the *UI testing framework* layer: query the program for available UI elements and how they can be activated — independent of HTTP/HTML.
- **Selenium test cases** — the manual baseline: a `test_successful_order(driver, url)` fills the form field-by-field, submits, then asserts on the confirmation page's `title`/`confirmation` text — a classic [[Selenium]] regression test. The chapter notes writing these by hand is laborious, motivating automatic generation.
- **UI actions** — a small action vocabulary the fuzzer emits as executable Python strings: `fill(<name>, <text>)`, `check(<name>, <bool>)`, `submit(<name>)`, `click(<name>)`, plus `ignore(<name>)` for off-host links (kept only to characterize a state, never executed).
- **`GUIGrammarMiner`** — the [[GrammarMiner|grammar miner]] for UIs. `mine_state_actions()` returns a `frozenset` of all actions on the *current* page by merging `mine_input_element_actions()` (text→`fill`, checkbox/radio→`check`, submit→`submit`), `mine_button_element_actions()`, and `mine_a_element_actions()` (links, with `follow_link()` keeping exploration on the same host). `mine_state_grammar()` then turns those actions into a [[Grammar|grammar]]: form fields/submit collapse into one form-submission alternative, each `click()`/`submit()` introduces a fresh *state symbol* marked `<unexplored>`, and a `<end>` final state lets the (otherwise infinite) action stream terminate. A `GUI_GRAMMAR` template supplies value rules per input type (`<text>`, `<number>`, `<email>`, `<boolean>`, `<password>`, …).
- **States identified by interactive elements** — a key departure from [[fuzzingbook-27-web-fuzzer|Ch 27]]: a UI *state* is defined by *the set of interactive elements it offers*, **not** by its URL — because with JavaScript a URL may stay fixed while the page changes, and non-Web UIs may have no URLs at all.
- **FSM ↔ grammar embedding** ([[ModelBasedTesting]]) — every FSM *state* `<s>` becomes a grammar *symbol*; every *transition* from `<s>` to `<t>` with actions `a₁ a₂ …` becomes an *alternative* `a₁ a₂ … <t>` of `<s>`. Expanding the grammar yields navigation sequences; `fsm_diagram()` renders a state grammar back as a Graphviz state machine.
- **`GUIRunner`** ([[Runner|`Runner`]] subclass) — executes an action string on the driver. `run()` uses `exec()` with `__builtins__` set to `{}` and only the four action functions in scope, plus `html.escape()` on all third-party names, to limit (though, per [[fuzzingbook-19-information-flow|Ch 19]], not fully prevent) code injection through UI element names. `find_element()` matches by `By.NAME` then `By.LINK_TEXT`; `do_fill/do_check/do_submit/do_click` defer to Selenium with explicit `WebDriverWait` delays so pages can reload.
- **[[GUIFuzzer|`GUIFuzzer`]]** ([[GrammarFuzzer|`GrammarFuzzer`]] subclass) — explores the UI and *grows its grammar at runtime*: test generation and exploration happen simultaneously. It tracks `state_symbol`, `state` (the action frozenset), and `states_seen` (state→symbol map). `run(runner)` restarts, fuzzes one action sequence, reads the expected last state symbol from the [[DerivationTree|derivation tree]] (`fsm_path()`/`fsm_last_state_symbol()`), executes it, and `update_state()`s — either `update_new_state()` (mine a sub-grammar for the newly reached page and merge it) or `update_existing_state()` (merge the expected state into a previously seen one via `replace_symbol()`).
- **`GUICoverageFuzzer`** — combines `GUIFuzzer`'s `run()` with [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]'s coverage-preferring choices via **multiple inheritance** (resolved with `inheritance_conflicts()` and a custom `__init__`). Its `explore_all(runner, max_actions=100)` keeps running until no `<unexplored>` state remains; because every state transition is a grammar expansion, covering expansions covers transitions ([[GrammarCoverage|grammar coverage]] = [[FiniteStateMachine|FSM]] transition coverage).
- **Scaling and limits** — the fuzzer explores nontrivial real sites (the chapter runs it on fuzzingbook.org). It is explicitly *experimental*: it supports only a subset of HTML form/link features and **does not handle JavaScript**.
- **Background** — GUI test-coverage criteria (Memon 2001) and *GUI Ripping* (Memon 2003), the CrawlJax tool (Mesbah 2012, which also uses the set of interactable elements as a state), and the Alex framework for learning web-app automata.

## Key Claims
- A UI state can be characterized by *the set of interactive elements it offers* rather than by a URL — this is what lets the model handle JavaScript-driven pages and non-Web UIs uniformly.
- Embedding a finite state machine into a grammar unifies two generation problems — producing text for forms and producing interaction sequences for navigation — under a single representation and a single fuzzer.
- Because each FSM transition is a grammar expansion, an off-the-shelf [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]] automatically achieves state-and-transition coverage with no GUI-specific coverage machinery.
- UI exploration and test generation are inseparable: reaching a new state may require generating the right form inputs first, so the model is mined *while* it is being explored, growing the grammar one discovered state at a time.
- Driving a real browser via [[Selenium]] enables "deep" exploration — filling out forms to reach the states behind them — and generalizes from rich Web apps to mobile apps (Selenium has Android variants).
- Running `exec()` on third-party UI element names is dangerous; restricting builtins and escaping strings mitigates but does not eliminate code injection (cross-referencing [[fuzzingbook-19-information-flow|Ch 19]]).

## Key Quotes
> "the way a UI can be interacted with uniquely defines its state." — Retrieving User Interface Actions

> "We can embed the finite state machine into a grammar, which is then used for both states and form values." — State Machines as Grammars

> "Since test generation and user interface exploration take place at the same time" — Exploring User Interfaces

> "Encoding user interface models into a grammar integrates generating text (for forms) and generating user interactions (for navigating)." — Lessons Learned

## Connections
- [[GUIFuzzing]] — the chapter's overarching technique: testing arbitrary GUIs by discovering and activating their elements.
- [[GUIFuzzer]] — the headline class (`GUIFuzzer`/`GUICoverageFuzzer`/`GUIRunner`/`GUIGrammarMiner`).
- [[ModelBasedTesting]] — modeling the UI as an FSM-in-a-grammar and generating tests by traversing it.
- [[UINavigationModel]] — the FSM of pages and the actions/transitions between them that the fuzzer mines.
- [[Selenium]] / [[WebDriver]] — the browser-automation framework that drives the real browser.
- [[ChromeDriver]] — the Chrome WebDriver server (alongside Firefox `geckodriver`).
- [[FiniteStateMachine]] — the model embedded into the grammar; transition coverage is the goal.
- [[GrammarCoverageFuzzer]] — the superclass that makes `GUICoverageFuzzer` cover transitions for free ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]).
- [[GrammarFuzzer]] — `GUIFuzzer`'s superclass; supplies the [[DerivationTree|derivation-tree]] generation engine ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]).
- [[GrammarMiner]] / [[GrammarMining]] — `GUIGrammarMiner` mines a grammar from a *live UI* (a new sense alongside Ch 18/23/25/27).
- [[Grammar]] — the data structure that encodes both states and form values ([[fuzzingbook-09-grammars|Ch 9]]).
- [[Runner]] — `GUIRunner` subclasses the book's harness abstraction to execute action strings.
- [[WebApplicationFuzzing]] / [[WebFormFuzzer]] — the [[fuzzingbook-27-web-fuzzer|Ch 27]] HTTP/HTML approach this chapter generalizes past JavaScript.
- [[WebCrawling]] / [[WebCrawler]] — the chapter explores/crawls a whole site by following links, like Ch 27's crawler but through a browser.
- [[DerivationTree]] — `GUIFuzzer` reads the target state from the tree's last expanded symbol.
- [[AndreasZeller]] / [[CISPA]] — author and publisher.
- [[fuzzingbook-27-web-fuzzer|Ch 27]] — the immediate prerequisite (Web testing) whose server and form-fuzzing this chapter reuses and generalizes.
- [[fuzzingbook-09-grammars|Ch 9]] — the grammar foundation reused to encode the UI model.
- [[fuzzingbook-18-grammar-miner|Ch 18]] — the grammar-mining lineage; here the source is a live UI rather than program traces.
- [[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]] — supplies the coverage strategy reused as transition coverage.
- [[fuzzingbook-19-information-flow|Ch 19]] — cited for the residual `exec()` injection risk.
- [[fuzzingbook-29-fuzzing-in-the-large|Ch 29]] — the next chapter (running fuzzers at scale).

## Contradictions
- None identified.
