### TensorFlow
learn TensorFlow
### 導入
[WindowsユーザーがTensorFlowをインストールしてみた(Docker版)](http://yaju3d.hatenablog.jp/entry/2016/04/07/011033)
### 起動
[[TensorFlow][Docker] TensorFlowをWindowsで動かす](http://scriptlife.hacca.jp/contents/programming/2016/08/11/post-1698/)  
  
・Dockerをインストール.  
・Docker Quickstart Terminalのアイコンをクリックして起動.  
・Dockerコンソール上で,TensorFlowのdockerイメージを起動する.
>docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel 
  
・起動に成功すると以下のように表示される.
>root@hogehoge:~#  
  
・pythonを起動. 
>root@hogehoge:~# python
   
・pythonコマンドでTensolflowの動作確認 
・

### 入門解説
[TensorFlowとは？ データフローグラフを構築・実行してみよう](http://www.buildinsider.net/small/booktensorflow/0001)
[TensorFlowのチュートリアルを通して、人工知能の原理について学習する](http://qiita.com/jintaka1989/items/3b70b5c5541620536fa2)

### NN構築(TensorFlow)
[TensorFlowチュートリアル - 畳み込みニューラルネットワーク（翻訳）](http://qiita.com/KojiOhki/items/e218f36840df10ae358d)  

### NN構築(テキストのベクトル化)
[TensorFlowを使ってテキストをクラス分類してみた](http://www.slideshare.net/YuyaKato3/tensorflow-58795721)  
ある文字列を特徴化して, 入力用のベクトルに直す方法が使えそう？  
テキストのベクトル化はサポートベクトルマシン, ブースティングが他の手法と比べて高精度らしい[要出典]  


### TensorFlowで遊ぶ
[Googleの機械学習フレームワーク「TensorFlow」でImageNetの学習データを使った画像認識を試してみた - TensorFlowのインストールから画像認識まで](http://qiita.com/nkjm/items/a2dada74d48b29f0e5f4)  
丁寧なImageNet導入・実行の解説. 手軽に画像分類で遊べるようになる. 取りあえず動かしてみたい人向け.  

### ベイズ分類
>ナイーブベイズ分類器は、一言でいうと、分類問題ってベイズの定理を使えば解けるんじゃね？というものです。  
  
[単純ベイズ分類器がまったく単純じゃないので入門](https://hogehuga.com/post-563/)  
単純ベイズ分類について, 初歩的なところからの解説.  
  
[自然言語処理×ナイーブベイズ分類器で羽生さんと羽生くんを分類してみた](http://qiita.com/tmnck/items/175787ed94ae3eb62616)  
[ナイーブベイズを用いたテキスト分類](http://aidiary.hatenablog.com/entry/20100613/1276389337)  

### その他
[TensorFlowの勉強に必要なDocker導入サバイバルメモ](http://itsukara.hateblo.jp/entry/2016/05/31/024632)  
[[docker] コンテナを一括削除](http://qiita.com/ozdev/items/9e2090da22ffd6c7ad2a)  
  
[深層学習に基づくタンパク質と化合物の相互作用予測](https://www.ipsj.or.jp/award/9faeag0000004emc-att/4B-07.pdf)  
[DBN(Deep Belief Network)](http://qiita.com/t_Signull/items/f776aecb4909b7c5c116)  
