# --------------------- iterator -------------------
nums=[10,20,30]
it=iter(nums)
print(next(it))

# infinit cycle with itertool

# generator
# yield automatically implementation the iterator protocol

# given two list build a dict only for pair
key = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]

dist = dict(zip(key, values))
print(dist)
