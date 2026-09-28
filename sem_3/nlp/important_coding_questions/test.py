# ============================================================
# NLP UNIT 2 - COMPLETE PRACTICAL CODE
# Using spaCy
# ============================================================

import spacy
import re


# ============================================================
# LOAD SPACY MODEL
# ============================================================

nlp = spacy.load("en_core_web_sm")


# ============================================================
# UNIVERSAL TEXT
# We use the SAME text for all questions
# ============================================================

text = """
Piyush is studying Natural Language Processing at PES University
in Bengaluru. He is learning NLP concepts and working with
machine learning models. Amazon is a large organization.
The students are learning, studying, playing and running.
"""


# Create spaCy document once
doc = nlp(text)


print("=" * 60)
print("ORIGINAL TEXT")
print("=" * 60)

print(text)


# ============================================================
# Q1. TOKENIZATION
# Perform tokenization and display all tokens
# ============================================================

print("\n" + "=" * 60)
print("Q1. TOKENIZATION")
print("=" * 60)

for token in doc:
    print(token.text)


# ============================================================
# Q2. QUESTION NOT AVAILABLE
# ============================================================

print("\n" + "=" * 60)
print("Q2. QUESTION NOT AVAILABLE")
print("=" * 60)

print("Question 2 was not visible/provided.")


# ============================================================
# Q3. LOWERCASE
# Convert text into lowercase
# ============================================================

print("\n" + "=" * 60)
print("Q3. LOWERCASE")
print("=" * 60)

lower_text = text.lower()

print(lower_text)


# ============================================================
# Q4. STOP-WORD REMOVAL
# Remove stop words using spaCy
# ============================================================

print("\n" + "=" * 60)
print("Q4. STOP-WORD REMOVAL")
print("=" * 60)

for token in doc:

    if not token.is_stop and not token.is_punct:

        print(token.text)


# ============================================================
# Q5. PUNCTUATION REMOVAL
# Display only words after removing punctuation
# ============================================================

print("\n" + "=" * 60)
print("Q5. PUNCTUATION REMOVAL")
print("=" * 60)

for token in doc:

    if not token.is_punct:

        print(token.text)


# ============================================================
# Q6. ALPHABETIC WORDS
# Display only alphabetic words
# ============================================================

print("\n" + "=" * 60)
print("Q6. ALPHABETIC WORDS")
print("=" * 60)

for token in doc:

    if token.is_alpha:

        print(token.text)


# ============================================================
# Q7. LEMMATIZATION
# Display original word and lemma
# ============================================================

print("\n" + "=" * 60)
print("Q7. LEMMATIZATION")
print("=" * 60)

for token in doc:

    if token.is_alpha:

        print(token.text, "->", token.lemma_)


# ============================================================
# Q8. PARTS OF SPEECH (POS)
# Display word and POS tag
# ============================================================

print("\n" + "=" * 60)
print("Q8. PARTS OF SPEECH (POS)")
print("=" * 60)

for token in doc:

    if token.is_alpha:

        print(token.text, "->", token.pos_)


# ============================================================
# Q9. NAMED ENTITY RECOGNITION (NER)
# Display entity and its label
# ============================================================

print("\n" + "=" * 60)
print("Q9. NAMED ENTITY RECOGNITION")
print("=" * 60)

for ent in doc.ents:

    print(ent.text, "->", ent.label_)


# ============================================================
# Q10. COMPLETE TEXT PREPROCESSING
#
# 1. Lowercase
# 2. Stop-word removal
# 3. Punctuation removal
# 4. Lemmatization
# ============================================================

print("\n" + "=" * 60)
print("Q10. COMPLETE TEXT PREPROCESSING")
print("=" * 60)

cleaned_words = []

for token in doc:

    # Remove punctuation
    if token.is_punct:
        continue

    # Remove stopwords
    if token.is_stop:
        continue

    # Keep alphabetic words
    if not token.is_alpha:
        continue

    # Lemmatization
    cleaned_words.append(token.lemma_.lower())


cleaned_text = " ".join(cleaned_words)

print("Final Cleaned Text:")
print(cleaned_text)


# ============================================================
# Q11. PREPROCESS + LEMMATIZATION + POS TAGS
#
# Display final cleaned and lemmatized tokens
# along with POS tags
# ============================================================

print("\n" + "=" * 60)
print("Q11. CLEANED + LEMMATIZED TOKENS + POS")
print("=" * 60)

for token in doc:

    # Remove punctuation
    if token.is_punct:
        continue

    # Remove stopwords
    if token.is_stop:
        continue

    # Keep alphabetic words
    if not token.is_alpha:
        continue

    print(
        token.text,
        "->",
        token.lemma_,
        "->",
        token.pos_
    )


# ============================================================
# Q12. WORD EMBEDDINGS
#
# spaCy pretrained model can provide word vectors.
# en_core_web_sm has limited/no real word vectors depending
# on spaCy model version, so we demonstrate the correct
# spaCy syntax.
# ============================================================

print("\n" + "=" * 60)
print("Q12. WORD EMBEDDING")
print("=" * 60)

word = "learning"

token = nlp(word)[0]

print("Word:", word)

print("Vector:")
print(token.vector)

print("Vector size:")
print(token.vector.shape)


# ============================================================
# WORD SIMILARITY USING SPACY
# ============================================================

print("\n" + "=" * 60)
print("WORD SIMILARITY")
print("=" * 60)

word1 = nlp("king")
word2 = nlp("queen")

print(
    "Similarity between king and queen:",
    word1.similarity(word2)
)


# ============================================================
# Q13. CBOW USING WORD2VEC
#
# NOTE:
# CBOW training is not implemented by spaCy.
# Word2Vec training is normally done using gensim.
# ============================================================

print("\n" + "=" * 60)
print("Q13. CBOW USING WORD2VEC")
print("=" * 60)

from gensim.models import Word2Vec


# Training sentences
sentences = [
    ["piyush", "is", "learning", "nlp"],
    ["students", "are", "learning", "nlp"],
    ["students", "are", "studying", "machine", "learning"],
    ["piyush", "is", "studying", "machine", "learning"],
    ["nlp", "is", "a", "branch", "of", "ai"],
    ["machine", "learning", "is", "part", "of", "ai"]
]


# CBOW
# sg=0 means CBOW
cbow_model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=2,
    min_count=1,
    sg=0,
    epochs=100
)


word = "learning"

print("Top 5 words similar to:", word)

similar_words = cbow_model.wv.most_similar(
    word,
    topn=5
)

for w, similarity in similar_words:

    print(w, "->", similarity)


# ============================================================
# Q14. SKIP-GRAM USING WORD2VEC
# ============================================================

print("\n" + "=" * 60)
print("Q14. SKIP-GRAM USING WORD2VEC")
print("=" * 60)


# Skip-Gram
# sg=1 means Skip-Gram

skipgram_model = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=2,
    min_count=1,
    sg=1,
    epochs=100
)


word = "learning"

print("Top 5 words similar to:", word)

similar_words = skipgram_model.wv.most_similar(
    word,
    topn=5
)

for w, similarity in similar_words:

    print(w, "->", similarity)


# ============================================================
# END
# ============================================================

print("\n" + "=" * 60)
print("ALL UNIT 2 PRACTICALS COMPLETED")
print("=" * 60)