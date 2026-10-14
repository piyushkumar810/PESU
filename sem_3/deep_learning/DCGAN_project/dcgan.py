'''
Question 1: DCGAN — Handwritten Digit Image Generation
We will build a Deep Convolutional Generative Adversarial Network (DCGAN) using TensorFlow/Keras to generate handwritten digits similar to those in the MNIST dataset.
The solution covers all the requirements in your question:
1. Load and preprocess the MNIST dataset.
2. Build a convolutional generator.
3. Build a convolutional discriminator.
4. Train both networks using real and generated images.
5. Generate and display 16 synthetic images.
6. Explain the generated image quality and how convolutional layers capture spatial features.
'''

# solution

'''
1. Understand the architecture first
A DCGAN is a GAN that uses convolutional layers rather than relying only on fully connected layers.

Random noise
100 random numbers
    |
Generator
Dense → Reshape → Transposed convolutions
    |
Synthetic digit image
28 × 28 × 1 pixels
    |
Discriminator
Convolutions → Dense → Real/fake score


The two networks have opposing goals:
- Generator: Make fake digit images convincing enough to be classified as real.
- Discriminator: Correctly distinguish real MNIST images from generated images.

During training, the discriminator learns from real and fake images, while the generator learns from the discriminator's feedback.
'''

'''
2. Complete TensorFlow/Keras code
Run the following code in a Kaggle notebook or Google Colab. It is organized into steps so you can understand each part.
'''
# Step 1 — Import libraries

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time

'''
Explanation
- tensorflow: builds and trains the neural networks.
- numpy: handles arrays and random values.
- matplotlib: displays the generated digit images.
- time: measures training duration.
'''

# Step 2 — Load and preprocess MNIST
(x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype("float32")
x_train = (x_train - 127.5) / 127.5
x_train = np.expand_dims(x_train, axis=-1)

BATCH_SIZE = 128

train_dataset = (
    tf.data.Dataset.from_tensor_slices(x_train)
    .shuffle(60000)
    .batch(BATCH_SIZE, drop_remainder=True)
    .prefetch(tf.data.AUTOTUNE)
)

print("Training data shape:", x_train.shape)
print("Batch size:", BATCH_SIZE)

'''
Explanation
MNIST contains grayscale images of handwritten digits from 0 to 9. Each image is \(28\times28\) pixels.
- (_, _) ignores the labels because GAN training does not require digit class labels for this task.
- Normalization converts pixel values from \([0,255]\) to \([-1,1]\).
- expand_dims adds a channel dimension, producing the shape (60000, 28, 28, 1).
- shuffle mixes the training examples.
- batch groups images into batches of 128.
Why normalize to −1 to 1? The generator will use tanh in its output layer, which produces values in the same range.
'''

# Step 3 — Build the generator
noise_dim = 100

generator = tf.keras.Sequential([
    tf.keras.Input(shape=(noise_dim,)),

    tf.keras.layers.Dense(
        7 * 7 * 128,
        use_bias=False
    ),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.LeakyReLU(negative_slope=0.2),

    tf.keras.layers.Reshape((7, 7, 128)),

    tf.keras.layers.Conv2DTranspose(
        64, 4, strides=2, padding="same",
        use_bias=False
    ),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.LeakyReLU(negative_slope=0.2),

    tf.keras.layers.Conv2DTranspose(
        1, 4, strides=2, padding="same",
        activation="tanh"
    )
], name="generator")

generator.summary()

'''
How does it work?

Random noise: 100 values
    |
Dense: 6,272 values
    |
Reshape: (7*7*128)
    |
Transposed convolution: (14*14*64)
    |
Transposed convolution: (28*28*1)


Key concepts:
- Dense: Expands the noise into an initial feature representation.
- Reshape: Arranges the features into a spatial grid.
- Conv2DTranspose: Learns to upsample the feature maps to create an image.
- BatchNormalization: Helps stabilize training.
- LeakyReLU: Allows a small negative output instead of setting all negative values to zero.
- Tanh: Restricts generated pixel values to \([-1,1]\).
The generator gradually constructs spatial structure: strokes, curves and digit-like shapes.
'''

# Step 4 — Build the discriminator
discriminator = tf.keras.Sequential([
    tf.keras.Input(shape=(28, 28, 1)),

    tf.keras.layers.Conv2D(
        64, 4, strides=2, padding="same"
    ),
    tf.keras.layers.LeakyReLU(negative_slope=0.2),
    tf.keras.layers.Dropout(0.3),

    tf.keras.layers.Conv2D(
        128, 4, strides=2, padding="same"
    ),
    tf.keras.layers.LeakyReLU(negative_slope=0.2),
    tf.keras.layers.Dropout(0.3),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1)
], name="discriminator")

discriminator.summary()

'''
Explanation
The discriminator receives a real or generated image and estimates whether it is real.
- Conv2D: extracts local image features.
- LeakyReLU: introduces nonlinearity.
- Dropout: reduces over-reliance on particular activations.
- Flatten: converts feature maps into a vector.
- Dense(1): produces one raw score, called a logit.
The final layer has no sigmoid because we will use binary cross-entropy with from_logits=True. The logit is not itself a probability.
'''

# Step 5 — Define losses and optimizers
cross_entropy = tf.keras.losses.BinaryCrossentropy(
    from_logits=True
)

generator_optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.0001,
    beta_1=0.5
)

discriminator_optimizer = tf.keras.optimizers.Adam(
    learning_rate=0.0001,
    beta_1=0.5
)

def generator_loss(fake_output):
    return cross_entropy(
        tf.ones_like(fake_output),
        fake_output
    )

def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(
        tf.ones_like(real_output),
        real_output
    )

    fake_loss = cross_entropy(
        tf.zeros_like(fake_output),
        fake_output
    )

    return real_loss + fake_loss

'''
Why are there two losses?
Loss	                What it encourages
Generator loss	        Fake images should be classified as real
Discriminator loss	    Real images should be classified as real, and fake images as fake
The generator uses target label 1 for its fake outputs because it wants to fool the discriminator. The discriminator uses 1 for real samples and 0 for fake samples.
Adam updates each network's weights using gradients calculated from its own loss.
'''


# Step 6 — Train both networks   -> This is the core of DCGAN.
@tf.function
def train_step(real_images):
    batch_size = tf.shape(real_images)[0]

    noise = tf.random.normal(
        shape=(batch_size, noise_dim)
    )

    with tf.GradientTape() as gen_tape, \
         tf.GradientTape() as disc_tape:

        fake_images = generator(noise, training=True)

        real_output = discriminator(
            real_images, training=True
        )

        fake_output = discriminator(
            fake_images, training=True
        )

        gen_loss = generator_loss(fake_output)

        disc_loss = discriminator_loss(
            real_output, fake_output
        )

    gen_gradients = gen_tape.gradient(
        gen_loss,
        generator.trainable_variables
    )

    disc_gradients = disc_tape.gradient(
        disc_loss,
        discriminator.trainable_variables
    )

    generator_optimizer.apply_gradients(
        zip(gen_gradients, generator.trainable_variables)
    )

    discriminator_optimizer.apply_gradients(
        zip(disc_gradients, discriminator.trainable_variables)
    )

    return gen_loss, disc_loss

'''
Understand the training step in order:
1. Generate random noise.
2. Pass noise through the generator to create fake images.
3. Pass real and fake images through the discriminator.
4. Calculate generator and discriminator losses.
5. Use GradientTape to calculate gradients for both networks.
6. Update each network with its own optimizer.
The generator's gradients flow through the discriminator's calculations, but only the generator's parameters are updated by the generator optimizer. The discriminator's parameters are updated separately.
'''

# Step 7 — Run training
EPOCHS = 30

for epoch in range(EPOCHS):
    start_time = time.time()

    gen_loss_total = 0.0
    disc_loss_total = 0.0
    batches = 0

    for real_images in train_dataset:
        gen_loss, disc_loss = train_step(real_images)

        gen_loss_total += float(gen_loss)
        disc_loss_total += float(disc_loss)
        batches += 1

    print(
        f"Epoch {epoch + 1}/{EPOCHS} | "
        f"Generator Loss: {gen_loss_total / batches:.4f} | "
        f"Discriminator Loss: {disc_loss_total / batches:.4f} | "
        f"Time: {time.time() - start_time:.1f}s"
    )

'''
What happens over the epochs?
Initially, the generator usually creates noise-like images. As training progresses, it may learn digit-like shapes and more realistic strokes.
However, GAN training is not guaranteed to improve smoothly at every epoch. The loss values can fluctuate, and both networks need to remain reasonably balanced.
Thirty epochs is a starting point, not a guarantee of perfect digits. Increase training time or tune the model if the generated images remain poor.
'''

# Step 8 — Generate and display 16 synthetic images  ->After training, we sample new random noise and pass it through the generator. No real images are supplied during this generation step.
noise = tf.random.normal((16, noise_dim))

generated_images = generator(
    noise, training=False
)

generated_images = (generated_images + 1) / 2

fig, axes = plt.subplots(4, 4, figsize=(7, 7))

for i, ax in enumerate(axes.flat):
    ax.imshow(
        generated_images[i, :, :, 0],
        cmap="gray",
        vmin=0,
        vmax=1
    )
    ax.axis("off")

plt.suptitle("16 Synthetic MNIST Images Generated by DCGAN")
plt.tight_layout()
plt.show()

'''
Explanation
- tf.random.normal((16, 100)) creates 16 independent latent noise vectors.
- The generator converts each vector into a \(28\times28\) image.
- (generated_images + 1) / 2 converts pixels from \([-1,1]\) to \([0,1]\) for display.
- plt.subplots(4, 4) displays all 16 generated images in a grid.
- training=False disables training-specific behavior in layers such as batch normalization and dropout.
The output will be a grid of 16 generated images. Their actual appearance depends on your training run; initially, some may look like noise or incomplete digits.
'''

# Step 9 — Compare real and generated images -> This additional visualization helps you assess image quality against the MNIST training examples.
real_images = next(iter(train_dataset))
real_images = (real_images[:16] + 1) / 2

fig, axes = plt.subplots(2, 8, figsize=(12, 4))

for i in range(8):
    axes[0, i].imshow(
        real_images[i, :, :, 0],
        cmap="gray",
        vmin=0,
        vmax=1
    )
    axes[0, i].axis("off")

    axes[1, i].imshow(
        generated_images[i, :, :, 0],
        cmap="gray",
        vmin=0,
        vmax=1
    )
    axes[1, i].axis("off")

axes[0, 0].set_ylabel("Real", fontsize=10)
axes[1, 0].set_ylabel("Generated", fontsize=10)

plt.suptitle("Real MNIST Images vs DCGAN-Generated Images")
plt.tight_layout()
plt.show()

'''
This extra plot compares eight real examples with eight generated examples. The main required output remains the grid of 16 synthetic images.
'''

# 9. Save trained models
generator.save("dcgan_generator.keras")
discriminator.save("dcgan_discriminator.keras")

print("Models saved successfully.")