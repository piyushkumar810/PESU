# ============================================
# NLP UNIT 2 - COMPLETE CODE
# Using spaCy + Gensim + NumPy + TensorFlow
# ============================================


# ============================================
# INSTALLATION
# ============================================
# Run these once in terminal:
#
# pip install spacy gensim numpy scikit-learn tensorflow
# python -m spacy download en_core_web_sm
#
# ============================================


import spacy
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from gensim.models import Word2Vec, FastText


# ============================================
# 1. LOAD spaCy MODEL
# ============================================

nlp = spacy.load("en_core_web_sm")


# ============================================
# 2. ORIGINAL TEXT
# ============================================

text = """
Apple is a technology company.
Steve Jobs founded Apple.
Apple is headquartered in California.
The company was founded in 1976.
"""


print("Original Text:")
print(text)


# ============================================
# 3. TOKENIZATION USING spaCy
# ============================================

doc = nlp(text)

print("\nTokens:")

for token in doc:
    print(token.text)


# ============================================
# 4. POS TAGGING USING spaCy
# ============================================

print("\nPOS Tags:")

for token in doc:
    print(token.text, "->", token.pos_)


# ============================================
# 5. LEMMATIZATION USING spaCy
# ============================================

print("\nLemmatization:")

for token in doc:
    print(token.text, "->", token.lemma_)


# ============================================
# 6. STOPWORD CHECK USING spaCy
# ============================================

print("\nStopwords:")

for token in doc:

    if token.is_stop:
        print(token.text)


# ============================================
# 7. NAMED ENTITY RECOGNITION (NER)
# ============================================

print("\nNamed Entities:")

for ent in doc.ents:

    print(
        ent.text,
        "->",
        ent.label_
    )


# ============================================
# 8. NER - ENTITY EXPLANATION
# ============================================

print("\nEntity Explanation:")

for ent in doc.ents:

    print(
        ent.text,
        "->",
        ent.label_,
        "->",
        spacy.explain(ent.label_)
    )


# ============================================
# 9. NER WITH CONTEXT
# ============================================

texts = [

    "Amazon is expanding rapidly.",

    "The Amazon is the largest rainforest.",

    "Jordan won the MVP award.",

    "Jordan is a country in the Middle East."
]


print("\nContext-based NER:")

for text in texts:

    doc = nlp(text)

    print("\nSentence:", text)

    for ent in doc.ents:

        print(
            ent.text,
            "->",
            ent.label_
        )


# ============================================
# 10. WORD EMBEDDINGS
# ============================================
#
# Word embedding converts words into
# numerical vectors.
#
# Example:
#
# king  -> [0.7, 0.2, 0.1]
# queen -> [0.6, 0.3, 0.2]
#
# ============================================


# Simple manual vectors

king = np.array([0.7, 0.2, 0.1])

queen = np.array([0.6, 0.3, 0.2])

man = np.array([0.5, 0.1, 0.1])

woman = np.array([0.4, 0.2, 0.2])


print("\nWord Vectors:")

print("King:", king)

print("Queen:", queen)

print("Man:", man)

print("Woman:", woman)


# ============================================
# 11. COSINE SIMILARITY
# ============================================

king_2d = king.reshape(1, -1)

queen_2d = queen.reshape(1, -1)

similarity = cosine_similarity(
    king_2d,
    queen_2d
)[0][0]


print("\nCosine Similarity:")

print(
    "King vs Queen:",
    similarity
)


# ============================================
# 12. COSINE SIMILARITY MANUALLY
# ============================================
#
# Formula:
#
#             A . B
# cosine = -----------
#            |A||B|
#
# ============================================


dot_product = np.dot(king, queen)

magnitude_king = np.linalg.norm(king)

magnitude_queen = np.linalg.norm(queen)

cosine_value = (
    dot_product /
    (magnitude_king * magnitude_queen)
)


print("\nManual Cosine Similarity:")

print("Dot Product:", dot_product)

print("King Magnitude:", magnitude_king)

print("Queen Magnitude:", magnitude_queen)

print("Cosine Similarity:", cosine_value)


# ============================================
# 13. WORD2VEC
# ============================================

sentences = [

    ["king", "queen", "man", "woman"],

    ["king", "queen", "royal"],

    ["man", "woman", "person"],

    ["king", "man", "royal"],

    ["queen", "woman", "royal"]

]


# Train Word2Vec

word2vec_model = Word2Vec(

    sentences,

    vector_size=50,

    window=2,

    min_count=1,

    workers=1,

    sg=1

)


# ============================================
# 14. WORD2VEC VECTOR
# ============================================

print("\nWord2Vec Vector:")

print(
    word2vec_model.wv["king"]
)


# ============================================
# 15. WORD2VEC SIMILAR WORDS
# ============================================

print("\nWords Similar to King:")

print(
    word2vec_model.wv.most_similar(
        "king"
    )
)


# ============================================
# 16. WORD2VEC SIMILARITY
# ============================================

similarity = word2vec_model.wv.similarity(
    "king",
    "queen"
)


print("\nKing vs Queen Similarity:")

print(similarity)


# ============================================
# 17. FASTTEXT
# ============================================
#
# FastText uses subword / character
# n-grams.
#
# ============================================


fasttext_model = FastText(

    sentences,

    vector_size=50,

    window=2,

    min_count=1,

    workers=1

)


print("\nFastText Vector:")

print(
    fasttext_model.wv["king"]
)


# ============================================
# 18. FASTTEXT CAN HANDLE UNKNOWN WORDS
# ============================================

print("\nFastText Unknown Word:")

print(
    fasttext_model.wv["kingdom"]
)


# ============================================
# 19. WORD2VEC vs FASTTEXT
# ============================================

print("\nWord2Vec vs FastText:")

print(
    "Word2Vec -> word-level representation"
)

print(
    "FastText -> subword-level representation"
)


# ============================================
# 20. GLOVE
# ============================================
#
# GloVe uses global word co-occurrence.
#
# It is usually used through pre-trained
# GloVe vectors rather than training from
# scratch in a simple exam program.
#
# Conceptual representation:
#
# word -> dense vector
#
# ============================================


glove_vectors = {

    "king":
    np.array([0.42, -0.31, 0.15]),

    "queen":
    np.array([0.40, -0.29, 0.18])

}


print("\nGloVe Vectors:")

print("King:", glove_vectors["king"])

print("Queen:", glove_vectors["queen"])


# ============================================
# 21. GLOVE COSINE SIMILARITY
# ============================================

glove_similarity = cosine_similarity(

    glove_vectors["king"].reshape(1, -1),

    glove_vectors["queen"].reshape(1, -1)

)[0][0]


print("\nGloVe King vs Queen Similarity:")

print(glove_similarity)


# ============================================
# 22. SIMPLE RNN
# ============================================

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import SimpleRNN

from tensorflow.keras.layers import Dense


# RNN expects:
#
# samples × time steps × features


X = np.array([

    [
        [1],
        [2],
        [3]
    ],

    [
        [2],
        [3],
        [4]
    ],

    [
        [3],
        [4],
        [5]
    ]

])


y = np.array([

    [4],

    [5],

    [6]

])


rnn_model = Sequential([

    SimpleRNN(
        10,
        input_shape=(3, 1)
    ),

    Dense(1)

])


rnn_model.compile(

    optimizer="adam",

    loss="mse"

)


print("\nRNN Model:")

rnn_model.summary()


# ============================================
# 23. LSTM
# ============================================

from tensorflow.keras.layers import LSTM


lstm_model = Sequential([

    LSTM(
        10,
        input_shape=(3, 1)
    ),

    Dense(1)

])


lstm_model.compile(

    optimizer="adam",

    loss="mse"

)


print("\nLSTM Model:")

lstm_model.summary()


# ============================================
# 24. GRU
# ============================================

from tensorflow.keras.layers import GRU


gru_model = Sequential([

    GRU(
        10,
        input_shape=(3, 1)
    ),

    Dense(1)

])


gru_model.compile(

    optimizer="adam",

    loss="mse"

)


print("\nGRU Model:")

gru_model.summary()


# ============================================
# 25. SEQ2SEQ BASIC IDEA
# ============================================
#
# Encoder:
# Input sequence -> Context
#
# Decoder:
# Context -> Output sequence
#
# ============================================


print("\nSeq2Seq:")

print(
    "Input Sequence"
)

print(
    "      ↓"
)

print(
    "Encoder"
)

print(
    "      ↓"
)

print(
    "Context Vector"
)

print(
    "      ↓"
)

print(
    "Decoder"
)

print(
    "      ↓"
)

print(
    "Output Sequence"
)


# ============================================
# 26. ATTENTION CALCULATION
# ============================================
#
# Attention(Q,K,V)
#
# = softmax(QK^T / sqrt(d_k)) V
#
# ============================================


Q = np.array([

    [1, 0]

])


K = np.array([

    [1, 0],

    [0, 1]

])


V = np.array([

    [2, 3],

    [4, 5]

])


# --------------------------------------------
# Step 1: QK^T
# --------------------------------------------

scores = np.dot(Q, K.T)


print("\nAttention Step 1: QK^T")

print(scores)


# --------------------------------------------
# Step 2: Divide by sqrt(d_k)
# --------------------------------------------

d_k = K.shape[1]

scaled_scores = (
    scores /
    np.sqrt(d_k)
)


print("\nAttention Step 2: Scaled Scores")

print(scaled_scores)


# --------------------------------------------
# Step 3: Softmax
# --------------------------------------------

def softmax(x):

    exp_x = np.exp(
        x - np.max(x)
    )

    return exp_x / exp_x.sum(
        axis=-1,
        keepdims=True
    )


attention_weights = softmax(
    scaled_scores
)


print("\nAttention Step 3: Softmax")

print(attention_weights)


# --------------------------------------------
# Step 4: Multiply by V
# --------------------------------------------

attention_output = np.dot(

    attention_weights,

    V

)


print("\nAttention Step 4: Final Output")

print(attention_output)


# ============================================
# 27. COMPLETE ATTENTION FORMULA
# ============================================

print("\nAttention Formula:")

print(
    "Attention(Q,K,V)"
)

print(
    "= softmax(QK^T / sqrt(d_k)) V"
)


# ============================================
# 28. BERT / TRANSFORMER CONCEPT
# ============================================

print("\nTransformer:")

print(
    "Input Embedding"
)

print(
    "      ↓"
)

print(
    "Positional Encoding"
)

print(
    "      ↓"
)

print(
    "Multi-Head Self-Attention"
)

print(
    "      ↓"
)

print(
    "Feed Forward Network"
)

print(
    "      ↓"
)

print(
    "Add & Norm"
)

print(
    "      ↓"
)

print(
    "Output"
)


# ============================================
# 29. BERT
# ============================================

print("\nBERT:")

print(
    "Transformer Encoder"
)

print(
    "Mainly used for understanding text"
)

print(
    "Examples: NER, classification, QA"
)


# ============================================
# 30. GPT
# ============================================

print("\nGPT:")

print(
    "Transformer Decoder"
)

print(
    "Uses masked / causal self-attention"
)

print(
    "Predicts next token"
)


# ============================================
# 31. BART
# ============================================

print("\nBART:")

print(
    "Transformer Encoder + Decoder"
)

print(
    "Used for understanding + generation"
)

print(
    "Examples: summarization, translation"
)


# ============================================
# 32. NER COMPLETE PIPELINE
# ============================================

text = """

Barack Obama was born in Hawaii.
He worked at Google in California.
"""

doc = nlp(text)


print("\nNER Pipeline:")

print("Input")

print("  ↓")

print("Tokenization")

print("  ↓")

print("Contextual Representation")

print("  ↓")

print("Entity Classification")

print("  ↓")

print("Entity Grouping")

print("  ↓")

print("Final Entities")


print("\nDetected Entities:")

for ent in doc.ents:

    print(
        ent.text,
        "->",
        ent.label_
    )


# ============================================
# 33. IMPORTANT NER LABELS
# ============================================

print("\nImportant NER Labels:")

print("PERSON -> Person")

print("ORG -> Organization")

print("GPE -> Geopolitical Entity")

print("LOC -> Location")

print("DATE -> Date")

print("MONEY -> Monetary Value")

print("PERCENT -> Percentage")


# ============================================
# 34. FINAL SUMMARY
# ============================================

print("\n====================================")

print("UNIT 2 COMPLETE")

print("====================================")

print("""
Word2Vec  -> Prediction based
GloVe     -> Global co-occurrence
FastText  -> Subword information

RNN       -> Sequential processing
LSTM      -> Long-term memory
GRU       -> Simplified gated RNN

Seq2Seq   -> Encoder + Decoder
Attention -> Focus on important words

Transformer -> Attention-based architecture

BERT      -> Encoder -> Understanding
GPT       -> Decoder -> Generation
BART      -> Encoder + Decoder

NER       -> Identify entities

LLM       -> Large-scale language model
""")