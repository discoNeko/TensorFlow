# 対話的なTensorFlowのセッションを入力
import tensorflow as tf
sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.0])

# 初期化用のopsのrunメソッドを利用してxを初期化する
x.initializer.run()
# xからaを減算するops
sub = tf.sub(x, a)
print(sub.eval())
sess.close()
