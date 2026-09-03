from sklearn.feature_extraction.text import CountVectorizer

# Text
text = "NLP is powerful and intuitive language processing is natural language understanding"

# 8. N-grams (e.g., bi-grams)
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2))

# Create bi-gram matrix
bigram_matrix = bigram_vectorizer.fit_transform([text])

# Display bi-grams
print("Bi-grams:")
print(bigram_vectorizer.get_feature_names_out())

# Display matrix
print("Bi-gram Matrix:")
print(bigram_matrix.toarray())


'''
from sklearn.feature_extraction.text import CountVectorizer

text = "NLP is powerful and intuitive language processing"

vectorizer = CountVectorizer(ngram_range=(1, 2))

matrix = vectorizer.fit_transform([text])

print("N-grams:")
print(vectorizer.get_feature_names_out())

print("N-gram Matrix:")
print(matrix.toarray())
'''