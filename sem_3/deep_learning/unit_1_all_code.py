"""UNIT 1 — All exam-relevant TensorFlow examples in one Python file.
Install: pip install tensorflow numpy
Run: python unit1_all_codes.py
Each section uses tiny synthetic data; no downloads required.
"""
import numpy as np
import tensorflow as tf

np.random.seed(42)
tf.random.set_seed(42)


def heading(s):
    print('\n' + '=' * 16 + ' ' + s + ' ' + '=' * 16)

# 1. ACTIVATION FUNCTIONS
heading('1. ReLU, sigmoid, tanh')
x = tf.constant([-2., -1., 0., 1., 2.])
print('ReLU   :', tf.keras.activations.relu(x).numpy())
print('Sigmoid:', np.round(tf.keras.activations.sigmoid(x).numpy(), 3))
print('Tanh   :', np.round(tf.keras.activations.tanh(x).numpy(), 3))

# 2. MANUAL NEURON: weighted sum + activation
heading('2. Manual neuron')
x = tf.constant([2., 3.])
w = tf.constant([0.5, -0.2])
b = tf.constant(0.1)
z = tf.reduce_sum(x * w) + b
out = tf.keras.activations.relu(z)
print('z =', z.numpy(), '; ReLU(z) =', out.numpy())  # 0.5, 0.5

# 3. DENSE LAYER AND FEEDFORWARD NETWORK
heading('3. Dense layer / Sequential')
model = tf.keras.Sequential([
    tf.keras.Input(shape=(4,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])
model.summary()
print('One prediction:', model(tf.constant([[0.1, 0.2, 0.3, 0.4]])).numpy())

# 4. MSE LOSS
heading('4. Mean Squared Error')
y_true = tf.constant([[10.], [20.], [30.]])
y_pred = tf.constant([[12.], [18.], [29.]])
mse = tf.keras.losses.MeanSquaredError()
print('MSE:', mse(y_true, y_pred).numpy())  # 3.0

# 5. BINARY CROSS-ENTROPY (probabilities and logits)
heading('5. Binary Cross-Entropy')
y_true = tf.constant([[1.], [0.], [1.]])
y_prob = tf.constant([[0.9], [0.2], [0.7]])
bce = tf.keras.losses.BinaryCrossentropy()
print('BCE probabilities:', bce(y_true, y_prob).numpy())
logits = tf.math.log(y_prob / (1. - y_prob))
print('BCE from logits:', tf.keras.losses.BinaryCrossentropy(from_logits=True)(y_true, logits).numpy())

# 6. CATEGORICAL vs SPARSE CATEGORICAL CROSS-ENTROPY
heading('6. CCE and Sparse CCE')
y_onehot = tf.constant([[0., 1., 0.]])
y_integer = tf.constant([1])
y_prob = tf.constant([[0.1, 0.8, 0.1]])
print('CCE:', tf.keras.losses.CategoricalCrossentropy()(y_onehot, y_prob).numpy())
print('Sparse CCE:', tf.keras.losses.SparseCategoricalCrossentropy()(y_integer, y_prob).numpy())

# 7. MATCH OUTPUT LAYER TO LOSS
heading('7. Model compilation: task and loss')
regression = tf.keras.Sequential([tf.keras.Input(shape=(4,)), tf.keras.layers.Dense(1)])
regression.compile(optimizer='adam', loss='mse', metrics=['mae'])
binary = tf.keras.Sequential([tf.keras.Input(shape=(4,)), tf.keras.layers.Dense(1, activation='sigmoid')])
binary.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
multiclass = tf.keras.Sequential([tf.keras.Input(shape=(4,)), tf.keras.layers.Dense(3, activation='softmax')])
multiclass.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
sparse_multiclass = tf.keras.Sequential([tf.keras.Input(shape=(4,)), tf.keras.layers.Dense(3, activation='softmax')])
sparse_multiclass.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print('Regression: linear + MSE; binary: sigmoid + BCE; multiclass: softmax + CCE/sparse CCE')

# 8. FORWARD PASS + LOSS + BACKPROPAGATION USING GRADIENTTAPE
heading('8. Forward pass, loss and gradients')
train_model = tf.keras.Sequential([tf.keras.Input(shape=(2,)), tf.keras.layers.Dense(1, activation='sigmoid')])
inputs = tf.constant([[1., 2.]])
targets = tf.constant([[1.]])
with tf.GradientTape() as tape:
    predictions = train_model(inputs, training=True)
    loss = tf.reduce_mean((targets - predictions) ** 2)
gradients = tape.gradient(loss, train_model.trainable_variables)
print('Prediction:', predictions.numpy(), 'Loss:', loss.numpy())
for variable, gradient in zip(train_model.trainable_variables, gradients):
    print(variable.name, 'gradient shape:', gradient.shape)

# 9. SIMPLE AUTOMATIC DIFFERENTIATION
heading('9. Gradient of y = x^2 at x = 3')
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x ** 2
print('dy/dx =', tape.gradient(y, x).numpy())  # 6.0

# 10. MANUAL GRADIENT DESCENT UPDATE
heading('10. Manual update')
w = tf.Variable(0.50)
learning_rate = 0.10
gradient = tf.constant(0.30)
w.assign_sub(learning_rate * gradient)
print('New weight:', round(float(w.numpy()), 2))  # 0.47

# 11. SGD, SGD + MOMENTUM, ADAM, RMSPROP
heading('11. Optimizers')
optimizers = {
    'SGD': tf.keras.optimizers.SGD(learning_rate=0.01),
    'Momentum': tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    'Adam': tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-7),
    'RMSprop': tf.keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9, momentum=0., epsilon=1e-7),
}
for name, optimizer in optimizers.items():
    print(name, '->', type(optimizer).__name__)

# 12. FAIR OPTIMIZER COMPARISON (fresh model each time)
heading('12. Train the same architecture with different optimizers')
features = np.random.default_rng(42).normal(size=(32, 4)).astype('float32')
labels = (features.sum(axis=1) > 0).astype('float32').reshape(-1, 1)
def build_model():
    return tf.keras.Sequential([
        tf.keras.Input(shape=(4,)),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])
for name, optimizer in [('SGD', tf.keras.optimizers.SGD(0.01)), ('Adam', tf.keras.optimizers.Adam(0.001)), ('RMSprop', tf.keras.optimizers.RMSprop(0.001))]:
    tf.keras.utils.set_random_seed(123)  # same initial weights for a fair illustration
    m = build_model()
    m.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    history = m.fit(features, labels, epochs=2, batch_size=8, verbose=0)
    print(name, 'final training loss:', round(history.history['loss'][-1], 4))

# 13. GLOTOR/XAVIER vs HE INITIALIZATION
heading('13. Initializers')
glorot = tf.keras.layers.Dense(16, activation='tanh', kernel_initializer='glorot_uniform')
he = tf.keras.layers.Dense(16, activation='relu', kernel_initializer='he_normal')
print('Glorot/Xavier: often tanh/sigmoid; He: often ReLU')

# 14. INPUT STANDARDIZATION (fit ONLY on training data)
heading('14. Input standardization')
train = np.array([[40., 100.], [50., 200.], [60., 300.]], dtype=np.float32)
test = np.array([[70., 400.]], dtype=np.float32)
mean = train.mean(axis=0)
std = train.std(axis=0)
print('Standardized train:', (train - mean) / (std + 1e-7))
print('Standardized test:', (test - mean) / (std + 1e-7))

# 15. BATCH NORMALIZATION + DROPOUT + L2 REGULARIZATION
heading('15. Regularized model')
regularized = tf.keras.Sequential([
    tf.keras.Input(shape=(20,)),
    tf.keras.layers.Dense(64, use_bias=False, kernel_initializer='he_normal',
                          kernel_regularizer=tf.keras.regularizers.L2(0.001)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])
regularized.summary()
print('Dropout 0.3: drops 30% of inputs during training, not inference')

# 16. EARLY STOPPING
heading('16. EarlyStopping callback')
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss', min_delta=0.001, patience=5,
    mode='min', restore_best_weights=True,
)
print('Callback:', type(early_stopping).__name__)
# Use with: model.fit(x_train, y_train, validation_data=(x_val, y_val),
#                     epochs=100, callbacks=[early_stopping])

# 17. L2 PENALTY NUMERICAL
heading('17. L2 penalty numerical')
weights = tf.constant([0.5, -0.2, 0.1])
lam = 0.01
penalty = lam * tf.reduce_sum(weights ** 2)
print('L2 penalty:', round(float(penalty.numpy()), 3))  # 0.003

# 18. ADAMW DECOUPLED WEIGHT DECAY
heading('18. AdamW')
adamw = tf.keras.optimizers.AdamW(learning_rate=0.001, weight_decay=0.004)
print('Optimizer:', type(adamw).__name__)
print('\nUNIT 1 FINISHED')
