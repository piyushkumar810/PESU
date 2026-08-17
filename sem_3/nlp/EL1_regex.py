'''
Tasks:-
1. Extract all alphabetic words.
2. Extract all integers.
3. Extract all decimal numbers.
4. Extract the email address.
5. Extract the numbers and words together as tokens.
6. Extract special symbols such as @, $, %, :, _.
7. Create one final tokenizer that separates:
        words
        integers
        decimals
        symbols
'''

import re

input_test = """
Student Piyush123 scored 95.5% in Python.
Contact: piyush123@gmail.com
Fees: $2500.50
Roll_No: 28
"""

print(input_test)

# 1) Extract only alphabets
words = re.findall(r'[A-Za-z]+', input_test)
print("Words:", words)


# 2) Extract integers
integers = re.findall(r'\d+', input_test)
print("Integers:", integers)


# 3) Extract decimal numbers
decimals = re.findall(r'\d+\.\d+', input_test)
print("Decimals:", decimals)


# 4) Extract email address
email = re.findall(r'\w+@\w+\.\w+', input_test)
print("Email:", email)


# 5) Extract words and numbers together
tokens = re.findall(r'[A-Za-z]+|\d+', input_test)
print("Words + Numbers:", tokens)


# 6) Extract special symbols
symbols = re.findall(r'[^A-Za-z0-9\s]', input_test)
print("Symbols:", symbols)


# 7) Final tokenizer
final_tokens = re.findall(
    r'\d+\.\d+|[A-Za-z]+|\d+|[^A-Za-z0-9\s]',
    input_test
)

print("Final Tokens:", final_tokens)


'''
# very importsnt

r'\d+\.\d+|[A-Za-z]+|\d+|[^A-Za-z0-9\s]'

\d+\.\d+       → decimal numbers
      |
[A-Za-z]+      → words
      |
\d+            → integers
      |
[^A-Za-z0-9\s] → special symbols
'''