<!-- source: https://hypothesis.readthedocs.io/en/latest/how-to/external-fuzzers.html -->

# Use Hypothesis with an external fuzzer

Sometimes you might want to point a traditional fuzzer like [python-afl](https://github.com/jwilk/python-afl) or Google's [atheris](https://pypi.org/project/atheris/) at your code, to get coverage-guided exploration of native C extensions. The associated tooling is often much less mature than property-based testing libraries though, so you might want to use Hypothesis strategies to describe your input data, and our world-class shrinking and [observability](https://hypothesis.readthedocs.io/en/latest/reference/integrations.html#observability) tools to wrangle the results. That's exactly what this how-to guide is about!

> **Note**
>
> If you already have Hypothesis tests and want to fuzz them, or are targeting pure Python code, we strongly recommend the purpose-built [HypoFuzz](https://hypofuzz.com/).
> This page is about writing traditional 'fuzz harnesses' with an external fuzzer, using parts of Hypothesis.

In order to support this workflow, Hypothesis exposes the `fuzz_one_input` method. `fuzz_one_input` takes a bytestring, parses it into a test case, and executes the corresponding test once. This means you can treat each of your Hypothesis tests as a traditional fuzz target, by pointing the fuzzer at `fuzz_one_input`.

For example:

```python
from hypothesis import given, strategies as st

@given(st.integers())
def test_ints(n):
    pass

# this parses the bytestring into a test case using st.integers(),
# and then executes `test_ints` once.
test_ints.hypothesis.fuzz_one_input(b"\x00" * 50)
```

Note that `fuzz_one_input` bypasses the standard test lifecycle. In a standard test run, Hypothesis is responsible for managing the lifecycle of a test, for example by moving between each `Phase`. In contrast, `fuzz_one_input` executes one test case, independent of this lifecycle.

See the documentation of `fuzz_one_input` for details of how it interacts with other features of Hypothesis, such as `@settings`.

## Worked example: using Atheris

Here is an example that uses `fuzz_one_input` with the [Atheris](https://github.com/google/atheris) coverage-guided fuzzer (which is built on top of [libFuzzer](https://llvm.org/docs/LibFuzzer.html)):

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

Generating valid JSON objects based only on Atheris' `FuzzDataProvider` interface would be considerably more difficult.

You may also want to use `atheris.instrument_all` or `atheris.instrument_imports` in order to add coverage instrumentation to Atheris. See the [Atheris](https://github.com/google/atheris) documentation for full details.

---

<!-- The following is the authoritative `fuzz_one_input` API docstring (from
     hypothesis/src/hypothesis/core.py, HypothesisHandle.fuzz_one_input), which
     the how-to page links to for "details of how it interacts with other
     features of Hypothesis". Reproduced here so the source page can cite exact
     return-value / database / settings semantics. -->

## API: `fuzz_one_input`

Run the test as a fuzz target, driven with the `buffer` of bytes.

Depending on the passed `buffer` one of three things will happen:

* If the bytestring was invalid, for example because it was too short or was
  filtered out by `assume` or `.filter`, `fuzz_one_input` returns `None`.
* If the bytestring was valid and the test passed, `fuzz_one_input` returns
  a canonicalised and pruned bytestring which will replay that test case.
  This is provided as an option to improve the performance of mutating
  fuzzers, but can safely be ignored.
* If the test *failed*, i.e. raised an exception, `fuzz_one_input` will
  add the pruned buffer to the Hypothesis example database
  and then re-raise that exception. All you need to do to reproduce,
  minimize, and de-duplicate all the failures found via fuzzing is run
  your test suite!

To reduce the performance impact of database writes, `fuzz_one_input` only
records failing inputs which would be valid shrinks for a known failure -
meaning writes are somewhere between constant and log(N) rather than linear
in runtime. However, this tracking only works within a persistent fuzzing
process; for forkserver fuzzers we recommend `database=None` for the main
run, and then replaying with a database enabled if you need to analyse
failures.

Note that the interpretation of both input and output bytestrings is
specific to the exact version of Hypothesis you are using and the strategies
given to the test, just like the database and `@reproduce_failure`.

### Interaction with `@settings`

`fuzz_one_input` uses just enough of Hypothesis' internals to drive your
test function with a bytestring, and most settings therefore have no effect
in this mode. We recommend running your tests the usual way before fuzzing
to get the benefits of health checks, as well as afterwards to replay,
shrink, deduplicate, and report whatever errors were discovered.

* `settings.database` *is* used by `fuzz_one_input` - adding failures to
  the database to be replayed when
  you next run your tests is our preferred reporting mechanism and response
  to [the 'fuzzer taming' problem](https://blog.regehr.org/archives/925).
* `settings.verbosity` and `settings.stateful_step_count` work as usual.
* The `deadline`, `derandomize`, `max_examples`,
  `phases`, `print_blob`, `report_multiple_bugs`,
  and `suppress_health_check` settings do not affect `fuzz_one_input`.

### Example Usage

```python
@given(st.text())
def test_foo(s): ...

# This is a traditional fuzz target - call it with a bytestring,
# or a binary IO object, and it runs the test once.
fuzz_target = test_foo.hypothesis.fuzz_one_input

# For example:
fuzz_target(b"\x00\x00\x00\x00\x00\x00\x00\x00")
fuzz_target(io.BytesIO(b"\x01"))
```

> **Tip**
>
> If you expect to discover many failures while using `fuzz_one_input`,
> consider wrapping your database with `BackgroundWriteDatabase`, for
> low-overhead writes of failures.

> **Tip**
>
> Want an integrated workflow for your team's local tests, CI, and continuous fuzzing?
> Use [HypoFuzz](https://hypofuzz.com/) to fuzz your whole test suite, and find more bugs with the same tests!

Signature: `fuzz_one_input(buffer: bytes | bytearray | memoryview | BinaryIO) -> bytes | None`
