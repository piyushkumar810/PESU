# Import KeyedVectors class from the models module of Gensim
from gensim.models import KeyedVectors


# Load a pre-trained Word2Vec model
# KeyedVectors stores word embeddings (vectors) of words
model = KeyedVectors.load_word2vec_format(
    
    # Name/path of the pre-trained Word2Vec model file
    "word2vec.bin",
    
    # binary=True means the model file is in binary format
    # Use binary=False if the file is in text format
    binary=True
)


# Find the 5 words most similar to "king"
# most_similar() compares the word vectors
# "king" is the input word
# topn=5 means return the top 5 most similar words
print(model.most_similar("king", topn=5))


# Calculate the similarity between two words
# similarity() uses cosine similarity between their vectors
# "king" = first word
# "queen" = second word
# The result is usually between -1 and 1
print(model.similarity("king", "queen"))