result = set()

for x in range(1, 21):
    if x % 2 == 0:
        result.add(x * x)

print(result)


# -------set compherension
newset={x*x for x in range(1,21) if(x%2==0)}
print(newset)