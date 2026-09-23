# ==========================================================
# NLP UNIT 1 - COMPLETE WORKING CODE
# ==========================================================

import re
import spacy
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# ----------------------------------------------------------
# 1. INPUT TEXT
# ----------------------------------------------------------

text = "The students are studying NLP. NLP is very interesting and useful!"


# ----------------------------------------------------------
# 2. LOWERCASE
# ----------------------------------------------------------

text_lower = text.lower()

print("\n1. LOWERCASE")
print(text_lower)


# ----------------------------------------------------------
# 3. SPLIT
# ----------------------------------------------------------

words_split = text_lower.split()

print("\n2. SPLIT")
print(words_split)


# ----------------------------------------------------------
# 4. TOKENIZATION USING NLTK
# ----------------------------------------------------------

tokens = word_tokenize(text_lower)

print("\n3. TOKENIZATION")
print(tokens)


# ----------------------------------------------------------
# 5. REMOVE PUNCTUATION
# ----------------------------------------------------------

clean_text = re.sub(r'[^\w\s]', '', text_lower)

print("\n4. REMOVE PUNCTUATION")
print(clean_text)


# ----------------------------------------------------------
# 6. STOPWORD REMOVAL
# ----------------------------------------------------------

stop_words = set(stopwords.words("english"))

words = word_tokenize(clean_text)

filtered_words = [
    word for word in words
    if word not in stop_words
]

print("\n5. STOPWORD REMOVAL")
print(filtered_words)


# ----------------------------------------------------------
# 7. STEMMING
# ----------------------------------------------------------

stemmer = PorterStemmer()

stemmed_words = [
    stemmer.stem(word)
    for word in filtered_words
]

print("\n6. STEMMING")
print(stemmed_words)


# ----------------------------------------------------------
# 8. LEMMATIZATION
# ----------------------------------------------------------

lemmatizer = WordNetLemmatizer()

lemmatized_words = [
    lemmatizer.lemmatize(word)
    for word in filtered_words
]

print("\n7. LEMMATIZATION")
print(lemmatized_words)


# ----------------------------------------------------------
# 9. POS TAGGING
# ----------------------------------------------------------

pos_tags = pos_tag(tokens)

print("\n8. POS TAGGING")
print(pos_tags)


# ----------------------------------------------------------
# 10. BAG OF WORDS
# ----------------------------------------------------------

documents = [
    "NLP is interesting",
    "NLP is useful",
    "NLP is interesting and useful"
]

bow = CountVectorizer()

bow_matrix = bow.fit_transform(documents)

print("\n9. BAG OF WORDS")
print("Vocabulary:")
print(bow.get_feature_names_out())

print("BoW Matrix:")
print(bow_matrix.toarray())


# ----------------------------------------------------------
# 11. TF-IDF
# ----------------------------------------------------------

tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(documents)

print("\n10. TF-IDF")
print("Vocabulary:")
print(tfidf.get_feature_names_out())

print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())


# ----------------------------------------------------------
# 12. N-GRAMS (BIGRAM)
# ----------------------------------------------------------

bigram = CountVectorizer(ngram_range=(2, 2))

bigram_matrix = bigram.fit_transform(documents)

print("\n11. BIGRAM")
print("Bigrams:")
print(bigram.get_feature_names_out())

print("Bigram Matrix:")
print(bigram_matrix.toarray())


# ----------------------------------------------------------
# 13. N-GRAMS (TRIGRAM)
# ----------------------------------------------------------

trigram = CountVectorizer(ngram_range=(3, 3))

trigram_matrix = trigram.fit_transform(documents)

print("\n12. TRIGRAM")
print("Trigrams:")
print(trigram.get_feature_names_out())

print("Trigram Matrix:")
print(trigram_matrix.toarray())


# ==========================================================
# SPACY
# ==========================================================

# Load English spaCy model
nlp = spacy.load("en_core_web_sm")

doc = nlp(text)

print("\n13. SPACY TOKENIZATION + POS")

for token in doc:
    print(token.text, "->", token.pos_)


# ==========================================================
# SPACY USEFUL OUTPUT
# ==========================================================

print("\n14. SPACY TOKENS")

for token in doc:
    print(token.text)


print("\n15. SPACY LEMMATIZATION")

for token in doc:
    print(token.text, "->", token.lemma_)


print("\n16. SPACY POS TAGGING")

for token in doc:
    print(token.text, "->", token.pos_, "->", token.tag_)