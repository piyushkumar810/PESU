# normal dictionary
d = {}

for x in range(1, 21):
    if x % 3 == 0:
        d[x] = x ** 3

print(d)

newdict={x:x**3 for x in range(1,21) if(x%3==0)}
print(newdict)