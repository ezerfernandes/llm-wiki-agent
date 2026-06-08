# Fuzzing with Constraints

In previous chapters, we have seen how [Grammar-Based Fuzzing](GrammarFuzzer.ipynb) allows us to efficiently generate myriads of syntactically valid inputs.
However, there are _semantic_ input features that cannot be expressed in a context-free grammar, such as

* "$X$ is the length of $Y$";
* "$X$ is an identifier previously declared"; or
* "$X$ should be longer than 4,096 bytes".

In this chapter, we show how the [ISLa](https://rindphi.github.io/isla/) framework allows us to express such features as _constraints_ added to a grammar.
By having ISLa solve these constraints automatically, we produce inputs that are not only _syntactically_ valid, but actually _semantically_ valid.
Furthermore, such constraints allow us to very precisely _shape_ the inputs we want for testing.

```python
from bookutils import YouTubeVideo
YouTubeVideo("dgaGuwn-1OU")
```

**Prerequisites**

* You should have read the [chapter on grammars](Grammars.ipynb).
* The chapter on [generators and filters](GeneratorGrammarFuzzer.ipynb) addresses a similar problem, but with program code instead of constraints.

```python
import bookutils.setup
```

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
>>> from fuzzingbook.FuzzingWithConstraints import <identifier>
```

and then make use of the following features.


This chapter introduces the [ISLa](https://rindphi.github.io/isla/) framework, consisting of 
* the _ISLa specification language_, allowing to add _constraints_ to a grammar
* the _ISLa solver_, solving these constraints to produce semantically (and syntactically) valid inputs
* the _ISLa checker_, checking given inputs for whether they satisfy these constraints.

A typical usage of the ISLa solver is as follows.
First, install ISLa, using 
```shell
$ pip install isla-solver
```
Then, you can import the solver as

```python
>>> from isla.solver import ISLaSolver  # type: ignore
```
The ISLa solver needs two things. First, a _grammar_ - say, US phone numbers.

```python
>>> from Grammars import US_PHONE_GRAMMAR
```
Second, you need _constraints_ – a string expressing a condition over one or more grammar elements.
Common functions include
* `str.len()`, returning the length of a string
* `str.to.int()`, converting a string to an integer

Here, we instantiate the ISLa solver with a constraint stating that the area code should be above 900:

```python
>>> solver = ISLaSolver(US_PHONE_GRAMMAR, 
>>>             """
>>>             str.to.int(<area>) > 900
>>>             """)
```
With that, invoking `solver.solve()` returns a _solution_ for the constraints.

```python
>>> str(solver.solve())
'(902)805-6934'
```
`solve()` returns a derivation tree, which typically is converted into a string using `str()` as above. The `print()` function does this implicitly.

Subsequent calls of `solve()` return more solutions:

```python
>>> for _ in range(10):
>>>     print(solver.solve())
(902)671-8520
(902)308-8044
(902)737-2584
(902)500-2834
(902)429-5794
(902)292-0499
(902)977-9111
(902)209-4775
(902)565-2710
(909)223-7794

```
We see that the solver produces a number of inputs that all satisfy the constraint - the area code is always more than 900.

The `ISLaSolver()` constructor provides several additional parameters to configure the solver, as documented below.
Additional `ISLaSolver` methods allow checking inputs against constraints, and provide additional functionality.

![](PICS/FuzzingWithConstraints-synopsis-1.svg)

The ISLa functionality is also available on the command line:

```python
>>> !isla --help
usage: isla [-h] [-v]
            {solve,fuzz,check,find,parse,repair,mutate,create,config} ...

The ISLa command line interface.

options:
  -h, --help            show this help message and exit
  -v, --version         Print the ISLa version number

Commands:
  {solve,fuzz,check,find,parse,repair,mutate,create,config}
    solve               create solutions to ISLa constraints or check their
                        unsatisfiability
    fuzz                pass solutions to an ISLa constraint to a test subject
    check               check whether an input satisfies an ISLa constraint
    find                filter files satisfying syntactic & semantic
                        constraints
    parse               parse an input into a derivation tree if it satisfies
                        an ISLa constraint
    repair              try to repair an existing input such that it satisfies
                        an ISLa constraint
    mutate              mutate an input such that the result satisfies an ISLa
                        constraint
    create              create grammar and constraint stubs
    config              dumps the default configuration file

```


## Semantic Input Properties

In this book, we have frequently used [grammars](Grammars.ipynb) to [systematically generate inputs](GrammarFuzzer.ipynb) that [cover input structure](GrammarCoverageFuzzer.ipynb) and more.
But while it is relatively easy to express the _syntax_ of an input using a grammar, there are input properties that _cannot_ be expressed using a grammar.
Such input properties are called _semantic_ properties.

Let us illustrate semantic properties using a simple example.
We want to test some system that is configured by two settings, a _page size_ and a _buffer size_. 
Both these come as integer numbers as part of a human-readable configuration file.
The _syntax_ of this file is given by the following grammar:

```python
from Grammars import Grammar, is_valid_grammar, syntax_diagram, crange
```

```python
import string
```

```python
CONFIG_GRAMMAR: Grammar = {
    "<start>": ["<config>"],
    "<config>": [
        "pagesize=<pagesize>\n"
        "bufsize=<bufsize>"
    ],
    "<pagesize>": ["<int>"],
    "<bufsize>": ["<int>"],
    "<int>": ["<leaddigit><digits>"],
    "<digits>": ["", "<digit><digits>"],
    "<digit>": list("0123456789"),
    "<leaddigit>": list("123456789")
}
```

```python
assert is_valid_grammar(CONFIG_GRAMMAR)
```

Here's a visualization of this grammar as a railroad diagram, showing its structure:

```python
# ignore
syntax_diagram(CONFIG_GRAMMAR)
```

Using this grammar, we can now use any of our grammar-based fuzzers to generate valid inputs.
For instance:

```python
from GrammarFuzzer import GrammarFuzzer, DerivationTree
```

```python
fuzzer = GrammarFuzzer(CONFIG_GRAMMAR)
```

```python
for i in range(10):
    print(i)
    print(fuzzer.fuzz())
```

So far, so good - and indeed, these random values will help us test our (hypothetical) system.
But what if we want to _control_ these values further, putting our system to the test?

A grammar gives us _some_ control. If we want to ensure a page size of at least 100,000, for instance, a rule like
```python
"<bufsize>": ["<leaddigit><digit><digit><digit><digit><digit>"]
```
would do the job.
We could also express that the page size should be an odd number, by having it end in an odd digit.
But if we want to state that the page size should be, say, a multiple of 8, or larger or less than the buffer size, we are out of luck.

In the [chapter on fuzzing with generators](GeneratorGrammarFuzzer.ipynb), we have seen how to attach _program code_ to individual rules - program code that would either _generate_ individual elements right away or _filter_ only these that satisfy specific conditions.

Attaching code makes things very flexible, but also has several disadvantages:

* First, it is pretty hard to generate inputs that satisfy multiple constraints at once.
In essence, you have to code your own _strategy_ for generating inputs, which at some point negates the advantage of having an abstract representation such as a grammar.
* Second, your code is not portable. While a grammar can be easily adapted to _any_ grammar-based fuzzer, adding, say, Python code, ties you to the Python environment forever.
* Third, program code can only be used for _producing_ inputs or _checking_ inputs, but not both. This, again, is a downside compared to a pure grammar representation.

Hence, we are looking to a more _general_ way to express semantic properties - and also a more _declarative_ way to express semantic properties.

### Excursion: Unrestricted Grammars

One very general solution to this problem would be to use _unrestricted_ grammars rather than the _context-free_ grammars we have used so far.
In an unrestricted grammar, one can have multiple symbols also on the left-hand side of an expansion rule, making them very flexible.
In fact, unrestricted grammars are _Turing-universal_, meaning that they can express any feature that could also be expressed in program code; and they could thus check and produce arbitrary strings with arbitrary features. (If they finish, that is – unrestricted grammars also suffer from the halting problem.)
The downside is that there is literally no programming support for unrestricted grammars – we'd have to implement all arithmetic, strings, and other functionality from scratch in a grammar, which is - well - not fun.

### End of Excursion

## Specifying Constraints

In recent work, _Dominic Steinhöfel_ and _Andreas Zeller_ (one of the authors of this book) have presented an infrastructure that allows producing inputs with _arbitrary properties_, but without having to go through the trouble of implementing producers or checkers.
Instead, they suggest a dedicated _language_ for specifying inputs, named [ISLa](https://rindphi.github.io/isla/) (for input specification language).
_ISLa_ combines a standard context-free _grammar_ with _constraints_ that express _semantic_ properties of the inputs and their elements.
ISLa can be used as a _fuzzer_ (producing inputs that satisfy the constraints) as well as a _checker_ (checking inputs whether they satisfy the given constraints).

Let us illustrate ISLa by example. ISLa comes as a Python package named `isla-solver` that can be easily installed using `pip`:

```shell
$ pip install isla-solver
```

This also installs all dependent packages.

The core of ISLa is the _ISLa Solver_ – the component that actually _solves_ constraints to produce satisfying inputs.

```python
import isla  # type: ignore
```

```python
from isla.solver import ISLaSolver  # type: ignore
```

The constructor of an `ISLaSolver` takes two mandatory arguments.
* The _grammar_ is the grammar the solver should produce inputs from.
* The _constraint_ is the constraint the produced inputs should satisfy.

To express a constraint, we have a variety of _functions_ and _predicates_ at our disposition.
These can be applied to individual elements of the grammar, notably their nonterminals.
The function `str.len()`, for instance, returns the length of a string.
If we want to have inputs in which the page size has at least 6 digits, we can write:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 'str.len(<pagesize>) >= 6')
```

The method `solve()` returns the next produced string from the ISLa solver, as a _derivation tree_ (seen in the [Chapter on fuzzing with grammars](GrammarFuzzer.ipynb)).
To convert these into a string, we can use the `str()` converter:

```python
str(solver.solve())
```

The `print()` method converts its arguments to strings implicitly.
To get, say, the next 10 solutions, we can thus write

```python
for _ in range(10):
    print(solver.solve())
```

... and we see that, indeed, each page size has exactly six digits.

### Excursion: Derivation Trees

If you inspect a derivation tree as returned from `solve()` directly, you will get quite a structure:

```python
solution = solver.solve()
solution
```

We can easily visualize the tree, revealing its structure:

```python
# ignore
from Parser import EarleyParser  # minor dependency
from GrammarFuzzer import display_tree
```

```python
display_tree(solution)
```

By converting the derivation tree into a string, we get the represented string:

```python
str(solution)
```

`print()` does this implicitly, so `print`ing the solution gives us the string:

```python
print(solution)
```

Unless you want to inspect the derivation tree or access its elements, converting it into a string makes it more manageable.

### End of Excursion

To express a minimum numeric value, we can use a more elegant way.
The function `str.to.int()`, for instance, converts a string into an integer.
To obtain a page size that of at least 100000, we can thus also write

```python
solver = ISLaSolver(CONFIG_GRAMMAR,
                    'str.to.int(<pagesize>) >= 100000')
```

```python
print(solver.solve())
```

If we want the page size to be in the range of 100 to 200, we can state this as a logical conjunction (using `and`)

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
                    '''
                    str.to.int(<pagesize>) >= 100 and 
                    str.to.int(<pagesize>) <= 200
                    ''')
print(solver.solve())
```

And if we want the page size to be a multiple of seven, we can write

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
                    '''
                    str.to.int(<pagesize>) mod 7 = 0
                    ''')
print(solver.solve())
```

```python
from bookutils import quiz
```

```python
quiz("Which of the following constraints expresses "
     "that the page size and the buffer size "
     "have to be equal? Try it out!",
     [
         "`<pagesize> is <bufsize>`",
         "`str.to.int(<pagesize>) = str.to.int(<bufsize>)`",
         "`<pagesize> = <bufsize>`",
         "`atoi(<pagesize>) == atoi(<bufsize>)`",
     ], "[4 ** 0.5, 9 ** 0.5]")
```

Indeed, ISLa constraints can also involve multiple elements. Expressing equality between two elements is easy, and uses a single equal sign. (There's no assignment in ISLa the `=` could be confused with.)

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
                    '''
                    <pagesize> = <bufsize>
                    ''')
print(solver.solve())
```

We can also use numerical constraints, stating that the buffer size should always be exactly one more than the page size:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
                    '''
                    str.to.int(<pagesize>) > 1024 and
                    str.to.int(<bufsize>) = str.to.int(<pagesize>) + 1
                    ''')
print(solver.solve())
```

All the above functions (like `str.to.int()`) actually stem from the _SMT-LIB_ library for _satisfiability modulo theories_ (SMT), a standard for expressing constraints for constraint solvers (like ISLa).
The [list of all theories defined in SMT-LIB](https://smtlib.cs.uiowa.edu/theories.shtml) lists dozens of functions and predicates that can be used in ISLa constraints.

```python
quiz("Which constraints are necessary to "
     "ensure that all digits are between 1 and 3?",
     [
         "`str.to.int(<digit>) >= 1`",
         "`str.to.int(<digit>) <= 3`",
         "`str.to.int(<leaddigit>) >= 1`",
         "`str.to.int(<leaddigit>) <= 3`",
     ], "[1 ** 0, 4 ** 0.5, 16 ** 0.5]")
```

### Excursion: Using SMT-LIB Syntax

Instead of the above "infix" syntax which is familiar to programmers, ISLa also supports full SMT-LIB syntax.
Instead of writing $f(x_1, x_2, x_3, \dots)$ for a function $f$ and its arguments $x_1 \dots x_n$, SMT-LIB uses a "prefix" LISP-like syntax in which all functions and operators are written as $(f x_1 x_2 x_3 \dots)$.
The above predicate would thus be written as

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
                '''
                (and
                  (> (str.to.int <pagesize>) 1024)
                  (= (str.to.int <bufsize>)
                     (+ (str.to.int <pagesize>) 1)))
                ''')
print(solver.solve())
```

Note that for boolean operators such as `and`, we still use the ISLa infix syntax; having ISLa handle these operators is more efficient than passing them on to the constraint solver.

### End of Excursion

## ISLa on the Command Line

When you install `isla-solver`, you also get an `isla` command-line tool.
This allows you to create inputs from the command line or shell scripts.

Let us first create a _grammar file_ suitable for `isla`. `isla` accepts grammars in Fuzzingbook format; they need to define a variable named `grammar`.

```python
with open('grammar.py', 'w') as f:
    f.write('grammar = ')
    f.write(str(CONFIG_GRAMMAR))
```

```python
from bookutils import print_file
```

```python
print_file('grammar.py')
```

With this, we can use `isla` as a grammar fuzzer, plain and simple
By default, `isla solve` produces one single matching output:

```python
!isla solve grammar.py
```

The true power of `isla`, however, comes to be as we (again) add _constraints_ to be solved - either in separate _constraint files_ or (easier) directly on the command line:

```python
!isla solve grammar.py --constraint '<pagesize> = <bufsize>'
```

```python
!isla solve grammar.py \
    --constraint '<pagesize> = <bufsize> and str.to.int(<pagesize>) > 10000'
```

The `isla` executable provides several options and commands, and is a great alternative on the command line.

```python
!isla --help
```

## Accessing Elements

So far, we have accessed nonterminals simply by referencing their name, as in `<bufsize>` or `<pagesize>`.
However, in some cases, this simple method is not sufficient.
In our configuration grammar, for instance, we may want to access (or constrain) `<int>` elements.
However, we do not want to constrain _all_ integers at once, but only those in a particular _context_ – say, those that occur as a part of a `<pagesize>` element, or only those that occur as part of a `<config>` element.

To this end, ISLa allows referencing _parts_ of a given element, using two special operators.

The expression `<a>.<b>` refers to the _immediate_ subpart `<b>` of some element `<a>`.
That is, `<b>` has to appear in one of the expansion rules of `<a>`.
For instance, `<pagesize>.<int>` refers to the `<int>` element of a page size.
Here is an example using the dot operator:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
                '''
                <pagesize>.<int> = <bufsize>.<int>
                ''')
print(solver.solve())
```

The expression `<a>..<b>`, however, refers to _any_ subpart `<b>` of some element `<a>`. That is, `<b>` can appear in the expansion of `<a>`, but also in the expansion of any subelement (and any subelement thereof).
Here is an example using the double dot operator, enforcing _every_ digit in a `<config>` element to be `7`:

```python
from ExpectError import ExpectError
```

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            <config>..<digit> = "7" and <config>..<leaddigit> = "7"
            ''')
print(solver.solve())
```

To reason about dots and double dots, it helps to visualize the string in question as a _derivation tree_ discussed in the [chapter on grammar-based fuzzing](GrammarFuzzer.ipynb).
The derivation tree of the input 
```
pagesize=12
bufsize=34
```
for instance, looks like this:

```python
# ignore
inp = 'pagesize=12\nbufsize=34'
parser = EarleyParser(CONFIG_GRAMMAR)
tree = next(parser.parse(inp))
display_tree(tree)
```

In this tree, the `.` syntax refers to _immediate_ children. `<bufsize>.<int>` is the one `<int>` node that is the immediate descendant of `<bufsize>` (but not any other `<int>` node).
In contrast, `<config>..<digit>` refers to _all_ `<digit>` descendants of the `<config>` node.

If an element has multiple *immediate* children of the same type, one can use the special `<a>[$n$]` syntax to access the $n$-th child of type `<a>`. To access the first child, $n$ is equal to one, not zero, as in the [XPath abbreviated syntax](https://www.w3.org/TR/1999/REC-xpath-19991116/#path-abbrev). In our configuration grammar, there is no expansion including the same nonterminal more than once, so we do not need this feature.

For a demonstration of indexed dots, consider the following grammar, which produces lines of three "a" or "b" characters:

```python
LINES_OF_THREE_AS_OR_BS_GRAMMAR: Grammar = {
    '<start>': ['<A>'],
    '<A>': ['<B><B><B>', '<B><B><B>\n<A>'],
    '<B>': ['a', 'b']
}
```

```python
fuzzer = GrammarFuzzer(LINES_OF_THREE_AS_OR_BS_GRAMMAR)
for i in range(5):
    print(i)
    print(fuzzer.fuzz())
```

We can force, say, the second character in a line to always be a "b:"

```python
solver = ISLaSolver(LINES_OF_THREE_AS_OR_BS_GRAMMAR, 
            '''
            <A>.<B>[2] = "b"
            ''')

for i in range(5):
    print(i)
    print(solver.solve())
```

## Quantifiers

By default, all nonterminals in ISLa constraints are _universally_ quantified - that is, any constraint applying to, say, some `<int>` element applies to _all_ `<int>` elements in the resulting string.
If you only want to constrain _one_ element, though, you have to (and can) specify this in ISLa, using an _existential quantifier_.

To use an existential quantifier in ISLa, use the construct
```
exists TYPE VARIABLE in CONTEXT:
    (CONSTRAINT)
```
where `VARIABLE` is some identifier, `TYPE` is its type (as a nonterminal), and `CONTEXT` is the context (again a nonterminal) in which the constraint should hold.
`CONSTRAINT` is again a constraint expression, in which you now can make use of `VARIABLE` as the element whose existence you assume.

Let us illustrate existential quantification again using a simple example.
We want to make sure that at least one integer in our generated string has a value of more than 1000.
So we write

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            exists <int> i in <start>:
                str.to.int(i) > 1000
            ''')

for _ in range(10):
    print(solver.solve())
```

We note that all generated inputs satisfy the constraint of having at least one integer that satisfies the constraint.

Specifying a variable name is optional; if you omit it, you can use the quantified nonterminal instead.
The above constraint can thus also be expressed in a more compact fashion:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            exists <int> in <start>:
                str.to.int(<int>) > 1000
            ''')

print(solver.solve())
```

Besides existential quantification, there also is _universal_ quantification, using the `forall` keyword instead of `exists`.
If we want _all_ elements in some context to satisfy a constraint, this comes in handy.

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            forall <int> in <start>:
                str.to.int(<int>) > 1000
            ''')

for _ in range(10):
    print(solver.solve())
```

We see that all `<int>` elements satisfy the constraint.

By default, all nonterminals that are re-used directly in constraints are universally quantified within the `<start>` symbol, so the above can actually be simplified to

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            str.to.int(<int>) > 1000
            ''')

for _ in range(10):
    print(solver.solve())
```

... and you realize that in all our initial constraints, we always had an implicit universal quantification.

## Picking Expansions

Sometimes, we'd like a quantifier to apply only for a specific expansion alternative of a nonterminal.
The form
```
forall TYPE VARIABLE=PATTERN in CONTEXT:
    (CONSTRAINT)
```
means that the CONSTRAINT only applies to a VARIABLE that actually matches the expansion given in PATTERN.
(Again, we can replace `forall` with `exists`, and make this an existential quantification rather than a universal quantification.)

Here's an example of using `forall`:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            forall <int>="<leaddigit><digits>" in <start>:
                (<leaddigit> = "7")
            ''')
```

This ensures that when `<int>` is expanded to a lead digit followed by more digits, the lead digit becomes `7`.
The effect is that all `<int>` values now start with a `7` digit:

```python
str(solver.solve())
```

Likewise, we can constrain `<int>` as a whole, and thus ensure that all numbers are greater than 100:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            forall <int> in <start>:
                (str.to.int(<int>) > 100)
            ''')

str(solver.solve())
```

By default, all variables are universally quantified in `<start>`, so the above can also be expressed as

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            str.to.int(<int>) > 100
            ''')

str(solver.solve())
```

## Matching Expansion Elements

In a quantification pattern, we can also _name_ individual nonterminal elements and use them in our constraints.
This is done by replacing the nonterminal `<ID>` with the special form `{<ID> VARIABLE}` (in curly braces) which then makes the variable `VARIABLE` a placeholder for the value matched by `ID`; `VARIABLE` can then be used in constraints.

Here is an example. In the expansion `<leaddigit><int>`, we want to ensure that the `<leaddigit>` is always `9`.
Using the special brace form, we make `lead` a variable holding the value of `<leaddigit>`, and can then use it in a constraint:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            forall <int> i="{<leaddigit> lead}<digits>" in <start>:
                (lead = "9")
            ''')
```

This (again) ensures that all lead digits should be `9`:

```python
for _ in range(10):
    print(solver.solve())
```

Could we express the above in a simpler fashion? Yes! For one, we can refer to `<leaddigit>` directly rather than introducing variables like `i` and `lead`:

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            forall <int>="<leaddigit><digits>" in <start>:
                (<leaddigit> = "9")
            ''')
print(solver.solve())
```

Furthermore, using implicit universal quantification and the dot notation introduced earlier, we could write, for instance

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            <int>.<leaddigit> = "9"
            ''')
print(solver.solve())
```

or just

```python
solver = ISLaSolver(CONFIG_GRAMMAR, 
            '''
            <leaddigit> = "9"
            ''')
print(solver.solve())
```

and obtain the same result (not necessarily the exact same values, though, due to randomness):

But while universal quantification and dot notation are sufficient for many cases, the pattern matching notation is more general and more flexible – even if it may be harder to read.

## Checking Strings

Using an `ISLaSolver`, we can also check if an string satisfies the constraints.
This can be applied to inputs, but also to _outputs_; ISLa constraints can thus server as _oracles_ – that is, _predicates_ that check a test result.

Let us check if in a given string, `<pagesize>` and `<bufsize>` are the same.

```python
constraint = '<pagesize> = <bufsize>'
solver = ISLaSolver(CONFIG_GRAMMAR, constraint)
```

To check the tree, we can pass it into the `evaluate()` method of the `solver` – and find that the given input does _not_ satisfy our constraint.

```python
solver.check('pagesize=12\nbufsize=34')
```

If we repeat the above, however, with an input that satisfies the constraint, we obtain a `True` result.

```python
solver.check('pagesize=27\nbufsize=27')
```

Checking constraints is much more efficient than solving them, as ISLa does not have to search for possible solutions.

## Case Studies

Let us further illustrate ISLa using a few case studies.

### Matching Identifiers in XML

The Extensible Markup Language (XML) is a typical example of an input language that cannot be fully expressed using a context-free grammar.
The problem is not so much expressing the _syntax_ of XML – the basics are fairly easy:

```python
XML_GRAMMAR: Grammar = {
    "<start>": ["<xml-tree>"],
    "<xml-tree>": ["<open-tag><xml-content><close-tag>"],
    "<open-tag>": ["<<id>>"],
    "<close-tag>": ["</<id>>"],
    "<xml-content>": ["Text", "<xml-tree>"],
    "<id>": ["<letter>", "<id><letter>"],
    "<letter>": crange('a', 'z')
}
```

```python
assert is_valid_grammar(XML_GRAMMAR)
```

```python
# ignore
syntax_diagram(XML_GRAMMAR)
```

The problem becomes evident when we produce inputs from the grammar: The `<id>` elements in `<open-tag>` and `<close-tag>` do not match.

```python
fuzzer = GrammarFuzzer(XML_GRAMMAR)
fuzzer.fuzz()
```

If we want the tag IDs to match, we need to come up with a _finite_ set of tags (as in, say, HTML); then we can extend the grammar with one rule for each tag - `<body>...</body>`, `<p>...</p>`, `<strong>...</strong>`, and so on.
For an _infinite_ set of tags, though, as in our grammar, expressing that the two tag IDs must match is not possible in a context-free grammar.

With ISLa, however, constraining the grammar is easy.
All we need is the rule that constrains the `<xml-tree>`:

```python
solver = ISLaSolver(XML_GRAMMAR, 
            '''
            <xml-tree>.<open-tag>.<id> = <xml-tree>.<close-tag>.<id>
            ''', max_number_smt_instantiations=1)

for _ in range(3):
    print(solver.solve())
```

and we see that the `<id>` tags now indeed match each other.

### Excursion: Solver Configuration Parameters

The configuration parameter `max_number_smt_instantiations` we passed to the `ISLaSolver` object above limits the number of calls to ISLa's underlying SMT solver. Generally, higher numbers lead to more inputs generated per time. Many of those will look structurally similar, though. If we aim for structurally diverse inputs and do not care about, e.g., the names of tags, it can make sense to choose a lower value for this parameter. This is what happens with `max_number_smt_instantiations=10`, which is the current default:

```python
solver = ISLaSolver(XML_GRAMMAR, 
            '''
            <xml-tree>.<open-tag>.<id> = <xml-tree>.<close-tag>.<id>
            ''', max_number_smt_instantiations=10)

for _ in range(3):
    print(solver.solve())
```

The parameter `max_number_free_instantiations` serves a similar purpose: ISla randomly instantiates nonterminal symbols whose values are not restricted by a constraint. It chooses&mdash;surprise!&mdash;at most `max_number_free_instantiations` such random instantiations.

Other configuration parameters of interest are `structural_predicates` and `semantic_predicates`, which let you extend the ISLa language by passing custom structural and semantic predicates to the solver. You can use all the predicates in these sets inside the ISLa constraint to solve. Per default, the semantic predicate `count(in_tree, NEEDLE, NUM)` and the following structural predicates are available:

- `after(node_1, node_2)`
- `before(node_1, node_2)`
- `consecutive(node_1, node_2)`
- `count(in_tree, NEEDLE, NUM)`
- `different_position(node_1, node_2)`
- `direct_child(node_1, node_2)`
- `inside(node_1, node_2)`
- `level(PRED, NONTERMINAL, node_1, node_2)`
- `nth(N, node_1, node_2)`
- `same_position(node_1, node_2)`

### End of Excursion

In contrast to the "input generator" solution in the [chapter on generators](GeneratorGrammarFuzzer), our constraint-based solution is purely declarative - and can also be used to parse and check inputs.
Plus, of course, we can easily add more constraints:

```python
solver = ISLaSolver(XML_GRAMMAR, 
            '''
            <xml-tree>.<open-tag>.<id> = <xml-tree>.<close-tag>.<id>
            and
            str.len(<id>) > 10
            ''', max_number_smt_instantiations=1)

for _ in range(3):
    print(solver.solve())
```

### Definitions and Usages in Programming Languages

When testing compilers with generated program code, one often encounters the problem that before _using_ an identifier, one has to _declare_ it first - specifying its type, some initial value, and more.

This problem is easily illustrated in the following grammar, which produces _sequences of assignments_.
Variable names consist of a single lowercase letter; values can only be digits; assignments are separated by semicolons.

```python
LANG_GRAMMAR: Grammar = {
    "<start>":
        ["<stmt>"],
    "<stmt>":
        ["<assgn>", "<assgn>; <stmt>"],
    "<assgn>":
        ["<lhs> := <rhs>"],
    "<lhs>":
        ["<var>"],
    "<rhs>":
        ["<var>", "<digit>"],
    "<var>": list(string.ascii_lowercase),
    "<digit>": list(string.digits)
}
```

```python
assert is_valid_grammar(LANG_GRAMMAR)
```

```python
syntax_diagram(LANG_GRAMMAR)
```

Here are some assignment sequences produced by the grammar:

```python
fuzzer = GrammarFuzzer(LANG_GRAMMAR)
```

```python
for _ in range(10):
    print(fuzzer.fuzz())
```

We see that the assignment _syntax_ is similar to what we have in common programming languages.
The _semantics_, however, are, well, questionable, as we commonly access variables whose values have not been previously defined.
Again, this is a _semantic_ property that cannot be expressed in a context-free grammar alone.

What we need here is a constraint specifying that on the right-hand side of an assignment, we can only have variable names that occur on the left-hand side.
In ISLa, we achieve this through the following constraint:

```python
solver = ISLaSolver(LANG_GRAMMAR, 
            '''
            forall <rhs> in <assgn>:
                exists <assgn> declaration:
                    <rhs>.<var> = declaration.<lhs>.<var>
            ''',
            max_number_smt_instantiations=1,
            max_number_free_instantiations=1)
```

```python
for _ in range(10):
    print(solver.solve())
```

This is much better already, but not perfect yet - we might still have assignments like `a := a` or `a := b; b := 5`.
That is because our constraints do not yet take care of _ordering_ – in a `<rhs>` element, we can only use variables that are defined earlier.

For this purpose, ISLa provides a `before()` predicate: `before(A, B)` expresses that the element `A` must occur before the element `B`.
With `before()`, we can rewrite our constraint as

```python
solver = ISLaSolver(LANG_GRAMMAR, 
            '''
            forall <rhs> in <assgn>:
                exists <assgn> declaration:
                    (before(declaration, <assgn>) and
                     <rhs>.<var> = declaration.<lhs>.<var>)
            ''',
            max_number_free_instantiations=1,
            max_number_smt_instantiations=1)
```

... and thus ensure that on the right-hand-side of assignments, we only use identifiers defined earlier.

```python
for _ in range(10):
    print(solver.solve())
```

In case you find that the assignment sequences are too short, you can use the ISLa `count()` predicate.
`count(VARIABLE, NONTERMINAL, N)` ensures that the number of NONTERMINALs in VARIABLE is exactly N.
To have statements with exactly 5 assignments, write

```python
solver = ISLaSolver(LANG_GRAMMAR, 
            '''
            forall <rhs> in <assgn>:
                exists <assgn> declaration:
                    (before(declaration, <assgn>) and
                     <rhs>.<var> = declaration.<lhs>.<var>)
            and
            count(start, "<assgn>", "5")
            ''', 
            max_number_smt_instantiations=1,
            max_number_free_instantiations=1)
```

```python
for _ in range(10):
    print(solver.solve())
```

## Synopsis

This chapter introduces the [ISLa](https://rindphi.github.io/isla/) framework, consisting of 
* the _ISLa specification language_, allowing to add _constraints_ to a grammar
* the _ISLa solver_, solving these constraints to produce semantically (and syntactically) valid inputs
* the _ISLa checker_, checking given inputs for whether they satisfy these constraints.

A typical usage of the ISLa solver is as follows.
First, install ISLa, using 
```shell
$ pip install isla-solver
```
Then, you can import the solver as

```python
from isla.solver import ISLaSolver  # type: ignore
```

The ISLa solver needs two things. First, a _grammar_ - say, US phone numbers.

```python
from Grammars import US_PHONE_GRAMMAR
```

Second, you need _constraints_ – a string expressing a condition over one or more grammar elements.
Common functions include
* `str.len()`, returning the length of a string
* `str.to.int()`, converting a string to an integer

Here, we instantiate the ISLa solver with a constraint stating that the area code should be above 900:

```python
solver = ISLaSolver(US_PHONE_GRAMMAR, 
            """
            str.to.int(<area>) > 900
            """)
```

With that, invoking `solver.solve()` returns a _solution_ for the constraints.

```python
str(solver.solve())
```

`solve()` returns a derivation tree, which typically is converted into a string using `str()` as above. The `print()` function does this implicitly.

Subsequent calls of `solve()` return more solutions:

```python
for _ in range(10):
    print(solver.solve())
```

We see that the solver produces a number of inputs that all satisfy the constraint - the area code is always more than 900.

The `ISLaSolver()` constructor provides several additional parameters to configure the solver, as documented below.
Additional `ISLaSolver` methods allow checking inputs against constraints, and provide additional functionality.

```python
# ignore
from ClassDiagram import display_class_hierarchy
```

```python
# ignore
display_class_hierarchy([ISLaSolver],
                         public_methods=[
                            ISLaSolver.__init__,
                            ISLaSolver.solve,
                            ISLaSolver.check,
                            ISLaSolver.parse,
                        ])
```

The ISLa functionality is also available on the command line:

```python
!isla --help
```

## Lessons Learned

* Using ISLa, we can add and solve _constraints_ to grammars, allowing to express _semantic properties_ of our test inputs
* Declaring constraints (and have a solver solve them) is much more versatile than adding generator code, and language-independent, too
* Using ISLa is fun :-)

## Next Steps

In the next chapters, we will continue to focus on semantics.
Among others, we will learn how to

* [mine grammars from existing inputs](GrammarMiner.ipynb)
* use [symbolic fuzzing](SymbolicFuzzer.ipynb) - that is, using constraint solvers to reach particular locations
* use [concolic fuzzing](ConcolicFuzzer.ipynb) - that is, combining symbolic fuzzing with concrete runs for higher efficiency

## Background

* ISLa is presented in the paper ["Input Invariants"](https://publications.cispa.saarland/3596/) at ESEC/FSE 2022.
* The [ISLa project](https://github.com/rindPHI/isla) contains the full source code and a complete reference.

## Exercises

### Exercise 1: String Encodings

A common way of representing strings is _length-prefixed strings_, a representation made popular by the _PASCAL_ programming language.
A length-prefixed string starts with a few bytes that encode the length $L$ of the string, followed by the $L$ actual characters.
For instance, assuming that two bytes are used to encode the length, the string `"Hello"` could be represented as the sequence

```
0x00 0x05 'H' 'e' 'l' 'l' 'o'
```

#### Part 1: Syntax

Write a grammar that defines the syntax of length-prefixed strings.

**Solution.** This is actually pretty easy:

```python
import string
```

```python
PASCAL_STRING_GRAMMAR: Grammar = {
    "<start>": ["<string>"],
    "<string>": ["<length><chars>"],
    "<length>": ["<byte>"],
    "<byte>": crange('\x00', '\xff'),
    "<chars>": ["", "<char><chars>"],
    "<char>": list(string.printable),
}
```

```python
assert is_valid_grammar(PASCAL_STRING_GRAMMAR)
```

```python
fuzzer = GrammarFuzzer(PASCAL_STRING_GRAMMAR)
```

```python
for _ in range(10):
    print(repr(fuzzer.fuzz()))
```

#### Part 2: Semantics

Use ISLa to produce valid length-prefixed strings.
Make use of the [SMT-LIB string library](https://smtlib.cs.uiowa.edu/theories-UnicodeStrings.shtml) to find appropriate conversion functions.

**Solution.** 
The function we need is `str.to_code(c)` to convert a single character to its ordinal value (e.g. `str.to_code('0x03') = 3`).
With this, we can formulate an appropriate constraint:

```python
solver = ISLaSolver(PASCAL_STRING_GRAMMAR, 
            '''
            str.to_code(<string>.<length>.<byte>) =
            str.len(<string>.<chars>)
            ''')
```

```python
for _ in range(10):
    # Get the solution
    solution = solver.solve()
    print(f'Solution: {repr(str(solution))}', end=' ')

    # Print statistics
    low_byte = solution.filter(lambda n: n.value == "<length>")[0][1]
    chars = solution.filter(lambda n: n.value == "<chars>")[0][1]
    print(f'(<length> = {ord(str(low_byte))}, len(<chars>) = {len(str(chars))})')
    print()
```

```python
# ignore
# We're done, so we can clean up:
import os

with ExpectError(FileNotFoundError, mute=True):
    os.remove('grammar.py')
```
