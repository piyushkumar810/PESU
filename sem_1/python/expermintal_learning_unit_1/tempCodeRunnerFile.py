
from collections import Counter
user_input=input("Enter a string: ")
frequency=Counter(user_input)
print(frequency)

print("\ncharacter with frequency greater than 2: ")
for char, count in frequency.items():
    if count>2:
        print(f"'{char}': {count}")