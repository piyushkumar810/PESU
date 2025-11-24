from collections import Counter
n=input("enter the string: ")
freq=Counter(n)
print(freq)

for char, count in freq.items():
    if count>2:
        print(f"{char} with {count}")