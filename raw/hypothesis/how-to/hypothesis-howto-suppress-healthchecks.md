<!-- Source: https://hypothesis.readthedocs.io/en/latest/how-to/suppress-healthchecks.html -->

# Suppress a health check everywhere

Hypothesis raises `HealthCheck` warnings to signal potential issues with test
effectiveness, performance, or example generation quality. While these warnings
can be valuable, you may want to disable specific ones globally.

To suppress a health check across all tests, use Hypothesis's settings profile
system. Create a profile using `register_profile()` and `load_profile()`,
placing this code in a file loaded before tests run (such as `conftest.py` for
pytest):

```python
from hypothesis import HealthCheck, settings

settings.register_profile(
    "my_profile", suppress_health_check=[HealthCheck.filter_too_much]
)
settings.load_profile("my_profile")
```

This example suppresses the `filter_too_much` health check globally. Individual
test decorators using `@settings` with explicit `suppress_health_check` values
will override the profile setting.

## I want to suppress all health checks!

> **Warning**
>
> We strongly recommend that you suppress health checks as you encounter them,
> rather than using a blanket suppression. Several health checks check for
> subtle interactions that may save you hours of debugging, such as
> `HealthCheck.function_scoped_fixture` and `HealthCheck.differing_executors`.

While not recommended, you can disable all health checks:

```python
from hypothesis import HealthCheck, settings

settings.register_profile("my_profile", suppress_health_check=list(HealthCheck))
settings.load_profile("my_profile")
```
