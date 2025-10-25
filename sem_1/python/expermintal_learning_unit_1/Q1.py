'''
Write a Python program that uses a loop to count the frequency 
of each character in a given string using collections. 
Display only those characters whose frequency is greater than 2.
'''

from collections import Counter
user_input=input("Enter a string: ")
frequency=Counter(user_input)

print("\ncharacter with frequency greater than 2: ")
for char, count in frequency.items():
    if count>2:
        print(f"'{char}': {count}")