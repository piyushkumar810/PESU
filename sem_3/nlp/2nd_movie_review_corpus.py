import nltk
from nltk.corpus import movie_reviews

nltk.download('movie_reviews')

words = movie_reviews.words()

# getting total no of words
print(len(words))

sentences = movie_reviews.sents()

# no of sentences
print(len(sentences))

files = movie_reviews.fileids()

# document
print(len(files))

# fetching first 5 documents
print(files[:5])

categories = movie_reviews.categories()

# category
print(categories)

# review the category
for category in categories:
    print(category, ":", len(movie_reviews.fileids(category)))

# first 5 
print(words[:5])

print("\n7. First 5 sentences:")

for sentence in sentences[:5]:
    print(sentence)
    print()
    print(" ".join(sentence))
    print()

positive_words = movie_reviews.words(categories="pos")

print("\n8. Number of words in positive reviews:")
print(len(positive_words))

negative_words = movie_reviews.words(categories="neg")

print("\n9. Number of words in negative reviews:")
print(len(negative_words))

print("\n10. First positive review:")

positive_files = movie_reviews.fileids("pos")

print(movie_reviews.raw(positive_files[0]))

print("\n11. First negative review:")

negative_files = movie_reviews.fileids("neg")

print(movie_reviews.raw(negative_files[0]))

print("\n========== CORPUS INFORMATION ==========")

print("Corpus name: Movie Reviews Corpus")
print("Type: Movie review text corpus")
print("Categories:", categories)
print("Total documents:", len(files))
print("Total words:", len(words))
print("Total sentences:", len(sentences))