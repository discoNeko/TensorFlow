## TensorFlow
TensorFlowのメモ  
  
環境  
--
・Windows10 Home (64bit)  
・Python 2.7.6  
・DockerToolBox  
・VirtualBox  
  
導入
--
[WindowsユーザーがTensorFlowをインストールしてみた(Docker版)](http://yaju3d.hatenablog.jp/entry/2016/04/07/011033)
  
Mac,Linux環境ではVirtualEnvからのインストールが公式推奨  
  
起動
--
[TensorFlowをMac & Dockerで使ってみたよ](http://qiita.com/yanosen_jp/items/41938cc361c9e7c83acc)  
Mac向けの記事だが、Dockerについて詳しい.  
[[TensorFlow][Docker] TensorFlowをWindowsで動かす](http://scriptlife.hacca.jp/contents/programming/2016/08/11/post-1698/)  
主にここを見ながら導入した.
  
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

Docker
--
### ホスト(Windows)とコンテナでファイルを共有する
つまり画像認識のチュートリアルimageNet/classify_image.pyでパンダ以外の画像を指定したいとき.  
  
[[TensorFlow][Docker] TensorFlowをWindowsで動かす](http://scriptlife.hacca.jp/contents/programming/2016/08/11/post-1698/)より  
>Windows側のファイルをそのまま使用したいときは、runのときに-vオプションを使います。
>>$ docker run -v /c/Users/(共有したいフォルダのパス):(TensorFlowのDockerでアクセスするときのパス) -it b.gcr.io/tensorflow/tensorflow:latest-devel
  
>例えば、「C:\Users\tmp」を「/root/share」に共有するときは以下のようにします。
>>$ docker run -v /c/Users/tmp:/root/share -it b.gcr.io/tensorflow/tensorflow:latest-devel
  
  
### Dockerコマンド
>docker ps -a  
  
作成したコンテナ一覧を表示.  
  
>docker rm $(docker ps -aq)  
  
作成したコンテナを全削除.  
  
入門解説
--
[TensorFlowとは？ データフローグラフを構築・実行してみよう](http://www.buildinsider.net/small/booktensorflow/0001)  
[TensorFlowのチュートリアルを通して、人工知能の原理について学習する](http://qiita.com/jintaka1989/items/3b70b5c5541620536fa2)  

  
NN構築(TensorFlow)
--
[TensorFlowチュートリアル - 畳み込みニューラルネットワーク（翻訳）](http://qiita.com/KojiOhki/items/e218f36840df10ae358d)  
  
NN構築(テキストのベクトル化)
--
[TensorFlowを使ってテキストをクラス分類してみた](http://www.slideshare.net/YuyaKato3/tensorflow-58795721)  
ある文字列を特徴化して, 入力用のベクトルに直す方法が使えそう？  
テキストのベクトル化はサポートベクトルマシン, ブースティングが他の手法と比べて高精度らしい[要出典]  
  
[畳み込みニューラルネットワークによるテキスト分類を TensorFlow で実装する](http://tkengo.github.io/blog/2016/03/14/text-classification-by-cnn/)  
比較的新しい記事(16/03). TensorFlowでの各層の実装についてソース付き解説.  
  
TensorFlowで遊ぶ
--
[Googleの機械学習フレームワーク「TensorFlow」でImageNetの学習データを使った画像認識を試してみた - TensorFlowのインストールから画像認識まで](http://qiita.com/nkjm/items/a2dada74d48b29f0e5f4)  
丁寧なImageNet導入・実行の解説. 手軽に画像分類で遊べるようになる. 取りあえず動かしてみたい人向け.  
[TensorFlowチュートリアル - 画像認識（翻訳）](http://qiita.com/KojiOhki/items/dab6922b6cd7b990c002)
ImageNet導入は公式訳の方が分かりやすい.  
  
imageNetのclassify_image.pyを実行する際に,ソースの入ったフォルダまで移動するところで,  
>cd ~/tensorflow/lib/python2.7/site-packages/tensorflow/models/image/imagenet/
  
とあるが, 実際には  
>cd ~/tensorflow/tensorflow/models/image/imagenet/
  
となる.  
フォルダの構造が変わったのか, 実行環境の違いなのかは不明.  
  
どこにも書かれていないが任意の画像を指定する場合は、ファイルをどこに置けばいい？  
絶対パスやURLで指定してもエラーが出るので, 相対パスで指定したいが, そもそもDockerコンテナのディレクトリはあるのか.  
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
