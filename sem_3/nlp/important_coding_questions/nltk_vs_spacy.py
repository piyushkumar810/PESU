# ============================================================
#              NLTK vs spaCy - BEST EXAM NOTES
# ============================================================


# ============================================================
# 1. NLTK
# ============================================================

"""
NLTK = Natural Language Toolkit

MAIN IDEA:
    NLTK provides individual NLP tools.
    It is very useful for learning, teaching,
    experimentation and research.

THINK:
    NLTK = TOOLBOX

You usually choose the specific tool you need.
"""


# ============================================================
# 2. spaCy
# ============================================================

"""
spaCy is a modern NLP library designed for
fast, practical and production-oriented NLP.

MAIN IDEA:
    spaCy provides a complete NLP pipeline
    using pre-trained language models.

THINK:
    spaCy = READY-MADE NLP SYSTEM
"""


# ============================================================
# 3. MAIN DIFFERENCE
# ============================================================

"""
                    NLTK              spaCy
                    ----              -----
Purpose          Learning/          Practical/
                 experimentation    production NLP

Approach         Individual         Complete
                 NLP tools          NLP pipeline

Speed            Generally slower   Generally faster

Models           Uses separate      Strong pre-trained
                 resources          language models

Stemming         YES                NO built-in
                                   stemming focus

Lemmatization    YES                YES

Tokenization     YES                YES

POS Tagging      YES                YES

Stopwords        YES                YES

NER              YES                YES

Dependency       Basic/available    Strong
Parsing

Best remembered:
    NLTK  -> Individual NLP tools
    spaCy -> Complete NLP pipeline
"""


# ============================================================
# 4. NLTK CODING STYLE
# ============================================================

"""
In NLTK, you generally import and use
the specific tool you need.
"""


# -------------------------
# Tokenization - NLTK
# -------------------------

from nltk.tokenize import word_tokenize

text = "Students are learning NLP."

tokens = word_tokenize(text)

print(tokens)


# -------------------------
# Stemming - NLTK
# -------------------------

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

print(stemmer.stem("playing"))
# Output: play


# -------------------------
# Lemmatization - NLTK
# -------------------------

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cars"))
# Output: car


# -------------------------
# POS Tagging - NLTK
# -------------------------

from nltk import pos_tag

tokens = word_tokenize(text)

print(pos_tag(tokens))


# -------------------------
# Stopwords - NLTK
# -------------------------

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

words = word_tokenize(text)

filtered = [
    word for word in words
    if word.lower() not in stop_words
]

print(filtered)


# ============================================================
# 5. spaCy CODING STYLE
# ============================================================

"""
In spaCy, you normally load a language model,
process the text once, and then access many
NLP features from each token.
"""


import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Process text
doc = nlp("Students are learning NLP.")


# -------------------------
# Tokenization - spaCy
# -------------------------

for token in doc:
    print(token.text)


# -------------------------
# Lemmatization - spaCy
# -------------------------

for token in doc:
    print(token.text, "->", token.lemma_)


# -------------------------
# POS Tagging - spaCy
# -------------------------

for token in doc:
    print(token.text, "->", token.pos_)


# -------------------------
# Stopword Checking - spaCy
# -------------------------

for token in doc:
    print(token.text, "->", token.is_stop)


# -------------------------
# Named Entity Recognition
# -------------------------

for entity in doc.ents:
    print(entity.text, "->", entity.label_)


# -------------------------
# Dependency Parsing
# -------------------------

for token in doc:
    print(token.text, "->", token.dep_)


# ============================================================
# 6. VERY IMPORTANT CODING DIFFERENCE
# ============================================================

"""
NLTK:

    text
     |
     +--> word_tokenize()
     |
     +--> PorterStemmer()
     |
     +--> WordNetLemmatizer()
     |
     +--> pos_tag()
     |
     +--> stopwords()


spaCy:

    text
     |
     v
    nlp(text)
     |
     v
    doc
     |
     +--> token.text
     +--> token.lemma_
     +--> token.pos_
     +--> token.is_stop
     +--> token.ent_type_
     +--> token.dep_
"""


# ============================================================
# 7. SAME TASK - NLTK vs spaCy
# ============================================================

"""
TOKENIZATION

NLTK:
    tokens = word_tokenize(text)

spaCy:
    doc = nlp(text)
    tokens = [token.text for token in doc]
"""


"""
LEMMATIZATION

NLTK:
    lemmatizer = WordNetLemmatizer()
    lemma = lemmatizer.lemmatize(word)

spaCy:
    doc = nlp(text)
    lemma = token.lemma_
"""


"""
POS TAGGING

NLTK:
    pos_tag(tokens)

spaCy:
    token.pos_
"""


"""
STOPWORD CHECK

NLTK:
    word not in stop_words

spaCy:
    not token.is_stop
"""


# ============================================================
# 8. BoW AND TF-IDF
# ============================================================

"""
BoW and TF-IDF are generally handled using
scikit-learn, not as the main difference
between NLTK and spaCy.

BoW:
    from sklearn.feature_extraction.text import CountVectorizer

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(documents)


TF-IDF:
    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
"""


# ============================================================
# 9. EASY MEMORY TRICK
# ============================================================

"""
             NLTK vs spaCy

NLTK
  |
  +--> Individual tools
  +--> Learning
  +--> Experimentation
  +--> Stemming available
  +--> word_tokenize()
  +--> PorterStemmer()
  +--> WordNetLemmatizer()
  +--> pos_tag()


spaCy
  |
  +--> Complete pipeline
  +--> Practical / production NLP
  +--> Fast processing
  +--> Pre-trained models
  +--> nlp(text)
  +--> token.lemma_
  +--> token.pos_
  +--> token.is_stop
  +--> token.ent_type_
  +--> token.dep_


MEMORY:
    NLTK  = TOOLBOX
    spaCy = READY-MADE NLP SYSTEM
"""


# ============================================================
# 10. EXAM GOLDEN POINTS
# ============================================================

"""
1. NLTK stands for Natural Language Toolkit.

2. NLTK is commonly used for learning, teaching,
   experimentation and research.

3. spaCy is designed for fast, practical and
   production-oriented NLP.

4. NLTK provides many individual NLP tools.

5. spaCy provides a complete NLP pipeline.

6. NLTK has PorterStemmer for stemming.

7. spaCy does not focus on stemming; lemmatization
   is provided through its NLP pipeline.

8. Both NLTK and spaCy support:
       - Tokenization
       - Lemmatization
       - POS tagging
       - Stopword handling
       - NER

9. spaCy uses:
       nlp = spacy.load("en_core_web_sm")
       doc = nlp(text)

10. In spaCy, many features can be accessed from
    the same Doc/Token objects.

11. BoW is commonly implemented using:
       CountVectorizer()

12. TF-IDF is commonly implemented using:
       TfidfVectorizer()


FINAL ONE-LINE DIFFERENCE:

    NLTK  -> Individual NLP tools for learning/
             experimentation.

    spaCy -> Fast, ready-made NLP pipeline for
             practical/production NLP.
"""