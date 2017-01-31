import tensorflow as tf

# 変数を初期化して0(スカラー値)
state = tf.Variable(0, name="counter")

# opを生成してstateに追加
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 変数はグラフを立ち上げた後にinitのopを実行することで初期化されなければならない
# 初期状態で、グラフにinitのOPを追加しなければならない
init_op = tf.initialize_all_variables()

# グラフを立ち上げてopsを実行する
with tf.Session() as sess:
	sess.run(init_op)
	# 0が出力される
	print(sess.run(state))
	for _ in range(3):
		sess.run(update)
		# ループで1,2,3が出力される
		print(sess.run(state))