# Fuzzing with Grammars

In the chapter on ["Mutation-Based Fuzzing"](MutationFuzzer.ipynb), we have seen how to use extra hints – such as sample input files – to speed up test generation.  In this chapter, we take this idea one step further, by providing a _specification_ of the legal inputs to a program.  Specifying inputs via a _grammar_ allows for very systematic and efficient test generation, in particular for complex input formats.  Grammars also serve as the base for configuration fuzzing, API fuzzing, GUI fuzzing, and many more.

```python
from bookutils import YouTubeVideo
YouTubeVideo('Jc8Whz0W41o')
```

**Prerequisites**

* You should know how basic fuzzing works, e.g. from the [Chapter introducing fuzzing](Fuzzer.ipynb).
* Knowledge on [mutation-based fuzzing](MutationFuzzer.ipynb) and [coverage](Coverage.ipynb) is _not_ required yet, but still recommended.

```python
import bookutils.setup
```

```python
from typing import List, Dict, Union, Any, Tuple, Optional
```

```python
import Fuzzer
```

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.Grammars import <identifier>
```

and then make use of the following features.

This chapter introduces _grammars_ as a simple means to specify input languages, and to use them for testing programs with syntactically valid inputs.  A grammar is defined as a mapping of nonterminal symbols to lists of alternative expansions, as in the following example:

```python
>>> US_PHONE_GRAMMAR: Grammar = {
>>>     "<start>": ["<phone-number>"],
>>>     "<phone-number>": ["(<area>)<exchange>-<line>"],
>>>     "<area>": ["<lead-digit><digit><digit>"],
>>>     "<exchange>": ["<lead-digit><digit><digit>"],
>>>     "<line>": ["<digit><digit><digit><digit>"],
>>>     "<lead-digit>": ["2", "3", "4", "5", "6", "7", "8", "9"],
>>>     "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
>>> }
>>>
>>> assert is_valid_grammar(US_PHONE_GRAMMAR)
```
Nonterminal symbols are enclosed in angle brackets (say, `<digit>`).  To generate an input string from a grammar, a _producer_ starts with the start symbol (`<start>`) and randomly chooses a random expansion for this symbol.  It continues the process until all nonterminal symbols are expanded.  The function `simple_grammar_fuzzer()` does just that:

```python
>>> [simple_grammar_fuzzer(US_PHONE_GRAMMAR) for i in range(5)]
['(692)449-5179',
 '(519)230-7422',
 '(613)761-0853',
 '(979)881-3858',
 '(810)914-5475']
```
In practice, though, instead of `simple_grammar_fuzzer()`, you should use [the `GrammarFuzzer` class](GrammarFuzzer.ipynb) or one of its [coverage-based](GrammarCoverageFuzzer.ipynb), [probabilistic-based](ProbabilisticGrammarFuzzer.ipynb), or [generator-based](GeneratorGrammarFuzzer.ipynb) derivatives; these are more efficient, protect against infinite growth, and provide several additional features.

This chapter also introduces a [grammar toolbox](#A-Grammar-Toolbox) with several helper functions that ease the writing of grammars, such as using shortcut notations for character classes and repetitions, or extending grammars

## Input Languages

All possible behaviors of a program can be triggered by its input.  "Input" here can be a wide range of possible sources: We are talking about data that is read from files, from the environment, or over the network, data input by the user, or data acquired from interaction with other resources.  The set of all these inputs determines how the program will behave – including its failures.  When testing, it is thus very helpful to think about possible input sources, how to get them under control, and _how to systematically test them_.

For the sake of simplicity, we will assume for now that the program has only one source of inputs; this is the same assumption we have been using in the previous chapters, too.  The set of valid inputs to a program is called a _language_.  Languages range from the simple to the complex: the CSV language denotes the set of valid comma-separated inputs, whereas the Python language denotes the set of valid Python programs.  We commonly separate data languages and programming languages, although any program can also be treated as input data (say, to a compiler).  The [Wikipedia page on file formats](https://en.wikipedia.org/wiki/List_of_file_formats) lists more than 1,000 different file formats, each of which is its own language.

To formally describe languages, the field of *formal languages* has devised a number of *language specifications* that describe a language.  *Regular expressions* represent the simplest class of these languages to denote sets of strings: The regular expression `[a-z]*`, for instance, denotes a (possibly empty) sequence of lowercase letters.  *Automata theory* connects these languages to automata that accept these inputs; *finite state machines*, for instance, can be used to specify the language of regular expressions.

Regular expressions are great for not-too-complex input formats, and the associated finite state machines have many properties that make them great for reasoning.  To specify more complex inputs, though, they quickly encounter limitations.  At the other end of the language spectrum, we have *universal grammars* that denote the language accepted by *Turing machines*.  A Turing machine can compute anything that can be computed; and with Python being Turing-complete, this means that we can also use a Python program $p$ to specify or even enumerate legal inputs.  But then, computer science theory also tells us that each such testing program has to be written specifically for the program to be tested, which is not the level of automation we want.

## Grammars

The middle ground between regular expressions and Turing machines is covered by *grammars*.  Grammars are among the most popular (and best understood) formalisms to formally specify input languages.  Using a grammar, one can express a wide range of the properties of an input language.  Grammars are particularly great for expressing the *syntactical structure* of an input, and are the formalism of choice to express nested or recursive inputs.  The grammars we use are so-called *context-free grammars*, one of the easiest and most popular grammar formalisms.

### Rules and Expansions

A grammar consists of a *start symbol* and a set of *expansion rules* (or simply *rules*) which indicate how the start symbol (and other symbols) can be expanded.  As an example, consider the following grammar, denoting a sequence of two digits:

```
<start> ::= <digit><digit>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

To read such a grammar, start with the start symbol (`<start>`).  An expansion rule `<A> ::= <B>` means that the symbol on the left side (`<A>`) can be replaced by the string on the right side (`<B>`).  In the above grammar, `<start>` would be replaced by `<digit><digit>`.

In this string again, `<digit>` would be replaced by the string on the right side of the `<digit>` rule.  The special operator `|` denotes *expansion alternatives* (or simply *alternatives*), meaning that any of the digits can be chosen for an expansion.  Each `<digit>` thus would be expanded into one of the given digits, eventually yielding a string between `00` and `99`.  There are no further expansions for `0` to `9`, so we are all set.

The interesting thing about grammars is that they can be *recursive*. That is, expansions can make use of symbols expanded earlier – which would then be expanded again.  As an example, consider a grammar that describes integers:

```
<start>  ::= <integer>
<integer> ::= <digit> | <digit><integer>
<digit>   ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

Here, a `<integer>` is either a single digit, or a digit followed by another integer.  The number `1234` thus would be represented as a single digit `1`, followed by the integer `234`, which in turn is a digit `2`, followed by the integer `34`.

If we wanted to express that an integer can be preceded by a sign (`+` or `-`), we would write the grammar as

```
<start>   ::= <number>
<number>  ::= <integer> | +<integer> | -<integer>
<integer> ::= <digit> | <digit><integer>
<digit>   ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

These rules formally define the language: Anything that can be derived from the start symbol is part of the language; anything that cannot is not.

```python
from bookutils import quiz
```

```python
quiz("Which of these strings cannot be produced "
     "from the above `<start>` symbol?",
     [
         "`007`",
         "`-42`",
         "`++1`",
         "`3.14`"
     ], "[27 ** (1/3), 256 ** (1/4)]")
```

### Arithmetic Expressions

Let us expand our grammar to cover full *arithmetic expressions* – a poster child example for a grammar.  We see that an expression (`<expr>`) is either a sum, or a difference, or a term; a term is either a product or a division, or a factor; and a factor is either a number or a parenthesized expression.  Almost all rules can have recursion, and thus allow arbitrary complex expressions such as `(1 + 2) * (3.4 / 5.6 - 789)`.

```
<start>   ::= <expr>
<expr>    ::= <term> + <expr> | <term> - <expr> | <term>
<term>    ::= <term> * <factor> | <term> / <factor> | <factor>
<factor>  ::= +<factor> | -<factor> | (<expr>) | <integer> | <integer>.<integer>
<integer> ::= <digit><integer> | <digit>
<digit>   ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

In such a grammar, if we start with `<start>` and then expand one symbol after another, randomly choosing alternatives, we can quickly produce one valid arithmetic expression after another.  Such *grammar fuzzing* is highly effective as it comes to produce complex inputs, and this is what we will implement in this chapter.

```python
quiz("Which of these strings cannot be produced "
     "from the above `<start>` symbol?",
     [
         "`1 + 1`",
         "`1+1`",
         "`+1`",
         "`+(1)`",
     ], "4 ** 0.5")
```

## Representing Grammars in Python

Our first step in building a grammar fuzzer is to find an appropriate format for grammars.  To make the writing of grammars as simple as possible, we use a format that is based on strings and lists.  Our grammars in Python take the format of a _mapping_ between symbol names and expansions, where expansions are _lists_ of alternatives.  A one-rule grammar for digits thus takes the form

```python
DIGIT_GRAMMAR = {
    "<start>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}
```

### Excursion: A `Grammar` Type

Let us define a type for grammars, such that we can check grammar types statically.

A first attempt at a grammar type would be that each symbol (a string) is mapped to a list of expansions (strings):

```python
SimpleGrammar = Dict[str, List[str]]
```

However, our `opts()` feature for adding optional attributes, which we will introduce later in this chapter, also allows expansions to be _pairs_ that consist of strings and options, where options are mappings of strings to values:

```python
Option = Dict[str, Any]
```

Hence, an expansion is either a string – or a pair of a string and an option.

```python
Expansion = Union[str, Tuple[str, Option]]
```

With this, we can now define a `Grammar` as a mapping of strings to `Expansion` lists.

### End of Excursion

We can capture the grammar structure in a _`Grammar`_ type, in which each symbol (a string) is mapped to a list of expansions (strings):

```python
Grammar = Dict[str, List[Expansion]]
```

With this `Grammar` type, the full grammar for arithmetic expressions looks like this:

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

In the grammar, every symbol can be defined exactly once.  We can access any rule by its symbol...

```python
EXPR_GRAMMAR["<digit>"]
```

....and we can check whether a symbol is in the grammar:

```python
"<identifier>" in EXPR_GRAMMAR
```

Note that we assume that on the left-hand side of a rule (i.e., the key in the mapping) is always a single symbol.  This is the property that gives our grammars the characterization of _context-free_.

## Some Definitions

We assume that the canonical start symbol is `<start>`:

```python
START_SYMBOL = "<start>"
```

The handy `nonterminals()` function extracts the list of nonterminal symbols (i.e., anything between `<` and `>`, except spaces) from an expansion.

```python
import re
```

```python
RE_NONTERMINAL = re.compile(r'(<[^<> ]*>)')
```

```python
def nonterminals(expansion):
    # In later chapters, we allow expansions to be tuples,
    # with the expansion being the first element
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return RE_NONTERMINAL.findall(expansion)
```

```python
assert nonterminals("<term> * <factor>") == ["<term>", "<factor>"]
assert nonterminals("<digit><integer>") == ["<digit>", "<integer>"]
assert nonterminals("1 < 3 > 2") == []
assert nonterminals("1 <3> 2") == ["<3>"]
assert nonterminals("1 + 2") == []
assert nonterminals(("<1>", {'option': 'value'})) == ["<1>"]
```

Likewise, `is_nonterminal()` checks whether some symbol is a nonterminal:

```python
def is_nonterminal(s):
    return RE_NONTERMINAL.match(s)
```

```python
assert is_nonterminal("<abc>")
assert is_nonterminal("<symbol-1>")
assert not is_nonterminal("+")
```

## A Simple Grammar Fuzzer

Let us now put the above grammars to use.  We will build a very simple grammar fuzzer that starts with a start symbol (`<start>`) and then keeps on expanding it.  To avoid expansion to infinite inputs, we place a limit (`max_nonterminals`) on the number of nonterminals.  Furthermore, to avoid being stuck in a situation where we cannot reduce the number of symbols any further, we also limit the total number of expansion steps.

```python
import random
```

```python
class ExpansionError(Exception):
    pass
```

```python
def simple_grammar_fuzzer(grammar: Grammar,
                          start_symbol: str = START_SYMBOL,
                          max_nonterminals: int = 10,
                          max_expansion_trials: int = 100,
                          log: bool = False) -> str:
    """Produce a string from `grammar`.
       `start_symbol`: use a start symbol other than `<start>` (default).
       `max_nonterminals`: the maximum number of nonterminals
         still left for expansion
       `max_expansion_trials`: maximum # of attempts to produce a string
       `log`: print expansion progress if True"""

    term = start_symbol
    expansion_trials = 0

    while len(nonterminals(term)) > 0:
        symbol_to_expand = random.choice(nonterminals(term))
        expansions = grammar[symbol_to_expand]
        expansion = random.choice(expansions)
        # In later chapters, we allow expansions to be tuples,
        # with the expansion being the first element
        if isinstance(expansion, tuple):
            expansion = expansion[0]

        new_term = term.replace(symbol_to_expand, expansion, 1)

        if len(nonterminals(new_term)) < max_nonterminals:
            term = new_term
            if log:
                print("%-40s" % (symbol_to_expand + " -> " + expansion), term)
            expansion_trials = 0
        else:
            expansion_trials += 1
            if expansion_trials >= max_expansion_trials:
                raise ExpansionError("Cannot expand " + repr(term))

    return term
```

Let us see how this simple grammar fuzzer obtains an arithmetic expression from the start symbol:

```python
simple_grammar_fuzzer(grammar=EXPR_GRAMMAR, max_nonterminals=3, log=True)
```

By increasing the limit of nonterminals, we can quickly get much longer productions:

```python
for i in range(10):
    print(simple_grammar_fuzzer(grammar=EXPR_GRAMMAR, max_nonterminals=5))
```

Note that while our fuzzer does the job in most cases, it has a number of drawbacks.

```python
quiz("What drawbacks does `simple_grammar_fuzzer()` have?",
     [
         "It has a large number of string search and replace operations",
         "It may fail to produce a string (`ExpansionError`)",
         "It often picks some symbol to expand "
         "that does not even occur in the string",
         "All of the above"
     ], "1 << 2")
```

Indeed, `simple_grammar_fuzzer()` is rather inefficient due to the large number of search and replace operations, and it may even fail to produce a string. On the other hand, the implementation is straightforward and does the job in most cases. For this chapter, we'll stick to it; in the [next chapter](GrammarFuzzer.ipynb), we'll show how to build a more efficient one.

## Visualizing Grammars as Railroad Diagrams

With grammars, we can easily specify the format for several of the examples we discussed earlier.  The above arithmetic expressions, for instance, can be directly sent into `bc` (or any other program that takes arithmetic expressions).  Before we introduce a few additional grammars, let us give a means to _visualize_ them, giving an alternate view to aid their understanding.

_Railroad diagrams_, also called _syntax diagrams_, are a graphical representation of context-free grammars.  They are read left to right, following possible "rail" tracks; the sequence of symbols encountered on the track defines the language. To produce railroad diagrams, we implement a function `syntax_diagram()`.

### Excursion: Implementing `syntax_diagram()`

We use [RailroadDiagrams](RailroadDiagrams.ipynb), an external library for visualization.

```python
from RailroadDiagrams import NonTerminal, Terminal, Choice, HorizontalChoice, Sequence
from RailroadDiagrams import show_diagram
```

```python
from IPython.display import SVG
```

We first define the method `syntax_diagram_symbol()` to visualize a given symbol.  Terminal symbols are denoted as ovals, whereas nonterminal symbols (such as `<term>`) are denoted as rectangles.

```python
def syntax_diagram_symbol(symbol: str) -> Any:
    if is_nonterminal(symbol):
        return NonTerminal(symbol[1:-1])
    else:
        return Terminal(symbol)
```

```python
SVG(show_diagram(syntax_diagram_symbol('<term>')))
```

We define `syntax_diagram_expr()` to visualize expansion alternatives.

```python
def syntax_diagram_expr(expansion: Expansion) -> Any:
    # In later chapters, we allow expansions to be tuples,
    # with the expansion being the first element
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    symbols = [sym for sym in re.split(RE_NONTERMINAL, expansion) if sym != ""]
    if len(symbols) == 0:
        symbols = [""]  # special case: empty expansion

    return Sequence(*[syntax_diagram_symbol(sym) for sym in symbols])
```

```python
SVG(show_diagram(syntax_diagram_expr(EXPR_GRAMMAR['<term>'][0])))
```

This is the first alternative of `<term>` – a `<factor>` followed by `*` and a `<term>`.

Next, we define `syntax_diagram_alt()` for displaying alternate expressions.

```python
from itertools import zip_longest
```

```python
def syntax_diagram_alt(alt: List[Expansion]) -> Any:
    max_len = 5
    alt_len = len(alt)
    if alt_len > max_len:
        iter_len = alt_len // max_len
        alts = list(zip_longest(*[alt[i::iter_len] for i in range(iter_len)]))
        exprs = [[syntax_diagram_expr(expr) for expr in alt
                  if expr is not None] for alt in alts]
        choices = [Choice(len(expr) // 2, *expr) for expr in exprs]
        return HorizontalChoice(*choices)
    else:
        return Choice(alt_len // 2, *[syntax_diagram_expr(expr) for expr in alt])
```

```python
SVG(show_diagram(syntax_diagram_alt(EXPR_GRAMMAR['<digit>'])))
```

We see that a `<digit>` can be any single digit from `0` to `9`.

Finally, we define `syntax_diagram()` which given a grammar, displays the syntax diagram of its rules.

```python
def syntax_diagram(grammar: Grammar) -> None:
    from IPython.display import SVG, display

    for key in grammar:
        print("%s" % key[1:-1])
        display(SVG(show_diagram(syntax_diagram_alt(grammar[key]))))
```

### End of Excursion

Let us use `syntax_diagram()` to produce a railroad diagram of our expression grammar:

```python
syntax_diagram(EXPR_GRAMMAR)
```

This railroad representation will come in handy as it comes to visualizing the structure of grammars – especially for more complex grammars.

## Some Grammars

Let us create (and visualize) some more grammars and use them for fuzzing.

### A CGI Grammar

Here's a grammar for `cgi_decode()` introduced in the [chapter on coverage](Coverage.ipynb).

```python
CGI_GRAMMAR: Grammar = {
    "<start>":
        ["<string>"],

    "<string>":
        ["<letter>", "<letter><string>"],

    "<letter>":
        ["<plus>", "<percent>", "<other>"],

    "<plus>":
        ["+"],

    "<percent>":
        ["%<hexdigit><hexdigit>"],

    "<hexdigit>":
        ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "a", "b", "c", "d", "e", "f"],

    "<other>":  # Actually, could be _all_ letters
        ["0", "1", "2", "3", "4", "5", "a", "b", "c", "d", "e", "-", "_"],
}
```

```python
syntax_diagram(CGI_GRAMMAR)
```

In contrast to [basic fuzzing](Fuzzer.ipynb) or [mutation-based fuzzing](MutationFuzzer.ipynb), the grammar quickly produces all sorts of combinations:

```python
for i in range(10):
    print(simple_grammar_fuzzer(grammar=CGI_GRAMMAR, max_nonterminals=10))
```

### A URL Grammar

The same properties we have seen for CGI input also hold for more complex inputs.  Let us use a grammar to produce numerous valid URLs:

```python
URL_GRAMMAR: Grammar = {
    "<start>":
        ["<url>"],
    "<url>":
        ["<scheme>://<authority><path><query>"],
    "<scheme>":
        ["http", "https", "ftp", "ftps"],
    "<authority>":
        ["<host>", "<host>:<port>", "<userinfo>@<host>", "<userinfo>@<host>:<port>"],
    "<host>":  # Just a few
        ["cispa.saarland", "www.google.com", "fuzzingbook.com"],
    "<port>":
        ["80", "8080", "<nat>"],
    "<nat>":
        ["<digit>", "<digit><digit>"],
    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "<userinfo>":  # Just one
        ["user:password"],
    "<path>":  # Just a few
        ["", "/", "/<id>"],
    "<id>":  # Just a few
        ["abc", "def", "x<digit><digit>"],
    "<query>":
        ["", "?<params>"],
    "<params>":
        ["<param>", "<param>&<params>"],
    "<param>":  # Just a few
        ["<id>=<id>", "<id>=<nat>"],
}
```

```python
syntax_diagram(URL_GRAMMAR)
```

Again, within milliseconds, we can produce plenty of valid inputs.

```python
for i in range(10):
    print(simple_grammar_fuzzer(grammar=URL_GRAMMAR, max_nonterminals=10))
```

### A Natural Language Grammar

Finally, grammars are not limited to *formal languages* such as computer inputs, but can also be used to produce *natural language*.  This is the grammar we used to pick a title for this book:

```python
TITLE_GRAMMAR: Grammar = {
    "<start>": ["<title>"],
    "<title>": ["<topic>: <subtopic>"],
    "<topic>": ["Generating Software Tests", "<fuzzing-prefix>Fuzzing", "The Fuzzing Book"],
    "<fuzzing-prefix>": ["", "The Art of ", "The Joy of "],
    "<subtopic>": ["<subtopic-main>",
                   "<subtopic-prefix><subtopic-main>",
                   "<subtopic-main><subtopic-suffix>"],
    "<subtopic-main>": ["Breaking Software",
                        "Generating Software Tests",
                        "Principles, Techniques and Tools"],
    "<subtopic-prefix>": ["", "Tools and Techniques for "],
    "<subtopic-suffix>": [" for <reader-property> and <reader-property>",
                          " for <software-property> and <software-property>"],
    "<reader-property>": ["Fun", "Profit"],
    "<software-property>": ["Robustness", "Reliability", "Security"],
}
```

```python
syntax_diagram(TITLE_GRAMMAR)
```

```python
from typing import Set
```

```python
titles: Set[str] = set()
while len(titles) < 10:
    titles.add(simple_grammar_fuzzer(
        grammar=TITLE_GRAMMAR, max_nonterminals=10))
titles
```

(If you find that there is redundancy ("Robustness and Robustness") in here: In [our chapter on coverage-based fuzzing](GrammarCoverageFuzzer.ipynb), we will show how to cover each expansion only once.  And if you like some alternatives more than others, [probabilistic grammar fuzzing](ProbabilisticGrammarFuzzer.ipynb) will be there for you.)

## Grammars as Mutation Seeds

One very useful property of grammars is that they produce mostly valid inputs.  From a syntactical standpoint, the inputs are actually _always_ valid, as they satisfy the constraints of the given grammar.  (Of course, one needs a valid grammar in the first place.)  However, there are also _semantic_ properties that cannot be easily expressed in a grammar.  If, say, for a URL, the port range is supposed to be between 1024 and 2048, this is hard to write in a grammar.  If one has to satisfy more complex constraints, one quickly reaches the limits of what a grammar can express.

One way around this is to attach constraints to grammars, as we will discuss [later in this book](FuzzingWithConstraints.ipynb).  Another possibility is to put together the strengths of grammar-based fuzzing and [mutation-based fuzzing](MutationFuzzer.ipynb).  The idea is to use the grammar-generated inputs as *seeds* for further mutation-based fuzzing.  This way, we can explore not only _valid_ inputs, but also check out the _boundaries_ between valid and invalid inputs.  This is particularly interesting as  slightly invalid inputs allow finding parser errors (which are often abundant).  As with fuzzing in general, it is the unexpected which reveals errors in programs.

To use our generated inputs as seeds, we can feed them directly into the mutation fuzzers introduced earlier:

```python
from MutationFuzzer import MutationFuzzer  # minor dependency
```

```python
number_of_seeds = 10
seeds = [
    simple_grammar_fuzzer(
        grammar=URL_GRAMMAR,
        max_nonterminals=10) for i in range(number_of_seeds)]
seeds
```

```python
m = MutationFuzzer(seeds)
```

```python
[m.fuzz() for i in range(20)]
```

While the first 10 `fuzz()` calls return the seeded inputs (as designed), the later ones again create arbitrary mutations.  Using `MutationCoverageFuzzer` instead of `MutationFuzzer`, we could again have our search guided by coverage – and thus bring together the best of multiple worlds.

## A Grammar Toolbox

Let us now introduce a few techniques that help us writing grammars.

### Escapes

With `<` and `>` delimiting nonterminals in our grammars, how can we actually express that some input should contain `<` and `>`?  The answer is simple: Just introduce a symbol for them.

```python
simple_nonterminal_grammar: Grammar = {
    "<start>": ["<nonterminal>"],
    "<nonterminal>": ["<left-angle><identifier><right-angle>"],
    "<left-angle>": ["<"],
    "<right-angle>": [">"],
    "<identifier>": ["id"]  # for now
}
```

In `simple_nonterminal_grammar`, neither the expansion for `<left-angle>` nor the expansion for `<right-angle>` can be mistaken for a nonterminal. Hence, we can produce as many as we want.

(Note that this does not work with `simple_grammar_fuzzer()`, but rather with the `GrammarFuzzer` class we'll introduce in the next chapter.)

### Extending Grammars

In the course of this book, we frequently run into the issue of creating a grammar by _extending_ an existing grammar with new features.  Such an extension is very much like subclassing in object-oriented programming.

To create a new grammar $g'$ from an existing grammar $g$, we first copy $g$ into $g'$, and then go and extend existing rules with new alternatives and/or add new symbols.  Here's an example, extending the above `nonterminal` grammar with a better rule for identifiers:

```python
import copy
```

```python
nonterminal_grammar = copy.deepcopy(simple_nonterminal_grammar)
nonterminal_grammar["<identifier>"] = ["<idchar>", "<identifier><idchar>"]
nonterminal_grammar["<idchar>"] = ['a', 'b', 'c', 'd']  # for now
```

```python
nonterminal_grammar
```

Since such an extension of grammars is a common operation, we introduce a custom function `extend_grammar()` which first copies the given grammar and then updates it from a dictionary, using the Python dictionary `update()` method:

```python
def extend_grammar(grammar: Grammar, extension: Grammar = {}) -> Grammar:
    """Create a copy of `grammar`, updated with `extension`."""
    new_grammar = copy.deepcopy(grammar)
    new_grammar.update(extension)
    return new_grammar
```

This call to `extend_grammar()` extends `simple_nonterminal_grammar` to `nonterminal_grammar` just like the "manual" example above:

```python
nonterminal_grammar = extend_grammar(simple_nonterminal_grammar,
                                     {
                                         "<identifier>": ["<idchar>", "<identifier><idchar>"],
                                         # for now
                                         "<idchar>": ['a', 'b', 'c', 'd']
                                     }
                                     )
```

### Character Classes

In the above `nonterminal_grammar`, we have enumerated only the first few letters; indeed, enumerating all letters or digits in a grammar manually, as in `<idchar> ::= 'a' | 'b' | 'c' ...` is a bit painful.

However, remember that grammars are part of a program, and can thus also be constructed programmatically.  We introduce a function `srange()` which constructs a list of characters in a string:

```python
import string
```

```python
def srange(characters: str) -> List[Expansion]:
    """Construct a list with all characters in the string"""
    return [c for c in characters]
```

If we pass it the constant `string.ascii_letters`, which holds all ASCII letters, `srange()` returns a list of all ASCII letters:

```python
string.ascii_letters
```

```python
srange(string.ascii_letters)[:10]
```

We can use such constants in our grammar to quickly define identifiers:

```python
nonterminal_grammar = extend_grammar(nonterminal_grammar,
                                     {
                                         "<idchar>": (srange(string.ascii_letters) +
                                                      srange(string.digits) +
                                                      srange("-_"))
                                     }
                                     )
```

```python
[simple_grammar_fuzzer(nonterminal_grammar, "<identifier>") for i in range(10)]
```

The shortcut `crange(start, end)` returns a list of all characters in the ASCII range of `start` to (including) `end`:

```python
def crange(character_start: str, character_end: str) -> List[Expansion]:
    return [chr(i)
            for i in range(ord(character_start), ord(character_end) + 1)]
```

We can use this to express ranges of characters:

```python
crange('0', '9')
```

```python
assert crange('a', 'z') == srange(string.ascii_lowercase)
```

### Grammar Shortcuts

In the above `nonterminal_grammar`, as in other grammars, we have to express repetitions of characters using _recursion_, that is, by referring to the original definition:

```python
nonterminal_grammar["<identifier>"]
```

It could be a bit easier if we simply could state that a nonterminal should be a non-empty sequence of letters – for instance, as in

```
<identifier> = <idchar>+
```

where `+` denotes a non-empty repetition of the symbol it follows.

Operators such as `+` are frequently introduced as handy _shortcuts_ in grammars.  Formally, our grammars come in the so-called [Backus-Naur form](https://en.wikipedia.org/wiki/Backus-Naur_form), or *BNF* for short.  Operators _extend_ BNF to so-called _extended BNF*, or *EBNF* for short:

* The form `<symbol>?` indicates that `<symbol>` is optional – that is, it can occur 0 or 1 times.
* The form `<symbol>+` indicates that `<symbol>` can occur 1 or more times repeatedly.
* The form `<symbol>*` indicates that `<symbol>` can occur 0 or more times.  (In other words, it is an optional repetition.)

To make matters even more interesting, we would like to use _parentheses_ with the above shortcuts.  Thus, `(<foo><bar>)?` indicates that the sequence of `<foo>` and `<bar>` is optional.

Using such operators, we can define the identifier rule in a simpler way.  To this end, let us create a copy of the original grammar and modify the `<identifier>` rule:

```python
nonterminal_ebnf_grammar = extend_grammar(nonterminal_grammar,
                                          {
                                              "<identifier>": ["<idchar>+"]
                                          }
                                          )
```

Likewise, we can simplify the expression grammar.  Consider how signs are optional, and how integers can be expressed as sequences of digits.

```python
EXPR_EBNF_GRAMMAR: Grammar = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>"],

    "<factor>":
        ["<sign>?<factor>", "(<expr>)", "<integer>(.<integer>)?"],

    "<sign>":
        ["+", "-"],

    "<integer>":
        ["<digit>+"],

    "<digit>":
        srange(string.digits)
}
```

Let us implement a function `convert_ebnf_grammar()` that takes such an EBNF grammar and automatically translates it into a BNF grammar.

#### Excursion: Implementing `convert_ebnf_grammar()`

Our aim is to convert EBNF grammars such as the ones above into a regular BNF grammar.  This is done by four rules:

1. An expression `(content)op`, where `op` is one of `?`, `+`, `*`, becomes `<new-symbol>op`, with a new rule `<new-symbol> ::= content`.
2. An expression `<symbol>?` becomes `<new-symbol>`, where `<new-symbol> ::= <empty> | <symbol>`.
3. An expression `<symbol>+` becomes `<new-symbol>`, where `<new-symbol> ::= <symbol> | <symbol><new-symbol>`.
4. An expression `<symbol>*` becomes `<new-symbol>`, where `<new-symbol> ::= <empty> | <symbol><new-symbol>`.

Here, `<empty>` expands to the empty string, as in `<empty> ::= `.  (This is also called an *epsilon expansion*.)

If these operators remind you of _regular expressions_, this is not by accident: Actually, any basic regular expression can be converted into a grammar using the above rules (and character classes with `crange()`, as defined above).

Applying these rules on the examples above yields the following results:

* `<idchar>+` becomes `<idchar><new-symbol>` with `<new-symbol> ::= <idchar> | <idchar><new-symbol>`.
* `<integer>(.<integer>)?` becomes `<integer><new-symbol>` with `<new-symbol> ::= <empty> | .<integer>`.

Let us implement these rules in three steps.

##### Creating New Symbols

First, we need a mechanism to create new symbols.  This is fairly straightforward.

```python
def new_symbol(grammar: Grammar, symbol_name: str = "<symbol>") -> str:
    """Return a new symbol for `grammar` based on `symbol_name`"""
    if symbol_name not in grammar:
        return symbol_name

    count = 1
    while True:
        tentative_symbol_name = symbol_name[:-1] + "-" + repr(count) + ">"
        if tentative_symbol_name not in grammar:
            return tentative_symbol_name
        count += 1
```

```python
assert new_symbol(EXPR_EBNF_GRAMMAR, '<expr>') == '<expr-1>'
```

##### Expanding Parenthesized Expressions

Next, we need a means to extract parenthesized expressions from our expansions and expand them according to the rules above.  Let's start with extracting expressions:

```python
RE_PARENTHESIZED_EXPR = re.compile(r'\([^()]*\)[?+*]')
```

```python
def parenthesized_expressions(expansion: Expansion) -> List[str]:
    # In later chapters, we allow expansions to be tuples,
    # with the expansion being the first element
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_PARENTHESIZED_EXPR, expansion)
```

```python
assert parenthesized_expressions("(<foo>)* (<foo><bar>)+ (+<foo>)? <integer>(.<integer>)?") == [
    '(<foo>)*', '(<foo><bar>)+', '(+<foo>)?', '(.<integer>)?']
```

We can now use these to apply rule number 1, above, introducing new symbols for expressions in parentheses.

```python
def convert_ebnf_parentheses(ebnf_grammar: Grammar) -> Grammar:
    """Convert a grammar in extended BNF to BNF"""
    grammar = extend_grammar(ebnf_grammar)
    for nonterminal in ebnf_grammar:
        expansions = ebnf_grammar[nonterminal]

        for i in range(len(expansions)):
            expansion = expansions[i]
            if not isinstance(expansion, str):
                expansion = expansion[0]

            while True:
                parenthesized_exprs = parenthesized_expressions(expansion)
                if len(parenthesized_exprs) == 0:
                    break

                for expr in parenthesized_exprs:
                    operator = expr[-1:]
                    contents = expr[1:-2]

                    new_sym = new_symbol(grammar)

                    exp = grammar[nonterminal][i]
                    opts = None
                    if isinstance(exp, tuple):
                        (exp, opts) = exp
                    assert isinstance(exp, str)

                    expansion = exp.replace(expr, new_sym + operator, 1)
                    if opts:
                        grammar[nonterminal][i] = (expansion, opts)
                    else:
                        grammar[nonterminal][i] = expansion

                    grammar[new_sym] = [contents]

    return grammar
```

This does the conversion as sketched above:

```python
convert_ebnf_parentheses({"<number>": ["<integer>(.<integer>)?"]})
```

It even works for nested parenthesized expressions:

```python
convert_ebnf_parentheses({"<foo>": ["((<foo>)?)+"]})
```

##### Expanding Operators

After expanding parenthesized expressions, we now need to take care of symbols followed by operators (`?`, `*`, `+`).  As with `convert_ebnf_parentheses()`, above, we first extract all symbols followed by an operator.

```python
RE_EXTENDED_NONTERMINAL = re.compile(r'(<[^<> ]*>[?+*])')
```

```python
def extended_nonterminals(expansion: Expansion) -> List[str]:
    # In later chapters, we allow expansions to be tuples,
    # with the expansion being the first element
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return re.findall(RE_EXTENDED_NONTERMINAL, expansion)
```

```python
assert extended_nonterminals(
    "<foo>* <bar>+ <elem>? <none>") == ['<foo>*', '<bar>+', '<elem>?']
```

Our converter extracts the symbol and the operator, and adds new symbols according to the rules laid out above.

```python
def convert_ebnf_operators(ebnf_grammar: Grammar) -> Grammar:
    """Convert a grammar in extended BNF to BNF"""
    grammar = extend_grammar(ebnf_grammar)
    for nonterminal in ebnf_grammar:
        expansions = ebnf_grammar[nonterminal]

        for i in range(len(expansions)):
            expansion = expansions[i]
            extended_symbols = extended_nonterminals(expansion)

            for extended_symbol in extended_symbols:
                operator = extended_symbol[-1:]
                original_symbol = extended_symbol[:-1]
                assert original_symbol in ebnf_grammar, \
                    f"{original_symbol} is not defined in grammar"

                new_sym = new_symbol(grammar, original_symbol)

                exp = grammar[nonterminal][i]
                opts = None
                if isinstance(exp, tuple):
                    (exp, opts) = exp
                assert isinstance(exp, str)

                new_exp = exp.replace(extended_symbol, new_sym, 1)
                if opts:
                    grammar[nonterminal][i] = (new_exp, opts)
                else:
                    grammar[nonterminal][i] = new_exp

                if operator == '?':
                    grammar[new_sym] = ["", original_symbol]
                elif operator == '*':
                    grammar[new_sym] = ["", original_symbol + new_sym]
                elif operator == '+':
                    grammar[new_sym] = [
                        original_symbol, original_symbol + new_sym]

    return grammar
```

```python
convert_ebnf_operators({"<integer>": ["<digit>+"], "<digit>": ["0"]})
```

##### All Together

We can combine the two, first extending parentheses and then operators:

```python
def convert_ebnf_grammar(ebnf_grammar: Grammar) -> Grammar:
    return convert_ebnf_operators(convert_ebnf_parentheses(ebnf_grammar))
```

#### End of Excursion

Here's an example of using `convert_ebnf_grammar()`:

```python
convert_ebnf_grammar({"<authority>": ["(<userinfo>@)?<host>(:<port>)?"]})
```

```python
expr_grammar = convert_ebnf_grammar(EXPR_EBNF_GRAMMAR)
expr_grammar
```

Success! We have nicely converted the EBNF grammar into BNF.

With character classes and EBNF grammar conversion, we have two powerful tools that make the writing of grammars easier.  We will use these again and again as it comes to working with grammars.

### Grammar Extensions

During the course of this book, we frequently want to specify _additional information_ for grammars, such as [_probabilities_](ProbabilisticGrammarFuzzer.ipynb) or [_constraints_](GeneratorGrammarFuzzer.ipynb).  To support these extensions, as well as possibly others, we define an _annotation_ mechanism.

Our concept for annotating grammars is to add _annotations_ to individual expansions.  To this end, we allow that an expansion cannot only be a string, but also a _pair_ of a string and a set of attributes, as in

```python
    "<expr>":
        [("<term> + <expr>", opts(min_depth=10)),
         ("<term> - <expr>", opts(max_depth=2)),
         "<term>"]
```

Here, the `opts()` function would allow us to express annotations that apply to the individual expansions; in this case, the addition would be annotated with a `min_depth` value of 10, and the subtraction with a `max_depth` value of 2.  The meaning of these annotations is left to the individual algorithms dealing with the grammars; the general idea, though, is that they can be ignored.

#### Excursion: Implementing `opts()`

Our `opts()` helper function returns a mapping of its arguments to values:

```python
def opts(**kwargs: Any) -> Dict[str, Any]:
    return kwargs
```

```python
opts(min_depth=10)
```

To deal with both expansion strings and pairs of expansions and annotations, we access the expansion string and the associated annotations via designated helper functions, `exp_string()` and `exp_opts()`:

```python
def exp_string(expansion: Expansion) -> str:
    """Return the string to be expanded"""
    if isinstance(expansion, str):
        return expansion
    return expansion[0]
```

```python
exp_string(("<term> + <expr>", opts(min_depth=10)))
```

```python
def exp_opts(expansion: Expansion) -> Dict[str, Any]:
    """Return the options of an expansion.  If options are not defined, return {}"""
    if isinstance(expansion, str):
        return {}
    return expansion[1]
```

```python
def exp_opt(expansion: Expansion, attribute: str) -> Any:
    """Return the given attribution of an expansion.
    If attribute is not defined, return None"""
    return exp_opts(expansion).get(attribute, None)
```

```python
exp_opts(("<term> + <expr>", opts(min_depth=10)))
```

```python
exp_opt(("<term> - <expr>", opts(max_depth=2)), 'max_depth')
```

Finally, we define a helper function that sets a particular option:

```python
def set_opts(grammar: Grammar, symbol: str, expansion: Expansion,
             opts: Option = {}) -> None:
    """Set the options of the given expansion of grammar[symbol] to opts"""
    expansions = grammar[symbol]
    for i, exp in enumerate(expansions):
        if exp_string(exp) != exp_string(expansion):
            continue

        new_opts = exp_opts(exp)
        if opts == {} or new_opts == {}:
            new_opts = opts
        else:
            for key in opts:
                new_opts[key] = opts[key]

        if new_opts == {}:
            grammar[symbol][i] = exp_string(exp)
        else:
            grammar[symbol][i] = (exp_string(exp), new_opts)

        return

    raise KeyError(
        "no expansion " +
        repr(symbol) +
        " -> " +
        repr(
            exp_string(expansion)))
```

#### End of Excursion

## Checking Grammars

Since grammars are represented as strings, it is fairly easy to introduce errors.  So let us introduce a helper function that checks a grammar for consistency.

The helper function `is_valid_grammar()` iterates over a grammar to check whether all used symbols are defined, and vice versa, which is very useful for debugging; it also checks whether all symbols are reachable from the start symbol.  You don't have to delve into details here, but as always, it is important to get the input data straight before we make use of it.

### Excursion: Implementing `is_valid_grammar()`

```python
import sys
```

```python
def def_used_nonterminals(grammar: Grammar, start_symbol:
                          str = START_SYMBOL) -> Tuple[Optional[Set[str]],
                                                       Optional[Set[str]]]:
    """Return a pair (`defined_nonterminals`, `used_nonterminals`) in `grammar`.
    In case of error, return (`None`, `None`)."""

    defined_nonterminals = set()
    used_nonterminals = {start_symbol}

    for defined_nonterminal in grammar:
        defined_nonterminals.add(defined_nonterminal)
        expansions = grammar[defined_nonterminal]
        if not isinstance(expansions, list):
            print(repr(defined_nonterminal) + ": expansion is not a list",
                  file=sys.stderr)
            return None, None

        if len(expansions) == 0:
            print(repr(defined_nonterminal) + ": expansion list empty",
                  file=sys.stderr)
            return None, None

        for expansion in expansions:
            if isinstance(expansion, tuple):
                expansion = expansion[0]
            if not isinstance(expansion, str):
                print(repr(defined_nonterminal) + ": "
                      + repr(expansion) + ": not a string",
                      file=sys.stderr)
                return None, None

            for used_nonterminal in nonterminals(expansion):
                used_nonterminals.add(used_nonterminal)

    return defined_nonterminals, used_nonterminals
```

```python
def reachable_nonterminals(grammar: Grammar,
                           start_symbol: str = START_SYMBOL) -> Set[str]:
    reachable = set()

    def _find_reachable_nonterminals(grammar, symbol):
        nonlocal reachable
        reachable.add(symbol)
        for expansion in grammar.get(symbol, []):
            for nonterminal in nonterminals(expansion):
                if nonterminal not in reachable:
                    _find_reachable_nonterminals(grammar, nonterminal)

    _find_reachable_nonterminals(grammar, start_symbol)
    return reachable
```

```python
def unreachable_nonterminals(grammar: Grammar,
                             start_symbol=START_SYMBOL) -> Set[str]:
    return grammar.keys() - reachable_nonterminals(grammar, start_symbol)
```

```python
def opts_used(grammar: Grammar) -> Set[str]:
    used_opts = set()
    for symbol in grammar:
        for expansion in grammar[symbol]:
            used_opts |= set(exp_opts(expansion).keys())
    return used_opts
```

```python
def is_valid_grammar(grammar: Grammar,
                     start_symbol: str = START_SYMBOL,
                     supported_opts: Set[str] = set()) -> bool:
    """Check if the given `grammar` is valid.
       `start_symbol`: optional start symbol (default: `<start>`)
       `supported_opts`: options supported (default: none)"""

    defined_nonterminals, used_nonterminals = \
        def_used_nonterminals(grammar, start_symbol)
    if defined_nonterminals is None or used_nonterminals is None:
        return False

    # Do not complain about '<start>' being not used,
    # even if start_symbol is different
    if START_SYMBOL in grammar:
        used_nonterminals.add(START_SYMBOL)

    for unused_nonterminal in defined_nonterminals - used_nonterminals:
        print(repr(unused_nonterminal) + ": defined, but not used. Consider applying trim_grammar() on the grammar",
              file=sys.stderr)
    for undefined_nonterminal in used_nonterminals - defined_nonterminals:
        print(repr(undefined_nonterminal) + ": used, but not defined",
              file=sys.stderr)

    # Symbols must be reachable either from <start> or given start symbol
    unreachable = unreachable_nonterminals(grammar, start_symbol)
    msg_start_symbol = start_symbol

    if START_SYMBOL in grammar:
        unreachable = unreachable - \
            reachable_nonterminals(grammar, START_SYMBOL)
        if start_symbol != START_SYMBOL:
            msg_start_symbol += " or " + START_SYMBOL

    for unreachable_nonterminal in unreachable:
        print(repr(unreachable_nonterminal) + ": unreachable from " + msg_start_symbol + ". Consider applying trim_grammar() on the grammar",
              file=sys.stderr)

    used_but_not_supported_opts = set()
    if len(supported_opts) > 0:
        used_but_not_supported_opts = opts_used(
            grammar).difference(supported_opts)
        for opt in used_but_not_supported_opts:
            print(
                "warning: option " +
                repr(opt) +
                " is not supported",
                file=sys.stderr)

    return used_nonterminals == defined_nonterminals and len(unreachable) == 0
```

To make a grammar suitable for `is_valid_grammar()`, the following function may be useful.
The function `trim_grammar()` automatically _removes_ rules for nonterminals that are no longer needed.
This is useful if you have added new rules that _remove_ some extensions, rendering some nonterminals obsolete.

```python
def trim_grammar(grammar: Grammar, start_symbol=START_SYMBOL) -> Grammar:
    """Create a copy of `grammar` where all unused and unreachable nonterminals are removed."""
    new_grammar = extend_grammar(grammar)
    defined_nonterminals, used_nonterminals = \
        def_used_nonterminals(grammar, start_symbol)
    if defined_nonterminals is None or used_nonterminals is None:
        return new_grammar

    unused = defined_nonterminals - used_nonterminals
    unreachable = unreachable_nonterminals(grammar, start_symbol)
    for nonterminal in unused | unreachable:
        del new_grammar[nonterminal]

    return new_grammar
```

### End of Excursion

Let us make use of `is_valid_grammar()`. Our grammars defined above pass the test:

```python
assert is_valid_grammar(EXPR_GRAMMAR)
assert is_valid_grammar(CGI_GRAMMAR)
assert is_valid_grammar(URL_GRAMMAR)
```

The check can also be applied to EBNF grammars:

```python
assert is_valid_grammar(EXPR_EBNF_GRAMMAR)
```

These do not pass the test, though:

```python
assert not is_valid_grammar({"<start>": ["<x>"], "<y>": ["1"]})  # type: ignore
```

```python
assert not is_valid_grammar({"<start>": "123"})  # type: ignore
```

```python
assert not is_valid_grammar({"<start>": []})  # type: ignore
```

```python
assert not is_valid_grammar({"<start>": [1, 2, 3]})  # type: ignore
```

(The `#type: ignore` annotations avoid static checkers flagging the above as errors).

From here on, we will always use `is_valid_grammar()` when defining a grammar.

## Synopsis

This chapter introduces _grammars_ as a simple means to specify input languages, and to use them for testing programs with syntactically valid inputs.  A grammar is defined as a mapping of nonterminal symbols to lists of alternative expansions, as in the following example:

```python
US_PHONE_GRAMMAR: Grammar = {
    "<start>": ["<phone-number>"],
    "<phone-number>": ["(<area>)<exchange>-<line>"],
    "<area>": ["<lead-digit><digit><digit>"],
    "<exchange>": ["<lead-digit><digit><digit>"],
    "<line>": ["<digit><digit><digit><digit>"],
    "<lead-digit>": ["2", "3", "4", "5", "6", "7", "8", "9"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

assert is_valid_grammar(US_PHONE_GRAMMAR)
```

Nonterminal symbols are enclosed in angle brackets (say, `<digit>`).  To generate an input string from a grammar, a _producer_ starts with the start symbol (`<start>`) and randomly chooses a random expansion for this symbol.  It continues the process until all nonterminal symbols are expanded.  The function `simple_grammar_fuzzer()` does just that:

```python
[simple_grammar_fuzzer(US_PHONE_GRAMMAR) for i in range(5)]
```

In practice, though, instead of `simple_grammar_fuzzer()`, you should use [the `GrammarFuzzer` class](GrammarFuzzer.ipynb) or one of its [coverage-based](GrammarCoverageFuzzer.ipynb), [probabilistic-based](ProbabilisticGrammarFuzzer.ipynb), or [generator-based](GeneratorGrammarFuzzer.ipynb) derivatives; these are more efficient, protect against infinite growth, and provide several additional features.

This chapter also introduces a [grammar toolbox](#A-Grammar-Toolbox) with several helper functions that ease the writing of grammars, such as using shortcut notations for character classes and repetitions, or extending grammars

## Lessons Learned

* Grammars are powerful tools to express and produce syntactically valid inputs.
* Inputs produced from grammars can be used as is, or used as seeds for mutation-based fuzzing.
* Grammars can be extended with character classes and operators to make writing easier.

## Next Steps

As they make a great foundation for generating software tests, we use grammars again and again in this book.  As a sneak preview, we can use grammars to [fuzz configurations](ConfigurationFuzzer.ipynb):

```
<options> ::= <option>*
<option> ::= -h | --version | -v | -d | -i | --global-config <filename>
```

We can use grammars for [fuzzing functions and APIs](APIFuzzer.ipynb) and [fuzzing graphical user interfaces](WebFuzzer.ipynb):

```
<call-sequence> ::= <call>*
<call> ::= urlparse(<url>) | urlsplit(<url>)
```

We can assign [probabilities](ProbabilisticGrammarFuzzer.ipynb) and [constraints](GeneratorGrammarFuzzer.ipynb) to individual expansions:

```
<term>: 50% <factor> * <term> |  30% <factor> / <term> | 20% <factor>
<integer>: <digit>+ { <integer> >= 100 }
```

All these extras become especially valuable as we can

1. _infer grammars automatically_, dropping the need to specify them manually, and
2. _guide them towards specific goals_ such as coverage or critical functions;

which we also discuss for all techniques in this book.

To get there, however, we still have a bit of homework to do.  In particular, we first have to learn how to

* [create an efficient grammar fuzzer](GrammarFuzzer.ipynb)

## Background

As one of the foundations of human language, grammars have been around as long as human language existed.  The first _formalization_ of generative grammars was by Dakṣiputra Pāṇini in 350 BC \cite{Panini350bce}.  As a general means to express formal languages for both data and programs, their role in computer science cannot be overstated.  The seminal work by Chomsky \cite{Chomsky1956} introduced the central models of regular languages, context-free grammars, context-sensitive grammars, and universal grammars as they are used (and taught) in computer science as a means to specify input and programming languages ever since.

The use of grammars for _producing_ test inputs goes back to Burkhardt \cite{Burkhardt1967}, to be later rediscovered and applied by Hanford \cite{Hanford1970} and Purdom \cite{Purdom1972}.  The most important use of grammar testing since then has been *compiler testing*.  Actually, grammar-based testing is one important reason why compilers and Web browsers work as they should:

* The [CSmith](https://embed.cs.utah.edu/csmith/) tool \cite{Yang2011} specifically targets C programs, starting with a C grammar and then applying additional steps, such as referring to variables and functions defined earlier or ensuring integer and type safety.  Their authors have used it "to find and report more than 400 previously unknown compiler bugs."

* The [LangFuzz](http://issta2016.cispa.saarland/interview-with-christian-holler/) work \cite{Holler2012}, which shares two authors with this book, uses a generic grammar to produce outputs, and is used day and night to generate JavaScript programs and test their interpreters; as of today, it has found more than 2,600 bugs in browsers such as Mozilla Firefox, Google Chrome, and Microsoft Edge.

* The [EMI Project](http://web.cs.ucdavis.edu/~su/emi-project/) \cite{Le2014} uses grammars to stress-test C compilers, transforming known tests into alternative programs that should be semantically equivalent over all inputs.  Again, this has led to more than 100 bugs in C compilers being fixed.

* [Grammarinator](https://github.com/renatahodovan/grammarinator) \cite{Hodovan2018} is an open-source grammar fuzzer (written in Python!), using the popular ANTLR format as grammar specification.  Like LangFuzz, it uses the grammar for both parsing and producing, and has found more than 100 issues in the *JerryScript* lightweight JavaScript engine and an associated platform.

* [Domato](https://github.com/googleprojectzero/domato) is a generic grammar generation engine that is specifically used for fuzzing DOM input.  It has revealed a number of security issues in popular Web browsers.

Compilers and Web browsers, of course, are not only domains where grammars are needed for testing, but also domains where grammars are well-known.  Our claim in this book is that grammars can be used to generate almost _any_ input, and our aim is to empower you to do precisely that.

## Exercises

### Exercise 1: A JSON Grammar

Take a look at the [JSON specification](http://www.json.org) and derive a grammar from it:

* Use _character classes_ to express valid characters
* Use EBNF to express repetitions and optional parts
* Assume that
    - a string is a sequence of digits, ASCII letters, punctuation and space characters without quotes or escapes
    - whitespace is just a single space.
* Use `is_valid_grammar()` to ensure the grammar is valid.

Feed the grammar into `simple_grammar_fuzzer()`.  Do you encounter any errors, and why?

**Solution.** This is a fairly straightforward translation:

```python
CHARACTERS_WITHOUT_QUOTE = (string.digits
                            + string.ascii_letters
                            + string.punctuation.replace('"', '').replace('\\', '')
                            + ' ')
```

```python
JSON_EBNF_GRAMMAR: Grammar = {
    "<start>": ["<json>"],

    "<json>": ["<element>"],

    "<element>": ["<ws><value><ws>"],

    "<value>": ["<object>", "<array>", "<string>", "<number>",
                "true", "false", "null", "'; DROP TABLE STUDENTS"],

    "<object>": ["{<ws>}", "{<members>}"],

    "<members>": ["<member>(,<members>)*"],

    "<member>": ["<ws><string><ws>:<element>"],

    "<array>": ["[<ws>]", "[<elements>]"],

    "<elements>": ["<element>(,<elements>)*"],

    "<element>": ["<ws><value><ws>"],

    "<string>": ['"' + "<characters>" + '"'],

    "<characters>": ["<character>*"],

    "<character>": srange(CHARACTERS_WITHOUT_QUOTE),

    "<number>": ["<int><frac><exp>"],

    "<int>": ["<digit>", "<onenine><digits>", "-<digit>", "-<onenine><digits>"],

    "<digits>": ["<digit>+"],

    "<digit>": ['0', "<onenine>"],

    "<onenine>": crange('1', '9'),

    "<frac>": ["", ".<digits>"],

    "<exp>": ["", "E<sign><digits>", "e<sign><digits>"],

    "<sign>": ["", '+', '-'],

    # "<ws>": srange(string.whitespace)

    "<ws>": [" "]
}

assert is_valid_grammar(JSON_EBNF_GRAMMAR)
```

```python
JSON_GRAMMAR = convert_ebnf_grammar(JSON_EBNF_GRAMMAR)
```

```python
from ExpectError import ExpectError
```

```python
for i in range(50):
    with ExpectError():
        print(simple_grammar_fuzzer(JSON_GRAMMAR, '<object>'))
```

We get these errors because `simple_grammar_fuzzer()` first expands to a maximum number of elements, and then is limited because every further expansion would _increase_ the number of nonterminals, even though these may eventually reduce the string length.  This issue is addressed in the [next chapter](GrammarFuzzer.ipynb), introducing a more solid algorithm for producing strings from grammars.

### Exercise 2: Finding Bugs

The name `simple_grammar_fuzzer()` does not come by accident: The way it expands grammars is limited in several ways.  What happens if you apply `simple_grammar_fuzzer()` on `nonterminal_grammar` and `expr_grammar`, as defined above, and why?

**Solution**.  `nonterminal_grammar` does not work because `simple_grammar_fuzzer()` eventually tries to expand the just generated nonterminal:

```python
from ExpectError import ExpectError, ExpectTimeout
```

```python
with ExpectError():
    simple_grammar_fuzzer(nonterminal_grammar, log=True)
```

For `expr_grammar`, things are even worse, as `simple_grammar_fuzzer()` can start a series of infinite expansions:

```python
with ExpectTimeout(1):
    for i in range(10):
        print(simple_grammar_fuzzer(expr_grammar))
```

Both issues are addressed and discussed in the [next chapter](GrammarFuzzer.ipynb), introducing a more solid algorithm for producing strings from grammars.

### Exercise 3: Grammars with Regular Expressions

In a _grammar extended with regular expressions_, we can use the special form
```
/regex/
```
to include regular expressions in expansions.  For instance, we can have a rule
```
<integer> ::= /[+-]?[0-9]+/
```
to quickly express that an integer is an optional sign, followed by a sequence of digits.

#### Part 1: Convert regular expressions

Write a converter `convert_regex(r)` that takes a regular expression `r` and creates an equivalent grammar.  Support the following regular expression constructs:

* `*`, `+`, `?`, `()` should work just in EBNFs, above.
* `a|b` should translate into a list of alternatives `[a, b]`.
* `.` should match any character except newline.
* `[abc]` should translate into `srange("abc")`
* `[^abc]` should translate into the set of ASCII characters _except_ `srange("abc")`.
* `[a-b]` should translate into `crange(a, b)`
* `[^a-b]` should translate into the set of ASCII characters _except_ `crange(a, b)`.

Example: `convert_regex(r"[0-9]+")` should yield a grammar such as
```python
{
    "<start>": ["<s1>"],
    "<s1>": [ "<s2>", "<s1><s2>" ],
    "<s2>": crange('0', '9')
}
```

**Solution.** Left as exercise to the reader.

#### Part 2: Identify and expand regular expressions

Write a converter `convert_regex_grammar(g)` that takes a EBNF grammar `g` containing regular expressions in the form `/.../` and creates an equivalent BNF grammar.  Support the regular expression constructs as above.

Example: `convert_regex_grammar({ "<integer>" : "/[+-]?[0-9]+/" })` should yield a grammar such as
```python
{
    "<integer>": ["<s1><s3>"],
    "<s1>": [ "", "<s2>" ],
    "<s2>": srange("+-"),
    "<s3>": [ "<s4>", "<s4><s3>" ],
    "<s4>": crange('0', '9')
}
```

Optional: Support _escapes_ in regular expressions: `\c` translates to the literal character `c`; `\/` translates to `/` (and thus does not end the regular expression); `\\` translates to `\`.

**Solution.** Left as exercise to the reader.

### Exercise 4: Defining Grammars as Functions (Advanced)

To obtain a nicer syntax for specifying grammars, one can make use of Python constructs which then will be _parsed_ by an additional function.  For instance, we can imagine a grammar definition which uses `|` as a means to separate alternatives:

```python
def expression_grammar_fn():
    start = "<expr>"
    expr = "<term> + <expr>" | "<term> - <expr>"
    term = "<factor> * <term>" | "<factor> / <term>" | "<factor>"
    factor = "+<factor>" | "-<factor>" | "(<expr>)" | "<integer>.<integer>" | "<integer>"
    integer = "<digit><integer>" | "<digit>"
    digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
```

If we execute `expression_grammar_fn()`, this will yield an error.  Yet, the purpose of `expression_grammar_fn()` is not to be executed, but to be used as _data_ from which the grammar will be constructed.

```python
with ExpectError():
    expression_grammar_fn()
```

To this end, we make use of the `ast` (abstract syntax tree) and `inspect` (code inspection) modules.

```python
import ast
import inspect
```

First, we obtain the source code of `expression_grammar_fn()`...

```python
source = inspect.getsource(expression_grammar_fn)
source
```

... which we then parse into an abstract syntax tree:

```python
tree = ast.parse(source)
```

We can now parse the tree to find operators and alternatives.  `get_alternatives()` iterates over all nodes `op` of the tree; If the node looks like a binary _or_ (`|`) operation, we drill deeper and recurse. If not, we have reached a single production, and we try to get the expression from the production. We define the `to_expr` parameter depending on how we want to represent the production. In this case, we represent a single production by a single string.

```python
def get_alternatives(op, to_expr=lambda o: o.s):
    if isinstance(op, ast.BinOp) and isinstance(op.op, ast.BitOr):
        return get_alternatives(op.left, to_expr) + [to_expr(op.right)]
    return [to_expr(op)]
```

`funct_parser()` takes the abstract syntax tree of a function (say, `expression_grammar_fn()`) and iterates over all assignments:

```python
def funct_parser(tree, to_expr=lambda o: o.s):
    return {assign.targets[0].id: get_alternatives(assign.value, to_expr)
            for assign in tree.body[0].body}
```

The result is a grammar in our regular format:

```python
grammar = funct_parser(tree)
for symbol in grammar:
    print(symbol, "::=", grammar[symbol])
```

#### Part 1 (a): One Single Function

Write a single function `define_grammar(fn)` that takes a grammar defined as function (such as `expression_grammar_fn()`) and returns a regular grammar.

**Solution**.  This is straightforward:

```python
def define_grammar(fn, to_expr=lambda o: o.s):
    source = inspect.getsource(fn)
    tree = ast.parse(source)
    grammar = funct_parser(tree, to_expr)
    return grammar
```

```python
define_grammar(expression_grammar_fn)
```

**Note.** Python allows us to directly bind the generated grammar to the name `expression_grammar_fn` using function decorators. This can be used to ensure that we do not have a faulty function lying around:

```python
@define_grammar
def expression_grammar():
    start = "<expr>"
    expr = "<term> + <expr>" | "<term> - <expr>"
    #...
```

#### Part 1 (b): Alternative representations

We note that the grammar representation we designed previously does not allow simple generation of alternatives such as `srange()` and `crange()`. Further, one may find the string representation of expressions limiting.  It turns out that it is simple to extend our grammar definition to support grammars such as below:

```python
def define_name(o):
    return o.id if isinstance(o, ast.Name) else o.s
```

```python
def define_expr(op):
    if isinstance(op, ast.BinOp) and isinstance(op.op, ast.Add):
        return (*define_expr(op.left), define_name(op.right))
    return (define_name(op),)
```

```python
def define_ex_grammar(fn):
    return define_grammar(fn, define_expr)
```

The grammar:

```python
@define_ex_grammar
def expression_grammar():
    start   = expr
    expr    = (term + '+' + expr
            |  term + '-' + expr)
    term    = (factor + '*' + term
            |  factor + '/' + term
            |  factor)
    factor  = ('+' + factor
            |  '-' + factor
            |  '(' + expr + ')'
            |  integer + '.' + integer
            |  integer)
    integer = (digit + integer
            |  digit)
    digit   = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

for symbol in expression_grammar:
    print(symbol, "::=", expression_grammar[symbol])
```

**Note.** The grammar data structure thus obtained is a little more detailed than the standard data structure. It represents each production as a tuple.

We note that we have not enabled `srange()` or `crange()` in the above grammar. How would you go about adding these? (*Hint:* wrap `define_expr()` to look for `ast.Call`)

#### Part 2: Extended Grammars

Introduce an operator `*` that takes a pair `(min, max)` where `min` and `max` are the minimum and maximum number of repetitions, respectively.  A missing value `min` stands for zero; a missing value `max` for infinity.

```python
def identifier_grammar_fn():
    identifier = idchar * (1,)
```

With the `*` operator, we can generalize the EBNF operators – `?` becomes (0,1), `*` becomes (0,), and `+` becomes (1,).  Write a converter that takes an extended grammar defined using `*`, parse it, and convert it into BNF.

**Solution.** No solution yet :-)