# Testing Compilers

In this chapter, we will make use of [grammars and grammar-based testing](Grammars.ipynb) to systematically generate _program code_ – for instance, to test a compiler or an interpreter. Not very surprisingly, we use _Python_ and the _Python interpreter_ as our domain.

We chose Python not only because the rest of the book is also based on Python.
Most importantly, Python brings lots of built-in infrastructure we can leverage, especially

* _parsers_ that convert Python code into an abstract syntax tree (AST) representation and
* _unparsers_ that take an AST and convert it back into Python code.

This allows us to leverage grammars that operate on ASTs rather than concrete syntax, greatly reducing complexity.

```python
from bookutils import YouTubeVideo
YouTubeVideo('Nr1xbKj_WRQ')
```

**Prerequisites**

* You must read the chapter on [Fuzzing with Grammars](Grammars.ipynb) to understand how grammars and grammar-based testing work.

```python
# ignore
import sys
```

```python
# ignore
if sys.version_info < (3, 10):
    print("This code requires Python 3.10 or later")
    sys.exit(0)
```

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.PythonFuzzer import <identifier>
```

and then make use of the following features.

This chapter provides a `PythonFuzzer` class that allows producing arbitrary Python code elements:

```python
>>> fuzzer = PythonFuzzer()
>>> print(fuzzer.fuzz())
def R():
    break

```
By default, `PythonFuzzer` produces a _function definition_ – that is, a list of statements as above.
You can pass a `start_symbol` argument to state which Python element you'd like to have:

```python
>>> fuzzer = PythonFuzzer('<While>')
>>> print(fuzzer.fuzz())
while {set()[set():set():set()]}:
    C = set()
    D @= set()
    break
else:
    return

```
Here is a list of all possible start symbols. Their names reflect the nonterminals from the [Python `ast` module documentation](https://docs.python.org/3/library/ast.html).

```python
>>> sorted(list(PYTHON_AST_GRAMMAR.keys()))
['<Assert>',
 '<Assign>',
 '<Attribute>',
 '<AugAssign>',
 '<BinOp>',
 '<BoolOp>',
 '<Break>',
 '<Call>',
 '<Compare>',
 '<Constant>',
 '<Continue>',
 '<Delete>',
 '<Dict>',
 '<EmptySet>',
 '<Expr>',
 '<For>',
 '<FunctionDef>',
 '<If>',
 '<List>',
 '<Module>',
 '<Name>',
 '<Pass>',
 '<Return>',
 '<Set>',
 '<Slice>',
 '<Starred>',
 '<Subscript>',
 '<Tuple>',
 '<UnaryOp>',
 '<While>',
 '<With>',
 '<arg>',
 '<arg_list>',
 '<args>',
 '<args_param>',
 '<arguments>',
 '<bool>',
 '<boolop>',
 '<cmpop>',
 '<cmpop_list>',
 '<cmpops>',
 '<decorator_list_param>',
 '<defaults_param>',
 '<digit>',
 '<digits>',
 '<expr>',
 '<expr_list>',
 '<exprs>',
 '<float>',
 '<func>',
 '<id>',
 '<id_continue>',
 '<id_start>',
 '<identifier>',
 '<integer>',
 '<keyword>',
 '<keyword_list>',
 '<keywords>',
 '<keywords_param>',
 '<kw_defaults_param>',
 '<kwarg>',
 '<kwonlyargs_param>',
 '<lhs_Attribute>',
 '<lhs_List>',
 '<lhs_Name>',
 '<lhs_Starred>',
 '<lhs_Subscript>',
 '<lhs_Tuple>',
 '<lhs_expr>',
 '<lhs_exprs>',
 '<literal>',
 '<mod>',
 '<none>',
 '<nonempty_expr_list>',
 '<nonempty_lhs_expr_list>',
 '<nonempty_stmt_list>',
 '<nonzerodigit>',
 '<not_double_quotes>',
 '<not_single_quotes>',
 '<operator>',
 '<orelse_param>',
 '<posonlyargs_param>',
 '<returns>',
 '<start>',
 '<stmt>',
 '<stmt_list>',
 '<stmts>',
 '<string>',
 '<type_comment>',
 '<type_ignore>',
 '<type_ignore_list>',
 '<type_ignore_param>',
 '<type_ignores>',
 '<unaryop>',
 '<vararg>',
 '<withitem>',
 '<withitem_list>',
 '<withitems>']
```
If you'd like more control over Python code generation, here is what is happening behind the scenes.
The EBNF grammar `PYTHON_AST_GRAMMAR` can parse and produce _abstract syntax trees_ for Python.
To produce a Python module without `PythonFuzzer`, you would take these steps:

**Step 1:** Create a non-EBNF grammar suitable for `ISLaSolver` (or any other grammar fuzzer):

```python
>>> python_ast_grammar = convert_ebnf_grammar(PYTHON_AST_GRAMMAR)
```
**Step 2:**  Feed the resulting grammar into a grammar fuzzer such as ISLa:

```python
>>> solver = ISLaSolver(python_ast_grammar, start_symbol='<FunctionDef>')
```
**Step 3:**  Have the grammar fuzzer produce a string. This string represents an AST.

```python
>>> ast_string = str(solver.solve())
>>> ast_string
'FunctionDef(name=\'y\', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return()], decorator_list=[Call(func=Name(id="set", ctx=Load()), args=[], keywords=[])])'
```
**Step 4:**  Convert the AST into an actual Python AST data structure.

```python
>>> from ast import *
>>> abstract_syntax_tree = eval(ast_string)
```
**Step 5:** Finally, convert the AST structure back into readable Python code:

```python
>>> ast.fix_missing_locations(abstract_syntax_tree)
>>> print(ast.unparse(abstract_syntax_tree))
@set()
def y():
    return

```
The chapter has many more applications, including parsing and mutating Python code, evolutionary fuzzing, and more.

Here are the details on the `PythonFuzzer` constructor:

<p><code>PythonFuzzer(self, start_symbol: Optional[str] = None, *, grammar: Optional[Dict[str, List[Union[str, Tuple[str, Dict[str, Any]]]]]] = None, constraint: Optional[str] = None, **kw_params) -&gt; None</code></p>
<p>Produce Python code. Parameters are:</p>
<ul>
<li><code>start_symbol</code>: The grammatical entity to be generated (default: <code>&lt;FunctionDef&gt;</code>)</li>
<li><code>grammar</code>: The EBNF grammar to be used (default: <code>PYTHON__AST_GRAMMAR</code>); and</li>
<li><code>constraint</code> an ISLa constraint (if any).</li>
</ul>
<p>Additional keyword parameters are passed to the <code>ISLaSolver</code> superclass.</p>

![](PICS/PythonFuzzer-synopsis-1.svg)

## A Grammar for Concrete Code

To _produce_ code, it is fairly easy to write a grammar with _concrete_ syntax. If we want to produce, say, arithmetic expressions, we can easily create a concrete grammar which does precisely that.

```python
import bookutils.setup
```

```python
from Grammars import Grammar
from Grammars import is_valid_grammar, convert_ebnf_grammar, extend_grammar, trim_grammar
```

```python
from typing import Optional
```

We use the [Fuzzingbook format for grammars](https://www.fuzzingbook.org/html/Grammars.html), in which grammars are represented as dictionaries from symbols to lists of expansion alternatives.

```python
EXPR_GRAMMAR: Grammar = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>"],

    "<factor>":
        ["+<factor>",
         "-<factor>",
         "(<expr>)",
         "<integer>.<integer>",
         "<integer>"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}
```

```python
assert is_valid_grammar(EXPR_GRAMMAR)
```

We can use this grammar to produce syntactically valid arithmetic expressions.
We use the [ISLa solver](FuzzingWithConstraints.ipynb) as our generator, as it is the most powerful; but we could also use any other of our grammar fuzzers such as [GrammarFuzzer](GrammarFuzzer.ipynb) at this point.

```python
from isla.solver import ISLaSolver  # type: ignore
```

Here are some concrete inputs produced from the grammar:

```python
expr_solver = ISLaSolver(EXPR_GRAMMAR)
for _ in range(10):
    print(expr_solver.solve())
```

We could extend the grammar further to also produce assignments and other statements, and piece by piece cover the entire syntax of the programming language. However, this would be a not-so-great idea. Why?

The problem is that when testing _compilers_, you not only want to be able to _produce_ code, but also to _parse_ code, such that you can mutate and manipulate it at will. And this is where our "concrete" syntax will give us problems. While we can easily parse code (or expressions) that exactly adheres to the syntax...

```python
expr_solver.check('2 + 2')
```

... a single space will already suffice to make it fail...

```python
expr_solver.check('2 +  2')
```

... as does the absence of spaces:

```python
expr_solver.check('2+2')
```

Indeed, spaces are optional in most programming languages. We _could_ update our grammar such that it can handle optional spaces at all times (introducing a `<space>` nonterminal). But then, there are other features like _comments_...

```python
expr_solver.check('2 + 2    # should be 4')
```

... or _continuation lines_ ...

```python
expr_solver.check('2 + \\\n2')  # An expression split over two lines
```

that our grammar would have to cover.

On top, there are language features that cannot be even represented properly in a context-free grammar:

* In the C programming language, for instance, the parser needs to know whether an identifier has been defined as a _type_
* In Python, _indentation_ levels cannot be represented by a context-free grammar.

For this reason, it is often a good idea to make use of a dedicated _parser_ (or _preprocessor_) to turn input into a more _abstract_ representation - typically a _tree_ structure. In programming languages, such a tree is called an _abstract syntax tree_ (AST); it is the data structure that compilers operate on.

## Abstract Syntax Trees

Abstract Syntax Trees (ASTs) that represent program code are among the most complex data structures in the world (if not _the_ most complex data structures) - notably because they reflect all the complexity of the programming language and its features.
The good news is that in Python, working with ASTs is particularly easy - one can work with them using standard language features.

Let us illustrate ASTs using an example. Here is a piece of code that we'd like to work with:

```python
def main():
    print("Hello, world!")  # A simple example
```

```python
main()
```

Let us obtain the source code of this function:

```python
import inspect
```

```python
main_source = inspect.getsource(main)
print(main_source)
```

We make use of the [Python AST module](https://docs.python.org/3/library/ast.html) to convert this code string to an AST and back.

```python
import ast
```

With `ast.parse()`, we can parse the `main()` source into an AST:

```python
main_tree = ast.parse(main_source)
```

This is what this tree looks like:

```python
from bookutils import show_ast
```

```python
show_ast(main_tree)
```

We see how the function definition has become a `FunctionDef` node, whose third child is an `Expr` node, which in turn becomes a `Call` – of the `"print"` function with an argument of `"Hello, world!"`.

Each of these AST nodes comes as a _constructor_ – that is, we can invoke `FunctionDef()` to obtain a function definition node, or `Call()` to obtain a call node.
These constructors take the AST _children_ as arguments, but also lots of _optional_ arguments (which we did not use so far). The _dump_ of the AST into a string reveals all the arguments for each constructor:

```python
print(ast.dump(main_tree, indent=4))
```

The [Python ast documentation](https://docs.python.org/3/library/ast.html) lists all these constructors, which make up the abstract syntax. There are more than 100 individual constructors! (We said that ASTs are complex, right?)

The nice thing about the above string representation is that we can take it _as is_ and turn it into a tree again:

```python
from ast import *
```

```python
my_main_tree = Module(
    body=[
        FunctionDef(
            name='main',
            args=arguments(
                posonlyargs=[],
                args=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Constant(value='Hello, world!')],
                        keywords=[]))],
            decorator_list=[])],
    type_ignores=[])
```

We can take this tree and compile it into executable code:

```python
my_main_tree = fix_missing_locations(my_main_tree)  # required for trees built from constructors
my_main_code = compile(my_main_tree, filename='<unknown>', mode='exec')
```

```python
del main  # This deletes the definition of main()
```

```python
exec(my_main_code)  # This defines main() again from `code`
```

```python
main()
```

We can also _unparse_ the tree (= turn it into source code again). (Note how the comment got lost during parsing.)

```python
print(ast.unparse(my_main_tree))
```

Hence, we can

1. _Parse_ concrete code into ASTs (with `ast.parse()`)
2. _Generate_ new ASTs and _mutate_ existing ones
3. _Unparse_ ASTs to obtain concrete code again (with `ast.unparse()`)

To _generate_ and _mutate_ ASTs (step #2, above), we need means to produce _correct_ ASTs, invoking all constructors with the correct arguments.
The plan is thus to have a _grammar_ for ASTs, which produces (and parses) ASTs as we like.

## A Grammar for ASTs

Programming language grammars are among the most complicated formal grammars around, and ASTs reflect much of this complexity. We will use the [abstract AST grammar](https://docs.python.org/3/library/ast.html) as specified in the Python documentation as base, and build a formal context-free grammar step by step.

### Constants

We will start with simple constants – strings and integers. Again, we use the `fuzzingbook` syntax for grammars, as it allows for easier extension.

```python
import string
```

```python
ANYTHING_BUT_DOUBLE_QUOTES_AND_BACKSLASH = (string.digits + string.ascii_letters + string.punctuation + ' ').replace('"', '').replace('\\', '')
ANYTHING_BUT_SINGLE_QUOTES_AND_BACKSLASH = (string.digits + string.ascii_letters + string.punctuation + ' ').replace("'", '').replace('\\', '')
```

```python
ANYTHING_BUT_DOUBLE_QUOTES_AND_BACKSLASH
```

```python
ANYTHING_BUT_SINGLE_QUOTES_AND_BACKSLASH
```

```python
PYTHON_AST_CONSTANTS_GRAMMAR: Grammar = {
    '<start>': [ '<expr>' ],

    # Expressions
    '<expr>': [ '<Constant>', '<Expr>' ],
    '<Expr>': [ 'Expr(value=<expr>)' ],

    # Constants
    '<Constant>': [ 'Constant(value=<literal>)' ],
    '<literal>': [ '<string>', '<integer>', '<float>', '<bool>', '<none>' ],

    # Strings
    '<string>': [ '"<not_double_quotes>*"', "'<not_single_quotes>*'" ],
    '<not_double_quotes>': list(ANYTHING_BUT_DOUBLE_QUOTES_AND_BACKSLASH),
    '<not_single_quotes>': list(ANYTHING_BUT_SINGLE_QUOTES_AND_BACKSLASH),
    # FIXME: The actual rules for Python strings are also more complex:
    # https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals

    # Numbers
    '<integer>': [ '<digit>', '<nonzerodigit><digits>' ],
    '<float>': [ '<integer>.<integer>' ],
    '<nonzerodigit>': ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '<digits>': [ '<digit><digits>', '<digit>' ],
    '<digit>': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    # FIXME: There are _many_ more ways to express numbers in Python; see
    # https://docs.python.org/3/reference/lexical_analysis.html#numeric-literals

    # More
    '<bool>': [ 'True', 'False' ],
    '<none>': [ 'None' ],

    # FIXME: Not supported: bytes, format strings, regex strings...
}
```

Note that we use _extended Backus-Naur form_ in our grammars (here: `<string>`):

* `<elem>+` stands for one or more instances of `<elem>`;
* `<elem>*` stands for zero or more instances of `<elem>`;
* `<elem>?` stands for one or zero instances of `<elem>`.

A call to `is_valid_grammar()` ensures our grammar is free of common mistakes. Don't write grammars without it!

```python
assert is_valid_grammar(PYTHON_AST_CONSTANTS_GRAMMAR)
```

```python
constants_grammar = convert_ebnf_grammar(PYTHON_AST_CONSTANTS_GRAMMAR)
constants_solver = ISLaSolver(constants_grammar)
constants_tree_str = str(constants_solver.solve())
print(constants_tree_str)
```

We can create an AST from this expression and turn it into Python code (well, a literal):

```python
constants_tree = eval(constants_tree_str)
ast.unparse(constants_tree)
```

Let's do this a number of times:

```python
def test_samples(grammar: Grammar, iterations: int = 10, start_symbol = None, log: bool = True):
    g = convert_ebnf_grammar(grammar)
    solver = ISLaSolver(g, start_symbol=start_symbol, max_number_free_instantiations=iterations)
    for i in range(iterations):
        tree_str = str(solver.solve())
        tree = eval(tree_str)
        ast.fix_missing_locations(tree)
        if log:
            code = ast.unparse(tree)
            print(f'{code:40} # {tree_str}')
```

```python
test_samples(PYTHON_AST_CONSTANTS_GRAMMAR)
```

Our grammar can also _parse_ ASTs obtained from concrete code.

```python
sample_constant_code = "4711"
sample_constant_ast = ast.parse(sample_constant_code).body[0]  # get the `Expr` node
sample_constant_ast_str = ast.dump(sample_constant_ast)
print(sample_constant_ast_str)
```

```python
constant_solver = ISLaSolver(constants_grammar)
constant_solver.check(sample_constant_ast_str)
```

Let us now come up with a quiz question: _Does our grammar support negative numbers?_
For this, let's first find out if the `Constant()` constructor also take a _negative_ number as an argument? It turns out it can:

```python
ast.unparse(Constant(value=-1))
```

But what happens if we parse a negative number, say `-1`? One might assume that this simply results in a `Constant(-1)`, right? Try it out yourself!

```python
from bookutils import quiz
```

```python
quiz("If we parse a negative number, do we obtain ",
    [
        "a `Constant()` with a negative value, or",
        "a unary `-` operator applied to a positive value?"
    ], 1 ** 0 + 1 ** 1)
```

The answer is that parsing `-1` yields a unary minus `USub()` applied to a positive value:

```python
print(ast.dump(ast.parse('-1')))
```

As unary operators are not part of our grammar (yet), it cannot handle negative numbers:

```python
sample_constant_code = "-1"
sample_constant_ast = ast.parse(sample_constant_code).body[0]  # get the `Expr` node
sample_constant_ast_str = ast.dump(sample_constant_ast)
constant_solver = ISLaSolver(constants_grammar)
constant_solver.check(sample_constant_ast_str)
```

In the next sections, we will gradually expand our grammar with more and more Python features, eventually covering (almost) the entire language.

### Excursion: Composites

Let us add composite constants – lists, dictionaries, tuples, etc. Here is how these are represented in an AST:

```python
print(ast.dump(ast.parse("{ 'a': set() }"), indent=4))
```

Let us encode these into a grammar, again using the definitions from the [abstract AST grammar](https://docs.python.org/3/library/ast.html).
All these structures also take _contexts_ in which identifiers are used – `Load()` if they are used for evaluation, `Store()` if they appear on the left-hand side of an assignment (yes, in Python, you can have a tuple on the left-hand side of an assignment, say `(x, y) = (1, 2)`), and `Del()` if they are used as operands in a `del` statement. Right now, we only use `Load()` and `Del()` interchangeably.

```python
PYTHON_AST_COMPOSITES_GRAMMAR: Grammar = extend_grammar(
    PYTHON_AST_CONSTANTS_GRAMMAR, {
    '<expr>': PYTHON_AST_CONSTANTS_GRAMMAR['<expr>'] + [
        '<Dict>', '<Set>', '<List>', '<Tuple>'
    ],

    '<Dict>': [ 'Dict(keys=<expr_list>, values=<expr_list>)' ],
    '<Set>': [ 'Set(elts=<nonempty_expr_list>)', '<EmptySet>' ],
    '<EmptySet>': [ 'Call(func=Name(id="set", ctx=Load()), args=[], keywords=[])' ],
    '<List>': [
        'List(elts=<expr_list>, ctx=Load())',
        'List(elts=<expr_list>, ctx=Del())',
    ],
    '<Tuple>': [
        'Tuple(elts=<expr_list>, ctx=Load())',
        'Tuple(elts=<expr_list>, ctx=Del())',
    ],

    # Lists of expressions
    '<expr_list>': [ '[<exprs>?]' ],
    '<nonempty_expr_list>': [ '[<exprs>]' ],
    '<exprs>': [ '<expr>', '<exprs>, <expr>' ],
})
```

```python
assert is_valid_grammar(PYTHON_AST_COMPOSITES_GRAMMAR)
```

```python
for elt in [ '<Constant>', '<Dict>', '<Set>', '<List>', '<Tuple>' ]:
    print(elt)
    test_samples(PYTHON_AST_COMPOSITES_GRAMMAR, start_symbol=elt)
    print()
```

You may encounter a number of uncommon expressions here. For instance:

1. `()` is an empty tuple.
2. `(1,)` is a tuple with one element.
3. `{}` is an empty dictionary; `{1}` is a set with one element.
4. An empty set is denoted by `set()`.

The fact that we use `set()` to represent empty sets is actually a feature of our `PYTHON_AST_COMPOSITES_GRAMMAR` grammar.
If we invoke the `Set()` AST constructor without any elements, we obtain this beautiful expression...

```python
print(ast.unparse(Set(elts=[])))
```

... which indeed evaluates into an empty set.

```python
{*()}
```

Technically speaking, all of this is correct, but we'd like to stick to (somewhat) more readable code. If you want to confuse your programmer friends, always use `{*()}` instead of `set()`.

### End of Excursion

### Excursion: Expressions

Let us extend our grammar with _expressions_. The Python parser already takes care of precedence rules, so we can treat all unary and binary operators in a similar fashion.

```python
print(ast.dump(ast.parse("2 + 2 is not False"), indent=4))
```

```python
PYTHON_AST_EXPRS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_COMPOSITES_GRAMMAR, {
    '<expr>': PYTHON_AST_COMPOSITES_GRAMMAR['<expr>'] + [
        '<BoolOp>', '<BinOp>', '<UnaryOp>', '<Compare>',
    ],

    # Booleans: and or
    '<BoolOp>': [ 'BoolOp(op=<boolop>, values=<expr_list>)' ],
    '<boolop>': [ 'And()', 'Or()' ],

    # Binary operators: + - * ...
    '<BinOp>': [ 'BinOp(left=<expr>, op=<operator>, right=<expr>)' ],
    '<operator>': [ 'Add()', 'Sub()', 'Mult()', 'MatMult()',
                   'Div()', 'Mod()', 'Pow()',
                   'LShift()', 'RShift()', 'BitOr()', 'BitXor()', 'BitAnd()',
                   'FloorDiv()' ],

    # Unary operators: not + - ...
    '<UnaryOp>': [ 'UnaryOp(op=<unaryop>, operand=<expr>)'],
    '<unaryop>': [ 'Invert()', 'Not()', 'UAdd()', 'USub()' ],

    # Comparisons: == != < <= > >= is in ...
    '<Compare>': [ 'Compare(left=<expr>, ops=<cmpop_list>, comparators=<expr_list>)'],
    '<cmpop_list>': [ '[<cmpops>?]' ],
    '<cmpops>': [ '<cmpop>', '<cmpop>, <cmpops>' ],
    '<cmpop>': [ 'Eq()', 'NotEq()', 'Lt()', 'LtE()', 'Gt()', 'GtE()',
                 'Is()', 'IsNot()', 'In()', 'NotIn()' ],

    # FIXME: There's a few more expressions: GeneratorExp, Await, YieldFrom, ...
})
```

```python
assert is_valid_grammar(PYTHON_AST_EXPRS_GRAMMAR)
```

```python
for elt in [ '<BoolOp>', '<BinOp>', '<UnaryOp>', '<Compare>' ]:
    print(elt)
    test_samples(PYTHON_AST_EXPRS_GRAMMAR, start_symbol=elt)
    print()
```

Not all of these expressions are _type-correct_. For instance, `set() * set()` raises a type error at runtime. They _can_ be properly parsed, though.

How good is our grammar at this point? Let us create 20 expressions and check how many of these
1. parse without `SyntaxError`
2. evaluate without `TypeError`.

```python
expr_iterations = 20
bad_syntax = 0
bad_type = 0
ast_exprs_grammar = convert_ebnf_grammar(PYTHON_AST_EXPRS_GRAMMAR)
expr_solver = ISLaSolver(ast_exprs_grammar, max_number_free_instantiations=expr_iterations)
for i in range(expr_iterations):
    expr_tree = eval(str(expr_solver.solve()))
    expr_tree = fix_missing_locations(expr_tree)
    expr_str = ast.unparse(expr_tree)
    print(i, expr_str)
    try:
        ...  # insert parsing code here
    except SyntaxError:
        bad_syntax += 1
    except TypeError:
        bad_type += 1

    try:
        ...  # <-- insert evaluation code here
    except TypeError:
        bad_type += 1
    except SyntaxError:
        bad_syntax += 1

print(f"Bad syntax: {bad_syntax}/{expr_iterations}")
print(f"Bad type: {bad_type}/{expr_iterations}")
```

We're not doing too bad here.
It is possible, in principle, to use ISLa constraints such that the resulting code will be properly typed - but this would take hundreds to thousands of rules. We will leave this exercise to the reader.

Note that you should _not_ repeat this experiment once _identifiers_ come into play. There is a remote chance that the fuzzer synthesizes a call like `os.remove("/")` – and away goes your file system!

### End of Excursion

### Excursion: Names and Function Calls

Let us add some _identifiers_ such that we can call _functions_.

```python
ID_START = string.ascii_letters + '_'
ID_CONTINUE = ID_START + string.digits
```

```python
ID_CONTINUE
```

```python
print(ast.dump(ast.parse("xyzzy(a, b=c)"), indent=4))
```

```python
PYTHON_AST_IDS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_EXPRS_GRAMMAR, {
    '<expr>': PYTHON_AST_EXPRS_GRAMMAR['<expr>'] + [
        '<Name>', '<Call>'
    ],

    # Identifiers
    '<Name>': [
        'Name(id=<identifier>, ctx=Load())',
        'Name(id=<identifier>, ctx=Del())'
    ],
    '<identifier>': [ "'<id>'" ],
    '<id>': [ '<id_start><id_continue>*' ],
    '<id_start>': list(ID_START),
    '<id_continue>': list(ID_CONTINUE),
    # FIXME: Actual rules are a bit more complex; see
    # https://docs.python.org/3/reference/lexical_analysis.html#identifiers

    # Function Calls
    '<Call>': [ 'Call(func=<func><args_param><keywords_param>)' ],
    '<args_param>': [ ', args=<expr_list>' ],
    '<keywords_param>': [ ', keywords=<keyword_list>' ],
    '<func>': [ '<expr>' ],  # Actually <Expr>, but this is more readable and parses 90%
    '<keyword_list>': [ '[<keywords>?]' ],
    '<keywords>': [ '<keyword>', '<keyword>, <keywords>' ],
    '<keyword>': [ 'keyword(arg=<identifier>, value=<expr>)' ]
})
```

```python
# do import this unconditionally
if sys.version_info >= (3, 13):
    PYTHON_AST_IDS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_IDS_GRAMMAR, {
        # As of 3.13, args and keywords parameters are optional
        '<Call>': [ 'Call(func=<func><args_param>?<keywords_param>?)' ],
    })
```

```python
assert is_valid_grammar(PYTHON_AST_IDS_GRAMMAR)
```

```python
for elt in [ '<Name>', '<Call>' ]:
    print(elt)
    test_samples(PYTHON_AST_IDS_GRAMMAR, start_symbol=elt)
    print()
```

```python
ast_ids_grammar = convert_ebnf_grammar(PYTHON_AST_IDS_GRAMMAR)
```

```python
id_solver = ISLaSolver(ast_ids_grammar, start_symbol='<id>')
assert id_solver.check('open')
```

```python
name_solver = ISLaSolver(ast_ids_grammar)
assert name_solver.check("Name(id='open', ctx=Load())")
```

```python
call_solver = ISLaSolver(ast_ids_grammar, start_symbol='<keyword_list>')
assert call_solver.check('[]')
```

```python
call_str = ast.dump(ast.parse('open("foo.txt", "r")').body[0].value)  # type: ignore
print(call_str)
call_solver = ISLaSolver(ast_ids_grammar)
assert call_solver.check(call_str)
```

### End of Excursion

### Excursion: Attributes and Subscripts

Let us add attributes and subscripts.

```python
print(ast.dump(ast.parse("a[b].c"), indent=4))
```

```python
PYTHON_AST_ATTRS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_IDS_GRAMMAR, {
    '<expr>': PYTHON_AST_IDS_GRAMMAR['<expr>'] + [
        '<Attribute>', '<Subscript>', '<Starred>',
    ],

    # Attributes
    '<Attribute>': [
        'Attribute(value=<expr>, attr=<identifier>, ctx=Load())',
        'Attribute(value=<expr>, attr=<identifier>, ctx=Del())',
    ],

    # Subscripts
    '<Subscript>': [
        'Subscript(value=<expr>, slice=<Slice>, ctx=Load())',
        'Subscript(value=<expr>, slice=<Slice>, ctx=Del())',
    ],
    '<Slice>': [
        'Slice()',
        'Slice(<expr>)',
        'Slice(<expr>, <expr>)',
        'Slice(<expr>, <expr>, <expr>)',
    ],

    # Starred
    '<Starred>': [
        'Starred(value=<expr>, ctx=Load())',
        'Starred(value=<expr>, ctx=Del())',
    ],

    # We're extending the set of callers a bit
    '<func>': [ '<Name>', '<Attribute>', '<Subscript>' ],
})
```

```python
assert is_valid_grammar(PYTHON_AST_ATTRS_GRAMMAR)
```

```python
for elt in [ '<Attribute>', '<Subscript>', '<Starred>' ]:
    print(elt)
    test_samples(PYTHON_AST_ATTRS_GRAMMAR, start_symbol=elt)
    print()
```

### End of Excursion

### Excursion: Variable Assignments

Now for variable assignments. These make things more complex, as we have a restricted set of expressions on the left hand side of an assignment.

```python
PYTHON_AST_ASSIGNMENTS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_ATTRS_GRAMMAR, {
    '<start>': [ '<stmt>' ],

    '<stmt>': [
        '<Assign>', '<AugAssign>',
        '<Expr>'
    ],

    # Assignments
    '<Assign>': [
        'Assign(targets=<nonempty_lhs_expr_list>, value=<expr><type_comment>?)',
    ],
    '<type_comment>': [ ', type_comment=<string>' ],
    '<AugAssign>': [
        'AugAssign(target=<lhs_expr>, op=<operator>, value=<expr>)',
    ],

    # Lists of left-hand side expressions
    # '<lhs_expr_list>': [ '[<lhs_exprs>?]' ],
    '<nonempty_lhs_expr_list>': [ '[<lhs_exprs>]' ],
    '<lhs_exprs>': [ '<lhs_expr>', '<lhs_exprs>, <lhs_expr>' ],

    # On the left-hand side of assignments, we allow a number of structures
    '<lhs_expr>': [
        '<lhs_Name>',  # Most common
        '<lhs_List>', '<lhs_Tuple>',
        '<lhs_Attribute>',
        '<lhs_Subscript>',
        '<lhs_Starred>',
    ],

    '<lhs_Name>': [ 'Name(id=<identifier>, ctx=Store())', ],

    '<lhs_List>': [
        'List(elts=<nonempty_lhs_expr_list>, ctx=Store())',
    ],
    '<lhs_Tuple>': [
        'Tuple(elts=<nonempty_lhs_expr_list>, ctx=Store())',
    ],
    '<lhs_Attribute>': [
        'Attribute(value=<lhs_expr>, attr=<identifier>, ctx=Store())',
    ],
    '<lhs_Subscript>': [
        'Subscript(value=<lhs_expr>, slice=<Slice>, ctx=Store())',
    ],
    '<lhs_Starred>': [
        'Starred(value=<lhs_expr>, ctx=Store())',
    ],
})
```

```python
assert is_valid_grammar(PYTHON_AST_ASSIGNMENTS_GRAMMAR)
```

```python
for elt in ['<Assign>', '<AugAssign>']:
    print(elt)
    test_samples(PYTHON_AST_ASSIGNMENTS_GRAMMAR, start_symbol=elt)
    print()
```

### End of Excursion

### Excursion: Statements

Now for statements. There's quite a lot of these.

```python
PYTHON_AST_STMTS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_ASSIGNMENTS_GRAMMAR, {
    '<start>': [ '<stmt>' ],

    '<stmt>': PYTHON_AST_ASSIGNMENTS_GRAMMAR['<stmt>'] + [
        '<For>', '<While>', '<If>',
        '<Return>', '<Delete>', '<Assert>',
        '<Pass>', '<Break>', '<Continue>',
        '<With>'
    ],

    # Control structures
    '<For>': [
        'For(target=<lhs_expr>, iter=<expr>, body=<nonempty_stmt_list>, orelse=<stmt_list><type_comment>)'
    ],
    '<stmt_list>': [ '[<stmts>?]' ],
    '<nonempty_stmt_list>': [ '[<stmts>]' ],
    '<stmts>': [ '<stmt>', '<stmt>, <stmts>' ],

    '<While>': [
        'While(test=<expr>, body=<nonempty_stmt_list>, orelse=<stmt_list>)'
    ],

    '<If>': [
        'If(test=<expr>, body=<nonempty_stmt_list><orelse_param>)'
    ],
    '<orelse_param>': [
        ', orelse=<stmt_list>'
    ],

    '<With>': [
        'With(items=<withitem_list>, body=<nonempty_stmt_list><type_comment>?)'
    ],
    '<withitem_list>': [ '[<withitems>?]' ],
    '<withitems>': [ '<withitem>', '<withitems>, <withitem>' ],
    '<withitem>': [
        'withitem(context_expr=<expr>)',
        'withitem(context_expr=<expr>, optional_vars=<lhs_expr>)',
    ],

    # Other statements
    '<Return>': [
        'Return()',
        'Return(value=<expr>)'
    ],
    '<Delete>': [
        'Delete(targets=<expr_list>)'
    ],
    '<Assert>': [
        'Assert(test=<expr>)',
        'Assert(test=<expr>, msg=<expr>)'
    ],
    '<Pass>': [ 'Pass()'],
    '<Break>': [ 'Break()' ],
    '<Continue>': [ 'Continue()']

    # FIXME: A few more: AsyncFor, AsyncWith, Match, Try, TryStar
    # Import, ImportFrom, Global, Nonlocal...
})
```

```python
# do import this unconditionally
if sys.version_info >= (3, 13):
    PYTHON_AST_STMTS_GRAMMAR: Grammar = \
        extend_grammar(PYTHON_AST_STMTS_GRAMMAR, {
        # As of 3.13, orelse is optional
        '<If>': [
            'If(test=<expr>, body=<nonempty_stmt_list><orelse_param>?)'
        ],
    })
```

```python
assert is_valid_grammar(PYTHON_AST_STMTS_GRAMMAR)
```

```python
for elt in PYTHON_AST_STMTS_GRAMMAR['<stmt>']:
    print(elt)
    test_samples(PYTHON_AST_STMTS_GRAMMAR, start_symbol=elt)
    print()
```

Let us see if we can also _parse_ code properly. Here is a sample:

```python
with_tree = ast.parse("""
with open('foo.txt') as myfile:
    content = myfile.readlines()
    if content is not None:
        print(content)
""")
```

```python
python_ast_stmts_grammar = convert_ebnf_grammar(PYTHON_AST_STMTS_GRAMMAR)
with_tree_str = ast.dump(with_tree.body[0])  # get the `With(...)` subtree
print(with_tree_str)
with_solver = ISLaSolver(python_ast_stmts_grammar)
assert with_solver.check(with_tree_str)
```

It seems our grammar can also parse non-trivial code properly. We are doing well!

### End of Excursion

### Excursion: Function Definitions

Now for function definitions.
Not too many surprises here.

```python
print(ast.dump(ast.parse("""
def f(a, b=1):
    pass
"""
), indent=4))
```

```python
PYTHON_AST_DEFS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_STMTS_GRAMMAR, {
    '<stmt>': PYTHON_AST_STMTS_GRAMMAR['<stmt>'] + [ '<FunctionDef>' ],

    '<FunctionDef>': [
        'FunctionDef(name=<identifier>, args=<arguments>, body=<nonempty_stmt_list><decorator_list_param><returns>?<type_comment>?)'
    ],
    '<decorator_list_param>': [
        ', decorator_list=<expr_list>'
    ],

    '<arguments>': [
        'arguments(<posonlyargs_param>args=<arg_list><vararg>?<kwonlyargs_param><kw_defaults_param><kwarg>?<defaults_param>)'
    ],
    '<posonlyargs_param>': [
        'posonlyargs=<arg_list>, '
    ],
    '<kwonlyargs_param>': [
        ', kwonlyargs=<arg_list>'
    ],
    '<kw_defaults_param>': [
        ', kw_defaults=<expr_list>'
    ],
    '<defaults_param>': [
        ', defaults=<expr_list>'
    ],

    '<arg_list>': [ '[<args>?]' ],
    '<args>': [ '<arg>', '<arg>, <arg>' ],
    '<arg>': [ 'arg(arg=<identifier>)' ],

    '<vararg>': [ ', vararg=<arg>' ],
    '<kwarg>': [ ', kwarg=<arg>' ],
    '<returns>': [ ', returns=<expr>' ],

    # FIXME: Not handled: AsyncFunctionDef, ClassDef
})
```

In Python 3.12 and later, function definitions also have a `type_param` field:

```python
# do import this unconditionally
if sys.version_info >= (3, 12):
    PYTHON_AST_DEFS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_DEFS_GRAMMAR, {
    '<FunctionDef>': [
        'FunctionDef(name=<identifier>, args=<arguments>, body=<nonempty_stmt_list><decorator_list_param><returns>?<type_comment>?<type_params>?)'
    ],
    '<type_params>': [
        ', type_params=<type_param_list>',
    ],
    '<type_param_list>': [ '[<type_param>?]' ],
    '<type_param>': [ '<TypeVar>', '<ParamSpec>', '<TypeVarTuple>' ],
    '<TypeVar>': [
        'TypeVar(name=<identifier>(, bound=<expr>)?)'
    ],
    '<ParamSpec>': [
        'ParamSpec(name=<identifier>)'
    ],
    '<TypeVarTuple>': [
        'TypeVarTuple(name=<identifier>)'
    ]
    })
```

In Python 3.13 and later, several `<FunctionDef>` and `<arguments>` attributes are optional:

```python
# do import this unconditionally
if sys.version_info >= (3, 13):
    PYTHON_AST_DEFS_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_DEFS_GRAMMAR, {
    '<FunctionDef>': [
        'FunctionDef(name=<identifier>, args=<arguments>, body=<nonempty_stmt_list><decorator_list_param>?<returns>?<type_comment>?<type_params>?)'
    ],
    '<arguments>': [
        'arguments(<posonlyargs_param>?args=<arg_list><vararg>?<kwonlyargs_param>?<kw_defaults_param>?<kwarg>?<defaults_param>?)'
    ],
    })
```

```python
assert is_valid_grammar(PYTHON_AST_DEFS_GRAMMAR)
```

```python
for elt in [ '<arguments>', '<FunctionDef>' ]:
    print(elt)
    test_samples(PYTHON_AST_DEFS_GRAMMAR, start_symbol=elt)
    print()
```

### End of Excursion

### Excursion: Modules

We close with _modules_ – sequences of definitions.
After all the other definitions, this is now fairly straightforward.

```python
PYTHON_AST_MODULE_GRAMMAR: Grammar = extend_grammar(PYTHON_AST_DEFS_GRAMMAR, {
    '<start>': [ '<mod>' ],
    '<mod>': [ '<Module>' ],
    '<Module>': [ 'Module(body=<nonempty_stmt_list><type_ignore_param>)'],

    '<type_ignore_param>': [ ', type_ignores=<type_ignore_list>' ],
    '<type_ignore_list>': [ '[<type_ignores>?]' ],
    '<type_ignores>': [ '<type_ignore>', '<type_ignore>, <type_ignore>' ],
    '<type_ignore>': [ 'TypeIgnore(lineno=<integer>, tag=<string>)' ],
})
```

```python
# do import this unconditionally
if sys.version_info >= (3, 13):
    PYTHON_AST_MODULE_GRAMMAR: Grammar = \
        extend_grammar(PYTHON_AST_MODULE_GRAMMAR, {
        # As of 3.13, the type_ignore parameter is optional
        '<Module>': [ 'Module(body=<nonempty_stmt_list><type_ignore_param>?)'],
    })
```

```python
assert is_valid_grammar(PYTHON_AST_MODULE_GRAMMAR)
```

```python
for elt in [ '<Module>' ]:
    print(elt)
    test_samples(PYTHON_AST_MODULE_GRAMMAR, start_symbol=elt)
    print()
```

### End of Excursion

At this point, we have covered (almost) all AST elements of Python.
There would be a few more Python elements to consider (marked as `FIXME`, above), but we'll leave these to the reader.
Let us define `PYTHON_AST_GRAMMAR` as the official grammar coming out of this chapter.

```python
PYTHON_AST_GRAMMAR = PYTHON_AST_MODULE_GRAMMAR
python_ast_grammar = convert_ebnf_grammar(PYTHON_AST_GRAMMAR)
```

Here are a few (very weird) examples of Python functions we can produce.
All of these are valid, but only _syntactically_ – very few of the code samples produced this way will actually result in something meaningful.

```python
for elt in [ '<FunctionDef>' ]:
    print(elt)
    test_samples(PYTHON_AST_GRAMMAR, start_symbol=elt)
    print()
```

## A Class for Fuzzing Python

For convenience, let us introduce a class `PythonFuzzer` that makes use of the above grammar in order to produce Python code. This will be fairly easy to use.

```python
class PythonFuzzer(ISLaSolver):
    """Produce Python code."""

    def __init__(self,
                 start_symbol: Optional[str] = None, *,
                 grammar: Optional[Grammar] = None,
                 constraint: Optional[str] =None,
                 **kw_params) -> None:
        """Produce Python code. Parameters are:

        * `start_symbol`: The grammatical entity to be generated (default: `<FunctionDef>`)
        * `grammar`: The EBNF grammar to be used (default: `PYTHON__AST_GRAMMAR`); and
        * `constraint` an ISLa constraint (if any).

        Additional keyword parameters are passed to the `ISLaSolver` superclass.
        """
        if start_symbol is None:
            start_symbol = '<FunctionDef>'
        if grammar is None:
            grammar = PYTHON_AST_GRAMMAR
        assert start_symbol in grammar

        g = convert_ebnf_grammar(grammar)
        if constraint is None:
            super().__init__(g, start_symbol=start_symbol, **kw_params)
        else:
            super().__init__(g, constraint, start_symbol=start_symbol, **kw_params)

    def fuzz(self) -> str:
        """Produce a Python code string."""
        abstract_syntax_tree = eval(str(self.solve()))
        ast.fix_missing_locations(abstract_syntax_tree)
        return ast.unparse(abstract_syntax_tree)
```

By default, the `PythonFuzzer` will produce a _function definition_ - that is, a function header and body.

```python
fuzzer = PythonFuzzer()
print(fuzzer.fuzz())
```

By passing a start symbol as parameter, you can have `PythonFuzzer` produce arbitrary Python elements:

```python
fuzzer = PythonFuzzer('<While>')
print(fuzzer.fuzz())
```

Here is a list of all possible start symbols:

```python
sorted(list(PYTHON_AST_GRAMMAR.keys()))
```

## Customizing the Python Fuzzer

When fuzzing, you may be interested in _specific_ properties of the produced output. How can we influence the code that `PythonFuzzer` produces? We explore two ways:

* By adjusting the _grammar_ to our needs
* By adding _constraints_ that customize the output for us.

### Adjusting the Grammar

A simple way to adjust output generation is to _adapt the grammar_.

Let us assume you'd like to have function definitions without decorators.
To achieve this, you can _alter the rule that produces function definitions_:

```python
PYTHON_AST_GRAMMAR['<FunctionDef>']
```

As any AST rule, it comes in _abstract syntax_, so we first have to identify the element we'd like to adjust.
In our case, this is `decorator_list`.

Since decorator_list is a list, we can alter the rule to produce empty lists only.
To create a new adapted grammar, we do not alter the existing `PYTHON_AST_GRAMMAR`.
Instead, we use the `extend_grammar()` function to create a new grammar with a new, adapted rule for `<FunctionDef>`:

```python
python_ast_grammar_without_decorators: Grammar = extend_grammar(PYTHON_AST_GRAMMAR,
{
    '<FunctionDef>' :
        ['FunctionDef(name=<identifier>, args=<arguments>, body=<nonempty_stmt_list>, decorator_list=[])']
})
```

However, we're not done yet.
We also need to ensure that our grammar is _valid_, as any misspelled nonterminal identifier will result in problems during production.
For this, we use the `is_valid_grammar()` function:

```python
from ExpectError import ExpectError
```

```python
with ExpectError():
    assert is_valid_grammar(python_ast_grammar_without_decorators)
```

We see that with our change, our grammar has an _orphaned rule_: The `<returns>` rule is no longer used.
This is because `<returns>` is part of the `<type_annotation>` we just have deleted.
(`<type_annotation>` is still used when defining types for variables.)

To fix this, we need to delete the `<returns>` rule from our grammar.
Fortunately, we have a function `trim_grammar()`, which deletes all orphaned rules:

```python
python_ast_grammar_without_decorators = trim_grammar(python_ast_grammar_without_decorators)
```

With this, our grammar becomes valid...

```python
assert is_valid_grammar(python_ast_grammar_without_decorators)
```

... and we can use it for fuzzing - now without decorators:

```python
fuzzer = PythonFuzzer(grammar=python_ast_grammar_without_decorators)
print(fuzzer.fuzz())
```

Adjusting the grammar is straightforward once you understood the grammar structure, but the AST grammar is complex; also, your changes and extensions tie you closely to the grammar structure.
Carefully study how the individual rules are defined, above.

### Using Constraints for Customizing

A more elegant alternative to altering the grammar is to make use of _constraints_ that tune the grammar to your needs.
Since `PythonFuzzer` is derived from `ISLaSolver`, we can pass a `constraint` argument constraining the grammar, as discussed in the chapter on [fuzzing with constraints](FuzzingWithConstraints.ipynb).

If we want to have a function definition with 10 characters in each identifier, we make use of an ISLa constraint:

```python
fuzzer = PythonFuzzer(constraint='str.len(<id>) = 10')
print(fuzzer.fuzz())
```

We can also constrain individual children – say, the actual identifier of the function.

```python
# Also works (the <identifier> has quotes)
fuzzer = PythonFuzzer(constraint='<FunctionDef>.<identifier> = "\'my_favorite_function\'"')
print(fuzzer.fuzz())
```

Assume we want to test how the compiler handles large numbers. Let us define a constraint such that the function body (`<nonempty_stmt_list>`) contains at least one integer (`<integer>`) with a value of at least 1000:

```python
fuzzer = PythonFuzzer(constraint=
"""
    exists <integer> x:
        (inside(x, <nonempty_stmt_list>) and str.to.int(x) > 1000)
""")
print(fuzzer.fuzz())
```

Assume we'd like to test compilers with non-trivial functions. Here's how to define a constraint such that the function body has exactly _three_ statements (`<stmt>`). Note that this can take more than a minute to resolve, but the result definitely is a nontrivial function.

```python
# This will not work with ISLa 2
fuzzer = PythonFuzzer(constraint="""
    forall <FunctionDef> def: count(def, "<stmt>", "3")
""")
print(fuzzer.fuzz())
```

And finally, if we want the decorator list to be empty, as in our grammar-altering example, we can constrain the decorator list to be empty:

```python
# ignore
# with ExpectError(mute=True):
#     # Triggers an ISLa error (AssertionError)
#     fuzzer = PythonFuzzer(constraint='''
#         str.contains(<FunctionDef>, "decorator_list=[]")
#     ''')
#     print(fuzzer.fuzz())
```

```python
# ignore
# with ExpectError(mute=True):
#     # Triggers an ISLa error (AssertionError)
#     fuzzer = PythonFuzzer(constraint='<FunctionDef>.<expr_list> = "[]"')
#     print(fuzzer.fuzz())
```

```python
fuzzer = PythonFuzzer(constraint='<FunctionDef>..<expr_list> = "[]"')
print(fuzzer.fuzz())
```

## Mutating Code

When producing code for compilers (or actually, producing inputs in general), it is often a good idea to not just create _everything_ from scratch, but rather to _mutate_ existing inputs. This way, one can achieve a better balance between _common_ inputs (the ones to mutate) and _uncommon inputs_ (the new parts added via mutation).

### Parsing Inputs

To _mutate_ inputs, we first need to be able to _parse_ them. This is where a grammar is really put to test - can it really parse all possible code? This is why relying on an _existing_ parser that is tried and proven (in our case the Python parser) and operating on an _abstraction_ (in our case the AST) is really handy.

We already have seen how to parse code into an AST, using `ast.parse()`:

```python
def sum(a, b):    # A simple example
    the_sum = a + b
    return the_sum
```

```python
sum_source = inspect.getsource(sum)
sum_tree = ast.parse(sum_source)
print(ast.unparse(sum_tree))
```

```python
sum_str = ast.dump(sum_tree)
sum_str
```

Our grammar is able to parse this (non_trivial) string:

```python
solver = ISLaSolver(python_ast_grammar)
assert solver.check(sum_str)
```

To mutate the input, we first have to parse it into a _derivation tree_ structure. This is (again) a tree representation of the code, but this time, using the elements of _our_ grammar.

```python
sum_tree = solver.parse(sum_str)
```

Let us inspect what a derivation tree looks like. Alas, the string representation is very long and not that useful:

```python
len(repr(sum_tree))
```

```python
repr(sum_tree)[:200]
```

However, we can _visualize_ the derivation tree:

```python
from GrammarFuzzer import display_tree
```

```python
display_tree(sum_tree)
```

We see that a derivation tree consists of _nonterminal_ nodes whose children make up an _expansion_ from the grammar.
For instance, at the very top, we see that a `<start>` nonterminal expands into a `<mod>` nonterminal, which again expands into a `<Module>` nonterminal.
This comes right from the grammar rules

```python
python_ast_grammar['<start>']
```

and

```python
python_ast_grammar['<mod>']
```

The child of `<mod>` is a `<Module>`, which expands into the nodes

* `(body=`
* `<nonempty_stmt_list>`
* `, type_ignores=`
* `<type_ignore_list>`
* `)`

Here, nodes like `(body=` or `, type_ignores=` are called _terminal_ nodes (because they have no more elements to expand).
The nonterminals like `<nonempty_stmt_list>` get expanded further below – notably, `<nonempty_stmt_list>` expands into a `<FunctionDef>` node that represents the `sum()` definition.

Again, the structure exactly follows the `<Module>` definition in our grammar:

```python
python_ast_grammar['<Module>']
```

If we traverse the tree depth-first, left to right, and only collect the terminal symbols, we obtain the original string we parsed.
Applying the `str()` function to the derivation tree gets us exactly that string:

```python
str(sum_tree)
```

And again, we can convert this string into an AST and thus obtain our original function:

```python
sum_ast = ast.fix_missing_locations(eval(str(sum_tree)))
print(ast.unparse(sum_ast))
```

### Mutating Inputs

With derivation trees, we can have a _structured_ representation of our input. In our case, we already have that with ASTs, so why bother introducing a new one? The answer is simple: Derivation trees also allow us to _synthesize_ new inputs, because we have a _grammar_ that describes their structure.

Most notably, we can mutate inputs as follows:

1. Parse the input into a derivation tree, as shown above.
2. Randomly choose some node `<symbol>` in the derivation tree to be mutated.
3. Use the grammar to produce a new expansion for `<symbol>`.
4. Replace the children of `<symbol>` by the expansion just generated.
5. Repeat the process as often as needed.

This is a decent programming task, and if you'd like a blueprint, have a look at the `FragmentMutator` in this tutorial on [greybox fuzzing with grammars](https://www.fuzzingbook.org/html/GreyboxGrammarFuzzer.html).

Fortunately, ISLa already provides us with functionality that does exactly this.
The `ISLaSolver.mutate()` method takes an input and mutates it according to the rules in the grammar.
The input to mutate can be given as a derivation tree, or as a string; its output is a derivation tree (which can again be converted into a string).

Let us apply `mutate()` on our `sum()` function. The `min_mutations` and `max_mutations` parameters define how many mutation steps should be performed; we set both to 1 in order to have exactly one mutation.

```python
sum_mutated_tree = solver.mutate(sum_str, min_mutations=1, max_mutations=1)
```

```python
sum_mutated_ast = ast.fix_missing_locations(eval(str(sum_mutated_tree)))
print(ast.unparse(sum_mutated_ast))
```

Toy with the above to see the effect of a mutation.
Note if one of the top-level nodes (like `<FunctionDef>` or `<Module>`) is selected for mutation, then `sum()` will be replaced by something entirely different. Otherwise, though, the code will still be pretty similar to the original `sum()` code.

Of course, the more we increase the number of mutations, the more different the code will look like:

```python
sum_mutated_tree = solver.mutate(sum_str, min_mutations=10, max_mutations=20)
```

```python
sum_mutated_ast = ast.fix_missing_locations(eval(str(sum_mutated_tree)))
print(ast.unparse(sum_mutated_ast))
```

By toying with the `mutate()` parameters, we can control how _common_ and how _uncommon_ our input should be.

### How Effective is Mutation?

Does mutating existing code help us in finding bugs?
Let us assume we have a buggy compiler that generates bad code for an expression of the form `<elem> * (<elem> + <elem>)`.
The code in `has_distributive_law()` checks an AST for the presence of this bug:

```python
def has_distributive_law(tree) -> bool:
    for node in walk(tree):  # iterate over all nodes in `tree`
        # print(node)
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Mult):
                if isinstance(node.right, ast.BinOp):
                    if isinstance(node.right.op, ast.Add):
                        return True

                if isinstance(node.left, ast.BinOp):
                    if isinstance(node.left.op, ast.Add):
                        return True

    return False
```

To understand how this works, a visualization of the AST comes in handy:

```python
show_ast(ast.parse("1 + (2 * 3)"))
```

```python
has_distributive_law(ast.parse("1 * (2 + 3)"))
```

```python
has_distributive_law(ast.parse("(1 + 2) * 3"))
```

```python
has_distributive_law(ast.parse("1 + (2 * 3)"))
```

```python
has_distributive_law(ast.parse("def f(a, b):\n    return a * (b + 10)"))
```

How many attempts does it take for each until we find a mutation that triggers the bug in `has_distributive_law()`?
Let us write a function that computes this number.

```python
def how_many_mutations(code: str) -> int:
    solver = ISLaSolver(python_ast_grammar)

    code_ast = ast.parse(code)
    code_ast = ast.fix_missing_locations(code_ast)
    code_ast_str = ast.dump(code_ast)
    code_derivation_tree = solver.parse(code_ast_str)
    mutations = 0
    mutated_code_ast = code_ast

    while not has_distributive_law(mutated_code_ast):
        mutations += 1
        if mutations % 100 == 0:
            print(f'{mutations}...', end='')

        mutated_code_str = str(solver.mutate(code_derivation_tree))
        mutated_code_ast = eval(mutated_code_str)
        # mutated_code_ast = ast.fix_missing_locations(mutated_code_ast)
        # print(ast.dump(mutated_code_ast))
        # print(ast.unparse(mutated_code_ast))

    return mutations
```

If we pass an input that already exhibits the bug, we do not need any mutation:

```python
assert how_many_mutations('1 * (2 + 3)') == 0
```

However, the further we are away from the bug, the more mutations (and the more time) it takes to find it.
Notably, mutating `2 + 2` until we have a distributive law still is much faster than mutating `2`.

```python
how_many_mutations('2 + 2')    # <-- Note: this can take a minute
```

```python
how_many_mutations('2')  # <-- Note: this can take several minutes
```

We conclude that mutating existing code can indeed be helpful, especially if it is syntactically _close to inputs that trigger bugs_.
If you want to have a good chance in finding bugs, focus on _inputs that have triggered bugs before_ – sometimes a simple mutation of these already helps finding a new bug.

## Evolutionary Fuzzing

One interesting application of mutating inputs is to use mutations for _evolutionary fuzzing_.
The idea is to have a population of inputs, to apply _mutations_ on them, and to check whether they improve on a particular goal (mostly code coverage).
Those inputs that _do_ improve are being retained ("survival of the fittest") as the next generation, and evolved further.
By repeating this process often enough, we may obtain inputs that cover large parts of code and thus improve chances to uncover bugs.

Let us assume we have a buggy compiler that generates bad code for an expression of the form `<elem> * (<elem> + <elem>)`.
The function `has_distributive_law()`, above, checks an AST for the presence of this bug.

Our aim is to detect this bug via fuzzing. But if we simply generate random inputs from scratch, it may take a long time until we generate the exact copmbination of operators that triggers the bug.

### Getting Coverage

To have our fuzzers guided by coverage, we first need to _measure_ code coverage.
We make use of the [Coverage module from the Fuzzing Book](https://www.fuzzingbook.org/html/Coverage.html), which is particularly easy to use.
It simply uses a `with` clause to obtain coverage from the code in the `with` body.
Here is how to obtain coverage for our `has_distributive_law()` code, above:

```python
from Coverage import Coverage
```

```python
mult_ast = ast.parse("1 * 2")
with Coverage() as cov:
    has_distributive_law(mult_ast)
```

The `coverage()` method tells us which lines in the code actually have been reached.
This includes lines from `has_distributive_law()`, but also lines from other functions called.

```python
cov.coverage()
```

Which are the lines executed?
With a bit of code inspection, we can easily visualize the covered lines:

```python
def show_coverage(cov, fun):
    fun_lines, fun_start = inspect.getsourcelines(fun)
    fun_name = fun.__name__
    coverage = cov.coverage()
    for line in range(len(fun_lines)):
        if (fun_name, line + fun_start) in coverage:
            print('# ', end='')  # covered lines
        else:
            print('  ', end='')  # uncovered lines
        print(line + fun_start, fun_lines[line], end='')
```

```python
show_coverage(cov, has_distributive_law)
```

In this listing, a `#` indicates that the code has been executed (covered).
We see that our input "1 * 2" satisfies the conditions in Lines 4 and 5, but does not satisfy the conditions in later lines.

### Fitness

Let us now use coverage as a _fitness function_ to guide evolution.
The higher the fitness (the coverage), the higher the chances of an input to be retained for further evolution.
Our `ast_fitness()` function simply counts the number of lines covered in `has_distributive_law()`.

```python
def ast_fitness(code_ast) -> int:
    with Coverage() as cov:
        has_distributive_law(code_ast)
    lines = set()
    for (name, line) in cov.coverage():
        if name == has_distributive_law.__name__:
            lines.add(line)
    return len(lines)
```

Here is the fitness of a number of given inputs:

```python
ast_fitness(ast.parse("1"))
```

```python
ast_fitness(ast.parse("1 + 1"))
```

```python
ast_fitness(ast.parse("1 * 2"))
```

```python
ast_fitness(ast.parse("1 * (2 + 3)"))
```

Now, let's set up a fitness function that takes derivation trees.
Essentially, our `tree_fitness()` function is based on the `ast_fitness()` function, above;
however, we also add a small component `1 / len(code_str)` to give extra fitness to shorter inputs.
Otherwise, our inputs may grow and keep on growing, making mutations inefficient.

```python
def tree_fitness(tree) -> float:
    code_str = str(tree)
    code_ast = ast.fix_missing_locations(eval(code_str))
    fitness = ast_fitness(code_ast)
    # print(ast.unparse(code_ast), f"\n=> Fitness = {fitness}\n")
    return fitness + 1 / len(code_str)
```

```python
tree_fitness(sum_tree)
```

### Evolving Inputs

Let us now make use of our fitness function to implement a simple evolutionary fuzzing algorithm.
We start with _evolution_ – that is, taking a population and adding offspring via mutations.
Our initial population consists of a single candidate – in our case, `sum_tree` reflecting the `sum()` function, above.

```python
def initial_population(tree):
    return [ (tree, tree_fitness(tree)) ]
```

```python
sum_population = initial_population(sum_tree)
```

```python
len(sum_population)
```

Our `evolve()` function adds two new children to each population member.

```python
OFFSPRING = 2
```

```python
def evolve(population, min_fitness=-1):
    solver = ISLaSolver(python_ast_grammar)

    for (candidate, _) in list(population):
        for i in range(OFFSPRING):
            child = solver.mutate(candidate, min_mutations=1, max_mutations=1)
            child_fitness = tree_fitness(child)
            if child_fitness > min_fitness:
                population.append((child, child_fitness))
    return population
```

```python
sum_population = evolve(sum_population)
len(sum_population)
```

As we can evolve all these, too, we get an exponential growth.

```python
sum_population = evolve(sum_population)
len(sum_population)
```

```python
sum_population = evolve(sum_population)
len(sum_population)
```

```python
sum_population = evolve(sum_population)
len(sum_population)
```

```python
sum_population = evolve(sum_population)
len(sum_population)
```

### Survival of the Fittest

No population can expand forever and still survive.
Let us thus limit the population to a certain size.

```python
POPULATION_SIZE = 100
```

The `select()` function implements survival of the fittest: It limits the population to at most `POPULATION_SIZE` elements, sorting them by their fitness (highest to lowest).
Members with low fitness beyond `POPULATION_SIZE` do not survive.

```python
def get_fitness(elem):
    (candidate, fitness) = elem
    return fitness

def select(population):
    population = sorted(population, key=get_fitness, reverse=True)
    population = population[:POPULATION_SIZE]
    return population
```

We can use the following call to trim our `sum_population` to the fittest members:

```python
sum_population = select(sum_population)
len(sum_population)
```

### Evolution

We now have everything in place:

* We have a _population_ (say, `sum_population`)
* We can evolve the population (using `evolve()`)
* We can have only the fittest survive (using `select()`)

Let us repeat this process over several generations.
We track whenever we have found a new "best" candidate and log them.
If we find a candidate that triggers the bug, we stop.
Note that this may take a long time, and not necessarily yield a perfect result.

As common in search-based approaches, we stop and restart the search if we have not found a sufficient solution after a number of generations (here: `GENERATIONS`).
Other than that, we keep searching until we have a solution.

```python
GENERATIONS = 100  # Upper bound
```

```python
trial = 1
found = False

while not found:
    sum_population = initial_population(sum_tree)
    prev_best_fitness = -1

    for generation in range(GENERATIONS):
        sum_population = evolve(sum_population, min_fitness=prev_best_fitness)
        sum_population = select(sum_population)
        best_candidate, best_fitness = sum_population[0]
        if best_fitness > prev_best_fitness:
            print(f"Generation {generation}: found new best candidate (fitness={best_fitness}):")
            best_ast = ast.fix_missing_locations(eval(str(best_candidate)))
            print(ast.unparse(best_ast))
            prev_best_fitness = best_fitness

            if has_distributive_law(best_ast):
                print("Done!")
                found = True
                break

    trial = trial + 1
    print(f"\n\nRestarting; trial #{trial}")
```

Success! We found a piece of code that triggers the bug. Check for occurrences of the distributive law.

```python
print(ast.unparse(best_ast))
```

```python
assert has_distributive_law(best_ast)
```

You may note that not all of the code is required to trigger the bug.
We could run our evolutionary fuzzer a bit longer to see whether it can be further reduced,
or use a dedicated input reduction technique such as [Delta Debugging](https://www.fuzzingbook.org/html/Reducer.html).

### Chances of Evolutionary Fuzzing

Could the bug in `distributive_law()` have been found without evolutionary guidance - i.e., simply by applying one mutation to `sum()`?

When producing an expression (`<expr>`), we calculate how big the chances are to

* Produce a binary operator, and
* Produce a `*`, and
* Produce another binary operator as one child, and
* Produce a `+`

Let's do a few queries on our grammar to compute the chances.

```python
assert '<BinOp>' in python_ast_grammar['<expr>']
```

```python
len(python_ast_grammar['<expr>'])
```

```python
assert 'Add()' in python_ast_grammar['<operator>']
assert 'Mult()' in python_ast_grammar['<operator>']
```

```python
len(python_ast_grammar['<operator>'])
```

```python
(len(python_ast_grammar['<expr>'])       # chances of choosing a `BinOp`
* len(python_ast_grammar['<operator>'])  # chances of choosing a `*`
* len(python_ast_grammar['<expr>'])      # chances of choosing a `BinOp` as a child
* len(python_ast_grammar['<operator>'])  # chances of choosing a `+`
/ 2)   # two chances - one for the left child, one for the right
```

On average, it would take about 19000 (non-evolutionary) runs until we have an expression that triggers the distributive law.
So it is definitely better to make use of additional information (say, coverage) in order to guide mutations towards a goal.

## Synopsis

This chapter provides a `PythonFuzzer` class that allows producing arbitrary Python code elements:

```python
fuzzer = PythonFuzzer()
print(fuzzer.fuzz())
```

By default, `PythonFuzzer` produces a _function definition_ – that is, a list of statements as above.
You can pass a `start_symbol` argument to state which Python element you'd like to have:

```python
fuzzer = PythonFuzzer('<While>')
print(fuzzer.fuzz())
```

Here is a list of all possible start symbols. Their names reflect the nonterminals from the [Python `ast` module documentation](https://docs.python.org/3/library/ast.html).

```python
sorted(list(PYTHON_AST_GRAMMAR.keys()))
```

If you'd like more control over Python code generation, here is what is happening behind the scenes.
The EBNF grammar `PYTHON_AST_GRAMMAR` can parse and produce _abstract syntax trees_ for Python.
To produce a Python module without `PythonFuzzer`, you would take these steps:

**Step 1:** Create a non-EBNF grammar suitable for `ISLaSolver` (or any other grammar fuzzer):

```python
python_ast_grammar = convert_ebnf_grammar(PYTHON_AST_GRAMMAR)
```

**Step 2:**  Feed the resulting grammar into a grammar fuzzer such as ISLa:

```python
solver = ISLaSolver(python_ast_grammar, start_symbol='<FunctionDef>')
```

**Step 3:**  Have the grammar fuzzer produce a string. This string represents an AST.

```python
ast_string = str(solver.solve())
ast_string
```

**Step 4:**  Convert the AST into an actual Python AST data structure.

```python
from ast import *
```

```python
abstract_syntax_tree = eval(ast_string)
```

**Step 5:** Finally, convert the AST structure back into readable Python code:

```python
ast.fix_missing_locations(abstract_syntax_tree)
print(ast.unparse(abstract_syntax_tree))
```

The chapter has many more applications, including parsing and mutating Python code, evolutionary fuzzing, and more.

Here are the details on the `PythonFuzzer` constructor:

```python
# ignore
import inspect
import markdown
from bookutils import HTML
```

```python
# ignore
sig = inspect.signature(PythonFuzzer.__init__)
sig_str = str(sig) if sig else ""
doc = inspect.getdoc(PythonFuzzer.__init__) or ""
HTML(markdown.markdown('`PythonFuzzer' + sig_str + '`\n\n' + doc))
```

```python
# ignore
from ClassDiagram import display_class_hierarchy
```

```python
# ignore
display_class_hierarchy([PythonFuzzer],
                        public_methods=[
                            PythonFuzzer.__init__,
                            PythonFuzzer.fuzz,
                            ISLaSolver.__init__
                        ],
                        project='fuzzingbook')
```

## Lessons Learned

* When creating and processing complex inputs such as program code,
  * try to rely on existing infrastructure to _parse_ inputs into some _abstract syntax_, and then
  * have your grammars _process that abstract syntax_ rather than the concrete syntax.
* Specifically, program code is normally converted into _abstract syntax trees_ before being compiled or interpreted, and you can (and should) make use of such conversions.
* Once program code is turned into an AST, it is fairly easy to generate, mutate, and evolve despite its complexity.

## Background

The seminal work on compiler testing is _Csmith_ \cite{Yang2011}, a generator of C programs.
Csmith has been used to thoroughly test compilers such as Clang or GCC; beyond producing code that is syntactically correct, it also aims at _semantic_ correctness as well as avoiding undefined and unspecified behaviors.
This is a must read for anyone in the field in compiler testing.