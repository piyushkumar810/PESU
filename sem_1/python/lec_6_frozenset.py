# ---------------------------------------------- FtozenSet()---------------------------------------

'''
In Python, a frozenset is just like a set, but it is immutable — meaning you cannot change it 
(no adding or removing elements).

set → changeable
frozenset → unchangeable (frozen set)
'''
# normal set (changeable)
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")   # ✅ works fine
print(fruits)

# frozen set (unchangeable)
frozen_fruits = frozenset(["apple", "banana", "cherry"])
# frozen_fruits.add("mango") ❌ will give error
print(frozen_fruits)


# example of use
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print(a.union(b))        # frozenset({1, 2, 3, 4, 5})
print(a.intersection(b)) # frozenset({3})
