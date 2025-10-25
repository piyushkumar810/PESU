'''
Write a function is_palindrome(word) that returns True if the string is palindrome (case insensitive).
'''

def palindrome(word):
    word=word.lower()
    reversed_word=""
    
    for ch in word:
        reversed_word=ch+reversed_word
        
    if word ==reversed_word:
        return True
    else:
        return False
        
text="Madam"
result=palindrome(text)
print("is palindrome: ",result)