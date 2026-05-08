# ============================================================
# SUPPORT VECTOR MACHINE (SVM) USING LinearSVC
# ============================================================
# Goal:
# We are building a Machine Learning model that classifies
# fruits based on:
#   1. Weight
#   2. Size
#
# The model will learn patterns and predict the fruit class.
# ============================================================



# =========================
# IMPORTING LIBRARIES
# =========================

# pandas -> used for handling datasets (CSV files, tables)
import pandas as pd

# LabelEncoder -> converts categorical text labels into numbers
# Example:
# Apple -> 0
# Orange -> 1
from sklearn.preprocessing import LabelEncoder

# train_test_split -> divides dataset into training and testing data
from sklearn.model_selection import train_test_split

# LinearSVC -> Support Vector Machine classifier
from sklearn.svm import LinearSVC

# warnings -> used to ignore unnecessary warning messages
import warnings

# classification_report -> gives precision, recall, f1-score
# confusion_matrix -> shows prediction performance
from sklearn.metrics import classification_report, confusion_matrix

# plot_decision_regions -> plots SVM decision boundaries
from mlxtend.plotting import plot_decision_regions

# numpy -> numerical operations
import numpy as np

# matplotlib -> plotting graphs
import matplotlib.pyplot as plt



# ============================================================
# LOADING THE DATASET
# ============================================================

# read_csv() loads CSV file into dataframe

df = pd.read_csv(
    r"C:\Users\piyush kumar\OneDrive\Desktop\GitHub\PESU\sem_2\ai_ml\unit3\1st_fruit_data.csv"
)



# ============================================================
# BASIC DATA ANALYSIS
# ============================================================

# shape gives:
# (number_of_rows, number_of_columns)

print("Dataset Shape =", df.shape)



# head() prints first 5 rows of dataset
print("\nFirst 5 Rows:\n")
print(df.head())



# isnull().sum() checks missing values in each column
print("\nMissing Values:\n")
print(df.isnull().sum())



# ============================================================
# HANDLING CATEGORICAL DATA
# ============================================================

# Machine Learning models cannot understand text labels directly
# Example:
# Apple, Orange, Banana
#
# So we convert them into numbers.

le = LabelEncoder()

# Transforming 'Class' column
# Example:
# Apple  -> 0
# Orange -> 1

df["Class"] = le.fit_transform(df["Class"])



# Printing transformed dataset
print("\nDataset After Encoding:\n")
print(df.head())



# ============================================================
# SELECTING INPUT FEATURES AND OUTPUT LABEL
# ============================================================

# x = input features
# These are independent variables

x = df[["Weight", "Size"]]



# y = target/output column
# This is dependent variable

y = df["Class"]



# ============================================================
# SPLITTING DATASET
# ============================================================

# train_test_split divides data into:
#
# Training Data  -> used to train model
# Testing Data   -> used to test model
#
# test_size=0.2 means:
# 20% testing data
# 80% training data

xtrain, xtest, ytrain, ytest = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)



# ============================================================
# BUILDING THE SVM MODEL
# ============================================================

# Ignore warning messages
warnings.simplefilter("ignore")



# Creating Linear SVM classifier
classifier = LinearSVC()



# Training the model using training data
classifier.fit(xtrain, ytrain)



# ============================================================
# MODEL ACCURACY
# ============================================================

# score() gives accuracy
#
# Training Accuracy:
# Accuracy on data used for training
#
# Testing Accuracy:
# Accuracy on unseen data

print("\nTraining Accuracy =",
      classifier.score(xtrain, ytrain))

print("Testing Accuracy =",
      classifier.score(xtest, ytest))



# ============================================================
# MAKING PREDICTIONS
# ============================================================

# predict() predicts output for testing data

ypred = classifier.predict(xtest)



# ============================================================
# CONFUSION MATRIX
# ============================================================

# Confusion Matrix tells:
#
# Correct Predictions
# Wrong Predictions
#
# Format:
#
#                Predicted
#              0         1
#
# Actual 0   TP        FN
# Actual 1   FP        TN

print("\nConfusion Matrix:\n")
print(confusion_matrix(ytest, ypred))



# ============================================================
# CLASSIFICATION REPORT
# ============================================================

# Gives:
#
# Precision -> correctness of positive predictions
# Recall    -> ability to find all positives
# F1-score  -> balance between precision and recall
# Support   -> number of actual samples

print("\nClassification Report:\n")
print(classification_report(ytest, ypred))



# ============================================================
# DECISION REGION PLOT
# ============================================================

# plot_decision_regions() visualizes:
#
# 1. Decision Boundary
# 2. Different Classes
# 3. How SVM separates classes

plot_decision_regions(
    x.values,
    np.array(y),
    clf=classifier,
    legend=2
)



# Graph title
plt.title("SVM Decision Region Boundary", size=16)



# Showing graph
plt.show()



# ============================================================
# IMPORTANT THEORY NOTES
# ============================================================

# 1. SVM (Support Vector Machine)
# --------------------------------
# SVM is a supervised machine learning algorithm used for:
#   - Classification
#   - Regression
#
# Main goal:
# Find the best boundary (hyperplane)
# that separates classes.



# 2. Hyperplane
# --------------------------------
# A line separating classes in 2D
# A plane in higher dimensions



# 3. Support Vectors
# --------------------------------
# Data points nearest to boundary
# They are very important because:
# They decide the position of hyperplane.



# 4. Margin
# --------------------------------
# Distance between hyperplane and nearest data points.
#
# SVM tries to maximize margin.



# 5. LinearSVC
# --------------------------------
# Used when data is approximately linearly separable.



# 6. Overfitting Condition
# --------------------------------
# If training accuracy is high
# but testing accuracy is low,
# model is overfitting.



# ============================================================
# GATE / EXAM IMPORTANT POINTS
# ============================================================

# 1. SVM is supervised learning algorithm.
#
# 2. SVM tries to maximize margin.
#
# 3. Support vectors are nearest points to hyperplane.
#
# 4. LinearSVC is used for linear classification.
#
# 5. Kernel trick is used for non-linear data.
#
# 6. Hyperplane dimension:
#       n-dimensional data -> (n-1)-dimensional hyperplane
#
# 7. Large margin => better generalization.
#
# 8. SVM works well in high-dimensional spaces.
#
# 9. LinearSVC is faster than SVC(kernel='linear')
#
# 10. SVM is sensitive to feature scaling.
#     Standardization is usually recommended.
#
# ============================================================