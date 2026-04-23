# ============================================
# STEP 1: IMPORT LIBRARIES
# ============================================

import pandas as pd                      # For data handling
import numpy as np                       # For numerical operations

# Preprocessing tools
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Train-test split
from sklearn.model_selection import train_test_split

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

# Multiclass strategies
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier

# Evaluation metrics
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# ============================================
# STEP 2: LOAD DATASET
# ============================================

# Load your uploaded CSV file
df = pd.read_csv(r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\multi_clissification.csv")

# Display first 5 rows
print("First 5 rows:\n", df.head())

# Shape of dataset (rows, columns)
print("\nDataset Shape:", df.shape)


# ============================================
# STEP 3: CHECK MISSING VALUES
# ============================================

# Count missing values in each column
print("\nMissing Values:\n", df.isna().sum())

# (In your PDF → No missing values)


# ============================================
# STEP 4: LABEL ENCODING (Gender → Numeric)
# ============================================

# Convert categorical column to numeric
le = LabelEncoder()

# Male → 1, Female → 0 (auto assigned)
df['Gender'] = le.fit_transform(df['Gender'])

print("\nAfter Label Encoding:\n", df.head())


# ============================================
# STEP 5: FEATURE SCALING
# ============================================

# Scaling makes values between 0 and 1
mm = MinMaxScaler()

# Apply scaling to Height and Weight
df['Height'] = mm.fit_transform(df[['Height']])
df['Weight'] = mm.fit_transform(df[['Weight']])

print("\nAfter Scaling:\n", df.head())


# ============================================
# STEP 6: SPLIT DATA (X and Y)
# ============================================

# Features (independent variables)
X = df.iloc[:, 0:3]

# Target (dependent variable)
y = df.iloc[:, 3]

# Train-test split (80% train, 20% test)
xtrain, xtest, ytrain, ytest = train_test_split(
    X, y,
    test_size=0.2,
    random_state=1,
    shuffle=True
)

print("\nTrain-Test Split Done")


# ============================================
# STEP 7: LOGISTIC REGRESSION MODEL
# ============================================

LR = LogisticRegression(max_iter=1000)

# Train model
LR.fit(xtrain, ytrain)

# Model parameters
print("\nLogistic Regression Coefficients:\n", LR.coef_)
print("Intercept:\n", LR.intercept_)
print("Classes:\n", LR.classes_)


# ============================================
# STEP 8: EVALUATION (LOGISTIC REGRESSION)
# ============================================

# Predictions
ypred = LR.predict(xtest)

# Confusion Matrix
print("\nConfusion Matrix:\n", confusion_matrix(ytest, ypred))

# Accuracy
print("Accuracy:", accuracy_score(ytest, ypred))

# Precision
print("Precision:", precision_score(ytest, ypred, average='weighted'))

# Recall
print("Recall:", recall_score(ytest, ypred, average='weighted'))

# F1 Score
print("F1 Score:", f1_score(ytest, ypred, average='weighted'))

# ROC-AUC (for multiclass)
yprob = LR.predict_proba(xtest)
print("AUC Score:", roc_auc_score(ytest, yprob, multi_class='ovr'))


# ============================================
# STEP 9: NAIVE BAYES MODEL
# ============================================

gnb = GaussianNB()

# Train model
gnb.fit(xtrain, ytrain)

# Predictions
ypred_nb = gnb.predict(xtest)

print("\nNaive Bayes Confusion Matrix:\n", confusion_matrix(ytest, ypred_nb))
print("Accuracy:", accuracy_score(ytest, ypred_nb))


# ============================================
# STEP 10: ONE VS REST (OvR)
# ============================================

ovr_model = OneVsRestClassifier(LogisticRegression(max_iter=1000))

# Train
ovr_model.fit(xtrain, ytrain)

# Predict
y_pred_ovr = ovr_model.predict(xtest)

print("\nOvR Results:")
print("Confusion Matrix:\n", confusion_matrix(ytest, y_pred_ovr))
print("Accuracy:", accuracy_score(ytest, y_pred_ovr))
print("Precision:", precision_score(ytest, y_pred_ovr, average='weighted'))
print("Recall:", recall_score(ytest, y_pred_ovr, average='weighted'))
print("F1 Score:", f1_score(ytest, y_pred_ovr, average='weighted'))


# ============================================
# STEP 11: ONE VS ONE (OvO)
# ============================================

ovo_model = OneVsOneClassifier(LogisticRegression(max_iter=1000))

# Train
ovo_model.fit(xtrain, ytrain)

# Predict
y_pred_ovo = ovo_model.predict(xtest)

print("\nOvO Results:")
print("Confusion Matrix:\n", confusion_matrix(ytest, y_pred_ovo))
print("Accuracy:", accuracy_score(ytest, y_pred_ovo))
print("Precision:", precision_score(ytest, y_pred_ovo, average='weighted'))
print("Recall:", recall_score(ytest, y_pred_ovo, average='weighted'))
print("F1 Score:", f1_score(ytest, y_pred_ovo, average='weighted'))


# ============================================
# STEP 12: NUMBER OF CLASSIFIERS
# ============================================

n_classes = len(y.unique())

print("\nNumber of Classes:", n_classes)

# OvR → K models
print("OvR Classifiers:", n_classes)

# OvO → K(K-1)/2 models
print("OvO Classifiers:", n_classes * (n_classes - 1) // 2)


# ============================================
# END OF COMPLETE PIPELINE
# ============================================