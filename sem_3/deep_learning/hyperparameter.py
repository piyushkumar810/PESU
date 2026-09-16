# ============================================================
#       RANDOM SEARCH HYPERPARAMETER TUNING
# ============================================================

import numpy as np
import tensorflow as tf
import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler


# ============================================================
# 1. LOAD DATASET
# ============================================================

data = load_iris()

X = data.data
y = data.target


# ============================================================
# 2. TRAIN-TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ============================================================
# 3. FEATURE SCALING
# ============================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ============================================================
# 4. FUNCTION TO CREATE MODEL
# ============================================================

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


# ============================================================
# 5. FUNCTION TO EVALUATE A CONFIGURATION
# ============================================================

def evaluate_configuration(
    hidden_units,
    learning_rate,
    dropout
):

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
    loss, accuracy = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    return accuracy


# ============================================================
# 6. DEFINE HYPERPARAMETERS
# ============================================================

random_parameters = {

    "hidden_units": [16, 32, 64, 128],

    "learning_rate": [
        0.001,
        0.005,
        0.01
    ],

    "dropout": [
        0.0,
        0.2,
        0.3,
        0.5
    ]
}


# ============================================================
# 7. NUMBER OF RANDOM TRIALS
# ============================================================

number_of_trials = 10


# ============================================================
# 8. STORE RESULTS
# ============================================================

random_results = []


# ============================================================
# 9. RANDOM SEARCH
# ============================================================

for i in range(number_of_trials):

    # --------------------------------------------------------
    # Randomly select hyperparameters
    # --------------------------------------------------------

    hidden_units = random.choice(
        random_parameters["hidden_units"]
    )

    learning_rate = random.choice(
        random_parameters["learning_rate"]
    )

    dropout = random.choice(
        random_parameters["dropout"]
    )


    # --------------------------------------------------------
    # Print current experiment
    # --------------------------------------------------------

    print(
        f"Experiment {i + 1}/{number_of_trials}: "
        f"units = {hidden_units}, "
        f"learning_rate = {learning_rate}, "
        f"dropout = {dropout}"
    )


    # --------------------------------------------------------
    # Evaluate selected configuration
    # --------------------------------------------------------

    score = evaluate_configuration(
        hidden_units,
        learning_rate,
        dropout
    )


    # --------------------------------------------------------
    # Store result
    # --------------------------------------------------------

    random_results.append({

        "hidden_units": hidden_units,

        "learning_rate": learning_rate,

        "dropout": dropout,

        "accuracy": score
    })


    print(f"Accuracy = {score:.4f}")
    print("-" * 60)


# ============================================================
# 10. FIND BEST CONFIGURATION
# ============================================================

best_random = max(
    random_results,
    key=lambda x: x["accuracy"]
)


# ============================================================
# 11. PRINT BEST CONFIGURATION
# ============================================================

print("\nBest Random Search Configuration:")

print(best_random)