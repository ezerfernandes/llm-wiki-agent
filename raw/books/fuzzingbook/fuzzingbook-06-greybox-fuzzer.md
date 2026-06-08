# Greybox Fuzzing

In the [previous chapter](MutationFuzzer.ipynb), we have introduced _mutation-based fuzzing_, a technique that generates fuzz inputs by applying small mutations to given inputs. In this chapter, we show how to _guide_ these mutations towards specific goals such as coverage. The algorithms in this chapter stem from the popular [American Fuzzy Lop](http://lcamtuf.coredump.cx/afl/) (AFL) fuzzer, in particular from its [AFLFast](https://github.com/mboehme/aflfast) and [AFLGo](https://github.com/aflgo/aflgo) flavors. We will explore the greybox fuzzing algorithm behind AFL and how we can exploit it to solve various problems for automated vulnerability detection.

```python
from bookutils import YouTubeVideo
YouTubeVideo('vBrNT9q2t1Y')
```

**Prerequisites**

* Reading the introduction on [mutation-based fuzzing](MutationFuzzer.ipynb) is recommended.

## Synopsis
<!-- Automatically generated. Do not edit. -->

To [use the code provided in this chapter](Importing.ipynb), write

```python
>>> from fuzzingbook.GreyboxFuzzer import <identifier>
```

and then make use of the following features.

This chapter introduces advanced methods for grey-box fuzzing inspired by the popular AFL fuzzer. The `GreyboxFuzzer` class has three arguments. First, a list of seed inputs:

```python
>>> seed_input = "http://www.google.com/search?q=fuzzing"
>>> seeds = [seed_input]
```
Second, a _mutator_ that changes individual parts of the input.

```python
>>> mutator = Mutator()
```
Third, a _power schedule_ that assigns fuzzing effort across the population:

```python
>>> schedule = PowerSchedule()
```
These three go into the `GreyboxFuzzer` constructor:

```python
>>> greybox_fuzzer = GreyboxFuzzer(seeds=seeds, mutator=mutator, schedule=schedule)
```
The `GreyboxFuzzer` class is used in conjunction with a `FunctionCoverageRunner`:

```python
>>> http_runner = FunctionCoverageRunner(http_program)
>>> outcomes = greybox_fuzzer.runs(http_runner, trials=10000)
```
After fuzzing, we can inspect the population:

```python
>>> greybox_fuzzer.population[:20]
[http://www.google.com/search?q=fuzzing,
 http;//www.google.com/serch?q=fuzzing,
 http://www.gongl{e.com/searchq=fuzing,
 http:/i?gww.gongl{e.mcom/serchq=fuzi~g,
 http://w#wwo.gongl{e.com/searchq=fuzing,
 http://w#wwo.ongl{e.com_/%searchbq=urn,
 http:/w#ww.ongl;e.com_/%sRarbhbq<urrn,
 httt:V0/-w#ww/`Hg-ngcmm/sirhSHq=8nzi>n,
 htt&p:/i,;gw.gongl{e)mcom/ercHq=fuzi~g,
 p:/[gmXn+gl.jc/s-/surc(2q=zog,
 htCpE/wwLV.nngD7Pl;
 e.Gwoi]/sRarrb,[t|rln,
 ht$p!//w>uw.go2/n{Cre.k/BeqrAci
 QS=fwzic,
 hty8/www.*ongPl{acomeach&q?fwuzing,
 http/w#wJwonlG{e.cm/sqearcchq=fuzg,
 htp:/\ww7.gong{e.com/searchq=feu~ing,
 htdp://w#wo.gogl{e.com/searchq
 fuzing,
 ttp8/w"ww4.kongl;,eco_%s]qrbh"zrn,
 L]td02/eWgo.wgg{gno~-c%arbhb5-i,
 htPtzp:/{i?gx.gonl:{e.mcotm/rKerhHM0q=fuvzi~g,
 `ttp://www.ngd{e(*/mserbh,qfuzing]
```
Besides the simple `PowerSchedule`, we can have advanced power schedules.

* `AFLFastSchedule` assigns high energy to "unusual" paths not taken very often.
* `AFLGoSchedule` assigns high energy to paths close to uncovered program locations.

The `AFLGoSchedule` class constructor requires a `distance` metric from each node towards target locations, as determined via analysis of the program code. See the chapter for details.

![](PICS/GreyboxFuzzer-synopsis-1.svg)

## AFL: An Effective Greybox Fuzzer

The algorithms in this chapter stem from the popular [American Fuzzy Lop](http://lcamtuf.coredump.cx/afl/) (AFL) fuzzer.

AFL is a *mutation-based fuzzer*. Meaning, AFL generates new inputs by slightly modifying a seed input (i.e., mutation), or by joining the first half of one input with the second half of another (i.e., splicing).

AFL is also a *greybox fuzzer* (not blackbox nor whitebox). Meaning, AFL leverages coverage-feedback to learn how to reach deeper into the program. It is not entirely blackbox because AFL leverages at least *some* program analysis. It is not entirely whitebox either because AFL does not build on heavyweight program analysis or constraint solving. Instead, AFL uses lightweight program instrumentation to glean some information about the (branch) coverage of a generated input.
If a generated input increases coverage, it is added to the seed corpus for further fuzzing.

To instrument a program, AFL injects a piece of code right after every conditional jump instruction. When executed, this so-called trampoline assigns the exercised branch a unique identifier and increments a counter that is associated with this branch. For efficiency, only a coarse branch hit count is maintained. In other words, for each input the fuzzer knows which branches and roughly how often they are exercised.
The instrumentation is usually done at compile-time, i.e., when the program source code is compiled to an executable binary. However, it is possible to run AFL on non-instrumented binaries using tools such as a virtual machine (e.g., [QEMU](https://github.com/mirrorer/afl/blob/master/qemu_mode)) or a dynamic instrumentation tool (e.g., [Intel PinTool](https://github.com/vanhauser-thc/afl-pin)). For Python programs, we can collect coverage information without any instrumentation (see chapter on [collecting coverage](Coverage.ipynb#Coverage-of-Basic-Fuzzing)).

## Ingredients for Greybox Fuzzing

We start with discussing the most important parts we need for mutational testing and goal guidance.

### Mutators

We introduce specific classes for mutating a seed.

```python
import bookutils.setup
```

```python
from typing import List, Set, Any, Tuple, Dict, Union
from collections.abc import Sequence
```

```python
import random
```

```python
from Coverage import population_coverage
```

First, we'll introduce the `Mutator` class. Given a seed input `inp`, the mutator returns a slightly modified version of `inp`.  In the [chapter on greybox grammar fuzzing](GreyboxGrammarFuzzer.ipynb), we extend this class to consider the input grammar for smart greybox fuzzing.

```python
class Mutator:
    """Mutate strings"""

    def __init__(self) -> None:
        """Constructor"""
        self.mutators = [
            self.delete_random_character,
            self.insert_random_character,
            self.flip_random_character
        ]
```

For insertion, we add a random character in a random position.

```python
class Mutator(Mutator):
    def insert_random_character(self, s: str) -> str:
        """Returns s with a random character inserted"""
        pos = random.randint(0, len(s))
        random_character = chr(random.randrange(32, 127))
        return s[:pos] + random_character + s[pos:]
```

For deletion, if the string is non-empty choose a random position and delete the character. Otherwise, use the insertion-operation.

```python
class Mutator(Mutator):
    def delete_random_character(self, s: str) -> str:
        """Returns s with a random character deleted"""
        if s == "":
            return self.insert_random_character(s)

        pos = random.randint(0, len(s) - 1)
        return s[:pos] + s[pos + 1:]
```

For substitution, if the string is non-empty choose a random position and flip a random bit in the character. Otherwise, use the insertion-operation.

```python
class Mutator(Mutator):
    def flip_random_character(self, s: str) -> str:
        """Returns s with a random bit flipped in a random position"""
        if s == "":
            return self.insert_random_character(s)

        pos = random.randint(0, len(s) - 1)
        c = s[pos]
        bit = 1 << random.randint(0, 6)
        new_c = chr(ord(c) ^ bit)
        return s[:pos] + new_c + s[pos + 1:]
```

The main method is `mutate` which chooses a random mutation operator from the list of operators.

```python
class Mutator(Mutator):
    def mutate(self, inp: Any) -> Any:  # can be str or Seed (see below)
        """Return s with a random mutation applied. Can be overloaded in subclasses."""
        mutator = random.choice(self.mutators)
        return mutator(inp)
```

Let's try the mutator. You can actually interact with such a "cell" and try other inputs by loading this chapter as Jupyter notebook. After opening, run all cells in the notebook using "Kernel -> Restart & Run All".

```python
Mutator().mutate("good")
```

### Seeds and Power Schedules

Now we introduce a new concept; the *power schedule*. A power schedule distributes the precious fuzzing time among the seeds in the population. Our objective is to maximize the time spent fuzzing those (most progressive) seeds which lead to higher coverage increase in shorter time.

We call the likelihood with which a seed is chosen from the population as the seed's *energy*. Throughout a fuzzing campaign, we would like to prioritize seeds that are more promising. Simply said, we do not want to waste energy fuzzing non-progressive seeds. We call the procedure that decides a seed's energy as the fuzzer's *power schedule*. For instance, AFL's schedule assigns more energy to seeds that are shorter, that execute faster, and yield coverage increases more often.

First, there is some information that we need to attach to each seed in addition to the seed's data. Hence, we define the following `Seed` class.

```python
from Coverage import Location
```

```python
class Seed:
    """Represent an input with additional attributes"""

    def __init__(self, data: str) -> None:
        """Initialize from seed data"""
        self.data = data

        # These will be needed for advanced power schedules
        self.coverage: Set[Location] = set()
        self.distance: Union[int, float] = -1
        self.energy = 0.0

    def __str__(self) -> str:
        """Returns data as string representation of the seed"""
        return self.data

    __repr__ = __str__
```

The power schedule that is implemented below assigns each seed the same energy. Once a seed is in the population, it will be fuzzed as often as any other seed in the population.

In Python, we can squeeze long for-loops into much smaller statements.
* `lambda x: ...` returns a function that takes `x` as input. Lambda allows for quick definitions unnamed functions.
* `map(f, l)` returns a list where the function `f` is applied to each element in list `l`.
* `random.choices(l, weights)[0]` returns element `l[i]` with probability in `weights[i]`.

```python
class PowerSchedule:
    """Define how fuzzing time should be distributed across the population."""

    def __init__(self) -> None:
        """Constructor"""
        self.path_frequency: Dict = {}

    def assignEnergy(self, population: Sequence[Seed]) -> None:
        """Assigns each seed the same energy"""
        for seed in population:
            seed.energy = 1

    def normalizedEnergy(self, population: Sequence[Seed]) -> List[float]:
        """Normalize energy"""
        energy = list(map(lambda seed: seed.energy, population))
        sum_energy = sum(energy)  # Add up all values in energy
        assert sum_energy != 0
        norm_energy = list(map(lambda nrg: nrg / sum_energy, energy))
        return norm_energy

    def choose(self, population: Sequence[Seed]) -> Seed:
        """Choose weighted by normalized energy."""
        self.assignEnergy(population)
        norm_energy = self.normalizedEnergy(population)
        seed: Seed = random.choices(population, weights=norm_energy)[0]
        return seed
```

Let's see whether this power schedule chooses seeds uniformly at random. We ask the schedule 10k times to choose a seed from the population of three seeds (A, B, C) and keep track of the number of times we have seen each seed. We should see each seed about 3.3k times.

```python
population = [Seed("A"), Seed("B"), Seed("C")]
schedule = PowerSchedule()
hits = {
    "A": 0,
    "B": 0,
    "C": 0
}
```

```python
for i in range(10000):
    seed = schedule.choose(population)
    hits[seed.data] += 1
```

```python
hits
```

Looks good. Every seed has been chosen about a third of the time.

### Runners and a Sample Program

We'll start with a small sample program of six lines. In order to collect coverage information during execution, we import the `FunctionCoverageRunner` class from the chapter on [mutation-based fuzzing](MutationFuzzer.ipynb#Guiding-by-Coverage).

The `FunctionCoverageRunner` constructor takes a Python `function` to execute. The function `run` takes an input, passes it on to the Python `function`, and collects the coverage information for this execution. The function `coverage()` returns a list of tuples `(function name, line number)` for each statement that has been covered in the Python `function`.

```python
from MutationFuzzer import FunctionCoverageRunner, http_program
```

The `crashme()` function raises an exception for the input "bad!". Let's see which statements are covered for the input "good".

```python
def crashme(s: str) -> None:
    if len(s) > 0 and s[0] == 'b':
        if len(s) > 1 and s[1] == 'a':
            if len(s) > 2 and s[2] == 'd':
                if len(s) > 3 and s[3] == '!':
                    raise Exception()
```

```python
crashme_runner = FunctionCoverageRunner(crashme)
crashme_runner.run("good")
list(crashme_runner.coverage())
```

In `crashme`, the input "good" only covers the if-statement in line 2. The branch condition `len(s) > 0 and s[0] == 'b'` evaluates to False.

## Advanced Blackbox Mutation-based Fuzzing

Let's integrate both the mutator and power schedule into a fuzzer. We'll start with a blackbox fuzzer -- which does *not* leverage any coverage information.

Our `AdvancedMutationFuzzer` class is an advanced and _parameterized_ version of the `MutationFuzzer` class from the [chapter on mutation-based fuzzing](MutationFuzzer.ipynb). It also inherits from the [Fuzzer](Fuzzer.ipynb#Fuzzer-Classes) class. For now, we only need to know the functions `fuzz()` which returns a generated input and `runs()` which executes `fuzz()` a specified number of times. For our `AdvancedMutationFuzzer` class, we override the function `fuzz()`.

```python
from Fuzzer import Fuzzer
```

The `AdvancedMutationFuzzer` is constructed with a set of initial seeds, a mutator, and a power schedule. Throughout the fuzzing campaign, it maintains a seed corpus called `population`. The function `fuzz` returns either an unfuzzed seed from the initial seeds, or the result of fuzzing a seed in the population. The function `create_candidate` handles the latter. It randomly chooses an input from the population and applies a number of mutations.

```python
class AdvancedMutationFuzzer(Fuzzer):
    """Base class for mutation-based fuzzing."""

    def __init__(self, seeds: List[str],
                 mutator: Mutator,
                 schedule: PowerSchedule) -> None:
        """Constructor.
        `seeds` - a list of (input) strings to mutate.
        `mutator` - the mutator to apply.
        `schedule` - the power schedule to apply.
        """
        self.seeds = seeds
        self.mutator = mutator
        self.schedule = schedule
        self.inputs: List[str] = []
        self.reset()

    def reset(self) -> None:
        """Reset the initial population and seed index"""
        self.population = list(map(lambda x: Seed(x), self.seeds))
        self.seed_index = 0

    def create_candidate(self) -> str:
        """Returns an input generated by fuzzing a seed in the population"""
        seed = self.schedule.choose(self.population)

        # Stacking: Apply multiple mutations to generate the candidate
        candidate = seed.data
        trials = min(len(candidate), 1 << random.randint(1, 5))
        for i in range(trials):
            candidate = self.mutator.mutate(candidate)
        return candidate

    def fuzz(self) -> str:
        """Returns first each seed once and then generates new inputs"""
        if self.seed_index < len(self.seeds):
            # Still seeding
            self.inp = self.seeds[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()

        self.inputs.append(self.inp)
        return self.inp
```

Okay, let's take the mutation fuzzer for a spin. Given a single seed, we ask it to generate three inputs.

```python
seed_input = "good"
mutation_fuzzer = AdvancedMutationFuzzer([seed_input], Mutator(), PowerSchedule())
print(mutation_fuzzer.fuzz())
print(mutation_fuzzer.fuzz())
print(mutation_fuzzer.fuzz())
```

Let's see how many statements the mutation-based blackbox fuzzer covers in a campaign with n=30k inputs.

The fuzzer function `runs(crashme_runner, trials=n)` generates `n` inputs and executes them on the `crashme` function via the `crashme_runner`. As stated earlier, the `crashme_runner` also collects coverage information.

```python
import time
```

```python
n = 30000
```

```python
blackbox_fuzzer = AdvancedMutationFuzzer([seed_input], Mutator(), PowerSchedule())

start = time.time()
blackbox_fuzzer.runs(FunctionCoverageRunner(crashme), trials=n)
end = time.time()

"It took the blackbox mutation-based fuzzer %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

In order to measure coverage, we import the [population_coverage](Coverage.ipynb#Coverage-of-Basic-Fuzzing) function. It takes a set of inputs and a Python function, executes the inputs on that function and collects coverage information. Specifically, it returns a tuple `(all_coverage, cumulative_coverage)` where `all_coverage` is the set of statements covered by all inputs, and `cumulative_coverage` is the number of statements covered as the number of executed inputs increases. We are just interested in the latter to plot coverage over time.

We extract the generated inputs from the blackbox fuzzer and measure coverage as the number of inputs increases.

```python
_, blackbox_coverage = population_coverage(blackbox_fuzzer.inputs, crashme)
bb_max_coverage = max(blackbox_coverage)

"The blackbox mutation-based fuzzer achieved a maximum coverage of %d statements." % bb_max_coverage
```

The following generated inputs increased the coverage for our `crashme` [example](#Runner-and-Sample-Program).

```python
[seed_input] + \
    [
        blackbox_fuzzer.inputs[idx] for idx in range(len(blackbox_coverage))
        if blackbox_coverage[idx] > blackbox_coverage[idx - 1]
    ]
```

***Summary***. This is how a blackbox mutation-based fuzzer works. We have integrated the *mutator* to generate inputs by fuzzing a provided set of initial seeds and the *power schedule* to decide which seed to choose next.

## Greybox Mutation-based Fuzzing

In contrast to a blackbox fuzzer, a greybox fuzzer like [AFL](http://lcamtuf.coredump.cx/afl/) _does_ leverage coverage information. Specifically, a greybox fuzzer adds to the seed population generated inputs which increase code coverage.

The method `run()` is inherited from the [Fuzzer](Fuzzer.ipynb#Fuzzer-Classes) class. It is called to generate and execute exactly one input. We override this function to add an input to the `population` that increases coverage. The greybox fuzzer attribute `coverages_seen` maintains the set of statements, that have previously been covered.

```python
class GreyboxFuzzer(AdvancedMutationFuzzer):
    """Coverage-guided mutational fuzzing."""

    def reset(self):
        """Reset the initial population, seed index, coverage information"""
        super().reset()
        self.coverages_seen = set()
        self.population = []  # population is filled during greybox fuzzing

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome = super().run(runner)
        new_coverage = frozenset(runner.coverage())
        if new_coverage not in self.coverages_seen:
            # We have new coverage
            seed = Seed(self.inp)
            seed.coverage = runner.coverage()
            self.coverages_seen.add(new_coverage)
            self.population.append(seed)

        return (result, outcome)
```

Let's take our greybox fuzzer for a spin.

```python
seed_input = "good"
greybox_fuzzer = GreyboxFuzzer([seed_input], Mutator(), PowerSchedule())

start = time.time()
greybox_fuzzer.runs(FunctionCoverageRunner(crashme), trials=n)
end = time.time()

"It took the greybox mutation-based fuzzer %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

Does the greybox fuzzer cover more statements after generating the same number of test inputs?

```python
_, greybox_coverage = population_coverage(greybox_fuzzer.inputs, crashme)
gb_max_coverage = max(greybox_coverage)

"Our greybox mutation-based fuzzer covers %d more statements" % (gb_max_coverage - bb_max_coverage)
```

Our seed population for our [example](#Runner-and-Sample-Program) now contains the following seeds.

```python
greybox_fuzzer.population
```

Coverage-feedback is indeed helpful. The new seeds are like bread crumbs or milestones that guide the fuzzer to progress more quickly into deeper code regions. Following is a simple plot showing the coverage achieved over time for both fuzzers on our simple [example](#Runner-and-Sample-Program).

```python
%matplotlib inline
```

```python
import matplotlib.pyplot as plt  # type: ignore
```

```python
line_bb, = plt.plot(blackbox_coverage, label="Blackbox")
line_gb, = plt.plot(greybox_coverage, label="Greybox")
plt.legend(handles=[line_bb, line_gb])
plt.title('Coverage over time')
plt.xlabel('# of inputs')
plt.ylabel('lines covered');
```

***Summary***. We have seen how a greybox fuzzer "discovers" interesting seeds that can lead to more progress. From the input `good`, our greybox fuzzer has slowly learned how to generate the input `bad!` which raises the exception. Now, how can we do that even faster?

***Try it***. How much coverage would be achieved over time using a blackbox *generation-based* fuzzer? Try plotting the coverage for all three fuzzers. You can define the blackbox generation-based fuzzer as follows.
```Python
from Fuzzer import RandomFuzzer
blackbox_gen_fuzzer = RandomFuzzer(min_length=4, max_length=4, char_start=32, char_range=96)
```
You can execute your own code by opening this chapter as Jupyter notebook.

***Read***. This is the high-level view how AFL works, one of the most successful vulnerability detection tools. If you are interested in the technical details, have a look at: https://github.com/mirrorer/afl/blob/master/docs/technical_details.txt

## Boosted Greybox Fuzzing

Our boosted greybox fuzzer assigns more energy to seeds that promise to achieve more coverage. We change the power schedule such that seeds that exercise "unusual" paths have more energy. With *unusual paths*, we mean paths that are not exercised very often by generated inputs.

In order to identify which path is exercised by an input, we leverage the function `getPathID` from the section on [trace coverage](WhenIsEnough.ipynb#Trace-Coverage).

```python
import pickle   # serializes an object by producing a byte array from all the information in the object
import hashlib  # produces a 128-bit hash value from a byte array
```

The function `getPathID` returns a unique hash for a coverage set.

```python
def getPathID(coverage: Any) -> str:
    """Returns a unique hash for the covered statements"""
    pickled = pickle.dumps(sorted(coverage))
    return hashlib.md5(pickled).hexdigest()
```

There are several ways to assign energy based on how unusual the exercised path is. In this case, we implement an _exponential power schedule_ which computes the energy $e(s)$ for a seed $s$ as follows
$$e(s) = \frac{1}{f(p(s))^a}$$
where
* $p(s)$ returns the ID of the path exercised by $s$,
* $f(p)$ returns the number of times the path $p$ is exercised by generated inputs, and
* $a$ is a given exponent.

```python
class AFLFastSchedule(PowerSchedule):
    """Exponential power schedule as implemented in AFL"""

    def __init__(self, exponent: float) -> None:
        self.exponent = exponent

    def assignEnergy(self, population: Sequence[Seed]) -> None:
        """Assign exponential energy inversely proportional to path frequency"""
        for seed in population:
            seed.energy = 1 / (self.path_frequency[getPathID(seed.coverage)] ** self.exponent)
```

In the greybox fuzzer, let's keep track of the number of times $f(p)$ each path $p$ is exercised, and update the power schedule.

```python
class CountingGreyboxFuzzer(GreyboxFuzzer):
    """Count how often individual paths are exercised."""

    def reset(self):
        """Reset path frequency"""
        super().reset()
        self.schedule.path_frequency = {}

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Inform scheduler about path frequency"""
        result, outcome = super().run(runner)

        path_id = getPathID(runner.coverage())
        if path_id not in self.schedule.path_frequency:
            self.schedule.path_frequency[path_id] = 1
        else:
            self.schedule.path_frequency[path_id] += 1

        return(result, outcome)
```

Okay, let's run our boosted greybox fuzzer $n=10k$ times on our simple [example](#Runner-and-Sample-Program). We set the exponentent of our exponential power schedule to $a=5$.

```python
n = 10000
seed_input = "good"
fast_schedule = AFLFastSchedule(5)
fast_fuzzer = CountingGreyboxFuzzer([seed_input], Mutator(), fast_schedule)
start = time.time()
fast_fuzzer.runs(FunctionCoverageRunner(crashme), trials=n)
end = time.time()

"It took the fuzzer w/ exponential schedule %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

```python
import numpy as np
```

```python
x_axis = np.arange(len(fast_schedule.path_frequency))
y_axis = list(fast_schedule.path_frequency.values())

plt.bar(x_axis, y_axis)
plt.xticks(x_axis)
plt.ylim(0, n)
# plt.yscale("log")
# plt.yticks([10,100,1000,10000])
plt;
```

```python
print("             path id 'p'           : path frequency 'f(p)'")
fast_schedule.path_frequency
```

How does it compare to our greybox fuzzer with the classical power schedule?

```python
seed_input = "good"
orig_schedule = PowerSchedule()
orig_fuzzer = CountingGreyboxFuzzer([seed_input], Mutator(), orig_schedule)
start = time.time()
orig_fuzzer.runs(FunctionCoverageRunner(crashme), trials=n)
end = time.time()

"It took the fuzzer w/ original schedule %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

```python
x_axis = np.arange(len(orig_schedule.path_frequency))
y_axis = list(orig_schedule.path_frequency.values())

plt.bar(x_axis, y_axis)
plt.xticks(x_axis)
plt.ylim(0, n)
# plt.yscale("log")
# plt.yticks([10,100,1000,10000])
plt;
```

```python
print("             path id 'p'           : path frequency 'f(p)'")
orig_schedule.path_frequency
```

The exponential power schedule shaves some of the executions of the "high-frequency path" off and adds them to the lower-frequency paths. The path executed least often is either not at all exercised using the traditional power schedule or it is exercised much less often.

Let's have a look at the energy that is assigned to the discovered seeds.

```python
orig_energy = orig_schedule.normalizedEnergy(orig_fuzzer.population)

for (seed, norm_energy) in zip(orig_fuzzer.population, orig_energy):
    print("'%s', %0.5f, %s" % (getPathID(seed.coverage),  # type: ignore
                               norm_energy, repr(seed.data)))
```

```python
fast_energy = fast_schedule.normalizedEnergy(fast_fuzzer.population)

for (seed, norm_energy) in zip(fast_fuzzer.population, fast_energy):
    print("'%s', %0.5f, %s" % (getPathID(seed.coverage),  # type: ignore
                               norm_energy, repr(seed.data)))
```

Exactly. Our new exponential power schedule assigns most energy to the seed exercising the lowest-frequency path.

Let's compare them in terms of coverage achieved over time for our simple [example](#Runner-and-Sample-Program).

```python
_, orig_coverage = population_coverage(orig_fuzzer.inputs, crashme)
_, fast_coverage = population_coverage(fast_fuzzer.inputs, crashme)
line_orig, = plt.plot(orig_coverage, label="Original Greybox Fuzzer")
line_fast, = plt.plot(fast_coverage, label="Boosted Greybox Fuzzer")
plt.legend(handles=[line_orig, line_fast])
plt.title('Coverage over time')
plt.xlabel('# of inputs')
plt.ylabel('lines covered');
```

As expected, the boosted greybox fuzzer (with the exponential power schedule) achieves coverage much faster.

***Summary***. By fuzzing seeds more often that exercise low-frequency paths, we can explore program paths in a much more efficient manner.

***Try it***. You can try other exponents for the fast power schedule, or change the power schedule entirely. Note that a large exponent can lead to overflows and imprecisions in the floating point arithmetic producing unexpected results. You can execute your own code by opening this chapter as Jupyter notebook.

***Read***. You can find out more about fuzzer boosting in the paper "[Coverage-based Greybox Fuzzing as Markov Chain](https://mboehme.github.io/paper/CCS16.pdf)" \cite{boehme2018greybox} and check out the implementation into AFL at [http://github.com/mboehme/aflfast].

## A Complex Example: HTMLParser

Let's compare the three fuzzers on a more realistic example, the Python [HTML parser](https://docs.python.org/3/library/html.parser.html). We run all three fuzzers $n=5k$ times on the HTMLParser, starting with the "empty" seed.

```python
from html.parser import HTMLParser
```

```python
# create wrapper function
def my_parser(inp: str) -> None:
    parser = HTMLParser()  # resets the HTMLParser object for every fuzz input
    parser.feed(inp)
```

```python
n = 5000
seed_input = " "  # empty seed
blackbox_fuzzer = AdvancedMutationFuzzer([seed_input], Mutator(), PowerSchedule())
greybox_fuzzer = GreyboxFuzzer([seed_input], Mutator(), PowerSchedule())
boosted_fuzzer = CountingGreyboxFuzzer([seed_input], Mutator(), AFLFastSchedule(5))
```

```python
start = time.time()
blackbox_fuzzer.runs(FunctionCoverageRunner(my_parser), trials=n)
greybox_fuzzer.runs(FunctionCoverageRunner(my_parser), trials=n)
boosted_fuzzer.runs(FunctionCoverageRunner(my_parser), trials=n)
end = time.time()

"It took all three fuzzers %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

How do the fuzzers compare in terms of coverage over time?

```python
_, black_coverage = population_coverage(blackbox_fuzzer.inputs, my_parser)
_, grey_coverage = population_coverage(greybox_fuzzer.inputs, my_parser)
_, boost_coverage = population_coverage(boosted_fuzzer.inputs, my_parser)
line_black, = plt.plot(black_coverage, label="Blackbox Fuzzer")
line_grey, = plt.plot(grey_coverage, label="Greybox Fuzzer")
line_boost, = plt.plot(boost_coverage, label="Boosted Greybox Fuzzer")
plt.legend(handles=[line_boost, line_grey, line_black])
plt.title('Coverage over time')
plt.xlabel('# of inputs')
plt.ylabel('lines covered');
```

Both greybox fuzzers clearly outperform the blackbox fuzzer. The reason is that the greybox fuzzer "discovers" interesting inputs along the way. Let's have a look at the last 10 inputs generated by the greybox versus blackbox fuzzer.

```python
blackbox_fuzzer.inputs[-10:]
```

```python
greybox_fuzzer.inputs[-10:]
```

The greybox fuzzer executes much more complicated inputs, many of which include special characters such as opening and closing brackets and chevrons (i.e., `<, >, [, ]`). Yet, many important keywords, such as `<html>` are still missing.

To inform the fuzzer about these important keywords, we will need [grammars](Grammars.ipynb); in the section on [smart greybox fuzzing](LangFuzzer.ipynb), we combine them with the techniques above.

***Try it***. You can re-run these experiments to understand the variance of fuzzing experiments. Sometimes, the fuzzer that we claim to be superior does not seem to outperform the inferior fuzzer. In order to do this, you just need to open this chapter as Jupyter notebook.

## Directed Greybox Fuzzing

Sometimes, you just want the fuzzer to reach some dangerous location in the source code. This could be a location where you expect a buffer overflow. Or you want to test a recent change in your code base. How do we direct the fuzzer towards these locations?

In this chapter, we introduce directed greybox fuzzing as an optimization problem.

### Solving the Maze

To provide a meaningful example where you can easily change the code complexity and target location, we generate the maze source code from the maze provided as string. This example is loosely based on an old [blog post](https://feliam.wordpress.com/2010/10/07/the-symbolic-maze/) on symbolic execution by Felipe Andres Manzano (Quick shout-out!).

You simply specify the maze as a string. Like so.

```python
maze_string = """
+-+-----+
|X|     |
| | --+ |
| |   | |
| +-- | |
|     |#|
+-----+-+
"""
```

The code is generated using the function `generate_maze_code()`. We'll hide the implementation and instead explain what it does. If you are interested in the coding, go [here](ControlFlow.ipynb#Example:-Maze).

```python
from ControlFlow import generate_maze_code
```

```python
# ignore
def maze(s: str) -> str:
    return ""  # Will be overwritten by exec()
```

```python
# ignore
def target_tile() -> str:
    return ' '  # Will be overwritten by exec()
```

```python
maze_code = generate_maze_code(maze_string)
```

```python
exec(maze_code)
```

The objective is to get the "X" to the "#" by providing inputs `D` for down, `U` for up, `L` for left, and `R` for right.

```python
print(maze("DDDDRRRRUULLUURRRRDDDD"))  # Appending one more 'D', you have reached the target.
```

Each character in `maze_string` represents a tile. For each tile, a tile-function is generated.
* If the current tile is "benign" (` `), the tile-function corresponding to the next input character (D, U, L, R) is called. Unexpected input characters are ignored. If no more input characters are left, it returns "VALID" and the current maze state.
* If the current tile is a "trap" (`+`,`|`,`-`), it returns "INVALID" and the current maze state.
* If the current tile is the "target" (`#`), it returns "SOLVED" and the current maze state.

***Try it***. You can test other sequences of input characters, or even change the maze entirely. In order to execute your own code, you just need to open this chapter as Jupyter notebook.

To get an idea of the generated code, lets look at the static [call graph](https://en.wikipedia.org/wiki/Call_graph). A call graph shows the order in which functions can be executed.

```python
from ControlFlow import callgraph
```

```python
callgraph(maze_code)
```

### A First Attempt

We introduce a `DictMutator` class which mutates strings by inserting a keyword from a given dictionary:

```python
class DictMutator(Mutator):
    """Variant of `Mutator` inserting keywords from a dictionary"""

    def __init__(self, dictionary: Sequence[str]) -> None:
        """Constructor.
        `dictionary` - a list of strings that can be used as keywords
        """
        super().__init__()
        self.dictionary = dictionary
        self.mutators.append(self.insert_from_dictionary)

    def insert_from_dictionary(self, s: str) -> str:
        """Returns `s` with a keyword from the dictionary inserted"""
        pos = random.randint(0, len(s))
        random_keyword = random.choice(self.dictionary)
        return s[:pos] + random_keyword + s[pos:]
```

To fuzz the maze, we extend the `DictMutator` class to append dictionary keywords to the end of the seed and to remove a character from the end of the seed.

```python
class MazeMutator(DictMutator):
    def __init__(self, dictionary: Sequence[str]) -> None:
        super().__init__(dictionary)
        self.mutators.append(self.delete_last_character)
        self.mutators.append(self.append_from_dictionary)

    def append_from_dictionary(self, s: str) -> str:
        """Returns s with a keyword from the dictionary appended"""
        random_keyword = random.choice(self.dictionary)
        return s + random_keyword

    def delete_last_character(self, s: str) -> str:
        """Returns s without the last character"""
        if len(s) > 0:
            return s[:-1]
        return s
```

Let's try a standard greybox fuzzer with the classic power schedule and our extended maze mutator (n=20k).

```python
n = 20000
seed_input = " "  # empty seed

maze_mutator = MazeMutator(["L", "R", "U", "D"])
maze_schedule = PowerSchedule()
maze_fuzzer = GreyboxFuzzer([seed_input], maze_mutator, maze_schedule)

start = time.time()
maze_fuzzer.runs(FunctionCoverageRunner(maze), trials=n)
end = time.time()

"It took the fuzzer %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

We will need to print statistics for several fuzzers. Why don't we define a function for that?

```python
def print_stats(fuzzer: GreyboxFuzzer) -> None:
    total = len(fuzzer.population)
    solved = 0
    invalid = 0
    valid = 0
    for seed in fuzzer.population:
        s = maze(str(seed.data))
        if "INVALID" in s:
            invalid += 1
        elif "VALID" in s:
            valid += 1
        elif "SOLVED" in s:
            solved += 1
            if solved == 1:
                print("First solution: %s" % repr(seed))
        else:
            print("??")

    print("""Out of %d seeds,
* %4d solved the maze,
* %4d were valid but did not solve the maze, and
* %4d were invalid""" % (total, solved, valid, invalid))
```

How well does our good, old greybox fuzzer do?

```python
print_stats(maze_fuzzer)
```

It probably didn't solve the maze a single time. How can we make the fuzzer aware how "far" a seed is from reaching the target? If we know that, we can just assign more energy to that seed.

***Try it***. Print the statistics for the boosted fuzzer using the `AFLFastSchedule` and the `CountingGreyboxFuzzer`. It will likely perform much better than the unboosted greybox fuzzer: The lowest-probablity path happens to be also the path which reaches the target. You can execute your own code by opening this chapter as Jupyter notebook.

### Computing Function-Level Distance

Using the static call graph for the maze code and the target function, we can compute the distance of each function $f$ to the target $t$ as the length of the shortest path between $f$ and $t$.

Fortunately, the generated maze code includes a function called `target_tile` which returns the name of the target-function.

```python
target = target_tile()
target
```

Now, we need to find the corresponding function in the call graph. The function `get_callgraph` returns the call graph for the maze code as [networkx](https://networkx.github.io/) graph. Networkx provides some useful functions for graph analysis.

```python
import networkx as nx  # type: ignore
```

```python
from ControlFlow import get_callgraph
```

```python
cg = get_callgraph(maze_code)
for node in cg.nodes():
    if target in node:
        target_node = node
        break
```

```python
target_node
```

We can now generate the function-level distance. The dictionary `distance` contains for each function the distance to the target-function.  If there is no path to the target, we assign a maximum distance (`0xFFFF`).

The function `nx.shortest_path_length(CG, node, target_node)` returns the length of the shortest path from function `node` to function `target_node` in the call graph `CG`.

```python
distance = {}
for node in cg.nodes():
    if "__" in node:
        name = node.split("__")[-1]
    else:
        name = node
    try:
        distance[name] = nx.shortest_path_length(cg, node, target_node)
    except:
        distance[name] = 0xFFFF
```

These are the distance values for all tile-functions on the path to the target function.

```python
{k: distance[k] for k in list(distance) if distance[k] < 0xFFFF}
```

***Summary***. Using the static call graph and the target function $t$, we have shown how to compute the function-level distance of each function $f$ to the target $t$.

***Try it***. You can try and execute your own code by opening this chapter as Jupyter notebook.

* How do we compute distance if there are multiple targets? (Hint: [Geometric Mean](https://en.wikipedia.org/wiki/Geometric_mean)).
* Given the call graph (CG) and the control-flow graph (CFG$_f$) for each function $f$, how do we compute basic-block (BB)-level distance? (Hint: In CFG$_f$, measure the BB-level distance to *calls* of functions on the path to the target function. Remember that BB-level distance in functions with higher function-level distance is higher, too.)

***Read***. If you are interested in other aspects of search, you can follow up by reading the chapter on [Search-based Fuzzing](SearchBasedFuzzer.ipynb). If you are interested, how to solve the problems above, you can have a look at our paper on "[Directed Greybox Fuzzing](https://mboehme.github.io/paper/CCS17.pdf)".

### Directed Power Schedule
Now that we know how to compute the function-level distance, let's try to implement a power schedule that assigns *more energy to seeds with a lower average distance* to the target function. Notice that the distance values are all *pre-computed*. These values are injected into the program binary, just like the coverage instrumentation. In practice, this makes the computation of the average distance *extremely efficient*.

If you really want to know. Given the function-level distance $d_f(s,t)$ of a function $s$ to a function $t$ in call graph $CG$, our directed power schedule computes the seed distance $d(i,t)$ for a seed $i$ to function $t$ as $d(i,t)=\dfrac{\sum_{s\in CG} d_f(s,t)}{|CG|}$ where $|CG|$ is the number of nodes in the call graph $CG$.

```python
class DirectedSchedule(PowerSchedule):
    """Assign high energy to seeds close to some target"""

    def __init__(self, distance: Dict[str, int], exponent: float) -> None:
        self.distance = distance
        self.exponent = exponent

    def __getFunctions__(self, coverage: Set[Location]) -> Set[str]:
        functions = set()
        for f, _ in set(coverage):
            functions.add(f)
        return functions

    def assignEnergy(self, population: Sequence[Seed]) -> None:
        """Assigns each seed energy inversely proportional
           to the average function-level distance to target."""
        for seed in population:
            if seed.distance < 0:
                num_dist = 0
                sum_dist = 0
                for f in self.__getFunctions__(seed.coverage):
                    if f in list(self.distance):
                        sum_dist += self.distance[f]
                        num_dist += 1
                seed.distance = sum_dist / num_dist
                seed.energy = (1 / seed.distance) ** self.exponent
```

Let's see how the directed schedule performs against the good, old greybox fuzzer.

```python
directed_schedule = DirectedSchedule(distance, 3)
directed_fuzzer = GreyboxFuzzer([seed_input], maze_mutator, directed_schedule)

start = time.time()
directed_fuzzer.runs(FunctionCoverageRunner(maze), trials=n)
end = time.time()

"It took the fuzzer %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

```python
print_stats(directed_fuzzer)
```

It probably didn't solve a single maze either, but we have more valid solutions. So, there is definitely progress.

Let's have a look at the distance values for each seed.

```python
y = [seed.distance for seed in directed_fuzzer.population]  # type: ignore
x = range(len(y))
plt.scatter(x, y)
plt.ylim(0, max(y))
plt.xlabel("Seed ID")
plt.ylabel("Distance");
```

Let's normalize the y-axis and improve the importance of the small distance seeds.

### Improved Directed Power Schedule

The improved directed schedule normalizes seed distance between the minimal and maximal distance.
Again, if you really want to know. Given the seed distance $d(i,t)$ of a seed $i$ to a function $t$, our improved power schedule computes the new seed distance $d'(i,t)$ as
$$
d'(i,t)=\begin{cases}
1 & \text{if } d(i,t) = \text{minD} = \text{maxD}\\
\text{maxD} - \text{minD} & \text{if } d(i,t) = \text{minD} \neq \text{maxD}\\
\frac{\text{maxD} - \text{minD}}{d(i,t)-\text{minD}} & \text{otherwise}
\end{cases}
$$
where
$$\text{minD}=\min_{i\in T}[d(i,t)]$$
and
$$\text{maxD}=\max_{i\in T}[d(i,t)]$$
where $T$ is the set of seeds (i.e., the population).

```python
class AFLGoSchedule(DirectedSchedule):
    """Assign high energy to seeds close to the target"""

    def assignEnergy(self, population: Sequence[Seed]):
        """Assigns each seed energy inversely proportional
           to the average function-level distance to target."""
        min_dist: Union[int, float] = 0xFFFF
        max_dist: Union[int, float] = 0

        for seed in population:
            if seed.distance < 0:
                num_dist = 0
                sum_dist = 0
                for f in self.__getFunctions__(seed.coverage):
                    if f in list(self.distance):
                        sum_dist += self.distance[f]
                        num_dist += 1
                seed.distance = sum_dist / num_dist
            if seed.distance < min_dist:
                min_dist = seed.distance
            if seed.distance > max_dist:
                max_dist = seed.distance

        for seed in population:
            if seed.distance == min_dist:
                if min_dist == max_dist:
                    seed.energy = 1
                else:
                    seed.energy = max_dist - min_dist
            else:
                seed.energy = (max_dist - min_dist) / (seed.distance - min_dist)
```

Let's see how the improved power schedule performs.

```python
aflgo_schedule = AFLGoSchedule(distance, 3)
aflgo_fuzzer = GreyboxFuzzer([seed_input], maze_mutator, aflgo_schedule)

start = time.time()
aflgo_fuzzer.runs(FunctionCoverageRunner(maze), trials=n)
end = time.time()

"It took the fuzzer %0.2f seconds to generate and execute %d inputs." % (end - start, n)
```

```python
print_stats(aflgo_fuzzer)
```

In contrast to all previous power schedules, this one generates hundreds of solutions. It has generated many solutions.

Let's filter out all ignored input characters from the first solution. The function `filter(f, seed.data)` returns a list of elements `e` in `seed.data` where the function `f` applied on `e` returns True.

```python
for seed in aflgo_fuzzer.population:
    s = maze(str(seed.data))
    if "SOLVED" in s:
        filtered = "".join(list(filter(lambda c: c in "UDLR", seed.data)))
        print(filtered)
        break
```

This is definitely a solution for the maze specified at the beginning!

***Summary***. After pre-computing the function-level distance to the target, we can develop a power schedule that assigns more energy to a seed with a smaller average function-level distance to the target. By normalizing seed distance values between the minimum and maximum seed distance, we can further boost the directed power schedule.

***Try it***. Implement and evaluate a simpler directed power that uses the minimal (rather than average) function-level distance. What is the downside of using the minimal distance? In order to execute your code, you just need to open this chapter as Jupyter notebook.

***Read***. You can find out more about directed greybox fuzzing in the equally-named paper "[Directed Greybox Fuzzing](https://mboehme.github.io/paper/CCS17.pdf)" \cite{boehme2017greybox} and check out the implementation into AFL at [http://github.com/aflgo/aflgo](http://github.com/aflgo/aflgo).

## Synopsis

This chapter introduces advanced methods for grey-box fuzzing inspired by the popular AFL fuzzer. The `GreyboxFuzzer` class has three arguments. First, a list of seed inputs:

```python
seed_input = "http://www.google.com/search?q=fuzzing"
seeds = [seed_input]
```

Second, a _mutator_ that changes individual parts of the input.

```python
mutator = Mutator()
```

Third, a _power schedule_ that assigns fuzzing effort across the population:

```python
schedule = PowerSchedule()
```

These three go into the `GreyboxFuzzer` constructor:

```python
greybox_fuzzer = GreyboxFuzzer(seeds=seeds, mutator=mutator, schedule=schedule)
```

The `GreyboxFuzzer` class is used in conjunction with a `FunctionCoverageRunner`:

```python
http_runner = FunctionCoverageRunner(http_program)
outcomes = greybox_fuzzer.runs(http_runner, trials=10000)
```

After fuzzing, we can inspect the population:

```python
greybox_fuzzer.population[:20]
```

Besides the simple `PowerSchedule`, we can have advanced power schedules.

* `AFLFastSchedule` assigns high energy to "unusual" paths not taken very often.
* `AFLGoSchedule` assigns high energy to paths close to uncovered program locations.

The `AFLGoSchedule` class constructor requires a `distance` metric from each node towards target locations, as determined via analysis of the program code. See the chapter for details.

```python
# ignore
from ClassDiagram import display_class_hierarchy
```

```python
# ignore
display_class_hierarchy([CountingGreyboxFuzzer, AFLFastSchedule, AFLGoSchedule,
                         DictMutator, Seed],
                        public_methods=[
                            Fuzzer.run,
                            Fuzzer.__init__,
                            Fuzzer.runs,
                            Fuzzer.fuzz,
                            AdvancedMutationFuzzer.__init__,
                            AdvancedMutationFuzzer.fuzz,
                            GreyboxFuzzer.run,
                            CountingGreyboxFuzzer.run,
                            PowerSchedule.__init__,
                            DirectedSchedule.__init__,
                            AFLGoSchedule.__init__,
                            AFLFastSchedule.__init__,
                            Seed.__init__,
                            Mutator.__init__,
                            DictMutator.__init__,
                        ],
                        types={'Location': Location},
                        project='fuzzingbook')
```

## Lessons Learned

* A *greybox fuzzer* generates thousands of inputs per second. Pre-processing and lightweight instrumentation
  * allows maintaining the efficiency *during* the fuzzing campaign, and
  * still provides enough information to control progress and slightly steer the fuzzer.
* The *power schedule* allows _steering and controlling_ the fuzzer. For instance,
  * Our [boosted greybox fuzzer](#Fuzzer-Boosting) spends more energy on seeds that exercise "unlikely" paths. The hope is that the generated inputs exercise even more unlikely paths. This in turn increases the number of paths explored per unit time.
  * Our [directed greybox fuzzer](#Directed-Greybox-Fuzzing) spends more energy on seeds that are "closer" to a target location. The hope is that the generated inputs get even closer to the target.
* The *mutator* defines the fuzzer's search space. [Customizing the mutator](GreyboxFuzzer.ipynb#A-First-Attempt) for the given program allows reducing the search space to only relevant inputs. In a couple of chapters, we'll learn about [dictionary-based, and grammar-based mutators](GreyboxGrammarFuzzer.ipynb) to increase the ratio of valid inputs generated.

## Background

* **Find out more about AFL**: http://lcamtuf.coredump.cx/afl/
* **Learn about LibFuzzer** (another famous greybox fuzzer): http://llvm.org/docs/LibFuzzer.html
* **How quickly must a whitebox fuzzer exercise each path to remain more efficient than a greybox fuzzer?** Marcel Böhme and Soumya Paul. 2016. [A Probabilistic Analysis of the Efficiency of Automated Software Testing](https://mboehme.github.io/paper/TSE15.pdf), IEEE TSE, 42:345-360 \cite{boehme2016efficiency}

## Next Steps

Our aim is still to sufficiently cover functionality, such that we can trigger as many bugs as possible.  To this end, we focus on two classes of techniques:

1. Try to cover as much _specified_ functionality as possible.  Here, we would need a _specification of the input format,_ distinguishing between individual input elements such as (in our case) numbers, operators, comments, and strings – and attempting to cover as many of these as possible.  We will explore this as it comes to [grammar-based testing](GrammarFuzzer.ipynb), and especially in [grammar-based mutations](GreyboxGrammarFuzzer.ipynb).

2. Try to cover as much _implemented_ functionality as possible.  The concept of a "population" that is systematically "evolved" through "mutations" will be explored in depth when discussing [search-based testing](SearchBasedFuzzer.ipynb).  Furthermore, [symbolic testing](SymbolicFuzzer.ipynb) introduces how to systematically reach program locations by solving the conditions that lie on their paths.

These two techniques make up the gist of the book; and, of course, they can also be combined with each other.  As usual, we provide runnable code for all.  Enjoy!

We're done, so we clean up:

```python
import os
```

```python
if os.path.exists('callgraph.dot'):
    os.remove('callgraph.dot')

if os.path.exists('callgraph.py'):
    os.remove('callgraph.py')
```

## Compatibility

In previous version of the chapter, the `AdvancedMutationFuzzer` class was named simply `MutationFuzzer`, causing name confusion with the `MutationFuzzer` class in the [introduction to mutation-based fuzzing](MutationFuzzer.ipynb). The following declaration introduces a backward-compatible alias.

```python
class MutationFuzzer(AdvancedMutationFuzzer):
    pass
```

## Exercises

To be added. \todo{}