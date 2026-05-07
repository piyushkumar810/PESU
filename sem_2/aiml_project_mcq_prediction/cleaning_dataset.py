# import pandas as pd
# import string
# import pickle

# from sklearn.preprocessing import LabelEncoder
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix


# # LOAD DATASET
# df = pd.read_excel(r"C:/ai_ml_project/squad_dataset.xlsx")

# print("\nFIRST 5 ROWS OF DATASET")
# print(df.head())

# print("\nDATASET SHAPE")
# print(df.shape)

# print("\nCOLUMN NAMES")
# print(df.columns)


# # CHECK NULL VALUES
# print("\nNULL VALUES")
# print(df.isnull().sum())


# # REMOVE NULL VALUES
# df = df.dropna()


# # CHECK DUPLICATES
# print("\nDUPLICATE ROWS")
# print(df.duplicated().sum())


# # REMOVE DUPLICATES
# df = df.drop_duplicates()


# # LOWERCASE CONVERSION
# df['context'] = df['context'].astype(str).str.lower()
# df['question'] = df['question'].astype(str).str.lower()


# # REMOVE PUNCTUATION
# df['context'] = df['context'].str.replace(
#     f"[{string.punctuation}]",
#     "",
#     regex=True
# )

# df['question'] = df['question'].str.replace(
#     f"[{string.punctuation}]",
#     "",
#     regex=True
# )


# # REMOVE EXTRA SPACES
# df['context'] = df['context'].str.strip()
# df['question'] = df['question'].str.strip()


# # CREATE CUSTOM TOPIC LABELS
# def assign_topic(text):

#     text = str(text).lower()

#     if "regression" in text or "classification" in text:
#         return "Supervised Learning"

#     elif "clustering" in text or "k means" in text:
#         return "Unsupervised Learning"

#     elif "reward" in text or "q learning" in text:
#         return "Reinforcement Learning"

#     elif "neural network" in text or "deep learning" in text:
#         return "Deep Learning"

#     else:
#         return "General AI"


# df['topic'] = df['context'].apply(assign_topic)


# # DISPLAY SAMPLE TOPICS
# print("\nCONTEXT + GENERATED TOPICS")
# print(df[['context', 'topic']].head())


# # LABEL ENCODING
# encoder = LabelEncoder()

# df['topic_encoded'] = encoder.fit_transform(df['topic'])


# # FEATURE EXTRACTION USING TF-IDF
# tfidf = TfidfVectorizer()

# X = tfidf.fit_transform(df['context'])


# # TARGET VARIABLE
# y = df['topic_encoded']


# # TRAIN TEST SPLIT
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )


# # TRAIN MODEL
# model = MultinomialNB()

# model.fit(X_train, y_train)


# # PREDICTION
# prediction = model.predict(X_test)


# # ACCURACY
# accuracy = accuracy_score(y_test, prediction)

# print("\nMODEL ACCURACY")
# print(accuracy)


# # CONFUSION MATRIX
# print("\nCONFUSION MATRIX")
# print(confusion_matrix(y_test, prediction))


# # SAVE CLEANED DATASET
# df.to_csv(
#     r"C:/ai_ml_project/cleaned_dataset.csv",
#     index=False
# )

# print("\nCLEANED DATASET SAVED")


# # SAVE TRAINED MODEL
# pickle.dump(
#     model,
#     open(r"C:/ai_ml_project/model.pkl", "wb")
# )

# print("MODEL SAVED")


# # SAVE TF-IDF VECTORIZER
# pickle.dump(
#     tfidf,
#     open(r"C:/ai_ml_project/vectorizer.pkl", "wb")
# )

# print("TF-IDF VECTORIZER SAVED")


# # SAVE LABEL ENCODER
# pickle.dump(
#     encoder,
#     open(r"C:/ai_ml_project/encoder.pkl", "wb")
# )

# print("LABEL ENCODER SAVED")


# # TEST CUSTOM INPUT
# sample_text = [
#     "K means clustering groups similar data points"
# ]

# sample_vector = tfidf.transform(sample_text)

# predicted_label = model.predict(sample_vector)

# predicted_topic = encoder.inverse_transform(predicted_label)

# print("\nSAMPLE PREDICTION")
# print("INPUT :", sample_text[0])
# print("PREDICTED TOPIC :", predicted_topic[0])






import pandas as pd
import string
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_excel(r"C:/ai_ml_project/squad_dataset.xlsx")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)


# =========================================================
# CHECK NULL VALUES
# =========================================================

print("\nNULL VALUES")
print(df.isnull().sum())


# =========================================================
# REMOVE NULL VALUES
# =========================================================

df = df.dropna()


# =========================================================
# CHECK DUPLICATES
# =========================================================

print("\nDUPLICATES")
print(df.duplicated().sum())


# =========================================================
# REMOVE DUPLICATES
# =========================================================

df = df.drop_duplicates()


# =========================================================
# CONVERT TO LOWERCASE
# =========================================================

df['context'] = df['context'].astype(str).str.lower()
df['question'] = df['question'].astype(str).str.lower()


# =========================================================
# REMOVE PUNCTUATION
# =========================================================

df['context'] = df['context'].str.replace(
    f"[{string.punctuation}]",
    "",
    regex=True
)

df['question'] = df['question'].str.replace(
    f"[{string.punctuation}]",
    "",
    regex=True
)


# =========================================================
# REMOVE EXTRA SPACES
# =========================================================

df['context'] = df['context'].str.strip()
df['question'] = df['question'].str.strip()


# =========================================================
# DISPLAY CLEANED DATA
# =========================================================

print("\nCLEANED DATASET")
print(df[['context', 'question']].head())


# =========================================================
# FEATURE EXTRACTION USING TF-IDF
# =========================================================

tfidf = TfidfVectorizer(max_features=5000)

X = tfidf.fit_transform(df['context'])


# =========================================================
# TARGET VARIABLE
# =========================================================

y = df['question']


# =========================================================
# TRAIN TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================================================
# TRAIN MODEL
# =========================================================

model = MultinomialNB()

model.fit(X_train, y_train)


# =========================================================
# PREDICTION
# =========================================================

prediction = model.predict(X_test)


# =========================================================
# ACCURACY
# =========================================================

accuracy = accuracy_score(y_test, prediction)

print("\nMODEL ACCURACY")
print(accuracy)


# =========================================================
# CONFUSION MATRIX
# =========================================================

print("\nCONFUSION MATRIX")

print(confusion_matrix(
    y_test[:20],
    prediction[:20]
))


# =========================================================
# SAVE CLEANED DATASET
# =========================================================

df.to_csv(
    r"C:/ai_ml_project/cleaned_dataset.csv",
    index=False
)

print("\nCLEANED DATASET SAVED")


# =========================================================
# SAVE MODEL
# =========================================================

pickle.dump(
    model,
    open(r"C:/ai_ml_project/model.pkl", "wb")
)

print("MODEL SAVED")


# =========================================================
# SAVE TF-IDF VECTORIZER
# =========================================================

pickle.dump(
    tfidf,
    open(r"C:/ai_ml_project/vectorizer.pkl", "wb")
)

print("TF-IDF VECTORIZER SAVED")


# =========================================================
# TEST SAMPLE INPUT
# =========================================================

sample_text = [
    "machine learning is a branch of artificial intelligence"
]

sample_vector = tfidf.transform(sample_text)

predicted_question = model.predict(sample_vector)

print("\nSAMPLE PREDICTION")
print("INPUT :", sample_text[0])
print("GENERATED QUESTION :", predicted_question[0])