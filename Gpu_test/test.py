import tensorflow as tf

hello = tf.constant("Hello world!")

sess = tf.Session()

a = tf.constant(10)

b = tf.constant(32)
print(222)
print(sess.run(a + b))