## TensorFlow
TensorFlowのメモ  
  
* [深層学習の用語解説まとめ](https://github.com/discoNeko/TensorFlow/blob/master/keyword.md)
* [TensorFlow導入（Win10 + Docker）まとめ](https://github.com/discoNeko/TensorFlow/blob/master/install.md)  
  
環境  
--
・Windows10 Home (64bit)  
・Python 2.7.6  
・DockerToolBox  
・VirtualBox  
  
入門解説
--
[TensorFlowとは？ データフローグラフを構築・実行してみよう](http://www.buildinsider.net/small/booktensorflow/0001)  
[TensorFlowのチュートリアルを通して、人工知能の原理について学習する](http://qiita.com/jintaka1989/items/3b70b5c5541620536fa2)  

  
実装
--
* [TensorFlowでアニメゆるゆりの制作会社を識別する](http://kivantium.hateblo.jp/entry/2015/11/18/233834)  
TensorFlow自体の簡単な解説+コード.
* [ニューラルネットワークでプロ野球選手の給与を査定してみる](http://qiita.com/sergeant-wizard/items/9bb45c0850aebca2bc07)  
入力データの取り込み方から出力までを具体例で解説.
* [TensorFlowのPythonコードの初歩を噛み砕いてみる](http://qiita.com/To_Murakami/items/5984a4891597b17fc40e)  
上の記事のソース解説.
* [畳み込みニューラルネットワークによるテキスト分類を TensorFlow で実装する](http://tkengo.github.io/blog/2016/03/14/text-classification-by-cnn/)  
比較的新しい記事(16/03). TensorFlowでの各層の実装についてソース付き解説.  
  

公式訳
--
[TensorFlowチュートリアル - 画像認識（翻訳）](http://qiita.com/KojiOhki/items/dab6922b6cd7b990c002)  
[TensorFlowチュートリアル - ML初心者のためのMNIST（翻訳）](http://qiita.com/KojiOhki/items/ff6ae04d6cf02f1b6edf)  
[TensorFlowチュートリアル - 熟練者のためのディープMNIST（翻訳）](http://qiita.com/KojiOhki/items/64a2ee54214b01a411c7) 


TensorFlowで遊ぶ
--
### MNIST
[TensorFlowで手書きの数字を認識するチュートリアルを試した](http://tech.mof-mof.co.jp/blog/tensorflow-tutorial.html)  
掲載ソースそのままで実行できる.  
  
### ImageNet
[Googleの機械学習フレームワーク「TensorFlow」でImageNetの学習データを使った画像認識を試してみた - TensorFlowのインストールから画像認識まで](http://qiita.com/nkjm/items/a2dada74d48b29f0e5f4)  
丁寧なImageNet導入・実行の解説. 手軽に画像分類で遊べるようになる. 取りあえず動かしてみたい人向け.  
  
ImageNetのclassify_image.pyを実行する際に,ソースの入ったフォルダまで移動するところで,  
>cd ~/tensorflow/lib/python2.7/site-packages/tensorflow/models/image/imagenet/
  
と説明しているサイトもあるが, 実際には  
>cd ~/tensorflow/tensorflow/models/image/imagenet/
  
となる(公式チュートリアルでは後者).  
フォルダの構造が変わったのか, 実行環境の違いなのかは不明.  
  
任意の画像を指定する場合は, ファイルをどこに置けばいい？  
絶対パスやURLで指定してもエラーが出るので相対パスで指定したいが, そもそもDockerコンテナのディレクトリとは.  
->上記「Docker/ホスト(Windows)とコンテナでファイルを共有する」を参照.  
  

ベイズ分類
--
>ナイーブベイズ分類器は、一言でいうと、分類問題ってベイズの定理を使えば解けるんじゃね？というものです。  
  
[単純ベイズ分類器がまったく単純じゃないので入門](https://hogehuga.com/post-563/)  
単純ベイズ分類について, 初歩的なところからの解説.  
  
[自然言語処理×ナイーブベイズ分類器で羽生さんと羽生くんを分類してみた](http://qiita.com/tmnck/items/175787ed94ae3eb62616)  
[ナイーブベイズを用いたテキスト分類](http://aidiary.hatenablog.com/entry/20100613/1276389337)  
ざっくりと用語解説 + python実装ソース.  
  

その他
--
[TensorFlowの勉強に必要なDocker導入サバイバルメモ](http://itsukara.hateblo.jp/entry/2016/05/31/024632)  
[[docker] コンテナを一括削除](http://qiita.com/ozdev/items/9e2090da22ffd6c7ad2a)  
  
[深層学習に基づくタンパク質と化合物の相互作用予測](https://www.ipsj.or.jp/award/9faeag0000004emc-att/4B-07.pdf)  
[DBN(Deep Belief Network)](http://qiita.com/t_Signull/items/f776aecb4909b7c5c116)  

