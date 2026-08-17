import re
import spacy
input_test5 = "hello123 world456 python"
token6=re.findall(r'\w+',input_test5)
print(token6)