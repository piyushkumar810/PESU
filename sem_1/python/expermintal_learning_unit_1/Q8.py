'''
Define count_vowels(text) that counts and returns the number of vowels in a string.
'''

def count_vowels(text):
    vowels="aeiouAEIOU"
    counter=0
    
    for ch in text:
        if ch in vowels:
            counter=counter+1
    return counter
        
sentence="hellO WorLD"
result=count_vowels(sentence)
print("number of vowels: ",result)