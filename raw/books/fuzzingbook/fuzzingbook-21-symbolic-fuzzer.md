# Symbolic Fuzzing

One of the problems with traditional methods of fuzzing is that they fail to exercise all the possible behaviors that a system can have, especially when the input space is large. Quite often the execution of a specific branch of execution may happen only with very specific inputs, which could represent a minimal fraction of the input space. The traditional fuzzing methods relies on chance to produce inputs they need. However, relying on randomness to generate values that we want is a bad idea when the space to be explored is huge. For example, a function that accepts a string, even if one only considers the first $10$ characters, already has $2^{80}$ possible inputs. If one is looking for a specific string, random generation of values will take a few thousand years even in one of the super computers.

In the [chapter on concolic testing](ConcolicFuzzer.ipynb), we have seen how _concolic tracing_ can offer a way out. We saw how concolic tracing can be implemented using direct information flows using the Python interpreter. However, there are two problems with this approach.
* The first is that concolic tracing relies on the existence of sample inputs. What if one has no sample inputs?
* Second, direct information flows could be unreliable if the program has indirect information flows such as those based on control flow.

In both cases, _static code analysis_ can bridge the gap. However, that raises the question: Can we determine the complete behavior of the program by examining it statically, and check if it behaves unexpectedly under some (unknown) input or result in an unexpected output?

_Symbolic execution_ is one of the ways that we can reason about the behavior of a program without executing it. A program is a computation that can be treated as a system of equations that obtains the output values from the given inputs. Executing the program symbolically -- that is, solving these mathematically -- along with any specified objective such as covering a particular branch or obtaining a particular output will get us inputs that can accomplish this task.

In this chapter, we investigate how symbolic execution can be implemented, and how it can be used to obtain interesting values for fuzzing.

```python
from bookutils import YouTubeVideo
YouTubeVideo('AJfRBF8NEWU')
```

**Prerequisites**

* You should understand how to use [type annotations](https://docs.python.org/3/library/typing.html) in Python.
* A working knowledge of [SMT solvers](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories), especially [Z3](https://github.com/Z3Prover/z3) is useful.
* You should have read the [chapter on coverage](Coverage.ipynb).
* A familiarity with [chapter on concolic fuzzing](ConcolicFuzzer.ipynb) would be helpful.

```python
# ignore
import sys
```

```python
# ignore
if sys.version_info > (3, 11):
    print("This code requires Python 3.11 or earlier")
    sys.exit(0)
```

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.SymbolicFuzzer import <identifier>
```

and then make use of the following features.


This chapter provides an implementation of a symbolic fuzzing engine `SymbolicFuzzer`. The fuzzer uses symbolic execution to exhaustively explore paths in the program to a limited depth, and generate inputs that will reach these paths.

As an example, consider the function `gcd()`, computing the greatest common divisor of `a` and `b`:

```python
def gcd(a: int, b: int) -> int:
    if a < b:
        c: int = a  # type: ignore
        a = b
        b = c

    while b != 0:
        c: int = a  # type: ignore
        a = b
        b = c % b

    return a
```
To explore `gcd()`, the fuzzer can be used as follows, producing values for arguments that cover different paths in `gcd()` (including multiple times of loop iterations):

```python
>>> gcd_fuzzer = SymbolicFuzzer(gcd, max_tries=10, max_iter=10, max_depth=10)
>>> for i in range(10):
>>>     args = gcd_fuzzer.fuzz()
>>>     print(args)
{'a': 8, 'b': 3}
{'a': 1, 'b': 2}
{'a': 2, 'b': 5}
{'a': 7, 'b': 6}
{'a': 9, 'b': 10}
{'a': 4, 'b': 4}
{'a': 23, 'b': 11}
{'a': 8, 'b': 16}
{'a': 10, 'b': 1}
{'a': 28, 'b': 9}

```
Note that the variable values returned by `fuzz()` are Z3 _symbolic_ values; to convert them to Python numbers, use their method `as_long()`:

```python
>>> for i in range(10):
>>>     args = gcd_fuzzer.fuzz()
>>>     a = args['a'].as_long()
>>>     b = args['b'].as_long()
>>>     d = gcd(a, b)
>>>     print(f"gcd({a}, {b}) = {d}")
gcd(0, 12) = 12
gcd(-1, 0) = -1
gcd(29, 17) = 1
gcd(0, 7) = 7
gcd(-2, -1) = -1
gcd(40, 8) = 8
gcd(-1, 18) = -1
gcd(3, 0) = 3
gcd(1, -2) = -1
gcd(-3, -1) = -1

```
The symbolic fuzzer is subject to a number of constraints. First, it requires that the function to be fuzzed has correct type annotations, including all local variables. Second, it solves loops by unrolling them, but only for a fixed amount.

For programs without loops and variable reassignments, the `SimpleSymbolicFuzzer` is a faster, but more limited alternative.

![](PICS/SymbolicFuzzer-synopsis-1.svg)



## Obtaining Path Conditions for Coverage

In the chapter on [parsing and recombining inputs](SearchBasedFuzzer.ipynb), we saw how difficult it was to generate inputs for `process_vehicle()` -- a simple function that accepts a string. The solution given there was to rely on preexisting sample inputs. However, this solution is inadequate as it assumes the existence of sample inputs. What if there are no sample inputs at hand?

For a simpler example, let us consider the following triangle function (which we already have seen in the [chapter on concolic fuzzing](ConcolicFuzzer.ipynb)). Can we generate inputs to cover all the paths?

*Note.* We use type annotations to denote the argument types of programs. The [chapter on discovering dynamic invariants](DynamicInvariants.ipynb) will discuss how these types can be inferred automatically.

```python
def check_triangle(a: int, b: int, c: int) -> str:
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"
```

### The Control Flow Graph

The control flow graph of this function can be represented as follows:

```python
import bookutils.setup
```

```python
import inspect
```

```python
from ControlFlow import PyCFG, to_graph, gen_cfg
```

```python
def show_cfg(fn, **kwargs):
    return to_graph(gen_cfg(inspect.getsource(fn)), **kwargs)
```

```python
show_cfg(check_triangle)
```

The possible execution paths traced by the program can be represented as follows, with the numbers indicating the specific line numbers executed.

```python
paths = {
    '<path 1>': ([1, 2, 3, 4, 5], 'Equilateral'),
    '<path 2>': ([1, 2, 3, 4, 7], 'Isosceles'),
    '<path 3>': ([1, 2, 3, 9], 'Isosceles'),
    '<path 4>': ([1, 2, 11, 12, 13], 'Isosceles'),
    '<path 5>': ([1, 2, 11, 12, 15], 'Scalene'),
    '<path 6>': ([1, 2, 11, 17], 'Isosceles'),
}
```

Consider the `<path 1>`. To trace this path, we need to execute the following statements in order.

```python
1: check_triangle(a, b, c)
2: if (a == b) -> True
3: if (a == c) -> True
4: if (b == c) -> True
5: return 'Equilateral'
```

That is, any execution that traces this path has to start with values for `a`, `b`, and `c` that obeys the constraints in line numbers `2: (a == b)` evaluates to `True`, `3: (a == c)` evaluates to `True`, and `4: (b == c)` evaluates to `True`. Can we generate inputs such that these constraints are satisfied?

We have seen from the [chapter on concolic fuzzing](ConcolicFuzzer.ipynb) how one can use an SMT solver such as Z3 to obtain a solution.

```python
import z3  # type: ignore
```

```python
z3_ver = z3.get_version()
print(z3_ver)
```

```python
assert z3_ver >= (4, 8, 6, 0), "Please check z3 version"
```

What kind of symbolic variables do we need? We can obtain that information from the type annotations of the function.

```python
def get_annotations(fn):
    sig = inspect.signature(fn)
    return ([(i.name, i.annotation)
             for i in sig.parameters.values()], sig.return_annotation)
```

```python
params, ret = get_annotations(check_triangle)
params, ret
```

We create symbolic variables to represent each of the parameters

```python
SYM_VARS = {
    int: (
        z3.Int, z3.IntVal), float: (
            z3.Real, z3.RealVal), str: (
                z3.String, z3.StringVal)}
```

```python
def get_symbolicparams(fn):
    params, ret = get_annotations(fn)
    return [SYM_VARS[typ][0](name)
            for name, typ in params], SYM_VARS[ret][0]('__return__')
```

```python
(a, b, c), r = get_symbolicparams(check_triangle)
a, b, c, r
```

We can now ask *z3* to solve the set of equations for us as follows.

```python
z3.solve(a == b, a == c, b == c)
```

Here we find the first problem in our program. Our program seems to not check whether the sides are greater than zero. (Real-world triangles all have sides with a positive length.) Assume for now that we do not have that restriction. Does our program correctly follow the path described?

We can use the `ArcCoverage` from the [chapter on concolic fuzzing](ConcolicFuzzer.ipynb) as a tracer to visualize that information as below.

```python
from ConcolicFuzzer import ArcCoverage  # minor dependency
```

First, we recover the trace.

```python
with ArcCoverage() as cov:
    assert check_triangle(0, 0, 0) == 'Equilateral'
cov._trace, cov.arcs()
```

We can now determine the path taken.

### The CFG with Path Taken

```python
show_cfg(check_triangle, arcs=cov.arcs())
```

As you can see, the path taken is `<path 1>`.

Similarly, for solving `<path 2>` we need to simply invert the condition at <line 2>:

```python
z3.solve(a == b, a == c, z3.Not(b == c))
```

The symbolic execution suggests that there is no solution. A moment's reflection will convince us that it is indeed true. Let us proceed with the other paths. The `<path 3>` can be obtained by inverting the condition at `<line 4>`.

```python
z3.solve(a == b, z3.Not(a == c))
```

```python
with ArcCoverage() as cov:
    assert check_triangle(1, 1, 0) == 'Isosceles'
[i for fn, i in cov._trace if fn == 'check_triangle']
```

```python
paths['<path 3>']
```

How about path <4>?

```python
z3.solve(z3.Not(a == b), b != c, a == c)
```

As we mentioned earlier, our program does not account for sides with zero or negative length. We can modify our program to check for zero and negative input. However, do we always have to make sure that every function has to account for all possible inputs? It is possible that the `check_triangle` is not directly exposed to the user, and it is called from another function that already guarantees that the inputs would be positive. In the [chapter on dynamic invariants](DynamicInvariants.ipynb), we will show how to discover such preconditions and post conditions.

We can easily add such a precondition here.

```python
pre_condition = z3.And(a > 0, b > 0, c > 0)
```

```python
z3.solve(pre_condition, z3.Not(a == b), b != c, a == c)
```

```python
with ArcCoverage() as cov:
    assert check_triangle(1, 2, 1) == 'Isosceles'
[i for fn, i in cov._trace if fn == 'check_triangle']
```

```python
paths['<path 4>']
```

Continuing to path <5>:

```python
z3.solve(pre_condition, z3.Not(a == b), b != c, z3.Not(a == c))
```

And indeed it is a *Scalene* triangle.

```python
with ArcCoverage() as cov:
    assert check_triangle(3, 1, 2) == 'Scalene'
```

```python
paths['<path 5>']
```

Finally, for `<path 6>` the procedure is similar.

```python
z3.solve(pre_condition, z3.Not(a == b), z3.Not(b != c))
```

```python
with ArcCoverage() as cov:
    assert check_triangle(2, 1, 1) == 'Isosceles'
[i for fn, i in cov._trace if fn == 'check_triangle']
```

```python
paths['<path 6>']
```

What if we wanted another solution? We can simply ask the solver to solve again, and not give us the same values.

```python
seen = [z3.And(a == 2, b == 1, c == 1)]
```

```python
z3.solve(pre_condition, z3.Not(z3.Or(seen)), z3.Not(a == b), z3.Not(b != c))
```

```python
seen.append(z3.And(a == 1, b == 2, c == 2))
```

```python
z3.solve(pre_condition, z3.Not(z3.Or(seen)), z3.Not(a == b), z3.Not(b != c))
```

That is, using simple symbolic computation, we were able to easily see that (1) some paths are not reachable, and (2) some conditions were insufficient -- we needed preconditions. What about the total coverage obtained?

### Visualizing the Coverage

Visualizing the statement coverage can be accomplished as below.

```python
class VisualizedArcCoverage(ArcCoverage):
    def show_coverage(self, fn):
        src = fn if isinstance(fn, str) else inspect.getsource(fn)
        covered = set([lineno for method, lineno in self._trace])
        for i, s in enumerate(src.split('\n')):
            print('%s %2d: %s' % ('#' if i + 1 in covered else ' ', i + 1, s))
```

We run all the inputs obtained under the coverage tracer.

```python
with VisualizedArcCoverage() as cov:
    assert check_triangle(0, 0, 0) == 'Equilateral'
    assert check_triangle(1, 1, 0) == 'Isosceles'
    assert check_triangle(1, 2, 1) == 'Isosceles'
    assert check_triangle(3, 1, 2) == 'Scalene'
    assert check_triangle(2, 1, 1) == 'Isosceles'
```

```python
cov.show_coverage(check_triangle)
```

The coverage is as expected. The generated values do seem to cover all code that can be covered.

We have seen how to reason about each path through the program. Can we combine them together to produce a single expression that represents the program behavior? This is what we will discuss next.

### Function Summaries

Consider this equation for determining absolute value.

```python
def abs_value(x: float) -> float:
    if x < 0:
        v: float = -x  # type: ignore
    else:
        v: float = x  # type: ignore
    return v
```

```python
show_cfg(abs_value)
```

What can we say about the value of `v` at `line: 5`? Let us trace and see. First, we have variable `x` at `line: 1`.

```python
(x,), r = get_symbolicparams(abs_value)
```

At `line: 2`, we face a bifurcation in the possible paths. Hence, we produce two paths with corresponding constraints.

```python
l2_T = x < 0
l2_F = z3.Not(x < 0)
```

For `line: 3`, we only need to consider the `If` path. However, we have an assignment. So we use a new variable here. The type _float_ is indicated in the source, and its equivalent *z3* type is _Real_.

```python
v_0 = z3.Real('v_0')
l3 = z3.And(l2_T, v_0 == -x)
```

Similarly, for `line: 5`, we have an assignment. (Can we reuse the variable `v_0` from before?)

```python
v_1 = z3.Real('v_1')
l5 = z3.And(l2_F, v_1 == x)
```

When we come to `line: 6`, we see that we have *two* input streams. We have a choice. We can either keep each path separate as we did previously.

```python
v = z3.Real('v')
for s in [z3.And(l3, v == v_0), z3.And(l5, v == v_1)]:
    z3.solve(x != 0, s)
```

Or, we can combine them together and produce a single predicate at `line: 6`.

```python
v = z3.Real('v')
l6 = z3.Or(z3.And(l3, v == v_0), z3.And(l5, v == v_1))
z3.solve(l6)
```

**Note.** Merging two incoming streams of execution can be non-trivial, especially when the execution paths are traversed multiple times (E.g. loops and recursion). For those interested, lookup [inferring loop invariants](https://www.st.cs.uni-saarland.de/publications/details/galeotti-hvc-2014/).

We can get this to produce any number of solutions for `abs()` as below.

```python
s = z3.Solver()
s.add(l6)
for i in range(5):
    if s.check() == z3.sat:
        m = s.model()
        x_val = m[x]
        print(m)
    else:
        print('no solution')
        break
    s.add(z3.Not(x == x_val))
s
```

The solver is not particularly random. So we need to help it a bit to produce values on the negative range.

```python
s.add(x < 0)
for i in range(5):
    if s.check() == z3.sat:
        m = s.model()
        x_val = m[x]
        print(m)
    else:
        print('no solution')
        break
    s.add(z3.Not(x == x_val))
```

```python
s
```

Note that the single expression produced at `line: 6` is essentially a summary for `abs_value()`. 

```python
abs_value_summary = l6
abs_value_summary
```

The *z3* solver can be used to simplify the predicates where possible.

```python
z3.simplify(l6)
```

One can use this summary rather than trace into `abs_value()` when `abs_value()` is used elsewhere. However, that presents us with a problem. It is possible that the same function may be called multiple times. In this case, using the same variables will lead to collision. One way to avoid that is to *prefix* some call specific value to the variables.

**Note:** The SMT 2.0 standard allows one to define functions (*macros* in SMT parlance) directly. For example, the `abs-value` will be defined as follows:

```lisp
(define-fun abs-value ((x Int)) Int
       (if (> x 0)
           x
           (* -1 x)))
```

Or equivalently, (especially if `abs-value` is recursively defined)

```lisp
(declare-fun abs-value (Int) Int)
(assert (forall ((x Int))
                (= (abs-value x)
                   (if (> x 0)
                       x
                       (* -1 x)))))
```
One can then say
```
(> (abs-value x) (abs-value y))
```

Unfortunately, the z3py project does not expose this facility in Python. Hence, we have to use the `prefix_vars()` hack.

```python
import ast
```

The method `prefix_vars()` modifies the variables in an expression such that the variables are prefixed with a given value.

```python
def prefix_vars(astnode, prefix):
    if isinstance(astnode, ast.BoolOp):
        return ast.BoolOp(astnode.op,
                          [prefix_vars(i, prefix) for i in astnode.values], [])
    elif isinstance(astnode, ast.BinOp):
        return ast.BinOp(
            prefix_vars(astnode.left, prefix), astnode.op,
            prefix_vars(astnode.right, prefix))
    elif isinstance(astnode, ast.UnaryOp):
        return ast.UnaryOp(astnode.op, prefix_vars(astnode.operand, prefix))
    elif isinstance(astnode, ast.Call):
        return ast.Call(prefix_vars(astnode.func, prefix),
                        [prefix_vars(i, prefix) for i in astnode.args],
                        astnode.keywords)
    elif isinstance(astnode, ast.Compare):
        return ast.Compare(
            prefix_vars(astnode.left, prefix), astnode.ops,
            [prefix_vars(i, prefix) for i in astnode.comparators])
    elif isinstance(astnode, ast.Name):
        if astnode.id in {'And', 'Or', 'Not'}:
            return ast.Name('z3.%s' % (astnode.id), astnode.ctx)
        else:
            return ast.Name('%s%s' % (prefix, astnode.id), astnode.ctx)
    elif isinstance(astnode, ast.Return):
        return ast.Return(prefix_vars(astnode.value, env))
    else:
        return astnode
```

For applying `prefix_vars()` one needs the _abstract syntax tree_ (AST) of the Python expression involved. We obtain this by invoking `ast.parse()`:

```python
xy_ast = ast.parse('x+y')
```

We can visualize the resulting tree as follows:

```python
from bookutils import rich_output
```

```python
if rich_output():
    # Normally, this will do
    from showast import show_ast
else:
    def show_ast(tree):
        ast.dump(tree, indent=4)
```

```python
show_ast(xy_ast)
```

What the visualization does _not_ show, though, is that when parsing Python source code, the resulting AST comes wrapped in a `Module` by default:

```python
xy_ast
```

And to access the expression (`Expr`), we need to access the first child of that "module":

```python
xy_ast.body[0]
```

The actual expression is within that `Expr` object:

```python
xy_ast.body[0].value  # type: ignore
```

Hence, for easier manipulation of an expression AST, we define a function `get_expression()` which unwraps it and returns the AST representation of the expression inside.

```python
def get_expression(src):
    return ast.parse(src).body[0].value
```

It is used as follows:

```python
e = get_expression('x+y')
e
```

The function `to_src()` allows us to *unparse* an expression.

```python
def to_src(astnode):
    return ast.unparse(astnode).strip()
```

It is used as follows:

```python
to_src(e)
```

We can combine both pieces to produce a prefixed expression. Let us prefix all variables with `x1_`:

```python
abs_value_summary_ast = get_expression(str(abs_value_summary))
print(to_src(prefix_vars(abs_value_summary_ast, 'x1_')))
```

#### Get Names and Types of Variables Used

What about the declarations used? Given that we have all equations in *Z3*, we can retrieve this information directly. We define `z3_names_and_types()` that takes in a *Z3* expression, and extracts the variable definitions required.

```python
def z3_names_and_types(z3_ast):
    hm = {}
    children = z3_ast.children()
    if children:
        for c in children:
            hm.update(z3_names_and_types(c))
    else:
        # HACK.. How else to distinguish literals and vars?
        if (str(z3_ast.decl()) != str(z3_ast.sort())):
            hm["%s" % str(z3_ast.decl())] = 'z3.%s' % str(z3_ast.sort())
        else:
            pass
    return hm
```

```python
abs_value_declarations = z3_names_and_types(abs_value_summary)
abs_value_declarations
```

However, `z3_names_and_types()` is limited in that it requires the *Z3* AST to operate. Hence, we also define `used_identifiers()` that can extract identifiers directly from the string representation of any Python expression, (including *Z3* constraints). One trade-off here is that we lose track of the type information. But we will see how to recover that later.

```python
def used_identifiers(src):
    def names(astnode):
        lst = []
        if isinstance(astnode, ast.BoolOp):
            for i in astnode.values:
                lst.extend(names(i))
        elif isinstance(astnode, ast.BinOp):
            lst.extend(names(astnode.left))
            lst.extend(names(astnode.right))
        elif isinstance(astnode, ast.UnaryOp):
            lst.extend(names(astnode.operand))
        elif isinstance(astnode, ast.Call):
            for i in astnode.args:
                lst.extend(names(i))
        elif isinstance(astnode, ast.Compare):
            lst.extend(names(astnode.left))
            for i in astnode.comparators:
                lst.extend(names(i))
        elif isinstance(astnode, ast.Name):
            lst.append(astnode.id)
        elif isinstance(astnode, ast.Expr):
            lst.extend(names(astnode.value))
        elif isinstance(astnode, (ast.Num, ast.Str, ast.Tuple, ast.NameConstant)):
            pass
        elif isinstance(astnode, ast.Assign):
            for t in astnode.targets:
                lst.extend(names(t))
            lst.extend(names(astnode.value))
        elif isinstance(astnode, ast.Module):
            for b in astnode.body:
                lst.extend(names(b))
        else:
            raise Exception(str(astnode))
        return list(set(lst))
    return names(ast.parse(src))
```

```python
used_identifiers(str(abs_value_summary))
```

We can now register the function summary `abs_value` for later use.

```python
function_summaries = {}
function_summaries['abs_value'] = {
    'predicate': str(abs_value_summary),
    'vars': abs_value_declarations}
```

As we mentioned previously, we do not want to rely on *Z3* to extract the type information. A better alternative is to let the user specify the type information as annotations, and extract this information from the program. We will see next how this can be achieved.

First, we convert the *Python type to Z3 type* map to its string equivalent.

```python
SYM_VARS_STR = {
    k.__name__: ("z3.%s" % v1.__name__, "z3.%s" % v2.__name__)
    for k, (v1, v2) in SYM_VARS.items()
}
SYM_VARS_STR
```

We also define a convenience method `translate_to_z3_name()` for accessing the *Z3* type for symbolic variables.

```python
def translate_to_z3_name(v):
    return SYM_VARS_STR[v][0]
```

We now define the method `declarations()` that extracts variables used in Python _statements_. The idea is to look for augmented assignments that contain annotated type information. These are collected and returned.

If there are `call` nodes, they represent function calls. The used variables in these function calls are recovered from the corresponding function summaries.

```python
def declarations(astnode, hm=None):
    if hm is None:
        hm = {}
    if isinstance(astnode, ast.Module):
        for b in astnode.body:
            declarations(b, hm)
    elif isinstance(astnode, ast.FunctionDef):
        # hm[astnode.name + '__return__'] = \
        # translate_to_z3_name(astnode.returns.id)
        for a in astnode.args.args:
            hm[a.arg] = translate_to_z3_name(a.annotation.id)
        for b in astnode.body:
            declarations(b, hm)
    elif isinstance(astnode, ast.Call):
        # get declarations from the function summary.
        n = astnode.function
        assert isinstance(n, ast.Name)  # for now.
        name = n.id
        hm.update(dict(function_summaries[name]['vars']))
    elif isinstance(astnode, ast.AnnAssign):
        assert isinstance(astnode.target, ast.Name)
        hm[astnode.target.id] = translate_to_z3_name(astnode.annotation.id)
    elif isinstance(astnode, ast.Assign):
        # verify it is already defined
        for t in astnode.targets:
            assert isinstance(t, ast.Name)
            assert t.id in hm
    elif isinstance(astnode, ast.AugAssign):
        assert isinstance(astnode.target, ast.Name)
        assert astnode.target.id in hm
    elif isinstance(astnode, (ast.If, ast.For, ast.While)):
        for b in astnode.body:
            declarations(b, hm)
        for b in astnode.orelse:
            declarations(b, hm)
    elif isinstance(astnode, ast.Return):
        pass
    else:
        raise Exception(str(astnode))
    return hm
```

With this, we can now extract the variables used in an expression.

```python
declarations(ast.parse('s: int = 3\np: float = 4.0\ns += 1'))
```

We wrap `declarations()` in the method `used_vars()` that operates directly on function objects.

```python
def used_vars(fn):
    return declarations(ast.parse(inspect.getsource(fn)))
```

Here is how it can be used:

```python
used_vars(check_triangle)
```

```python
used_vars(abs_value)
```

Given the extracted variables and their *Z3* types, we need a way to re-instantiate them when needed. We define `define_symbolic_vars()` that translates these descriptions to a form that can be directly `exec()`ed.

```python
def define_symbolic_vars(fn_vars, prefix):
    sym_var_dec = ', '.join([prefix + n for n in fn_vars])
    sym_var_def = ', '.join(["%s('%s%s')" % (t, prefix, n)
                             for n, t in fn_vars.items()])
    return "%s = %s" % (sym_var_dec, sym_var_def)
```

Here is how it can be used:

```python
define_symbolic_vars(abs_value_declarations, '')
```

We next define `gen_fn_summary()` that returns a function summary in instantiable form using *Z3*. 

```python
def gen_fn_summary(prefix, fn):
    summary = function_summaries[fn.__name__]['predicate']
    fn_vars = function_summaries[fn.__name__]['vars']
    decl = define_symbolic_vars(fn_vars, prefix)
    summary_ast = get_expression(summary)
    return decl, to_src(prefix_vars(summary_ast, prefix))
```

Here is how it can be used:

```python
gen_fn_summary('a_', abs_value)
```

```python
gen_fn_summary('b_', abs_value)
```

How do we use our function summaries? Here is a function `abs_max()` that uses `abs_value()`.

```python
def abs_max(a: float, b: float):
    a1: float = abs_value(a)
    b1: float = abs_value(b)
    if a1 > b1:
        c: float = a1  # type: ignore
    else:
        c: float = b1  # type: ignore
    return c
```

To trace this function symbolically, we first define the two variables `a` and `b`.

```python
a = z3.Real('a')
b = z3.Real('b')
```

The `line: 2` contains definition for `a1`, which we define as a symbolic variable.

```python
a1 = z3.Real('a1')
```

We also need to call `abs_value()`, which is accomplished as follows. Since this is the first call to `abs_value()`, we use `abs1` as the prefix.

```python
d, v = gen_fn_summary('abs1_', abs_value)
d, v
```

We also need to equate the resulting value (`<prefix>_v`) to the symbolic variable `a1` we defined earlier.

```python
l2_src = "l2 = z3.And(a == abs1_x, a1 == abs1_v, %s)" % v
l2_src
```

Applying both declaration and the assignment.

```python
exec(d)
exec(l2_src)
```

```python
l2  # type: ignore
```

We need to do the same for `line: 3`, but with `abs2` as the prefix.

```python
b1 = z3.Real('b1')
d, v = gen_fn_summary('abs2_', abs_value)
l3_src = "l3_ = z3.And(b == abs2_x, b1 == abs2_v, %s)" % v
exec(d)
exec(l3_src)
```

```python
l3_  # type: ignore
```

To get the true set of predicates at `line: 3`, we need to add the predicates from `line: 2`.

```python
l3 = z3.And(l2, l3_)  # type: ignore
```

```python
l3
```

This equation can be simplified a bit using z3.

```python
z3.simplify(l3)
```

Coming to `line: 4`, we have a condition.

```python
l4_cond = a1 > b1
l4 = z3.And(l3, l4_cond)
```

For `line: 5`, we define the symbolic variable `c_0` assuming we took the *IF* branch.

```python
c_0 = z3.Real('c_0')
l5 = z3.And(l4, c_0 == a1)
```

For `line: 6`, the *ELSE* branch was taken. So we invert that condition.

```python
l6 = z3.And(l3, z3.Not(l4_cond))
```

For `line: 7`, we define `c_1`.

```python
c_1 = z3.Real('c_1')
l7 = z3.And(l6, c_1 == b1)
```

```python
s1 = z3.Solver()
s1.add(l5)
s1.check()
```

```python
m1 = s1.model()
sorted([(d, m1[d]) for d in m1.decls() if not d.name(
).startswith('abs')], key=lambda x: x[0].name())
```

```python
s2 = z3.Solver()
s2.add(l7)
s2.check()
```

```python
m2 = s2.model()
sorted([(d, m2[d]) for d in m2.decls() if not d.name(
).startswith('abs')], key=lambda x: x[0].name())
```

What we really want to do is to automate this process, because doing this by hand is tedious and error-prone. Essentially, we want the ability to extract *all paths* in the program, and symbolically execute each path, which will generate the inputs required to cover all reachable portions of the program.

## Simple Symbolic Fuzzing

We define a simple *symbolic fuzzer* that can generate input values *symbolically* with the following assumptions:

* There are no loops in the program
* The function is self-contained.
* No recursion.
* No reassignments for variables.

The key idea is as follows: We traverse through the control flow graph from the entry point, and generate all possible paths to a given depth. Then we collect constraints that we encountered along the path, and generate inputs that will traverse the program up to that point.

We build our fuzzer based on the class `Fuzzer`.

```python
from Fuzzer import Fuzzer
```

We start by extracting the control flow graph of the function passed. We also provide a hook for child classes to do their processing.

```python
class SimpleSymbolicFuzzer(Fuzzer):
    """Simple symbolic fuzzer"""

    def __init__(self, fn, **kwargs):
        """Constructor.
        `fn` is the function to be fuzzed.
        Possible keyword parameters:
        * `max_depth` - the depth to which one should attempt
          to trace the execution (default 100) 
        * `max_tries` - the maximum number of attempts
          we will try to produce a value before giving up (default 100)
        * `max_iter` - the number of iterations we will attempt (default 100).
        """
        self.fn_name = fn.__name__
        py_cfg = PyCFG()
        py_cfg.gen_cfg(inspect.getsource(fn))
        self.fnenter, self.fnexit = py_cfg.functions[self.fn_name]
        self.used_variables = used_vars(fn)
        self.fn_args = list(inspect.signature(fn).parameters)
        self.z3 = z3.Solver()

        self.paths = None
        self.last_path = None

        self.options(kwargs)
        self.process()

    def process(self):
        ...  # to be defined later
```

We need a few variables to control how much we are willing to traverse.

`MAX_DEPTH` is the depth to which one should attempt to trace the execution.

```python
MAX_DEPTH = 100
```

`MAX_TRIES` is the maximum number of attempts we will try to produce a value before giving up.

```python
MAX_TRIES = 100
```

`MAX_ITER` is the number of iterations we will attempt.

```python
MAX_ITER = 100
```

The `options()` method sets these parameters in the fuzzing class.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def options(self, kwargs):
        self.max_depth = kwargs.get('max_depth', MAX_DEPTH)
        self.max_tries = kwargs.get('max_tries', MAX_TRIES)
        self.max_iter = kwargs.get('max_iter', MAX_ITER)
        self._options = kwargs
```

The initialization generates a control flow graph and hooks it to `fnenter` and `fnexit`.

```python
symfz_ct = SimpleSymbolicFuzzer(check_triangle)
```

```python
symfz_ct.fnenter, symfz_ct.fnexit
```

### Generating All Possible Paths
We can use the procedure `get_all_paths()` starting from `fnenter` to recursively retrieve all paths in the function.

The idea is as follows: Start with the function entry point `fnenter`, and recursively follow the children using the CFG. At any node there is a branching, there would be multiple children. On other nodes there would be only one child. Let us say a node had $n$ children. Such a node would result in $n$ paths. We attach the current node to the head of each path, and return all paths thus generated.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def get_all_paths(self, fenter, depth=0):
        if depth > self.max_depth:
            raise Exception('Maximum depth exceeded')
        if not fenter.children:
            return [[(0, fenter)]]

        fnpaths = []
        for idx, child in enumerate(fenter.children):
            child_paths = self.get_all_paths(child, depth + 1)
            for path in child_paths:
                # In a conditional branch, idx is 0 for IF, and 1 for Else
                fnpaths.append([(idx, fenter)] + path)
        return fnpaths
```

This can be used as follows.

```python
symfz_ct = SimpleSymbolicFuzzer(check_triangle)
all_paths = symfz_ct.get_all_paths(symfz_ct.fnenter)
```

```python
len(all_paths)
```

```python
all_paths[1]
```

We hook `get_all_paths()` to initialization as below.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def process(self):
        self.paths = self.get_all_paths(self.fnenter)
        self.last_path = len(self.paths)
```

### Extracting All Constraints

For any given path, we define a function `extract_constraints()` to extract the constraints such that they are executable directly with *Z3*. The `idx` represents the particular branch that was taken. Hence, if the `False` branch was taken in a conditional, we attach a negation of the conditional.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def extract_constraints(self, path):
        predicates = []
        for (idx, elt) in path:
            if isinstance(elt.ast_node, ast.AnnAssign):
                if elt.ast_node.target.id in {'_if', '_while'}:
                    s = to_src(elt.ast_node.annotation)
                    predicates.append(("%s" if idx == 0 else "z3.Not(%s)") % s)
                elif isinstance(elt.ast_node.annotation, ast.Call):
                    assert elt.ast_node.annotation.func.id == self.fn_name
                else:
                    node = elt.ast_node
                    t = ast.Compare(node.target, [ast.Eq()], [node.value])
                    predicates.append(to_src(t))
            elif isinstance(elt.ast_node, ast.Assign):
                node = elt.ast_node
                t = ast.Compare(node.targets[0], [ast.Eq()], [node.value])
                predicates.append(to_src(t))
            else:
                pass
        return predicates
```

```python
symfz_ct = SimpleSymbolicFuzzer(check_triangle)
all_paths = symfz_ct.get_all_paths(symfz_ct.fnenter)
symfz_ct.extract_constraints(all_paths[0])
```

```python
constraints = symfz_ct.extract_constraints(all_paths[1])
constraints
```

### Fuzzing with Simple Symbolic Fuzzer

To actually generate solutions, we define `fuzz()`. For that, we need to first extract all paths. Then choose a particular path, and extract the constraints in that path, which is then solved using *z3*.

```python
from contextlib import contextmanager
```

First we create a checkpoint for our current solver so that we can check a predicate, and rollback if necessary.

```python
@contextmanager
def checkpoint(z3solver):
    z3solver.push()
    yield z3solver
    z3solver.pop()
```

The `use_path()` function extracts constraints for a single function, applies it to our current solver (under a checkpoint), and returns the results if some solutions can be found.
If solutions were found, we also make sure that we never reuse those solutions.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def solve_path_constraint(self, path):
        # re-initializing does not seem problematic.
        # a = z3.Int('a').get_id() remains the same.
        constraints = self.extract_constraints(path)
        decl = define_symbolic_vars(self.used_variables, '')
        exec(decl)

        solutions = {}
        with checkpoint(self.z3):
            st = 'self.z3.add(%s)' % ', '.join(constraints)
            eval(st)
            if self.z3.check() != z3.sat:
                return {}
            m = self.z3.model()
            solutions = {d.name(): m[d] for d in m.decls()}
            my_args = {k: solutions.get(k, None) for k in self.fn_args}
        predicate = 'z3.And(%s)' % ','.join(
            ["%s == %s" % (k, v) for k, v in my_args.items()])
        eval('self.z3.add(z3.Not(%s))' % predicate)
        return my_args
```

We define `get_path()` that retrieves the current path and updates the path used.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def get_next_path(self):
        self.last_path -= 1
        if self.last_path == -1:
            self.last_path = len(self.paths) - 1
        return self.paths[self.last_path]
```

The `fuzz()` method simply solves each path in order.

```python
class SimpleSymbolicFuzzer(SimpleSymbolicFuzzer):
    def fuzz(self):
        """Produce one solution for each path.
        Returns a mapping of variable names to (symbolic) Z3 values."""
        for i in range(self.max_tries):
            res = self.solve_path_constraint(self.get_next_path())
            if res:
                return res

        return {}
```

The fuzzer can be used as follows. Note that we need to convert the symbolic variables returned to Python numbers, using `as_long()`:

```python
a, b, c = None, None, None
symfz_ct = SimpleSymbolicFuzzer(check_triangle)
for i in range(1, 10):
    args = symfz_ct.fuzz()
    res = check_triangle(args['a'].as_long(),
                         args['b'].as_long(),
                         args['c'].as_long())
    print(args, "result:", res)
```

For symbolic fractions, we access their numerators and denominators:

```python
symfz_av = SimpleSymbolicFuzzer(abs_value)
for i in range(1, 10):
    args = symfz_av.fuzz()
    abs_res = abs_value(args['x'].numerator_as_long() /
                        args['x'].denominator_as_long())
    print(args, "result:", abs_res)
```

The _SimpleSymbolicFuzzer_ seems to work well for the _simple_ programs we checked above.

### Problems with the Simple Fuzzer

As we mentioned earlier, the `SimpleSymbolicFuzzer` cannot yet deal with variable reassignments. Further, it also fails to account for any loops. For example, consider the following program.

```python
def gcd(a: int, b: int) -> int:
    if a < b:
        c: int = a  # type: ignore
        a = b
        b = c

    while b != 0:
        c: int = a  # type: ignore
        a = b
        b = c % b

    return a
```

```python
show_cfg(gcd)
```

```python
from ExpectError import ExpectError
```

```python
with ExpectError():
    symfz_gcd = SimpleSymbolicFuzzer(gcd, max_depth=1000, max_iter=10)
    for i in range(1, 100):
        r = symfz_gcd.fuzz()
        v = gcd(r['a'].as_long(), r['b'].as_long())
        print(r, v)
```

The problem here is that our *SimpleSymbolicFuzzer* has no concept of loops and variable reassignments. We will see how to fix this shortcoming next.

## Advanced Symbolic Fuzzing

We next define `SymbolicFuzzer` that can deal with reassignments and *unrolling of loops*.

```python
class SymbolicFuzzer(SimpleSymbolicFuzzer):
    """Symbolic fuzzing with reassignments and loop unrolling"""

    def options(self, kwargs):
        super().options(kwargs)
```

Once we allow reassignments and loop unrolling, we have to deal with what to call the new variables generated. This is what we will tackle next.

### Dealing with Reassignments

We want to rename all variables present in an expression such that the variables are annotated with their usage count. This makes it possible to determine variable reassignments.  To do that, we define the `rename_variables()` function that, when given an `env` that contains the current usage index of different variables, renames the variables in the passed AST node with the annotations, and returns a copy with the modifications. Note that we can't use [NodeTransformer](https://docs.python.org/3/library/ast.html#ast.NodeTransformer) here as it would modify the AST.

That is, if the expression is `env[v] == 1`, `v` is renamed to `_v_1`

```python
def rename_variables(astnode, env):
    if isinstance(astnode, ast.BoolOp):
        fn = 'z3.And' if isinstance(astnode.op, ast.And) else 'z3.Or'
        return ast.Call(
            ast.Name(fn, None),
            [rename_variables(i, env) for i in astnode.values], [])
    elif isinstance(astnode, ast.BinOp):
        return ast.BinOp(
            rename_variables(astnode.left, env), astnode.op,
            rename_variables(astnode.right, env))
    elif isinstance(astnode, ast.UnaryOp):
        if isinstance(astnode.op, ast.Not):
            return ast.Call(
                ast.Name('z3.Not', None),
                [rename_variables(astnode.operand, env)], [])
        else:
            return ast.UnaryOp(astnode.op,
                               rename_variables(astnode.operand, env))
    elif isinstance(astnode, ast.Call):
        return ast.Call(astnode.func,
                        [rename_variables(i, env) for i in astnode.args],
                        astnode.keywords)
    elif isinstance(astnode, ast.Compare):
        return ast.Compare(
            rename_variables(astnode.left, env), astnode.ops,
            [rename_variables(i, env) for i in astnode.comparators])
    elif isinstance(astnode, ast.Name):
        if astnode.id not in env:
            env[astnode.id] = 0
        num = env[astnode.id]
        return ast.Name('_%s_%d' % (astnode.id, num), astnode.ctx)
    elif isinstance(astnode, ast.Return):
        return ast.Return(rename_variables(astnode.value, env))
    else:
        return astnode
```

To verify that it works as intended, we start with an environment.

```python
env = {'x': 1}
```

```python
ba = get_expression('x == 1 and y == 2')
type(ba)
```

```python
assert to_src(rename_variables(ba, env)) == 'z3.And(_x_1 == 1, _y_0 == 2)'
```

```python
bo = get_expression('x == 1 or y == 2')
type(bo.op)
```

```python
assert to_src(rename_variables(bo, env)) == 'z3.Or(_x_1 == 1, _y_0 == 2)'
```

```python
b = get_expression('x + y')
type(b)
```

```python
assert to_src(rename_variables(b, env)) == '_x_1 + _y_0'
```

```python
u = get_expression('-y')
type(u)
```

```python
assert to_src(rename_variables(u, env)) == '-_y_0'
```

```python
un = get_expression('not y')
type(un.op)
```

```python
assert to_src(rename_variables(un, env)) == 'z3.Not(_y_0)'
```

```python
c = get_expression('x == y')
type(c)
```

```python
assert to_src(rename_variables(c, env)) == '_x_1 == _y_0'
```

```python
f = get_expression('fn(x,y)')
type(f)
```

```python
assert to_src(rename_variables(f, env)) == 'fn(_x_1, _y_0)'
```

```python
env
```

Next, we want to process the CFG, and correctly transform the paths.

### Tracking Assignments

For keeping track of assignments in the CFG, We define a data structure `PNode` that stores the current CFG node.

```python
class PNode:
    def __init__(self, idx, cfgnode, parent=None, order=0, seen=None):
        self.seen = {} if seen is None else seen
        self.max_iter = MAX_ITER
        self.idx, self.cfgnode, self.parent, self.order = idx, cfgnode, parent, order

    def __repr__(self):
        return "PNode:%d[%s order:%d]" % (self.idx, str(self.cfgnode),
                                          self.order)
```

Defining a new `PNode` is done as follows.

```python
cfg = PyCFG()
cfg.gen_cfg(inspect.getsource(gcd))
gcd_fnenter, _ = cfg.functions['gcd']
```

```python
PNode(0, gcd_fnenter)
```

The `copy()` method generates a copy for the child's keep, indicating which path was taken (with `order` of the child).

```python
class PNode(PNode):
    def copy(self, order):
        p = PNode(self.idx, self.cfgnode, self.parent, order, self.seen)
        assert p.order == order
        return p
```

Using the copy operation.

```python
PNode(0, gcd_fnenter).copy(1)
```

#### Stepwise Exploration of Paths

A problem we had with our `SimpleSymbolicFuzzer` is that it explored a path to completion before attempting another. However, this is non-optimal. One may want to explore the graph in a more step-wise manner, expanding every possible execution one step at a time.

Hence, we define `explore()` which explores the children of a node if any, one step at a time. If done exhaustively, this will generate all paths from a starting node until no more children are left. We made `PNode` to a container class so that this iteration can be driven from outside, and stopped if say a maximum iteration is complete, or certain paths need to be prioritized.

```python
class PNode(PNode):
    def explore(self):
        ret = []
        for (i, n) in enumerate(self.cfgnode.children):
            key = "[%d]%s" % (self.idx + 1, n)
            ccount = self.seen.get(key, 0)
            if ccount > self.max_iter:
                continue  # drop this child
            self.seen[key] = ccount + 1
            pn = PNode(self.idx + 1, n, self.copy(i), seen=self.seen)
            ret.append(pn)
        return ret
```

We can use `explore()` as follows.

```python
PNode(0, gcd_fnenter).explore()
```

```python
PNode(0, gcd_fnenter).explore()[0].explore()
```

The method `get_path_to_root()` recursively goes up through child->parent chain retrieving the complete chain to the topmost parent.

```python
class PNode(PNode):
    def get_path_to_root(self):
        path = []
        n = self
        while n:
            path.append(n)
            n = n.parent
        return list(reversed(path))
```

```python
p = PNode(0, gcd_fnenter)
[s.get_path_to_root() for s in p.explore()[0].explore()[0].explore()[0].explore()]
```

The string representation of the node is in `z3` solvable form.

```python
class PNode(PNode):
    def __str__(self):
        path = self.get_path_to_root()
        ssa_path = to_single_assignment_predicates(path)
        return ', '.join([to_src(p) for p in ssa_path])
```

However, before using it, we need to take care of variable renaming so that reassignments can work.

#### Renaming Used Variables

We need to rename used variables. Any variable `v = xxx` should be renamed to `_v_0` and any later assignment such as `v = v + 1` should be transformed to `_v_1 = _v_0 + 1` and later conditionals such as `v == x` should be transformed to `(_v_1 == _x_0)`. The method `to_single_assignment_predicates()` does this for a given path.

```python
def to_single_assignment_predicates(path):
    env = {}
    new_path = []
    for i, node in enumerate(path):
        ast_node = node.cfgnode.ast_node
        new_node = None
        if isinstance(ast_node, ast.AnnAssign) and ast_node.target.id in {
                'exit'}:
            new_node = None
        elif isinstance(ast_node, ast.AnnAssign) and ast_node.target.id in {'enter'}:
            args = [
                ast.parse(
                    "%s == _%s_0" %
                    (a.id, a.id)).body[0].value for a in ast_node.annotation.args]
            new_node = ast.Call(ast.Name('z3.And', None), args, [])
        elif isinstance(ast_node, ast.AnnAssign) and ast_node.target.id in {'_if', '_while'}:
            new_node = rename_variables(ast_node.annotation, env)
            if node.order != 0:
                assert node.order == 1
                new_node = ast.Call(ast.Name('z3.Not', None), [new_node], [])
        elif isinstance(ast_node, ast.AnnAssign):
            assigned = ast_node.target.id
            val = [rename_variables(ast_node.value, env)]
            env[assigned] = 0 if assigned not in env else env[assigned] + 1
            target = ast.Name('_%s_%d' %
                              (ast_node.target.id, env[assigned]), None)
            new_node = ast.Expr(ast.Compare(target, [ast.Eq()], val))
        elif isinstance(ast_node, ast.Assign):
            assigned = ast_node.targets[0].id
            val = [rename_variables(ast_node.value, env)]
            env[assigned] = 0 if assigned not in env else env[assigned] + 1
            target = ast.Name('_%s_%d' %
                              (ast_node.targets[0].id, env[assigned]), None)
            new_node = ast.Expr(ast.Compare(target, [ast.Eq()], val))
        elif isinstance(ast_node, (ast.Return, ast.Pass)):
            new_node = None
        else:
            s = "NI %s %s" % (type(ast_node), ast_node.target.id)
            raise Exception(s)
        new_path.append(new_node)
    return new_path
```

Here is how it can be used:

```python
p = PNode(0, gcd_fnenter)
path = p.explore()[0].explore()[0].explore()[0].get_path_to_root()
spath = to_single_assignment_predicates(path)
```

```python
[to_src(s) for s in spath]
```

#### Check Before You Loop

One of the ways in which the *concolic* execution simplifies *symbolic* execution is in the treatment of loops. Rather than trying to determine an invariant for a loop, we simply _unroll_ the loops a number of times until we hit the `MAX_DEPTH` limit.
However, not all loops will need to be unrolled until `MAX_DEPTH` is reached. Some of them may exit before. Hence, it is necessary to check whether the given set of constraints can be satisfied before continuing to explore further. 

```python
def identifiers_with_types(identifiers, defined):
    with_types = dict(defined)
    for i in identifiers:
        if i[0] == '_':
            nxt = i[1:].find('_', 1)
            name = i[1:nxt + 1]
            assert name in defined
            typ = defined[name]
            with_types[i] = typ
    return with_types
```

The `extract_constraints()` generates the `z3` constraints from a path. The main work is done by `to_single_assignment_predicates()`. The `extract_constraints()` then converts the AST to source.

```python
class SymbolicFuzzer(SymbolicFuzzer):
    def extract_constraints(self, path):
        return [to_src(p) for p in to_single_assignment_predicates(path) if p]
```

### Solving Path Constraints

We now update our `solve_path_constraint()` method to take into account the new identifiers created during reassignments.

```python
class SymbolicFuzzer(SymbolicFuzzer):
    def solve_path_constraint(self, path):
        # re-initializing does not seem problematic.
        # a = z3.Int('a').get_id() remains the same.
        constraints = self.extract_constraints(path)
        identifiers = [
            c for i in constraints for c in used_identifiers(i)]  # <- changes
        with_types = identifiers_with_types(
            identifiers, self.used_variables)  # <- changes
        decl = define_symbolic_vars(with_types, '')
        exec(decl)

        solutions = {}
        with checkpoint(self.z3):
            st = 'self.z3.add(%s)' % ', '.join(constraints)
            eval(st)
            if self.z3.check() != z3.sat:
                return {}
            m = self.z3.model()
            solutions = {d.name(): m[d] for d in m.decls()}
            my_args = {k: solutions.get(k, None) for k in self.fn_args}

        predicate = 'z3.And(%s)' % ','.join(
            ["%s == %s" % (k, v) for k, v in my_args.items()])
        eval('self.z3.add(z3.Not(%s))' % predicate)

        return my_args
```

### Generating All Paths

The `get_all_paths()` is now similarly updated so that we unroll loops only to a specified height. It is also converted to an iterative exploration style so that we explore the CFG in a breadth first manner.

```python
class SymbolicFuzzer(SymbolicFuzzer):
    def get_all_paths(self, fenter):
        path_lst = [PNode(0, fenter)]
        completed = []
        for i in range(self.max_iter):
            new_paths = [PNode(0, fenter)]
            for path in path_lst:
                # explore each path once
                if path.cfgnode.children:
                    np = path.explore()
                    for p in np:
                        if path.idx > self.max_depth:
                            break
                        new_paths.append(p)
                else:
                    completed.append(path)
            path_lst = new_paths
        return completed + path_lst
```

We can now obtain all paths using our advanced symbolic fuzzer as follows.

```python
asymfz_gcd = SymbolicFuzzer(
    gcd, max_iter=10, max_tries=10, max_depth=10)
all_paths = asymfz_gcd.get_all_paths(asymfz_gcd.fnenter)
```

```python
len(all_paths)
```

```python
all_paths[37].get_path_to_root()
```

We can also list the predicates in each path.

```python
for s in to_single_assignment_predicates(all_paths[37].get_path_to_root()):
    if s is not None:
        print(to_src(s))
```

```python
constraints = asymfz_gcd.extract_constraints(all_paths[37].get_path_to_root())
```

```python
constraints
```

The constraints printed out demonstrates that our approach for renaming variables was successful. We need only one more piece to complete the puzzle. Our path is still a `PNode`. We need to modify `get_next_path()` so that we return the corresponding predicate chain.

```python
class SymbolicFuzzer(SymbolicFuzzer):
    def get_next_path(self):
        self.last_path -= 1
        if self.last_path == -1:
            self.last_path = len(self.paths) - 1
        return self.paths[self.last_path].get_path_to_root()
```

We will see next how to use our fuzzer for fuzzing.

### Fuzzing with Advanced Symbolic Fuzzer

We use our advanced symbolic fuzzer on *gcd* to generate plausible inputs.

```python
asymfz_gcd = SymbolicFuzzer(
    gcd, max_tries=10, max_iter=10, max_depth=10)
data = []
for i in range(10):
    r = asymfz_gcd.fuzz()
    data.append((r['a'].as_long(), r['b'].as_long()))
    v = gcd(*data[-1])
    print(r, "result:", repr(v))
```

The outputs look reasonable. However, what is the coverage obtained?

```python
with VisualizedArcCoverage() as cov:
    for a, b in data:
        gcd(a, b)
```

```python
cov.show_coverage(gcd)
```

```python
show_cfg(gcd, arcs=cov.arcs())
```

Indeed, both branch and statement coverage visualization seems to indicate that we achieved complete coverage.
How do we make use of our fuzzer in practice? We explore a small case study of a program to solve the roots of a quadratic equation.

#### Example: Roots of a Quadratic Equation
Here is the famous equation for finding the roots of a quadratic equation.

```python
from typing import Tuple
```

```python
def roots(a: float, b: float, c: float) -> Tuple[float, float]:
    d: float = b * b - 4 * a * c
    ax: float = 0.5 * d
    bx: float = 0
    while (ax - bx) > 0.1:
        bx = 0.5 * (ax + d / ax)
        ax = bx

    s: float = bx
    a2: float = 2 * a
    ba2: float = b / a2

    return -ba2 + s / a2, -ba2 - s / a2
```

Does the program look correct? Let us investigate if the program is reasonable. But before that, we need a helper
function `sym_to_float()` to convert symbolic values to floating point.

```python
def sym_to_float(v):
    if v is None:
        return math.inf
    elif isinstance(v, z3.IntNumRef):
        return v.as_long()
    return v.numerator_as_long() / v.denominator_as_long()
```

Now we are ready to fuzz.

```python
asymfz_roots = SymbolicFuzzer(
    roots,
    max_tries=10,
    max_iter=10,
    max_depth=10)
```

```python
with ExpectError():
    for i in range(100):
        r = asymfz_roots.fuzz()
        print(r)
        d = [sym_to_float(r[i]) for i in ['a', 'b', 'c']]
        v = roots(*d)
        print(d, v)
```

We have a `ZeroDivisionError`. Can we eliminate it?

#####  Roots - Check Before Divide

```python
def roots2(a: float, b: float, c: float) -> Tuple[float, float]:
    d: float = b * b - 4 * a * c

    xa: float = 0.5 * d
    xb: float = 0
    while (xa - xb) > 0.1:
        xb = 0.5 * (xa + d / xa)
        xa = xb

    s: float = xb

    if a == 0:
        return -c / b, -c / b  # only one solution

    a2: float = 2 * a
    ba2: float = b / a2
    return -ba2 + s / a2, -ba2 - s / a2
```

```python
asymfz_roots = SymbolicFuzzer(
    roots2,
    max_tries=10,
    max_iter=10,
    max_depth=10)
```

```python
with ExpectError():
    for i in range(1000):
        r = asymfz_roots.fuzz()
        d = [sym_to_float(r[i]) for i in ['a', 'b', 'c']]
        v = roots2(*d)
        #print(d, v)
```

Apparently, our fix was incomplete. Let us try again.

#####  Roots - Eliminating the Zero Division Error

```python
import math
```

```python
def roots3(a: float, b: float, c: float) -> Tuple[float, float]:
    d: float = b * b - 4 * a * c

    xa: float = 0.5 * d
    xb: float = 0
    while (xa - xb) > 0.1:
        xb = 0.5 * (xa + d / xa)
        xa = xb
    s: float = xb

    if a == 0:
        if b == 0:
            return math.inf, math.inf
        return -c / b, -c / b  # only one solution

    a2: float = 2 * a
    ba2: float = b / a2
    return -ba2 + s / a2, -ba2 - s / a2
```

```python
asymfz_roots = SymbolicFuzzer(
    roots3,
    max_tries=10,
    max_iter=10,
    max_depth=10)
```

```python
for i in range(10):
    r = asymfz_roots.fuzz()
    print(r)
    d = [sym_to_float(r[i]) for i in ['a', 'b', 'c']]
    v = roots3(*d)
    print(d, v)
```

With this, we have demonstrated that we can use our *SymbolicFuzzer* to fuzz programs, and it can aid in identifying problems in code.

## Limitations

There is an evident error in the `roots3()` function. We are not checking for negative roots. However, the symbolic execution does not seem to have detected it. Why are we not able to detect the problem of negative roots? Because we stop execution at a predetermined depth without throwing an error. That is, our symbolic execution is wide but shallow. One of the ways this limitation can be overcome is by relying on [concolic execution](ConcolicFuzzer.ipynb), that allows one to go deeper than pure symbolic execution.

A second problem is that symbolic execution is necessarily computation intensive. This means that specification based fuzzers are often able to generate a much larger set of inputs, and consecutively more coverage on programs that do not check for magic bytes, such that they provide a reasonable gradient of exploration.

## Synopsis

This chapter provides an implementation of a symbolic fuzzing engine `SymbolicFuzzer`. The fuzzer uses symbolic execution to exhaustively explore paths in the program to a limited depth, and generate inputs that will reach these paths.

As an example, consider the function `gcd()`, computing the greatest common divisor of `a` and `b`:

```python
# ignore
from bookutils import print_content
```

```python
# ignore
print_content(inspect.getsource(gcd), '.py')
```

To explore `gcd()`, the fuzzer can be used as follows, producing values for arguments that cover different paths in `gcd()` (including multiple times of loop iterations):

```python
gcd_fuzzer = SymbolicFuzzer(gcd, max_tries=10, max_iter=10, max_depth=10)
for i in range(10):
    args = gcd_fuzzer.fuzz()
    print(args)
```

Note that the variable values returned by `fuzz()` are Z3 _symbolic_ values; to convert them to Python numbers, use their method `as_long()`:

```python
for i in range(10):
    args = gcd_fuzzer.fuzz()
    a = args['a'].as_long()
    b = args['b'].as_long()
    d = gcd(a, b)
    print(f"gcd({a}, {b}) = {d}")
```

The symbolic fuzzer is subject to a number of constraints. First, it requires that the function to be fuzzed has correct type annotations, including all local variables. Second, it solves loops by unrolling them, but only for a fixed amount.

For programs without loops and variable reassignments, the `SimpleSymbolicFuzzer` is a faster, but more limited alternative.

```python
# ignore
from ClassDiagram import display_class_hierarchy
display_class_hierarchy(SymbolicFuzzer)
```

## Lessons Learned

* One can use symbolic execution to augment the inputs that explore all characteristics of a program.
* Symbolic execution can be broad but shallow.
* Symbolic execution is well suited for programs that rely on specific values to be present in the input, however, its utility decreases when such values are not present, and the input space represents a gradient in terms of coverage.

## Next Steps

* [Search based fuzzing](SearchBasedFuzzer.ipynb) can often be an acceptable middle ground when random fuzzing does not provide sufficient results, but symbolic fuzzing is too heavyweight.

## Background

Symbolic execution of programs was originally described by King \cite{king1976symbolic} in 1976. It is used extensively in vulnerability analysis of software, especially binary programs. Some well known symbolic execution tools include *KLEE* \cite{KLEE}, *angr* \cite{wang2017angr}, *Driller* \cite{stephens2016driller}, and *SAGE* \cite{godefroid2012sage}. The best known symbolic execution environment for Python is CHEF \cite{bucur2014prototyping} which does symbolic execution by modifying the interpreter.

The Z3 solver we use in this chapter was developed at Microsoft Research under the lead of Leonardo de Moura and Nikolaj Bjørner \cite{z3}. It is one of the most popular solvers.

## Exercises

### Exercise 1: Extending Symbolic Fuzzer to use function summaries

We showed in the first section how function summaries may be produced. Can you extend the `SymbolicFuzzer` to use function summaries when needed?

**Solution.** _None yet available._

### Exercise 2: Statically checking if a loop should be unrolled further

We examined how loops would be unrolled during exploration to a fixed depth. However, not all loops need to be unrolled completely. Some loops may contain only a constant number of iterations. For example, consider the loop below.

```python
i = 0
while i < 10:
    i += 1
```

This loop needs to be unrolled exactly $10$ times. For such cases, can you implement a method `can_be_satisfied()` which is invoked as below, to only unroll further if the path condition can be satisfied.

```python
class SymbolicFuzzer(SymbolicFuzzer):
    def get_all_paths(self, fenter):
        path_lst = [PNode(0, fenter)]
        completed = []
        for i in range(self.max_iter):
            new_paths = [PNode(0, fenter)]
            for path in path_lst:
                # explore each path once
                if path.cfgnode.children:
                    np = path.explore()
                    for p in np:
                        if path.idx > self.max_depth:
                            break
                        if self.can_be_satisfied(p):
                            new_paths.append(p)
                        else:
                            break
                else:
                    completed.append(path)
            path_lst = new_paths
        return completed + path_lst
```

**Solution.** Here is a solution.

```python
class SymbolicFuzzer(SymbolicFuzzer):
    def can_be_satisfied(self, p):
        s2 = self.extract_constraints(p.get_path_to_root())
        s = z3.Solver()
        identifiers = [c for i in s2 for c in used_identifiers(i)]
        with_types = identifiers_with_types(identifiers, self.used_variables)
        decl = define_symbolic_vars(with_types, '')
        exec(decl)
        exec("s.add(z3.And(%s))" % ','.join(s2), globals(), locals())
        return s.check() == z3.sat
```

With this implementation, new conditions are appended to paths if and only if the paths are still satisfiable after incorporating the condition.

### Exercise 3: Implementing a Concolic Fuzzer


We have seen in the chapter on [concolic fuzzing](ConcolicFuzzer.ipynb) how to trace a function concolically using information flow. However, this is somewhat suboptimal as the constraints can get dropped when the information flow is indirect (as in control flow based information flow). Can you implement concolic tracing using the infrastructure we built for symbolic execution?

**Solution.** Here is a possible solution.

In *concolic execution*, we rely on a seed input to guide our symbolic execution. We collect the line numbers that our seed input traces, and feed it to the symbolic execution such that in the `explore` step, only the child node that correspond to the seed input execution path is chosen. This allows us to collect the complete set of constraints along a *representative path*. Once we have it, we can choose any particular predicate and invert it to explore the program execution paths near the representative path.

We modify our original `ArcCoverage` to provide *all* line numbers that the program traversed.

```python
class TrackingArcCoverage(ArcCoverage):
    def offsets_from_entry(self, fn):
        zero = self._trace[0][1] - 1
        return [l - zero for (f, l) in self._trace if f == fn]
```

```python
with TrackingArcCoverage() as cov:
    roots3(1, 1, 1)
```

```python
cov.offsets_from_entry('roots3')
```

The `ConcolicTracer` first extracts the program trace on a seed input.

```python
class ConcolicTracer(SymbolicFuzzer):
    def __init__(self, fn, fnargs, **kwargs):
        with TrackingArcCoverage() as cov:
            fn(*fnargs)
        self.lines = cov.offsets_from_entry(fn.__name__)
        self.current_line = 0
        super().__init__(fn, **kwargs)
```

The method `get_all_paths()` now tries to follow the seed execution path.

```python
class ConcolicTracer(ConcolicTracer):
    def get_all_paths(self, fenter):
        assert fenter.ast_node.lineno == self.lines[self.current_line]
        self.current_line += 1
        last_node = PNode(0, fenter)
        while last_node and self.current_line < len(self.lines):
            if last_node.cfgnode.children:
                np = last_node.explore()
                for p in np:
                    if self.lines[self.current_line] == p.cfgnode.ast_node.lineno:
                        self.current_line += 1
                        last_node = p
                        break
                else:
                    last_node = None
                    break
            else:
                break
        assert len(self.lines) == self.current_line
        return [last_node]
```

We are now ready to concolically trace our execution.

#### Tracing the Execution Concolically

```python
acfz_roots = ConcolicTracer(
    roots3,
    fnargs=[1, 1, 1],
    max_tries=10,
    max_iter=10,
    max_depth=10)
```

```python
acfz_roots.paths[0].get_path_to_root()
```

```python
print(cov.offsets_from_entry('roots3'))
print([i.cfgnode.ast_node.lineno for i in acfz_roots.paths[0].get_path_to_root()])
print(acfz_roots.lines)
```

As can be seen above, we recovered the trace information correctly.
Next, we extract the constraints as usual.

```python
constraints = acfz_roots.extract_constraints(
    acfz_roots.paths[0].get_path_to_root())
```

```python
constraints
```

Next, we change our constraints to symbolic variables and solve them.

```python
identifiers = [c for i in constraints for c in used_identifiers(i)]
with_types = identifiers_with_types(identifiers, acfz_roots.used_variables)
decl = define_symbolic_vars(with_types, '')
exec(decl)
```

We are ready to solve our constraints. However, before that, here is a question for you.
*Should it result in exactly the same arguments?*

```python
eval('z3.solve(%s)' % ','.join(constraints))
```

```python
acfz_roots.fuzz()
```

Did they take the same path?

```python
with ArcCoverage() as cov:
    roots(1, 1, 1)
show_cfg(roots, arcs=cov.arcs())
```

```python
with ArcCoverage() as cov:
    roots(-1, 0, 0)
show_cfg(roots, arcs=cov.arcs())
```

Indeed, even though the arguments were different, the path traced is exactly the same.

As we saw in the chapter on [concolic fuzzing](ConcolicFuzzer.ipynb), concolic tracing has another use, namely that we can use it to explore nearby paths. We will see how to do that next.

#### Exploring Nearby Paths

We collected the following constraints.

```python
constraints
```

We can explore nearby paths by negating the conditionals starting from the very last. (A question for the student: Why do we want to start negating from the very last?)

```python
new_constraints = constraints[0:4] + ['z3.Not(%s)' % constraints[4]]
```

```python
new_constraints
```

```python
eval('z3.solve(%s)' % ','.join(new_constraints))
```

```python
with ArcCoverage() as cov:
    roots3(1, 0, -11 / 20)
show_cfg(roots3, arcs=cov.arcs())
```

Indeed, the path traced is now different. One can continue this procedure to the necessary number of times to explore all nearby paths to the execution.

Can you incorporate this exploration into the concolic fuzzer?

**Solution.** _None yet available._

## Compatibility

Earlier versions of this chapter used the name `AdvancedSymbolicFuzzer` for `SymbolicFuzzer`.

```python
AdvancedSymbolicFuzzer = SymbolicFuzzer
```
