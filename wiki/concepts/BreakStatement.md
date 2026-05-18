---
title: "break Statement (C)"
type: concept
tags: [c-language, control-flow, structured-jump]
sources: [dis-1-3-conditionals-loops]
last_updated: 2026-05-17
---

# break Statement (C)

The **`break` statement** in [[CLanguage|C]] terminates the **innermost enclosing** loop ([[WhileLoop|`while`]] / [[DoWhileLoop|`do`–`while`]] / [[ForLoop|`for`]]) or [[SwitchStatement|`switch`]] immediately, transferring control to the statement following the construct.

```c
for (int i = 0; i < N; i++) {
    if (a[i] == target) {
        index = i;
        break;       /* exit the loop right now */
    }
}
/* execution resumes here */
```

## Rules (per [[dis-1-3-conditionals-loops|DiS Ch 1.3]])

- **Targets only the innermost** enclosing loop or `switch`. There is no labeled `break` in C; to exit nested loops, use a flag variable, restructure, or `goto`.
- **Inside a [[SwitchStatement|`switch`]]**, `break` is the standard way to terminate a [[CaseLabel|`case`]] arm and prevent fall-through to the next case.
- **Outside any loop or `switch`**, `break` is a compile-time error.

## Typical idioms

- **Search-and-exit** — scan an array and bail out when the target is found.
- **Sentinel-based input** — read until a sentinel value, then `break`.
- **`switch` case terminator** — close each [[CaseLabel|`case`]] body with `break` to keep the cases disjoint.

## Connections

- [[dis-1-3-conditionals-loops]] — source.
- [[ContinueStatement]] — sibling structured jump; skips the rest of the iteration instead of exiting.
- [[WhileLoop]] / [[DoWhileLoop]] / [[ForLoop]] — loop constructs `break` can exit.
- [[SwitchStatement]] / [[CaseLabel]] — the `switch` use of `break`.
- [[ControlFlow]] / [[CLanguage]] / [[DiveIntoSystems]].
