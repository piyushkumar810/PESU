# Create a dictionary that maps words to their lengths from a given sentence.
user=input("enter the sentence").strip()
print(f"your sentence is {user}")

extract_word=user.split()

dict_word={word:(len(word)) for word in extract_word}

print(dict_word)