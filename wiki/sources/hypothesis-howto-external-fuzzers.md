---
title: "Use Hypothesis with an external fuzzer (Hypothesis how-to)"
type: source
tags: [testing, python, property-based-testing, fuzzing, how-to, hypothesis]
date: 2026-06-05
source_file: raw/hypothesis/how-to/hypothesis-howto-external-fuzzers.md
---

## Summary
A [[Hypothesis]] how-to guide for pointing a traditional coverage-guided fuzzer (python-afl, Google's Atheris, libFuzzer) at a [[PropertyBasedTesting|property-based]] test. The integration point is the `test_function.hypothesis.fuzz_one_input` method: it takes a **bytestring**, parses it into a test case via the test's strategies, and runs the test **once** — so a Hypothesis `@given` test becomes a drop-in fuzz target. This lets you use Hypothesis strategies to describe structured input (e.g. valid JSON) while a native fuzzer drives coverage-guided exploration, and reuse Hypothesis' [[Shrinking|shrinking]] + observability + [[ExampleDatabase|example database]] to triage the results. For pure-Python code or fuzzing existing Hypothesis tests, the guide instead recommends the purpose-built HypoFuzz product.

## Key Claims
- Hypothesis exposes `fuzz_one_input` to bridge property-based tests with external fuzzers; you reach it as the `.hypothesis.fuzz_one_input` attribute on a `@given`-decorated test function (e.g. `test_ints.hypothesis.fuzz_one_input(b"\x00" * 50)`).
- **Bytestring → example mapping:** `fuzz_one_input` takes a bytestring (or a binary IO object), parses it into a single test case using the test's [[SearchStrategy|strategies]], and executes the test exactly once. The bytestring is the fuzzer's mutable input; Hypothesis decodes it into a concrete generated value.
- **Return-value semantics (three outcomes):** (1) if the bytestring is *invalid* — too short, or filtered out by `assume()` / `.filter()` — it returns `None`; (2) if *valid and the test passes*, it returns a **canonicalised, pruned bytestring** that replays the same case (an optional optimisation for mutating fuzzers, safe to ignore); (3) if the test *fails* (raises), it adds the pruned buffer to the [[ExampleDatabase|example database]] and **re-raises** the exception.
- **Interacts with — not bypasses — the database:** `settings.database` *is* used; failing inputs are written so a normal `pytest` run will later replay, [[Shrinking|shrink]], deduplicate, and report them ("fuzzer taming"). To limit write overhead, only failing inputs that would be valid shrinks of a known failure are recorded (writes are constant-to-log(N), not linear); this dedup tracking only works within a *persistent* process, so for forkserver fuzzers the guide recommends `database=None` during the main run and replaying with a DB enabled afterward.
- **Bypasses the standard lifecycle / most settings:** `fuzz_one_input` runs one case independent of Hypothesis' normal `Phase` lifecycle. The `deadline`, `derandomize`, `max_examples`, `phases`, `print_blob`, `report_multiple_bugs`, and `suppress_health_check` settings have **no effect**; only `database`, `verbosity`, and `stateful_step_count` apply. Shrinking is *not* done inside `fuzz_one_input` — you get minimization by re-running the test suite over the database afterward.
- **Worked Atheris example:** a `st.recursive(...)` strategy generating valid JSON is wired in via `atheris.Setup(sys.argv, test_json_dumps_valid_json.hypothesis.fuzz_one_input)` then `atheris.Fuzz()`. The guide notes generating valid JSON from Atheris' raw `FuzzDataProvider` would be far harder, and suggests `atheris.instrument_all` / `atheris.instrument_imports` for coverage instrumentation.
- **Tooling guidance:** Atheris is built on libFuzzer; this workflow shines for coverage-guided exploration of native C extensions. For existing Hypothesis tests or pure-Python targets, use HypoFuzz instead. For many expected failures, wrap the database in `BackgroundWriteDatabase` for low-overhead writes.

## Key Quotes
> "In order to support this workflow, Hypothesis exposes the `fuzz_one_input` method. `fuzz_one_input` takes a bytestring, parses it into a test case, and executes the corresponding test once. This means you can treat each of your Hypothesis tests as a traditional fuzz target, by pointing the fuzzer at `fuzz_one_input`." — the core integration mechanism

> "Note that `fuzz_one_input` bypasses the standard test lifecycle. In a standard test run, Hypothesis is responsible for managing the lifecycle of a test, for example by moving between each `Phase`. In contrast, `fuzz_one_input` executes one test case, independent of this lifecycle." — why it's a single-shot target, not a full run

> "If the test *failed*, i.e. raised an exception, `fuzz_one_input` will add the pruned buffer to the Hypothesis example database and then re-raise that exception. All you need to do to reproduce, minimize, and de-duplicate all the failures found via fuzzing is run your test suite!" — `fuzz_one_input` API docstring; the database is the reporting/triage channel

> "If the bytestring was valid and the test passed, `fuzz_one_input` returns a canonicalised and pruned bytestring which will replay that test case. This is provided as an option to improve the performance of mutating fuzzers, but can safely be ignored." — return value on success

> "If you already have Hypothesis tests and want to fuzz them, or are targeting pure Python code, we strongly recommend the purpose-built HypoFuzz. This page is about writing traditional 'fuzz harnesses' with an external fuzzer, using parts of Hypothesis." — scoping note

## Code Receipt
Minimal target — the `.hypothesis.fuzz_one_input` entry point on a `@given` test:
```python
from hypothesis import given, strategies as st

@given(st.integers())
def test_ints(n):
    pass

# parses the bytestring into a test case using st.integers(), runs test_ints once
test_ints.hypothesis.fuzz_one_input(b"\x00" * 50)
```

Atheris harness (coverage-guided, built on libFuzzer):
```python
import json
import sys
import atheris
from hypothesis import given, strategies as st

@given(
    st.recursive(
        st.none() | st.booleans() | st.integers() | st.floats() | st.text(),
        lambda j: st.lists(j) | st.dictionaries(st.text(), j),
    )
)
def test_json_dumps_valid_json(value):
    json.dumps(value)

atheris.Setup(sys.argv, test_json_dumps_valid_json.hypothesis.fuzz_one_input)
atheris.Fuzz()
```

Signature & return contract (per the API docstring):
```text
fuzz_one_input(buffer: bytes | bytearray | memoryview | BinaryIO) -> bytes | None
  invalid input (too short / filtered by assume()/.filter())  -> None
  valid + test passed   -> canonicalised, pruned replay bytestring (optional, ignorable)
  test failed (raised)  -> writes pruned buffer to example database, then re-raises
```
Settings that apply: `database`, `verbosity`, `stateful_step_count`.
Settings ignored: `deadline`, `derandomize`, `max_examples`, `phases`, `print_blob`, `report_multiple_bugs`, `suppress_health_check`.

## Connections
- [[Hypothesis]] — exposes `fuzz_one_input` as the `.hypothesis` attribute on `@given` tests; this how-to documents that bridge.
- [[Fuzzing]] — the coverage-guided / mutation-based input-generation paradigm this guide connects Hypothesis to; names Atheris, python-afl, libFuzzer, and HypoFuzz.
- [[PropertyBasedTesting]] — the complementary strategy-driven input model; `fuzz_one_input` makes a property test consumable by a fuzzer's mutation loop.
- [[SearchStrategy]] — the strategies that decode the fuzzer's bytestring into a concrete test case (e.g. `st.recursive(...)` for JSON).
- [[ExampleDatabase]] — where failures discovered while fuzzing are written for later replay/shrink/dedup; the guide's preferred "fuzzer taming" reporting channel.
- [[Shrinking]] — *not* performed inside `fuzz_one_input`; you minimise by re-running the suite over the database afterward.
- [[HypothesisSettings]] — most settings (deadline, max_examples, phases, suppress_health_check, …) have no effect here; only `database`, `verbosity`, `stateful_step_count` apply.
- [[Python]] — implementation/target language.

## Contradictions
- None. This guide *extends* the Hypothesis cluster: it reuses the [[ExampleDatabase]] and [[Shrinking]] machinery rather than conflicting with them. It clarifies (without contradicting) the [[hypothesis-domain-and-distribution]] note that points distribution-control seekers to `hypofuzz` — here HypoFuzz is recommended for fuzzing *existing* tests or pure-Python code, whereas `fuzz_one_input` is for harnessing an *external* fuzzer.
