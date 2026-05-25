# DSPy Tutorial: Saving and Loading Programs

Source: https://dspy.ai/tutorials/saving/
Fetched: 2026-05-24

## Overview

DSPy offers two approaches for persisting programs: saving only the state (similar to PyTorch weight-only checkpoints) or saving the complete program including architecture.

## State-Only Saving

### Concept

"State represents the DSPy program's internal state, including the signature, demos (few-shot examples), and other information" plus configurable module attributes. This approach is lighter and recommended when you can recreate the architecture.

### JSON Format (Recommended)

Save to JSON using:
```python
compiled_dspy_program.save("./dspy_program/program.json", save_program=False)
```

JSON is safer and human-readable but cannot serialize non-serializable objects like `dspy.Image` or datetime objects.

### Pickle Format

For non-serializable objects, use pickle:
```python
compiled_dspy_program.save("./dspy_program/program.pkl", save_program=False)
```

> **Security Warning**: "Loading `.pkl` files can execute arbitrary code and may be dangerous. Only load pickle files from trusted sources in secure environments."

### Loading State-Only Programs

Recreate the architecture first, then load:
```python
loaded_program = dspy.ChainOfThought("question -> answer")
loaded_program.load("./dspy_program/program.json")
```

For pickle files, include the safety flag:
```python
loaded_program.load("./dspy_program/program.pkl", allow_pickle=True)
```

Loaded demos appear as dictionaries rather than `dspy.Example` objects.

## Whole Program Saving

### Overview

"Starting from `dspy>=2.6.0`, DSPy supports saving the whole program, including the architecture and the state." This uses `cloudpickle` for serialization, requiring a directory rather than a single file.

### Saving
```python
compiled_dspy_program.save("./dspy_program/", save_program=True)
```

The system preserves both architecture and metadata (dependency versions).

### Loading
```python
loaded_dspy_program = dspy.load("./dspy_program/")
```

No reconstruction needed — the complete program loads directly.

### Custom Module Serialization

For programs depending on custom modules, register them during saving:
```python
compiled_dspy_program.save(
    "./dspy_program/",
    save_program=True,
    modules_to_serialize=[my_custom_module]
)
```

This uses `cloudpickle.register_pickle_by_value` internally to serialize dependencies by value rather than reference.

## Backward Compatibility

Current versions (pre-3.0.0) offer no guarantee of backward compatibility across DSPy versions. Load saved programs using the same version they were created with for consistent performance.

Future releases (3.0.0+) will guarantee backward compatibility within major versions.
