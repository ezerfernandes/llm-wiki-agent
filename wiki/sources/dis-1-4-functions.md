---
title: "Dive into Systems — Ch 1.4 Functions"
type: source
tags: [book, dive-into-systems, c-language, functions]
date: 2026-05-17
source_file: https://diveintosystems.org/book/C1-C_intro/functions.html
---

## Summary

Section 1.4 of [[DiveIntoSystems]] (fourth content section of Ch 1 *By the C, the Beautiful C*) adds the **function** abstraction on top of the [[CLanguage|C]] surface area built up across [[dis-1-1-getting-started|Ch 1.1]] (types / [[CArithmeticOperators|arithmetic]] / [[MainFunction|`main`]]), [[dis-1-2-input-output|Ch 1.2]] (I/O), and [[dis-1-3-conditionals-loops|Ch 1.3]] (control flow). It introduces the **definition** / **declaration** distinction — full [[FunctionDefinition|function definitions]] with `return type, name, parameter list, body` versus header-only [[FunctionPrototype|prototypes]] that let a caller name a function before its definition appears in the file — the **`void`** return type for functions that produce no value, and the chapter's load-bearing semantic rule: **[[PassByValue|arguments to C functions are passed by value]]** — each parameter is *assigned* the value of the corresponding argument, so mutations to parameters are invisible to the caller. Section 1.4.1 zooms into the runtime: every [[FunctionCall|call]] pushes a new [[StackFrame|stack frame]] (also called an *activation record*) onto the [[ExecutionStack|execution stack]] containing that activation's [[FunctionParameter|parameters]] and [[LocalVariable|local variables]]; only the top frame's names are in [[FunctionScope|scope]]; a [[ReturnStatement|`return`]] pops the frame and yields one value back to the caller. The worked example pair — a `void print_table(int start, int stop)` that prints squares and an `int max(int n1, int n2)` that returns the larger of its arguments — anchors all of this against [[MainFunction|`main`]] doing the calls.

## Key Claims

- **A function is named, typed, parameterized code.** Header form `<return type> <name>(<parameter list>) { <body> }`; the parameter list is comma-separated `<type> <name>` pairs. Functions accept zero or more inputs and return at most one value.
- **`void` is the *no-value* return type.** Functions performing only side effects (printing, modifying global state) declare `void` as their return type and omit the trailing value on `return;` (or omit the statement entirely). The print_table example uses `void`.
- **[[FunctionDefinition|Definition]] vs. [[FunctionPrototype|prototype]] is the chapter's main distinction.** A *definition* supplies the full body; a *prototype* / *declaration* gives only the header (`int max(int n1, int n2);`) and tells the [[CCompiler|compiler]] *enough to type-check calls* without requiring the body yet.
- **C is single-pass over declarations.** A function must be either *defined* or *prototyped* **before** it is called. The practical idiom is: prototypes at the top of the file (above [[MainFunction|`main`]]), full definitions below — so [[MainFunction|`main`]] can read top-down even though it calls everything.
- **[[PassByValue|Arguments are passed by value]].** Per [[dis-1-4-functions|Ch 1.4]]: *"each function parameter is assigned the value of the corresponding argument passed to it in the function call by the caller."* Direct consequence: *"any change to a parameter's value in the function … is not visible to the caller."* Parameters are *local variables initialized from the argument values*.
- **Parameters vs. arguments is a vocabulary point.** *Parameters* are the named placeholders in the function header; *arguments* are the concrete values supplied at a [[FunctionCall|call site]]. The C language matches them positionally and by type, performing the usual conversions where applicable.
- **[[LocalVariable|Local variables]] (declared inside a function body) and [[FunctionParameter|parameters]] are in [[FunctionScope|scope]] only within that function.** Once the function returns, its frame is gone and those names cannot be referenced.
- **The [[ExecutionStack|execution stack]] tracks active calls.** Each [[FunctionCall|call]] pushes a [[StackFrame|stack frame]] (a.k.a. **activation frame** / **activation record**) holding *this activation's* parameter values and local variable values. Only the **top** frame is the *active* frame — only its names are in scope. [[ReturnStatement|Returning]] pops the frame, exposing the caller's frame again.
- **Two worked examples carry the chapter.** `void print_table(int start, int stop)` — prints squares from `start` to `stop` using a [[ForLoop|`for` loop]] — exemplifies a `void` function with two `int` parameters. `int max(int n1, int n2)` — uses an [[IfStatement|`if`]] to track which input is larger, then `return`s it — exemplifies a value-returning function.
- **Cross-walk to [[Python]].** Python's `def` infers types and returns a single value (or `None`); C requires an explicit return type and explicit parameter types, distinguishes `void` from non-`void`, and routes return through a frame on a stack the programmer can reason about (and which the rest of [[DiveIntoSystems]] will eventually open up at the assembly / [[MemoryHierarchy|memory hierarchy]] level).

## Key Quotes

> "A function **declaration** or **prototype** specifies the function's name, its return type, and its parameter list (the number and types of all the parameters)." — establishes the *header-only* artifact that fronts a definition appearing later in the file.

> "Arguments to C functions are **passed by value**: each function parameter is assigned the value of the corresponding argument passed to it in the function call by the caller." — the chapter's headline semantic rule; the single most important takeaway about C function calls.

> "Any change to a parameter's value in the function (that is, assigning a parameter a new value in the function) is not visible to the caller." — the direct consequence of [[PassByValue|pass-by-value]] and the reason C needs *pointers* (next chapter) to express *output parameters*.

> "Functions that don't return a value should specify the `void` return type." — anchors the [[VoidType|`void`]]-as-return convention that the print_table example demonstrates.

> "The **execution stack** keeps track of the state of active functions in a program. Each function call creates a new **stack frame** (sometimes called an **activation frame** or **activation record**) containing its parameter and local variable values." — the *runtime* model that gives the rest of the [[DiveIntoSystems]] corpus (assembly, calling conventions, [[MemoryHierarchy|memory hierarchy]]) something concrete to graft onto.

> "When a function is called, a new stack frame is created for it (pushed on the top of the stack), and space for its local variables and parameters is allocated in the new frame. When a function returns, its stack frame is removed from the stack (popped from the top of the stack), leaving the caller's stack frame on the top of the stack." — the **push-on-call / pop-on-return** invariant that makes [[FunctionScope|scope]] and [[LocalVariable|local variable]] lifetimes mechanical.

## Worked examples

**Function prototypes at the top of the file:**

```c
int  max(int n1, int n2);
void print_table(int start, int stop);
```

**Definition: `void` function with two `int` parameters:**

```c
void print_table(int start, int stop) {
    int i;

    for (i = start; i <= stop; i++) {
        printf("%d\t", i*i);
    }

    printf("\n");
}
```

**Definition: value-returning function with an `if` and a `return`:**

```c
int max(int n1, int n2) {
    int result;

    result = n1;

    if (n2 > n1) {
        result = n2;
    }

    return result;
}
```

**Calling them from [[MainFunction|`main`]]:**

```c
int main(void) {
    int x, y, larger;

    printf("This program will operate over two int values.\n");

    printf("Enter the first value: ");
    scanf("%d", &x);

    printf("Enter the second value: ");
    scanf("%d", &y);

    larger = max(x, y);

    printf("The larger of %d and %d is %d\n", x, y, larger);

    print_table(x, larger);

    return 0;
}
```

## Connections

- [[DiveIntoSystems]] — the book; this is Ch 1.4 (4th content section after [[dis-1-1-getting-started|Ch 1.1]] / [[dis-1-2-input-output|Ch 1.2]] / [[dis-1-3-conditionals-loops|Ch 1.3]]).
- [[SuzanneJMatthews]] / [[TiaNewhall]] / [[KevinCWebb]] — co-authors.
- [[dis-1-1-getting-started]] — supplied [[CLanguage|C]] / [[MainFunction|`main`]] / [[CPrimitiveType|primitive types]] / [[VariableDeclaration|declarations]]; this chapter promotes [[MainFunction|`main`]] from *the only function* to *one function among many*.
- [[dis-1-2-input-output]] — the worked examples reuse [[Printf|`printf`]] / [[Scanf|`scanf`]] / [[AddressOfOperator|`&`]] from Ch 1.2 inside the new function bodies.
- [[dis-1-3-conditionals-loops]] — the function bodies use [[ForLoop|`for`]] (in `print_table`) and [[IfStatement|`if`]] (in `max`) from Ch 1.3.
- [[CLanguage]] — functions are a primary structural unit of the language; this section adds the *modularity* layer.
- [[Function]] — the umbrella concept for named, typed, parameterized code blocks.
- [[FunctionDefinition]] — the full header-plus-body artifact.
- [[FunctionPrototype]] — the header-only declaration that lets [[MainFunction|`main`]] call code defined later in the file.
- [[FunctionParameter]] — the named, typed placeholder in a function header.
- [[FunctionArgument]] — the concrete value supplied at a [[FunctionCall|call site]].
- [[ReturnStatement]] — the construct that yields a value (or none) from a function back to its caller.
- [[ReturnType]] — the typed slot in the function header that names what (if anything) the function yields.
- [[VoidType]] — the *no-value* return type for side-effect-only functions; also used in [[MainFunction|`int main(void)`]] to declare no parameters.
- [[PassByValue]] — the **headline rule** for C function calls; explains why mutating a parameter does not affect the caller's variable.
- [[FunctionScope]] — the lexical-scope rule: a [[FunctionParameter|parameter]] or [[LocalVariable|local variable]] is in scope only within its own function.
- [[LocalVariable]] — a variable declared inside a function body; lives in that activation's [[StackFrame|stack frame]].
- [[FunctionCall]] — the runtime act that pushes a new [[StackFrame|stack frame]] onto the [[ExecutionStack|execution stack]].
- [[ExecutionStack]] — the LIFO discipline that tracks active function calls; later [[DiveIntoSystems]] chapters open up its assembly-level layout.
- [[StackFrame]] — the per-call record holding [[FunctionParameter|parameters]] + [[LocalVariable|locals]] + the return address.
- [[MainFunction]] — promoted here from *only function in the program* to *just the first frame on the stack*.
- [[ControlFlow]] — function calls/returns are themselves a control-flow mechanism layered on top of the [[dis-1-3-conditionals-loops|Ch 1.3]] branches and loops.
- [[Python]] — contrast: `def` infers types, returns `None` implicitly, has no separate prototype-vs-definition split, and packages locals via frame objects rather than C stack frames.
- [[TheEmbeddedRustBook]] — sibling systems-track book; Rust has the same call/return + stack-frame discipline at the ABI level (`extern "C"`), differing chiefly in *ownership*-driven parameter semantics rather than C's flat pass-by-value of bits.

## Contradictions

- None with existing wiki content. This section **extends** [[MainFunction]] (previously the *only* function the wiki had described in C) into a general [[Function]] concept; **complements** [[ControlFlow]] from [[dis-1-3-conditionals-loops|Ch 1.3]] with the call/return layer; and **sets up** the pointer chapter that follows (where [[PassByValue]] becomes the *motivation* for explicit address-passing as a workaround). The [[ExecutionStack]] / [[StackFrame]] vocabulary introduced here is the same model the rest of the [[DiveIntoSystems]] corpus (assembly, calling conventions, [[MemoryHierarchy]]) will build on.
