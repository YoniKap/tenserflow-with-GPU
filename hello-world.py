import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
result = hello.numpy() 
print(result.decode())  