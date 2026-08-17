import re
import spacy
nlp=spacy.blank("en")

email="virat@kholi.com"

token=re.findall(r'\w+|@|\.', email)
print(token)

input_test="abc123def456"
print(input_test)

token1=re.findall(r'[A-Za-z]+|\d+', input_test)
print(token1)

token2=''.join(re.findall(r'[A-Za-z]'))