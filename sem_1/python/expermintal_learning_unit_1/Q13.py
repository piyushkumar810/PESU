'''
Write reverse_words(sentence) that returns the sentence with words reversed but order preserved.
'''

def reverse_word(sentence):
    words=sentence.split()
    reversed_list=[]
    
    for word in words:
        reversed_word=word[::-1]
        reversed_list.append(reversed_word)
        
    final_sentence=" ".join(reversed_list)
    return final_sentence
    
text="hello pyhton world"
result=reverse_word(text)
print("reversed word is : ",result)