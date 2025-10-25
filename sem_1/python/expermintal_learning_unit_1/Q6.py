'''
Use deque to check if a string (ignore case and non-alphanumerics) is a palindrome by 
popping from both ends. Print TRUE/FALSE.
'''

from collections import deque

user_input=input("enter a string: ")

cleaned=""
for ch in user_input:
    if ch.isalnum():
        cleaned += ch.lower()
        
dq=deque(cleaned)

is_palindrome=True

while len(dq)>1:
    if dq.popleft()!=dq.pop():
        is_palindrome=False
        break
    
if is_palindrome:
    print("TRUE")
else:
    print("False")
    