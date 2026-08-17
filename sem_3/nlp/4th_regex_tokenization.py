import re
import spacy
nlp=spacy.blank("en")

email="virat@kholi.com"

token=re.findall(r'\w+|@|\.', email)
print(token)


# q1) input_test="abc123def456"
'''
# ---- output should be like:- 
abc123def456
['abc', '123', 'def', '456']
abcdef
'''
input_test="abc123def456"
print(input_test)

token1=re.findall(r'[A-Za-z]+|\d+', input_test)
print(token1)
'''
token2=re.findall(r'[A-Za-z]',input_test)
print(token2)

# this gave me solution - ['a', 'b', 'c', 'd', 'e', 'f'] but we want "abcdef"
'''
token2=''.join(re.findall(r'[A-Za-z]',input_test))
print(token2)


# question 2
'''
input_test = "hello123world456"

# Expected:
# ['hello', '123', 'world', '456']
'''

input_test1 = "hello123world456"
token3=re.findall(r'[A-Za-z]+|\d+',input_test1)
print(token3)


# Question 3 — Extract only numbers
'''
input_test = "Python123 is easy456"

Task: Extract only the numbers.

Expected:
['123', '456']
'''
input_test2 = "Python123 is easy456"

token4=re.findall(r'\d[0-9]+|\d[0-9]',input_test2)
print(token4)


# Question 3 — Extract only alphabets
'''
input_test = "Python123Java456C789"

Task: Extract only alphabetic words.

Expected:
['Python', 'Java', 'C']
'''

text="Python123Java456C789"
token5=(re.findall(r'[A-Za-z]+',text))
print(token5)


# question 4
'''
input_test = "hello123@world456#python"

Words: ['hello', 'world', 'python']
Numbers: ['123', '456']
'''
import re
import spacy
input_test4 = "hello123@world456#python"
words=re.findall(r'[A-Za-z]+',input_test4)
number=re.findall(r'[0-9]+',input_test4)
print(words)
print(number)


# Question 5 — Using \w
'''
input_test = "hello123 world456 python"

# output
['hello123', 'world456', 'python']
'''
import re
import spacy
input_test5 = "hello123 world456 python"
token6=re.findall(r'\w+',input_test5)
print(token6)

'''
Explanation
\w

matches word characters:

A-Z
a-z
0-9
_

So hello123 stays together.
'''

# Question 6 — Extract numbers
'''
input_test = "I have 2 apples and 10 bananas."

output:- 
['2', '10']
'''
import re
input_test8 = "I have 2 apples and 10 bananas."
numbers = re.findall(r'\d+', input_test8)
print(numbers)


# Question 7 — Extract words
'''
input_test = "I love Python programming!"

['I', 'love', 'Python', 'programming']
'''
import re
input_test = "I love Python programming!"
words = re.findall(r'[A-Za-z]+', input_test)
print(words)


# Question 8 — Separate letters and numbers
'''
['A', '12', 'B', '34', 'C', '56', 'D', '78']
'''
import re
input_test = "A12B34C56D78"
tokens = re.findall(r'[A-Za-z]+|\d+', input_test)
print(tokens)

# Question 9 — Extract decimal numbers
import re
input_test = "The price is 25.50 dollars and discount is 10.5%"
numbers = re.findall(r'\d+\.\d+', input_test)
print(numbers)

# Question 10 — Extract email addresses
import re
input_test = "Contact abc@gmail.com or xyz@yahoo.com"
emails = re.findall(r'\w+@\w+\.\w+', input_test)
print(emails)