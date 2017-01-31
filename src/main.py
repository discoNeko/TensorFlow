import tensorflow as tf
import numpy as np
​
LOG_SIZE = 300 # スコアデータ 300 + labelデータ 15 + 分離したlabelデータ 15*3 = 360 列_csvファイル
HIDDEN_UNIT_SIZE1 = 180 # 隠れ層1のユニット数 180
HIDDEN_UNIT_SIZE2 = 90 # 隠れ層2のユニット数 90
HIDDEN_UNIT_SIZE3 = 45 # 隠れ層3のユニット数 45
TRAIN_DATA_SIZE = 70000 # 訓練データ 70000 + テストデータ 8000 = 78000 行_csvファイル
BATCH_SIZE = 100 # バッチサイズ 100
​
# 処理時間計測
import time
start = time.time()
​
# 入力データ形成
raw_input = np.loadtxt(open("input.csv"), delimiter=",")
​
# 列(縦)分割 (...299 300 || ここで分割 || 301 302...)
[log, label, wolf1, wolf2, wolf3]  = np.hsplit(raw_input, [300,315,330,345])
​
# 行(横)分割 (上から [TRAIN_DATA_SIZE] までを訓練データ、それ以下をテストデータとする)
[log_train, log_test] = np.vsplit(log, [TRAIN_DATA_SIZE])
[label_train, label_test] = np.vsplit(label, [TRAIN_DATA_SIZE])
[wolf1_train, wolf1_test] = np.vsplit(wolf1, [TRAIN_DATA_SIZE])
[wolf2_train, wolf2_test] = np.vsplit(wolf2, [TRAIN_DATA_SIZE])
[wolf3_train, wolf3_test] = np.vsplit(wolf3, [TRAIN_DATA_SIZE])
​
def inference(log_placeholder, dropout_rates):
# 隠れ層 1
  with tf.name_scope('hidden1') as scope:
    hidden1_weight = tf.Variable(tf.truncated_normal([LOG_SIZE, HIDDEN_UNIT_SIZE1], stddev=0.1), name="hidden1_weight")
    hidden1_bias = tf.Variable(tf.constant(0.1, shape=[HIDDEN_UNIT_SIZE1]), name="hidden1_bias")
    hidden1_output = tf.nn.relu(tf.matmul(log_placeholder, hidden1_weight) + hidden1_bias)
# 隠れ層 2
  with tf.name_scope('hidden2') as scope:
    hidden2_weight = tf.Variable(tf.truncated_normal([HIDDEN_UNIT_SIZE1, HIDDEN_UNIT_SIZE2], stddev=0.1), name="hidden2_weight")
    hidden2_bias = tf.Variable(tf.constant(0.1, shape=[HIDDEN_UNIT_SIZE2]), name="hidden2_bias")
    hidden2_output = tf.nn.relu(tf.matmul(hidden1_output, hidden2_weight) + hidden2_bias)
# 隠れ層 3
  with tf.name_scope('hidden3') as scope:
    hidden3_weight = tf.Variable(tf.truncated_normal([HIDDEN_UNIT_SIZE2, HIDDEN_UNIT_SIZE3], stddev=0.1), name="hidden3_weight")
    hidden3_bias = tf.Variable(tf.constant(0.1, shape=[HIDDEN_UNIT_SIZE3]), name="hidden3_bias")
    hidden3_output = tf.nn.relu(tf.matmul(hidden2_output, hidden3_weight) + hidden3_bias)  
# dropoutの設定
    output_drop = tf.nn.dropout(hidden3_output, dropout_rates)
# 出力層
  with tf.name_scope('output') as scope:
    output_weight = tf.Variable(tf.truncated_normal([HIDDEN_UNIT_SIZE3, 15], stddev=0.1), name="output_weight")
    output_bias = tf.Variable(tf.constant(0.1, shape=[1]), name="output_bias")
    output = tf.matmul(output_drop, output_weight) + output_bias
  return tf.nn.l2_normalize(output, 0)
​
def loss(output, label_placeholder, loss_label_placeholder):
  with tf.name_scope('loss') as scope:
    loss = tf.nn.l2_loss(output - tf.nn.l2_normalize(label_placeholder, 0))
    tf.scalar_summary(loss_label_placeholder, loss)
  return loss
​
def training(loss):
  with tf.name_scope('training') as scope:
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
  return train_step
​
def accuracy(log, w1, w2, w3):
  with tf.name_scope('accuracy') as scope:
    c1 = tf.equal(tf.argmax(log, 1), tf.argmax(w1, 1))
    c2 = tf.equal(tf.argmax(log, 1), tf.argmax(w2, 1))
    c3 = tf.equal(tf.argmax(log, 1), tf.argmax(w3, 1))
    correct_prediction = tf.logical_or(tf.logical_or(c1,c2),c3)
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    tf.scalar_summary("accuracy", accuracy)
  return accuracy
​
with tf.Graph().as_default():
#logを入れる仮のTensor
  log_placeholder = tf.placeholder("float", [None, LOG_SIZE], name="log_placeholder")
#labelを入れる仮のTensor
  label_placeholder = tf.placeholder("float", [None, 15], name="label_placeholder")
#wolf1を入れる仮のTensor
  wolf1_placeholder = tf.placeholder("float", [None, 15], name="wolf1_placeholder")
#wolf2を入れる仮のTensor
  wolf2_placeholder = tf.placeholder("float", [None, 15], name="wolf2_placeholder")
#wolf3を入れる仮のTensor
  wolf3_placeholder = tf.placeholder("float", [None, 15], name="wolf3_placeholder")
#lossを入れる仮のTensor
  loss_label_placeholder = tf.placeholder("string", name="loss_label_placeholder")
#dropout_rateを入れる仮のTensor
  dropout_rates = tf.placeholder("float")
​​
# inference()を呼び出してモデルを生成
  output = inference(log_placeholder, dropout_rates)
# loss()を呼び出して損失を計算
  loss = loss(output, label_placeholder, loss_label_placeholder)
# training()を呼び出して訓練
  training_op = training(loss)
#　精度計算
  acc = accuracy(output, wolf1_placeholder, wolf2_placeholder, wolf3_placeholder)
​
# TensorBoard表示用
  summary_op = tf.merge_all_summaries()
​
# 変数を初期化
  init = tf.initialize_all_variables()
​
  with tf.Session() as sess:
    summary_writer = tf.train.SummaryWriter('data', graph_def=sess.graph_def)
    sess.run(init)
​# 10000 step　実行する
    for step in range(10000):
      for i in range(TRAIN_DATA_SIZE/BATCH_SIZE):
        batch = BATCH_SIZE*i
        sess.run(training_op, feed_dict={
          log_placeholder: log_train[batch:batch+BATCH_SIZE],
          label_placeholder: label_train[batch:batch+BATCH_SIZE],
          loss_label_placeholder: "loss_train",
          dropout_rates: 0.5})
        
# 1 step ごとに訓練データとテストデータの精度を計算
      train_accuracy = sess.run(acc, feed_dict={
        log_placeholder: log_train,
        wolf1_placeholder: wolf1_train,
        wolf2_placeholder: wolf2_train,
        wolf3_placeholder: wolf3_train,
        dropout_rates: 1.0})
      print "step %d, training accuracy %g"%(step, train_accuracy)
        
      train_accuracy = sess.run(acc, feed_dict={
        log_placeholder: log_test,
        wolf1_placeholder: wolf1_test,
        wolf2_placeholder: wolf2_test,
        wolf3_placeholder: wolf3_test,
        dropout_rates: 1.0})
      print "step %d, test accuracy %g"%(step, train_accuracy)
"""
# 1 step終わるたびにTensorBoardに表示する値を追加する
      summary_str = sess.run(summary_op, feed_dict={
          log_placeholder: log_train,
          label_placeholder: label_train})
      summary_writer.add_summary(summary_str, step)
"""     