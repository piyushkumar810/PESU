# ---------------- basic Tocknization
# Import the spaCy library
import spacy

# Create a blank English NLP pipeline
nlp = spacy.blank("en")

# Pass the given text to spaCy for processing
# spaCy converts the text into a Doc object containing individual tokens
doc = nlp("Dr. strange loves pav bhaji of mumbai as it costs 2$ per plate")

# Loop through each token in the Doc object
for token in doc:
    # Print each token separately
    print(token)

# -------------------- Accessing Tokens by index
# first token
print(doc[0])

# last token
print(doc[-1])

# display 1 to 4
print(doc[1:5])

doc=nlp('''"Let's go to N.Y.!"''')
for tok in doc:
    print(tok)

print("Total number of tokens:", len(doc))

for token in doc:
    print(token.text,"| is_alpha:",token.is_alpha, "| is_digit:",token.is_digit,"| is_punct:",token.is_punct)