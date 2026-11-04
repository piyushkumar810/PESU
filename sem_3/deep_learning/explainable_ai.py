
# ============================================================
# EXPLAINABLE AI (XAI) USING CNN AND GRAD-CAM
# Dataset: Fashion MNIST
# Framework: TensorFlow / Keras
# ============================================================


# STEP 1: IMPORT REQUIRED LIBRARIES

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)

from tensorflow.keras.datasets import fashion_mnist


# STEP 2: LOAD THE DATASET

# Fashion MNIST contains 70,000 grayscale images.
# 60,000 images are used for training.
# 10,000 images are used for testing.

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()


# STEP 3: PREPROCESS THE DATA

# Select 10,000 training images.
# Select 2,000 testing images.

x_train = x_train[:10000]
y_train = y_train[:10000]

x_test = x_test[:2000]
y_test = y_test[:2000]


# Normalize pixel values.
# Original pixel values range from 0 to 255.
# Dividing by 255 converts them into 0 to 1.

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0


# CNN expects images in 3D format:
# (Height, Width, Channels)
#
# Fashion MNIST is grayscale, so channels = 1.

x_train = np.expand_dims(x_train, axis=-1)
x_test = np.expand_dims(x_test, axis=-1)


# Display dataset shapes.

print("Train Data Shape:", x_train.shape)
print("Test Data Shape:", x_test.shape)


# STEP 4: DISPLAY FIRST 10 IMAGES

# Fashion MNIST class names.

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]

# Create a figure with 10 subplots.

plt.figure(figsize=(12, 5))

for i in range(10):

    # Create subplot.
    plt.subplot(2, 5, i + 1)

    # Display grayscale image.
    plt.imshow(x_train[i].squeeze(), cmap="gray")

    # Display actual class name.
    plt.title(class_names[y_train[i]])

    plt.axis("off")

plt.tight_layout()
plt.show()


# STEP 5: BUILD CNN MODEL

# Sequential model allows us to stack layers one after another.

model = Sequential([

    # Input image size: 28 x 28 with 1 channel.
    Input(shape=(28, 28, 1)),

    # First convolution layer.
    # Extracts basic image features such as edges.
    Conv2D(
        32,
        kernel_size=(3, 3),
        activation="relu",
        name="conv1"
    ),

    # Reduces spatial dimensions.
    MaxPooling2D(pool_size=(2, 2)),

    # Second convolution layer.
    # Learns more complex image features.
    Conv2D(
        64,
        kernel_size=(3, 3),
        activation="relu",
        name="conv2"
    ),

    # Reduces feature map size.
    MaxPooling2D(pool_size=(2, 2)),

    # Converts 2D feature maps into a 1D vector.
    Flatten(),

    # Fully connected layer.
    Dense(128, activation="relu"),

    # Prevents overfitting.
    Dropout(0.3),

    # Output layer.
    # 10 neurons represent 10 Fashion MNIST classes.
    Dense(10, activation="softmax")

])


# STEP 6: DISPLAY MODEL SUMMARY

model.summary()


# STEP 7: COMPILE THE MODEL

model.compile(

    # Adam optimizer updates model weights.
    optimizer="adam",

    # Sparse categorical crossentropy for integer labels.
    loss="sparse_categorical_crossentropy",

    # Accuracy measures correct predictions.
    metrics=["accuracy"]

)


# STEP 8: TRAIN THE MODEL

history = model.fit(

    x_train,
    y_train,

    # Number of complete passes through training data.
    epochs=5,

    # Number of samples processed in one batch.
    batch_size=64,

    # Validation data checks performance during training.
    validation_split=0.2

)


# STEP 9: EVALUATE THE MODEL

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test
)

print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)


# STEP 10: VISUALIZE TRAINING ACCURACY

plt.figure(figsize=(10, 4))

plt.plot(history.history["accuracy"], label="Training Accuracy")

plt.plot(
    history.history["val_accuracy"],
    label="Validation Accuracy"
)

plt.title("Model Accuracy")

plt.xlabel("Epochs")
plt.ylabel("Accuracy")

plt.legend()
plt.show()


# STEP 11: MAKE PREDICTIONS

# Select one test image.
image = x_test[0]

# Add batch dimension.
image_input = np.expand_dims(image, axis=0)

# Predict class probabilities.
prediction = model.predict(image_input, verbose=0)

# Find class with highest probability.
predicted_class = np.argmax(prediction[0])

# Actual class.
actual_class = y_test[0]

print("Predicted Class:", class_names[predicted_class])
print("Actual Class:", class_names[actual_class])

print(
    "Prediction Confidence:",
    prediction[0][predicted_class] * 100,
    "%"
)


# STEP 12: IMPLEMENT GRAD-CAM
# GRAD-CAM = Gradient-weighted Class Activation Mapping
#
# It highlights image regions that influence the prediction.


def make_gradcam_heatmap(image_input, model, last_conv_layer_name):

    # Create a model that returns:
    # 1. Feature maps from the last convolution layer.
    # 2. Final model predictions.

    grad_model = Model(
        inputs=model.inputs,
        outputs=[
            model.get_layer(last_conv_layer_name).output,
            model.output
        ]
    )

    # GradientTape records operations for gradient calculation.
    with tf.GradientTape() as tape:

        # Get convolution feature maps and predictions.
        conv_outputs, predictions = grad_model(image_input)

        # Select the predicted class score.
        class_index = tf.argmax(predictions[0])

        class_score = predictions[:, class_index]

    # Calculate gradients of class score
    # with respect to convolution feature maps.

    grads = tape.gradient(class_score, conv_outputs)

    # Calculate importance weights by averaging gradients.
    pooled_grads = tf.reduce_mean(
        grads,
        axis=(0, 1, 2)
    )

    # Remove batch dimension.
    conv_outputs = conv_outputs[0]

    # Multiply feature maps by their importance weights.
    heatmap = tf.reduce_sum(
        conv_outputs * pooled_grads,
        axis=-1
    )

    # Apply ReLU to keep positive contributions.
    heatmap = tf.maximum(heatmap, 0)

    # Normalize heatmap between 0 and 1.
    heatmap = heatmap / (
        tf.reduce_max(heatmap) + tf.keras.backend.epsilon()
    )

    return heatmap.numpy()


# STEP 13: GENERATE GRAD-CAM HEATMAP

heatmap = make_gradcam_heatmap(
    image_input,
    model,
    "conv2"
)


# STEP 14: DISPLAY ORIGINAL IMAGE AND HEATMAP

plt.figure(figsize=(10, 4))

# Original image.
plt.subplot(1, 2, 1)

plt.imshow(image.squeeze(), cmap="gray")

plt.title("Original Image")

plt.axis("off")


# Grad-CAM heatmap.
plt.subplot(1, 2, 2)

plt.imshow(image.squeeze(), cmap="gray")

plt.imshow(
    heatmap,
    cmap="jet",
    alpha=0.5
)

plt.title("Grad-CAM Heatmap")

plt.axis("off")

plt.tight_layout()
plt.show()


# STEP 15: DISPLAY FINAL EXPLANATION

plt.figure(figsize=(6, 5))

plt.imshow(image.squeeze(), cmap="gray")

plt.imshow(
    heatmap,
    cmap="jet",
    alpha=0.5
)

plt.title(
    f"Prediction: {class_names[predicted_class]}"
)

plt.axis("off")

plt.show()


# STEP 16: SAVE TRAINED MODEL

model.save("fashion_mnist_xai_model.keras")

print("Model saved successfully!")
