import nltk
from nltk.corpus import brown

nltk.download('brown')

# Get words
words = brown.words()

# Print first 5 words
print("First 5 words:")
print(words[:5])

# Get sentences
sentences = brown.sents()

# Print first 5 sentences
print("\nFirst 5 sentences:")
for sentence in sentences[:5]:
    # print(sentence)
    # using join
    print(" ".join(sentence))