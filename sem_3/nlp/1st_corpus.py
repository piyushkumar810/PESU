import nltk
from nltk.corpus import brown

nltk.download('brown')

words = brown.words()

print("First 5 words:")
print(words[:5])

sentences = brown.sents()

print("\nFirst 5 sentences:")
for sentence in sentences[:5]:
    print(sentence)
    print()
    # using join
    print(" ".join(sentence))