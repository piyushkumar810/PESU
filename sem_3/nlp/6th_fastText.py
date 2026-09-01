# Import the FastText class from the models module of Gensim
from gensim.models import FastText


# Create a small training dataset
# Each inner list represents one sentence
# Each word is written separately (tokenized)
sentences = [
    ["i", "love", "python"],              # Sentence 1
    ["python", "is", "easy"],             # Sentence 2
    ["i", "love", "machine", "learning"]  # Sentence 3
]


# Create and train the FastText model
model = FastText(

    # sentences = training data given to FastText
    sentences,

    # vector_size = size/dimension of each word vector
    # Here, every word is represented using 50 numbers
    vector_size=50,

    # window = maximum distance between the current word
    # and neighboring words
    # window=3 means it looks at up to 3 words around a word
    window=3,

    # min_count = minimum number of times a word must appear
    # min_count=1 means even words appearing only once are included
    min_count=1,

    # epochs = number of times the complete dataset is used
    # to train the model
    epochs=10
)


# Get the vector representation of the word "python"
# .wv = Word Vectors stored inside the FastText model
# ["python"] = access the vector of the word python
print(model.wv["python"])


# Find the 3 words most similar to "python"
# most_similar() compares word vectors
# "python" = word for which we want similar words
# topn=3 = return the top 3 similar words
print(model.wv.most_similar("python", topn=3))


'''
note:- 
FastText is a word embedding technique developed by Facebook/Meta that represents words using
 character n-grams, allowing it to handle rare and out-of-vocabulary words better than 
 traditional Word2Vec.
'''