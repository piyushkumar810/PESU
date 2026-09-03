from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd

# Three-line corpus
corpus = [
    "Data science is amazing",
    "Machine learning is a part of datat science",
    "I enjoy learning Science and data"
]

# Bag of Words
vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(corpus)

# Convert into DataFrame
df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)

# Display DataFrame
print("Bag of Words - Frequency:")
print(df)

# ---------------- BAG OF WORDS ----------------

bow_vectorizer = CountVectorizer()

# Convert corpus into Bag of Words matrix
bow_matrix = bow_vectorizer.fit_transform(corpus)

# Display words
print("Bag of Words Features:")
print(bow_vectorizer.get_feature_names_out())

# Display frequency/count matrix
print("\nBag of Words Frequency Matrix:")
print(bow_matrix.toarray())



# -------------------------Create TF-IDF vectorizer


vectorizer = TfidfVectorizer()

# Convert corpus into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(df["Text"])

# Create TF-IDF DataFrame
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print("\nTF-IDF DataFrame:")
print(tfidf_df)

# Convert corpus into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(corpus)

# Display words/features
print("Features:")
print(vectorizer.get_feature_names_out())

# Display TF-IDF values
print("TF-IDF Matrix:")
print(tfidf_matrix.toarray())