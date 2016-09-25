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
[TensorFlowを触ってみたよ！](http://www.slideshare.net/satoshinoda792/tensorflow-56455816)  
TensorBoardのポートについて説明がある(スライド:6,7).  
[[TensorFlow][Docker] TensorFlowをWindowsで動かす](http://scriptlife.hacca.jp/contents/programming/2016/08/11/post-1698/)  
主にここを見た.
  
・Dockerをインストール(「導入」を参照).  
・Docker Quickstart Terminalのアイコンをクリックして起動.  
・Dockerコンソール上で,TensorFlowのdockerイメージを起動する.
>docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel 
  
・起動に成功すると以下のように表示される.  
`root@hogehoge:~#`
  
・`root@hogehoge:~# python` pythonを起動. 

   
・pythonコマンドでTensolflowの動作確認.  
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
  
例えば下記のように実行するとclassify_image.pyが実行できなくなるので注意.  
>docker run -v /c/Users/share:/tensorflow/tensorflow/models/image/imagenet/ -it b.gcr.io/tensorflow/tensorflow:latest-devel
  
これは「/tensorflow/tensorflow/models/image/imagenet/」が「/c/Users/share」として扱われ,   本来「/tensorflow/tensorflow/models/image/imagenet/」内にあるはずのclassify_image.pyが認識されなくなるため.  
  
適当な共有用のフォルダを指定しておけば問題ない.  
>docker run -v /c/Users/share:/tensorflow/tensorflow/models/image/imagenet/share/ -it b.gcr.io/tensorflow/tensorflow:latest-devel
  
--image_fileのあとに相対パスで画像を指定する.
>python classify_image.py --image_file ./share/1.jpg
  
### Dockerコマンド
よく使うものを記載.

|コマンド|内容|
|---|---|
|docker run -it b.gcr.io/tensorflow/tensorflow:latest-devel|コンテナを起動|
|docker run -p 8888:8888 -p 6006:6006 b.gcr.io/tensorflow/tensorflow|コンテナを起動（ポート指定）|
|docker ps -a|作成したコンテナ一覧を表示|
|docker rm $(docker ps -aq)|コンテナを全削除|
|docker start [Container ID or Name]|指定したコンテナを起動|
|docker stop $(docker ps -aq)|コンテナを全停止|
|docker stop [Container ID or Name]|指定したコンテナを停止|
