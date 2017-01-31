import tensorflow as tf

# placeholderとして場所を確保し、後から値を書き込む
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
	print(sess.run([output], feed_dict={input1:[7.], input2:[2.]}))