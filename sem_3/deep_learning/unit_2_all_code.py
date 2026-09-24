"""UNIT 2 — All exam-relevant TensorFlow examples in one Python file.
Install: pip install tensorflow numpy
Run: python unit2_all_codes.py
No dataset or pretrained-weight downloads required; optional ImageNet code is shown as comments.
"""
import numpy as np
import tensorflow as tf

tf.keras.utils.set_random_seed(42)

def heading(s):
    print('\n' + '=' * 12 + ' ' + s + ' ' + '=' * 12)

# 1. DEEP FEEDFORWARD NETWORK
heading('1. Deep feedforward network')
ffn = tf.keras.Sequential([
    tf.keras.Input(shape=(20,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])
ffn.summary()
print('Dense(20 -> 64) parameters =', 20 * 64 + 64)  # 1344

# 2. CONVOLUTION NUMERICAL (CNN uses cross-correlation, no kernel flip)
heading('2. Manual convolution')
patch = np.array([[1, 2, 0], [0, 1, 3], [2, 1, 0]])
kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
print('Convolution result:', np.sum(patch * kernel))  # 0

# 3. CONV OUTPUT SIZE AND PARAMETER COUNT
heading('3. Output size and parameters')
def conv_output_size(n, k, p=0, s=1):
    return (n + 2 * p - k) // s + 1
print('32x32, 3x3 valid stride 1:', conv_output_size(32, 3))  # 30
print('7x7, 3x3 valid stride 2:', conv_output_size(7, 3, s=2))  # 3
print('28x28, 3x3 valid stride 1:', conv_output_size(28, 3))  # 26
print('Conv2D 3x3, 3 input channels, 32 filters:', (3 * 3 * 3 + 1) * 32)  # 896
print('Conv2D 3x3, 3 input channels, 16 filters:', (3 * 3 * 3 + 1) * 16)  # 448

# 4. CONV2D + MAXPOOL + GLOBAL AVERAGE POOLING
heading('4. Conv2D, MaxPool and GAP')
cnn = tf.keras.Sequential([
    tf.keras.Input(shape=(32, 32, 3)),
    tf.keras.layers.Rescaling(1. / 255.),
    tf.keras.layers.Conv2D(32, (3, 3), strides=(1, 1), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(10, activation='softmax'),
])
cnn.summary()
print('Output shape:', cnn(tf.zeros((1, 32, 32, 3))).shape)
print('2x2 max pooling of [[1,5],[2,3]]:', np.max([[1, 5], [2, 3]]))
print('Pooling (1,32,32,16) with 2x2 stride 2 -> (1,16,16,16)')

# 5. LENET-STYLE NETWORK (modern Keras approximation)
heading('5. LeNet-style model')
lenet = tf.keras.Sequential([
    tf.keras.Input(shape=(32, 32, 1)),
    tf.keras.layers.Conv2D(6, (5, 5), activation='tanh'),
    tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(16, (5, 5), activation='tanh'),
    tf.keras.layers.AveragePooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(120, activation='tanh'),
    tf.keras.layers.Dense(84, activation='tanh'),
    tf.keras.layers.Dense(10, activation='softmax'),
])
lenet.summary()
print('First LeNet conv parameters:', (5 * 5 * 1 + 1) * 6)  # 156

# 6. VGG-STYLE BLOCK AND OPTIONAL PRETRAINED VGG16
heading('6. VGG-style block')
vgg_block = tf.keras.Sequential([
    tf.keras.Input(shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2),
])
print('VGG block output:', vgg_block.output.shape)
print('One 5x5 vs two 3x3 (same channel count C): 25*C^2 vs 18*C^2 weights')
# PRETRAINED VGG16 (requires internet first time):
# vgg = tf.keras.applications.VGG16(include_top=False, weights='imagenet',
#                                  input_shape=(224, 224, 3), pooling='avg')
# rgb_images = tf.keras.applications.vgg16.preprocess_input(rgb_images)

# 7. RESNET BASIC RESIDUAL BLOCK (identity shortcut)
heading('7. ResNet residual block')
def residual_block(x, filters):
    shortcut = x
    y = tf.keras.layers.Conv2D(filters, (3, 3), padding='same', use_bias=False)(x)
    y = tf.keras.layers.BatchNormalization()(y)
    y = tf.keras.layers.Activation('relu')(y)
    y = tf.keras.layers.Conv2D(filters, (3, 3), padding='same', use_bias=False)(y)
    y = tf.keras.layers.BatchNormalization()(y)
    y = tf.keras.layers.Add()([y, shortcut])
    return tf.keras.layers.Activation('relu')(y)
inputs = tf.keras.Input(shape=(32, 32, 64))
outputs = residual_block(inputs, 64)
resnet_block_model = tf.keras.Model(inputs, outputs)
print('Residual block output:', resnet_block_model.output.shape)
print('ResNet rule: output = F(x) + x (before final activation)')

# 8. PROJECTION SHORTCUT WHEN CHANNELS / SPATIAL SHAPES CHANGE
heading('8. Projection shortcut')
def projection_block(x, filters, stride=2):
    shortcut = tf.keras.layers.Conv2D(filters, (1, 1), strides=stride, padding='same')(x)
    y = tf.keras.layers.Conv2D(filters, (3, 3), strides=stride, padding='same', activation='relu')(x)
    y = tf.keras.layers.Conv2D(filters, (3, 3), padding='same')(y)
    return tf.keras.layers.Add()([y, shortcut])
x = tf.keras.Input(shape=(32, 32, 32))
projected = tf.keras.Model(x, projection_block(x, 64))
print('Projection output:', projected.output.shape)  # (None,16,16,64)
print('Bottleneck middle 3x3 weights, 256->256 vs 64->64:', 3 * 3 * 256 * 256, 3 * 3 * 64 * 64)
# PRETRAINED RESNET50 (requires internet first time):
# base = tf.keras.applications.ResNet50(include_top=False, weights='imagenet',
#                                      input_shape=(224,224,3), pooling='avg')
# base.trainable = False
# inputs = tf.keras.Input(shape=(224,224,3))
# x = tf.keras.applications.resnet.preprocess_input(inputs)
# x = base(x, training=False)
# outputs = tf.keras.layers.Dense(5, activation='softmax')(x)
# transfer_model = tf.keras.Model(inputs, outputs)

# 9. INCEPTION PARALLEL BRANCHES + CHANNEL CONCATENATION
heading('9. Inception module')
inputs = tf.keras.Input(shape=(28, 28, 192))
branch1 = tf.keras.layers.Conv2D(32, (1, 1), padding='same')(inputs)
branch2 = tf.keras.layers.Conv2D(48, (3, 3), padding='same')(inputs)
branch3 = tf.keras.layers.MaxPooling2D((3, 3), strides=1, padding='same')(inputs)
branch3 = tf.keras.layers.Conv2D(16, (1, 1), padding='same')(branch3)
merged = tf.keras.layers.Concatenate(axis=-1)([branch1, branch2, branch3])
inception = tf.keras.Model(inputs, merged)
print('Inception output:', inception.output.shape)  # 28x28x96
print('1x1 conv 192 -> 32 parameters:', (192 + 1) * 32)  # 6176
# PRETRAINED INCEPTIONV3 (requires internet first time):
# inception_v3 = tf.keras.applications.InceptionV3(include_top=False,
#     weights='imagenet', input_shape=(299,299,3), pooling='avg')
# x = tf.keras.applications.inception_v3.preprocess_input(images)

# 10. LEARNING RATE NUMERICAL AND EXPONENTIAL DECAY
heading('10. LR update and ExponentialDecay')
w, grad, lr = 4., 0.8, 0.1
print('Weight update:', w - lr * grad)  # 3.92
exp_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=0.01, decay_steps=1000, decay_rate=0.9, staircase=False)
print('ExponentialDecay at step 1000:', exp_schedule(1000).numpy())  # ~0.009
exp_optimizer = tf.keras.optimizers.SGD(learning_rate=exp_schedule)

# 11. PIECEWISE CONSTANT DECAY
heading('11. PiecewiseConstantDecay')
piecewise = tf.keras.optimizers.schedules.PiecewiseConstantDecay(
    boundaries=[1000, 2000], values=[0.01, 0.001, 0.0001])
for step in [0, 999, 1000, 2000, 2001]:
    print('Step', step, 'LR', float(piecewise(step).numpy()))
print('Note: Keras uses the preceding value AT each boundary (step 1000 -> 0.01).')

# 12. REDUCE LR ON PLATEAU
heading('12. ReduceLROnPlateau')
reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor='val_loss', factor=0.5, patience=3,
    mode='min', min_delta=0.0001, verbose=1)
print('Example: LR 0.01 ->', 0.01 * 0.5, 'after a reduction')

# 13. BATCH NORMALIZATION NUMERICAL
heading('13. BatchNorm numerical')
values = np.array([2., 4., 6.])
mean, variance = values.mean(), values.var()
normalized = (values - mean) / np.sqrt(variance + 1e-3)
gamma, beta = 2., 1.
print('Mean:', mean, 'Variance:', variance)
print('Normalized:', np.round(normalized, 3))
print('Scaled and shifted:', np.round(gamma * normalized + beta, 3))

# 14. BATCH NORM IN CNN + SCHEDULE IN SAME MODEL
heading('14. CNN with BN + schedule')
model = tf.keras.Sequential([
    tf.keras.Input(shape=(32, 32, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), padding='same', use_bias=False),
    tf.keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax'),
])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=exp_schedule),
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
print('Training BN: batch statistics; inference BN: stored moving statistics.')
# To train on your own arrays:
# history = model.fit(x_train, y_train, validation_data=(x_val, y_val),
#                     epochs=10, callbacks=[reduce_lr])
# IMPORTANT: ReduceLROnPlateau should use an optimizer with an ordinary numeric
# learning_rate, NOT the scheduled optimizer above. Choose ONE LR strategy:
# plateau_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
# model.compile(optimizer=plateau_optimizer,
#               loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train, y_train, validation_data=(x_val,y_val),
#           epochs=10, callbacks=[reduce_lr])
print('\nUNIT 2 FINISHED')
