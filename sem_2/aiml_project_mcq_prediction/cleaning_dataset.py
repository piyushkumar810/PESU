import pandas as pd
import string
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# LOAD DATASET
df = pd.read_excel(r"C:/ai_ml_project/squad_dataset.xlsx")

print("\n================ FIRST 5 ROWS ================\n")
print(df.head())

print("\n================ DATASET SHAPE ================\n")
print(df.shape)

print("\n================ COLUMN NAMES ================\n")
print(df.columns)


# CHECK NULL VALUES
print("\n================ NULL VALUES ================\n")
print(df.isnull().sum())


# REMOVE NULL VALUES
df = df.dropna()


# CHECK DUPLICATES
print("\n================ DUPLICATES ================\n")
print(df.duplicated().sum())


# REMOVE DUPLICATES
df = df.drop_duplicates()


# TEXT CLEANING
# convert to lowercase
df['context'] = df['context'].astype(str).str.lower()


# remove punctuation
df['context'] = df['context'].str.replace(
    f"[{string.punctuation}]",
    "",
    regex=True
)


# remove extra spaces
df['context'] = df['context'].str.strip()


# CREATE CUSTOM TOPIC LABELS
def assign_topic(text):

    text = str(text).lower()

    # Supervised Learning
    if (
        "regression" in text or
        "classification" in text or
        "label" in text or
        "training data" in text
    ):
        return "Supervised Learning"

    # Unsupervised Learning
    elif (
        "clustering" in text or
        "k means" in text or
        "grouping" in text
    ):
        return "Unsupervised Learning"

    # Reinforcement Learning
    elif (
        "reward" in text or
        "agent" in text or
        "q learning" in text
    ):
        return "Reinforcement Learning"

    # Deep Learning
    elif (
        "neural network" in text or
        "deep learning" in text or
        "cnn" in text or
        "rnn" in text
    ):
        return "Deep Learning"

    else:
        return "General AI"


# apply topic generation
df['topic'] = df['context'].apply(assign_topic)


# DISPLAY CLEANED DATASET
print("\n================ CLEANED DATASET ================\n")
print(df[['context', 'topic']].head())


# LABEL ENCODING
encoder = LabelEncoder()
df['topic_encoded'] = encoder.fit_transform(df['topic'])


# FEATURE EXTRACTION USING TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['context'])


# TARGET VARIABLE
y = df['topic_encoded']


# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TRAIN MODEL
model = MultinomialNB()
model.fit(X_train, y_train)


# PREDICTION
prediction = model.predict(X_test)


# ACCURACY
accuracy = accuracy_score(y_test, prediction)
print("\n================ MODEL ACCURACY ================\n")
print(f"Accuracy : {accuracy:.2f}")


# CONFUSION MATRIX
print("\n================ CONFUSION MATRIX ================\n")
print(confusion_matrix(y_test, prediction))


# CLASSIFICATION REPORT
print("\n================ CLASSIFICATION REPORT ================\n")
print(classification_report(y_test, prediction))


# SAVE CLEANED DATASET
df.to_csv(
    r"C:/ai_ml_project/cleaned_dataset.csv",
    index=False
)

print("\nCLEANED DATASET SAVED")


# SAVE MODEL
pickle.dump(
    model,
    open(r"C:/ai_ml_project/model.pkl", "wb")
)

print("MODEL SAVED")


# SAVE TF-IDF VECTORIZER
pickle.dump(
    tfidf,
    open(r"C:/ai_ml_project/vectorizer.pkl", "wb")
)

print("TF-IDF VECTORIZER SAVED")


# SAVE LABEL ENCODER
pickle.dump(
    encoder,
    open(r"C:/ai_ml_project/encoder.pkl", "wb")
)

print("LABEL ENCODER SAVED")


# TEST SAMPLE INPUT
sample_text = [
    "K means clustering groups similar data points"
]

sample_vector = tfidf.transform(sample_text)

predicted_label = model.predict(sample_vector)

predicted_topic = encoder.inverse_transform(predicted_label)

print("\n================ SAMPLE PREDICTION ================\n")

print("INPUT TEXT :")
print(sample_text[0])

print("\nPREDICTED TOPIC :")
print(predicted_topic[0])