---
title: "Dive into Systems — Appendix 1.2 Input/Output (for Java Programmers)"
type: source
tags: [book, dive-into-systems, c-language, java, io, cross-walk]
date: 2026-05-18
source_file: https://diveintosystems.org/book/Appendix1/input_output.html
---

## Summary

Appendix 1.2 of [[DiveIntoSystems]] is the [[Java]]-programmer's retelling of [[dis-1-2-input-output|Ch 1.2]]. Covers the same [[FormatSpecifier|`%`-specifier]] vocabulary (`%d` / `%g` / `%s` / `%c`), [[Printf|`printf`]] (Java's `System.out.printf` is the closest cousin), [[Scanf|`scanf`]] (vs. Java's [[Scanner]] class), and the **first sighting of a [[CMemoryAddress|memory address]] as a value** — the [[AddressOfOperator|address-of `&`]] operator that `scanf` requires on its output arguments. See [[JavaVsC]] for the consolidated cross-walk.

## Key Claims (Java-vs-C deltas)

- **Java's `Scanner` ↔ C's [[Scanf|`scanf`]]**: Java reads via `Scanner sc = new Scanner(System.in); int n = sc.nextInt();`. C reads via `scanf("%d", &num1);` — same outcome, very different shape.
- **The `&` operator is the key syntactic shock for Java programmers.** [[Scanf|`scanf`]] must write *back* into the caller's variable, and C has no implicit pass-by-reference, so the caller must pass the variable's [[CMemoryAddress|address]] explicitly via [[AddressOfOperator|`&`]]. Java's `Scanner` handles this implicitly via object methods.
- **Format-specifier vocabulary is shared with Java's `printf`** — `%d` / `%g` / `%s` / `%c` work identically on both sides for formatted output.
- **[[EscapeSequence|Escape sequences]] are shared** — `\n` / `\t` / `\\` work the same way in C's `printf` and Java's `printf`.
- **C's `scanf` is "picky"** about exact input formatting — malformed input can produce infinite loops (the read pointer doesn't advance). Java's `Scanner` is more forgiving and throws an exception instead.
- **Both libraries are stdlib**: [[StandardIOLibrary|`<stdio.h>`]] in C; `java.util.Scanner` / `java.lang.System` in Java.

## Key Quote

> *"scanf is "picky" about exact input formatting and less forgiving of malformed data compared to Java's Scanner approach."*

## Worked example — read two ints

```c
#include <stdio.h>
int main(void) {
    int num1, num2;
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);   // note: &num1 not num1
    printf("Sum = %d\n", num1 + num2);
    return 0;
}
```

```java
import java.util.Scanner;
public class Sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        System.out.printf("Sum = %d%n", n1 + n2);
    }
}
```

## Connections

- [[DiveIntoSystems]] — Appendix 1 sister of [[dis-1-2-input-output|Ch 1.2]].
- [[dis-1-2-input-output]] — the Python-cross-walk sibling.
- [[JavaVsC]] — consolidated cross-walk table.
- [[Java]] / [[Scanner]] — Java's input class.
- [[Printf]] / [[Scanf]] / [[FormatSpecifier]] / [[EscapeSequence]] / [[AddressOfOperator]] / [[CMemoryAddress]] / [[StandardInput]] / [[StandardOutput]] / [[StandardIOLibrary]] — reused unchanged from Ch 1.2.

## Contradictions

- None. Pure Java-perspective retelling of [[dis-1-2-input-output|Ch 1.2]].
