# AWSOrgIAMCreate

AWS Organizationの親アカウント権限で、配下のAWSアカウントにログインするためのIAMユーザを作成します。

**利用方法**
1.  リポジトリをCloneないしファイルDLしてください。
2.  DLディレクトリに移動し、「docker build . -t 任意のイメージ名」を実行 してイメージをbuildしてください。
3.  「docker run 2のイメージ名 親アカウントでのアクセスキー 親アカウントでのシークレットキー 入りたいAWSアカウントID 作成するユーザのユーザ名 作成するユーザのパスワード」 を実行することでユーザが作成されます。

（実行例）  
C:\Users\68H3316\Desktop\test>DIR  
 ドライブ C のボリューム ラベルがありません。  
 ボリューム シリアル番号は 8C25-E6D2 です  
 C:\Users\68H3316\Desktop\test のディレクトリ  
2020/10/14  10:48    <DIR>          .
2020/10/14  10:48    <DIR>          ..  
2020/10/14  11:52             1,287 app.py  
2020/10/14  11:33               429 Dockerfile  
2020/10/14  10:24                 5 requirements.txt  
               3 個のファイル               1,721 バイト  
               2 個のディレクトリ  12,275,068,928 バイトの空き領域    
  
C:\Users\68H3316\Desktop\test>docker build . -t hoge  
C:\Users\68H3316\Desktop\test>docker run hoge AKIAZH2TUDVAJGR4DJZ4 pOsUj+IN4WCgQPF4GFtA7vvXpbRov+BC5v4WUZLU 414826627551 hogeuser P@ssw0rd      
※この認証情報はダミーです。  
