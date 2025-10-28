# from two lists via zip
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = {k: v for k, v in zip(keys, vals)}
# {'a': 1, 'b': 2, 'c': 3}
print(d)
