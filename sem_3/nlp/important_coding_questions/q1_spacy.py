'''🔥 Exam-type question

Question:
Given a string, use spaCy to perform:

Tokenization
Lemmatization
Remove stopwords
Create Bag of Words

✅ Code to learn
'''

import spacy
from collections import Counter

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Given string
text = "The students are learning natural language processing. The students love NLP."

# Process the text
doc = nlp(text)

# --------------------------------
# 1. Tokenization
# --------------------------------
tokens = [token.text for token in doc]

print("Tokens:")
print(tokens)


# --------------------------------
# 2. Lemmatization
# --------------------------------
lemmas = [token.lemma_ for token in doc]

print("\nLemmatization:")
print(lemmas)


# --------------------------------
# 3. Remove Stopwords
# --------------------------------
filtered_words = [
    token.lemma_
    for token in doc
    if not token.is_stop and not token.is_punct
]

print("\nAfter Stopword Removal:")
print(filtered_words)


# --------------------------------
# 4. Bag of Words
# --------------------------------
bow = Counter(filtered_words)

print("\nBag of Words:")
print(bow)