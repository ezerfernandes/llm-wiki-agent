---
title: "Hypothesis"
type: entity
tags: [testing, python, library, property-based-testing, tooling]
sources: [hypothesis-howto-suppress-healthchecks, hypothesis-domain-and-distribution, hypothesis-howto-type-strategies, hypothesis-example-count, hypothesis-howto-custom-database, hypothesis-howto-detect-tests, hypothesis-howto-external-fuzzers, fuzzingbook-24-api-fuzzer]
last_updated: 2026-06-06
---

# Hypothesis

**Hypothesis** is the leading [[PropertyBasedTesting|property-based testing]] library for [[Python]], originally created by David R. MacIver and maintained by the HypothesisWorks project. Instead of writing example-by-example assertions, you declare *strategies* that describe the space of valid inputs; Hypothesis generates many examples, and when a test fails it *shrinks* the failing input to a minimal reproducing case.

It integrates tightly with [[Pytest]] (its `@given` decorator wraps ordinary test functions, and `conftest.py` is the usual place to configure it), and is commonly compared to QuickCheck-style tools from other languages.

The strategy object you declare has the public type [[SearchStrategy]]`[T]` (generic over the example type it generates), and Hypothesis ships [[TypeHints|type hints]] for all of its strategies and strategy factories; see [[hypothesis-howto-type-strategies]].

## Configuration & health checks
- Test behavior is tuned through the [[HypothesisSettings|settings system]] — `@settings(...)` decorators and named profiles registered with `settings.register_profile()` / `settings.load_profile()`.
- During a run, Hypothesis emits [[HealthCheck]] warnings to flag potential problems with test effectiveness, performance, or generated-example quality (e.g. `filter_too_much`, `function_scoped_fixture`, `differing_executors`).
- Health checks can be silenced per-test or globally via the `suppress_health_check` setting; see [[hypothesis-howto-suppress-healthchecks]].

## How many times a test runs
The run count is *approximately* `max_examples` but not fixed (per [[hypothesis-example-count]]): **fewer** if the search space is exhausted (e.g. `st.integers(0, 19)` → 20 runs), **more** if examples are retried because they failed an `assume()`/`.filter()` or were too large (→ [[HealthCheck|`HealthCheck.data_too_large`]]), and a variable count once a failure is found and the [[Shrinking|`Phase.shrink` / `Phase.explain`]] phases run. A minimal failing example is always replayed **one extra time** to check for flakiness — so a failure at `n=0` executes `n=0` twice. `.filter()` is more efficient than `assume()` (it retries within an example rather than discarding the whole example).

## Persisting failing examples
Hypothesis keeps a pluggable [[ExampleDatabase]] — a key-value byte store — that saves the [[Shrinking|minimal failing example]] when a test fails and replays it on the next run (default: the `.hypothesis/examples` directory). The backend is swappable via the `database=` [[HypothesisSettings|setting]]; you can subclass `hypothesis.database.ExampleDatabase` (implement `save`/`fetch`/`delete`, optionally `move`) for stores like SQLite or shared/CI-backed databases — see [[hypothesis-howto-custom-database]].

## Design philosophy: domain vs distribution
A defining stance (per [[hypothesis-domain-and-distribution]]): **the user owns the *domain*** (which inputs a strategy *can* produce) but **the library owns the *distribution*** (how often each is produced). Distribution is intentionally *not* a public knob — the engine biases generation toward bug discovery via static strategy design, dynamic engine features, source analysis, and swarm testing, and reserves the right to change it without breaking APIs. Users who need explicit distribution control are pointed to alternative backends — `hypofuzz` (fuzzing loop over the same strategies) and `crosshair` (concolic/SMT-based execution).

## Detecting Hypothesis tests
For plugins and tooling that need to know whether a callable is a Hypothesis test, the public predicate `is_hypothesis_test()` (imported `from hypothesis import is_hypothesis_test`) returns true for `@given`-decorated functions **and** for stateful tests — e.g. `is_hypothesis_test(MyStateMachine.TestCase().runTest)` where `MyStateMachine` subclasses `RuleBasedStateMachine` (from `hypothesis.stateful`). Under [[Pytest]], the Hypothesis pytest plugin auto-applies the `@pytest.mark.hypothesis` mark to every Hypothesis test, so a plugin can also detect one via `node.get_closest_marker("hypothesis")`. See [[hypothesis-howto-detect-tests]].

## External fuzzers (`fuzz_one_input`)
For [[Fuzzing|coverage-guided fuzzing]] of native code, Hypothesis exposes `test_fn.hypothesis.fuzz_one_input` — a method that takes a **bytestring** (or binary IO), decodes it via the test's [[SearchStrategy|strategies]] into one test case, and runs the test **once**, turning a `@given` test into a traditional fuzz target for external fuzzers like Atheris (built on libFuzzer) or python-afl. It bypasses the normal `Phase` lifecycle: returns `None` for invalid/filtered inputs, returns a canonicalised replay bytestring on pass, and on failure **writes the pruned buffer to the [[ExampleDatabase]] and re-raises** — so re-running the suite replays, [[Shrinking|shrinks]], and deduplicates fuzzing-found bugs ("fuzzer taming"). Only `database`, `verbosity`, `stateful_step_count` settings apply; `deadline` / `max_examples` / `phases` / `suppress_health_check` / etc. do not. For pure-Python targets or fuzzing existing tests, the docs recommend HypoFuzz instead. See [[hypothesis-howto-external-fuzzers]].

## From The Fuzzing Book — Fuzzing APIs
[[fuzzingbook-24-api-fuzzer|Ch 24]] cites Hypothesis in its Background as "a very nice implementation for Python" of the same idea the chapter develops by hand: using *generator functions* to build and combine data-structure generators for testing APIs. The chapter's manual machinery — [[GeneratorGrammar|generator grammars]] producing integers/floats/strings/lists for [[APIFuzzing|API fuzzing]] — is the do-it-yourself analogue of Hypothesis's `strategies`, and both trace their lineage to QuickCheck (the chapter's stated origin for the generator-function approach).

## Connections
- [[PropertyBasedTesting]] — the paradigm Hypothesis implements.
- [[APIFuzzing]] — Ch 24 builds, by hand, the generator-based API-testing approach Hypothesis productizes (cited in its Background).
- [[Fuzzing]] — bridged to property-based tests via `fuzz_one_input` for coverage-guided fuzzing of native extensions.
- [[Shrinking]] — how failing inputs are minimized (`Phase.shrink`) before reporting.
- [[HypothesisSettings]] — how its runtime behavior is configured.
- [[HealthCheck]] — its built-in test-quality warnings.
- [[Pytest]] — primary host test framework.
- [[Python]] — implementation language and target.
- [[SearchStrategy]] — the public generic type of a strategy object.
- [[TypeHints]] — Hypothesis ships type hints for all strategies and factories.
- [[ExampleDatabase]] — pluggable byte store that persists/replays failing examples across runs.

## Sources
- [[hypothesis-howto-suppress-healthchecks]] — how-to on globally suppressing a health check via settings profiles.
- [[hypothesis-domain-and-distribution]] — the domain (user-owned) vs distribution (library-owned) design philosophy.
- [[hypothesis-howto-type-strategies]] — how-to on writing type hints for strategies (`SearchStrategy[T]`, `@composite`, covariance).
- [[hypothesis-example-count]] — explanation of how many times a test actually runs (`max_examples`, retries, shrink/explain, flakiness replay).
- [[hypothesis-howto-custom-database]] — how-to on subclassing `ExampleDatabase` to persist/replay failing examples (SQLite example, change listening).
- [[hypothesis-howto-detect-tests]] — how-to on detecting whether a callable is a Hypothesis test (`is_hypothesis_test()`; pytest's `@pytest.mark.hypothesis` mark).
- [[hypothesis-howto-external-fuzzers]] — how-to on using `fuzz_one_input` to drive an external coverage-guided fuzzer (Atheris/libFuzzer/python-afl) through Hypothesis strategies.
- [[fuzzingbook-24-api-fuzzer]] — *The Fuzzing Book* Ch 24, "Fuzzing APIs," cites Hypothesis as the leading Python implementation of generator-based API testing.
