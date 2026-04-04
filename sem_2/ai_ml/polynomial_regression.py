# ✅ POLYNOMIAL REGRESSION (FULL BEGINNER EXPLANATION)

# -------------------------------

# 🧠 WHAT IS sklearn?

# -------------------------------

# sklearn (Scikit-learn) = Python library used for Machine Learning

# It gives ready-made tools like:

# - Linear Regression

# - Polynomial Features

# - Train-test splitting

# - Evaluation metrics

# Think:

# sklearn = toolbox for ML

# -------------------------------

# STEP 1: IMPORT LIBRARIES

# -------------------------------

import numpy as np   # used for math operations (like sqrt)
import pandas as pd  # used to handle data in table form

# model_selection = module in sklearn used for splitting data
from sklearn.model_selection import train_test_split

# preprocessing = module used for transforming data
from sklearn.preprocessing import PolynomialFeatures

# linear_model = module that contains Linear Regression algorithm
from sklearn.linear_model import LinearRegression

# metrics = module used to evaluate model performance
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------                                                                                                                

# STEP 2: CREATE DATASET

# -------------------------------

# We create simple data manually

# lotsize, bathrms → input

# price → output

data = {
'lotsize': [1,2,3,4,5],
'bathrms': [1,1,2,2,3],
'price':   [10,18,25,42,60]
}              

# Convert dictionary → table (DataFrame)

df = pd.DataFrame(data)

# -------------------------------

# STEP 3: SEPARATE INPUT AND OUTPUT

# -------------------------------

# X = independent variables (inputs)

x = df[['lotsize','bathrms']]

# Y = dependent variable (output)

y = df['price']

# -------------------------------

# STEP 4: POLYNOMIAL FEATURES

# -------------------------------

# PolynomialFeatures creates new features like:

# [1, x1, x2, x1^2, x2^2, x1*x2]

poly = PolynomialFeatures(degree=2)

# fit_transform:

# fit = learn structure

# transform = apply transformation

xpoly = poly.fit_transform(x)

# Example:

# If x = [2,1]

# Output = [1, 2, 1, 4, 1, 2]

# -------------------------------

# STEP 5: TRAIN-TEST SPLIT

# -------------------------------

# train_test_split = function used to divide data into 2 parts

# WHY?

# 👉 Train data → used to learn

# 👉 Test data → used to check performance

# test_size=0.3 → 30% data for testing

# random_state=1 → ensures same split every time (important for reproducibility)

xtrain, xtest, ytrain, ytest = train_test_split(
xpoly, y, test_size=0.3, random_state=1
)

# Think:

# Training = studying

# Testing = exam

# -------------------------------

# STEP 6: CREATE MODEL

# -------------------------------

# LinearRegression = algorithm that finds best line/curve

model = LinearRegression()

# IMPORTANT:

# Even in polynomial regression,

# we still use LinearRegression!

# -------------------------------

# STEP 7: TRAIN MODEL

# -------------------------------

# fit() = train the model

model.fit(xtrain, ytrain)

# Model learns relationship between input and output

# -------------------------------

# STEP 8: MAKE PREDICTIONS

# -------------------------------

# predict() = use trained model to predict output

ypred = model.predict(xtest)

# -------------------------------

# STEP 9: EVALUATE MODEL

# -------------------------------

# MSE = average of squared errors

mse = mean_squared_error(ytest, ypred)

# RMSE = square root of MSE

rmse = np.sqrt(mse)

# R2 score = how good model is (1 = perfect)

r2 = r2_score(ytest, ypred)

# -------------------------------

# STEP 10: PRINT RESULTS

# -------------------------------

print("Predictions:", ypred)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# -------------------------------

# 🧠 FINAL UNDERSTANDING

# -------------------------------

# sklearn = ML library

# model_selection = used to split data

# train_test_split = divides data into training & testing

# PolynomialFeatures = creates new features

# LinearRegression = learns relationship

# fit() = training

# predict() = testing

# Good model:

# low MSE

# low RMSE

# high R2
