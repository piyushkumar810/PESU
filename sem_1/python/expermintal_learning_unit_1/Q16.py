'''
Define contains_word(sentence, word) that returns how many times the word appears (case insensitive).
Print message accordingly.
'''

def contains_word(sentence,word):
    sentence_lower=sentence.lower()
    word_lower=word.lower()
    
    word_list=sentence_lower.split()
    
    count=0
    for wrd in word_list:
        if wrd == word_lower:
            count+=1
    return count
    
input_sentence=input("enter a sentence: ")
input_word=input("enter a word to search: ")

word_occurrences=contains_word(input_sentence,input_word)

if word_occurrences>0:
    print(f"the word '{input_word}' appears {word_occurrences} times.")
else:
    print(f"the word '{input_word}' does not appear in the sentence.")
    