import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = load_iris()

X = data.data
y = data.target


# --------------------------------------------------
# 2. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# 3. Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# --------------------------------------------------
# 4. Function to Create Model
# --------------------------------------------------

def create_model(hidden_units, learning_rate, dropout):

    model = Sequential([
        Dense(
            hidden_units,
            activation="relu",
            input_shape=(X_train.shape[1],)
        ),

        Dropout(dropout),

        Dense(3, activation="softmax")
    ])

    model.compile(
        optimizer=Adam(learning_rate=learning_rate),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


# --------------------------------------------------
# 5. Hyperparameter Values
# --------------------------------------------------

hidden_units_list = [16, 32, 64]
learning_rate_list = [0.001, 0.01]
dropout_list = [0.0, 0.2, 0.5]


# --------------------------------------------------
# 6. Grid Search
# --------------------------------------------------

grid_results = []


for hidden_units in hidden_units_list:

    for learning_rate in learning_rate_list:

        for dropout in dropout_list:

            print(
                f"\nTesting: "
                f"hidden_units={hidden_units}, "
                f"learning_rate={learning_rate}, "
                f"dropout={dropout}"
            )

            # Create model
            model = create_model(
                hidden_units,
                learning_rate,
                dropout
            )

            # Train model
            model.fit(
                X_train,
                y_train,
                epochs=50,
                batch_size=16,
                verbose=0
            )

            # Evaluate model
            loss, score = model.evaluate(
                X_test,
                y_test,
                verbose=0
            )

            # Store result
            grid_results.append({
                "hidden_units": hidden_units,
                "learning_rate": learning_rate,
                "dropout": dropout,
                "accuracy": score
            })


# --------------------------------------------------
# 7. Find Best Configuration
# --------------------------------------------------

best_grid = max(
    grid_results,
    key=lambda x: x["accuracy"]
)


# --------------------------------------------------
# 8. Print Best Configuration
# --------------------------------------------------

print("\nBest Grid Search Configuration:")
print(best_grid)


#---------------------------------------------------- explanation
# ============================================================
#          HYPERPARAMETER TUNING USING GRID SEARCH
# ============================================================
#
#                 BEGINNER FRIENDLY FLOW
# ============================================================


# ============================================================
# BIG PICTURE
# ============================================================

# We have a dataset.
#
# We want to build a Neural Network that can make predictions.
#
# But we don't know which settings (hyperparameters) will
# give the best performance.
#
# So we try different combinations of:
#
#       1. hidden_units
#       2. learning_rate
#       3. dropout
#
# For every combination:
#
#       Create Model
#            ↓
#       Train Model
#            ↓
#       Test Model
#            ↓
#       Get Accuracy
#            ↓
#       Store Accuracy
#
# Finally:
#
#       Compare all accuracies
#            ↓
#       Select highest accuracy
#            ↓
#       BEST CONFIGURATION
#
#
# ============================================================
# SIMPLE REAL-LIFE EXAMPLE
# ============================================================
#
# Imagine you are preparing for an exam.
#
# You want to find the best study strategy.
#
# You try:
#
# Study Hours = 2, 4, 6
# Break Time  = 10, 20 minutes
# Revision    = Yes, No
#
# You try EVERY possible combination.
#
# Example:
#
# 2 hours + 10 min break + Revision
# 2 hours + 10 min break + No Revision
# 2 hours + 20 min break + Revision
# 2 hours + 20 min break + No Revision
# ...
#
# After trying everything, you check your marks.
#
# The combination giving the highest marks
# becomes your BEST strategy.
#
#
# GRID SEARCH DOES EXACTLY THE SAME THING
#
# Instead of:
#
#       Study Hours
#       Break Time
#       Revision
#
# We have:
#
#       hidden_units
#       learning_rate
#       dropout
#
# And instead of exam marks:
#
#       Accuracy
#
#
# ============================================================
# STEP 1: LOAD THE DATASET
# ============================================================
#
# First, we need data.
#
# Example:
#
# X = input/features
# y = output/target
#
# For Iris dataset:
#
# X contains:
#
#       sepal length
#       sepal width
#       petal length
#       petal width
#
# y contains the flower class:
#
#       0
#       1
#       2
#
#
# So:
#
#          X --------------> Neural Network
#          |
#          | features
#          ↓
#       Prediction
#
#
# ============================================================
# STEP 2: SPLIT THE DATA
# ============================================================
#
# We divide our data into:
#
#       Training Data
#       Testing Data
#
#
# TRAINING DATA
# ----------------
# Used to TEACH the neural network.
#
#
# TESTING DATA
# ----------------
# Used to CHECK how well the neural network learned.
#
#
# Example:
#
# Total Data = 100%
#
#       80% ----------------> Training
#       20% ----------------> Testing
#
#
# Why?
#
# If we test the model using the same data that it memorized,
# we cannot properly know whether it can work on new data.
#
#
# ============================================================
# STEP 3: FEATURE SCALING
# ============================================================
#
# Sometimes features have very different ranges.
#
# Example:
#
# Age       = 20 - 60
# Salary    = 20,000 - 2,00,000
#
# Salary has much larger numbers.
#
# This can make training difficult.
#
# So we scale the features.
#
# After scaling, values are generally around a similar range.
#
#
# FLOW:
#
# Original Data
#      ↓
# Feature Scaling
#      ↓
# Scaled Data
#      ↓
# Neural Network
#
#
# ============================================================
# STEP 4: CREATE A NEURAL NETWORK
# ============================================================
#
# Now we create our model.
#
# Example:
#
#       Input
#         ↓
#   Hidden Layer
#         ↓
#      Dropout
#         ↓
#   Output Layer
#
#
# The important thing is that some values of the model
# are NOT fixed.
#
# These are our HYPERPARAMETERS.
#
#
# ============================================================
# STEP 5: WHAT IS A HYPERPARAMETER?
# ============================================================
#
# A hyperparameter is a setting that we choose BEFORE
# training the neural network.
#
# Example:
#
# hidden_units = 32
# learning_rate = 0.001
# dropout = 0.2
#
#
# These values control HOW the neural network learns.
#
#
# ============================================================
# 1. hidden_units
# ============================================================
#
# hidden_units tells us how many neurons are present
# in the hidden layer.
#
# Example:
#
# hidden_units = 16
#
#             Hidden Layer
#          ○ ○ ○ ○ ○ ○ ○ ○
#          ○ ○ ○ ○ ○ ○ ○ ○
#
# 16 neurons
#
#
# If:
#
# hidden_units = 64
#
#             Hidden Layer
#       ○ ○ ○ ○ ○ ○ ○ ○ ○ ○
#       ○ ○ ○ ○ ○ ○ ○ ○ ○ ○
#       ○ ○ ○ ○ ○ ○ ○ ○ ○ ○
#       ○ ○ ○ ○ ○ ○ ○ ○ ○ ○
#       ...
#
# More neurons = more model capacity.
#
#
# ============================================================
# 2. learning_rate
# ============================================================
#
# learning_rate controls HOW BIG a step the model takes
# while learning.
#
#
# Imagine you are walking toward a destination.
#
# Very large steps:
#
#       🧍 --------> --------> -------->
#
# You may overshoot the destination.
#
#
# Very small steps:
#
#       🧍 -> -> -> -> -> -> -> -> -> 🏁
#
# You may learn very slowly.
#
#
# So we try different values:
#
#       0.001
#       0.01
#
# and see which works better.
#
#
# ============================================================
# 3. dropout
# ============================================================
#
# Dropout is used to reduce OVERFITTING.
#
# During training, dropout randomly turns off some neurons.
#
# Example:
#
# Without Dropout:
#
#       ○ ○ ○ ○ ○ ○ ○ ○
#
#
# With Dropout:
#
#       ○ ✕ ○ ○ ✕ ○ ✕ ○
#
# Some neurons are temporarily ignored.
#
# This encourages the network to learn more general patterns.
#
#
# Example dropout values:
#
#       0.0
#       0.2
#       0.5
#
#
# ============================================================
# STEP 6: CREATE POSSIBLE VALUES
# ============================================================
#
# We now decide which values we want to test.
#
#
# hidden_units_list:
#
#       [16, 32, 64]
#
# learning_rate_list:
#
#       [0.001, 0.01]
#
# dropout_list:
#
#       [0.0, 0.2, 0.5]
#
#
# We are basically saying:
#
# "Let's try these different settings."
#
#
# ============================================================
# STEP 7: GRID SEARCH
# ============================================================
#
# Now comes the MAIN PART.
#
# We use loops to try EVERY possible combination.
#
#
# hidden_units:
#       16
#       32
#       64
#
# learning_rate:
#       0.001
#       0.01
#
# dropout:
#       0.0
#       0.2
#       0.5
#
#
# Number of combinations:
#
#       3 × 2 × 3
#       = 18 combinations
#
#
# So the program trains 18 different models.
#
#
# ============================================================
# STEP 8: FIRST COMBINATION
# ============================================================
#
# Suppose the program starts with:
#
# hidden_units = 16
# learning_rate = 0.001
# dropout = 0.0
#
#
# The model becomes:
#
#       16 neurons
#       learning rate = 0.001
#       dropout = 0.0
#
#
# Then we TRAIN this model.
#
#
# ============================================================
# STEP 9: TRAIN THE MODEL
# ============================================================
#
# During training:
#
#       Input Data
#           ↓
#       Neural Network
#           ↓
#       Prediction
#           ↓
#       Calculate Error
#           ↓
#       Update Weights
#           ↓
#       Repeat
#
#
# This happens for many epochs.
#
# Example:
#
# epochs = 50
#
# means the model goes through the training data
# multiple times.
#
#
# ============================================================
# STEP 10: TEST THE MODEL
# ============================================================
#
# After training, we test the model using TEST DATA.
#
#
# Example:
#
# Model predicts:
#
#       [0, 1, 2, 1, 0]
#
# Actual:
#
#       [0, 1, 2, 0, 0]
#
#
# The model gets some predictions correct
# and some incorrect.
#
# From this we calculate:
#
#       Accuracy
#
#
# Example:
#
#       Accuracy = 0.93
#
# This means approximately:
#
#       93% predictions were correct.
#
#
# ============================================================
# STEP 11: STORE THE RESULT
# ============================================================
#
# We store:
#
#       hidden_units
#       learning_rate
#       dropout
#       accuracy
#
#
# Example:
#
# {
#     "hidden_units": 16,
#     "learning_rate": 0.001,
#     "dropout": 0.0,
#     "accuracy": 0.93
# }
#
#
# This is saved inside:
#
#       grid_results
#
#
# ============================================================
# STEP 12: TRY THE NEXT COMBINATION
# ============================================================
#
# The program does NOT stop.
#
# It changes the settings.
#
#
# Example:
#
# First:
#
#       16, 0.001, 0.0
#       Accuracy = 0.93
#
#
# Next:
#
#       16, 0.001, 0.2
#       Accuracy = 0.95
#
#
# Next:
#
#       16, 0.001, 0.5
#       Accuracy = 0.91
#
#
# And it continues...
#
#
# ============================================================
# STEP 13: ALL COMBINATIONS ARE TESTED
# ============================================================
#
# Eventually we get something like:
#
#
# hidden_units    learning_rate    dropout    accuracy
# ------------------------------------------------------
# 16              0.001            0.0        0.93
# 16              0.001            0.2        0.95
# 16              0.001            0.5        0.91
# 16              0.01             0.0        0.89
# 16              0.01             0.2        0.92
# 16              0.01             0.5        0.90
# 32              0.001            0.0        0.94
# 32              0.001            0.2        0.97   <-- BEST
# 32              0.001            0.5        0.93
# ...
#
#
# ============================================================
# STEP 14: FIND THE BEST RESULT
# ============================================================
#
# Now we have many results.
#
# We want the result with the HIGHEST accuracy.
#
# We use:
#
#       max()
#
#
# Code:
#
# best_grid = max(
#     grid_results,
#     key=lambda x: x["accuracy"]
# )
#
#
# Let's understand this slowly.
#
#
# max(grid_results)
#
# means:
#
#       "Find the largest/best item."
#
#
# But Python needs to know:
#
#       "Best according to WHAT?"
#
# So we write:
#
#       key=lambda x: x["accuracy"]
#
#
# This tells Python:
#
#       "Compare the items using their accuracy."
#
#
# Therefore:
#
#       Highest Accuracy
#              ↓
#       Best Configuration
#
#
# ============================================================
# STEP 15: PRINT THE BEST CONFIGURATION
# ============================================================
#
# Finally:
#
# print(best_grid)
#
#
# Example output:
#
# {
#     'hidden_units': 32,
#     'learning_rate': 0.001,
#     'dropout': 0.2,
#     'accuracy': 0.97
# }
#
#
# This means:
#
# The best combination among the combinations we tested was:
#
#       hidden_units = 32
#       learning_rate = 0.001
#       dropout = 0.2
#
# and it achieved:
#
#       accuracy = 97%
#
#
# ============================================================
# COMPLETE FLOW IN ONE DIAGRAM
# ============================================================
#
#
#                    DATASET
#                       |
#                       ↓
#                Split the Data
#                       |
#             ┌─────────┴─────────┐
#             ↓                   ↓
#         Training             Testing
#             |                   |
#             ↓                   |
#       Feature Scaling           |
#             |                   |
#             ↓                   |
#       Choose Hyperparameters     |
#             |                   |
#             ↓                   |
#       ┌───────────────────┐     |
#       │  GRID SEARCH      │     |
#       │                   │     |
#       │ hidden_units      │     |
#       │ learning_rate     │     |
#       │ dropout           │     |
#       └─────────┬─────────┘     |
#                 ↓               |
#            Create Model         |
#                 ↓               |
#             Train Model         |
#                 ↓               |
#             Test Model <────────┘
#                 ↓
#              Accuracy
#                 ↓
#          Store the Result
#                 ↓
#       Try Next Combination
#                 ↓
#          All Combinations?
#             /         \
#           NO           YES
#           |             |
#           └───→         ↓
#                  Find Maximum Accuracy
#                         ↓
#                  BEST CONFIGURATION
#
#
# ============================================================
# VERY IMPORTANT: WHAT IS HAPPENING?
# ============================================================
#
# Remember these 6 steps:
#
#
#       1. CHOOSE
#          ↓
#       Choose hyperparameter values
#
#       2. COMBINE
#          ↓
#       Make every possible combination
#
#       3. BUILD
#          ↓
#       Build a neural network
#
#       4. TRAIN
#          ↓
#       Train the network
#
#       5. TEST
#          ↓
#       Test and calculate accuracy
#
#       6. SELECT
#          ↓
#       Select the combination with highest accuracy
#
#
# ============================================================
# ONE-LINE MEMORY TRICK
# ============================================================
#
#       "TRY → TRAIN → TEST → RECORD → COMPARE → SELECT"
#
#
# ============================================================
# MOST IMPORTANT EXAM POINT
# ============================================================
#
# GRID SEARCH is a hyperparameter tuning technique.
#
# It systematically tries ALL specified combinations
# of hyperparameter values.
#
# Each combination is used to train and evaluate a model.
#
# Finally, the combination producing the best evaluation
# performance is selected.
#
#
# ============================================================
# HYPERPARAMETERS IN OUR EXAMPLE
# ============================================================
#
# hidden_units
#       ↓
# Number of neurons in hidden layer
#
# learning_rate
#       ↓
# Controls the size of weight updates during learning
#
# dropout
#       ↓
# Randomly disables some neurons during training
# to help reduce overfitting
#
#
# ============================================================
# FINAL UNDERSTANDING
# ============================================================
#
# We are NOT changing the dataset again and again.
#
# We are changing the MODEL'S SETTINGS.
#
# For every setting:
#
#       Model
#         ↓
#       Training
#         ↓
#       Accuracy
#
# Then we compare:
#
#       Accuracy 1
#       Accuracy 2
#       Accuracy 3
#       Accuracy 4
#       ...
#
# And select:
#
#       HIGHEST ACCURACY
#
# That is GRID SEARCH.
#
# ============================================================