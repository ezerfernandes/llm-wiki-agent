---
title: "GUIFuzzer"
type: concept
tags: [fuzzing, testing, gui, selenium, model-based-testing, class-hierarchy, python, tool]
sources: [fuzzingbook-28-gui-fuzzer]
last_updated: 2026-06-06
---

# GUIFuzzer

**`GUIFuzzer`** is *The Fuzzing Book*'s class for fuzzing graphical user interfaces through a real browser: a [[GrammarFuzzer|`GrammarFuzzer`]] subclass that *explores* a [[Selenium]]-driven UI while *growing its [[Grammar|grammar]] model* of that UI at the same time. It is the engine of [[GUIFuzzing|GUI fuzzing]] in [[fuzzingbook-28-gui-fuzzer|Ch 28]], paired with three collaborators (`GUIGrammarMiner`, `GUIRunner`) and capped by the coverage-driven `GUICoverageFuzzer`.

## The four collaborating classes
- **`GUIGrammarMiner`** ([[GrammarMiner|grammar miner]]) — discovers the actions available on the *current* page. `mine_state_actions()` returns a `frozenset` merging input-element actions (text→`fill`, checkbox/radio→`check`, submit→`submit`), button actions, and link actions (`mine_a_element_actions()`, with `follow_link()` keeping exploration on-host; off-host links become `ignore()`). `mine_state_grammar()` turns those actions into a state [[Grammar|grammar]]: each `click()`/`submit()` introduces a fresh state symbol marked `<unexplored>`, form fields collapse into one submission alternative, and a `<end>` final state terminates the otherwise-infinite stream. A `GUI_GRAMMAR` template supplies value rules per input type. Subclass it (passed via the `miner=` constructor argument) to extend GUI interpretation.
- **`GUIRunner`** ([[Runner|`Runner`]] subclass) — *executes* an action string on the driver. `run()` calls `exec()` with `__builtins__={}` and only `fill`/`check`/`submit`/`click` in scope, with `html.escape()`d names, to limit code injection through element names (residual risk per [[fuzzingbook-19-information-flow|Ch 19]]). `find_element()` matches `By.NAME` then `By.LINK_TEXT`; the `do_*` methods defer to Selenium with `WebDriverWait` delays.
- **`GUIFuzzer`** — explores and models simultaneously. It maintains `state_symbol` (current symbol, e.g. `<state-1>`), `state` (the action `frozenset`), and `states_seen` (state→symbol). `run(runner)` restarts, fuzzes one action sequence, reads the expected last state from the [[DerivationTree|derivation tree]] via `fsm_path()`/`fsm_last_state_symbol()`, executes it, then `update_state()`: `update_new_state()` mines a sub-grammar for the newly reached page and merges it; `update_existing_state()` merges the expected state into a previously seen one using `replace_symbol()`.
- **`GUICoverageFuzzer`** — combines `GUIFuzzer.run()` with [[GrammarCoverageFuzzer|`GrammarCoverageFuzzer`]]'s coverage-preferring expansion choices via **multiple inheritance** (`inheritance_conflicts()` + a custom `__init__` calling `reset_coverage()`). `explore_all(runner, max_actions=100)` runs until no `<unexplored>` symbol remains; since each transition is a grammar expansion, covering expansions covers transitions.

## Interface
```python
gui_driver = start_webdriver()
gui_driver.get(httpd_url)
gui_fuzzer = GUICoverageFuzzer(gui_driver)
gui_runner = GUIRunner(gui_driver)
gui_fuzzer.explore_all(gui_runner)        # mine the whole UI model
fsm_diagram(gui_fuzzer.grammar)           # view the FSM
actions = gui_fuzzer.fuzz()               # a new interaction sequence
gui_runner.run(actions)                   # execute it
```

## Limitations
Experimental: supports only a subset of HTML form and link features and does **not** account for JavaScript-driven behavior; some exceptions (`ElementClickInterceptedException`, `NoSuchElementException`, …) are swallowed during exploration.

## Connections
- [[GUIFuzzing]] — the technique this class family implements.
- [[UINavigationModel]] — the FSM-of-pages grammar `GUIFuzzer` mines and grows.
- [[ModelBasedTesting]] — the FSM-in-a-grammar generation strategy it embodies.
- [[GrammarFuzzer]] — the superclass supplying derivation-tree generation ([[fuzzingbook-10-grammar-fuzzer|Ch 10]]).
- [[GrammarCoverageFuzzer]] — mixed in for `GUICoverageFuzzer` to cover all transitions ([[fuzzingbook-11-grammar-coverage-fuzzer|Ch 11]]).
- [[GrammarMiner]] / [[GrammarMining]] — `GUIGrammarMiner` mines a grammar from a live UI.
- [[Runner]] — `GUIRunner` subclasses the harness abstraction.
- [[Selenium]] / [[WebDriver]] — the driver `GUIFuzzer` controls.
- [[FiniteStateMachine]] — the model embedded in the grammar.
- [[DerivationTree]] — read to determine the target state symbol.
- [[Grammar]] — the unified states-and-values data structure.
- [[Fuzzing]] — the parent discipline.
- [[fuzzingbook-28-gui-fuzzer]] — the chapter that introduces it.

## Sources
- [[fuzzingbook-28-gui-fuzzer]] — *The Fuzzing Book* Ch 28, "Testing Graphical User Interfaces."
