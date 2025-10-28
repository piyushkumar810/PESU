# ----------------- dictionary comperhension

# -> simple
# -> conditional
# -> nested
# -> nested conditional

'''
1. Simple dictionary comprehension
Pattern: {key_expr: value_expr for item in iterable}
'''

# map numbers to their squares
squares = {n: n*n for n in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# from two lists via zip
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = {k: v for k, v in zip(keys, vals)}
# {'a': 1, 'b': 2, 'c': 3}
print(d)

'''
Notes:
zip() pairs elements from both lists position by position:

If keys repeat, later values overwrite earlier ones (same as normal dict assignment).
Comprehension executes eagerly (builds full dict immediately).
'''


'''
2. Conditional dictionary comprehension

Pattern: {k: v for item in iterable if condition} — filter items.
You can also use conditional expressions inside values: {k: (expr_if_true if cond else expr_if_false) for ...}
'''
# include only even numbers
even_squares = {n: n*n for n in range(10) if n % 2 == 0}
# {0:0, 2:4, 4:16, 6:36, 8:64}

# conditional expression in the value
classification = {n: ("even" if n % 2 == 0 else "odd") for n in range(6)}
# {0: 'even', 1: 'odd', 2: 'even', ...}


'''
3. Nested dictionary comprehensions
You can nest comprehensions to build multi-level dicts. Syntax becomes {outer_key: {inner_key: inner_val for ...} for ...}.
'''
# multiplication table: {row: {col: product}}
table = {i: {j: i*j for j in range(1, 6)} for i in range(1, 4)}
# {
#  1: {1:1, 2:2, 3:3, 4:4, 5:5},
#  2: {1:2, 2:4, 3:6, ...},
#  3: {...}
# }

# group words by first letter -> nested dict of counts
# multiplication table: {row: {col: product}}
table = {i: {j: i*j for j in range(1, 6)} for i in range(1, 4)}
# {
#  1: {1:1, 2:2, 3:3, 4:4, 5:5},
#  2: {1:2, 2:4, 3:6, ...},
#  3: {...}
# }

# group words by first letter -> nested dict of counts
words = ["apple", "ant", "ball", "bat", "cat"]
grouped = {
    ch: {w: len(w) for w in words if w[0] == ch}
    for ch in sorted({w[0] for w in words})
}
# {'a': {'apple': 5, 'ant': 3}, 'b': {'ball': 4, 'bat': 3}, 'c': {'cat': 3}}


'''
4. Nested conditional (combined patterns)

Combine filters and conditional expressions inside nested comprehensions.

Example — create a nested dict where values are classified but only include lengths ≥ 3:
'''

words = ["a", "ant", "apple", "by", "bat"]
nested = {
    first: {
        w: ("long" if len(w) >= 5 else "short")
        for w in words
        if w[0] == first and len(w) >= 3
    }
    for first in sorted({w[0] for w in words})
}
# {'a': {'ant': 'short', 'apple': 'long'}, 'b': {'bat': 'short'}}


# ------------------------------------------ advance usage of dictionary comhrension
# Advanced techniques & useful patterns
# a) From enumerables with indices
# index -> value
d = {i: v for i, v in enumerate(["a","b","c"], 1)}  # start index at 1
# {1: 'a', 2: 'b', 3: 'c'}

# b) Multiple iterables (cartesian product)
# pair sums
d = {(i, j): i + j for i in range(3) for j in range(3)}
# {(0,0):0, (0,1):1, ...}

# c) From sequences where you need uniqueness or transformation
# last occurrence index of each character
s = "abracadabra"
last_index = {ch: i for i, ch in enumerate(s)}
# result: {'a':10, 'b':8, 'r':9, 'c':4, 'd':6}

# d) Combining dicts with comprehension
# merging two dicts but prefer values from b if they exist
a = {'x': 1, 'y': 2}
b = {'y': 20, 'z': 30}
merged = {k: (b[k] if k in b else a[k]) for k in set(a) | set(b)}
# {'x':1, 'y':20, 'z':30}

# e) Using functions inside comprehension
def expensive(x):
    # imagine heavy compute
    return x*x

d = {x: expensive(x) for x in range(10)}