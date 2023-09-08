import tensorflow as tf
import pdb

# Check available GPUs
print("Available GPUs:", tf.config.experimental.list_physical_devices('GPU'))

# Specify GPU to use
physical_devices = tf.config.experimental.list_physical_devices('GPU')
# pdb.set_trace()

print(physical_devices)
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)



if len(physical_devices) > 0:
    # Select the first GPU
    tf.config.experimental.set_visible_devices(physical_devices[0], 'GPU')
    print(f"Using GPU: {physical_devices[0]}")
else:
    print("No GPU available.")    



print("________________________________________________________________________________")
print(tf.test.gpu_device_name())
print("________________________________________________________________________________")


(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Create TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((train_images, train_labels)).shuffle(60000).batch(64)
test_dataset = tf.data.Dataset.from_tensor_slices((test_images, test_labels)).batch(64)

# Define and build your deep learning model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile your model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train your model on GPU
model.fit(train_dataset, epochs=10, validation_data=test_dataset)