# ============================================================
# NON-LINEAR SUPPORT VECTOR MACHINE (SVM)
# ============================================================

# ============================================================
# STEP 1 : IMPORT LIBRARIES
# ============================================================

# pandas → used for handling dataset in table form
import pandas as pd

# numpy → used for numerical operations and arrays
import numpy as np


# ============================================================
# STEP 2 : READ THE DATASET
# ============================================================

# read_csv() loads CSV file into dataframe
data = pd.read_csv("fruits.csv")

# head() shows first 5 rows
print(data.head())


# ============================================================
# DATASET UNDERSTANDING
# ============================================================

# Weight  -> feature/input
# Size    -> feature/input
# Class   -> output/target

# Example:
# orange = 1
# apple  = 0

# Machine learning models cannot understand text labels,
# so we convert categorical values into numbers.


# ============================================================
# STEP 3 : LABEL ENCODING
# ============================================================

# LabelEncoder converts text labels into numbers
from sklearn.preprocessing import LabelEncoder

# create object of LabelEncoder
le = LabelEncoder()

# fit_transform():
# fit      -> learns unique classes
# transform-> converts classes into numbers
data.Class = le.fit_transform(data.Class)

# print encoded dataset
print(data.head())


# ============================================================
# AFTER ENCODING
# ============================================================

# apple  -> 0
# orange -> 1

# ML models work only with numerical values.


# ============================================================
# STEP 4 : SELECT FEATURES AND TARGET
# ============================================================

# X contains independent variables/features
# iloc[:,0:2]
# :      -> all rows
# 0:2    -> columns from index 0 to 1

# Features:
# Weight and Size
X = data.iloc[:, 0:2]

# y contains dependent variable/target/output
# Class column
y = data.Class


# ============================================================
# STEP 5 : IMPORT SVM MODELS
# ============================================================

# LinearSVC -> optimized linear SVM
# SVC       -> supports kernels like RBF and Polynomial
from sklearn.svm import LinearSVC, SVC


# ============================================================
# STEP 6 : LINEAR SVM
# ============================================================

# fit(X,y)
# X -> features
# y -> target

# LinearSVC creates linear decision boundary
lin_svc = LinearSVC().fit(X, y)

# ============================================================
# CONCEPT
# ============================================================

# Linear SVM:
# tries to separate classes using straight line/hyperplane

# Equation of hyperplane:
# w.x + b = 0

# Goal:
# maximize margin between classes


# ============================================================
# STEP 7 : SVC WITH LINEAR KERNEL
# ============================================================

# kernel='linear'
# creates linear boundary using SVC class

svc_lin = SVC(kernel='linear').fit(X, y)

# ============================================================
# CONCEPT
# ============================================================

# kernel:
# transforms data space

# linear kernel:
# used when data is linearly separable


# ============================================================
# STEP 8 : RBF KERNEL SVM
# ============================================================

# RBF = Radial Basis Function

# used for non-linear classification

# converts data into higher dimension
# so separation becomes easier

rbf_svc = SVC(kernel='rbf').fit(X, y)

# ============================================================
# CONCEPT
# ============================================================

# RBF kernel is most commonly used kernel

# works well when:
# classes are not separated using straight line


# ============================================================
# STEP 9 : POLYNOMIAL KERNEL (DEGREE 3)
# ============================================================

# polynomial kernel creates curved boundaries

# degree=3
# cubic polynomial transformation

poly_svc3 = SVC(kernel='poly', degree=3).fit(X, y)

# ============================================================
# CONCEPT
# ============================================================

# polynomial kernel formula:
# (x.y + c)^d

# d = degree

# higher degree -> more complex boundary


# ============================================================
# STEP 10 : POLYNOMIAL KERNEL (DEGREE 4)
# ============================================================

poly_svc4 = SVC(kernel='poly', degree=4).fit(X, y)

# degree 4 creates even more flexible boundary


# ============================================================
# STEP 11 : MODEL ACCURACY SCORES
# ============================================================

# score(X,y)
# calculates accuracy

# formula:
# accuracy = correct predictions / total predictions

print("Linear SVC Score:", lin_svc.score(X, y))

print("SVC Linear Score:", svc_lin.score(X, y))

print("RBF SVC Score:", rbf_svc.score(X, y))

print("3 Degree Polynomial SVC Score:",
      poly_svc3.score(X, y))

print("4 Degree Polynomial SVC Score:",
      poly_svc4.score(X, y))


# ============================================================
# OUTPUT UNDERSTANDING
# ============================================================

# Linear SVC Score: 0.9
# SVC Linear Score: 1.0
# RBF SVC Score: 0.975
# Polynomial Scores: 0.925

# Higher score -> better training accuracy

# But:
# extremely high accuracy may also mean overfitting


# ============================================================
# STEP 12 : PLOT DECISION BOUNDARIES
# ============================================================

# plot_decision_regions()
# visualizes classification regions

from mlxtend.plotting import plot_decision_regions


# ============================================================
# LINEAR SVC BOUNDARY
# ============================================================

plot_decision_regions(
    np.array(X),      # convert dataframe into numpy array
    y.values,         # convert target into array
    lin_svc           # trained model
)

# ============================================================
# GRAPH UNDERSTANDING
# ============================================================

# orange region -> one class
# blue region   -> another class

# line between them -> decision boundary

# SVM tries to maximize distance from nearest points


# ============================================================
# PLOT : LINEAR KERNEL SVC
# ============================================================

plot_decision_regions(
    np.array(X),
    y.values,
    svc_lin
)


# ============================================================
# PLOT : RBF KERNEL
# ============================================================

plot_decision_regions(
    np.array(X),
    y.values,
    rbf_svc
)

# ============================================================
# CONCEPT
# ============================================================

# RBF creates curved/non-linear boundaries

# useful for complex datasets


# ============================================================
# PLOT : POLYNOMIAL DEGREE 3
# ============================================================

plot_decision_regions(
    np.array(X),
    y.values,
    poly_svc3
)


# ============================================================
# PLOT : POLYNOMIAL DEGREE 4
# ============================================================

plot_decision_regions(
    np.array(X),
    y.values,
    poly_svc4
)


# ============================================================
# WARNING EXPLANATION
# ============================================================

# UserWarning:
# X does not have valid feature names

# This warning occurs because:
# model was trained using dataframe column names
# but plotting uses numpy arrays

# This is not an error.
# Program still works correctly.


# ============================================================
# COMPLETE SVM CONCEPT SUMMARY
# ============================================================

# SVM:
# finds best hyperplane

# Hyperplane:
# decision boundary

# Margin:
# distance between nearest points and boundary

# Support vectors:
# nearest data points affecting boundary

# Kernels:
# used for non-linear separation

# Linear Kernel:
# straight line separation

# RBF Kernel:
# non-linear flexible separation

# Polynomial Kernel:
# curved boundary using polynomial transformation


# ============================================================
# IMPORTANT EXAM POINTS
# ============================================================

# 1. SVM is mainly used for classification.
# 2. Goal of SVM is maximizing margin.
# 3. Support vectors define the hyperplane.
# 4. RBF is most popular kernel.
# 5. Kernels help solve non-linear problems.
# 6. High degree polynomial may cause overfitting.
# 7. SVM performs well in high-dimensional data.